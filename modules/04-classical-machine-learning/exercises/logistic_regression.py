"""M04.2 线性模型 · 练习 2：逻辑回归。

讲义：../notes/02-linear-models.qmd
测试：../tests/test_logistic_regression.py
运行：make ex M=04

约定
----
- ``X`` 形状为 ``(n, d)``；标签 ``y`` 形状为 ``(n,)``，取值 0 或 1。
- 带截距 ``b``，截距不参与正则化。
- 只使用 NumPy，不能调用 scikit-learn 或 ``scipy.optimize``。

把每个函数里的 ``raise NotImplementedError`` 换成你的实现。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


def sigmoid(z: Array | float) -> Array | float:
    """Logistic 函数 ``1 / (1 + exp(-z))``，逐元素作用。

    Parameters
    ----------
    z : ndarray 或 float

    Returns
    -------
    与 ``z`` 同形状，取值在 [0, 1]。

    Notes
    -----
    实现必须数值稳定：``z = ±1000`` 时不能出现溢出警告或 NaN。
    直接写 ``1 / (1 + np.exp(-z))`` 在 ``z`` 很负时会溢出（讲义第 6 节）。
    """
    raise NotImplementedError


def logistic_loss_and_grad(
    w: Array, b: float, X: Array, y: Array, lam: float = 0.0
) -> tuple[float, Array, float]:
    """带 L2 正则的平均交叉熵损失及其梯度。

        J(w, b) = 1/n * sum_i [ log(1 + exp(z_i)) - y_i * z_i ] + lam/2 * ||w||^2
        z_i = x_i^T w + b

    Parameters
    ----------
    w : ndarray, shape (d,)
    b : float
    X : ndarray, shape (n, d)
    y : ndarray, shape (n,)，取值 0 或 1
    lam : float
        L2 正则化强度，``lam >= 0``。

    Returns
    -------
    loss : float
    grad_w : ndarray, shape (d,)
    grad_b : float

    Notes
    -----
    - 损失同样要数值稳定：``log(1 + exp(z))`` 在 ``z`` 很大时不能溢出。
    - 梯度的形式见讲义第 5.4 节。测试用有限差分检验。
    """
    raise NotImplementedError


def fit_logistic_newton(
    X: Array,
    y: Array,
    lam: float,
    max_iter: int = 100,
    tol: float = 1e-10,
) -> tuple[Array, float]:
    """用 Newton 法（即 IRLS）最小化 :func:`logistic_loss_and_grad` 的目标函数。

    Parameters
    ----------
    X : ndarray, shape (n, d)
    y : ndarray, shape (n,)，取值 0 或 1
    lam : float
        L2 正则化强度，必须大于 0（保证线性可分数据上也有有限解）；否则抛出 ``ValueError``。
    max_iter : int
        最多迭代次数。
    tol : float
        梯度的无穷范数小于 ``tol`` 时停止。

    Returns
    -------
    w : ndarray, shape (d,)
    b : float

    Notes
    -----
    - 从 ``w = 0, b = 0`` 出发。把 ``(w, b)`` 拼成一个 ``d + 1`` 维向量，每步求解
      ``H * delta = -g``，其中 Hessian 见讲义第 5.4 节。注意正则项只作用在 ``w`` 上。
    - 目标函数是严格凸的，Newton 法在这里通常 10 步以内收敛。
    - 与 scikit-learn 对齐时的换算关系：``C = 1 / (n * lam)``。
    """
    raise NotImplementedError
