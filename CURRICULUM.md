# 课程总目录

<!-- 本文件由 scripts/sync_index.py 生成，请勿手工编辑。修改 curriculum.yaml 或讲义 frontmatter 后运行 `make sync`。 -->

共 12 个模块、73 章，其中 6 章已建设（建设状态为 Draft 及以上）。只有已建设的章节带讲义链接。

优先级：`P0` 核心必修，`P1` 主线进阶，`P2` 拓展，`P3` 长期专题，`Branch` 分支内容；`FT` 表示已熟悉者可快速浏览的章节（只看精要与实例 notebook）。两种状态的含义见 [学习指南](docs/learning-guide.md)。

## M01 计算机基础（Computer Science Foundations）

模块优先级 `P0` · 估算学时 30–45 h · 锚点 A4 · [模块说明](modules/01-cs-foundations/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M01.1 | [Python 进阶](modules/01-cs-foundations/notes/01-advanced-python.qmd) · [notebook](modules/01-cs-foundations/notebooks/01-advanced-python.ipynb)<br>Advanced Python | P0 · FT | — | — | Draft | Not Started |
| M01.2 | [数据结构与算法（科学计算取向）](modules/01-cs-foundations/notes/02-data-structures-algorithms.qmd) · [notebook](modules/01-cs-foundations/notebooks/02-data-structures-algorithms.ipynb)<br>Data Structures and Algorithms for Scientific Computing | P0 | M01.1 | — | Draft | Not Started |
| M01.3 | [开发工具链](modules/01-cs-foundations/notes/03-dev-toolchain.qmd) · [notebook](modules/01-cs-foundations/notebooks/03-dev-toolchain.ipynb)<br>Development Toolchain | P0 · FT | — | — | Draft | Not Started |
| M01.4 | [计算机系统基础](modules/01-cs-foundations/notes/04-computer-systems.qmd) · [notebook](modules/01-cs-foundations/notebooks/04-computer-systems.ipynb)<br>Computer Systems Basics | P1 | M01.1 | — | Draft | Not Started |
| M01.5 | [高性能科学 Python](modules/01-cs-foundations/notes/05-high-performance-python.qmd) · [notebook](modules/01-cs-foundations/notebooks/05-high-performance-python.ipynb)<br>High-Performance Scientific Python | P0 | M01.1 | — | Draft | Not Started |

## M02 数学、统计与最优化（Mathematics, Statistics and Optimization）

模块优先级 `P0/P1` · 估算学时 90–120 h · 锚点 A1, A4, A6 · [模块说明](modules/02-mathematics-statistics/README.md)

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

## M03 数据科学（Data Science）

模块优先级 `P0` · 估算学时 30–40 h · 锚点 A2, A5 · [模块说明](modules/03-data-science/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M03.1 | 数据获取与存储<br>Data Acquisition and Storage | P0 | — | — | Planned | Not Started |
| M03.2 | 数据处理<br>Data Wrangling | P0 · FT | M03.1 | — | Planned | Not Started |
| M03.3 | 探索性数据分析与可视化<br>Exploratory Data Analysis and Visualization | P0 | M03.2, M02.3 | — | Planned | Not Started |
| M03.4 | 数据划分、泄漏与分布偏移<br>Data Splitting, Leakage and Distribution Shift | P0 | M03.2, M04.1 | A2 | Planned | Not Started |
| M03.5 | 时间序列<br>Time Series | P1 | M03.2, M02.4 | A5 | Planned | Not Started |
| M03.6 | 实验设计（DOE）<br>Design of Experiments | P1 | M02.4 | — | Planned | Not Started |

## M04 传统机器学习（Classical Machine Learning）

模块优先级 `P0` · 估算学时 60–80 h · 锚点 A3 · [模块说明](modules/04-classical-machine-learning/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M04.1 | 统计学习基础<br>Statistical Learning Foundations | P0 | M02.1, M02.3 | — | Planned | Not Started |
| M04.2 | [线性模型](modules/04-classical-machine-learning/notes/02-linear-models.qmd) · [notebook](modules/04-classical-machine-learning/notebooks/02-linear-models.ipynb)<br>Linear Models | P0 | M02.1, M02.2, M02.4 | — | Draft | Not Started |
| M04.3 | 核方法与高斯过程<br>Kernel Methods and Gaussian Processes | P0 | M04.2, M02.3 | — | Planned | Not Started |
| M04.4 | 树模型与集成学习<br>Trees and Ensemble Learning | P0 | M04.1 | — | Planned | Not Started |
| M04.5 | 无监督学习<br>Unsupervised Learning | P0 | M02.1, M02.3 | — | Planned | Not Started |
| M04.6 | 异常检测<br>Anomaly Detection | P1 | M04.4, M04.5 | — | Planned | Not Started |
| M04.7 | 模型评价与解释<br>Model Evaluation and Interpretation | P0 | M04.1, M04.2 | A3 | Planned | Not Started |
| M04.8 | ML 研究方法论<br>ML Research Methodology | P0 | M04.7, M02.4 | A3 | Planned | Not Started |

## M05 深度学习（Deep Learning）

模块优先级 `P0` · 估算学时 50–70 h · 锚点 A1 · [模块说明](modules/05-deep-learning/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M05.1 | 神经网络基础<br>Neural Network Fundamentals | P0 | M02.2, M04.2 | — | Planned | Not Started |
| M05.2 | 自动微分<br>Automatic Differentiation | P0 | M02.2, M05.1 | A1 | Planned | Not Started |
| M05.3 | PyTorch 工程基础<br>PyTorch Engineering Basics | P0 · FT | M01.1, M05.1 | — | Planned | Not Started |
| M05.4 | 训练与优化技巧<br>Training and Optimization Techniques | P0 | M05.3, M02.5 | — | Planned | Not Started |
| M05.5 | 卷积网络与视觉<br>Convolutional Networks and Vision | P1 | M05.4 | — | Planned | Not Started |
| M05.6 | 序列模型<br>Sequence Models | P2 | M05.4 | — | Planned | Not Started |

## M06 现代 AI 架构（Advanced AI Architectures）

模块优先级 `P1` · 估算学时 70–90 h · 锚点 A2, A6 · [模块说明](modules/06-advanced-ai/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M06.1 | Attention 与 Transformer<br>Attention and Transformer | P1 | M05.4 | — | Planned | Not Started |
| M06.2 | 图神经网络基础<br>Graph Neural Network Basics | P1 | M05.4 | — | Planned | Not Started |
| M06.3 | 几何与等变深度学习<br>Geometric and Equivariant Deep Learning | P1 | M02.7, M06.2 | — | Planned | Not Started |
| M06.4 | 生成模型<br>Generative Models | P1 | M02.3, M02.8, M05.4 | A6 | Planned | Not Started |
| M06.5 | 不确定性量化、主动学习与贝叶斯优化<br>Uncertainty Quantification, Active Learning and Bayesian Optimization | P1 | M04.3, M04.7, M05.4 | A2 | Planned | Not Started |
| M06.6 | 表征学习与迁移<br>Representation Learning and Transfer | P2 | M05.4 | — | Planned | Not Started |

## M07 科学机器学习（Scientific Machine Learning）

模块优先级 `P1` · 估算学时 120 h 以上 · 锚点 A1, A2, A3, A4, A6, A8 · [模块说明](modules/07-scientific-machine-learning/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M07.1 | AI for Science 方法论<br>AI for Science Methodology | P1 | M04.8 | — | Planned | Not Started |
| M07.2 | 原子环境表示<br>Atomic Environment Representations | P1 | M02.7, M04.3 | — | Planned | Not Started |
| M07.3 | 机器学习势：训练与验证<br>Machine Learning Interatomic Potentials: Training and Validation | P1 · FT | M03.4, M05.2, M06.3 | A1, A2, A3 | Planned | Not Started |
| M07.4 | 通用势与材料基础模型<br>Universal Potentials and Materials Foundation Models | P1 | M07.3, M06.5 | A2 | Planned | Not Started |
| M07.5 | 电子结构机器学习<br>Machine Learning for Electronic Structure | P1 | M02.6, M06.3 | A4, A6 | Planned | Not Started |
| M07.6 | 晶体与材料生成模型<br>Generative Models for Crystals and Materials | P1 | M06.3, M06.4 | A6 | Planned | Not Started |
| M07.7 | 物理信息学习<br>Physics-Informed Learning | P2 | M02.6, M05.2 | — | Planned | Not Started |
| M07.8 | 神经算子<br>Neural Operators | P2 | M02.6, M05.4 | A8 | Planned | Not Started |
| M07.9 | 多尺度、可微分模拟与逆向设计<br>Multiscale Modeling, Differentiable Simulation and Inverse Design | P2 | M05.2, M07.3 | A8 | Planned | Not Started |
| M07.10 | 器件仿真中的 AI<br>AI in Device Simulation | P2 | M07.8 | A8 | Planned | Not Started |

## M08 半导体制造数据科学（Semiconductor Manufacturing Data Science）

模块优先级 `Branch` · 估算学时 40–60 h · 锚点 A5 · [模块说明](modules/08-semiconductor-data-science/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M08.1 | 半导体制造数据<br>Semiconductor Manufacturing Data | Branch | — | — | Planned | Not Started |
| M08.2 | 过程监控<br>Process Monitoring | Branch | M02.4, M04.5 | — | Planned | Not Started |
| M08.3 | 良率与缺陷分析<br>Yield and Defect Analysis | Branch | M04.7, M05.5 | — | Planned | Not Started |
| M08.4 | 虚拟量测<br>Virtual Metrology | Branch | M03.5, M04.4 | — | Planned | Not Started |
| M08.5 | 可靠性与优化<br>Reliability and Optimization | Branch | M02.4, M03.6 | A5 | Planned | Not Started |

## M09 ML 工程与 MLOps（ML Engineering and MLOps）

模块优先级 `P1/P2` · 估算学时 30–40 h · 锚点 — · [模块说明](modules/09-ml-engineering-mlops/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M09.1 | AI 项目工程化<br>Engineering AI Projects | P1 | M01.3 | — | Planned | Not Started |
| M09.2 | 实验管理与可复现性<br>Experiment Management and Reproducibility | P1 | M09.1 | — | Planned | Not Started |
| M09.3 | 科学计算工作流编排<br>Scientific Workflow Orchestration | P2 | M09.1 | — | Planned | Not Started |
| M09.4 | 模型部署与推理<br>Model Deployment and Inference | P2 | M05.3 | — | Planned | Not Started |
| M09.5 | 生产环境 ML<br>Machine Learning in Production | P3 | M09.2, M03.4 | — | Planned | Not Started |

## M10 大语言模型、RAG 与 Agent（LLM, RAG and Agents）

模块优先级 `P2` · 估算学时 30–40 h · 锚点 — · [模块说明](modules/10-llm-rag-agents/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M10.1 | 大语言模型原理<br>Large Language Model Principles | P2 | M06.1 | — | Planned | Not Started |
| M10.2 | 检索增强生成<br>Retrieval-Augmented Generation | P2 | M10.1 | — | Planned | Not Started |
| M10.3 | Agent 系统<br>Agent Systems | P2 | M10.1 | — | Planned | Not Started |
| M10.4 | 科学 Agent<br>Scientific Agents | P2 | M10.3 | — | Planned | Not Started |
| M10.5 | 高效使用编码 Agent<br>Working Effectively with Coding Agents | P1 | — | — | Planned | Not Started |

## M11 高性能计算与 GPU（HPC and GPU Computing）

模块优先级 `P1/P2` · 估算学时 30–50 h · 锚点 — · [模块说明](modules/11-hpc-gpu-computing/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M11.1 | 并行计算基础与性能分析<br>Parallel Computing Basics and Performance Analysis | P1 | M01.4 | A7 | Planned | Not Started |
| M11.2 | GPU 编程<br>GPU Programming | P2 | M11.1, M05.3 | — | Planned | Not Started |
| M11.3 | 分布式与多 GPU 训练<br>Distributed and Multi-GPU Training | P2 | M11.2 | — | Planned | Not Started |
| M11.4 | 集群工作流<br>Cluster Workflows | P1 · FT | M01.3 | — | Planned | Not Started |

## M12 进阶与前沿专题（Advanced and Emerging Topics）

模块优先级 `P3` · 估算学时 开放 · 锚点 A7 · [模块说明](modules/12-advanced-topics/README.md)

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M12.1 | 因果机器学习<br>Causal Machine Learning | P3 | M02.4 | — | Planned | Not Started |
| M12.2 | 强化学习<br>Reinforcement Learning | P3 | M05.4 | — | Planned | Not Started |
| M12.3 | 概率机器学习<br>Probabilistic Machine Learning | P3 | M02.3, M06.5 | — | Planned | Not Started |
| M12.4 | 机器学习系统<br>Machine Learning Systems | P3 | M11.1 | — | Planned | Not Started |
| M12.5 | AI 硬件与模拟存内计算<br>AI Hardware and Analog In-Memory Computing | P2 | M05.4 | A7 | Planned | Not Started |
