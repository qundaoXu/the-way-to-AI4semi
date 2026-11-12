# 中英术语表

讲义中的术语以本表为准。英文术语在讲义里首次出现时附上；新术语随所在章节的建设补充进来，并注明归属章节。领域内已经通用英文的名称（如 Ridge、Lasso、Transformer）保留英文。

术语随已建设章节更新；概念的系统讲解以“归属章节”为准。

## 计算机基础

| 中文 | English | 说明 | 归属章节 |
|---|---|---|---|
| 协议 | protocol | 由一组特殊方法定义的行为约定，如序列协议、迭代器协议、上下文管理协议 | M01.1 |
| 特殊方法 | special (dunder) method | `__len__`、`__getitem__` 等由解释器在类型上查找并调用的方法 | M01.1 |
| 生成器 | generator | 含 `yield` 的函数返回的惰性迭代器，只能遍历一次 | M01.1 |
| 惰性计算 | lazy evaluation | 需要时才产生数据，内存与数据总量无关 | M01.1 |
| 闭包 | closure | 嵌套函数连同其捕获的外层变量 | M01.1 |
| 后期绑定 | late binding | 闭包在调用时才读取所捕获变量的当前值 | M01.1 |
| 装饰器 | decorator | 接收函数并返回新函数的可调用对象，`@d` 等价于 `f = d(f)` | M01.1 |
| 上下文管理器 | context manager | 实现 `__enter__`/`__exit__`，保证资源获取与释放配对 | M01.1 |
| 往返精度 | round-trip precision | 写出再读回后数值完全相等所需的有效数字（float64 为 17 位） | M01.1 |
| 摊还复杂度 | amortized complexity | 一串操作的总代价除以操作次数，例如 `list.append` | M01.2 |
| 最小镜像约定 | minimum image convention | 周期性边界下只取最近的镜像计算位移；要求 $r_c \le L/2$（三斜盒子用面间距） | M01.2 |
| 格子链表法 | cell list (linked-cell) | 把盒子分成边长不小于 $r_c$ 的格子，只比较相邻格子；固定密度下为 $O(N)$ | M01.2 |
| Verlet 邻居表 | Verlet list | 用 $r_c$ 加一层 skin 建邻居表，若干步后再重建 | M01.2 |
| KD 树 | KD-tree | 按坐标递归二分空间的树，用于范围查询和最近邻查询 | M01.2 |
| 连通分量 | connected component | 图中彼此可达的节点集合，对应原子团簇 | M01.2 |
| 逾渗阈值 | percolation threshold | 最大团簇开始贯通体系时的占据概率 | M01.2 |
| 环统计 | ring statistics | 网络中环大小的分布，结果依赖环的定义 | M01.2 |
| 内容寻址 | content addressing | 对象以内容的哈希命名，Git 的存储模型 | M01.3 |
| 合并基 | merge base | 两分支最近的公共祖先，三方合并的基准 | M01.3 |
| 变基 | rebase | 把提交重放到新的父提交上，生成新提交 | M01.3 |
| 引用日志 | reflog | 本地记录分支指针移动的历史，用于找回提交 | M01.3 |
| 二分定位 | bisect | 在提交历史上二分查找引入回归的提交 | M01.3 |
| 锁文件 | lockfile | 记录精确依赖版本与哈希的文件，如 `uv.lock` | M01.3 |
| 事后调试 | post-mortem debugging | 异常发生后进入崩溃现场的栈帧检查变量 | M01.3 |
| 缓存行 | cache line | 内存与缓存之间搬运数据的最小单位（常见 64 或 128 B） | M01.4 |
| 空间局部性 / 时间局部性 | spatial / temporal locality | 访问邻近地址 / 重复访问同一数据的倾向 | M01.4 |
| 机器精度 | machine epsilon | 1 与下一个可表示浮点数之差，$2^{1-p}$ | M01.4 |
| 单位舍入误差 | unit roundoff | 单次运算的最大相对误差 $u = \varepsilon/2$ | M01.4 |
| 灾难性抵消 | catastrophic cancellation | 相近数相减，使前序误差按条件数放大 | M01.4 |
| 补偿求和 | Kahan (compensated) summation | 记录并补回舍入低位的求和算法 | M01.4 |
| 成对求和 | pairwise summation | 二分递归求和，误差约随 $\log n$ 增长 | M01.4 |
| 全局解释器锁 | global interpreter lock (GIL) | CPython 中同一时刻只允许一个线程执行字节码 | M01.4 |
| 超额订阅 | oversubscription | 线程总数超过核数导致变慢 | M01.4 |
| 启动方式 | start method (spawn / fork / forkserver) | `multiprocessing` 创建子进程的方式 | M01.4 |
| 步长 | strides | 沿各轴移动一个元素所跨的字节数 | M01.5 |
| 视图 | view | 共享原数组内存、只改元数据的数组 | M01.5 |
| 广播 | broadcasting | 按形状规则自动对齐、拉伸维度的逐元素运算 | M01.5 |
| 临时数组复用 | temporary elision | NumPy 复用无引用的中间结果数组 | M01.5 |
| 即时编译 | just-in-time (JIT) compilation | 首次调用时按参数类型编译为机器码（如 Numba） | M01.5 |
| 性能分析 | profiling | 测量时间或内存花在哪里 | M01.5 |

