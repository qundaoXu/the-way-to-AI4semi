# Module 11：高性能计算与 GPU（HPC and GPU Computing）

模块优先级 `P1/P2` · 估算学时 30–50 h

## 定位

定位性能瓶颈，掌握集群与多 GPU 环境下的 ML 训练和 ML 势模拟工作流。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M11.1 | 并行计算基础与性能分析<br>Parallel Computing Basics and Performance Analysis | P1 | M01.4 | A7 | Planned | Not Started |
| M11.2 | GPU 编程<br>GPU Programming | P2 | M11.1, M05.3 | — | Planned | Not Started |
| M11.3 | 分布式与多 GPU 训练<br>Distributed and Multi-GPU Training | P2 | M11.2 | — | Planned | Not Started |
| M11.4 | 集群工作流<br>Cluster Workflows | P1 · FT | M01.3 | — | Planned | Not Started |

**各章范围**

- **M11.1 并行计算基础与性能分析**：CPU 与 GPU 架构；存储层次与带宽瓶颈；Roofline 模型的直觉；性能分析方法论。
- **M11.2 GPU 编程**：CUDA 编程模型；PyTorch Profiler；显存管理；混合精度的数值问题；Triton 入门（P3）。
- **M11.3 分布式与多 GPU 训练**：multiprocessing；MPI 基础；PyTorch DDP；大模型训练的并行策略概览。
- **M11.4 集群工作流**：Slurm 与作业数组；容器（Apptainer）；ML 势在 LAMMPS 中的 GPU 性能瓶颈分析。FT 仅适用于部分内容。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 对一个 ML 势的 MD 模拟或训练任务给出性能分析报告：定位瓶颈（计算、显存、通信、I/O），提出并验证至少一项优化。

## 研究锚点

蓝图的锚点表把 A7 关联到 M11.1（见章节表）；模块本身没有单独指定锚点。
