# the-way-to-AI4semi

面向半导体 AI for Science 的个人长期学习仓库：一部分是知识库，一部分是算法实践场。目标是系统补齐 CS、数学、统计和机器学习基础，把已经在用的工具（MLIP、ML 哈密顿量、扩散模型）从“会用”提升到“理解原理、能修改、能诊断、能独立实现简化版本”，并积累能展示独立研发能力的综合项目。

仓库有三个区别于普通笔记仓库的设计：

- **讲义讲原理，notebook 讲代码。** 每章一篇讲义加一个带运行结果的实例讲解 notebook，在网站上直接读，也能在 VS Code 里逐单元运行、改参数。
- **讲义是导读、精要和桥接，不重写教材。** 内容按模块建设，一次一个模块。
- **阅读在浏览器，动手在 VS Code。** 讲义渲染为 Quarto 学习网站，批注直接写在源文件里，Agent 能读到并在原处回应。

最高层设计规范是 [PROJECT_BLUEPRINT.md](PROJECT_BLUEPRINT.md)。

## 快速开始

需要 [uv](https://docs.astral.sh/uv/)、[Quarto CLI](https://quarto.org/docs/get-started/)、Git、GNU Make 和 VS Code。

```bash
make setup      # 创建 .venv，安装依赖
make check      # 验证环境：ruff + 测试 + 仓库一致性
make preview    # 启动本地学习网站
make nb M=01    # 重新执行模块 01 的实例 notebook 并保存输出
```

详细步骤见 [docs/getting-started.md](docs/getting-started.md)，学习方法见 [docs/learning-guide.md](docs/learning-guide.md)。

## 当前状态

Phase 1（项目骨架与流程验证）已完成：12 个模块、73 章的课程结构已写入 `curriculum.yaml`，试点章节 **M04.2 线性模型**有讲义、实例 notebook，以及一套练习–解答–测试（保留作选做）。

2026-11 起进入 Phase 2：按模块建设核心课程，每章交付讲义和实例 notebook，不设练习桩、自测题和诊断测评。各模块建设进度见 [CURRICULUM.md](CURRICULUM.md)，待办事项见 [progress/backlog.md](progress/backlog.md)。

## 导航

| 想做什么 | 去哪里 |
|---|---|
| 看全部模块与章节 | [CURRICULUM.md](CURRICULUM.md)（由脚本生成） |
| 选学习路径 | [Path A 通用基础](learning-paths/path-a-core-cs-ai.md) · [Path B AI for Science（主路径）](learning-paths/path-b-ai-for-science.md) · [Path C 工业 AI](learning-paths/path-c-semiconductor-industrial-ai.md) · [Path D AI 硬件](learning-paths/path-d-hardware-for-ai.md) |
| 开始试点章节 | [M04.2 线性模型](modules/04-classical-machine-learning/notes/02-linear-models.qmd) · [实例 notebook](modules/04-classical-machine-learning/notebooks/02-linear-models.ipynb) · [练习（选做）](modules/04-classical-machine-learning/exercises/README.md) |
| 了解为什么学某一章 | [docs/research-anchors.md](docs/research-anchors.md) |
| 查进度 | [progress/knowledge-checklist.md](progress/knowledge-checklist.md) · [progress/open-questions.md](progress/open-questions.md) |
| 找教材、论文、数据集 | [resources/](resources/textbooks.md) · [datasets/README.md](datasets/README.md) |
| 给 Agent 下指令 | [docs/agent-prompts.md](docs/agent-prompts.md) |
| 综合项目 | [projects/README.md](projects/README.md) |

## 目录

```text
├── PROJECT_BLUEPRINT.md   最高层设计规范
├── AGENTS.md / CLAUDE.md  Agent 操作规范
├── curriculum.yaml        课程结构与建设状态的唯一来源
├── CURRICULUM.md          课程总目录（生成）
├── _quarto.yml, index.qmd 学习网站配置与首页仪表盘
├── theme/                 网站主题、批注样式、Lua 过滤器
├── modules/               12 个知识模块：notes/ 讲义，notebooks/ 实例 notebook
├── learning-paths/        四条学习路径
├── projects/              综合实践项目
├── docs/                  快速开始、学习指南、规范、术语、研究锚点、指令库
├── resources/             经过核实的教材、课程、论文、文档、仓库清单
├── datasets/              数据集登记（数据本身不入库）
├── progress/              进度清单、未解决疑问、status.json（生成）、待建设队列
├── templates/             讲义、练习、实验记录等模板
├── src/semiai/            公共代码包：统一绘图样式、练习加载器、梯度检验工具
├── scripts/               sync_index.py、check_repo.py
├── tests/                 semiai 的测试
└── _freeze/               Quarto 代码执行结果缓存（提交）
```

## 说明

仓库为私有。内容不包含未发表的研究数据或手稿；若将来转为公开，需要先复查。
