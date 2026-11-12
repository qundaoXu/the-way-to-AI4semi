"""讲义与实例 notebook 共用的 Nature 风格绘图样式。

讲义的代码单元和 ``modules/*/notebooks/`` 中的 notebook 都用这里的配色和 rcParams，
保证全站图表风格一致。用法::

    from semiai.plotting import BLUE, ORANGE, use_style
    use_style()

Plotly 交互图在 Quarto 页面里用 :func:`plotly_html` 输出，而不是 ``fig.show()``。
"""

from __future__ import annotations

from typing import Any

# 配色：以蓝色为主，暖棕与青色区分系列，灰色用于参照；不依赖红绿区分。
# 图的论点、面板顺序、坐标范围和数据由各章决定，公共样式只负责视觉编码。
BLUE = "#0f4d92"
ORANGE = "#b66b38"
AQUA = "#42949e"
PURPLE = "#7c6ccf"
GRAY = "#a8a8a8"
INK = "#272727"
MUTED = "#606060"
GRID = "#e5e5e5"
SURFACE = "#ffffff"

SERIES = (BLUE, ORANGE, AQUA, PURPLE)
CJK_FONTS = (
    "PingFang SC",
    "Heiti SC",
    "Hiragino Sans GB",
    "Noto Sans CJK SC",
    "Source Han Sans SC",
    "Microsoft YaHei",
)

RC_PARAMS: dict[str, Any] = {
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
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
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.axisbelow": True,
    "axes.labelsize": 9,
    "axes.titlesize": 10,
    "axes.titleweight": "normal",
    "grid.color": GRID,
    "grid.linewidth": 0.5,
    "lines.linewidth": 1.6,
    "lines.markersize": 4,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "font.family": "sans-serif",
    "font.size": 9,
    "legend.frameon": False,
    "legend.fontsize": 8,
    "mathtext.fontset": "dejavusans",
    # 西文采用 Nature 常用的 Arial / Helvetica，中文回退到本机 CJK 字体。
    "font.sans-serif": [
        "Arial",
        "Helvetica",
        "Liberation Sans",
        "DejaVu Sans",
    ],
    "axes.unicode_minus": True,
}


def use_style() -> None:
    """把全站统一的 rcParams 应用到当前 matplotlib 会话。"""
    import matplotlib as mpl
    from cycler import cycler
    from matplotlib.font_manager import fontManager

    mpl.rcParams.update(RC_PARAMS)
    # font.sans-serif 只选一个字体，不能逐字回退；把可用的中文字体加入 family，
    # 让 matplotlib 在同一标签中同时使用西文和 CJK 字形，避免中文变成方框。
    available = {font.name for font in fontManager.ttflist}
    cjk_font = next((font for font in CJK_FONTS if font in available), None)
    if cjk_font:
        mpl.rcParams["font.family"] = ["sans-serif", cjk_font]
    mpl.rcParams["axes.prop_cycle"] = cycler(color=list(SERIES))


def plotly_layout(**overrides: Any) -> dict[str, Any]:
    """交互图延续静态图的白底、字体和配色，嵌套参数可局部覆盖。"""
    axis = {
        "gridcolor": GRID,
        "showgrid": False,
        "zeroline": False,
        "showline": True,
        "linecolor": MUTED,
        "linewidth": 0.8,
        "ticks": "outside",
        "tickcolor": MUTED,
        "ticklen": 3,
        "automargin": True,
    }
    layout: dict[str, Any] = {
        "template": "none",
        "colorway": list(SERIES),
        "paper_bgcolor": SURFACE,
        "plot_bgcolor": SURFACE,
        "font": {
            "family": 'Arial, Helvetica, "PingFang SC", "Hiragino Sans GB", sans-serif',
            "size": 14,
            "color": INK,
        },
        "xaxis": axis.copy(),
        "yaxis": axis.copy(),
        "legend": {"orientation": "h", "y": 1.02, "x": 1, "xanchor": "right", "yanchor": "bottom"},
        "margin": {"l": 50, "r": 20, "t": 60, "b": 40},
        "height": 420,
    }
    for key, value in overrides.items():
        if isinstance(layout.get(key), dict) and isinstance(value, dict):
            layout[key].update(value)
        else:
            layout[key] = value
    if layout.get("sliders"):
        # 轴标题和滑块各占一行；固定底部空间，避免窄正文中互相覆盖。
        layout["height"] = max(layout["height"], 480)
        layout["margin"]["b"] = max(layout["margin"]["b"], 140)
        layout["sliders"] = [{"y": -0.25, **slider} for slider in layout["sliders"]]
    return layout


def plotly_html(fig: Any) -> Any:
    """把 Plotly 图转成可嵌入 Quarto 页面的 HTML 输出。

    不用 ``fig.show()``：Plotly 默认的 notebook 渲染器会再加载一份 MathJax 3，
    与页面自身的 MathJax 冲突，导致全页公式不渲染。
    """
    from IPython.display import HTML

    return HTML(fig.to_html(full_html=False, include_plotlyjs="cdn", include_mathjax=False))
