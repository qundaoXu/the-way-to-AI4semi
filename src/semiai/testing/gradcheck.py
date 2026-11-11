"""有限差分梯度检验。

解析梯度是否写对，最直接的检验方法是和中心差分比较：

    df/dx_i ≈ [f(x + h e_i) - f(x - h e_i)] / (2h)

中心差分的截断误差是 O(h^2)，舍入误差是 O(eps_machine / h)，两者在
h ~ eps_machine^(1/3) ≈ 6e-6 附近平衡，因此默认步长取 1e-6。
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
from numpy.typing import ArrayLike, NDArray


def numerical_gradient(
    f: Callable[[NDArray[np.float64]], float],
    x: ArrayLike,
    eps: float = 1e-6,
) -> NDArray[np.float64]:
    """用中心差分计算标量函数 ``f`` 在 ``x`` 处的梯度。

    Parameters
    ----------
    f
        接受与 ``x`` 同形状的数组、返回标量的函数。
    x
        求导点，任意形状。不会被原地修改。
    eps
        基础步长。实际步长按分量取 ``eps * max(1, |x_i|)``，对量级差异大的变量更稳健。

    Returns
    -------
    ndarray
        与 ``x`` 同形状的梯度。需要对 ``f`` 求值 ``2 * x.size`` 次。
    """
    x0 = np.array(x, dtype=np.float64)
    grad = np.zeros_like(x0)
    work = x0.copy()
    for index in np.ndindex(x0.shape):
        original = x0[index]
        step = eps * max(1.0, abs(original))
        work[index] = original + step
        f_plus = float(f(work))
        work[index] = original - step
        f_minus = float(f(work))
        work[index] = original
        grad[index] = (f_plus - f_minus) / (2.0 * step)
    return grad


def assert_gradient_close(
    f: Callable[[NDArray[np.float64]], float],
    grad: Callable[[NDArray[np.float64]], ArrayLike] | ArrayLike,
    x: ArrayLike,
    *,
    eps: float = 1e-6,
    rtol: float = 1e-5,
    atol: float = 1e-7,
) -> float:
    """断言解析梯度与有限差分梯度一致，返回最大绝对误差。

    Parameters
    ----------
    f
        标量函数。
    grad
        解析梯度：可以是函数 ``grad(x)``，也可以是已经算好的数组。
    x
        检验点。
    eps, rtol, atol
        差分步长与容差。判据为 ``|g_解析 - g_数值| <= atol + rtol * |g_数值|``，逐分量比较。

    Raises
    ------
    AssertionError
        形状不一致，或任一分量超出容差。错误信息给出误差最大的分量。
    """
    x0 = np.array(x, dtype=np.float64)
    analytic = np.asarray(grad(x0.copy()) if callable(grad) else grad, dtype=np.float64)
    numeric = numerical_gradient(f, x0, eps=eps)
    if analytic.shape != numeric.shape:
        raise AssertionError(f"梯度形状不一致：解析 {analytic.shape}，数值 {numeric.shape}")

    error = np.abs(analytic - numeric)
    tolerance = atol + rtol * np.abs(numeric)
    max_error = float(error.max(initial=0.0))
    if np.any(error > tolerance):
        worst = np.unravel_index(int(np.argmax(error - tolerance)), error.shape)
        raise AssertionError(
            "解析梯度与有限差分不一致："
            f"分量 {worst} 处解析值 {analytic[worst]:.8e}，数值 {numeric[worst]:.8e}，"
            f"误差 {error[worst]:.3e} 超过容差 {tolerance[worst]:.3e}"
        )
    return max_error
