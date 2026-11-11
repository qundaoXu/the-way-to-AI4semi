# 中英术语表

讲义中的术语以本表为准。英文术语在讲义里首次出现时附上；新术语随所在章节的建设补充进来，并注明归属章节。领域内已经通用英文的名称（如 Ridge、Lasso、Transformer）保留英文。

目前收录的是试点章节 M04.2 和仓库工作流用到的术语。

## 机器学习

| 中文 | English | 说明 | 归属章节 |
|---|---|---|---|
| 设计矩阵 | design matrix | 每行一个样本、每列一个特征的矩阵 $X$ | M04.2 |
| 最小二乘 | least squares | 最小化残差平方和；不带正则时称普通最小二乘（OLS） | M04.2 |
| 正规方程 | normal equations | $X^\top X\mathbf{w} = X^\top\mathbf{y}$ | M04.2 |
| 残差 | residual | 观测值与预测值之差 | M04.2 |
| 正交投影 | orthogonal projection | 子空间中距离给定向量最近的点 | M02.1 |
| 条件数 | condition number | 最大与最小奇异值之比，衡量问题对扰动的敏感度 | M02.1、M02.6 |
| 正则化 | regularization | 在目标函数中加入对模型复杂度的惩罚 | M04.1 |
| Ridge 回归（岭回归） | ridge regression | $\ell_2$ 惩罚的线性回归 | M04.2 |
| Lasso | lasso | $\ell_1$ 惩罚的线性回归，产生稀疏解 | M04.2 |
| 弹性网 | elastic net | $\ell_1$ 与 $\ell_2$ 惩罚的组合 | M04.2 |
| 收缩 | shrinkage | 估计值被系统地拉向零（或某个中心） | M04.2 |
| 稀疏性 | sparsity | 大部分系数精确为零 | M04.2 |
| 软阈值算子 | soft-thresholding operator | $S(z,t)=\operatorname{sign}(z)\max(\lvert z\rvert-t,0)$ | M04.2 |
| 坐标下降 | coordinate descent | 每次只优化一个坐标的迭代方法 | M04.2 |
| 逻辑回归 | logistic regression | Bernoulli 似然下的线性分类模型 | M04.2 |
| 交叉熵 | cross-entropy | 分类问题的负对数似然损失 | M02.3 |
| 迭代重加权最小二乘 | iteratively reweighted least squares (IRLS) | 逻辑回归和 GLM 的 Newton 法 | M04.2 |
| 广义线性模型 | generalized linear model (GLM) | 指数族响应分布 + 线性预测子 + 连接函数 | M04.2 |
| 连接函数 | link function | 把响应均值映射到线性预测子的函数 | M04.2 |
| 多重共线性 | multicollinearity | 特征之间近似线性相关 | M04.2 |
| 最大似然估计 | maximum likelihood estimation (MLE) | 最大化观测数据似然的参数估计 | M02.4 |
| 最大后验估计 | maximum a posteriori (MAP) | 最大化后验概率的参数估计 | M02.4 |
| 偏差–方差分解 | bias–variance decomposition | 期望预测误差分解为偏差、方差与噪声 | M04.1 |
| 数据泄漏 | data leakage | 测试信息以不该有的方式进入训练过程 | M03.4 |
| 校准 | calibration | 预测概率或不确定性与实际频率的一致程度 | M04.7、M06.5 |
| 机器学习势 | machine learning interatomic potential (MLIP) | 用 ML 模型拟合的原子间势能面 | M07.3 |

## 数值方法与测试

| 中文 | English | 说明 | 归属章节 |
|---|---|---|---|
| 有限差分梯度检验 | finite-difference gradient check | 用差分近似验证解析梯度 | M02.2、M05.2 |
| 中心差分 | central difference | $[f(x+h)-f(x-h)]/(2h)$，截断误差 $O(h^2)$ | M02.6 |
| 舍入误差 | round-off error | 浮点数有限精度造成的误差 | M02.6 |
| 性质测试 | property test | 检验对称性、守恒、形状等一般性质的测试 | M09.1 |
| 回归测试 | regression test | 固定种子下检查关键输出不变 | M09.1 |

## 本仓库的工作流术语

| 中文 | English / 标识 | 说明 |
|---|---|---|
| 练习桩 | exercise stub | 只有签名和 docstring、待学习者实现的函数文件 |
| 参考解答 | reference solution | Agent 编写、用于证明测试可通过的实现 |
| 学习状态 | `learn_status` | 学习者对某章的掌握程度，记录在讲义 frontmatter |
| 建设状态 | `build_status` | 某章讲义与代码的质量状态，记录在 `curriculum.yaml` |
| 研究锚点 | research anchor | 来自真实研究场景、用来说明“为什么学这一章”的问题（A1–A8） |
| 快速通过 | fast-track (FT) | 诊断通过即可跳过正文、只做练习验证的章节 |
| 即时建设 | just-in-time (JIT) build | 内容建设最多领先学习进度两章 |
| 概念归属 | concept ownership | 同一概念只在一个章节系统讲解，其他章节用链接引用 |
| 批注 | annotation | 写在讲义源文件中的 `.anno-*` callout |
