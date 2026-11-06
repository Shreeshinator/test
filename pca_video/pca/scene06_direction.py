"""Scene 06 (4:55-6:00) — choose a direction, project, ask what 'better' means."""

from manim import *
import numpy as np
from pca.common import (
    BG, INK, MUTED, COL_CENTR, COL_U, COL_NOTE,
    base_axes, axes_labels, make_dots, screen_title, scene_tag, eq, note, unit_vector, projection,
    CENTERED,
)

SQRT2 = 2 ** 0.5


def direction_layer(axes, direction, length=2.6):
    d = np.array(direction, dtype=float)
    d = d / np.linalg.norm(d)
    arrow = unit_vector(axes, direction, length=length, color=COL_U, stroke_width=6)
    line = Line(axes.c2p(-d[0] * 3.4, -d[1] * 3.4), axes.c2p(d[0] * 3.4, d[1] * 3.4),
                stroke_width=2, color=COL_U).set_opacity(0.35)
    dashes, feet, shadows = [], [], []
    for p in CENTERED:
        foot, _, dash = projection(axes, p, direction, color=COL_U)
        foot2 = Dot(foot.get_center(), radius=0.07, color=COL_U, z_index=7)
        dashes.append(dash)
        feet.append(foot2)
    return VGroup(line, arrow), VGroup(*dashes), VGroup(*feet)


def z_panel(zvalues, var_tex, color=COL_U):
    head = note("Projected positions on u:", font_size=15, color=COL_NOTE)
    head.move_to(RIGHT * 3.6 + UP * 1.15)
    nl = NumberLine(x_range=[-3.4, 3.4, 1], length=4.3, include_ticks=True,
                    include_numbers=False, color="#55606E", stroke_width=2)
    nl.move_to(RIGHT * 3.6 + UP * 0.05)
    labels = VGroup(
        MathTex("-2", font_size=13, color=MUTED).next_to(nl.number_to_point(-2), DOWN, buff=0.06),
        MathTex("0", font_size=13, color=MUTED).next_to(nl.number_to_point(0), DOWN, buff=0.06),
        MathTex("2", font_size=13, color=MUTED).next_to(nl.number_to_point(2), DOWN, buff=0.06),
    )
    dots = VGroup()
    for z, dy in zip(zvalues, [0.27, 0.13, -0.13, -0.27]):
        dpt = Dot(nl.number_to_point(z) + UP * dy, radius=0.075, color=COL_CENTR, z_index=6)
        dots.add(dpt)
    readout = eq(var_tex, font_size=23, color=color)
    readout.move_to(RIGHT * 3.6 + DOWN * 1.5)
    return VGroup(head, nl, labels, dots, readout)


