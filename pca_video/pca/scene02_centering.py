"""Scene 02 (0:45-1:45) — why we centre, then the animated shift to the origin."""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_DATA, COL_CENTR, COL_MEAN, COL_NOTE, POINTS, CENTERED, MEAN,
    base_axes, axes_labels, make_dots, mean_marker, screen_title, scene_tag, eq, note,
)


class Scene02Centering(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 1 — Why do we centre the data?")
        tag = scene_tag(2, "Centring")
        axes = base_axes()
        labels = axes_labels(axes)
        dots = make_dots(axes, POINTS, COL_DATA)

        coord_lbls = VGroup(
            MathTex("(5,3)", font_size=17, color=COL_DATA).next_to(axes.c2p(5, 3), RIGHT, buff=0.1),
            MathTex("(1,1)", font_size=17, color=COL_DATA).next_to(axes.c2p(1, 1), DOWN, buff=0.09),
            MathTex("(4,4)", font_size=17, color=COL_DATA).next_to(axes.c2p(4, 4), RIGHT, buff=0.1),
            MathTex("(2,0)", font_size=17, color=COL_DATA).next_to(axes.c2p(2, 0), DOWN, buff=0.09),
        )

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.play(Create(axes), FadeIn(labels), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.18), run_time=1.2)
        self.play(FadeIn(coord_lbls), run_time=0.6)
        self.wait(4.4)

        # --- mean, computed on screen --------------------------------------
        panel_head = Tex("Step one: find the average position", font_size=20, color=INK)
        panel_head.move_to(RIGHT * 3.6 + UP * 2.05)
        eq_x = eq(r"\mu_x = \frac{5+1+4+2}{4} = \frac{12}{4} = 3", font_size=25)
        eq_y = eq(r"\mu_y = \frac{3+1+4+0}{4} = \frac{8}{4} = 2", font_size=25)
        eq_m = eq(r"\mu = (3,\ 2)", font_size=30, color=COL_MEAN)
        mean_group = VGroup(eq_x, eq_y, eq_m).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        mean_group.move_to(RIGHT * 3.6 + UP * 0.9)

        self.play(FadeIn(panel_head, shift=DOWN * 0.1), run_time=0.6)
        self.play(Write(eq_x), run_time=1.3)
        self.play(Write(eq_y), run_time=1.3)
        self.play(Write(eq_m), run_time=0.8)
        self.wait(4.4)

        marker = mean_marker(axes)
        marker_lbl = MathTex(r"\mu = (3,2)", font_size=19, color=COL_MEAN)
        marker_lbl.move_to(axes.c2p(3, 2) + UP * 0.42 + RIGHT * 0.85)
        self.play(FadeIn(marker, scale=0.5), run_time=0.7)
        self.play(FadeIn(marker_lbl), run_time=0.5)
        self.wait(6.0)

        why = note("We care about variation around the average,\nnot absolute positions on the page.", font_size=18)
        why.move_to(RIGHT * 3.6 + DOWN * 1.35)
        self.play(FadeIn(why), run_time=0.7)
        self.wait(7.5)

        # --- the animated shift -------------------------------------------
        self.play(FadeOut(coord_lbls), FadeOut(panel_head), FadeOut(mean_group),
                  FadeOut(why), FadeOut(marker_lbl), run_time=0.6)

        origin_dot = Dot(axes.c2p(0, 0), radius=0.06, color=MUTED, z_index=5)
        origin_lbl = MathTex("O", font_size=18, color=MUTED).next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.08)
        shift_eq = eq(r"x_i' = x_i - \mu", font_size=28, color=INK)
        shift_eq.move_to(RIGHT * 3.6 + UP * 1.75)
        self.play(FadeIn(shift_eq), run_time=0.5)
        self.play(
            *[dots[i].animate.move_to(axes.c2p(*CENTERED[i])) for i in range(4)],
            marker.animate.move_to(axes.c2p(0, 0)),
            run_time=2.1,
        )
        self.play(*[dots[i].animate.set_color(COL_CENTR) for i in range(4)],
                  FadeIn(origin_dot), FadeIn(origin_lbl), run_time=0.8)

        # --- centred results ----------------------------------------------
        centred_list = MathTex(
            r"(2,1)\quad (-2,-1)\quad (1,2)\quad (-1,-2)", font_size=21, color=COL_CENTR
        ).move_to(RIGHT * 3.6 + UP * 0.95)
        centred_lbls = VGroup(
            MathTex("(2,1)", font_size=15, color=COL_CENTR).next_to(axes.c2p(2, 1), RIGHT, buff=0.08),
            MathTex("(-2,-1)", font_size=15, color=COL_CENTR).next_to(axes.c2p(-2, -1), LEFT, buff=0.08),
            MathTex("(1,2)", font_size=15, color=COL_CENTR).next_to(axes.c2p(1, 2), RIGHT, buff=0.08),
            MathTex("(-1,-2)", font_size=15, color=COL_CENTR).next_to(axes.c2p(-1, -2), LEFT, buff=0.08),
        )
        notes = VGroup(
            note("Every point moved by the same amount: (-3, -2).", font_size=18),
            note("The average position is now (0, 0).", font_size=18),
            note("The shape of the cloud is unchanged —\nonly the origin we measure from.", font_size=17),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(RIGHT * 3.6 + DOWN * 0.75)

        self.play(FadeIn(centred_list), run_time=0.6)
        self.play(FadeIn(centred_lbls), run_time=0.6)
        self.play(FadeIn(notes), run_time=0.9)
        self.wait(10.7)

        why_matters = note("From here on, every formula works\nwith deviations from the mean.", font_size=18,
                           color=INK).move_to(RIGHT * 3.6 + DOWN * 2.6)
        self.play(FadeIn(why_matters), run_time=0.6)
        self.wait(10.7)