## 数学、统计与最优化

| 中文 | English | 说明 | 归属章节 |
|---|---|---|---|
| 列空间 / 零空间 | column space / null space | 线性映射可表示的输出 / 被映射为零的输入方向 | M02.1 |
| 奇异值分解 | singular value decomposition (SVD) | 将线性映射分解为正交方向和非负缩放 | M02.1 |
| 主成分分析 | principal component analysis (PCA) | 中心化数据上的最大方差子空间，等价于最小正交重构误差 | M02.1 |
| 正定矩阵 | positive-definite matrix | 对称矩阵的二次型对所有非零向量严格为正 | M02.1 |
| 方向导数 | directional derivative | 沿指定方向的一阶变化率 | M02.2 |
| Jacobian 矩阵 | Jacobian matrix | 输出分量对输入分量的偏导矩阵，本仓库采用分子布局 | M02.2 |
| Hessian 矩阵 | Hessian matrix | 标量函数的二阶偏导矩阵 | M02.2 |
| Lagrange 乘子 | Lagrange multiplier | 描述约束极值点梯度法向平衡的变量，需要正则条件 | M02.2、M02.5 |
| 边缘化 / 条件化 | marginalization / conditioning | 对未知变量积分，或利用已知观测更新其余变量 | M02.3 |
| KL 散度 | Kullback–Leibler divergence | 有方向的分布差异，一般不对称，也不满足距离的三角不等式 | M02.3 |
| 互信息 | mutual information | 联合分布相对于边缘乘积的 KL，衡量统计依赖 | M02.3 |
| 估计量 | estimator | 依赖随机数据、用于估计参数的统计量 | M02.4 |
| 标准误 | standard error | 估计量抽样分布的标准差 | M02.4 |
| 置信区间 | confidence interval | 重复构造时具有目标覆盖率的随机区间 | M02.4 |
| 可信区间 | credible interval | 给定数据与先验后包含指定后验概率质量的参数区间 | M02.4 |
| 自助法 | bootstrap | 对经验分布重采样以近似统计量的抽样波动 | M02.4 |
| 错误发现率 | false discovery rate (FDR) | 发现中错误拒绝比例的期望，区别于家族误报率 FWER | M02.4 |
| 强凸性 | strong convexity | 目标具有严格二次下界，常支持唯一解与更强收敛保证 | M02.5 |
| 预条件 | preconditioning | 在不改变目标解的前提下改善求解过程的尺度或谱分布 | M02.5、M02.6 |
| 解耦权重衰减 | decoupled weight decay | 权重衰减独立于自适应梯度矩估计的更新方式 | M02.5 |
| 互补松弛 | complementary slackness | KKT 中不等式乘子与对应约束值的乘积为零 | M02.5 |
| 后向稳定性 | backward stability | 数值输出可看作轻微扰动输入后的精确结果 | M02.6 |
| Krylov 子空间 | Krylov subspace | 由起始向量及矩阵反复作用张成的子空间 | M02.6 |
| Ritz 值 | Ritz value | 原矩阵在子空间投影后的特征值近似 | M02.6 |
| 辛积分 | symplectic integration | 保持 Hamiltonian 辛结构的离散方法，不等于精确能量守恒 | M02.6 |
| 群表示 | group representation | 把群元素映射为保持复合规律的可逆线性映射 | M02.7 |
| 不可约表示 | irreducible representation (irrep) | 不含对所有群作用均封闭的非平凡真子空间的表示 | M02.7 |
| 陪集 | coset | 用某个群元素平移一个子群得到的集合 | M02.7 |
| 宇称 | parity | 特征在空间反演下的变换符号，区分 O(3) 表示 | M02.7 |
| 球谐函数 | spherical harmonics | 球面角向基函数，固定阶数形成旋转封闭块 | M02.7 |
| Clebsch–Gordan 分解 | Clebsch–Gordan decomposition | 将表示的张量积分解为不可约表示直和 | M02.7 |
| 平稳分布 | stationary distribution | 经转移核作用后不变的概率分布 | M02.8 |
| 详细平衡 | detailed balance | 平衡态下任意两状态的正反向概率流相等 | M02.8 |
| 混合 | mixing | 链从初态接近平稳分布并探索目标区域的过程 | M02.8 |
| 有效样本量 | effective sample size (ESS) | 针对给定观测量衡量相关性或权重集中导致的信息损失 | M02.8 |
| 重要性采样 | importance sampling | 从提议分布采样，用密度比纠正期望估计 | M02.8 |

