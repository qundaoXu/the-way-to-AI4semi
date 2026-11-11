# Module 10：大语言模型、RAG 与 Agent（LLM, RAG and Agents）

模块优先级 `P2` · 估算学时 30–40 h

## 定位

理解大语言模型、检索增强生成与 Agent 系统的原理，并把它们用于科学计算工作流。模块优先级为 P2，其中 M10.5（高效使用编码 Agent）为 P1：本仓库的建设过程本身就是它的实践。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M10.1 | 大语言模型原理<br>Large Language Model Principles | P2 | M06.1 | — | Planned | Not Started |
| M10.2 | 检索增强生成<br>Retrieval-Augmented Generation | P2 | M10.1 | — | Planned | Not Started |
| M10.3 | Agent 系统<br>Agent Systems | P2 | M10.1 | — | Planned | Not Started |
| M10.4 | 科学 Agent<br>Scientific Agents | P2 | M10.3 | — | Planned | Not Started |
| M10.5 | 高效使用编码 Agent<br>Working Effectively with Coding Agents | P1 | — | — | Planned | Not Started |

**各章范围**

- **M10.1 大语言模型原理**：Tokenization；基于 Transformer 的 LLM；预训练、指令微调与偏好优化概览；LoRA 与 PEFT；推理与评价。
- **M10.2 检索增强生成**：Embedding；向量检索与重排；RAG 流程；检索质量与答案可信度评价。
- **M10.3 Agent 系统**：工具调用；规划；状态与记忆；MCP 与工具集成；多 Agent 协作；人在回路；错误恢复与结果验证。
- **M10.4 科学 Agent**：文献检索；科学数据库交互；DFT、MD、有限元工具调用；自动化计算工作流；计算结果校验与溯源。
- **M10.5 高效使用编码 Agent**：编写可执行的规格文档；任务拆分与上下文管理；让 Agent 产出可验证结果；审阅 Agent 代码的方法。本仓库的建设过程本身就是本章的实践。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 设计并实现一个能可靠执行某个科学计算子任务（如结构弛豫 + 结果校验）的最小 Agent，包含工具调用、失败处理和结果验证。

## 研究锚点

本模块没有直接关联的研究锚点。
