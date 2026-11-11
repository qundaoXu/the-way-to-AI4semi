# 学习指南

本页说明怎么用这个仓库学习：一章的学习流程、每周节奏、批注协议、实例 notebook 的用法、学习状态怎么记录。设计依据见 `PROJECT_BLUEPRINT.md` 第 5、6、10 节。

## 1. 三条基本约定

- **讲义讲原理，notebook 讲代码。** 每章一篇讲义加一个带运行结果的实例 notebook。notebook 可以直接读，也可以在 VS Code 里逐单元运行、改参数看变化。
- **掌握要有证据。** 学习状态由你自己修改；改为 `Reviewed` 或 `Mastered` 时要记录证据。
- **熟悉的章节快速通过。** 标为 `FT` 的章节，如果已经熟悉，只浏览精要并运行一遍 notebook。

现阶段不设练习桩、自测题和诊断测评。试点章节 M04.2 保留了一套从零实现的练习（第 5 节），可以选做。

## 2. 一章的学习流程

1. **看定位和学习目标**，判断这章要解决什么问题。
2. **读推荐资源**。讲义是导读、精要和桥接，不替代教材；推荐阅读精确到章节。
3. **读讲义**：先看直觉图，再读推导；需要时展开折叠的完整推导；拖动交互图观察参数的影响。
4. **边读边批注**（第 4 节）。读不懂的地方立刻记下疑问，不要攒着。
5. **跑实例 notebook**：从讲义“实例 Notebook”小节进入，在 VS Code 中从上到下运行，对照每节末尾的“读法”理解输出；再按“可以尝试”的方向改参数或代码。
6. **更新状态**，写学习日志。

状态随流程推进：开始阅读时改为 `Reading`，开始动手运行和改动 notebook 时改为 `Practicing`，跑通并能讲清楚每节输出后改为 `Reviewed`。

## 3. 每周节奏

按每周 8–10 小时估算：

| 内容 | 次数 | 每次时长 |
|---|---|---|
| 理论学习：读推荐资源、完成推导 | 2 | 约 1.5 小时 |
| 编码实践：运行并改动实例 notebook | 2 | 约 2 小时 |
| 复盘：写学习日志、更新状态 | 1 | 约 1 小时 |

每月末做一次月度复盘，每季度末更新五维能力自评并调整路线，格式见 `templates/review-template.md`。

## 4. 批注协议

批注直接写在讲义的 `.qmd` 源文件里。这样它们由 Git 管理，Agent 能读到，也能在原处回应。在网页上点击“在 VS Code 中编辑”打开源文件，用代码片段插入批注，保存后网页自动刷新。

| 用途 | 代码片段 | 写法 | Agent 的处理方式 |
|---|---|---|---|
| 重点高亮 | `am` | `[文字]{.mark}` | 不修改 |
| 我的理解 | `an` | `::: {.callout-note .anno-note title="我的理解"}` | 只读，可用于判断理解程度 |
| 疑问 | `aq` | `::: {.callout-important .anno-question .anno-open title="……"}` | TUTOR 模式在其后追加回答 |
| 勘误 | `ab` | `::: {.callout-caution .anno-bug .anno-open title="勘误"}` | VERIFY 模式核实后修正正文，并在批注中注明处理结果 |
| 研究联想 | `ai` | `::: {.callout-tip .anno-idea title="研究联想"}` | 只读；你要求时可汇总到研究锚点说明 |
| Agent 回答 | — | `::: {.callout-note .anno-tutor title="解答"}` | 由 Agent 写，你可以删改 |

### 示例

在讲义里某段话后面提出疑问：

```markdown
::: {.callout-important .anno-question .anno-open title="Ridge 回归的闭式解为什么总是存在？"}
我的推导卡在 $X^\top X + \lambda I$ 的可逆性上。
:::
```

保存后，这条疑问以橙色批注显示在原位置，并出现在首页和 `progress/open-questions.md` 中（运行 `make sync` 后）。让 Agent 以 TUTOR 模式处理，它会在疑问下方追加：

```markdown
::: {.callout-note .anno-tutor title="解答"}
提示：先说明 $X^\top X$ 的特征值为什么非负，再看加上 $\lambda I$ 之后特征值如何变化。
:::
```

你确认理解之后，把疑问的 `.anno-open` 改成 `.anno-resolved`。这一步只能由你来做。

其余三种写法：

```markdown
这里的 [收缩因子 $\sigma_i^2/(\sigma_i^2+\alpha)$]{.mark} 是理解 Ridge 的关键。

::: {.callout-note .anno-note title="我的理解"}
Ridge 相当于给每个奇异方向加一个低通滤波。
:::

::: {.callout-caution .anno-bug .anno-open title="勘误"}
式 5 的分母似乎少了平方。
:::

::: {.callout-tip .anno-idea title="研究联想"}
能量和力的损失权重是不是可以从这个角度理解？
:::
```

### 规则

- 你可以直接改正文，例如改写一句不清楚的解释。较长的个人内容写在批注里，避免与 Agent 之后的更新冲突。
- Agent 不删除、不改写你的批注和“我的笔记”。
- 你开始学习某章后（学习状态不是 `Not Started`），Agent 对该章只做局部修改；确需重写时先征得你同意，并保留全部批注。
- 批注的类名（`.anno-question` 等）不要改，样式、首页汇总和 Agent 检索都依赖它。
- 写在代码块里的批注示例（比如本页）不会被当作真正的批注。

