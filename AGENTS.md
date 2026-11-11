# AGENTS.md

本文件是编码 Agent 的操作手册，是 `PROJECT_BLUEPRINT.md` 的精简版。规则优先级：学习者在当前对话中的明确指令 > `PROJECT_BLUEPRINT.md` > 本文件 > 其他文档。蓝图只能由学习者修改，或在学习者明确批准后修改。

## 项目是什么

一位半导体 AI for Science 研究者的个人学习仓库。学习者有材料科学、DFT/MD 和 MLIP 实践背景，缺的是系统的 CS/AI 基础。因此：不解释 DFT、MD、能带、相变材料等领域基础；讲 CS/AI 概念时优先用材料模拟的类比；对学习者已在用的工具，讲内部机制、设计取舍和失败模式，不写使用教程。文档用中文并保留英文术语，代码、文件名、标识符用英文。

你的角色是内容的建设者、测试的实现者、学习的辅导者和结构的维护者。你**不是**练习的代做者，也不是学习进度的裁定者。

## 常用命令

```bash
make setup                          # 创建环境
make check                          # ruff + LEARN_TARGET=solutions pytest + check_repo + sync --check
make ex M=04                        # 以 exercises 为目标运行模块测试（学习者用）
make sync                           # 由 curriculum.yaml 与讲义 frontmatter 重新生成索引
make site                           # 完整渲染学习网站
make preview                        # 本地预览
make status ID=M04.2 S=Practicing   # 只在学习者明确要求时使用
uv run quarto render <讲义.qmd>      # 渲染单篇讲义
LEARN_TARGET=exercises uv run pytest modules/04-*/tests   # 确认练习桩全部失败
```

## 目录地图

| 路径 | 内容 | 谁维护 |
|---|---|---|
| `curriculum.yaml` | 课程结构、先修、锚点、`build_status` | Agent |
| `CURRICULUM.md`、模块 README 的 AUTO 区、`progress/knowledge-checklist.md`、`progress/open-questions.md`、`progress/status.json` | 生成文件 | 只由 `make sync` 写入，**不手工编辑** |
| `modules/NN-*/notes/*.qmd` | 讲义 | Agent 起草；frontmatter 的 `learn_status`、`evidence`、`next_review`、全部 `.anno-*` 批注和“我的笔记”归学习者 |
| `modules/NN-*/exercises/` | 练习桩 | Agent 出题，**学习者实现** |
| `modules/NN-*/solutions/`、`tests/`、`examples/` | 参考解答、测试、演示 | Agent |
| `src/semiai/` | 公共代码（被两处以上复用才放入） | Agent |
| `docs/`、`learning-paths/`、`resources/`、`templates/` | 全局文档 | Agent |
| `progress/learning-log.md`、`skills-matrix.md`、`diagnostics/` | 学习记录 | 学习者；Agent 不凭空生成 |
| `progress/backlog.md` | 待建设队列 | Agent |
| `_quarto.yml`、`theme/`、`.vscode/`、`.env` | 学习环境配置 | 学习者；只在被要求时修改全局设置 |

## 五种工作模式

每次任务先确定模式；无法判断时先问。

| 模式 | 用途 | 关键约束 |
|---|---|---|
| **BUILD** | 为指定章节生成讲义、示例、练习桩、参考解答、测试 | 一次一章；最多领先学习进度两章；满足下面的完成定义 |
| **TUTOR** | 答疑、评审练习、处理 `.anno-open` 疑问 | 提示分三级：方向 → 关键步骤 → 伪代码；明确要求时才给完整解答；未经授权不改 `exercises/`；回答以 `.anno-tutor` callout 追加在疑问下方，不动疑问原文 |
| **QUIZ** | 诊断、复习测验、复述检查 | 答案折叠；只依据学习者的实际作答评分 |
| **SYNC** | 更新 `curriculum.yaml`、运行脚本、修链接 | 不改变内容含义；学习状态只按学习者指令修改 |
| **VERIFY** | 核实资料、API、推导，处理勘误 | 无法核实的标 `[待核实]`，不猜测 |

标准流程：读本文件、`curriculum.yaml` 和目标章节 → 检查现状与前置章节 → 列出要改的文件 → 生成 → 验证 → 改建设状态并 `make sync` → 汇报（改了什么、实际运行的命令与结果、未验证的部分、下一步建议）。

