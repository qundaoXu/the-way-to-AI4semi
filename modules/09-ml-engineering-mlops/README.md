# Module 09：ML 工程与 MLOps（ML Engineering and MLOps）

模块优先级 `P1/P2` · 估算学时 30–40 h

## 定位

把研究代码整理为可复现、可协作的工程项目。对研究者而言，可复现性优先于部署。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M09.1 | AI 项目工程化<br>Engineering AI Projects | P1 | M01.3 | — | Planned | Not Started |
| M09.2 | 实验管理与可复现性<br>Experiment Management and Reproducibility | P1 | M09.1 | — | Planned | Not Started |
| M09.3 | 科学计算工作流编排<br>Scientific Workflow Orchestration | P2 | M09.1 | — | Planned | Not Started |
| M09.4 | 模型部署与推理<br>Model Deployment and Inference | P2 | M05.3 | — | Planned | Not Started |
| M09.5 | 生产环境 ML<br>Machine Learning in Production | P3 | M09.2, M03.4 | — | Planned | Not Started |

**各章范围**

- **M09.1 AI 项目工程化**：包结构与接口设计；配置管理（YAML 或 Hydra，择一深入）；数值代码的测试策略（容差测试、性质测试、回归测试、梯度检验、对称性检验）；CI 基础。
- **M09.2 实验管理与可复现性**：实验追踪（MLflow 或 Weights & Biases，择一深入）；数据与模型版本管理（DVC 了解）；环境锁定；结果溯源。
- **M09.3 科学计算工作流编排**：高通量计算工作流的组织（如 Snakemake、AiiDA、jobflow/atomate2 等，择一了解）；失败重试与数据溯源。
- **M09.4 模型部署与推理**：FastAPI；Docker；推理优化（torch.compile、TorchScript、ONNX）。
- **M09.5 生产环境 ML**：模型监控；数据漂移检测；模型更新策略。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- Project 03 的训练框架满足：配置驱动、实验可追踪、关键数值逻辑有测试、CI 通过、任一实验可由记录完整复现。

## 研究锚点

本模块没有直接关联的研究锚点。
