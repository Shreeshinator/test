"""Scene 05 (3:35-4:55) — build the scatter matrix by hand, then the covariance matrix.

Column-vector convention is used throughout; each centred observation is
x_i' = [x_i', y_i']^T.  The scatter matrix sums outer products x' x'^T.
"""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_CENTR, COL_MATRIX, COL_NOTE,
    base_axes, axes_labels, make_dots, screen_title, scene_tag, eq, note, CENTERED,
)


class Scene05ScatterMatrix(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 4 — The scatter matrix, built by hand")
        tag = scene_tag(5, "Scatter & covariance matrices")
        axes = base_axes()
        axes.set_opacity(0.3)
        axes_lab = axes_labels(axes).set_opacity(0.3)
        dots = make_dots(axes, CENTERED, COL_CENTR).set_opacity(0.45)

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.play(Create(axes), FadeIn(axes_lab), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.15), run_time=1.0)
        self.wait(2.3)

        # --- Phase A: column vector & outer vs dot product -------------------
        col_head = note("One centred observation, as a column vector:", font_size=17, color=COL_NOTE)
        col_head.move_to(RIGHT * 3.6 + UP * 2.05)
        xcol = MathTex(r"x_i' = \begin{bmatrix} x_i' \\ y_i' \end{bmatrix}", font_size=26, color=INK)
        xcol.move_to(RIGHT * 2.0 + UP * 1.1)
        x_example = MathTex(r"\text{e.g.}\ \begin{bmatrix} 2 \\ 1 \end{bmatrix}", font_size=22, color=COL_CENTR)
        x_example.move_to(RIGHT * 5.15 + UP * 1.1)
        self.play(FadeIn(col_head), run_time=0.5)
        self.play(FadeIn(xcol, shift=DOWN * 0.12), FadeIn(x_example, shift=DOWN * 0.12), run_time=0.8)
        self.wait(4.1)

        outer_eq = eq(r"x_i' x_i'^T = \begin{bmatrix} x_i' \\ y_i' \end{bmatrix} "
                      r"\begin{bmatrix} x_i' & y_i' \end{bmatrix} = "
                      r"\begin{bmatrix} x_i'^2 & x_i' y_i' \\ x_i' y_i' & y_i'^2 \end{bmatrix}",
                      font_size=20, color=COL_MATRIX)
        outer_eq.move_to(RIGHT * 3.6 + UP * 0.05)
        self.play(Write(outer_eq), run_time=1.6)
        self.wait(3.6)

        dot_eq = eq(r"x_i'^T x_i' = x_i'^2 + y_i'^2 \quad \text{(one number)}",
                    font_size=17, color=MUTED)
        dot_eq.move_to(RIGHT * 3.6 + DOWN * 0.72)
        dot_warn = note("Outer product: a 2×2 matrix.   Dot product: a scalar.", font_size=15, color=INK)
        dot_warn.next_to(dot_eq, DOWN, buff=0.16)
        self.play(FadeIn(dot_eq), run_time=0.7)
        self.play(FadeIn(dot_warn), run_time=0.6)
        self.wait(6.5)

        # --- Phase B: the four outer products --------------------------------
        self.play(FadeOut(col_head), FadeOut(xcol), FadeOut(x_example),
                  FadeOut(outer_eq), FadeOut(dot_eq), FadeOut(dot_warn), run_time=0.6)

        sum_head = note("Do this for every point — and add the results:", font_size=17, color=COL_NOTE)
        sum_head.move_to(RIGHT * 3.6 + UP * 2.0)
        self.play(FadeIn(sum_head), run_time=0.5)

        caps = ["from (2,1)", "from (-2,-1)", "from (1,2)", "from (-1,-2)"]
        entries = [
            ("4", "2", "2", "1"),
            ("4", "2", "2", "1"),
            ("1", "2", "2", "4"),
            ("1", "2", "2", "4"),
        ]
        mats, cap_lbls = [], []
        grid_positions = [
            RIGHT * 2.1 + UP * 0.95, RIGHT * 5.1 + UP * 0.95,
            RIGHT * 2.1 + DOWN * 0.35, RIGHT * 5.1 + DOWN * 0.35,
        ]
        for (a, b, c, d), cap, pos in zip(entries, caps, grid_positions):
            m = Matrix([[a, b], [c, d]], v_buff=0.75, h_buff=1.15).scale(0.62)
            m.set_color(COL_MATRIX)
            m.move_to(pos)
            cap_lbl = Text(cap, font_size=13, color=MUTED).next_to(m, DOWN, buff=0.08)
            mats.append(m)
            cap_lbls.append(cap_lbl)
        for m, cap_lbl in zip(mats, cap_lbls):
            self.play(FadeIn(m, scale=0.6), FadeIn(cap_lbl), run_time=0.55)
        self.wait(5.4)

        plus_signs = VGroup(
            MathTex("+", font_size=40, color=MUTED).move_to(RIGHT * 3.6 + UP * 0.95),
            MathTex("+", font_size=40, color=MUTED).move_to(RIGHT * 3.6 + DOWN * 0.35),
            MathTex("+", font_size=40, color=MUTED).move_to(RIGHT * 2.1 + UP * 0.28),
        )
        # simpler: a single plus between the rows
        self.play(FadeIn(plus_signs[0]), FadeIn(plus_signs[1]), run_time=0.5)
        self.wait(4.7)

        # --- Phase C: entry-wise addition ------------------------------------
        self.play(FadeOut(sum_head), *[FadeOut(m) for m in mats],
                  *[FadeOut(c) for c in cap_lbls], FadeOut(plus_signs), run_time=0.6)

        entry_head = note("Add entry by entry:", font_size=17, color=COL_NOTE)
        entry_head.move_to(RIGHT * 3.6 + UP * 2.0)
        e11 = eq(r"4+4+1+1 = 10", font_size=24, color=INK).move_to(RIGHT * 2.05 + UP * 1.25)
        e12 = eq(r"2+2+2+2 = 8", font_size=24, color=INK).move_to(RIGHT * 5.15 + UP * 1.25)
        e21 = eq(r"2+2+2+2 = 8", font_size=24, color=INK).move_to(RIGHT * 2.05 + UP * 0.35)
        e22 = eq(r"1+1+4+4 = 10", font_size=24, color=INK).move_to(RIGHT * 5.15 + UP * 0.35)
        eqlabel = note("top-left", font_size=13, color=MUTED).next_to(e11, DOWN, buff=0.06)
        eqlabel2 = note("top-right", font_size=13, color=MUTED).next_to(e12, DOWN, buff=0.06)
        eqlabel3 = note("bottom-left", font_size=13, color=MUTED).next_to(e21, DOWN, buff=0.06)
        eqlabel4 = note("bottom-right", font_size=13, color=MUTED).next_to(e22, DOWN, buff=0.06)
        self.play(FadeIn(entry_head), run_time=0.4)
        for e in (e11, e12, e21, e22):
            self.play(Write(e), run_time=0.55)
        self.play(FadeIn(eqlabel), FadeIn(eqlabel2), FadeIn(eqlabel3), FadeIn(eqlabel4), run_time=0.6)
        self.wait(4.7)

        s_mat = Matrix([["10", "8"], ["8", "10"]], v_buff=1.0, h_buff=1.35)
        s_mat.set_color(COL_MATRIX).scale(0.9)
        s_mat.move_to(RIGHT * 3.6 + DOWN * 0.95)
        s_label = MathTex("S = \\sum_{i} x_i' x_i'^T", font_size=22, color=COL_MATRIX)
        s_label.next_to(s_mat, UP, buff=0.22)
        s_box = SurroundingRectangle(s_mat, color=COL_MATRIX, buff=0.16, corner_radius=0.12)
        s_caption = note("The scatter matrix: total spread, unnormalised.", font_size=16, color=INK)
        s_caption.next_to(s_mat, DOWN, buff=0.22)
        self.play(*[FadeOut(e) for e in (e11, e12, e21, e22)],
                  FadeOut(entry_head), FadeOut(eqlabel), FadeOut(eqlabel2),
                  FadeOut(eqlabel3), FadeOut(eqlabel4), run_time=0.6)
        self.play(FadeIn(s_label), FadeIn(s_mat, scale=0.7), Create(s_box), run_time=1.0)
        self.play(FadeIn(s_caption), run_time=0.5)
        self.wait(5.9)

        # --- Phase D: what each entry means ----------------------------------
        meanings = VGroup(
            note("top-left: total squared spread in x (10)", font_size=15),
            note("bottom-right: total squared spread in y (10)", font_size=15),
            note("off-diagonal: joint x–y variation (8)", font_size=15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        meanings.move_to(RIGHT * 3.6 + DOWN * 2.95)
        self.play(FadeIn(meanings), run_time=0.8)
        self.wait(7.8)
        self.play(FadeOut(meanings), FadeOut(s_caption), run_time=0.5)

        # --- Phase E: from scatter to covariance ------------------------------
        cov_eq1 = eq(r"C = \frac{1}{n-1}\, S = \frac{1}{3} \times \begin{bmatrix} 10 & 8 \\ 8 & 10 \end{bmatrix}",
                     font_size=20, color=COL_MATRIX)
        cov_eq2 = eq(r"= \begin{bmatrix} \frac{10}{3} & \frac{8}{3} \\[3pt] \frac{8}{3} & \frac{10}{3} \end{bmatrix}",
                     font_size=23, color=COL_MATRIX)
        cov_eq = VGroup(cov_eq1, cov_eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        cov_eq.move_to(RIGHT * 3.6 + DOWN * 1.2)
        self.play(ReplacementTransform(s_box, SurroundingRectangle(cov_eq, color=COL_MATRIX,
                                                                   buff=0.14, corner_radius=0.12)),
                  FadeOut(s_mat), FadeOut(s_label), run_time=0.8)
        self.play(Write(cov_eq1), run_time=1.0)
        self.play(Write(cov_eq2), run_time=0.9)
        self.wait(4.1)

        notes = VGroup(
            note("Scatter: unnormalised sum.   Covariance: scatter ÷ (n − 1).", font_size=15, color=INK),
            note("Same directions — dividing by the positive number 3\nnever changes an eigenvector; eigenvalues shrink by 3.",
                 font_size=15, color=COL_NOTE),
            note("C is symmetric: the x·y and y·x entries are equal.", font_size=15, color=INK),
            note("(“CV matrix” is just another name for this covariance matrix.)",
                 font_size=13, color=MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.17)
        notes.move_to(RIGHT * 3.6 + DOWN * 2.75)
        for nn in notes:
            self.play(FadeIn(nn), run_time=0.5)
        self.wait(7.8)
