# Module 06：现代 AI 架构（Advanced AI Architectures）

模块优先级 `P1` · 估算学时 70–90 h

## 定位

理解现代主流架构，重点是几何与等变深度学习、生成模型和不确定性量化。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M06.1 | Attention 与 Transformer<br>Attention and Transformer | P1 | M05.4 | — | Planned | Not Started |
| M06.2 | 图神经网络基础<br>Graph Neural Network Basics | P1 | M05.4 | — | Planned | Not Started |
| M06.3 | 几何与等变深度学习<br>Geometric and Equivariant Deep Learning | P1 | M02.7, M06.2 | — | Planned | Not Started |
| M06.4 | 生成模型<br>Generative Models | P1 | M02.3, M02.8, M05.4 | A6 | Planned | Not Started |
| M06.5 | 不确定性量化、主动学习与贝叶斯优化<br>Uncertainty Quantification, Active Learning and Bayesian Optimization | P1 | M04.3, M04.7, M05.4 | A2 | Planned | Not Started |
| M06.6 | 表征学习与迁移<br>Representation Learning and Transfer | P2 | M05.4 | — | Planned | Not Started |

**各章范围**

- **M06.1 Attention 与 Transformer**：Self-attention 与多头注意力；位置编码；Encoder 与 Decoder；预训练与迁移；注意力与图神经网络的关系。Attention 的主要归属章节。
- **M06.2 图神经网络基础**：图表示；消息传递框架（MPNN）；GCN、GAT；节点级与图级任务；过平滑与表达能力（WL 测试的直觉）。
- **M06.3 几何与等变深度学习**：不变性与等变性；基于距离与角度的不变网络（SchNet、DimeNet 类）；E(3) 等变网络（张量场网络、NequIP）；高阶多体相互作用（ACE、MACE）；局域性、截断半径与消息传递层数的关系；e3nn 实践。AI for Science 核心。
- **M06.4 生成模型**：自编码器与 VAE；GAN（了解）；Normalizing Flow；扩散模型（DDPM、score-based SDE）；Flow Matching；条件生成与 guidance。材料生成的具体处理见 M07.6。扩散模型的主要归属章节。
- **M06.5 不确定性量化、主动学习与贝叶斯优化**：偶然不确定性与认知不确定性；深度集成、MC Dropout、证据学习、最后一层高斯过程；校准评价（误差–不确定性相关性、校准曲线）；采集函数；主动学习循环及其失败模式（探索器与目标分布不匹配、不确定性失效、标注设置不一致）；贝叶斯优化。三者的主要归属章节。
- **M06.6 表征学习与迁移**：自监督学习；对比学习；预训练–微调；多任务学习；分布外泛化。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 从零实现 mini-Transformer，训练字符级语言模型（nanoGPT 规模，CPU 可运行）；
- 从零实现 SchNet 类不变 GNN，并通过旋转、平移、置换不变性的单元测试；
- 用 e3nn 构建一个等变消息传递层，并数值验证其等变性；
- 在二维玩具分布上分别实现 DDPM 与 Flow Matching，比较采样质量；
- 在一个回归任务上比较三种 UQ 方法的校准表现，并写出主动学习失败模式的分析笔记。

## 研究锚点

- **A2**：主动学习为什么会失效：探索器与目标构型分布不匹配、不确定性估计不准、标注设置不一致
- **A6**：晶体生成与电荷密度预测：扩散模型如何处理周期性与对称性，如何评价生成质量

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。
