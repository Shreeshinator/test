"""Scene 11 (10:15-10:55) — the actual eigenpairs of our C, and why the largest wins."""

from manim import *
import numpy as np
from pca.common import (
    BG, INK, MUTED, COL_CENTR, COL_MATRIX, COL_NOTE, COL_PC1, COL_PC2,
    base_axes, axes_labels, make_dots, screen_title, scene_tag, eq, note, pc_line, CENTERED,
)

PX = 0.35          # left edge of the right-hand computation panel
PW = 3.95          # panel nominal centre


def panel_line(tex, y, font, color, align_left=True):
    m = MathTex(tex, font_size=font, color=color)
    m.move_to([PX + m.width / 2, y, 0])
    return m


class Scene11Apply(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 10 — The actual answer for our data")
        tag = scene_tag(11, "Solving for the eigenpairs")
        axes = base_axes()
        labels = axes_labels(axes)
        dots = make_dots(axes, CENTERED, COL_CENTR)

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.play(Create(axes), FadeIn(labels), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.15), run_time=1.0)
        self.wait(4.0)

        # --- solve det(C - λI) = 0 --------------------------------------------
        head = Text("Solve det(C − λI) = 0", font_size=19, color=COL_MATRIX)
        head.move_to([PX + head.width / 2, 2.15, 0])
        self.play(FadeIn(head), run_time=0.4)

        d1 = panel_line(r"\left(\tfrac{10}{3} - \lambda\right)^2 - \left(\tfrac{8}{3}\right)^2 = 0",
                        1.62, 17, INK)
        self.play(Write(d1), run_time=1.0)
        d2 = panel_line(r"\tfrac{10}{3} - \lambda = \pm \tfrac{8}{3}", 1.12, 17, INK)
        self.play(Write(d2), run_time=0.8)
        d3 = panel_line(r"\lambda_1 = 6 \qquad \lambda_2 = \tfrac{2}{3}", 0.66, 21, INK)
        self.play(Write(d3), run_time=0.8)
        self.wait(4.0)

        # --- eigenvectors ------------------------------------------------------
        d4a = panel_line(r"\lambda_1 = 6:\;\; -\tfrac{8}{3} v_x + \tfrac{8}{3} v_y = 0",
                         0.02, 15.5, COL_PC1)
        d4b = panel_line(r"v_1 = \tfrac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}",
                         -0.48, 19, COL_PC1)
        d5a = panel_line(r"\lambda_2 = \tfrac{2}{3}:\;\; \tfrac{8}{3} v_x + \tfrac{8}{3} v_y = 0",
                         -1.02, 15.5, COL_PC2)
        d5b = panel_line(r"v_2 = \tfrac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -1 \end{bmatrix}",
                         -1.52, 19, COL_PC2)
        self.play(Write(d4a), run_time=0.9)
        self.play(Write(d4b), run_time=0.8)
        self.play(Write(d5a), run_time=0.9)
        self.play(Write(d5b), run_time=0.8)
        self.wait(4.0)

        # --- show the two directions on the plot --------------------------------
        pc1 = pc_line(axes, (1, 1), 2.85, COL_PC1, stroke_width=6)
        pc2 = pc_line(axes, (1, -1), 2.2, COL_PC2, stroke_width=4)
        pc1_lbl = MathTex("PC1", font_size=20, color=COL_PC1)
        pc1_lbl.move_to(axes.c2p(2.62, 2.62) + RIGHT * 0.32)
        pc2_lbl = MathTex("PC2", font_size=20, color=COL_PC2)
        pc2_lbl.move_to(axes.c2p(2.05, -2.05) + RIGHT * 0.32 + DOWN * 0.1)
        self.play(Create(pc1), FadeIn(pc1_lbl), run_time=0.9)
        self.play(Create(pc2), FadeIn(pc2_lbl), run_time=0.9)
        self.wait(6.4)

        # --- why the largest eigenvalue ------------------------------------------
        head2 = Tex("Why the largest?", font_size=16, color=COL_NOTE)
        head2.move_to([PX + head2.width / 2, -2.05, 0])
        w1 = panel_line(r"u = a v_1 + b v_2, \quad a^2 + b^2 = 1", -2.38, 15, INK)
        w2 = panel_line(r"u^T C u = 6 a^2 + \tfrac{2}{3} b^2 = 6 - \tfrac{16}{3} b^2 \leq 6",
                        -2.76, 14.5, INK)
        w3 = note("maximum exactly when b = 0, i.e. u = ±v₁", font_size=13, color=COL_PC1)
        w3.move_to([PX + w3.width / 2, -3.16, 0])
        self.play(FadeIn(head2), Write(w1), run_time=0.8)
        self.play(Write(w2), run_time=1.0)
        self.play(FadeIn(w3), run_time=0.5)
        self.wait(8.5)
