# 练习模板

一个练习由三个同名文件组成：练习桩、参考解答、测试。建设步骤和检查清单见末尾。

## 练习桩 `exercises/<name>.py`

```python
"""Mxx.y 章节名 · 练习 N：一句话主题。

讲义：../notes/<lesson>.qmd
测试：../tests/test_<name>.py
运行：make ex M=xx

约定
----
- 输入输出的形状、数据类型、单位。
- 允许使用和不允许使用的库。

把每个函数里的 ``raise NotImplementedError`` 换成你的实现。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


def function_name(x: Array, param: float) -> Array:
    """一句话说明，给出数学定义。

    Parameters
    ----------
    x : ndarray, shape (n, d)
        含义与单位。
    param : float
        含义与取值范围；非法取值时应抛出什么异常。

    Returns
    -------
    ndarray, shape (n,)
        含义与单位。

    Notes
    -----
    边界情况的约定、数值稳定性要求、指向讲义对应小节的提示。
    """
    raise NotImplementedError
```

## 参考解答 `solutions/<name>.py`

与练习桩同名、同接口。文件开头注明“完成练习前请不要阅读”。实现要正确、清晰，关键步骤用注释说明原因。

## 测试 `tests/test_<name>.py`

```python
"""Mxx.y 章节名 · 练习 N 的测试。"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from semiai.testing import load_impl

MODULE_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def impl():
    return load_impl(MODULE_DIR, "<name>")


def test_matches_reference_implementation(impl) -> None:
    """与成熟框架对齐到预设容差；注释写明容差的依据。"""


def test_some_property(impl) -> None:
    """性质测试：对称性、守恒、形状、单调性、解析解……"""
```

## 检查清单

- [ ] docstring 完整到不看讲义也知道接口；
- [ ] 每条测试都调用了被测实现；
- [ ] `LEARN_TARGET=solutions` 下全部通过；
- [ ] `LEARN_TARGET=exercises` 下全部失败（练习桩未实现时）；
- [ ] 测试以对齐、解析解、梯度检验、对称性等方法为主，不只是“能运行”；
- [ ] 测试文件的 docstring 写明章节 ID；
- [ ] 讲义的代码单元和 `examples/` 中没有泄露答案；
- [ ] 模块 `exercises/README.md` 的练习列表已更新；
- [ ] `ruff check` 通过。
