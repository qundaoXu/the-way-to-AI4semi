# Module 01：计算机基础（Computer Science Foundations）

模块优先级 `P0` · 估算学时 30–45 h

## 定位

从“能跑的科研脚本”提升到“可维护、可测试、性能可分析的 Python 项目”。本模块多处是 Fast-track 候选（`FT`）：已经熟悉的章节可以只浏览精要，运行一遍实例 notebook 即可。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M01.1 | Python 进阶<br>Advanced Python | P0 · FT | — | — | Planned | Not Started |
| M01.2 | 数据结构与算法（科学计算取向）<br>Data Structures and Algorithms for Scientific Computing | P0 | M01.1 | — | Planned | Not Started |
| M01.3 | 开发工具链<br>Development Toolchain | P0 · FT | — | — | Planned | Not Started |
| M01.4 | 计算机系统基础<br>Computer Systems Basics | P1 | M01.1 | — | Planned | Not Started |
| M01.5 | 高性能科学 Python<br>High-Performance Scientific Python | P0 | M01.1 | — | Planned | Not Started |

**各章范围**

- **M01.1 Python 进阶**：数据模型与 Pythonic 写法；迭代器、生成器与惰性计算；装饰器与闭包；上下文管理器；dataclass 与类型注解；包、模块与导入机制；异常设计；科学数据序列化（JSON、HDF5、extxyz）及 pickle 的安全与兼容性问题。
- **M01.2 数据结构与算法（科学计算取向）**：时间与空间复杂度；数组、哈希表、堆、树、图；排序与搜索；递归、分治、动态规划与贪心基础。领域例题：周期性边界条件下的最小镜像约定；cell list 与 KD-tree 邻居搜索；用连通分量与最短路计算键网络的团簇与环统计。面试刷题部分为 P2。
- **M01.3 开发工具链**：Linux 与 Shell 脚本；Git 进阶（分支策略、rebase、bisect、冲突处理）；环境与依赖管理（uv、conda）；调试（pdb、IDE 调试器）；日志；pytest；ruff；pre-commit。FT 仅适用于部分内容。
- **M01.4 计算机系统基础**：存储层次与缓存局部性；进程、线程与 GIL；并发与 multiprocessing；I/O 瓶颈；IEEE 754 浮点表示与舍入误差；网络与 HTTP/API 基础（P2）。
- **M01.5 高性能科学 Python**：NumPy 内存布局与 strides；广播与向量化；einsum；避免隐式拷贝；cProfile、line_profiler 性能分析；Numba 入门。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 把一个自己的旧科研脚本重构为可安装的包：包含命令行入口、配置文件、日志、至少 5 个单元测试，并通过 `ruff` 检查；
- 从零实现 cell list 邻居搜索（含周期性边界），与 ASE 的邻居表结果一致，并给出理论复杂度与实测 scaling 曲线；
- 对一段向量化前后的代码给出性能分析报告，说明加速来源。

## 研究锚点

- **A4**：大尺度无序体系的电子结构：带尾、局域化与大规模稀疏矩阵的数值方法

大体系数据处理的性能问题是本模块的主要动机。

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。

## 实例 notebook

每章配一个带运行结果的实例讲解 notebook，放在 `notebooks/` 目录，与讲义同名；章节表中“notebook”链接指向它。在 VS Code 中打开即可逐单元运行，改动后用 `make nb M=01` 重新执行并保存输出。
