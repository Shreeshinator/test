"""Scene 10 (9:20-10:15) — eigenvectors: definition, and λ as variance.

Layout: left column = two small geometric demos (kept direction / rotated
direction); right column = definition, the λ = Var identity, PSD, orthogonality.
"""

from manim import *
import numpy as np
from pca.common import (
    BG, INK, MUTED, COL_U, COL_PC1, COL_MATRIX, COL_NOTE, COL_PC2,
    screen_title, scene_tag, eq, note,
)


class Scene10Eigenvectors(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 9 — Directions that keep their line")
        tag = scene_tag(10, "Eigenvectors")
        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)


        # --- LEFT, top demo: C keeps the direction ---------------------------
        # --- LEFT, top demo: C keeps the direction (parallel before/after) ---
        o1 = np.array([-6.15, 0.55, 0])
        o2t = np.array([-3.35, 0.55, 0])
        self.play(FadeIn(Dot(o1, radius=0.07, color=INK)),
                  FadeIn(Dot(o2t, radius=0.07, color=INK)), run_time=0.3)
        v_tip = o1 + np.array([1.05, 1.05, 0])
        cv_tip = o2t + np.array([1.95, 1.95, 0])
        v_arrow = Arrow(o1, v_tip, buff=0, stroke_width=5, tip_length=0.17, color=COL_U)
        cv_arrow = Arrow(o2t, cv_tip, buff=0, stroke_width=6, tip_length=0.21, color=COL_PC1)
        v_lbl = MathTex("v_1", font_size=19, color=COL_U).next_to(v_tip, UP, buff=0.04)
        cv_lbl = MathTex("C v_1 = 6\\, v_1", font_size=19, color=COL_PC1)
        cv_lbl.next_to(cv_tip, UP, buff=0.04)
        cap_in = note("input", font_size=11, color=MUTED).next_to(o1, DOWN, buff=0.1)
        cap_out = note("output", font_size=11, color=MUTED).next_to(o2t, DOWN, buff=0.1)
        self.play(GrowArrow(v_arrow), FadeIn(v_lbl), FadeIn(cap_in), run_time=0.6)
        self.play(GrowArrow(cv_arrow), FadeIn(cv_lbl), FadeIn(cap_out), run_time=0.7)
        keep = note("same direction — C only stretches it", font_size=13, color=COL_PC1)
        keep.move_to(LEFT * 4.35 + DOWN * 0.55)
        scale_note = note("lengths schematic: |Cv| = 6|v|, far too long to draw to scale",
                          font_size=10.5, color=MUTED)
        scale_note.move_to(LEFT * 4.35 + DOWN * 0.95)
        self.play(FadeIn(keep), FadeIn(scale_note), run_time=0.5)
        self.wait(5.5)

        # --- LEFT, bottom demo: a direction that rotates ----------------------
        o2 = np.array([-5.25, -2.62, 0])
        self.play(FadeIn(Dot(o2, radius=0.07, color=INK)), run_time=0.3)
        ang = np.deg2rad(20)
        src = np.array([np.cos(ang), np.sin(ang), 0])
        img = np.array([4.044, 3.646, 0]) / np.linalg.norm([4.044, 3.646])
        a_tip = o2 + src * 1.05
        b_tip = o2 + img * 1.75
        a_arrow = Arrow(o2, a_tip, buff=0, stroke_width=4, tip_length=0.16, color=MUTED)
        b_arrow = Arrow(o2, b_tip, buff=0, stroke_width=4, tip_length=0.16, color=INK)
        a_lbl = MathTex("u", font_size=18, color=MUTED).next_to(a_tip, RIGHT, buff=0.05)
        b_lbl = MathTex("Cu", font_size=18, color=INK).next_to(b_tip, RIGHT, buff=0.05)
        self.play(GrowArrow(a_arrow), GrowArrow(b_arrow), FadeIn(a_lbl), FadeIn(b_lbl), run_time=0.9)
        rotate_note = note("Cu points elsewhere — not an eigenvector", font_size=12, color=MUTED)
        rotate_note.move_to(LEFT * 4.35 + DOWN * 3.25)
        self.play(FadeIn(rotate_note), run_time=0.5)
        self.wait(6.1)

        # --- RIGHT column -------------------------------------------------------
        definition = VGroup(
            note("Definition", font_size=15, color=COL_NOTE),
            MathTex(r"C v = \lambda v", font_size=34, color=INK),
            note("nonzero v keeps its direction;\nλ is the stretch factor (eigenvalue)", font_size=13),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        definition.move_to(RIGHT * 3.55 + UP * 2.15)
        self.play(FadeIn(definition), run_time=0.8)
        self.wait(6.1)

        chain_head = note("And for a unit eigenvector:", font_size=15, color=COL_NOTE)
        chain1 = eq(r"\operatorname{Var}(z) = u^T C u", font_size=21, color=INK)
        chain2 = eq(r"= u^T (\lambda u) = \lambda \, (u^T u) = \lambda", font_size=21, color=INK)
        chain = VGroup(chain_head, chain1, chain2).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        chain.move_to(RIGHT * 3.62 + UP * 0.32)
        self.play(FadeIn(chain_head), Write(chain1), run_time=0.8)
        self.play(Write(chain2), run_time=0.9)
        eigen_var_note = note("the eigenvalue IS the variance\nalong its eigenvector",
                              font_size=15, color=COL_U)
        eigen_var_note.next_to(chain, DOWN, buff=0.2).align_to(chain, LEFT)
        self.play(FadeIn(eigen_var_note), run_time=0.5)
        self.wait(7.4)

        psd = VGroup(
            note("Every eigenvalue is ≥ 0:", font_size=15, color=COL_NOTE),
            MathTex(r"u^T C u = \tfrac{1}{n-1} \textstyle\sum_i (u^T x_i')^2 \;\geq\; 0",
                    font_size=17, color=INK),
            note("a sum of squares — C is positive semidefinite", font_size=12.5, color=MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        psd.move_to(RIGHT * 3.6 + DOWN * 1.48)
        self.play(FadeIn(psd), run_time=0.8)
        self.wait(5.5)

        ortho = VGroup(
            note("Real symmetric ⇒ perpendicular eigenvectors:", font_size=14, color=COL_NOTE),
            MathTex(r"v_1 \cdot v_2 = \tfrac{1}{2} - \tfrac{1}{2} = 0", font_size=18, color=INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        ortho.move_to(RIGHT * 3.6 + DOWN * 2.62)
        self.play(FadeIn(ortho), run_time=0.7)
        self.wait(4.3)

        scatter_note = note("S = 3C: same eigenvectors, eigenvalues 18 and 2.",
                            font_size=13, color=COL_NOTE)
        scatter_note.move_to(RIGHT * 3.55 + DOWN * 3.5)
        self.play(FadeIn(scatter_note), run_time=0.6)
        self.wait(10.5)
