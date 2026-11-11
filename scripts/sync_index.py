#!/usr/bin/env python3
"""由 curriculum.yaml 与各讲义的 frontmatter、批注生成全部索引文件。

生成或更新：

- ``CURRICULUM.md``：课程总目录；
- 每个模块 ``README.md`` 中 AUTO 标记之间的章节表；
- ``progress/knowledge-checklist.md``：各章学习状态与建设状态；
- ``progress/open-questions.md``：全部带 ``.anno-open`` 的疑问与勘误；
- ``progress/status.json``：供学习网站首页读取的汇总数据；
- 讲义 frontmatter 中镜像的 ``build_status`` 字段。

用法::

    python scripts/sync_index.py                       # 重新生成
    python scripts/sync_index.py --check               # 只检查，不一致时返回非零
    python scripts/sync_index.py --set-status M04.2 Practicing

生成结果只取决于仓库内容，不含时间戳，因此 ``--check`` 可以用于 CI。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM_FILE = ROOT / "curriculum.yaml"

LEARN_STATES = ("Not Started", "Reading", "Practicing", "Reviewed", "Mastered")
BUILD_STATES = ("Planned", "Draft", "Reviewed", "Verified")
PRIORITIES = ("P0", "P1", "P2", "P3", "Branch")

AUTO_START = "<!-- AUTO:chapters:start -->"
AUTO_END = "<!-- AUTO:chapters:end -->"
GENERATED = (
    "<!-- 本文件由 scripts/sync_index.py 生成，请勿手工编辑。"
    "修改 curriculum.yaml 或讲义 frontmatter 后运行 `make sync`。 -->"
)

ANNOTATION_LABELS = {
    "question": "疑问",
    "bug": "勘误",
    "note": "我的理解",
    "idea": "研究联想",
    "tutor": "解答",
}

_FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n(.*?\n)---[ \t]*\n", re.S)
_DIV_OPEN_RE = re.compile(r"^\s*:{3,}\s*\{([^}]*)\}\s*$")
_DIV_CLOSE_RE = re.compile(r"^\s*:{3,}\s*$")
_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_TITLE_RE = re.compile(r'title\s*=\s*"((?:[^"\\]|\\.)*)"')
_ANNO_CLASS_RE = re.compile(r"\.anno-([a-z]+)")


# --------------------------------------------------------------------------- #
# 数据读取
# --------------------------------------------------------------------------- #


@dataclass
class Annotation:
    """讲义源文件中的一条批注。"""

    file: str  # 相对仓库根目录的路径
    line: int  # 起始行号（从 1 开始）
    index: int  # 该文件内第几条批注；网页锚点为 anno-<index>
    kind: str  # question / bug / note / idea / tutor
    title: str
    is_open: bool
    excerpt: str

    @property
    def anchor(self) -> str:
        return f"anno-{self.index}"


@dataclass
class Chapter:
    id: str
    module_id: str
    title: str
    title_zh: str
    priority: str
    tags: list[str]
    prereqs: list[str]
    anchors: list[str]
    note: str  # 相对仓库根目录的讲义路径
    build_status: str
    scope: str
    note_exists: bool = False
    learn_status: str = "Not Started"
    evidence: list[str] = field(default_factory=list)
    next_review: str | None = None
    frontmatter: dict[str, Any] = field(default_factory=dict)


@dataclass
class Module:
    id: str
    dir: str
    title: str
    title_zh: str
    priority: str
    hours: str
    anchors: list[str]
    chapters: list[Chapter]

    @property
    def number(self) -> str:
        return self.id[1:]


def load_curriculum_raw() -> dict[str, Any]:
    return yaml.safe_load(CURRICULUM_FILE.read_text("utf-8"))


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """把文本拆成 (frontmatter 原文, 正文)。没有 frontmatter 时前者为 None。"""
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    return match.group(1), text[match.end() :]


def read_frontmatter(path: Path) -> dict[str, Any]:
    raw, _ = split_frontmatter(path.read_text("utf-8"))
    if raw is None:
        return {}
    data = yaml.safe_load(raw)
    return data if isinstance(data, dict) else {}


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list | tuple):
        return [str(item) for item in value]
    return [str(value)]


def load_modules() -> list[Module]:
    """读取 curriculum.yaml，并合并各讲义 frontmatter 中的学习状态。"""
    raw = load_curriculum_raw()
    modules: list[Module] = []
    for module_raw in raw.get("modules", []):
        chapters: list[Chapter] = []
        for chapter_raw in module_raw.get("chapters", []):
            note = f"{module_raw['dir']}/{chapter_raw['note']}"
            chapter = Chapter(
                id=chapter_raw["id"],
                module_id=module_raw["id"],
                title=chapter_raw["title"],
                title_zh=chapter_raw["title_zh"],
                priority=str(chapter_raw["priority"]),
                tags=_as_list(chapter_raw.get("tags")),
                prereqs=_as_list(chapter_raw.get("prereqs")),
                anchors=_as_list(chapter_raw.get("anchors")),
                note=note,
                build_status=chapter_raw.get("build_status", "Planned"),
                scope=str(chapter_raw.get("scope", "")).strip(),
            )
            note_path = ROOT / note
            if note_path.is_file():
                chapter.note_exists = True
                chapter.frontmatter = read_frontmatter(note_path)
                chapter.learn_status = str(chapter.frontmatter.get("learn_status") or "Not Started")
                chapter.evidence = _as_list(chapter.frontmatter.get("evidence"))
                next_review = chapter.frontmatter.get("next_review")
                chapter.next_review = str(next_review) if next_review else None
            chapters.append(chapter)
        modules.append(
            Module(
                id=module_raw["id"],
                dir=module_raw["dir"],
                title=module_raw["title"],
                title_zh=module_raw["title_zh"],
                priority=str(module_raw["priority"]),
                hours=str(module_raw.get("hours", "")),
                anchors=_as_list(module_raw.get("anchors")),
                chapters=chapters,
            )
        )
    return modules


def scan_annotations(path: Path) -> list[Annotation]:
    """扫描一个 .qmd 源文件中的全部 ``.anno-*`` 批注（跳过代码块里的示例）。"""
    annotations: list[Annotation] = []
    lines = path.read_text("utf-8").splitlines()
    rel = path.relative_to(ROOT).as_posix()
    fence: str | None = None
    for number, line in enumerate(lines, start=1):
        fence_match = _FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker[0] * 3
            elif marker.startswith(fence):
                fence = None
            continue
        if fence is not None:
            continue
        div_match = _DIV_OPEN_RE.match(line)
        if not div_match:
            continue
        attrs = div_match.group(1)
        classes = _ANNO_CLASS_RE.findall(attrs)
        kinds = [name for name in classes if name in ANNOTATION_LABELS]
        if not kinds:
            continue
        title_match = _TITLE_RE.search(attrs)
        title = title_match.group(1).replace('\\"', '"') if title_match else ""
        excerpt = ""
        for body_line in lines[number:]:
            if _DIV_CLOSE_RE.match(body_line):
                break
            if body_line.strip():
                excerpt = body_line.strip()
                break
        annotations.append(
            Annotation(
                file=rel,
                line=number,
                index=len(annotations) + 1,
                kind=kinds[0],
                title=title or ANNOTATION_LABELS[kinds[0]],
                is_open="open" in classes,
                excerpt=excerpt[:120],
            )
        )
    return annotations


def annotated_sources() -> list[Path]:
    """可能含有批注的源文件：仓库中全部 .qmd（模板与渲染产物除外）。"""
    skip = {".venv", "_site", "_freeze", ".quarto", "templates", "library", "node_modules"}
    result = []
    for path in sorted(ROOT.rglob("*.qmd")):
        parts = path.relative_to(ROOT).parts
        if any(part in skip or part.startswith(".") for part in parts[:-1]):
            continue
        result.append(path)
    return result


def open_annotations() -> list[Annotation]:
    found: list[Annotation] = []
    for path in annotated_sources():
        found.extend(
            a for a in scan_annotations(path) if a.is_open and a.kind in ("question", "bug")
        )
    return found


def load_last_test() -> dict[str, Any] | None:
    path = ROOT / "progress" / "test-results.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text("utf-8"))
    except json.JSONDecodeError:
        return None
    return {
        "timestamp": data.get("timestamp"),
        "target": data.get("target"),
        "args": data.get("args", []),
        "summary": data.get("summary", {}),
        "failed": [t["nodeid"] for t in data.get("tests", []) if t.get("outcome") == "failed"],
    }


# --------------------------------------------------------------------------- #
# 渲染
# --------------------------------------------------------------------------- #


def _rel(target: str, start: str) -> str:
    """从目录 ``start``（相对仓库根）指向 ``target``（相对仓库根）的相对链接。"""
    return Path(os.path.relpath(ROOT / target, ROOT / start)).as_posix()


def _priority_cell(chapter: Chapter) -> str:
    return " · ".join([chapter.priority, *chapter.tags])


def _dash(items: list[str]) -> str:
    return ", ".join(items) if items else "—"


def _chapter_link(chapter: Chapter, start: str) -> str:
    if chapter.note_exists:
        return f"[{chapter.title_zh}]({_rel(chapter.note, start)})"
    return chapter.title_zh


def _chapter_table(module: Module, start: str) -> list[str]:
    lines = [
        "| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |",
        "|---|---|---|---|---|---|---|",
    ]
    for chapter in module.chapters:
        lines.append(
            f"| {chapter.id} | {_chapter_link(chapter, start)}<br>{chapter.title} "
            f"| {_priority_cell(chapter)} | {_dash(chapter.prereqs)} | {_dash(chapter.anchors)} "
            f"| {chapter.build_status} | {chapter.learn_status} |"
        )
    return lines


def render_curriculum(modules: list[Module]) -> str:
    total = sum(len(m.chapters) for m in modules)
    built = sum(c.build_status != "Planned" for m in modules for c in m.chapters)
    lines = [
        "# 课程总目录",
        "",
        GENERATED,
        "",
        f"共 {len(modules)} 个模块、{total} 章，其中 {built} 章已建设（建设状态为 Draft 及以上）。"
        "只有已建设的章节带讲义链接。",
        "",
        "优先级：`P0` 核心必修，`P1` 主线进阶，`P2` 拓展，`P3` 长期专题，"
        "`Branch` 分支内容；`FT` 表示诊断通过即可跳过正文、只做练习验证。"
        "两种状态的含义见 [学习指南](docs/learning-guide.md)。",
        "",
    ]
    for module in modules:
        lines += [
            f"## {module.id} {module.title_zh}（{module.title}）",
            "",
            f"模块优先级 `{module.priority}` · 估算学时 {module.hours} · "
            f"锚点 {_dash(module.anchors)} · [模块说明]({module.dir}/README.md)",
            "",
            *_chapter_table(module, "."),
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def render_module_block(module: Module) -> str:
    lines = [
        AUTO_START,
        "<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->",
        "",
        *_chapter_table(module, module.dir),
        "",
        "**各章范围**",
        "",
    ]
    lines += [f"- **{c.id} {c.title_zh}**：{c.scope}" for c in module.chapters]
    lines += ["", AUTO_END]
    return "\n".join(lines)


def render_checklist(modules: list[Module]) -> str:
    chapters = [c for m in modules for c in m.chapters]
    counts = {state: sum(c.learn_status == state for c in chapters) for state in LEARN_STATES}
    built = sum(c.build_status != "Planned" for c in chapters)
    lines = [
        "# 知识清单",
        "",
        GENERATED,
        "",
        f"共 {len(chapters)} 章，已建设 {built} 章。学习状态："
        + "、".join(f"{state} {counts[state]}" for state in LEARN_STATES)
        + "。",
        "",
        "勾选表示该章已达到 `Mastered`。学习状态记录在各讲义的 frontmatter 中，"
        "用 `make status ID=M04.2 S=Practicing` 修改。",
        "",
    ]
    for module in modules:
        lines += [f"## {module.id} {module.title_zh}", ""]
        for chapter in module.chapters:
            box = "x" if chapter.learn_status == "Mastered" else " "
            labels = " ".join(f"`{label}`" for label in [chapter.priority, *chapter.tags])
            lines.append(
                f"- [{box}] **{chapter.id}** {_chapter_link(chapter, 'progress')} {labels} · "
                f"建设：{chapter.build_status} · 学习：{chapter.learn_status}"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_open_questions(modules: list[Module], annotations: list[Annotation]) -> str:
    by_note = {c.note: c for m in modules for c in m.chapters}
    lines = ["# 未解决的疑问与勘误", "", GENERATED, ""]
    if not annotations:
        lines += ["目前没有未解决的疑问或勘误。", ""]
        return "\n".join(lines)
    lines += [
        f"共 {len(annotations)} 条。处理方式见 [学习指南](../docs/learning-guide.md) "
        "的批注协议一节；"
        "确认已解决后，把源文件中该批注的 `.anno-open` 改为 `.anno-resolved`。",
        "",
    ]
    current = None
    for annotation in annotations:
        if annotation.file != current:
            current = annotation.file
            chapter = by_note.get(annotation.file)
            heading = f"{chapter.id} {chapter.title_zh}" if chapter else annotation.file
            lines += [f"## {heading}", ""]
        link = f"{_rel(annotation.file, 'progress')}#{annotation.anchor}"
        excerpt = f"：{annotation.excerpt}" if annotation.excerpt else ""
        lines.append(
            f"- **{ANNOTATION_LABELS[annotation.kind]}** [{annotation.title}]({link})"
            f"（第 {annotation.line} 行）{excerpt}"
        )
    lines.append("")
    return "\n".join(lines)


def render_status(modules: list[Module], annotations: list[Annotation]) -> str:
    by_note = {c.note: c for m in modules for c in m.chapters}
    chapters = [c for m in modules for c in m.chapters]
    payload = {
        "totals": {
            "modules": len(modules),
            "chapters": len(chapters),
            "built": sum(c.build_status != "Planned" for c in chapters),
            "learn": {s: sum(c.learn_status == s for c in chapters) for s in LEARN_STATES},
            "build": {s: sum(c.build_status == s for c in chapters) for s in BUILD_STATES},
        },
        "modules": [
            {
                "id": m.id,
                "dir": m.dir,
                "title": m.title,
                "title_zh": m.title_zh,
                "priority": m.priority,
                "hours": m.hours,
                "chapters": len(m.chapters),
                "built": sum(c.build_status != "Planned" for c in m.chapters),
                "learn": {s: sum(c.learn_status == s for c in m.chapters) for s in LEARN_STATES},
            }
            for m in modules
        ],
        "chapters": [
            {
                "id": c.id,
                "module": c.module_id,
                "title": c.title,
                "title_zh": c.title_zh,
                "priority": c.priority,
                "tags": c.tags,
                "prereqs": c.prereqs,
                "anchors": c.anchors,
                "note": c.note,
                "note_exists": c.note_exists,
                "build_status": c.build_status,
                "learn_status": c.learn_status,
                "evidence_count": len(c.evidence),
                "next_review": c.next_review,
            }
            for c in chapters
        ],
        "open_annotations": [
            {
                "chapter": by_note[a.file].id if a.file in by_note else None,
                "file": a.file,
                "line": a.line,
                "anchor": a.anchor,
                "kind": a.kind,
                "title": a.title,
                "excerpt": a.excerpt,
            }
            for a in annotations
        ],
        "last_test": load_last_test(),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def update_module_readme(text: str, module: Module) -> str | None:
    """替换模块 README 中 AUTO 标记之间的内容；找不到标记时返回 None。"""
    start = text.find(AUTO_START)
    end = text.find(AUTO_END)
    if start == -1 or end == -1 or end < start:
        return None
    return text[:start] + render_module_block(module) + text[end + len(AUTO_END) :]


def set_frontmatter_field(text: str, key: str, value: str) -> str | None:
    """只改 frontmatter 中 ``key:`` 这一行的值，保留行尾注释与其余格式。"""
    raw, body = split_frontmatter(text)
    if raw is None:
        return None
    pattern = re.compile(rf"^({re.escape(key)}:[ \t]*)([^#\n]*?)([ \t]*(?:#.*)?)$", re.M)
    if not pattern.search(raw):
        return None
    new_raw = pattern.sub(lambda m: f"{m.group(1)}{value}{m.group(3)}", raw, count=1)
    return f"---\n{new_raw}---\n{body}"


# --------------------------------------------------------------------------- #
# 主流程
# --------------------------------------------------------------------------- #


def build_outputs(modules: list[Module]) -> tuple[dict[Path, str], list[str]]:
    """计算全部应生成的文件内容。返回 ({路径: 内容}, 问题列表)。"""
    outputs: dict[Path, str] = {}
    problems: list[str] = []

    # 讲义 frontmatter 中镜像的 build_status（以 curriculum.yaml 为准）
    for chapter in (c for m in modules for c in m.chapters if c.note_exists):
        path = ROOT / chapter.note
        text = path.read_text("utf-8")
        updated = set_frontmatter_field(text, "build_status", chapter.build_status)
        if updated is None:
            problems.append(f"{chapter.note}: frontmatter 中缺少 build_status 字段")
        elif updated != text:
            outputs[path] = updated

    annotations = open_annotations()
    outputs[ROOT / "CURRICULUM.md"] = render_curriculum(modules)
    outputs[ROOT / "progress" / "knowledge-checklist.md"] = render_checklist(modules)
    outputs[ROOT / "progress" / "open-questions.md"] = render_open_questions(modules, annotations)
    outputs[ROOT / "progress" / "status.json"] = render_status(modules, annotations)

    for module in modules:
        readme = ROOT / module.dir / "README.md"
        if not readme.is_file():
            problems.append(f"{module.dir}/README.md 不存在")
            continue
        updated = update_module_readme(readme.read_text("utf-8"), module)
        if updated is None:
            problems.append(f"{module.dir}/README.md 中缺少 AUTO:chapters 标记")
        else:
            outputs[readme] = updated
    return outputs, problems


def set_learn_status(chapter_id: str, status: str) -> int:
    if status not in LEARN_STATES:
        print(f"未知的学习状态 {status!r}，可选：{', '.join(LEARN_STATES)}", file=sys.stderr)
        return 2
    chapters = {c.id: c for m in load_modules() for c in m.chapters}
    chapter = chapters.get(chapter_id)
    if chapter is None:
        print(f"curriculum.yaml 中没有章节 {chapter_id}", file=sys.stderr)
        return 2
    if not chapter.note_exists:
        print(f"{chapter_id} 尚未建设讲义（{chapter.note}），无法修改学习状态", file=sys.stderr)
        return 2
    path = ROOT / chapter.note
    updated = set_frontmatter_field(path.read_text("utf-8"), "learn_status", status)
    if updated is None:
        print(f"{chapter.note}: frontmatter 中缺少 learn_status 字段", file=sys.stderr)
        return 2
    path.write_text(updated, "utf-8")
    print(f"{chapter_id} 学习状态：{chapter.learn_status} → {status}")
    if status in ("Reviewed", "Mastered") and not chapter.evidence:
        print(f"提示：请在 {chapter.note} 的 evidence 字段记录掌握证据。")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="只检查生成结果是否与现有文件一致")
    parser.add_argument(
        "--set-status",
        nargs=2,
        metavar=("ID", "STATUS"),
        help="修改某章的学习状态（写入讲义 frontmatter）后再同步",
    )
    parser.add_argument(
        "--touch-dashboard",
        action="store_true",
        help="同步后更新 index.qmd 的修改时间，让正在运行的 quarto preview 重新渲染首页",
    )
    args = parser.parse_args(argv)

    if args.set_status:
        code = set_learn_status(*args.set_status)
        if code:
            return code

    outputs, problems = build_outputs(load_modules())
    for problem in problems:
        print(f"错误：{problem}", file=sys.stderr)

    stale = [p for p, text in outputs.items() if not p.is_file() or p.read_text("utf-8") != text]
    if args.check:
        for path in stale:
            print(f"过期：{path.relative_to(ROOT)}（运行 make sync 重新生成）", file=sys.stderr)
        if stale or problems:
            return 1
        print(f"索引一致：检查了 {len(outputs)} 个生成文件")
        return 0

    for path in stale:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(outputs[path], "utf-8")
        print(f"已更新 {path.relative_to(ROOT)}")
    if not stale:
        print("索引已是最新")
    if args.touch_dashboard and (ROOT / "index.qmd").is_file():
        os.utime(ROOT / "index.qmd")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
