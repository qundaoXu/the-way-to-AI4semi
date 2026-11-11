"""仓库级 pytest 配置。

提供 ``--results-json PATH`` 选项：把本次测试的逐条结果写入 JSON 文件。
``make ex`` 用它生成 ``progress/test-results.json``，供学习网站首页显示。
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--results-json",
        action="store",
        default=None,
        metavar="PATH",
        help="把逐条测试结果写入指定的 JSON 文件",
    )


class _ResultsRecorder:
    def __init__(self, path: Path, rootdir: Path) -> None:
        self.path = path
        self.rootdir = rootdir
        self.outcomes: dict[str, str] = {}

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        # 一条测试有 setup / call / teardown 三个阶段：任一阶段失败即记为失败。
        previous = self.outcomes.get(report.nodeid)
        if report.failed:
            self.outcomes[report.nodeid] = "failed"
        elif report.skipped and previous is None:
            self.outcomes[report.nodeid] = "skipped"
        elif report.when == "call" and report.passed and previous is None:
            self.outcomes[report.nodeid] = "passed"

    def pytest_sessionfinish(self, session: pytest.Session) -> None:
        tests = [
            {"nodeid": nodeid, "outcome": outcome} for nodeid, outcome in self.outcomes.items()
        ]
        summary = {key: 0 for key in ("passed", "failed", "skipped")}
        for outcome in self.outcomes.values():
            summary[outcome] += 1
        payload = {
            "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
            "target": os.environ.get("LEARN_TARGET", "exercises"),
            "args": [str(arg) for arg in session.config.args],
            "summary": summary,
            "tests": tests,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", "utf-8")


def pytest_configure(config: pytest.Config) -> None:
    target = config.getoption("--results-json")
    if target:
        path = Path(target)
        if not path.is_absolute():
            path = Path(config.rootpath) / path
        config.pluginmanager.register(
            _ResultsRecorder(path, Path(config.rootpath)), "semiai-results"
        )
