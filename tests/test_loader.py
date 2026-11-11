"""semiai.testing.load_impl 的测试。"""

from __future__ import annotations

from pathlib import Path

import pytest

from semiai.testing import learn_target, load_impl


@pytest.fixture
def module_dir(tmp_path: Path) -> Path:
    """一个带 exercises/ 与 solutions/ 的假模块目录。"""
    root = tmp_path / "99-fake-module"
    for target, value in (("exercises", 1), ("solutions", 2)):
        (root / target).mkdir(parents=True)
        (root / target / "answer.py").write_text(f"VALUE = {value}\n", "utf-8")
    return root


def test_default_target_is_exercises(module_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LEARN_TARGET", raising=False)
    assert learn_target() == "exercises"
    assert load_impl(module_dir, "answer").VALUE == 1


def test_env_selects_solutions(module_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LEARN_TARGET", "solutions")
    assert load_impl(module_dir, "answer").VALUE == 2


def test_explicit_target_overrides_env(module_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LEARN_TARGET", "solutions")
    assert load_impl(module_dir, "answer", target="exercises").VALUE == 1


def test_both_targets_coexist(module_dir: Path) -> None:
    exercise = load_impl(module_dir, "answer", target="exercises")
    solution = load_impl(module_dir, "answer", target="solutions")
    assert (exercise.VALUE, solution.VALUE) == (1, 2)
    assert exercise.__name__ != solution.__name__


def test_reload_picks_up_edits(module_dir: Path) -> None:
    assert load_impl(module_dir, "answer", target="exercises").VALUE == 1
    (module_dir / "exercises" / "answer.py").write_text("VALUE = 42\n", "utf-8")
    assert load_impl(module_dir, "answer", target="exercises").VALUE == 42


def test_invalid_target_raises(module_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LEARN_TARGET", "answers")
    with pytest.raises(ValueError, match="LEARN_TARGET"):
        load_impl(module_dir, "answer")


def test_missing_file_raises(module_dir: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_impl(module_dir, "does_not_exist", target="exercises")
