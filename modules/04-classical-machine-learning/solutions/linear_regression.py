"""M04.2 线性模型 · 练习 1 的参考解答。完成练习前请不要阅读。

参考解答的作用是证明测试本身正确且可以通过。接口说明见
``../exercises/linear_regression.py``。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


def _center(X: Array, y: Array) -> tuple[Array, Array, Array, float]:
    """中心化：截距不受惩罚时，最优截距总是 ``y_mean - x_mean @ w``。"""
    x_mean = X.mean(axis=0)
    y_mean = float(y.mean())
    return X - x_mean, y - y_mean, x_mean, y_mean


def fit_ols(X: Array, y: Array) -> tuple[Array, float]:
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    Xc, yc, x_mean, y_mean = _center(X, y)
    # lstsq 基于 SVD，直接作用在 Xc 上：条件数是 cond(Xc) 而不是 cond(Xc)^2，
    # 秩亏时返回最小范数解。
    w, *_ = np.linalg.lstsq(Xc, yc, rcond=None)
    return w, y_mean - float(x_mean @ w)


def fit_ridge(X: Array, y: Array, alpha: float) -> tuple[Array, float]:
    if alpha <= 0:
        raise ValueError("alpha 必须大于 0")
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    Xc, yc, x_mean, y_mean = _center(X, y)
    n, d = Xc.shape
    if d <= n:
        # (Xc^T Xc + alpha I) w = Xc^T yc，系数矩阵对称正定，用 Cholesky 求解
        gram = Xc.T @ Xc + alpha * np.eye(d)
        w = _solve_spd(gram, Xc.T @ yc)
    else:
        # d > n 时用对偶形式 w = Xc^T (Xc Xc^T + alpha I)^{-1} yc，只需解 n 阶方程组
        gram = Xc @ Xc.T + alpha * np.eye(n)
        w = Xc.T @ _solve_spd(gram, yc)
    return w, y_mean - float(x_mean @ w)


def _solve_spd(a: Array, rhs: Array) -> Array:
    """用 Cholesky 分解求解对称正定方程组。"""
    lower = np.linalg.cholesky(a)
    return np.linalg.solve(lower.T, np.linalg.solve(lower, rhs))


def ridge_loss_and_grad(
    w: Array, b: float, X: Array, y: Array, alpha: float
) -> tuple[float, Array, float]:
    residual = X @ w + b - y
    loss = 0.5 * float(residual @ residual) + 0.5 * alpha * float(w @ w)
    grad_w = X.T @ residual + alpha * w
    grad_b = float(residual.sum())
    return loss, grad_w, grad_b


def soft_threshold(z: Array | float, t: float) -> Array | float:
    return np.sign(z) * np.maximum(np.abs(z) - t, 0.0)


def fit_lasso_cd(
    X: Array,
    y: Array,
    alpha: float,
    max_iter: int = 10_000,
    tol: float = 1e-10,
) -> tuple[Array, float]:
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    Xc, yc, x_mean, y_mean = _center(X, y)
    n, d = Xc.shape
    col_norm = (Xc**2).sum(axis=0) / n  # 1/n * ||x_j||^2
    w = np.zeros(d)
    residual = yc.copy()  # w = 0 时残差就是 yc

    for _ in range(max_iter):
        max_change = 0.0
        for j in range(d):
            if col_norm[j] == 0.0:
                continue
            old = w[j]
            # 把第 j 个特征的贡献加回残差，得到“去掉 j 之后”的部分残差
            rho = (Xc[:, j] @ residual) / n + col_norm[j] * old
            new = float(soft_threshold(rho, alpha)) / col_norm[j]
            if new != old:
                residual += Xc[:, j] * (old - new)
                w[j] = new
                max_change = max(max_change, abs(new - old))
        if max_change < tol:
            break
    return w, y_mean - float(x_mean @ w)
