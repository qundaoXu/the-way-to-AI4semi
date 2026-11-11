--[[
semiai.lua —— 学习网站的 Pandoc/Quarto 过滤器（PROJECT_BLUEPRINT.md 第 6.4、6.5、6.7 节）

1. 批注：给每个带 .anno-* 类名的 callout 套一层 <div class="anno anno-xxx" id="anno-N">。
   N 是该批注在源文件中的序号，与 scripts/sync_index.py 的编号规则一致，
   progress/open-questions.md 和首页据此链接到原位置。
2. 标题与页眉：没有 frontmatter 的 .md 以第一个一级标题为页面标题；从 frontmatter 读取章节 ID、优先级、先修、两种状态，显示在标题下方。
3. “在 VS Code 中编辑”按钮，以及把指向 .py 等源码文件的相对链接改写为 vscode:// 链接。
   只在本地渲染时生效。
4. 发布构建（quarto render --profile publish）：剥离全部批注，不注入任何本机路径。
]]

local function is_publish()
  local profile = os.getenv("QUARTO_PROFILE") or ""
  for name in profile:gmatch("[^,%s]+") do
    if name == "publish" then return true end
  end
  return false
end

local PUBLISH = is_publish()
local anno_count = 0

local function escape_html(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

local function encode_path(path)
  return (path:gsub("[^%w%-%._~/:]", function(c)
    return string.format("%%%02X", string.byte(c))
  end))
end

-- 折叠路径中的 "." 与 ".."
local function collapse(path)
  local parts = {}
  for part in path:gmatch("[^/]+") do
    if part == ".." then
      if #parts > 0 then table.remove(parts) end
    elseif part ~= "." then
      table.insert(parts, part)
    end
  end
  return "/" .. table.concat(parts, "/")
end

local function input_file()
  local file = quarto.doc.input_file
  if file:sub(1, 1) ~= "/" and quarto.project.directory then
    file = quarto.project.directory .. "/" .. file
  end
  return collapse(file)
end

local function vscode_url(abs_path)
  return "vscode://file" .. encode_path(abs_path)
end

-- ------------------------------------------------------------------ 批注

local function anno_classes(el)
  local found = {}
  for _, class in ipairs(el.classes) do
    if class:match("^anno%-") then table.insert(found, class) end
  end
  return found
end

local function wrap_annotation(el)
  local classes = anno_classes(el)
  if #classes == 0 then return nil end
  if PUBLISH then return {} end
  anno_count = anno_count + 1
  table.insert(classes, 1, "anno")
  return pandoc.Div({ el }, pandoc.Attr("anno-" .. anno_count, classes))
end

-- ------------------------------------------------------------------ 源码链接

local SOURCE_EXT = { py = true, yaml = true, yml = true, toml = true, json = true, lua = true, scss = true, sh = true }

local function rewrite_source_link(el)
  if PUBLISH then return nil end
  local target = el.target
  if target:match("^%a[%w+.-]*:") or target:sub(1, 1) == "#" then return nil end
  local path = target:gsub("[#?].*$", "")
  local ext = path:match("%.([%w]+)$")
  local is_makefile = path:match("Makefile$") ~= nil
  if not (is_makefile or (ext and SOURCE_EXT[ext:lower()])) then return nil end
  local base
  if path:sub(1, 1) == "/" then
    base = quarto.project.directory .. path
  else
    base = input_file():gsub("[^/]+$", "") .. path
  end
  el.target = vscode_url(collapse(base))
  table.insert(el.classes, "semiai-source-link")
  el.attributes["title"] = "在 VS Code 中打开"
  return el
end

-- ------------------------------------------------------------------ 页眉

local function read_status()
  if not quarto.project.directory then return nil end
  local handle = io.open(quarto.project.directory .. "/progress/status.json", "r")
  if not handle then return nil end
  local text = handle:read("a")
  handle:close()
  local ok, data = pcall(quarto.json.decode, text)
  if ok then return data end
  return nil
end

local function meta_string(meta, key)
  local value = meta[key]
  if value == nil then return nil end
  local text = pandoc.utils.stringify(value)
  if text == "" then return nil end
  return text
end

local function meta_list(meta, key)
  local value = meta[key]
  local items = {}
  if value == nil then return items end
  if pandoc.utils.type(value) == "List" then
    for _, item in ipairs(value) do table.insert(items, pandoc.utils.stringify(item)) end
  else
    local text = pandoc.utils.stringify(value)
    if text ~= "" then table.insert(items, text) end
  end
  return items
end

local function slug(text)
  return (text:lower():gsub("[^%w]+", "-"))
end

local function page_bar(meta)
  local parts = {}
  local chapter_id = meta_string(meta, "id")

  if chapter_id then
    local offset = quarto.project.offset or "."
    local notes = {}
    local status = read_status()
    if status and status.chapters then
      for _, chapter in ipairs(status.chapters) do
        if chapter.note_exists then notes[chapter.id] = chapter.note end
      end
    end

    table.insert(parts, '<span class="semiai-chip semiai-chip-id">' .. escape_html(chapter_id) .. "</span>")
    local priority = meta_string(meta, "priority")
    if priority then
      table.insert(parts, '<span class="semiai-chip semiai-priority-' .. slug(priority) .. '">' .. escape_html(priority) .. "</span>")
    end
    for _, tag in ipairs(meta_list(meta, "tags")) do
      table.insert(parts, '<span class="semiai-chip">' .. escape_html(tag) .. "</span>")
    end

    local prereqs = {}
    for _, id in ipairs(meta_list(meta, "prereqs")) do
      if notes[id] then
        local href = offset .. "/" .. notes[id]:gsub("%.qmd$", ".html")
        table.insert(prereqs, '<a href="' .. escape_html(href) .. '">' .. escape_html(id) .. "</a>")
      else
        table.insert(prereqs, '<span title="尚未建设">' .. escape_html(id) .. "</span>")
      end
    end
    if #prereqs > 0 then
      table.insert(parts, '<span class="semiai-field"><span class="semiai-label">先修</span>' .. table.concat(prereqs, "、") .. "</span>")
    end

    local learn = meta_string(meta, "learn_status")
    if learn and not PUBLISH then
      table.insert(parts, '<span class="semiai-field"><span class="semiai-label">学习</span><span class="semiai-state semiai-learn-' .. slug(learn) .. '">' .. escape_html(learn) .. "</span></span>")
    end
    local build = meta_string(meta, "build_status")
    if build then
      table.insert(parts, '<span class="semiai-field"><span class="semiai-label">建设</span><span class="semiai-state semiai-build-' .. slug(build) .. '">' .. escape_html(build) .. "</span></span>")
    end
  end

  if not PUBLISH then
    table.insert(parts, '<a class="semiai-edit" href="' .. vscode_url(input_file()) .. '" title="在 VS Code 中打开本页源文件">✎ 在 VS Code 中编辑</a>')
  end

  if #parts == 0 then return nil end
  local class = chapter_id and "semiai-pagebar" or "semiai-pagebar semiai-pagebar-plain"
  return pandoc.RawBlock("html", '<div class="' .. class .. '">' .. table.concat(parts, " ") .. "</div>")
end

-- ------------------------------------------------------------------ 入口

function Pandoc(doc)
  if not quarto.doc.is_format("html") then return nil end
  anno_count = 0
  -- .md 文件没有 frontmatter 时，用第一个一级标题作为页面标题
  if doc.meta.title == nil and #doc.blocks > 0 then
    local first = doc.blocks[1]
    if first.t == "Header" and first.level == 1 then
      doc.meta.title = pandoc.MetaInlines(first.content)
      doc.meta.pagetitle = pandoc.utils.stringify(first.content)
      table.remove(doc.blocks, 1)
    end
  end
  doc = doc:walk({ Div = wrap_annotation, Link = rewrite_source_link })
  local bar = page_bar(doc.meta)
  if bar then table.insert(doc.blocks, 1, bar) end
  return doc
end
