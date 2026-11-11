# 代码规范

适用于仓库中的全部 Python 代码：`src/semiai/`、各模块的 `examples/`、`exercises/`、`solutions/`、`tests/`、`notebooks/`，以及 `projects/`。依据 `PROJECT_BLUEPRINT.md` 第 5、8 节。

## 1. 代码放在哪里

| 位置 | 内容 | 规则 |
|---|---|---|
| `modules/<模块>/exercises/` | 练习桩 | 只有签名、完整 docstring 和 `raise NotImplementedError` |
| `modules/<模块>/solutions/` | 参考解答 | 与练习桩同名、同接口 |
| `modules/<模块>/tests/` | 测试 | 通过 `load_impl` 加载实现；文件 docstring 写明章节 ID |
| `modules/<模块>/examples/` | 概念演示 | 独立可运行，不泄露练习答案 |
| `modules/<模块>/notebooks/` | 探索实验 | Jupytext percent 格式的 `.py`；`.ipynb` 不提交 |
| `src/semiai/` | 公共代码 | 只有被两个以上模块或项目实际复用的代码才放进来 |
| `projects/` | 综合项目 | 做集成、规模化和真实评价，不重复单个算法练习 |

算法实现必须存在于 `.py` 文件中，不能只存在于 Notebook 或讲义的代码单元里。

## 2. 三个实现层次

- **Level 1：From Scratch。** 用 NumPy 或纯 Python 实现关键算法，目的是理解机制。练习的主体，由学习者完成。
- **Level 2：Framework。** 用 scikit-learn、PyTorch、e3nn 等实现同一算法，并与 Level 1 的结果对齐。
- **Level 3：Applied Experiment。** 在真实公开数据上完成实验，并按 `templates/experiment-record-template.md` 记录。

不是每个知识点都需要三个层次。每章在讲义“代码导航”里说明选了哪些层次和理由。

## 3. 质量要求

- 用函数和类组织代码，避免不必要的全局变量。
- 公共函数有类型注解和 docstring。docstring 采用 NumPy 风格，写明**数组形状**和**物理单位**。
- 随机性通过 `np.random.default_rng(seed)` 显式传入，固定种子。
- 示例默认在 CPU 上数分钟内运行完；需要 GPU 时在文件开头注明。
- 不提交模型权重、训练数据和运行产物（`.gitignore` 已覆盖常见类型）。
- 不写虚构的性能数字。文档里出现的结果必须是实际运行得到的。
- 通过 `ruff check`；提交时 pre-commit 会运行 `ruff format`。行宽 100。
- 标识符、文件名用英文；注释和 docstring 可以用中文。

## 4. 练习桩的写法

```python
def fit_ridge(X: Array, y: Array, alpha: float) -> tuple[Array, float]:
    """Ridge 回归：最小化 ``||y - X w - b||^2 + alpha * ||w||^2``。

    Parameters
    ----------
    X : ndarray, shape (n, d)
    y : ndarray, shape (n,)
    alpha : float
        正则化强度，必须大于 0；否则抛出 ``ValueError``。

    Returns
    -------
    w : ndarray, shape (d,)
    b : float
    """
    raise NotImplementedError
```

docstring 要完整到不看讲义也知道接口：数学定义、输入输出的形状、边界情况的约定、允许使用的库。

## 5. 测试的写法

```python
"""M04.2 线性模型 · 练习 1 的测试。"""  # 写明章节 ID，check_repo.py 据此找到测试

from pathlib import Path
import pytest
from semiai.testing import load_impl

MODULE_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def impl():
    return load_impl(MODULE_DIR, "linear_regression")  # 按 LEARN_TARGET 加载


def test_ridge_matches_sklearn(impl): ...
```

要求：

- **每条测试都必须调用被测实现**，这样练习桩在测试下全部失败，证明测试确实在检查实现。
- 参考解答在 `LEARN_TARGET=solutions` 下全部通过。
- 测试名说明被检查的性质，失败信息能帮学习者定位问题。
- 运行超过约 1 分钟的测试加 `@pytest.mark.slow`，需要 GPU 的加 `@pytest.mark.gpu`；两者默认不运行。

## 6. 数值代码怎么测

只测“能运行”没有意义。优先使用下面这些方法：

| 方法 | 示例 |
|---|---|
| 与参考实现对齐 | 自写 PCA 与 scikit-learn 对齐到 `atol=1e-8`（考虑符号不确定性） |
| 与解析解比较 | 线性回归的闭式解；谐振子的解析轨迹 |
| 有限差分梯度检验 | 力与能量梯度的一致性：`semiai.testing.assert_gradient_close` |
| 对称性检验 | 随机旋转、平移、置换下的不变性或等变性 |
| 守恒律检验 | NVE 模拟中的总能量漂移 |
| 回归测试 | 固定种子下关键输出不变 |

容差要有依据。与迭代求解器对齐时，容差取决于对方的收敛判据；涉及病态问题时，容差取决于条件数乘以机器精度。在测试里用注释写明容差的来源。

公共测试工具放在 `src/semiai/testing/`。目前有 `load_impl`、`numerical_gradient`、`assert_gradient_close`；等变性检验和随机旋转生成在 M02.7 需要时加入。

## 7. 依赖

- 只有某章确实需要时才添加依赖，放进对应的 extra，并在提交说明里写明原因。
- 不为一个示例引入重量级依赖。
- 添加或升级依赖后提交更新后的 `uv.lock`。

## 8. 提交信息

一个任务对应一个或一组小提交，前缀如下：

| 前缀 | 用途 |
|---|---|
| `content(M04.2): ...` | 讲义内容 |
| `exercise(M04.2): ...` | 练习桩、参考解答、测试 |
| `infra: ...` | 脚本、配置、CI、主题 |
| `fix: ...` | 修正错误 |
| `sync: ...` | 只更新生成的索引 |

不改写 Git 历史，不强制推送。
