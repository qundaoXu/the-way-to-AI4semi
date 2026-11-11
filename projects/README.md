# 综合实践项目

项目用于跨模块的综合实践：做集成、规模化和真实评价，不重复 `modules/` 里的单个算法练习。项目按学习阶段逐步启动，每个项目启动时用 `templates/project-template.md` 在自己的子目录里建立 README（目标、涉及模块、数据、里程碑、验收标准、当前状态）。

目前所有项目都处于“未启动”状态，子目录尚未创建。

| 项目 | 目录 | 涉及模块 | 路径 | 计划启动 |
|---|---|---|---|---|
| 01 Semiconductor Data Analysis | `01-semiconductor-data-analysis/` | M03、M04、M08 | C（A 的可选练习） | 选择 Path C 时 |
| 02 Mini ML Library | `02-mini-ml-library/` | M01、M02、M04 | A | 第 1–3 月 |
| 03 PyTorch Training Harness | `03-pytorch-training-harness/` | M01、M05、M09 | A | 第 4–6 月 |
| 04 Mini Equivariant MLIP | `04-mini-equivariant-mlip/` | M02.7、M05、M06.3、M06.5、M07.2–M07.4 | B | 第 7–9 月 |
| 05 SciML Surrogate | `05-sciml-surrogate/` | M02.6、M05、M07.7–M07.8、M09 | B | 第二年 |
| 06 PCM Multiscale AI | `06-pcm-multiscale-ai/` | M07、M09、M11 | B | 长期 |
| 07 Paper Reproductions | `07-paper-reproductions/` | 按论文而定 | — | 第 10–12 月起 |

## Project 01：Semiconductor Data Analysis

基于公开的半导体制造数据（如 UCI SECOM、WM-811K 晶圆图数据集）完成数据清洗与 EDA、特征工程、分类与异常检测、模型比较和可解释性分析。重点训练极度不平衡数据与高缺失率数据的处理。

## Project 02：Mini ML Library

把模块练习中的从零实现整合为一个风格统一、有测试、有文档的小型 ML 库，提供统一的 `fit`/`predict` 接口，与 scikit-learn 做数值对齐和性能对比。重点在接口设计与工程整合，不是重复写算法。

## Project 03：PyTorch Training Harness

开发一个轻量、规范的训练框架：数据加载、模型注册、训练与验证循环、checkpoint 与断点续训、日志与实验追踪、配置管理、混合精度、自动化测试。Project 04、05 复用这个框架。

## Project 04：Mini Equivariant MLIP

从零构建一个小型机器学习势。这是展示“理解而非调用”能力的核心作品。

1. 先实现 SchNet 类不变模型，再基于 e3nn 实现一个等变模型；
2. 用 autograd 计算力与应力，通过梯度检验与对称性测试；
3. 在公开数据（如 rMD17）上训练；
4. 按分层体系验证：误差指标、NVE 能量守恒、MD 稳定时长、结构性质；
5. 用集成方法估计不确定性并评价校准；
6. 与 MACE 在同一数据上对比，分析差距来源。

## Project 05：SciML Surrogate

以二维电热耦合或热传导问题（可抽象自 PCM 加热器结构）为对象：用有限差分或有限元生成数据；分别训练 FNO、PINN 与传统代理模型（如 GPR）；比较精度、分辨率泛化、计算加速和物理一致性。

## Project 06：PCM Multiscale AI（长期）

长期专业主线：GST 机器学习势、MLMD 热物性、材料参数向连续介质仿真的传递、PCM 器件电热仿真、代理模型与跨尺度不确定性评估。

**规则。** 初期只创建规划文档，后续根据真实研究进度建设。这个目录只链接外部研究仓库，不复制、不修改原始科研文件，不放入未发表数据。

## Project 07：Paper Reproductions

每篇复现一个子目录，使用 `templates/paper-reproduction-template.md`：要复现的核心结论、简化条件与原因、设置、结果与原文对比、差异分析。建议第一年复现 1–2 篇，候选方向：DDPM（玩具数据）、SchNet 或 NequIP（小数据集）、FNO（一维或二维 PDE）。