class Scene06Direction(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 5 — Project the cloud onto a direction")
        tag = scene_tag(6, "Choosing a direction")
        axes = base_axes()
        labels = axes_labels(axes)
        dots = make_dots(axes, CENTERED, COL_CENTR)

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.play(Create(axes), FadeIn(labels), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.15), run_time=1.0)
        self.wait(1.6)

        # --- introduce u ---------------------------------------------------
        u_eq = eq(r"u = \begin{bmatrix} u_x \\ u_y \end{bmatrix}", font_size=30, color=COL_U)
        u_eq.move_to(RIGHT * 3.6 + UP * 2.1)
        u_note = note("an arbitrary direction through the origin", font_size=15, color=COL_NOTE)
        u_note.next_to(u_eq, DOWN, buff=0.14)
        self.play(FadeIn(u_eq), FadeIn(u_note), run_time=0.7)
        self.wait(2.3)

        proj_eq = eq(r"z_i = u^T x_i'", font_size=28, color=INK)
        proj_eq.move_to(RIGHT * 3.6 + UP * 0.95)
        proj_note = note("dot product — the signed length of the shadow of point i along u",
                         font_size=13, color=COL_NOTE)
        proj_note.next_to(proj_eq, DOWN, buff=0.13)
        self.play(Write(proj_eq), FadeIn(proj_note), run_time=0.9)
        self.wait(3.1)
        self.play(FadeOut(u_eq), FadeOut(u_note), FadeOut(proj_eq), FadeOut(proj_note), run_time=0.5)

        # --- direction A: along x -------------------------------------------
        layerA, dashesA, feetA = direction_layer(axes, (1, 0), length=2.8)
        panelA = z_panel([2, -2, 1, -1],
                         r"\operatorname{Var}(z) = u^T C u = \tfrac{10}{3} \approx 3.33")
        tagA = MathTex("u = (1, 0)", font_size=19, color=COL_U).move_to(RIGHT * 3.6 + UP * 2.05)
        self.play(FadeIn(layerA), FadeIn(tagA), run_time=0.8)
        self.play(LaggedStart(*[Create(d) for d in dashesA], lag_ratio=0.15), run_time=1.3)
        self.play(FadeIn(feetA), run_time=0.5)
        self.play(FadeIn(panelA), run_time=0.9)
        self.wait(7.3)
        self.play(FadeOut(layerA), FadeOut(dashesA), FadeOut(feetA),
                  FadeOut(panelA), FadeOut(tagA), run_time=0.6)

        # --- direction B: along y -------------------------------------------
        layerB, dashesB, feetB = direction_layer(axes, (0, 1), length=2.4)
        panelB = z_panel([1, -1, 2, -2],
                         r"\operatorname{Var}(z) = u^T C u = \tfrac{10}{3} \approx 3.33")
        tagB = MathTex("u = (0, 1)", font_size=19, color=COL_U).move_to(RIGHT * 3.6 + UP * 2.05)
        self.play(FadeIn(layerB), FadeIn(tagB), run_time=0.7)
        self.play(LaggedStart(*[Create(d) for d in dashesB], lag_ratio=0.15), run_time=1.2)
        self.play(FadeIn(feetB), run_time=0.5)
        self.play(FadeIn(panelB), run_time=0.8)
        self.wait(7.0)
        self.play(FadeOut(layerB), FadeOut(dashesB), FadeOut(feetB),
                  FadeOut(panelB), FadeOut(tagB), run_time=0.6)

        # --- direction C: the diagonal ---------------------------------------
        diag = (1 / SQRT2, 1 / SQRT2)
        layerC, dashesC, feetC = direction_layer(axes, diag, length=2.9)
        panelC = z_panel([3 / SQRT2, -3 / SQRT2, 3 / SQRT2, -3 / SQRT2],
                         r"\operatorname{Var}(z) = u^T C u = 6", color=COL_U)
        tagC = MathTex(r"u = \tfrac{1}{\sqrt{2}}(1, 1)", font_size=19, color=COL_U)
        tagC.move_to(RIGHT * 3.6 + UP * 2.05)
        self.play(FadeIn(layerC), FadeIn(tagC), run_time=0.8)
        self.play(LaggedStart(*[Create(d) for d in dashesC], lag_ratio=0.15), run_time=1.2)
        self.play(FadeIn(feetC), run_time=0.5)
        self.play(FadeIn(panelC), run_time=0.8)
        better = note("Same data — but the diagonal spreads them further apart.",
                      font_size=15, color=INK)
        better.move_to(RIGHT * 3.6 + DOWN * 2.35)
        self.play(FadeIn(better), run_time=0.6)
        self.wait(7.3)

        # --- the question + the unit-length constraint -------------------------
        question = Text("What makes one direction better than another?",
                        font_size=19, color=INK, weight="BOLD")
        question.move_to(RIGHT * 3.6 + DOWN * 2.1)
        answer = note("Answer: its projected points have the greatest variance.",
                      font_size=15, color=COL_U)
        answer.move_to(RIGHT * 3.6 + DOWN * 2.82)
        self.play(FadeIn(question), run_time=0.7)
        self.wait(3.8)
        self.play(FadeIn(answer), run_time=0.6)
        self.wait(5.4)
        self.play(FadeOut(question), FadeOut(answer), FadeOut(better), run_time=0.4)

        cheat = note("Double u and every projection doubles — Var(z) ×4.\nThat is cheating. So fix the length:",
                     font_size=14, color=COL_NOTE)
        cheat.move_to(RIGHT * 3.6 + DOWN * 2.05)
        unit_eq = eq(r"u^T u = u_x^2 + u_y^2 = 1", font_size=23, color=INK)
        unit_eq.move_to(RIGHT * 3.6 + DOWN * 2.95)
        self.play(FadeIn(cheat), run_time=0.7)
        self.play(Write(unit_eq), run_time=0.9)
        self.wait(6.6)
        self.play(FadeOut(layerC), FadeOut(dashesC), FadeOut(feetC), FadeOut(panelC),
                  FadeOut(tagC), FadeOut(cheat), FadeOut(unit_eq),
                  run_time=0.6)
