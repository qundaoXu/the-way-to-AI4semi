"""M04.2 示例：多重共线性下 OLS 系数的方差爆炸，以及 Ridge 的稳定作用。

运行（约 1 秒，仅 CPU）：

    uv run python modules/04-classical-machine-learning/examples/collinearity_demo.py

做法：固定真实系数 w = (1, 1)，让两个特征的相关系数 rho 从 0 增加到 0.999。
对每个 rho 重复生成 500 份带噪声的数据，分别用 OLS 和 Ridge 拟合，统计
系数估计在重复实验之间的标准差，以及在独立测试集上的预测 RMSE。

本示例用 scikit-learn 演示现象；从零实现见 ../exercises/linear_regression.py。
"""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import LinearRegression, Ridge

W_TRUE = np.array([1.0, 1.0])
NOISE = 0.5
N_TRAIN = 30
N_TEST = 2000
N_REPEAT = 500


def sample(rho: float, n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """生成两个相关系数为 rho 的标准正态特征，以及 y = X w + 噪声。"""
    cov = np.array([[1.0, rho], [rho, 1.0]])
    X = rng.multivariate_normal(np.zeros(2), cov, size=n)
    y = X @ W_TRUE + NOISE * rng.normal(size=n)
    return X, y


def experiment(rho: float, alpha: float, seed: int = 0) -> dict[str, float]:
    """返回 OLS 与 Ridge 的系数标准差（第一个系数）和测试 RMSE 的均值。"""
    rng = np.random.default_rng(seed)
    X_test, y_test = sample(rho, N_TEST, rng)
    coefs: dict[str, list[np.ndarray]] = {"ols": [], "ridge": []}
    errors: dict[str, list[float]] = {"ols": [], "ridge": []}
    for _ in range(N_REPEAT):
        X, y = sample(rho, N_TRAIN, rng)
        for name, model in (("ols", LinearRegression()), ("ridge", Ridge(alpha=alpha))):
            model.fit(X, y)
            coefs[name].append(model.coef_.copy())
            errors[name].append(float(np.sqrt(np.mean((model.predict(X_test) - y_test) ** 2))))
    return {
        "cond": float(np.sqrt((1 + rho) / (1 - rho))),  # 总体协方差对应的 cond(X)
        "ols_std": float(np.std([c[0] for c in coefs["ols"]])),
        "ridge_std": float(np.std([c[0] for c in coefs["ridge"]])),
        "ols_rmse": float(np.mean(errors["ols"])),
        "ridge_rmse": float(np.mean(errors["ridge"])),
    }


def main() -> None:
    alpha = 1.0
    print(f"真实系数 w = {W_TRUE}，噪声标准差 {NOISE}，训练样本 {N_TRAIN}，Ridge alpha = {alpha}")
    print(
        f"{'rho':>6} {'cond(X)':>9} {'std(w1) OLS':>12} {'std(w1) Ridge':>14} "
        f"{'RMSE OLS':>9} {'RMSE Ridge':>11}"
    )
    for rho in (0.0, 0.9, 0.99, 0.999):
        r = experiment(rho, alpha)
        print(
            f"{rho:>6} {r['cond']:>9.1f} {r['ols_std']:>12.3f} {r['ridge_std']:>14.3f} "
            f"{r['ols_rmse']:>9.3f} {r['ridge_rmse']:>11.3f}"
        )
    print(
        "\n读法：rho 增大时 OLS 单个系数的标准差急剧增大（w1 - w2 方向几乎不受数据约束），\n"
        "但测试 RMSE 变化不大，因为预测主要依赖被良好约束的 w1 + w2。\n"
        "Ridge 把系数标准差压了下来。训练误差或预测误差小，并不说明单个系数可信。"
    )


if __name__ == "__main__":
    main()
