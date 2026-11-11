# Module 02：数学、统计与最优化（Mathematics, Statistics and Optimization）

模块优先级 `P0/P1` · 估算学时 90–120 h

## 定位

支撑全部 ML/DL 推导，并补齐等变网络（群论）和扩散模型（随机过程）所需的数学。M02.1–M02.6 为 P0，M02.7、M02.8 为 P1（AI for Science 必修）。按 12 个月计划，M02.1–M02.4 与 M04.1–M04.3 交替学习，不要求修完全部数学再开始机器学习。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M02.1 | 线性代数<br>Linear Algebra | P0 | — | A4 | Planned | Not Started |
| M02.2 | 微积分与矩阵微积分<br>Calculus and Matrix Calculus | P0 | M02.1 | A1 | Planned | Not Started |
| M02.3 | 概率论与信息论<br>Probability and Information Theory | P0 | M02.2 | — | Planned | Not Started |
| M02.4 | 数理统计<br>Mathematical Statistics | P0 | M02.3 | — | Planned | Not Started |
| M02.5 | 最优化<br>Optimization | P0 | M02.1, M02.2 | — | Planned | Not Started |
| M02.6 | 数值方法<br>Numerical Methods | P0 | M02.1, M02.2 | A1, A4 | Planned | Not Started |
| M02.7 | 群论与表示论<br>Group Theory and Representation Theory | P1 | M02.1 | A6 | Planned | Not Started |
| M02.8 | 随机过程与采样<br>Stochastic Processes and Sampling | P1 | M02.3, M02.6 | A6 | Planned | Not Started |

**各章范围**

- **M02.1 线性代数**：向量空间、子空间与正交投影；特征分解；SVD 与低秩近似；PCA 的两种推导（最大方差与最小重构误差）；正定矩阵；矩阵范数与条件数。
- **M02.2 微积分与矩阵微积分**：梯度、Jacobian、Hessian；矩阵形式的链式法则；常用矩阵求导结果；Taylor 展开；Lagrange 乘子。
- **M02.3 概率论与信息论**：随机变量与分布；条件概率与贝叶斯定理；多元高斯分布的边缘与条件分布（高斯过程的基础）；期望、方差、协方差；变量变换公式（normalizing flow 的基础）；熵、交叉熵、KL 散度、互信息。
- **M02.4 数理统计**：点估计、MLE、MAP；估计量的偏差与方差；置信区间；假设检验与多重比较校正；Bootstrap；贝叶斯推断入门。
- **M02.5 最优化**：凸集与凸函数；梯度下降与 SGD 的收敛直觉；Momentum、Adam、AdamW；二阶与拟牛顿方法（L-BFGS，及其在结构优化中的应用）；约束优化与 KKT 条件。贝叶斯优化归属 M06.5。
- **M02.6 数值方法**：浮点误差、条件数与数值稳定性；线性方程组（LU、Cholesky、共轭梯度）；稀疏矩阵存储与运算；迭代特征值算法（幂迭代、Lanczos）；插值与数值积分；ODE 积分器（Euler、Runge–Kutta、Verlet 与辛积分的能量守恒性质）；PDE 离散入门（有限差分、有限元的基本思想）。
- **M02.7 群论与表示论**：群、子群、陪集；对称群、SO(3)、O(3)、E(3)；群表示与不可约表示；球谐函数；Wigner-D 矩阵；张量积与 Clebsch–Gordan 分解；晶体点群与空间群简介。本章是 M06.3 的直接前置。
- **M02.8 随机过程与采样**：Markov 链与平稳分布；MCMC（Metropolis–Hastings）；Langevin 动力学与 Fokker–Planck 方程；随机微分方程入门；重要性采样。本章是连接分子动力学采样与扩散模型（M06.4）的桥梁。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 用 SVD 实现 PCA，并与 scikit-learn 结果对齐（考虑符号不确定性）；
- 手推两层 MLP 的反向传播，并用有限差分梯度检验验证实现；
- 实现共轭梯度法与 Lanczos 算法，在稀疏对称矩阵上与 SciPy 结果对比；
- 实现实球谐函数，并用随机旋转数值验证其在 Wigner-D 矩阵下的变换关系；
- 在二维双势阱上实现 Langevin 采样，与 Boltzmann 分布的解析结果比较；
- （可选）用核多项式方法（KPM）计算一维无序紧束缚模型的 DOS，并与精确对角化对比。

## 研究锚点

- **A1**：力与应力如何由能量模型通过自动微分得到；为什么某些势在 NVE 中能量不守恒
- **A4**：大尺度无序体系的电子结构：带尾、局域化与大规模稀疏矩阵的数值方法
- **A6**：晶体生成与电荷密度预测：扩散模型如何处理周期性与对称性，如何评价生成质量

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。

## 实例 notebook

每章配一个带运行结果的实例讲解 notebook，放在 `notebooks/` 目录，与讲义同名；章节表中“notebook”链接指向它。在 VS Code 中打开即可逐单元运行，改动后用 `make nb M=02` 重新执行并保存输出。
