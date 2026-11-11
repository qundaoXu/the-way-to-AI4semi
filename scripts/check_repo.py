#!/usr/bin/env python3
"""仓库一致性检查（PROJECT_BLUEPRINT.md 第 11.2 节）。

错误（返回非零）：

- 模块或章节 ID 重复、格式不对，章节 ID 与所属模块不匹配；
- 优先级、建设状态、学习状态取值非法；
- 先修关系引用了不存在的章节，或存在环；
- 引用了未定义的研究锚点；
- ``Draft`` 及以上章节缺少讲义，或讲义 frontmatter 的 ``id`` 与 curriculum.yaml 不一致；
- ``Draft`` 及以上章节缺少实例 notebook（``notebooks/<讲义同名>.ipynb``），notebook 中
  没有出现该章 ID，存在未执行的代码单元，或输出中有报错；
- Markdown / Quarto 文件及 notebook 的 Markdown 单元中，仓库内相对链接指向不存在的文件。

警告（不影响返回值）：

- ``Reviewed`` 或 ``Mastered`` 章节缺少 ``evidence``；
- 讲义 frontmatter 中镜像的字段与 curriculum.yaml 不一致；
- 讲义文件已存在但建设状态仍是 ``Planned``。
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sync_index import (  # noqa: E402
    BUILD_STATES,
    LEARN_STATES,
    PRIORITIES,
    ROOT,
    Module,
    load_curriculum_raw,
    load_modules,
)

_MODULE_ID_RE = re.compile(r"^M\d{2}$")
_CHAPTER_ID_RE = re.compile(r"^M\d{2}\.\d{1,2}$")
_LINK_RE = re.compile(r"(?<!\!)\[[^\]\n]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_IMAGE_RE = re.compile(r"!\[[^\]\n]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
_EXTERNAL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

# 不检查链接的文件：模板里是占位符，蓝图里是示例。
_LINK_SKIP = ("templates/", "PROJECT_BLUEPRINT.md")


def check_structure(modules: list[Module], anchors: set[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    seen_modules: set[str] = set()
    seen_chapters: set[str] = set()
    seen_notes: set[str] = set()
    all_ids = {c.id for m in modules for c in m.chapters}

    for module in modules:
        if not _MODULE_ID_RE.match(module.id):
            errors.append(f"模块 ID 格式错误：{module.id}")
        if module.id in seen_modules:
            errors.append(f"模块 ID 重复：{module.id}")
        seen_modules.add(module.id)
        if not (ROOT / module.dir).is_dir():
            errors.append(f"{module.id}: 目录不存在 {module.dir}")
        if not Path(module.dir).name.startswith(module.number + "-"):
            errors.append(f"{module.id}: 目录名 {module.dir} 的编号与模块 ID 不一致")
        for anchor in module.anchors:
            if anchor not in anchors:
                errors.append(f"{module.id}: 未定义的锚点 {anchor}")

        for chapter in module.chapters:
            cid = chapter.id
            if not _CHAPTER_ID_RE.match(cid):
                errors.append(f"章节 ID 格式错误：{cid}")
            if not cid.startswith(module.id + "."):
                errors.append(f"{cid}: 章节 ID 与所属模块 {module.id} 不匹配")
            if cid in seen_chapters:
                errors.append(f"章节 ID 重复：{cid}")
            seen_chapters.add(cid)
            if chapter.note in seen_notes:
                errors.append(f"{cid}: 讲义路径与其他章节重复 {chapter.note}")
            seen_notes.add(chapter.note)
            if chapter.priority not in PRIORITIES:
                errors.append(f"{cid}: 非法优先级 {chapter.priority}")
            if chapter.build_status not in BUILD_STATES:
                errors.append(f"{cid}: 非法建设状态 {chapter.build_status}")
            for prereq in chapter.prereqs:
                if prereq not in all_ids:
                    errors.append(f"{cid}: 先修章节不存在 {prereq}")
                if prereq == cid:
                    errors.append(f"{cid}: 先修关系指向自身")
            for anchor in chapter.anchors:
                if anchor not in anchors:
                    errors.append(f"{cid}: 未定义的锚点 {anchor}")

            built = chapter.build_status != "Planned"
            if built and not chapter.note_exists:
                errors.append(
                    f"{cid}: 建设状态为 {chapter.build_status}，但讲义不存在 {chapter.note}"
                )
            if chapter.note_exists:
                front = chapter.frontmatter
                if not built:
                    warnings.append(f"{cid}: 讲义已存在，但建设状态仍是 Planned")
                if front.get("id") != cid:
                    errors.append(
                        f"{cid}: 讲义 frontmatter 的 id 为 {front.get('id')!r}，"
                        "与 curriculum.yaml 不一致"
                    )
                if chapter.learn_status not in LEARN_STATES:
                    errors.append(f"{cid}: 非法学习状态 {chapter.learn_status!r}")
                mirrored = {
                    "module": module.id,
                    "priority": chapter.priority,
                    "prereqs": chapter.prereqs,
                    "anchors": chapter.anchors,
                    "tags": chapter.tags,
                    "build_status": chapter.build_status,
                }
                for key, expected in mirrored.items():
                    actual = front.get(key)
                    if isinstance(expected, list):
                        actual = [str(item) for item in (actual or [])]
                    if actual != expected:
                        warnings.append(
                            f"{cid}: frontmatter 的 {key} 为 {actual!r}，"
                            f"curriculum.yaml 中为 {expected!r}"
                        )
                if chapter.learn_status in ("Reviewed", "Mastered") and not chapter.evidence:
                    warnings.append(f"{cid}: 学习状态为 {chapter.learn_status}，但 evidence 为空")
            if built:
                errors.extend(_check_notebook(cid, chapter.notebook))

    errors.extend(_find_cycles(modules))
    return errors, warnings


def _load_notebook(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text("utf-8"))
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) and isinstance(data.get("cells"), list) else None


def _cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else str(source)


def _check_notebook(chapter_id: str, rel_path: str) -> list[str]:
    """实例 notebook 必须存在、提到章节 ID、全部代码单元已执行且没有报错输出。"""
    path = ROOT / rel_path
    if not path.is_file():
        return [f"{chapter_id}: 已建设，但缺少实例 notebook {rel_path}"]
    nb = _load_notebook(path)
    if nb is None:
        return [f"{chapter_id}: {rel_path} 不是有效的 notebook"]
    errors: list[str] = []
    if not any(chapter_id in _cell_source(c) for c in nb["cells"]):
        errors.append(f"{chapter_id}: {rel_path} 中没有出现章节 ID")
    for number, cell in enumerate(nb["cells"], start=1):
        if cell.get("cell_type") != "code" or not _cell_source(cell).strip():
            continue
        if cell.get("execution_count") is None:
            errors.append(f"{chapter_id}: {rel_path} 第 {number} 个单元未执行（运行 make nb）")
        if any(out.get("output_type") == "error" for out in cell.get("outputs", [])):
            errors.append(f"{chapter_id}: {rel_path} 第 {number} 个单元的输出中有报错")
    return errors


def _find_cycles(modules: list[Module]) -> list[str]:
    graph = {c.id: [p for p in c.prereqs if p != c.id] for m in modules for c in m.chapters}
    state: dict[str, int] = {}  # 1 = 访问中，2 = 已完成
    errors: list[str] = []

    def visit(node: str, trail: list[str]) -> None:
        if state.get(node) == 2 or node not in graph:
            return
        if state.get(node) == 1:
            cycle = trail[trail.index(node) :] + [node]
            errors.append("先修关系存在环：" + " → ".join(cycle))
            return
        state[node] = 1
        for nxt in graph[node]:
            visit(nxt, trail + [node])
        state[node] = 2

    for node in graph:
        visit(node, [])
    return errors


def _tracked_documents() -> list[Path]:
    """仓库中的 .md / .qmd 文件（已跟踪或未被忽略的未跟踪文件）。"""
    try:
        out = subprocess.run(
            ["git", "ls-files", "-co", "--exclude-standard", "*.md", "*.qmd"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        paths = [ROOT / line for line in out.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        skip = {".venv", "_site", "_freeze", ".quarto", "library", ".git"}
        paths = [
            p
            for pattern in ("*.md", "*.qmd")
            for p in ROOT.rglob(pattern)
            if not skip.intersection(p.relative_to(ROOT).parts)
        ]
    return sorted(p for p in paths if p.is_file())


def _notebooks() -> list[Path]:
    return sorted(p for p in ROOT.glob("modules/*/notebooks/*.ipynb") if p.is_file())


def _broken_links(path: Path, text: str, label: str) -> list[str]:
    errors: list[str] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), start=1):
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
        stripped = _INLINE_CODE_RE.sub("", line)
        for target in _LINK_RE.findall(stripped) + _IMAGE_RE.findall(stripped):
            if _EXTERNAL_RE.match(target) or target.startswith("#"):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                continue
            resolved = ROOT / clean.lstrip("/") if clean.startswith("/") else path.parent / clean
            if not resolved.exists():
                errors.append(f"{label}:{number}: 链接目标不存在 {target}")
    return errors


def check_links() -> list[str]:
    errors: list[str] = []
    for path in _tracked_documents():
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(_LINK_SKIP):
            continue
        errors += _broken_links(path, path.read_text("utf-8"), rel)
    for path in _notebooks():
        rel = path.relative_to(ROOT).as_posix()
        nb = _load_notebook(path)
        if nb is None:
            continue
        for number, cell in enumerate(nb["cells"], start=1):
            if cell.get("cell_type") == "markdown":
                errors += _broken_links(path, _cell_source(cell), f"{rel} 单元 {number} 行")
    return errors


def main() -> int:
    raw = load_curriculum_raw()
    anchors = set((raw.get("anchors") or {}).keys())
    modules = load_modules()

    errors, warnings = check_structure(modules, anchors)
    errors += check_links()

    for warning in warnings:
        print(f"警告：{warning}")
    for error in errors:
        print(f"错误：{error}", file=sys.stderr)

    chapters = sum(len(m.chapters) for m in modules)
    if errors:
        print(f"check_repo：{len(errors)} 个错误，{len(warnings)} 个警告", file=sys.stderr)
        return 1
    print(f"check_repo 通过：{len(modules)} 个模块、{chapters} 章，{len(warnings)} 个警告")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
