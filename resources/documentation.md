# 官方文档

本文件收录蓝图第 16.5 节中的官方文档与"学习环境"相关文档。所有链接均已于 2026-11-11 在线核实可访问且标题与内容相符；括号中的版本号是核实当日页面显示的版本。

## 机器学习与深度学习框架

- **scikit-learn developers. *scikit-learn documentation*.** [文档首页](https://scikit-learn.org/stable/) · [User Guide](https://scikit-learn.org/stable/user_guide.html) — 经典机器学习算法的 API 与用户指南（核实时为 1.9.1）；User Guide 对每类方法有原理说明，可与教材对照。
- **PyTorch. *PyTorch documentation*.** [文档首页](https://docs.pytorch.org/docs/stable/index.html) · [Tutorials](https://docs.pytorch.org/tutorials/) — 张量、自动微分与 `torch.nn` 的 API 参考及官方教程。
- **PyG Team. *PyG (PyTorch Geometric) Documentation*.** [文档首页](https://pytorch-geometric.readthedocs.io/en/latest/) — 图数据结构、消息传递层与数据集加载的参考文档。
- **e3nn developers. *e3nn: Euclidean neural networks*.** [文档首页](https://docs.e3nn.org/en/latest/) — 不可约表示、球谐函数与张量积的 API 说明（核实时为 0.5.1）。

## 原子模拟与材料工具

- **ASE developers. *Atomic Simulation Environment documentation*.** [文档首页](https://docs.ase-lib.org/) · [社区主页](https://ase-lib.org/) — `Atoms` 对象、计算器接口、结构优化与分子动力学的参考文档。
- **Materials Project. *pymatgen documentation*.** [文档首页](https://pymatgen.org/) — 晶体结构、对称性分析、相图与文件格式转换的参考文档。

## 学习环境：Quarto

- **Posit. *Quarto – Creating a Website*.** [文档](https://quarto.org/docs/websites/) — 网站项目的 `_quarto.yml`、导航与渲染流程。
- **Posit. *Quarto – Cross References*.** [文档](https://quarto.org/docs/authoring/cross-references.html) — 图、表、公式、章节的标签与引用语法。
- **Posit. *Quarto – Callout Blocks*.** [文档](https://quarto.org/docs/authoring/callouts.html) — note、tip、warning 等提示块的写法与折叠选项。
- **Posit. *Quarto – Article Layout*.** [文档](https://quarto.org/docs/authoring/article-layout.html) — 页面布局、页边内容（margin）与旁注。
- **Posit. *Quarto – Execution Options*.** [文档](https://quarto.org/docs/computations/execution-options.html) — 代码块的 `eval`、`echo`、`output` 等执行选项。
- **Posit. *Quarto – Caching*.** [文档](https://quarto.org/docs/computations/caching.html) — Jupyter Cache 与 knitr 缓存的启用方式。
- **Posit. *Quarto – Managing Execution*.** [文档](https://quarto.org/docs/projects/code-execution.html) — 项目级执行控制与 `freeze`，用于避免重复运行耗时计算。
- **Posit. *Quarto – Observable JS*.** [文档](https://quarto.org/docs/interactive/ojs/) — 在页面内用 OJS 编写交互式图表与控件。
- **Posit. *Quarto – VS Code*.** [文档](https://quarto.org/docs/tools/vscode/index.html) — Quarto VS Code 扩展的预览、代码块执行与编辑功能说明。
- **r-wasm. *Quarto Live Documentation*.** [文档](https://r-wasm.github.io/quarto-live/) · [源码](https://github.com/r-wasm/quarto-live) — `quarto-live` 扩展：在浏览器内通过 WebAssembly 运行 R/Python 代码块与练习题（MIT 许可）。

## 与蓝图种子清单的差异

- **PyTorch 文档**：`pytorch.org/docs` 与 `pytorch.org/tutorials` 现重定向到 `docs.pytorch.org`，本文件使用新地址。
- **ASE**：原地址 `wiki.fysik.dtu.dk/ase/` 现重定向到社区主页 `ase-lib.org`，文档位于 `docs.ase-lib.org`。
- **Quarto VS Code 扩展文档**：`quarto.org/docs/tools/vscode.html` 现为跳转页，实际内容在 `quarto.org/docs/tools/vscode/index.html`。
- **Quarto "代码执行与缓存"**：蓝图为一项，实际对应三页文档（Execution Options、Caching、Managing Execution/freeze），已分别列出。
