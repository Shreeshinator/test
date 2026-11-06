"""Scene 04 (2:35-3:35) — covariance, derived intuitively, then computed."""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_CENTR, COL_MATRIX, COL_NOTE, GRID_COL, CENTERED,
    base_axes, axes_labels, make_dots, screen_title, scene_tag, eq, note,
)


class Scene04Covariance(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 3 — Covariance: do x and y move together?")
        tag = scene_tag(4, "Covariance")
        axes = base_axes()
        labels = axes_labels(axes)
        dots = make_dots(axes, CENTERED, COL_CENTR)

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.play(Create(axes), FadeIn(labels), run_time=1.0)

        # shade the two quadrants where deviations share a sign
        q_pos_1 = Rectangle(width=2.55, height=2.35, fill_color=COL_CENTR,
                            fill_opacity=0.12, stroke_width=0).move_to(axes.c2p(1.32, 1.32))
        q_pos_3 = Rectangle(width=2.45, height=2.25, fill_color=COL_CENTR,
                            fill_opacity=0.12, stroke_width=0).move_to(axes.c2p(-1.28, -1.24))
        lbl_q1 = MathTex("(+,+)", font_size=17, color=COL_CENTR).move_to(axes.c2p(2.35, 2.2))
        lbl_q3 = MathTex(r"(-,-)", font_size=17, color=COL_CENTR).move_to(axes.c2p(-2.15, -0.55))
        self.play(FadeIn(q_pos_1), FadeIn(q_pos_3), FadeIn(lbl_q1), FadeIn(lbl_q3), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.15), run_time=1.1)
        self.wait(5.9)

        # --- the three possible patterns -----------------------------------
        cases = VGroup(
            note("Positive — the two features tend to rise together.", font_size=16, color=INK),
            note("Negative — one rises as the other falls.", font_size=16, color=INK),
            note("Near zero — no clear linear co-variation.", font_size=16, color=INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        cases.move_to(RIGHT * 3.6 + UP * 1.55)
        for c in cases:
            self.play(FadeIn(c, shift=RIGHT * 0.1), run_time=0.5)
        self.wait(7.1)

        # --- the formula, built from products --------------------------------
        prod_head = note("For each point, multiply its two deviations:", font_size=17, color=COL_NOTE)
        prod_head.move_to(RIGHT * 3.6 + UP * 0.15)
        prods = MathTex(
            r"(2)(1)=2 \qquad (-2)(-1)=2 \qquad (1)(2)=2 \qquad (-1)(-2)=2",
            font_size=17.5, color=INK,
        ).move_to(RIGHT * 3.6 + DOWN * 0.45)
        self.play(FadeIn(prod_head), run_time=0.5)
        self.play(Write(prods), run_time=1.3)
        self.wait(5.9)

        cov_eq = eq(r"\operatorname{Cov}(x,y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})",
                    font_size=22, color=INK).move_to(RIGHT * 3.6 + DOWN * 1.2)
        self.play(FadeIn(cov_eq, shift=UP * 0.1), run_time=0.8)

        cov_calc = eq(r"\operatorname{Cov}(x,y) = \frac{2+2+2+2}{3} = \frac{8}{3} \approx 2.67",
                      font_size=22, color=COL_MATRIX).move_to(RIGHT * 3.6 + DOWN * 2.0)
        self.play(Write(cov_calc), run_time=1.1)
        self.wait(9.3)

        verdict = note("Every product is positive \u2014 the features\nclearly increase together.",
                       font_size=17, color=COL_CENTR).move_to(RIGHT * 3.6 + DOWN * 2.85)
        self.play(FadeIn(verdict), run_time=0.7)
        self.wait(10.4)

        # --- recap of the three spread numbers -------------------------------
        recap_head = note("So the three spread numbers are", font_size=16, color=COL_NOTE)
        recap = MathTex(
            r"\operatorname{Var}(x) = \tfrac{10}{3} \quad"
            r"\operatorname{Var}(y) = \tfrac{10}{3} \quad"
            r"\operatorname{Cov}(x,y) = \tfrac{8}{3}",
            font_size=15, color=INK,
        )
        recap_group = VGroup(recap_head, recap).arrange(DOWN, buff=0.15)
        recap_group.move_to(RIGHT * 3.6 + UP * 0.15)
        self.play(FadeOut(prod_head), FadeOut(prods), run_time=0.5)
        self.play(FadeIn(recap_group), run_time=0.8)
        self.wait(10.4)
