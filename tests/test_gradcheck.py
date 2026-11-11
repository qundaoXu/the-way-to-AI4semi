"""semiai.testing 有限差分梯度检验工具的测试。"""

from __future__ import annotations

import numpy as np
import pytest

from semiai.testing import assert_gradient_close, numerical_gradient


def test_quadratic_form_matches_analytic_gradient() -> None:
    rng = np.random.default_rng(0)
    a = rng.normal(size=(5, 5))
    a = a + a.T
    x = rng.normal(size=5)

    def f(v: np.ndarray) -> float:
        return 0.5 * v @ a @ v

    np.testing.assert_allclose(numerical_gradient(f, x), a @ x, rtol=1e-7, atol=1e-8)


def test_supports_matrix_arguments() -> None:
    rng = np.random.default_rng(1)
    w = rng.normal(size=(3, 4))

    def f(m: np.ndarray) -> float:
        return float(np.sum(np.sin(m)))

    grad = numerical_gradient(f, w)
    assert grad.shape == w.shape
    np.testing.assert_allclose(grad, np.cos(w), rtol=1e-7, atol=1e-8)


def test_input_is_not_modified() -> None:
    x = np.array([1.0, -2.0, 3.0])
    before = x.copy()
    numerical_gradient(lambda v: float(np.sum(v**3)), x)
    np.testing.assert_array_equal(x, before)


def test_assert_passes_for_correct_gradient() -> None:
    x = np.array([0.3, -1.2, 2.5])
    max_error = assert_gradient_close(lambda v: float(np.sum(np.exp(v))), np.exp, x)
    assert max_error < 1e-6


def test_assert_accepts_precomputed_array() -> None:
    x = np.array([0.5, 1.5])
    assert_gradient_close(lambda v: float(np.sum(v**2)), 2 * x, x)


def test_assert_detects_wrong_gradient() -> None:
    x = np.array([0.3, -1.2, 2.5])
    with pytest.raises(AssertionError, match="不一致"):
        # 漏掉因子 2 是手推梯度时最常见的错误
        assert_gradient_close(lambda v: float(np.sum(v**2)), lambda v: v, x)


def test_assert_detects_shape_mismatch() -> None:
    x = np.zeros((2, 3))
    with pytest.raises(AssertionError, match="形状"):
        assert_gradient_close(lambda v: float(np.sum(v)), np.ones(6), x)
