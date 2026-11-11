# Module 04：传统机器学习（Classical Machine Learning）

模块优先级 `P0` · 估算学时 60–80 h

## 定位

统计学习的核心原理，以及作为研究者最需要的模型比较与评价方法论。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M04.1 | 统计学习基础<br>Statistical Learning Foundations | P0 | M02.1, M02.3 | — | Planned | Not Started |
| M04.2 | [线性模型](notes/02-linear-models.qmd)<br>Linear Models | P0 | M02.1, M02.2, M02.4 | — | Draft | Not Started |
| M04.3 | 核方法与高斯过程<br>Kernel Methods and Gaussian Processes | P0 | M04.2, M02.3 | — | Planned | Not Started |
| M04.4 | 树模型与集成学习<br>Trees and Ensemble Learning | P0 | M04.1 | — | Planned | Not Started |
| M04.5 | 无监督学习<br>Unsupervised Learning | P0 | M02.1, M02.3 | — | Planned | Not Started |
| M04.6 | 异常检测<br>Anomaly Detection | P1 | M04.4, M04.5 | — | Planned | Not Started |
| M04.7 | 模型评价与解释<br>Model Evaluation and Interpretation | P0 | M04.1, M04.2 | A3 | Planned | Not Started |
| M04.8 | ML 研究方法论<br>ML Research Methodology | P0 | M04.7, M02.4 | A3 | Planned | Not Started |

**各章范围**

- **M04.1 统计学习基础**：经验风险最小化；偏差–方差分解；过拟合与欠拟合；模型复杂度与泛化的直觉；正则化；No Free Lunch。
- **M04.2 线性模型**：最小二乘的几何视角与概率视角；Ridge、Lasso、Elastic Net；Logistic Regression；广义线性模型。
- **M04.3 核方法与高斯过程**：核技巧与再生核的直觉；核岭回归；SVM；高斯过程回归（后验推导、超参数学习、计算复杂度）；与 SOAP-GAP 类 MLIP 的联系。高斯过程的主要归属章节。
- **M04.4 树模型与集成学习**：决策树；Bagging 与随机森林；Gradient Boosting；XGBoost、LightGBM 的工程优化。
- **M04.5 无监督学习**：K-means；GMM 与 EM 算法；层次聚类；DBSCAN；PCA、t-SNE、UMAP 及其可视化陷阱。
- **M04.6 异常检测**：统计方法（Z-score、IQR）；Isolation Forest；One-Class SVM；LOF；异常检测的评价难点。
- **M04.7 模型评价与解释**：回归与分类指标；交叉验证的多种形式；超参数搜索；概率校准；特征重要性；SHAP 及其局限。不确定性量化归属 M06.5。
- **M04.8 ML 研究方法论**：基线选择；消融实验；多随机种子与置信区间；模型间的统计显著性比较；benchmark 设计与“刷榜”问题；代理指标与最终目标不一致的问题（如“低 RMSE ≠ 可用的势”）；如何阅读与复现论文。研究者必修。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 练习

M04.2 是全仓库的试点章节，练习–解答–测试机制在这里第一次完整走通。练习列表与运行方式见 [exercises/README.md](exercises/README.md)；完成练习前不要打开 `solutions/`。

```bash
make ex M=04        # 用自己的实现运行本模块的测试
```

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 从零实现线性回归、逻辑回归、决策树、K-means、高斯过程回归，在测试中与 scikit-learn 结果对齐到预设容差；
- 在一个 Matbench 任务上完成一份比较报告：包含合理基线、至少一组消融、5 个以上随机种子的统计结果；
- 写一篇 1–2 页的方法论短文：说明为什么误差指标不足以评价 MLIP，提出分层评价思路。

## 研究锚点

- **A3**：为什么“低 RMSE ≠ 可用的势”：如何设计分层评价体系

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。

## 诊断

本模块在开始前先做诊断测评，每章得到 `Skip`、`Light` 或 `Full` 的结论。诊断题在 Phase 1b 以 QUIZ 模式生成，作答结果保存到 `progress/diagnostics/`。