## 数据科学

| 中文 | English | 说明 | 归属章节 |
|---|---|---|---|
| 模式 / 数据契约 | schema / data contract | 字段类型、单位、键与有效范围的明确约定 | M03.1 |
| 列式存储 | columnar storage | 按列组织数据，便于只读所需变量与压缩 | M03.1 |
| 分块 | chunking | 将数组分成独立存储与压缩的块 | M03.1 |
| 事务快照 | transaction snapshot | 一次读取保持一致的数据库视图 | M03.1 |
| 整洁数据 | tidy data | 每变量一列、每观测一行，依赖明确的观测单位 | M03.2 |
| 关联基数 | join cardinality | 一对一、一对多或多对多的键匹配关系 | M03.2 |
| 完全随机缺失 | missing completely at random (MCAR) | 缺失与观测和未观测变量均独立 | M03.2 |
| 随机缺失 | missing at random (MAR) | 给定已观测量后，缺失不再依赖未观测值 | M03.2 |
| 非随机缺失 | missing not at random (MNAR) | 给定观测后缺失仍依赖未观测因素 | M03.2 |
| 经验分布函数 | empirical cumulative distribution function (ECDF) | 阈值以下观测比例的阶梯函数 | M03.3 |
| 秩相关 | rank correlation | 对排序后的秩衡量单调关联 | M03.3 |
| 分组划分 | group split | 以独立组为集合边界，避免同组跨集合 | M03.4 |
| 协变量偏移 | covariate shift | 输入边缘分布变化而条件标签分布不变 | M03.4 |
| 标签偏移 | label shift | 标签先验变化而类别条件输入分布不变 | M03.4 |
| 概念偏移 | concept shift | 条件标签机制发生变化 | M03.4 |
| 弱平稳 | weak stationarity | 有限二阶矩且均值恒定、协方差只依赖滞后 | M03.5 |
| 自相关函数 | autocorrelation function (ACF) | 同一过程不同滞后值的相关 | M03.5 |
| 变化点 | change point | 指定分布或动态机制发生变化的位置 | M03.5 |
| 因子设计 | factorial design | 组合多个输入水平以分离主效应和交互 | M03.6 |
| 混杂 / 别名 | confounding / aliasing | 设计点上多个效应不可独立区分 | M03.6 |
| 响应面 | response surface | 以局部回归近似输入到响应的关系 | M03.6 |
| 拉丁超立方采样 | Latin hypercube sampling (LHS) | 每个输入边缘的等概率分层各取一个点 | M03.6 |

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

## 传统机器学习补充

