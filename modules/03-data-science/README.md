# Module 03：数据科学（Data Science）

模块优先级 `P0` · 估算学时 30–40 h

## 定位

独立处理陌生数据集，并能正确处理科学数据中最常见的陷阱：相关样本与泄漏。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M03.1 | [数据获取与存储](notes/01-data-acquisition-storage.qmd) · [notebook](notebooks/01-data-acquisition-storage.ipynb)<br>Data Acquisition and Storage | P0 | — | — | Draft | Not Started |
| M03.2 | [数据处理](notes/02-data-wrangling.qmd) · [notebook](notebooks/02-data-wrangling.ipynb)<br>Data Wrangling | P0 · FT | M03.1 | — | Draft | Not Started |
| M03.3 | [探索性数据分析与可视化](notes/03-eda-visualization.qmd) · [notebook](notebooks/03-eda-visualization.ipynb)<br>Exploratory Data Analysis and Visualization | P0 | M03.2, M02.3 | — | Draft | Not Started |
| M03.4 | [数据划分、泄漏与分布偏移](notes/04-splitting-leakage-shift.qmd) · [notebook](notebooks/04-splitting-leakage-shift.ipynb)<br>Data Splitting, Leakage and Distribution Shift | P0 | M03.2, M04.1 | A2 | Draft | Not Started |
| M03.5 | [时间序列](notes/05-time-series.qmd) · [notebook](notebooks/05-time-series.ipynb)<br>Time Series | P1 | M03.2, M02.4 | A5 | Draft | Not Started |
| M03.6 | [实验设计（DOE）](notes/06-design-of-experiments.qmd) · [notebook](notebooks/06-design-of-experiments.ipynb)<br>Design of Experiments | P1 | M02.4 | — | Draft | Not Started |

**各章范围**

- **M03.1 数据获取与存储**：CSV、JSON、HDF5、Parquet；原子结构数据格式（extxyz、ASE database、LMDB）；SQL（SELECT、JOIN、GROUP BY、窗口函数）；数据库基础（P1）。
- **M03.2 数据处理**：pandas 核心操作与性能；tidy data；缺失值与异常值；缩放与编码。FT 仅适用于部分内容。
- **M03.3 探索性数据分析与可视化**：描述性统计；分布分析；Pearson、Spearman 相关与互信息；可视化原则与常见误导；降维可视化（算法细节归属 M04.5）。
- **M03.4 数据划分、泄漏与分布偏移**：随机划分、分组划分、时间划分、结构相似性划分；MD 轨迹相邻帧高度相关导致的泄漏；协变量偏移、标签偏移、概念偏移；训练集与部署分布不一致的诊断方法。泄漏问题的主要归属章节。
- **M03.5 时间序列**：平稳性与自相关；滑动窗口特征；趋势与季节性；变化点检测；非均匀与对数时间采样下的分析方法。
- **M03.6 实验设计（DOE）**：因子设计与部分因子设计；响应面方法；拉丁超立方采样；DOE 与主动学习、贝叶斯优化的关系。DOE 的主要归属章节。

<!-- AUTO:chapters:end -->

六章讲义与实例 notebook 已按模块建设并逐章执行、渲染；建设状态与学习状态分别维护。数据存储实例需 `uv sync --extra perf --extra data` 安装声明的可选依赖。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 对 SECOM 等公开数据集独立完成一份 EDA 报告（数据质量、分布、相关性、建模建议）；
- 用公开 MD 轨迹数据比较“随机划分”与“按轨迹/时间块划分”的验证误差，用数据说明泄漏的影响；
- 对一条合成的老化型时间序列，比较线性与对数时间采样下的趋势估计与变化点检测效果。

## 研究锚点

- **A2**：主动学习为什么会失效：探索器与目标构型分布不匹配、不确定性估计不准、标注设置不一致
- **A5**：老化轨迹的时间序列分析：对数时间采样、漂移、变化点

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。

## 实例 notebook

每章配一个带运行结果的实例讲解 notebook，放在 `notebooks/` 目录，与讲义同名；章节表中“notebook”链接指向它。在 VS Code 中打开即可逐单元运行，改动后用 `make nb M=03` 重新执行并保存输出。
