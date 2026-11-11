# Module 07：科学机器学习（Scientific Machine Learning）

模块优先级 `P1` · 估算学时 120 h 以上

## 定位

长期专业主线。学习者已在其中多个方向开展研究，因此本模块重点是补全理论、理解设计取舍、建立系统的验证方法，而不是工具使用教程。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

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

**各章范围**

- **M07.1 AI for Science 方法论**：科学数据与一般工业数据的差异；物理先验与归纳偏置；对称性与守恒律；多保真数据；“可用性”验证与误差指标的区别。
- **M07.2 原子环境表示**：原子中心对称函数（ACSF）；SOAP；ACE 展开；描述符的完备性、光滑性与计算成本；截断半径的物理意义。
- **M07.3 机器学习势：训练与验证**：能量、力、应力的损失权重；训练集构建（AIMD、熔融–淬火、主动学习）；DFT 设置一致性（泛函、vdW 修正、SOC、赝势、截断能）；分层验证体系（误差指标 → MD 稳定性 → 结构、动力学与热力学性质 → 电子结构）；与 LAMMPS 的耦合方式。FT 仅适用于实践部分。
- **M07.4 通用势与材料基础模型**：通用 MLIP（如 MACE-MP-0）的训练数据与适用范围；微调、蒸馏与迁移；通用模型作为探索器或初始化时的分布问题。
- **M07.5 电子结构机器学习**：ML 哈密顿量（DeepH 类方法）的等变性设计；电荷密度预测；DOS 与能带预测；大体系电子结构的数值方法（稀疏对角化、KPM）；无序体系的局域化指标（IPR、迁移率边、Urbach 带尾）。
- **M07.6 晶体与材料生成模型**：CDVAE、DiffCSP、MatterGen 等代表性方法；分数坐标的周期性处理（环面上的扩散）；晶格与对称性的生成；生成结果的评价（有效性、稳定性、新颖性、多样性）。
- **M07.7 物理信息学习**：PINN；PDE 残差损失；初边值条件的施加方式；失败模式（谱偏置、刚性问题、损失项不平衡）；替代与改进方法。
- **M07.8 神经算子**：Fourier Neural Operator；DeepONet；算子学习的问题设定；分辨率泛化；PDE 代理模型的评价。
- **M07.9 多尺度、可微分模拟与逆向设计**：DFT → MD → 连续介质的参数传递；多保真学习；可微分模拟（如 JAX-MD）；参数反演与逆向设计；不确定性传播。
- **M07.10 器件仿真中的 AI**：TCAD 代理模型；电热耦合代理模型；PCM 器件建模（阈值切换、熔化与非晶化、电阻漂移模型）；工艺–器件协同优化与 DTCO 中的 AI 方法。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 数据与研究内容的边界

本模块的示例一律使用公开数据或合成玩具体系。研究锚点只作为动机与案例背景，不放入未发表的数据、结果或手稿内容。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 在 rMD17 的一个分子上训练自写的小型 MLIP，并给出分层验证报告：误差指标、NVE 能量守恒、MD 稳定时长、RDF 对比；
- 写一份 MACE 架构的“源码导读”笔记：说明数据流、等变张量积在哪里发生、各超参数的物理含义；
- 实现一个紧束缚模型，用 KPM 与精确对角化计算 DOS，并计算 IPR；
- 在简化设置下复现一个晶体生成方法的核心训练步骤（可用 MP-20 子集或玩具晶格），并实现基本评价指标；
- 用 FNO 和 PINN 求解同一个二维热传导问题，与有限差分参考解比较精度和计算成本。

## 研究锚点

- **A1**：力与应力如何由能量模型通过自动微分得到；为什么某些势在 NVE 中能量不守恒
- **A2**：主动学习为什么会失效：探索器与目标构型分布不匹配、不确定性估计不准、标注设置不一致
- **A3**：为什么“低 RMSE ≠ 可用的势”：如何设计分层评价体系
- **A4**：大尺度无序体系的电子结构：带尾、局域化与大规模稀疏矩阵的数值方法
- **A6**：晶体生成与电荷密度预测：扩散模型如何处理周期性与对称性，如何评价生成质量
- **A8**：跨尺度传递：从 MLMD 热物性到连续介质电热仿真，再到代理模型与不确定性传播

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。
