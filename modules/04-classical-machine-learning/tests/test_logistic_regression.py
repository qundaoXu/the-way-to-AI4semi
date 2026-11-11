"""M04.2 线性模型 · 练习 2 的测试：逻辑回归。

默认检查 ``exercises/logistic_regression.py``（学习者的实现）；
``LEARN_TARGET=solutions`` 时检查参考解答。
"""

from __future__ import annotations

import warnings
from pathlib import Path

import numpy as np
import pytest
from sklearn.linear_model import LogisticRegression

from semiai.testing import assert_gradient_close, load_impl

MODULE_DIR = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def impl():
    return load_impl(MODULE_DIR, "logistic_regression")


@pytest.fixture
def data() -> tuple[np.ndarray, np.ndarray]:
    """两类有重叠的二维高斯数据，各 60 个样本，再加一维无关特征。"""
    rng = np.random.default_rng(7)
    n = 60
    X = np.vstack(
        [
            rng.normal([-1.0, 0.0, 0.0], 1.0, size=(n, 3)),
            rng.normal([1.0, 0.8, 0.0], 1.0, size=(n, 3)),
        ]
    )
    y = np.repeat([0.0, 1.0], n)
    return X, y


# --------------------------------------------------------------------------- #
# sigmoid
# --------------------------------------------------------------------------- #


def test_sigmoid_known_values(impl) -> None:
    z = np.array([-np.log(3.0), 0.0, np.log(3.0)])
    np.testing.assert_allclose(impl.sigmoid(z), [0.25, 0.5, 0.75], rtol=1e-14)
    assert float(impl.sigmoid(0.0)) == pytest.approx(0.5)


def test_sigmoid_symmetry_and_shape(impl) -> None:
    z = np.linspace(-30.0, 30.0, 41).reshape(1, 41)
    out = impl.sigmoid(z)
    assert np.shape(out) == z.shape
    np.testing.assert_allclose(out + impl.sigmoid(-z), 1.0, rtol=1e-14)


def test_sigmoid_is_stable_for_extreme_inputs(impl) -> None:
    """z = ±1000 时不能溢出：朴素写法 1/(1+exp(-z)) 会在这里触发 RuntimeWarning。"""
    z = np.array([-1000.0, -745.0, -50.0, 50.0, 745.0, 1000.0])
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        out = impl.sigmoid(z)
    assert np.all(np.isfinite(out))
    np.testing.assert_allclose(out[[0, -1]], [0.0, 1.0], atol=1e-300)
    np.testing.assert_allclose(out[2], np.exp(-50.0), rtol=1e-12)


# --------------------------------------------------------------------------- #
# 损失与梯度
# --------------------------------------------------------------------------- #


def test_loss_at_zero_parameters_is_log2(impl, data) -> None:
    """解析值：w = 0, b = 0 时每个样本的预测概率都是 1/2，平均损失为 log 2。"""
    X, y = data
    loss, grad_w, grad_b = impl.logistic_loss_and_grad(np.zeros(3), 0.0, X, y, lam=0.3)
    assert loss == pytest.approx(np.log(2.0), rel=1e-12)
    np.testing.assert_allclose(grad_w, X.T @ (0.5 - y) / len(y), rtol=1e-12)
    assert grad_b == pytest.approx(np.mean(0.5 - y), abs=1e-15)


@pytest.mark.parametrize("lam", [0.0, 0.2])
def test_gradient_matches_finite_difference(impl, data, lam: float) -> None:
    X, y = data
    rng = np.random.default_rng(8)
    theta = rng.normal(size=4)

    def loss(t: np.ndarray) -> float:
        return impl.logistic_loss_and_grad(t[:3], t[3], X, y, lam)[0]

    _, grad_w, grad_b = impl.logistic_loss_and_grad(theta[:3], theta[3], X, y, lam)
    assert np.shape(grad_w) == (3,)
    assert_gradient_close(loss, np.append(grad_w, grad_b), theta, rtol=1e-6, atol=1e-8)


def test_loss_is_stable_for_large_logits(impl) -> None:
    """|z| ~ 1e3 时损失应是有限值：正确分类的样本贡献 ≈ 0，错误分类的贡献 ≈ |z|。"""
    X = np.array([[1000.0], [-1000.0], [1000.0]])
    y = np.array([1.0, 0.0, 0.0])
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        loss, grad_w, grad_b = impl.logistic_loss_and_grad(np.array([1.0]), 0.0, X, y)
    assert loss == pytest.approx(1000.0 / 3.0, rel=1e-12)
    assert np.all(np.isfinite(grad_w)) and np.isfinite(grad_b)


# --------------------------------------------------------------------------- #
# Newton 法
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("lam", [1e-3, 0.05, 1.0])
def test_newton_matches_sklearn(impl, data, lam: float) -> None:
    X, y = data
    w, b = impl.fit_logistic_newton(X, y, lam)
    ref = LogisticRegression(C=1.0 / (len(y) * lam), tol=1e-12, max_iter=10_000).fit(X, y)
    np.testing.assert_allclose(w, ref.coef_.ravel(), rtol=1e-4, atol=1e-5)
    np.testing.assert_allclose(b, ref.intercept_[0], rtol=1e-4, atol=1e-5)


def test_newton_solution_has_zero_gradient(impl, data) -> None:
    """一阶最优条件，用测试内独立写出的目标函数做有限差分检验。"""
    X, y = data
    lam = 0.05
    w, b = impl.fit_logistic_newton(X, y, lam)

    def objective(t: np.ndarray) -> float:
        z = X @ t[:3] + t[3]
        return float(np.mean(np.logaddexp(0.0, z) - y * z) + 0.5 * lam * t[:3] @ t[:3])

    assert_gradient_close(objective, np.zeros(4), np.append(w, b), atol=1e-7)


def test_newton_stays_finite_on_separable_data(impl) -> None:
    """线性可分数据：没有正则化时 ||w|| 会发散，有 L2 正则时解有限且能完全分开两类。"""
    rng = np.random.default_rng(9)
    X = np.vstack([rng.normal(-3.0, 0.5, size=(20, 2)), rng.normal(3.0, 0.5, size=(20, 2))])
    y = np.repeat([0.0, 1.0], 20)
    w, b = impl.fit_logistic_newton(X, y, 1e-3)
    assert np.all(np.isfinite(w)) and np.isfinite(b)
    np.testing.assert_array_equal((X @ w + b > 0).astype(float), y)
    ref = LogisticRegression(C=1.0 / (len(y) * 1e-3), tol=1e-12, max_iter=10_000).fit(X, y)
    np.testing.assert_allclose(w, ref.coef_.ravel(), rtol=1e-3, atol=1e-4)


def test_newton_rejects_non_positive_lam(impl, data) -> None:
    X, y = data
    with pytest.raises(ValueError):
        impl.fit_logistic_newton(X, y, 0.0)
