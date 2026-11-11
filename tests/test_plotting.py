"""semiai.plotting 共用绘图样式的测试。"""

from __future__ import annotations

import re

import matplotlib

matplotlib.use("Agg")

import matplotlib as mpl  # noqa: E402

from semiai import plotting  # noqa: E402


def test_palette_is_valid_hex() -> None:
    for color in (*plotting.SERIES, plotting.INK, plotting.MUTED, plotting.GRID, plotting.SURFACE):
        assert re.fullmatch(r"#[0-9a-f]{6}", color)


def test_use_style_sets_rcparams_and_cycle() -> None:
    plotting.use_style()
    assert mpl.rcParams["axes.facecolor"] == plotting.SURFACE
    assert mpl.rcParams["axes.prop_cycle"].by_key()["color"][:2] == [
        plotting.BLUE,
        plotting.ORANGE,
    ]


def test_plotly_layout_overrides() -> None:
    layout = plotting.plotly_layout(height=300)
    assert layout["height"] == 300
    assert layout["paper_bgcolor"] == plotting.SURFACE