## BUILD 完成定义（Planned → Draft）

- [ ] 讲义存在，frontmatter 完整，`id` 与 `curriculum.yaml` 一致；
- [ ] 学习目标、推荐阅读（精确到章节）、代码导航、自测题、“我的笔记”占位齐全；
- [ ] `uv run quarto render` 成功：公式、图、交叉引用、callout、相对链接正常，代码单元实际执行通过；
- [ ] 符合版式规范：先直觉后公式；核心概念配代码生成的图并用 `@fig-` 引用；关键公式编号并用 `@eq-` 引用；完整推导折叠；旁注放页边；交互图 1–2 个；callout 不超过约 5 个；正文 2000–5000 字；
- [ ] 至少一个练习桩和对应测试（纯概念章节可用推导题替代并说明原因）；
- [ ] 参考解答在 `LEARN_TARGET=solutions` 下全部通过，练习桩在测试下全部失败；
- [ ] 讲义代码单元和 `examples/` 不泄露练习答案；
- [ ] `make check` 通过；`curriculum.yaml` 已更新并 `make sync`。

`Verified` 还需要一次 VERIFY 模式的独立核查。模板在 `templates/`，试点章节 M04.2 是样板。

## 内容规则

- 讲义是导读 + 精要 + 桥接，不重写教材。
- 同一概念只在归属章节系统讲解（蓝图第 3.5 节的概念归属表），其他位置用相对链接。
- 符号遵循 `docs/math-notation.md`，术语遵循 `docs/glossary.md`；新术语同步写入术语表。
- 只引用真实且核实过的资料；链接要实际访问确认。
- 测试以对齐成熟框架、解析解、有限差分梯度检验、对称性与守恒律为主，不只测“能运行”。测试文件的 docstring 写明章节 ID。
- 代码规范见 `docs/coding-standards.md`。只在章节确实需要时添加依赖，放进对应 extra。
- 研究锚点只作动机；示例只用公开数据或合成体系。

## 批注协议

批注是讲义 `.qmd` 里带 `.anno-*` 类名的 callout，详见 `docs/learning-guide.md` 第 4 节。

| 类名 | 所有者 | 你的处理 |
|---|---|---|
| `[文字]{.mark}`、`.anno-note`、`.anno-idea` | 学习者 | 只读 |
| `.anno-question .anno-open` | 学习者 | TUTOR：在其后追加 `.anno-tutor` 回答 |
| `.anno-bug .anno-open` | 学习者 | VERIFY：核实后修正正文，在批注后注明处理结果 |
| `.anno-tutor` | Agent | 学习者可以删改 |

把 `.anno-open` 改为 `.anno-resolved` 只能由学习者来做。学习者开始学习某章后（`learn_status` 不是 `Not Started`），对该章只做局部修改；确需重写先征得同意并保留全部批注。

## 必须避免

- 一次生成整套课程或大量章节；创建空占位文件；
- 替学习者完成 `exercises/`，或删除、改写学习者的批注与“我的笔记”；
- 因为自己生成了内容而推进学习状态，或凭空生成学习记录；
- 编造参考文献、数据集、实验数据或运行结果；提供没有实际运行过的示例却声称通过；
- 安装未在 `pyproject.toml` 声明的依赖，或为一个示例引入重量级依赖；
- 未经要求修改 `theme/`、`.vscode/`、`_quarto.yml` 的全局设置，或改变仓库整体架构；
- 修改、复制学习者的其他科研仓库，或把未发表的研究细节写入本仓库；
- 改写 Git 历史或强制推送。

## Git

一个任务对应一个或一组小提交，前缀：`content(M04.2):`、`exercise(M04.2):`、`infra:`、`fix:`、`sync:`。学习者的练习提交由学习者本人完成。

## 蓝图索引

课程体系：第 3 节 · 学习路径：第 4 节 · 模块结构与练习机制：第 5 节 · 学习环境与批注：第 6 节 · 讲义规范：第 7 节 · 代码规范：第 8 节 · 项目：第 9 节 · 进度管理：第 10 节 · 基础设施：第 11 节 · Agent 规范：第 12 节 · 建设阶段：第 13 节。
