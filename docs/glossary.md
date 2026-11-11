# 中英术语表

讲义中的术语以本表为准。英文术语在讲义里首次出现时附上；新术语随所在章节的建设补充进来，并注明归属章节。领域内已经通用英文的名称（如 Ridge、Lasso、Transformer）保留英文。

目前收录的是 Module 01、试点章节 M04.2 和仓库工作流用到的术语。

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
| 快速通过 | fast-track (FT) | 已熟悉者可只浏览精要、运行实例 notebook 的章节 |
| 按模块建设 | module-wise build | 一次建设一个模块的全部章节，建完交学习者过目（取代原先“最多领先两章”的即时建设） |
| 实例 notebook | worked-example notebook | 每章一个、带执行输出提交的 `.ipynb`，逐步讲解代码 |
| 概念归属 | concept ownership | 同一概念只在一个章节系统讲解，其他章节用链接引用 |
| 批注 | annotation | 写在讲义源文件中的 `.anno-*` callout |