## 5. 实例 notebook 与 M04.2 的练习

### 实例 notebook

每章在模块的 `notebooks/` 目录下有一个与讲义同名的 `.ipynb`，带执行输出提交，学习网站上也能直接阅读。在 VS Code 中打开，内核选仓库的 `.venv`，就可以逐单元运行。

- 随便改：notebook 是给你动手的，改坏了可以用 `git checkout -- <文件>` 恢复。
- 想保留改动后的输出：`make nb M=<模块号>` 重新执行该模块全部 notebook 并保存输出。
- 想做自己的探索而不影响原文件：另存到同目录的 `scratch/` 子目录，例如 `notebooks/scratch/try.ipynb`。这个目录被 Git 忽略，也不进网站；想长期保留的结论写进讲义的批注或“我的笔记”。

### M04.2 的练习（试点，选做）

试点章节 M04.2 保留了完整的练习–解答–测试机制，相关目录如下：

| 目录 | 内容 | 谁来写 |
|---|---|---|
| `exercises/` | 练习桩：函数签名、docstring、`raise NotImplementedError` | Agent 出题，**你来实现** |
| `solutions/` | 参考解答，用来证明测试可以通过 | Agent |
| `tests/` | 同一套测试，可以检查 `exercises/` 或 `solutions/` | Agent |
| `examples/` | 简短的概念演示 | Agent |

测试通过 `semiai.testing.load_impl` 加载实现，由环境变量 `LEARN_TARGET` 决定加载哪个目录，默认是 `exercises`。

```bash
make ex M=04                                                     # 检查你的实现
uv run pytest modules/04-classical-machine-learning/tests -k ols # 只跑一部分
LEARN_TARGET=solutions uv run pytest modules/04-*/tests          # 检查参考解答
```

测试优先采用这几类检验：与成熟框架对齐、与解析解比较、有限差分梯度检验、对称性与守恒律检验。失败信息通常能直接告诉你错在哪个性质上。

**求助的方式。** 向 Agent 要提示时说明要哪一级：方向提示、关键步骤、伪代码。先自己卡一会儿再问，问的时候贴出失败的测试名和你的思路。完整解答只在你明确要求时给出。自己通过之前不要看 `solutions/`。

**提交。** 练习代码由你自己提交，Agent 不改写这些提交。

## 6. 学习状态与证据

学习状态记录在讲义的 frontmatter 里，归你所有。

| 状态 | 含义 | 进入条件 |
|---|---|---|
| `Not Started` | 尚未开始 | — |
| `Reading` | 正在学习理论 | 开始阅读 |
| `Practicing` | 正在动手 | 开始运行和改动实例 notebook |
| `Reviewed` | 完成复习 | 跑通实例 notebook，能解释每节的输出；M04.2 另需练习测试全部通过 |
| `Mastered` | 达到章节验收目标 | 以上条件，加上不看资料完成一次讲解复述；P1 章节另需一项应用证据 |

```bash
make status ID=M04.2 S=Practicing
make status ID=M04.2 S="Not Started"     # 状态含空格时加引号
```

也可以直接编辑 frontmatter 后运行 `make sync`。改为 `Reviewed` 或 `Mastered` 时，在 `evidence` 里记录证据，例如：

```yaml
learn_status: Reviewed
evidence:
  - "make ex M=04 全部通过，commit 1a2b3c4"
  - "跑通 notebooks/02-linear-models.ipynb，第 3 节改用 Lasso 做了对比"
next_review: 2027-01-20
```

`Mastered` 的章节可以在 `next_review` 写一个回顾日期，到期后会出现在首页。

建设状态是另一回事，它描述讲义和代码的质量，由 Agent 在 `curriculum.yaml` 中维护：

| 状态 | 含义 |
|---|---|
| `Planned` | 已列入计划，还没有讲义 |
| `Draft` | 有讲义初稿和实例 notebook，通过了渲染与检查，但内容未经独立检查 |
| `Reviewed` | 内容经过一次独立检查（你读过，或 Agent 以 VERIFY 模式核查过） |
| `Verified` | 独立核查完成，notebook 与讲义代码在实际环境中重新运行过 |

## 7. 属于你的文件

下面这些内容只由你写，Agent 不会凭空生成。文件在你第一次需要时创建。

| 文件 | 内容 |
|---|---|
| 讲义 frontmatter 的 `learn_status`、`evidence`、`next_review` | 学习状态与证据 |
| 讲义中的批注和“我的笔记”小节 | 你的理解、疑问、联想 |
| `progress/learning-log.md` | 学习日志：日期、章节、完成内容、实践代码、未解决问题、下一步 |
| `progress/skills-matrix.md` | 五维能力自评（理论、实现、实验评价、工程、领域整合），每季度更新 |
| `modules/<模块>/concept-map.qmd` | 可选：用 Mermaid 画的模块概念图 |

你口述学习情况时，Agent 可以帮忙整理成日志格式。

## 8. 学习顺序

默认按 [Path B](../learning-paths/path-b-ai-for-science.md) 的顺序学习。研究任务临时需要某个靠后的章节时可以插队，先看它的先修章节是否已建设。

## 9. 与 Agent 协作

Agent 有四种工作模式：BUILD（建设章节）、TUTOR（答疑与讲解）、SYNC（维护索引）、VERIFY（核实资料与推导）。可以直接复制的指令见 [Agent 指令库](agent-prompts.md)。内容按模块建设：一次建设一个模块的全部章节，建完交给你过目。
