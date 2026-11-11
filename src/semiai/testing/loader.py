"""按 ``LEARN_TARGET`` 加载练习实现或参考解答。

同一套测试既要检查学习者写在 ``exercises/`` 里的实现，也要检查 ``solutions/`` 里的
参考解答。测试通过 :func:`load_impl` 取得实现模块，由环境变量决定加载哪一份。
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from types import ModuleType

LEARN_TARGETS = ("exercises", "solutions")
_ENV_VAR = "LEARN_TARGET"


def learn_target() -> str:
    """返回当前的加载目标：``exercises``（默认）或 ``solutions``。"""
    target = os.environ.get(_ENV_VAR, "exercises").strip() or "exercises"
    if target not in LEARN_TARGETS:
        raise ValueError(f"{_ENV_VAR} 必须是 {LEARN_TARGETS} 之一，当前为 {target!r}")
    return target


def load_impl(
    module_dir: str | os.PathLike[str], name: str, target: str | None = None
) -> ModuleType:
    """从 ``<module_dir>/<target>/<name>.py`` 加载实现模块。

    Parameters
    ----------
    module_dir
        模块目录，例如 ``modules/04-classical-machine-learning``。测试文件中通常写作
        ``Path(__file__).resolve().parents[1]``。
    name
        练习文件名，不含 ``.py``。
    target
        ``"exercises"`` 或 ``"solutions"``。缺省时读取环境变量 ``LEARN_TARGET``。

    Returns
    -------
    ModuleType
        已执行的模块对象。每次调用都重新执行文件，因此学习者修改代码后无需重启解释器。
    """
    target = target or learn_target()
    if target not in LEARN_TARGETS:
        raise ValueError(f"target 必须是 {LEARN_TARGETS} 之一，当前为 {target!r}")

    module_dir = Path(module_dir).resolve()
    path = module_dir / target / f"{name}.py"
    if not path.is_file():
        raise FileNotFoundError(f"找不到实现文件：{path}")

    # 模块名带上目标和模块目录，避免 exercises 与 solutions 的同名文件互相覆盖。
    slug = module_dir.name.replace("-", "_")
    qualified = f"semiai_impl.{target}.{slug}.{name}"
    spec = importlib.util.spec_from_file_location(qualified, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法为 {path} 创建模块加载器")
    module = importlib.util.module_from_spec(spec)
    sys.modules[qualified] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(qualified, None)
        raise
    return module
