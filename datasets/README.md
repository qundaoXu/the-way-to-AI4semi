# 数据集登记表

本文件登记蓝图第 16.4 节的数据集。目前尚无任何获取脚本；数据集一律不下载进仓库，仓库内只允许存放单个文件小于 5 MB 的样例文件。表中信息已于 2026-11-11 在来源页面核实，未能确认的字段标注 `[待核实]`。

| 数据集 | 内容 | 来源链接 | 许可 | 大小 | 获取脚本 | 关联章节 |
|---|---|---|---|---|---|---|
| UCI SECOM | 半导体制造过程的传感器数据，1567 个样本、591 个特征，带通过/失败标签 | [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/179/secom)（DOI: [10.24432/C54305](https://doi.org/10.24432/C54305)） | CC BY 4.0 | 下载包 1.9 MB；其中 `secom.data` 解压后 5.1 MB | 尚无 | M03.3, M08.2 |
| WM-811K | 晶圆图失效模式数据集；原始论文为 Wu, Jang, Chen, *IEEE Trans. Semicond. Manuf.* 28(1), 1–12 (2015)，[DOI](https://doi.org/10.1109/TSM.2014.2364237) | [Kaggle 镜像](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map)；原始发布页 `[待核实]` | `[待核实]` | `[待核实]` | 尚无 | M05.5, M08.3 |
| rMD17 | 10 种小分子的分子动力学构型及重新计算的能量与力；对应论文 Christensen & von Lilienfeld, *Mach. Learn.: Sci. Technol.* 1, 045018 (2020)，[DOI](https://doi.org/10.1088/2632-2153/abba6f) | [figshare](https://figshare.com/articles/dataset/Revised_MD17_dataset_rMD17_/12672038)（DOI: 10.6084/m9.figshare.12672038） | CC0 | `rmd17.tar.bz2` 约 1.07 GB；单分子 `.npz` 文件 67–175 MB | 尚无 | M03.4, M07.3 |
| QM9 | 133,885 个 GDB-9 小分子的平衡构型与量子化学性质；对应论文 Ramakrishnan et al., *Scientific Data* 1, 140022 (2014)，[DOI](https://doi.org/10.1038/sdata.2014.22) | [figshare 合集](https://figshare.com/collections/Quantum_chemistry_structures_and_properties_of_134_kilo_molecules/978904) | CC0（主数据文件条目）；合集内其余条目 `[待核实]` | 主文件 `dsgdb9nsd.xyz.tar.bz2` 约 86 MB | 尚无 | M06.2 |
| Matbench | 13 个材料性质预测任务的基准集；对应论文 Dunn et al., *npj Comput. Mater.* 6, 138 (2020)，[DOI](https://doi.org/10.1038/s41524-020-00406-3) | [项目主页](https://matbench.materialsproject.org/) · [仓库](https://github.com/materialsproject/matbench) | 代码仓库为 MIT；数据本身的许可 `[待核实]` | `[待核实]` | 尚无 | M04.8 |
| Matbench Discovery | 评估 ML 模型预测晶体稳定性（高通量材料发现）的基准与排行榜；对应论文 Riebesell et al., *Nat. Mach. Intell.* 7, 836–847 (2025)，[DOI](https://doi.org/10.1038/s42256-025-01055-1) | [项目主页](https://matbench-discovery.materialsproject.org/) · [仓库](https://github.com/janosh/matbench-discovery) | 代码仓库为 MIT；数据本身的许可 `[待核实]` | `[待核实]` | 尚无 | M07.4 |
| MPtrj | Materials Project 弛豫轨迹数据（能量、力、应力、磁矩），随 CHGNet 发布；对应论文 Deng et al., *Nat. Mach. Intell.* 5, 1031–1041 (2023)，[DOI](https://doi.org/10.1038/s42256-023-00716-3) | [figshare](https://figshare.com/articles/dataset/Materials_Project_Trjectory_MPtrj_Dataset/23713842)（DOI: 10.6084/m9.figshare.23713842） | MIT（figshare 页面所列） | `MPtrj_2022.9_full.json` 约 12.2 GB | 尚无 | M07.4 |
| MP-20 | 45,231 个晶胞内不超过 20 个原子的无机晶体结构（取自 Materials Project），随 CDVAE 发布，用于晶体生成 | [cdvae 仓库 `data/mp_20`](https://github.com/txie-93/cdvae/tree/main/data/mp_20) | 仓库为 MIT；数据源自 Materials Project，其数据条款 `[待核实]` | 三个 CSV 合计约 58 MB（train 35.0 MB、val 11.6 MB、test 11.6 MB） | 尚无 | M07.6 |
| PDEBench | 多种 PDE（对流、Burgers、扩散-反应、Navier–Stokes 等）的科学机器学习基准；对应论文 Takamoto et al., NeurIPS 2022 Datasets and Benchmarks, [论文页](https://proceedings.neurips.cc/paper_files/paper/2022/hash/0a9747136d411fb83f0cf81820d44afb-Abstract-Datasets_and_Benchmarks.html) | [DaRUS 数据仓储](https://darus.uni-stuttgart.de/dataset.xhtml?persistentId=doi:10.18419/darus-2986)（DOI: 10.18419/darus-2986） · [代码仓库](https://github.com/pdebench/PDEBench) | 数据 CC BY 4.0；代码 MIT | 全集 336 个文件，合计约 3.9 TB（按 DaRUS API 的文件大小求和）；只能按需下载单个子集 | 尚无 | M07.8 |

## 核实说明

- **SECOM**：`secom.data` 解压后为 5.1 MB，超过仓库 5 MB 的单文件上限，不能原样放入仓库。
- **WM-811K**：Kaggle 页面为前端渲染，许可与文件大小无法自动读取；通常引用的原始发布地址 `mirlab.org/dataSet/public/` 核实当日返回 404，因此原始来源、许可、大小均未确认。
- **rMD17**：figshare 记录当前为第 4 版；10 个分子为 aspirin、azobenzene、benzene、ethanol、malonaldehyde、naphthalene、paracetamol、salicylic acid、toluene、uracil（取自文件列表）。
- **Matbench / Matbench Discovery**：项目主页与仓库已确认，但数据文件的许可与总大小没有在已访问的页面上找到明确说明。
- **PDEBench**：3.9 TB 是对 DaRUS API 返回的 336 个文件大小求和得到的数字，不是页面上的官方说法。

## 与蓝图种子清单的差异

- 蓝图仅列出数据集名称，未给出来源、许可与大小；上述信息均为本次核实补充。
- **MP-20**：没有独立的发布页，官方来源是 CDVAE 代码仓库中的 `data/mp_20` 目录。
- **MPtrj**：figshare 条目的英文标题为 "Materials Project Trajectory (MPtrj) Dataset"（URL 路径中拼作 "Trjectory"，为原始 URL，未改动）。
