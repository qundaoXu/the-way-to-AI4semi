# %% [raw]
# ---
# title: "Mxx.y 实例：章节中文名"
# subtitle: "Worked Examples · English Title"
# ---

# %% [markdown]
# <!--
# 实例讲解 notebook 模板（Jupytext percent 格式，只用于起草）。
#
# 生成与执行：
#   uv run jupytext --to ipynb --set-kernel python3 templates/notebook-template.py \
#       -o modules/NN-xxx/notebooks/<讲义同名>.ipynb
#   make nb M=NN
# 仓库中以 .ipynb 为准，带执行输出提交；之后直接在 VS Code 里编辑 .ipynb。
#
# 要求：
# - 第一个 Markdown 单元写明章节 ID 和讲义链接（check_repo.py 检查章节 ID 是否出现）；
# - 每节 = 一段说明（要看什么、为什么）→ 代码 → 输出 → 一段“读法”（输出说明了什么）；
# - 讲义里的公式用链接引用：[讲义式名称](../notes/<讲义>.qmd#eq-xxx)，不用 @eq-xxx；
# - 全部单元在 CPU 上合计约 1 分钟内跑完，只用 pyproject.toml 中已声明的依赖；
# - 随机性用 np.random.default_rng(seed)；结果和结论必须来自实际运行的输出；
# - 不设自测题；结尾给小结和“可以尝试”的改动方向；
# - 通过 ruff check（行宽 100）。
# 写完删除本注释。
# -->
#
# 本 notebook 是 [Mxx.y 章节名](../notes/xx-slug.qmd) 的实例讲解。内容：
#
# 1. ……
# 2. ……
#
# **运行方式**：在 VS Code 中打开本文件，选择仓库 `.venv` 的 Python 内核，从上到下运行。
# 改动代码后可用 `make nb M=NN` 重新执行并保存输出。

# %%
import matplotlib.pyplot as plt
import numpy as np

from semiai.plotting import BLUE, use_style

use_style()
rng = np.random.default_rng(0)

# %% [markdown]
# ## 1. 小节标题
#
# 说明这一节要观察什么。

# %%
x = np.linspace(0, 1, 50)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, x**2, color=BLUE)
plt.show()

# %% [markdown]
# 读法：输出说明了什么，与讲义哪个结论对应。
#
# ## 小结
#
# - ……
#
# 可以尝试：……
