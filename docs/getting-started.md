# 快速开始

本页说明如何在一台新机器上把仓库跑起来：安装环境、启动学习网站、配置 VS Code、运行第一组练习测试。

## 1. 前置软件

| 软件 | 用途 | 说明 |
|---|---|---|
| [uv](https://docs.astral.sh/uv/) | Python 环境与依赖管理 | 会按 `.python-version` 自动准备 Python 3.12 |
| Git、GNU Make | 版本管理、命令入口 | macOS 与 Linux 自带或用包管理器安装 |
| [VS Code](https://code.visualstudio.com/) | 编辑、批注、练习、测试 | 扩展见第 4 节 |
| Quarto | 渲染学习网站 | **不需要单独安装**，见下文 |

本仓库在 2026-11-11 搭建并验证时使用的版本：Quarto 1.11.9，Python 3.12，uv 0.11。

### 关于 Quarto 的安装方式

蓝图原计划单独安装 Quarto CLI。实际采用的做法是把 Quarto 官方的 PyPI 发行版 `quarto-cli` 放进 `pyproject.toml` 的 `site` 依赖组：`make setup` 时它被装进 `.venv`，版本由 `uv.lock` 锁定，本机和 CI 用的是同一个版本，`make preview`、`make site` 通过 `uv run quarto` 调用它。

如果你已经用安装包或 Homebrew 装过 Quarto，想用系统里的那一份，可以 `uv sync --no-group site`，此时 `uv run quarto` 会找到 PATH 上的 Quarto。

## 2. 安装

```bash
git clone https://github.com/qundaoXu/the-way-to-AI4semi.git
cd the-way-to-AI4semi
make setup      # 创建 .venv，安装 semiai（可编辑模式）、dev 依赖、Quarto，并启用 pre-commit
make check      # 验证：ruff + 参考解答测试 + 仓库一致性 + 索引检查
```

`make check` 全部通过，说明环境正常。

### 依赖分组

`pyproject.toml` 的 `dependencies` 只有核心科学栈（NumPy、SciPy、pandas、Matplotlib、scikit-learn、Plotly）和渲染所需的 Jupyter 组件。重量级依赖只在某章确实需要时才加入，届时放在这些 extras 里：

| extra | 内容 | 首次需要的章节 |
|---|---|---|
| `dl` | PyTorch | M05 |
| `geometric` | e3nn、PyTorch Geometric | M06.2、M06.3 |
| `atomistic` | ASE、pymatgen | M01.2、M07 |
| `boosting` | XGBoost、LightGBM | M04.4 |
| `mlops` | MLflow 等 | M09.2 |

这些 extras 目前都还没有定义。

### PyTorch 的 CPU 与 CUDA 版本

PyTorch 尚未加入依赖。建设 M05 时再确定安装方式，原则是：本地开发与 CI 用 CPU 版，练习默认在 CPU 上数分钟内跑完；集群上按 CUDA 版本从 PyTorch 官方索引安装对应的 wheel，需要 GPU 的测试用 `@pytest.mark.gpu` 标记，默认不运行。具体命令在加入 `dl` extra 时补充到这里。

## 3. 学习网站

```bash
make preview    # 启动本地网站（默认 http://localhost:4848），保存源文件后页面自动刷新
make site       # 完整渲染到 _site/，用于检查全部页面能否成功渲染
```

- 讲义里的 `{python}` 代码单元在渲染时执行。执行结果缓存在 `_freeze/`（提交到仓库），只改文字或批注时不会重新执行代码。
- 首页仪表盘读取 `progress/status.json`。`make sync`、`make status`、`make ex` 在更新它之后会刷新首页。
- 公式使用 MathJax，交互图使用 Plotly，两者的脚本从 CDN 加载，首次打开页面需要联网。
- 右上角的按钮切换浅色与深色模式。
- 只在本地渲染时，页面顶部有“在 VS Code 中编辑”按钮，讲义中指向 `.py` 文件的链接也会直接在 VS Code 中打开。

## 4. VS Code

用 VS Code 打开仓库根目录，按提示安装推荐扩展（`.vscode/extensions.json`）：Quarto、Python、Pylance、Jupyter、Ruff。然后在命令面板里执行 “Python: Select Interpreter”，选择 `.venv`。

仓库里已经提交的配置：

| 文件 | 作用 |
|---|---|
| `.vscode/settings.json` | 启用 pytest 测试面板；解释器指向 `.venv`；读取 `.env`；Quarto 保存即渲染 |
| `.env` | `LEARN_TARGET=exercises`，测试面板默认检查你自己的实现 |
| `.vscode/semiai.code-snippets` | 批注代码片段：`aq` 疑问、`an` 我的理解、`ab` 勘误、`ai` 研究联想、`am` 高亮 |

编辑 `.qmd` 时，可以用源码编辑器，也可以用 Quarto 扩展的可视化编辑器（命令 “Quarto: Edit in Visual Mode”），两者改的是同一个文件。单屏工作时，命令 “Quarto: Preview” 可以在 VS Code 内部打开预览面板。

## 5. 常用命令

| 命令 | 作用 |
|---|---|
| `make setup` | 创建环境并安装全部依赖 |
| `make check` | `ruff check` + 以参考解答运行全部测试 + `check_repo.py` + `sync_index.py --check` |
| `make ex M=04` | 用你自己的练习实现运行模块 04 的测试，结果写入 `progress/test-results.json` |
| `make sync` | 重新生成索引：`CURRICULUM.md`、模块 README 章节表、`progress/` 下的清单 |
| `make test-src` | 只运行公共包 `semiai` 的测试 |
| `make preview` / `make site` | 启动本地网站 / 完整渲染 |
| `make status ID=M04.2 S=Practicing` | 修改某章的学习状态并同步索引 |

pytest 标记 `slow`（超过约 1 分钟）和 `gpu` 默认不运行；需要时用 `uv run pytest -m slow`。

## 6. 第一次使用

1. `make preview`，在浏览器里打开首页；
2. 进入“04 传统机器学习 → 线性模型”，这是试点章节；
3. `make ex M=04`：此时全部测试失败（`NotImplementedError`），这是预期的起点；
4. 按 [学习指南](learning-guide.md) 的流程开始学习。

## 7. 常见问题

**`make check` 报“索引过期”。** 改过 `curriculum.yaml` 或讲义 frontmatter 后没有同步，运行 `make sync`。

**页面上公式显示为源码。** MathJax 脚本没有加载成功，检查网络后刷新。

**讲义改了代码单元但图没变。** `_freeze/` 的缓存按源文件内容判断是否重新执行；确认保存了文件。需要强制重新执行时，删除 `_freeze/` 下对应讲义的目录后重新渲染。

**测试面板里看不到测试。** 确认解释器选的是 `.venv`，再执行 “Test: Refresh Tests”。
