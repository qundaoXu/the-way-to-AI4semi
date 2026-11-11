"""M04.2 线性模型 · 练习 2 的参考解答。完成练习前请不要阅读。

接口说明见 ``../exercises/logistic_regression.py``。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


def sigmoid(z: Array | float) -> Array | float:
    z = np.asarray(z, dtype=np.float64)
    # 只对非正数取 exp，避免溢出：
    #   z >= 0: 1 / (1 + exp(-z))
    #   z <  0: exp(z) / (1 + exp(z))
    e = np.exp(-np.abs(z))
    out = np.where(z >= 0, 1.0 / (1.0 + e), e / (1.0 + e))
    return out if out.ndim else float(out)


def logistic_loss_and_grad(
    w: Array, b: float, X: Array, y: Array, lam: float = 0.0
) -> tuple[float, Array, float]:
    n = X.shape[0]
    z = X @ w + b
    # log(1 + exp(z)) = logaddexp(0, z)，对任意 z 都稳定
    loss = float(np.mean(np.logaddexp(0.0, z) - y * z)) + 0.5 * lam * float(w @ w)
    error = sigmoid(z) - y  # p - y
    grad_w = X.T @ error / n + lam * w
    grad_b = float(error.mean())
    return loss, grad_w, grad_b


def fit_logistic_newton(
    X: Array,
    y: Array,
    lam: float,
    max_iter: int = 100,
    tol: float = 1e-10,
) -> tuple[Array, float]:
    if lam <= 0:
        raise ValueError("lam 必须大于 0")
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    n, d = X.shape
    # 增广设计矩阵：最后一列全 1 对应截距
    A = np.hstack([X, np.ones((n, 1))])
    theta = np.zeros(d + 1)
    penalty = np.full(d + 1, lam)
    penalty[-1] = 0.0  # 截距不受惩罚

    for _ in range(max_iter):
        p = sigmoid(A @ theta)
        grad = A.T @ (p - y) / n + penalty * theta
        if np.max(np.abs(grad)) < tol:
            break
        s = p * (1.0 - p)  # Hessian 的对角权重
        hessian = (A * s[:, None]).T @ A / n + np.diag(penalty)
        theta = theta - np.linalg.solve(hessian, grad)
    return theta[:-1], float(theta[-1])
