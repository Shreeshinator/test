"""Scene 03 (1:45-2:35) — variance for one variable, and its limits."""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_CENTR, COL_MATRIX,
    base_axes, axes_labels, make_dots, screen_title, scene_tag, eq, note,
)
from pca.common import CENTERED


class Scene03Variance(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 2 — Spread along one axis: variance")
        tag = scene_tag(3, "Variance")
        axes = base_axes()
        labels = axes_labels(axes)
        dots = make_dots(axes, CENTERED, COL_CENTR)

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.play(Create(axes), FadeIn(labels), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.15), run_time=1.1)
        self.wait(3.7)

        # --- the question ---------------------------------------------------
        ask = Tex("How spread out are the points?", font_size=22, color=INK)
        ask.move_to(RIGHT * 3.6 + UP * 2.15)
        self.play(FadeIn(ask), run_time=0.5)

        # --- variance formula ------------------------------------------------
        var_eq = eq(r"\operatorname{Var}(x) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2",
                    font_size=25, color=INK)
        var_eq.move_to(RIGHT * 3.6 + UP * 1.15)
        self.play(Write(var_eq), run_time=1.4)
        self.wait(3.7)

        bullets = VGroup(
            note("Subtract the mean — deviations from the middle.", font_size=16),
            note("Square them — signs vanish; big gaps count more.", font_size=16),
            note("Add them up — the total squared deviation.", font_size=16),
            note("Divide by n − 1 — sample variance.", font_size=16),
            note("Population variance divides by n instead.", font_size=16),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        bullets.move_to(RIGHT * 3.6 + UP * -0.1)
        for b in bullets:
            self.play(FadeIn(b, shift=RIGHT * 0.1), run_time=0.45)
        self.wait(4.7)

        convention = note("This video uses n − 1. With n, every variance\nrescales equally — the directions never change.",
                          font_size=15, color=MUTED)
        convention.move_to(RIGHT * 3.6 + DOWN * 1.5)
        self.play(FadeIn(convention), run_time=0.7)
        self.wait(7.5)

        # --- apply to our dataset -------------------------------------------
        s1 = eq(r"\sum x_i'^2 = 4+4+1+1 = 10 \;\Rightarrow\; \operatorname{Var}(x) = \tfrac{10}{3}",
                font_size=19, color=INK).move_to(RIGHT * 3.6 + DOWN * 2.3)
        s2 = eq(r"\sum y_i'^2 = 1+1+4+4 = 10 \;\Rightarrow\; \operatorname{Var}(y) = \tfrac{10}{3}",
                font_size=19, color=INK).move_to(RIGHT * 3.6 + DOWN * 2.9)
        self.play(FadeOut(convention), run_time=0.5)
        self.play(Write(s1), run_time=0.9)
        self.play(Write(s2), run_time=0.9)
        self.wait(9.4)

        # --- the pivot --------------------------------------------------------
        pivot = note("Variance looks at one axis at a time.\nIt cannot say whether x and y rise together.",
                     font_size=17, color=COL_MATRIX)
        pivot.move_to(RIGHT * 3.6 + UP * 2.15)
        self.play(ReplacementTransform(ask, pivot), run_time=0.9)
        self.wait(10.0)
