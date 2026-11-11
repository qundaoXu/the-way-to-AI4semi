# Agent 指令库

可以直接复制给编码 Agent（Claude Code 等）的指令，与 `PROJECT_BLUEPRINT.md` 第 15 节同步。Agent 的五种工作模式和约束见仓库根目录的 `AGENTS.md`。

使用时把章节 ID、文件路径和尖括号里的内容换成实际值。

## 初始化（Phase 1，已完成）

> 请以仓库根目录的 `PROJECT_BLUEPRINT.md` 作为最高层规范，初始化一个面向半导体 AI for Science 职业发展的个人 CS/AI 学习仓库。
>
> 只完成 Phase 1（第 13 节），并以第 14 节作为验收标准。开始前先阅读第 1.5 节的预设参数，若有与本机环境冲突之处，先向我确认。
>
> 具体要求：按第 2 节建立目录；按第 11.1 节把第 3 节的全部模块与章节写入 `curriculum.yaml`；实现 `sync_index.py` 与 `check_repo.py` 并用它们生成索引；按第 12.7 节编写精简的 `AGENTS.md`；实现 `src/semiai/testing` 的最小功能；按第 6 节搭建 Quarto 学习网站与 VS Code 工作台；以 M04.2 作为试点章节，完整走通练习–解答–测试流程。
>
> 不要生成试点章节以外的课程正文，不要创建空占位文件，不要编造学习记录或参考资料，不要修改我的其他科研仓库。
>
> 完成后运行 `make check`，并汇报：已创建的文件、实际执行的命令与结果、未能验证的部分、对 Phase 1b 的建议。

## 诊断与路线（Phase 1b）

**生成诊断题（QUIZ）：**

> QUIZ 模式：为 Module 02 生成诊断题，每章 2–4 道，答案折叠。我作答后请评分，并给出每章 Skip / Light / Full 的建议。

**生成个人化路线：**

> 根据 `progress/diagnostics/` 中 Module 01–05 的诊断结论，生成个人化的 `ROADMAP.md`：按每周 <9> 小时排期，Skip 的章节只安排练习验证，写明每个阶段的检查点。

## 日常指令

**建设一个章节（BUILD）：**

> BUILD 模式：建设 M02.1。先检查前置章节和概念归属表，列出计划后再动手。完成后按第 12.4 节逐条核对完成定义并汇报测试结果。

**评审我的练习（TUTOR）：**

> TUTOR 模式：我完成了 `modules/04-classical-machine-learning/exercises/linear_regression.py`，`make ex M=04` 有两个测试失败。请先只给方向提示，不要修改我的文件，也不要给出完整代码。

**回答讲义中的疑问（TUTOR）：**

> TUTOR 模式：处理 `progress/open-questions.md` 中 M04 的全部未解决疑问。在每个疑问下方追加 `.anno-tutor` 回答，先给思路，涉及推导的给出关键步骤。不要改动我的原文，也不要替我把疑问标记为已解决。

**复测（QUIZ）：**

> QUIZ 模式：对 M04.2 做一次不看资料的复测，5 道题，覆盖推导和实现要点。我作答后评分，并说明是否达到 Mastered 的要求。

**更新进度（SYNC）：**

> SYNC 模式：把 M04.2 的学习状态改为 Reviewed，证据是 `make ex M=04` 全部通过（commit `<hash>`）和 `progress/diagnostics/` 中的自测记录。然后运行 `make sync` 与 `make check`。

**核实资料（VERIFY）：**

> VERIFY 模式：核查 M06.3 lesson 中的参考文献、e3nn API 用法和关于等变性的推导，列出问题清单，确认后再修改。

**处理勘误（VERIFY）：**

> VERIFY 模式：处理 `progress/open-questions.md` 中的全部勘误。逐条核实，属实的修正正文并在该批注中注明处理结果，不属实的在批注下说明理由。不要替我把勘误标记为已处理。

**研究问题驱动的学习：**

> 我在研究中遇到了锚点 A2 相关的问题（主动学习迭代后模型在目标构型上没有改进）。请根据 `docs/research-anchors.md` 和 `curriculum.yaml`，列出我需要补的章节及其当前状态，给出一个两周的插队学习计划，并更新 `ROADMAP.md`。

**周计划：**

> 根据 `ROADMAP.md` 和 `curriculum.yaml` 的当前状态，为我制定下周的学习计划（总计约 9 小时），并检查接下来两章是否已建设好；如未建设，列入本周 BUILD 任务。

**整理学习日志：**

> 我口述这周的学习情况，请按 `docs/learning-guide.md` 第 7 节的格式整理进 `progress/learning-log.md`，只记录我说的内容，不要补充。

**月度复盘：**

> 按 `templates/review-template.md` 准备本月复盘的框架：列出本月状态有变化的章节、未解决的疑问和到期复测。各项评价留给我填写。
