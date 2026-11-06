"""Scene 08 (7:20-8:05) — the constrained optimisation problem, stated precisely."""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_U, COL_MATRIX, COL_NOTE, COL_PC1,
    screen_title, scene_tag, eq, note,
)


class Scene08Optimisation(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 7 — The problem, stated as mathematics")
        tag = scene_tag(8, "The optimisation problem")

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.wait(5.3)

        # --- the objective ---------------------------------------------------
        maximize = MathTex(r"\max_{u} \; u^T C u", font_size=58, color=INK)
        maximize.move_to(UP * 2.35)
        self.play(Write(maximize), run_time=1.1)
        subject = MathTex(r"\text{subject to} \quad u^T u = 1", font_size=30, color=COL_U)
        subject.move_to(UP * 1.42)
        self.play(FadeIn(subject, shift=UP * 0.1), run_time=0.8)
        self.wait(7.0)

        # --- what each symbol does -------------------------------------------
        parts = VGroup(
            MathTex(r"u \;=\; \text{the direction we are choosing}", font_size=19, color=COL_U),
            MathTex(r"C \;=\; \text{the data's spread and joint variation}", font_size=19, color=COL_MATRIX),
            MathTex(r"u^T C u \;=\; \text{variance along that direction}", font_size=19, color=INK),
            MathTex(r"u^T u = 1 \;=\; \text{unit length: no scaling cheats}", font_size=19, color=COL_U),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        parts.move_to(DOWN * -0.35)
        for p in parts:
            self.play(FadeIn(p, shift=RIGHT * 0.12), run_time=0.55)
        self.wait(7.0)

        # --- why the constraint bites ------------------------------------------
        cheat1 = MathTex(r"u \rightarrow 2u \quad\Rightarrow\quad u^T C u \rightarrow 4 \, u^T C u",
                         font_size=19, color=MUTED)
        cheat2 = note("Without the constraint, “bigger u” always looks better.", font_size=15, color=MUTED)
        cheat = VGroup(cheat1, cheat2).arrange(DOWN, buff=0.15)
        cheat.move_to(DOWN * 2.35)
        self.play(FadeIn(cheat), run_time=0.7)
        self.wait(9.4)

        # --- how do we solve a constrained max? ---------------------------------
        self.play(FadeOut(cheat), run_time=0.4)
        lagrange_head = Tex("How do we maximise with a constraint?", font_size=21, color=INK)
        lagrange_head.move_to(DOWN * 1.95)
        self.play(FadeIn(lagrange_head), run_time=0.7)
        idea = note("Fold the constraint into the function with a new unknown, λ:", font_size=17,
                    color=COL_NOTE)
        idea.move_to(DOWN * 2.48)
        self.play(FadeIn(idea), run_time=0.5)
        lagrangian = MathTex(r"L(u, \lambda) = u^T C u \;-\; \lambda \, \left( u^T u - 1 \right)",
                             font_size=30, color=COL_PC1)
        lagrangian.move_to(DOWN * 2.98)
        self.play(Write(lagrangian), run_time=1.0)
        self.wait(7.8)
