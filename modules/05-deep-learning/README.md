# Module 05：深度学习（Deep Learning）

模块优先级 `P0` · 估算学时 50–70 h

## 定位

不依赖高级封装，独立完成完整的 PyTorch 训练流程，并深入理解自动微分。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M05.1 | 神经网络基础<br>Neural Network Fundamentals | P0 | M02.2, M04.2 | — | Planned | Not Started |
| M05.2 | 自动微分<br>Automatic Differentiation | P0 | M02.2, M05.1 | A1 | Planned | Not Started |
| M05.3 | PyTorch 工程基础<br>PyTorch Engineering Basics | P0 · FT | M01.1, M05.1 | — | Planned | Not Started |
| M05.4 | 训练与优化技巧<br>Training and Optimization Techniques | P0 | M05.3, M02.5 | — | Planned | Not Started |
| M05.5 | 卷积网络与视觉<br>Convolutional Networks and Vision | P1 | M05.4 | — | Planned | Not Started |
| M05.6 | 序列模型<br>Sequence Models | P2 | M05.4 | — | Planned | Not Started |

**各章范围**

- **M05.1 神经网络基础**：感知机与 MLP；激活函数；损失函数与最大似然的关系；反向传播；梯度消失与爆炸；初始化。
- **M05.2 自动微分**：计算图；前向模式与反向模式；向量–Jacobian 积与 Jacobian–向量积；高阶导数与 create_graph；力作为能量的负梯度、应力作为能量对应变的导数；JAX 的函数式自动微分简介（P2）。自动微分的主要归属章节。
- **M05.3 PyTorch 工程基础**：Tensor 与设备管理；nn.Module；Dataset 与 DataLoader；手写训练循环；checkpoint 与断点续训；随机种子与确定性。FT 仅适用于部分内容。
- **M05.4 训练与优化技巧**：优化器与学习率调度；归一化层；正则化与 Dropout；混合精度；梯度裁剪；参数 EMA；训练调试清单（loss 不下降、NaN、过拟合的排查顺序）。
- **M05.5 卷积网络与视觉**：卷积与感受野；ResNet；数据增强与迁移学习；在晶圆图与显微图像上的应用。
- **M05.6 序列模型**：RNN、LSTM、GRU 的结构与局限，作为理解 Transformer 的历史背景。Attention 归属 M06.1。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 从零实现一个标量自动微分引擎（micrograd 规模），并用它训练一个小 MLP；
- 用 PyTorch autograd 实现 Lennard-Jones 势的力与应力，与有限差分对比（相对误差小于 1e-6），并在 NVE 模拟中验证能量守恒；
- 手写训练循环，在 CPU 上于 WM-811K 子集训练 CNN，包含 checkpoint、日志与可复现设置。

## 研究锚点

- **A1**：力与应力如何由能量模型通过自动微分得到；为什么某些势在 NVE 中能量不守恒

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。

## 诊断

本模块在开始前先做诊断测评，每章得到 `Skip`、`Light` 或 `Full` 的结论。诊断题在 Phase 1b 以 QUIZ 模式生成，作答结果保存到 `progress/diagnostics/`。