| 中文 | English | 说明 | 归属章节 |
|---|---|---|---|
| 经验风险最小化 | empirical risk minimization (ERM) | 在函数类内最小化训练样本平均损失 | M04.1 |
| 归纳偏置 | inductive bias | 学习器对函数、表示或解的结构偏好 | M04.1 |
| 再生核 Hilbert 空间 | reproducing kernel Hilbert space (RKHS) | 具有核截面再生取值性质的函数空间 | M04.3 |
| Gram 矩阵 | Gram matrix | 样本两两内积或核值形成的矩阵 | M04.3 |
| 高斯过程 | Gaussian process (GP) | 任意有限组函数值联合高斯的随机函数 | M04.3 |
| 边缘似然 | marginal likelihood | 对潜变量积分后的观测似然 | M04.3 |
| 支持向量 | support vector | 对间隔分类边界具有非零对偶作用的样本 | M04.3 |
| 装袋 | bootstrap aggregating (Bagging) | 对重采样基模型平均以降低波动 | M04.4 |
| 梯度提升 | gradient boosting | 逐轮拟合负损失梯度的加性模型 | M04.4 |
| 袋外估计 | out-of-bag (OOB) estimation | 用未包含某行的 bootstrap 模型评价该行 | M04.4 |
| 责任度 | responsibility | 混合模型中给定观测的分量后验概率 | M04.5 |
| 期望最大化 | expectation maximization (EM) | 交替更新隐变量后验与参数的下界优化 | M04.5 |
| 密度连通 | density connectivity | 通过核心点邻域链连接的密度聚类关系 | M04.5 |
| 调整 Rand 指数 | adjusted Rand index (ARI) | 对随机一致性调整的聚类标签相似度 | M04.5 |
| 新颖性检测 | novelty detection | 基于相对干净参考判断新样本的偏离 | M04.6 |
| 局部异常因子 | local outlier factor (LOF) | 邻居与自身局部可达密度比的平均 | M04.6 |
| 嵌套交叉验证 | nested cross-validation | 内层选择、外层评价完整选择流程 | M04.7 |
| 置换重要性 | permutation importance | 打乱特征后指定评分的下降 | M04.7 |
| Shapley 值 | Shapley value | 特征在所有加入顺序中的平均边际贡献 | M04.7 |
| 消融 | ablation | 为隔离指定组件作用而构造的受控比较 | M04.8 |
| 伪重复 | pseudoreplication | 将相关或重复观测误当独立证据单位 | M04.8 |
| 赢家偏差 | winner's curse / selection optimism | 从带噪候选中选择最佳导致的乐观偏差 | M04.8 |

## 深度学习

| 中文 | English | 说明 | 归属章节 |
|---|---|---|---|
| 多层感知机 | multilayer perceptron (MLP) | 仿射层与非线性激活组成的可学习表示 | M05.1 |
| 预激活 | preactivation | 进入激活函数之前的仿射输出 | M05.1 |
| 反向传播 | backpropagation | 按依赖逆序组织链式法则和贡献累加 | M05.1、M05.2 |
| 自动微分 | automatic differentiation (AD) | 对实际基本运算应用已知导数规则 | M05.2 |
| Jacobian–向量积 | Jacobian-vector product (JVP) | 将输入切向量传播为 Jv | M05.2 |
| 向量–Jacobian 积 | vector-Jacobian product (VJP) | 将输出余切传播为 Jᵀu | M05.2 |
| 可微梯度图 | derivative graph / create_graph | 使导数运算本身仍可继续求导的图 | M05.2 |
| 缓冲状态 | buffer | 随 Module 保存和迁移的非 Parameter 张量 | M05.3 |
| 检查点 | checkpoint | 支持声明边界恢复所需的模型与训练状态 | M05.3 |
| 步幅 | stride | 张量索引步进的存储偏移，或卷积空间步进；按语境区分 | M05.3、M05.5 |
| 预热 | warmup | 初期逐渐增加学习率的调度阶段 | M05.4 |
| 梯度裁剪 | gradient clipping | 按预定范数或范围限制梯度大小 | M05.4 |
| 指数移动平均 | exponential moving average (EMA) | 对参数或统计量作递推指数加权平均 | M05.4 |
| 自动混合精度 | automatic mixed precision (AMP) | 按算子选择精度并可配合梯度缩放 | M05.4 |
| 感受野 | receptive field | 某输出在输入中可能依赖的区域 | M05.5 |
| 残差连接 | residual connection | 通过恒等或投影捷径叠加分支输出 | M05.5 |
| 冻结特征 | frozen feature extraction | 固定表示参数，仅训练下游头部 | M05.5 |
| 时间反向传播 | backpropagation through time (BPTT) | 在时间展开的共享参数图上反向传播 | M05.6 |
| 门控 | gating | 用数据依赖系数控制状态保留与更新 | M05.6 |
| 截断 BPTT | truncated BPTT | 保留状态值但在块边界切断历史梯度 | M05.6 |
| 教师强制 | teacher forcing | 训练时使用真实前步输出作为递推输入 | M05.6 |

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
| 快速通过 | fast-track (FT) | 已熟悉者可只浏览精要、运行实例 notebook 的章节 |
| 按模块建设 | module-wise build | 一次建设一个模块的全部章节，建完交学习者过目（取代原先“最多领先两章”的即时建设） |
| 实例 notebook | worked-example notebook | 每章一个、带执行输出提交的 `.ipynb`，逐步讲解代码 |
| 概念归属 | concept ownership | 同一概念只在一个章节系统讲解，其他章节用链接引用 |
| 批注 | annotation | 写在讲义源文件中的 `.anno-*` callout |
