"""Scene 09 (8:05-9:20) — gradients, the Lagrangian, and the eigenvalue equation."""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_U, COL_NOTE, COL_MATRIX, COL_PC1,
    screen_title, scene_tag, eq, note,
)


class Scene09Lagrange(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 8 — Differentiate: out falls Cu = λu")
        tag = scene_tag(9, "Lagrange multipliers")
        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)

        # --- Phase A: expand the quadratic form --------------------------------
        c_mat = MathTex(r"C = \begin{bmatrix} a & b \\ b & d \end{bmatrix}", font_size=26,
                        color=COL_MATRIX)
        u_vec = MathTex(r"u = \begin{bmatrix} p \\ q \end{bmatrix}", font_size=26, color=COL_U)
        c_mat.move_to(LEFT * 4.35 + UP * 2.3)
        u_vec.move_to(LEFT * 0.9 + UP * 2.3)
        sym_note = note("Every covariance matrix has this symmetric shape.",
                        font_size=14, color=COL_NOTE)
        sym_note.move_to(RIGHT * 3.6 + UP * 2.3)
        self.play(FadeIn(c_mat), FadeIn(u_vec), FadeIn(sym_note), run_time=0.8)
        self.wait(7.6)

        expand = eq(r"u^T C u = a p^2 + 2 b p q + d q^2", font_size=27, color=INK)
        expand.move_to(UP * 1.55)
        expand_why = note("multiply out the brackets — treat it as an ordinary polynomial in p and q",
                          font_size=14, color=COL_NOTE)
        expand_why.next_to(expand, DOWN, buff=0.16)
        self.play(Write(expand), run_time=1.2)
        self.play(FadeIn(expand_why), run_time=0.5)
        self.wait(10.1)

        dp = eq(r"\frac{\partial}{\partial p} = 2 a p + 2 b q", font_size=20, color=INK)
        dq = eq(r"\frac{\partial}{\partial q} = 2 b p + 2 d q", font_size=20, color=INK)
        dp.move_to(LEFT * 3.35 + UP * 0.38)
        dq.move_to(RIGHT * 1.6 + UP * 0.38)
        self.play(Write(dp), run_time=0.8)
        self.play(Write(dq), run_time=0.8)
        self.wait(6.3)

        grad = eq(r"\nabla_u (u^T C u) = \begin{bmatrix} 2 a p + 2 b q \\ 2 b p + 2 d q \end{bmatrix} "
                  r"= 2 \begin{bmatrix} a & b \\ b & d \end{bmatrix} \begin{bmatrix} p \\ q \end{bmatrix} = 2 C u",
                  font_size=17.5, color=INK)
        grad.move_to(DOWN * 0.5)
        self.play(Write(grad), run_time=1.6)
        cross_note = note("the cross terms match only because C is symmetric",
                          font_size=13.5, color=MUTED)
        cross_note.next_to(grad, DOWN, buff=0.17)
        self.play(FadeIn(cross_note), run_time=0.5)
        self.wait(10.1)

        # --- Phase B: same trick for the constraint ------------------------------
        grad_norm = eq(r"u^T u = p^2 + q^2 \;\Rightarrow\; \nabla_u (u^T u) = \begin{bmatrix} 2p \\ 2q \end{bmatrix} = 2u",
                       font_size=19, color=INK)
        grad_norm.move_to(DOWN * 1.52)
        self.play(Write(grad_norm), run_time=1.2)
        self.wait(8.8)

        # --- Phase C: the Lagrangian ----------------------------------------------
        lagr = eq(r"L(u, \lambda) = u^T C u - \lambda \left( u^T u - 1 \right)", font_size=24,
                  color=COL_PC1)
        lagr.move_to(DOWN * 2.1)
        setzero = eq(r"\nabla_u L = 2 C u - 2 \lambda u = 0", font_size=24, color=INK)
        setzero.move_to(DOWN * 2.66)
        maxnote = note("at a maximum, the gradient must vanish", font_size=13, color=MUTED)
        maxnote.next_to(setzero, DOWN, buff=0.07)
        self.play(Write(lagr), run_time=1.0)
        self.play(Write(setzero), run_time=1.1)
        self.play(FadeIn(maxnote), run_time=0.4)
        self.wait(10.1)

        # --- Phase D: the punchline -------------------------------------------------
        eig = eq(r"C u = \lambda u", font_size=40, color=COL_U)
        eig.move_to(DOWN * 3.66)
        eig_box = SurroundingRectangle(eig, color=COL_U, buff=0.18, corner_radius=0.12)
        self.play(ReplacementTransform(setzero.copy(), eig), run_time=0.9)
        self.play(Create(eig_box), run_time=0.6)
        self.wait(10.1)
