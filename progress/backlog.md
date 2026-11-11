# 待建设任务队列

由 Agent 维护。内容按模块建设：一次建设一个模块的全部章节（讲义 + 实例 notebook），建完交学习者过目。完成的条目直接删除，历史见 Git 记录。

## 建设方式调整（2026-11-11，学习者决定）

- 每章只交付讲义和带输出的实例 notebook；不再新建练习桩、参考解答、测试；不出诊断题和自测题，QUIZ 模式暂停。
- [ ] 确认蓝图第 1.5 节的预设参数：每周可投入时间（默认 8–10 小时）、主路径（默认 Path B）。

## 模块建设队列

按 Path B 的顺序：

- [ ] Module 02 数学、统计与最优化（M02.1 建成后，把 M04.2 讲义第 2 节的前置说明改为链接）
- [ ] Module 04 其余章节（M04.1、M04.3–M04.8）
- [ ] Module 03、Module 05

## Module 01 的后续（2026-11-11 建设为 Draft）

- [ ] 学习者过目后，或 VERIFY 模式核查后，把 M01.1–M01.5 的建设状态提升到 `Reviewed`。
- [ ] 核实标注 `[待核实]` 的资料：Fluent Python 第 2 版出版信息、Matula 1968（M01.1）；CLRS 第 4 版第 3 章标题、Allen & Tildesley 邻居表所在小节、Franzblau 1991（M01.2）；Pro Git 出版社（M01.3）；Goldberg 1991 卷期页码（M01.4）；*High Performance Python* 第 2 版章节标题（M01.5）。
- [ ] 核实正文中的几处定性说法：PyTorch `torch.load` 默认 `weights_only=True` 的起始版本（M01.1）；ASE `neighbor_list("ijD", ...)` 的返回形式（M01.5，ASE 未安装）；GPU MD 代码的混合精度模式（M01.4）。
- [ ] notebook 的计时结果来自 Apple M4（macOS），M01.3 的 shell/Git 输出未在 Linux 上验证。

## 试点章节 M04.2 的后续

- [ ] 学习者阅读后，或 VERIFY 模式核查后，把建设状态从 `Draft` 提升到 `Reviewed`。
- [ ] `hastie.su.domains`（ESL 官方页面）在 2026-11-11 核实时访问超时，稍后复查讲义和 `resources/textbooks.md` 中的这个链接。

## 需要学习者在本机确认的验收项

下面几项依赖浏览器和 VS Code 的图形界面，Phase 1 中无法自动验证：

- [ ] 点击网页上的“在 VS Code 中编辑”能打开对应源文件。
- [ ] 在 VS Code 中用代码片段 `aq` 插入疑问并保存，网页自动刷新并显示该批注。
- [ ] VS Code 测试面板默认以 `exercises` 为目标运行 M04.2 的测试。
- [ ] 浅色与深色模式下，试点讲义的图、公式、页边注、折叠推导和交互图的实际观感。

## 资料核实

`resources/` 和 `datasets/README.md` 中标注 `[待核实]` 的条目，多数是出版社页面拒绝自动访问。用到对应资料时手工核对一次并去掉标注。

## 以后再做

- 发布构建（蓝图第 6.8 节，Phase 3 之后）：`theme/semiai.lua` 已支持 `--profile publish` 时剥离批注和本机路径，但还没有建立排除 `progress/` 的 profile 配置文件。
- `pyproject.toml` 的 optional extras（`dl`、`geometric`、`atomistic`、`boosting`、`mlops`）在首次需要的章节建设时再定义。
- `semiai.testing` 的等变性检验与随机旋转生成，在 M02.7 建设时加入。
- 第 3 个月末评估学习环境的摩擦点，决定是否需要增量工具（蓝图第 6.9 节）。
