"""Shared visual vocabulary for the PCA video.

Every scene imports from here so the coordinate system, palette, typography,
point placement and panel layout stay perfectly consistent across the film.
"""

from __future__ import annotations

import numpy as np
from manim import (
    Axes,
    Arrow,
    Circle,
    Cross,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    GrowArrow,
    Line,
    MathTex,
    SurroundingRectangle,
    Tex,
    Text,
    VGroup,
    Write,
    Create,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    DEGREES,
    ORIGIN,
    WHITE,
)

# ---------------------------------------------------------------- palette ---
BG        = "#10151C"   # dark neutral background
INK       = "#EDEFF2"   # primary text (off-white)
MUTED     = "#8B95A5"   # secondary text / ticks
AXES_COL  = "#55606E"   # axis lines
GRID_COL  = "#1B2330"   # faint grid
COL_DATA  = "#4CC9F0"   # original data points
COL_CENTR = "#80ED99"   # centred data points
COL_MEAN  = "#EF476F"   # the mean
COL_MATRIX= "#B388FF"   # scatter / covariance matrix accents
COL_U     = "#FFD166"   # the test direction u
COL_PC1   = "#FF9F1C"   # first principal component
COL_PC2   = "#3A86FF"   # second principal component
COL_NOTE  = "#9FB3C8"   # small annotation text

# ------------------------------------------------------------- the dataset --
POINTS      = [(5, 3), (1, 1), (4, 4), (2, 0)]
CENTERED    = [(2, 1), (-2, -1), (1, 2), (-1, -2)]
MEAN        = (3, 2)
SCATTER_TEX = r"\begin{bmatrix} 10 & 8 \\ 8 & 10 \end{bmatrix}"
COV_TEX     = r"\begin{bmatrix} \frac{10}{3} & \frac{8}{3} \\[2pt] \frac{8}{3} & \frac{10}{3} \end{bmatrix}"

# Column-vector LaTeX for each centred observation (kept ready for reuse).
CENTERED_COLS = [
    r"\begin{bmatrix} 2 \\ 1 \end{bmatrix}",
    r"\begin{bmatrix} -2 \\ -1 \end{bmatrix}",
    r"\begin{bmatrix} 1 \\ 2 \end{bmatrix}",
    r"\begin{bmatrix} -1 \\ -2 \end{bmatrix}",
]
OUTER_PRODUCTS = [
    r"\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}",
    r"\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}",
    r"\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}",
    r"\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}",
]

# ------------------------------------------------------------ axes geometry -
AXES_X_RANGE = [-4, 6, 2]      # span 10 -> x_length = 10 * UNIT
AXES_Y_RANGE = [-2.5, 5.5, 2]  # span 8  -> y_length = 8 * UNIT
UNIT = 0.62                    # equal x/y scale: angles are shown honestly
AXES_POS = LEFT * 3.75 + DOWN * 0.45

PANEL_CENTER_X = 3.35          # centre of the right-hand equation panel
PANEL_WIDTH = 6.6


def base_axes() -> Axes:
    """The one and only coordinate system used across every scatter scene."""
    axes = Axes(
        x_range=AXES_X_RANGE,
        y_range=AXES_Y_RANGE,
        x_length=10 * UNIT,
        y_length=8 * UNIT,
        tips=False,
        axis_config={
            "color": AXES_COL,
            "stroke_width": 2,
            "tick_size": 0.055,
            "include_ticks": True,
        },
    ).move_to(AXES_POS)
    return axes


def axes_labels(axes: Axes) -> VGroup:
    xlab = MathTex("x", font_size=28, color=INK)
    xlab.next_to(axes.x_axis, RIGHT, buff=0.12)
    ylab = MathTex("y", font_size=28, color=INK)
    ylab.next_to(axes.y_axis, UP, buff=0.08)
    return VGroup(xlab, ylab)


def make_dots(axes: Axes, points, color, radius=0.095) -> VGroup:
    return VGroup(*[Dot(axes.c2p(*p), radius=radius, color=color, z_index=6) for p in points])


def point_label(axes: Axes, p, text: str, color=INK, direction=UP, buff=0.07, font_size=17):
    lbl = MathTex(text, font_size=font_size, color=color)
    lbl.next_to(axes.c2p(*p), direction, buff=buff)
    return lbl


def mean_marker(axes: Axes) -> VGroup:
    dot = Dot(axes.c2p(*MEAN), radius=0.115, color=COL_MEAN, z_index=7)
    ring = Circle(radius=0.19, color=COL_MEAN, stroke_width=2.5).move_to(dot)
    return VGroup(dot, ring)


def screen_title(text: str) -> Text:
    return Text(text, font_size=30, color=INK, weight="BOLD").to_edge(UP, buff=0.28)


def scene_tag(idx: int, name: str) -> Text:
    return Text(f"PCA · {idx:02d} · {name}", font_size=16, color=MUTED).to_corner(
        LEFT + DOWN, buff=0.22
    )


def eq(tex: str, font_size: int = 30, color=INK) -> MathTex:
    return MathTex(tex, font_size=font_size, color=color)


def panel_heading(text: str) -> Tex:
    return Tex(text, font_size=24, color=COL_MATRIX)


def note(text: str, font_size: int = 17, color=COL_NOTE) -> Text:
    return Text(text, font_size=font_size, color=color)


def unit_vector(axes: Axes, direction, length=2.45, color=COL_U, stroke_width=5) -> Arrow:
    d = np.array(direction, dtype=float)
    d = d / np.linalg.norm(d)
    return Arrow(
        axes.c2p(0, 0),
        axes.c2p(d[0] * length, d[1] * length),
        buff=0,
        stroke_width=stroke_width,
        tip_length=0.24,
        color=color,
    )


def projection(axes: Axes, point, direction, color=COL_U) -> tuple[Dot, Dot, DashedLine]:
    """Return (foot dot, source dot, dashed connector) for one projection."""
    d = np.array(direction, dtype=float)
    d = d / np.linalg.norm(d)
    p = np.array(point, dtype=float)
    foot = d * float(np.dot(d, p))
    foot_dot = Dot(axes.c2p(*foot), radius=0.07, color=color, z_index=6)
    src_dot = Dot(axes.c2p(*p), radius=0.095, color=COL_CENTR, z_index=6)
    dash = DashedLine(
        axes.c2p(*p), axes.c2p(*foot), color=MUTED, stroke_width=2.2, dash_length=0.09
    )
    return foot_dot, src_dot, dash


def pc_line(axes: Axes, direction, length, color, stroke_width=6) -> Line:
    """A line through the origin along `direction` (both ways)."""
    d = np.array(direction, dtype=float)
    d = d / np.linalg.norm(d)
    return Line(
        axes.c2p(-d[0] * length, -d[1] * length),
        axes.c2p(d[0] * length, d[1] * length),
        stroke_width=stroke_width,
        color=color,
    )
