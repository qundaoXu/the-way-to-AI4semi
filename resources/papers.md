# 关键论文

本文件收录蓝图第 16.3 节的论文种子清单，按原主题分组。所有条目的作者、题目、发表刊物/会议、年份与链接均已于 2026-11-11 在线核实（期刊论文核对 Crossref DOI 记录；会议论文核对 NeurIPS、PMLR、ICLR 官方页面；预印本核对 arXiv 摘要页）。未标注 `[待核实]` 的条目没有未确认字段。

## MLIP 与表示

- **Behler, J., Parrinello, M. "Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces."** *Physical Review Letters* 98, 146401 (2007). [DOI](https://doi.org/10.1103/PhysRevLett.98.146401) — 原子中心对称函数与高维神经网络势的起点。arXiv 按题目检索无结果，无预印本链接。
- **Bartók, A. P., Payne, M. C., Kondor, R., Csányi, G. "Gaussian Approximation Potentials: The Accuracy of Quantum Mechanics, without the Electrons."** *Physical Review Letters* 104, 136403 (2010). [DOI](https://doi.org/10.1103/PhysRevLett.104.136403) · [arXiv:0910.1019](https://arxiv.org/abs/0910.1019) — GAP：基于高斯过程回归的原子间势。
- **Drautz, R. "Atomic cluster expansion for accurate and transferable interatomic potentials."** *Physical Review B* 99, 014104 (2019). [DOI](https://doi.org/10.1103/PhysRevB.99.014104) — ACE：完备的多体描述符基组，是 MACE 的理论基础。arXiv 按题目检索无结果，无预印本链接。
- **Zhang, L., Han, J., Wang, H., Car, R., E, W. "Deep Potential Molecular Dynamics: A Scalable Model with the Accuracy of Quantum Mechanics."** *Physical Review Letters* 120, 143001 (2018). [DOI](https://doi.org/10.1103/PhysRevLett.120.143001) · [arXiv:1707.09571](https://arxiv.org/abs/1707.09571) — DeePMD：局域坐标系下的深度势能模型。
- **Schütt, K. T., Sauceda, H. E., Kindermans, P.-J., Tkatchenko, A., Müller, K.-R. "SchNet – A deep learning architecture for molecules and materials."** *The Journal of Chemical Physics* 148, 241722 (2018). [DOI](https://doi.org/10.1063/1.5019779) · [arXiv:1712.06113](https://arxiv.org/abs/1712.06113) — 连续滤波卷积的不变消息传递势。
- **Batzner, S., Musaelian, A., Sun, L., Geiger, M., Mailoa, J. P., Kornbluth, M., Molinari, N., Smidt, T. E., Kozinsky, B. "E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials."** *Nature Communications* 13, 2453 (2022). [DOI](https://doi.org/10.1038/s41467-022-29939-5) · [arXiv:2101.03164](https://arxiv.org/abs/2101.03164) — NequIP：E(3) 等变消息传递势，数据效率高。
- **Batatia, I., Kovács, D. P., Simm, G. N. C., Ortner, C., Csányi, G. "MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields."** *Advances in Neural Information Processing Systems* 35 (NeurIPS 2022), pp. 11423–11436. [NeurIPS 论文页](https://proceedings.neurips.cc/paper_files/paper/2022/hash/4a36c3c51af11ed9f34615b81edb5bbc-Abstract-Conference.html) · [arXiv:2206.07697](https://arxiv.org/abs/2206.07697) — MACE：高阶体序的等变消息传递。
- **Batatia, I., Benner, P., Chiang, Y., Elena, A. M., Kovács, D. P., Riebesell, J., et al.（共 88 位作者）"A foundation model for atomistic materials chemistry."** *The Journal of Chemical Physics* 163, 184110 (2025). [DOI](https://doi.org/10.1063/5.0297006) · [arXiv:2401.00096](https://arxiv.org/abs/2401.00096) — MACE-MP-0：在 MPtrj 上训练的通用势。arXiv 首次提交于 2023-12-29。

## 图网络与等变性

- **Gilmer, J., Schoenholz, S. S., Riley, P. F., Vinyals, O., Dahl, G. E. "Neural Message Passing for Quantum Chemistry."** *Proceedings of the 34th International Conference on Machine Learning* (ICML 2017), PMLR 70:1263–1272. [PMLR 论文页](https://proceedings.mlr.press/v70/gilmer17a.html) · [arXiv:1704.01212](https://arxiv.org/abs/1704.01212) — MPNN：消息传递框架的统一表述。
- **Geiger, M., Smidt, T. "e3nn: Euclidean Neural Networks."** arXiv:2207.09453 (2022). [arXiv](https://arxiv.org/abs/2207.09453) — e3nn 库的数学与设计说明（不可约表示、张量积）。仅有 arXiv 预印本，摘要页备注为 "draft"。

## 电子结构 ML

- **Li, H., Wang, Z., Zou, N., Ye, M., Xu, R., Gong, X., Duan, W., Xu, Y. "Deep-learning density functional theory Hamiltonian for efficient ab initio electronic-structure calculation."** *Nature Computational Science* 2, 367–377 (2022). [DOI](https://doi.org/10.1038/s43588-022-00265-6) · [arXiv:2104.03786](https://arxiv.org/abs/2104.03786) — DeepH：用神经网络预测 DFT 哈密顿量。

## 生成模型

- **Ho, J., Jain, A., Abbeel, P. "Denoising Diffusion Probabilistic Models."** *Advances in Neural Information Processing Systems* 33 (NeurIPS 2020), pp. 6840–6851. [NeurIPS 论文页](https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) · [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) — DDPM：扩散模型的基础表述。
- **Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., Poole, B. "Score-Based Generative Modeling through Stochastic Differential Equations."** ICLR 2021（Oral）。[ICLR 页面](https://iclr.cc/virtual/2021/poster/3177) · [OpenReview](https://openreview.net/forum?id=PxTIG12RRHS) · [arXiv:2011.13456](https://arxiv.org/abs/2011.13456) — 用 SDE 统一 score matching 与扩散。
- **Lipman, Y., Chen, R. T. Q., Ben-Hamu, H., Nickel, M., Le, M. "Flow Matching for Generative Modeling."** ICLR 2023. [ICLR 页面](https://iclr.cc/virtual/2023/poster/11309) · [OpenReview](https://openreview.net/forum?id=PqvMRDCJT9t) · [arXiv:2210.02747](https://arxiv.org/abs/2210.02747) — Flow Matching：免模拟训练连续归一化流。
- **Xie, T., Fu, X., Ganea, O.-E., Barzilay, R., Jaakkola, T. "Crystal Diffusion Variational Autoencoder for Periodic Material Generation."** ICLR 2022. [ICLR 页面](https://iclr.cc/virtual/2022/poster/7063) · [OpenReview](https://openreview.net/forum?id=03RLpj-tc_) · [arXiv:2110.06197](https://arxiv.org/abs/2110.06197) — CDVAE：晶体生成模型，同时发布了 MP-20 等基准数据。
- **Jiao, R., Huang, W., Lin, P., Han, J., Chen, P., Lu, Y., Liu, Y. "Crystal Structure Prediction by Joint Equivariant Diffusion."** *Advances in Neural Information Processing Systems* 36 (NeurIPS 2023), pp. 17464–17497. [NeurIPS 论文页](https://proceedings.neurips.cc/paper_files/paper/2023/hash/38b787fc530d0b31825827e2cc306656-Abstract-Conference.html) · [arXiv:2309.04475](https://arxiv.org/abs/2309.04475) — DiffCSP：晶格与分数坐标的联合等变扩散。
- **Zeni, C., Pinsler, R., Zügner, D., Fowler, A., Horton, M., Fu, X., et al.（共 26 位作者）"A generative model for inorganic materials design."** *Nature* 639, 624–632 (2025). [DOI](https://doi.org/10.1038/s41586-025-08628-5) · [arXiv:2312.03687](https://arxiv.org/abs/2312.03687) — MatterGen：可按性质条件生成的无机材料扩散模型。arXiv 版题目为 "MatterGen: a generative model for inorganic materials design"。

## SciML

- **Raissi, M., Perdikaris, P., Karniadakis, G. E. "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations."** *Journal of Computational Physics* 378, 686–707 (2019). [DOI](https://doi.org/10.1016/j.jcp.2018.10.045) — PINN：把 PDE 残差写进损失函数。期刊版本身没有同名 arXiv 预印本；其前身为两篇 2017 年预印本 [arXiv:1711.10561](https://arxiv.org/abs/1711.10561)（Part I）与 [arXiv:1711.10566](https://arxiv.org/abs/1711.10566)（Part II）。
- **Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., Anandkumar, A. "Fourier Neural Operator for Parametric Partial Differential Equations."** ICLR 2021. [ICLR 页面](https://iclr.cc/virtual/2021/poster/3281) · [OpenReview](https://openreview.net/forum?id=c8P9NQVtmnO) · [arXiv:2010.08895](https://arxiv.org/abs/2010.08895) — FNO：在傅里叶空间参数化的算子学习。
- **Lu, L., Jin, P., Pang, G., Zhang, Z., Karniadakis, G. E. "Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators."** *Nature Machine Intelligence* 3, 218–229 (2021). [DOI](https://doi.org/10.1038/s42256-021-00302-5) · [arXiv:1910.03193](https://arxiv.org/abs/1910.03193) — DeepONet：branch/trunk 结构的算子网络。arXiv 版题目不同（"DeepONet: Learning nonlinear operators for identifying differential equations…"），且只列 3 位作者（Lu, Jin, Karniadakis）。

## Transformer

- **Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., Polosukhin, I. "Attention Is All You Need."** *Advances in Neural Information Processing Systems* 30 (NeurIPS 2017). [NeurIPS 论文页](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) · [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) — Transformer 原始论文。NeurIPS 论文页未给出页码，故不写页码。

## 核实说明

- OpenReview 对自动访问返回验证页面，上面 4 个 OpenReview 链接未能直接打开；论文 ID 取自 ICLR 官方虚拟会议页面上的 OpenReview 链接，题目、作者、会议年份以 ICLR 页面为准。
- 作者超过 9 人的论文只列前 6 位并注明总人数（人数取自 Crossref）。

## 与蓝图种子清单的差异

- **MACE-MP-0**：蓝图写作"Batatia et al., MACE-MP-0 (2023, arXiv)"。该文已正式发表于 *The Journal of Chemical Physics* 163, 184110 (2025)，题目为 "A foundation model for atomistic materials chemistry"；2023 是 arXiv 首次提交年份。
- **MatterGen**：蓝图年份与刊物（2025, Nature）无误；正式发表题目不含 "MatterGen:" 前缀。
- **PINN**：蓝图所写 2019, J. Comput. Phys. 无误；补充了两篇 2017 年 arXiv 前身预印本。
- **DeepONet**：蓝图所写 2021, Nat. Mach. Intell. 无误；arXiv 版题目与作者人数和期刊版不同（见条目）。
- 其余条目的年份与刊物/会议均与蓝图一致。
