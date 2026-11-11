# 代码仓库

本文件收录蓝图第 16.5 节中软件的源码仓库。所有条目的仓库地址、归属组织、许可证与配套文档链接均已于 2026-11-11 通过 GitHub/GitLab API 与仓库内许可证文件核实；核实当日所有仓库均未归档。

## 机器学习原子间势（MLIP）

- **ACEsuit. *mace*.** MIT 许可。[仓库](https://github.com/ACEsuit/mace) · [文档](https://mace-docs.readthedocs.io/en/latest/) — MACE 的官方实现，含 MACE-MP 基础模型的加载与微调入口。
- **mir-group. *nequip*.** MIT 许可。[仓库](https://github.com/mir-group/nequip) · [文档](https://nequip.readthedocs.io/en/latest/) — NequIP 的官方实现，用于训练 E(3) 等变原子间势。
- **deepmodeling. *deepmd-kit*.** LGPL-3.0 许可。[仓库](https://github.com/deepmodeling/deepmd-kit) · [文档](https://docs.deepmodeling.com/projects/deepmd/en/stable/) — DeePMD 的官方实现，含训练与 LAMMPS 等 MD 接口。
- **jax-md. *jax-md*.** Apache-2.0 许可。[仓库](https://github.com/jax-md/jax-md) · [文档](https://jax-md.readthedocs.io/en/main/) — 基于 JAX 的可微分分子动力学，适合自己写积分器与势函数的练习。

## 图网络与等变性

- **e3nn. *e3nn*.** MIT 许可。[仓库](https://github.com/e3nn/e3nn) · [文档](https://docs.e3nn.org/en/latest/) — E(3) 等变神经网络的基础库（不可约表示、张量积）。
- **pyg-team. *pytorch_geometric*.** MIT 许可。[仓库](https://github.com/pyg-team/pytorch_geometric) · [文档](https://pytorch-geometric.readthedocs.io/en/latest/) — PyTorch 图神经网络库，含 QM9、MD17 等数据集加载器。

## 原子模拟与材料工具

- **ASE developers. *ase*.** LGPL-2.1-or-later 许可。[仓库（GitLab）](https://gitlab.com/ase/ase) · [文档](https://docs.ase-lib.org/) — 原子模拟环境；多数 MLIP 都提供 ASE calculator。
- **Materials Project. *pymatgen*.** MIT 许可。[仓库](https://github.com/materialsproject/pymatgen) · [文档](https://pymatgen.org/) — 材料结构分析库，用于晶体结构处理与 Materials Project 数据访问。

## SciML

- **neuraloperator. *neuraloperator*.** MIT 许可。[仓库](https://github.com/neuraloperator/neuraloperator) · [文档](https://neuraloperator.github.io/dev/index.html) — FNO 等神经算子的 PyTorch 实现。
- **Lu, L. *deepxde*.** LGPL-2.1 许可。[仓库](https://github.com/lululxvi/deepxde) · [文档](https://deepxde.readthedocs.io/en/latest/) — PINN 与 DeepONet 的科学机器学习库。

## 模拟计算硬件

- **IBM. *aihwkit*.** MIT 许可。[仓库](https://github.com/IBM/aihwkit) · [文档](https://aihwkit.readthedocs.io/en/latest/) — IBM Analog Hardware Acceleration Kit，用于模拟存内计算器件上的神经网络训练与推理仿真。

## 核实说明

- GitHub API 对 mace、e3nn、pymatgen 的许可证字段返回 `NOASSERTION`，上面所写的 MIT 是直接读取仓库内 `LICENSE` 文件确认的。
- GitLab API 把 ASE 识别为 "GPL v2.0 or later"，但仓库内 `LICENSE` 文件写明为 GNU Lesser General Public License 2.1 或更高版本；本文件以 `LICENSE` 文件为准。

## 与蓝图种子清单的差异

- **JAX-MD**：仓库已从 `google/jax-md` 迁至 `jax-md/jax-md`，旧地址会自动重定向。
- **ASE**：源码托管在 GitLab 而非 GitHub；项目主页已从 `wiki.fysik.dtu.dk/ase/` 迁至 `ase-lib.org`。
- 蓝图仅列出软件名称，未给出仓库地址、许可证；上述信息均为本次核实补充。
