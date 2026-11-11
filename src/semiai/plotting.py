"""讲义与实例 notebook 共用的绘图样式。

讲义的代码单元和 ``modules/*/notebooks/`` 中的 notebook 都用这里的配色和 rcParams，
保证全站图表风格一致。用法::

    from semiai.plotting import BLUE, ORANGE, use_style
    use_style()

Plotly 交互图在 Quarto 页面里用 :func:`plotly_html` 输出，而不是 ``fig.show()``。
"""

from __future__ import annotations

from typing import Any

# 配色：前三个用于数据系列，其余用于文字、坐标轴和背景。
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
PURPLE = "#8a5cc7"
GRAY = "#a9a79d"
INK = "#0b0b0b"
MUTED = "#52514e"
GRID = "#e4e2da"
SURFACE = "#fcfcfb"

SERIES = (BLUE, ORANGE, AQUA, PURPLE)

RC_PARAMS: dict[str, Any] = {
    "figure.dpi": 150,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "text.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "lines.linewidth": 2.0,
    "font.size": 10,
    "legend.frameon": False,
    "mathtext.fontset": "cm",
    # macOS / Linux 上常见的中文字体，找不到时 matplotlib 依次回退。
    "font.sans-serif": [
        "PingFang SC",
        "Hiragino Sans GB",
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "Microsoft YaHei",
        "DejaVu Sans",
    ],
    "axes.unicode_minus": False,
}


def use_style() -> None:
    """把全站统一的 rcParams 应用到当前 matplotlib 会话。"""
    import matplotlib as mpl
    from cycler import cycler

    mpl.rcParams.update(RC_PARAMS)
    mpl.rcParams["axes.prop_cycle"] = cycler(color=list(SERIES))


def plotly_layout(**overrides: Any) -> dict[str, Any]:
    """Plotly 图的统一布局参数，可用关键字覆盖。"""
    layout: dict[str, Any] = {
        "paper_bgcolor": SURFACE,
        "plot_bgcolor": SURFACE,
        "font": {"color": INK},
        "xaxis": {"gridcolor": GRID, "zeroline": False},
        "yaxis": {"gridcolor": GRID, "zeroline": False},
        "legend": {"orientation": "h", "y": 1.02, "x": 1, "xanchor": "right", "yanchor": "bottom"},
        "margin": {"l": 50, "r": 20, "t": 60, "b": 40},
        "height": 420,
    }
    layout.update(overrides)
    return layout


def plotly_html(fig: Any) -> Any:
    """把 Plotly 图转成可嵌入 Quarto 页面的 HTML 输出。

    不用 ``fig.show()``：Plotly 默认的 notebook 渲染器会再加载一份 MathJax 3，
    与页面自身的 MathJax 冲突，导致全页公式不渲染。
    """
    from IPython.display import HTML

    return HTML(fig.to_html(full_html=False, include_plotlyjs="cdn", include_mathjax=False))
