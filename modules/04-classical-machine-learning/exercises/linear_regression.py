"""M04.2 线性模型 · 练习 1：最小二乘、Ridge 与 Lasso。

讲义：../notes/02-linear-models.qmd
测试：../tests/test_linear_regression.py
运行：make ex M=04

约定
----
- ``X`` 形状为 ``(n, d)``，``y`` 形状为 ``(n,)``，全部使用 float64。
- 所有模型都带截距 ``b``，且**截距不参与正则化**。
- 可以使用 NumPy（包括 ``np.linalg`` 中的 ``lstsq``、``solve``、``qr``、``svd``、``cholesky``），
  不能调用 scikit-learn 或 ``scipy.optimize``。

把每个函数里的 ``raise NotImplementedError`` 换成你的实现。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


def fit_ols(X: Array, y: Array) -> tuple[Array, float]:
    """普通最小二乘：最小化 ``||y - X w - b||^2``。

    Parameters
    ----------
    X : ndarray, shape (n, d)
        设计矩阵，不含全 1 列。允许列之间线性相关，也允许 ``n < d``。
    y : ndarray, shape (n,)
        目标值。

    Returns
    -------
    w : ndarray, shape (d,)
        系数。
    b : float
        截距。

    Notes
    -----
    - 解不唯一时（``X`` 中心化后列不满秩），返回中心化问题的最小范数解，即先令
      ``Xc = X - X.mean(axis=0)``、``yc = y - y.mean()``，取使 ``||w||`` 最小的 ``w``，
      再由 ``b = y.mean() - X.mean(axis=0) @ w`` 得到截距。这与 scikit-learn 的约定一致。
    - 不要显式求解正规方程 ``X^T X w = X^T y``：它的条件数是 ``X`` 条件数的平方，
      测试中有一个病态设计矩阵专门检查这一点（讲义第 6 节）。
    """
    raise NotImplementedError


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

    Notes
    -----
    截距不受惩罚，因此先把 ``X`` 和 ``y`` 中心化，在中心化数据上求解闭式解
    （讲义第 5.2 节），再恢复截距。``alpha > 0`` 时线性方程组的系数矩阵对称正定。
    """
    raise NotImplementedError


def ridge_loss_and_grad(
    w: Array, b: float, X: Array, y: Array, alpha: float
) -> tuple[float, Array, float]:
    """Ridge 目标函数及其梯度。

    目标函数取

        J(w, b) = 1/2 * ||y - X w - b||^2 + alpha/2 * ||w||^2

    它与 :func:`fit_ridge` 的目标只差常数因子 1/2，最小点相同。

    Parameters
    ----------
    w : ndarray, shape (d,)
    b : float
    X : ndarray, shape (n, d)
    y : ndarray, shape (n,)
    alpha : float

    Returns
    -------
    loss : float
        ``J(w, b)``。
    grad_w : ndarray, shape (d,)
        ``dJ/dw``。
    grad_b : float
        ``dJ/db``。

    Notes
    -----
    测试用有限差分检验梯度，并检查 :func:`fit_ridge` 的解处梯度为零。
    """
    raise NotImplementedError


def soft_threshold(z: Array | float, t: float) -> Array | float:
    """软阈值算子 ``S(z, t) = sign(z) * max(|z| - t, 0)``，逐元素作用。

    Parameters
    ----------
    z : ndarray 或 float
    t : float
        阈值，``t >= 0``。

    Returns
    -------
    与 ``z`` 同形状。``|z| <= t`` 的分量被置为 0，其余分量向 0 收缩 ``t``。
    """
    raise NotImplementedError


def fit_lasso_cd(
    X: Array,
    y: Array,
    alpha: float,
    max_iter: int = 10_000,
    tol: float = 1e-10,
) -> tuple[Array, float]:
    """用循环坐标下降求解 Lasso。

    目标函数（与 scikit-learn 的 ``Lasso`` 一致）：

        1/(2n) * ||y - X w - b||^2 + alpha * ||w||_1

    Parameters
    ----------
    X : ndarray, shape (n, d)
    y : ndarray, shape (n,)
    alpha : float
        正则化强度，``alpha >= 0``。
    max_iter : int
        最多扫描全部坐标的轮数。
    tol : float
        一轮扫描中系数的最大改变量小于 ``tol`` 时停止。

    Returns
    -------
    w : ndarray, shape (d,)
        很多分量会精确等于 0。
    b : float

    Notes
    -----
    - 从 ``w = 0`` 出发，在中心化数据上按 ``j = 0, 1, ..., d-1`` 的顺序循环更新：

          rho_j = 1/n * x_j^T (r + x_j * w_j)      # r 为当前残差
          w_j   = S(rho_j, alpha) / (1/n * ||x_j||^2)

      其中 ``S`` 是 :func:`soft_threshold`。推导见讲义第 5.3 节。
    - 维护残差 ``r`` 并在每次更新 ``w_j`` 后增量修正，这样单次坐标更新的代价是 O(n)。
    - 某一列中心化后全为 0 时，对应系数保持为 0。
    """
    raise NotImplementedError
