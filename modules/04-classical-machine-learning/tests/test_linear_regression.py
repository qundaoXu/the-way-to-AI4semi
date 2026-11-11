"""M04.2 线性模型 · 练习 1 的测试：最小二乘、Ridge 与 Lasso。

默认检查 ``exercises/linear_regression.py``（学习者的实现）；
``LEARN_TARGET=solutions`` 时检查参考解答。
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
from sklearn.linear_model import Lasso, LinearRegression, Ridge

from semiai.testing import assert_gradient_close, load_impl

MODULE_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def impl():
    return load_impl(MODULE_DIR, "linear_regression")


@pytest.fixture
def data() -> tuple[np.ndarray, np.ndarray]:
    """适定问题：n=60, d=5，特征之间有中等相关，带非零截距。"""
    rng = np.random.default_rng(42)
    n, d = 60, 5
    X = rng.normal(size=(n, d)) @ rng.normal(size=(d, d)) + rng.normal(size=d)
    w_true = np.array([1.5, -2.0, 0.0, 0.7, 0.0])
    y = X @ w_true + 3.0 + 0.3 * rng.normal(size=n)
    return X, y


# --------------------------------------------------------------------------- #
# 普通最小二乘
# --------------------------------------------------------------------------- #


def test_ols_matches_sklearn(impl, data) -> None:
    X, y = data
    w, b = impl.fit_ols(X, y)
    ref = LinearRegression().fit(X, y)
    assert np.shape(w) == (X.shape[1],)
    np.testing.assert_allclose(w, ref.coef_, rtol=1e-8, atol=1e-10)
    np.testing.assert_allclose(b, ref.intercept_, rtol=1e-8, atol=1e-10)


def test_ols_residual_is_orthogonal_to_column_space(impl, data) -> None:
    """几何视角：残差与每一列特征正交，且残差之和为零（对应截距列）。"""
    X, y = data
    w, b = impl.fit_ols(X, y)
    residual = y - X @ w - b
    scale = np.linalg.norm(X, axis=0) * np.linalg.norm(y)
    np.testing.assert_allclose(X.T @ residual / scale, 0.0, atol=1e-12)
    assert abs(residual.sum()) < 1e-9 * np.abs(y).sum()


def test_ols_recovers_exact_linear_relation(impl) -> None:
    """解析解比较：无噪声数据应当精确恢复真实参数。"""
    rng = np.random.default_rng(0)
    X = rng.normal(size=(30, 4))
    w_true = np.array([2.0, -1.0, 0.5, 3.0])
    w, b = impl.fit_ols(X, X @ w_true - 1.25)
    np.testing.assert_allclose(w, w_true, rtol=1e-10)
    np.testing.assert_allclose(b, -1.25, rtol=1e-10)


def test_ols_is_accurate_on_ill_conditioned_design(impl) -> None:
    """cond(X) ≈ 1e7：显式求解正规方程会把条件数平方到 1e14，丢掉大部分有效数字。"""
    rng = np.random.default_rng(1)
    n, d = 80, 6
    u, _ = np.linalg.qr(rng.normal(size=(n, d)))
    v, _ = np.linalg.qr(rng.normal(size=(d, d)))
    X = (u * np.logspace(0, -7, d)) @ v.T
    X -= X.mean(axis=0)  # 让中心化不改变奇异值
    w_true = rng.normal(size=d)
    w, b = impl.fit_ols(X, X @ w_true + 2.0)
    np.testing.assert_allclose(w, w_true, rtol=1e-6)
    np.testing.assert_allclose(b, 2.0, rtol=1e-8)


def test_ols_returns_minimum_norm_solution_when_rank_deficient(impl) -> None:
    """n < d：解不唯一时取中心化问题的最小范数解（与 scikit-learn 一致）。"""
    rng = np.random.default_rng(2)
    X = rng.normal(size=(8, 20))
    y = rng.normal(size=8)
    w, b = impl.fit_ols(X, y)
    ref = LinearRegression().fit(X, y)
    np.testing.assert_allclose(w, ref.coef_, rtol=1e-8, atol=1e-10)
    np.testing.assert_allclose(b, ref.intercept_, rtol=1e-8, atol=1e-10)
    np.testing.assert_allclose(X @ w + b, y, atol=1e-10)  # 欠定问题可以完全插值


# --------------------------------------------------------------------------- #
# Ridge
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("alpha", [1e-3, 1.0, 50.0])
def test_ridge_matches_sklearn(impl, data, alpha: float) -> None:
    X, y = data
    w, b = impl.fit_ridge(X, y, alpha)
    ref = Ridge(alpha=alpha, solver="cholesky").fit(X, y)
    np.testing.assert_allclose(w, ref.coef_, rtol=1e-8, atol=1e-10)
    np.testing.assert_allclose(b, ref.intercept_, rtol=1e-8, atol=1e-10)


def test_ridge_handles_more_features_than_samples(impl) -> None:
    rng = np.random.default_rng(3)
    X = rng.normal(size=(10, 25))
    y = rng.normal(size=10)
    w, b = impl.fit_ridge(X, y, 0.5)
    ref = Ridge(alpha=0.5, solver="svd").fit(X, y)
    np.testing.assert_allclose(w, ref.coef_, rtol=1e-8, atol=1e-10)
    np.testing.assert_allclose(b, ref.intercept_, rtol=1e-8, atol=1e-10)


def test_ridge_norm_shrinks_monotonically(impl, data) -> None:
    """alpha 越大，系数范数越小；alpha → 0 时回到最小二乘解。"""
    X, y = data
    alphas = [1e-8, 1e-2, 1.0, 1e2, 1e4]
    norms = [np.linalg.norm(impl.fit_ridge(X, y, a)[0]) for a in alphas]
    assert all(later < earlier for earlier, later in zip(norms, norms[1:], strict=False))
    w_small, b_small = impl.fit_ridge(X, y, alphas[0])
    ref = LinearRegression().fit(X, y)
    np.testing.assert_allclose(w_small, ref.coef_, rtol=1e-6)
    np.testing.assert_allclose(b_small, ref.intercept_, rtol=1e-6)


def test_ridge_does_not_penalize_intercept(impl, data) -> None:
    """给 y 加常数只改变截距，系数不变。"""
    X, y = data
    w0, b0 = impl.fit_ridge(X, y, 10.0)
    w1, b1 = impl.fit_ridge(X, y + 100.0, 10.0)
    np.testing.assert_allclose(w1, w0, rtol=1e-9, atol=1e-11)
    np.testing.assert_allclose(b1 - b0, 100.0, rtol=1e-9)


def test_ridge_rejects_non_positive_alpha(impl, data) -> None:
    X, y = data
    with pytest.raises(ValueError):
        impl.fit_ridge(X, y, 0.0)
    with pytest.raises(ValueError):
        impl.fit_ridge(X, y, -1.0)


def test_ridge_gradient_matches_finite_difference(impl, data) -> None:
    X, y = data
    rng = np.random.default_rng(4)
    d = X.shape[1]
    theta = rng.normal(size=d + 1)
    alpha = 0.7

    def loss(t: np.ndarray) -> float:
        return impl.ridge_loss_and_grad(t[:d], t[d], X, y, alpha)[0]

    _, grad_w, grad_b = impl.ridge_loss_and_grad(theta[:d], theta[d], X, y, alpha)
    assert np.shape(grad_w) == (d,)
    assert_gradient_close(loss, np.append(grad_w, grad_b), theta, rtol=1e-6, atol=1e-6)


def test_ridge_loss_value(impl) -> None:
    """手算可验证的小例子：J = 1/2 * ||r||^2 + alpha/2 * ||w||^2。"""
    X = np.array([[1.0, 0.0], [0.0, 2.0], [1.0, 1.0]])
    y = np.array([1.0, 2.0, 0.0])
    w = np.array([1.0, -1.0])
    # 预测 = [1, -2, 0] + 0.5 = [1.5, -1.5, 0.5]；残差 = [0.5, -3.5, 0.5]
    loss, _, _ = impl.ridge_loss_and_grad(w, 0.5, X, y, 3.0)
    assert loss == pytest.approx(0.5 * (0.25 + 12.25 + 0.25) + 0.5 * 3.0 * 2.0)


def test_ridge_solution_is_stationary_point(impl, data) -> None:
    """闭式解处梯度为零：把 fit_ridge 与 ridge_loss_and_grad 联系起来。"""
    X, y = data
    alpha = 2.5
    w, b = impl.fit_ridge(X, y, alpha)
    _, grad_w, grad_b = impl.ridge_loss_and_grad(w, b, X, y, alpha)
    scale = np.linalg.norm(X.T @ y)
    assert np.linalg.norm(grad_w) < 1e-10 * scale
    assert abs(grad_b) < 1e-10 * scale


# --------------------------------------------------------------------------- #
# Lasso
# --------------------------------------------------------------------------- #


def test_soft_threshold_values(impl) -> None:
    z = np.array([-3.0, -1.0, -0.2, 0.0, 0.2, 1.0, 3.0])
    expected = np.array([-2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0])
    np.testing.assert_allclose(impl.soft_threshold(z, 1.0), expected, atol=1e-15)
    np.testing.assert_allclose(impl.soft_threshold(z, 0.0), z, atol=1e-15)
    assert float(impl.soft_threshold(2.5, 1.0)) == pytest.approx(1.5)


@pytest.mark.parametrize("alpha", [0.01, 0.1, 0.5])
def test_lasso_matches_sklearn(impl, data, alpha: float) -> None:
    X, y = data
    w, b = impl.fit_lasso_cd(X, y, alpha)
    ref = Lasso(alpha=alpha, tol=1e-14, max_iter=100_000).fit(X, y)
    np.testing.assert_allclose(w, ref.coef_, rtol=1e-6, atol=1e-7)
    np.testing.assert_allclose(b, ref.intercept_, rtol=1e-6, atol=1e-7)


def test_lasso_produces_exact_zeros(impl, data) -> None:
    """稀疏性：足够强的 L1 惩罚把一部分系数精确压到 0，而不是很小的数。"""
    X, y = data
    w, _ = impl.fit_lasso_cd(X, y, 0.5)
    ref = Lasso(alpha=0.5, tol=1e-14, max_iter=100_000).fit(X, y)
    assert np.any(ref.coef_ == 0.0) and np.any(ref.coef_ != 0.0)  # 确认这个例子确实稀疏
    np.testing.assert_array_equal(w == 0.0, ref.coef_ == 0.0)


def test_lasso_all_zero_above_alpha_max(impl, data) -> None:
    """alpha >= max_j |x_j^T y_c| / n 时全部系数为 0，截距等于 y 的均值。"""
    X, y = data
    Xc, yc = X - X.mean(axis=0), y - y.mean()
    alpha_max = np.max(np.abs(Xc.T @ yc)) / len(y)
    w, b = impl.fit_lasso_cd(X, y, 1.01 * alpha_max)
    np.testing.assert_array_equal(w, np.zeros(X.shape[1]))
    assert b == pytest.approx(y.mean())
    w_below, _ = impl.fit_lasso_cd(X, y, 0.9 * alpha_max)
    assert np.count_nonzero(w_below) >= 1


def test_lasso_with_zero_alpha_equals_ols(impl, data) -> None:
    X, y = data
    w, b = impl.fit_lasso_cd(X, y, 0.0, max_iter=100_000, tol=1e-13)
    ref = LinearRegression().fit(X, y)
    np.testing.assert_allclose(w, ref.coef_, rtol=1e-6, atol=1e-8)
    np.testing.assert_allclose(b, ref.intercept_, rtol=1e-6, atol=1e-8)
