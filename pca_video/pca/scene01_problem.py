"""Scene 01 (0:00-0:45) — the problem: what are we trying to achieve?"""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_DATA, COL_PC1, POINTS,
    base_axes, axes_labels, make_dots, screen_title, scene_tag, note,
)


class Scene01Problem(Scene):
    def construct(self):
        self.camera.background_color = BG

        # --- Phase 1: title card -----------------------------------------
        title = Text("Principal Component Analysis", font_size=50, weight="BOLD", color=INK)
        subtitle = Text(
            "Finding the direction of greatest variation — from first principles",
            font_size=22, color=MUTED,
        ).next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(title, shift=UP * 0.25), run_time=1.1)
        self.play(FadeIn(subtitle, shift=UP * 0.15), run_time=0.8)
        self.wait(5.5)
        self.play(FadeOut(title, shift=UP * 0.2), FadeOut(subtitle, shift=UP * 0.2), run_time=0.7)

        # --- Phase 2: the scatter -----------------------------------------
        heading = screen_title("The problem — what are we trying to achieve?")
        tag = scene_tag(1, "The problem")
        axes = base_axes()
        labels = axes_labels(axes)
        dots = make_dots(axes, POINTS, COL_DATA)

        self.play(FadeIn(heading, shift=DOWN * 0.15), FadeIn(tag), run_time=0.6)
        self.play(Create(axes), FadeIn(labels), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.22), run_time=1.6)
        self.wait(2.8)

        # --- Phase 3: what the points mean ---------------------------------
        panel = VGroup(
            Text("Each dot is one observation.", font_size=21, color=INK),
            Text("Two features describe it: x and y.", font_size=21, color=INK),
            MathTex(r"(5,3)", r"(1,1)", r"(4,4)", r"(2,0)", font_size=20, color=COL_DATA)
            .arrange(RIGHT, buff=0.35),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.6 + UP * 1.7)
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.12) for m in panel], lag_ratio=0.35), run_time=2.0)
        self.wait(3.4)

        question = Text(
            "Can we find the direction\nalong which these points\nvary the most?",
            font_size=27, color=INK, weight="BOLD", line_spacing=1.05,
        ).move_to(RIGHT * 3.6 + DOWN * 0.35)
        self.play(Write(question), run_time=1.6)
        self.wait(4.8)

        # highlight the long axis of the cloud with a faint dashed hint
        hint = DashedLine(
            axes.c2p(-0.4, -0.4), axes.c2p(4.7, 4.7),
            color=COL_PC1, stroke_width=3, dash_length=0.16,
        ).set_opacity(0.55)
        self.play(Create(hint), run_time=1.2)
        self.wait(4.2)

        takeaway = Text(
            "PCA finds new directions of\ngreatest variation — and uses them\nas new axes for the data.",
            font_size=21, color=COL_PC1, line_spacing=1.08,
        ).move_to(RIGHT * 3.6 + DOWN * 2.45)
        self.play(FadeIn(takeaway, shift=UP * 0.15), run_time=1.0)
        self.wait(7.7)
        self.play(FadeOut(hint), run_time=0.6)
        self.wait(4.2)
