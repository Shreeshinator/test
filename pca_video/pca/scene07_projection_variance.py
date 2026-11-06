"""Scene 07 (6:00-7:20) — the full derivation of Var(z) = uᵀCu.

Two columns: derivation on the left, the reason for each step on the right.
"""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_U, COL_NOTE, COL_MATRIX,
    screen_title, scene_tag, eq, note,
)

EQ_FONT = 23
SMALL_EQ_FONT = 18
REASON_FONT = 13.5

ROWS_Y = [2.35, 1.72, 1.06, 0.42, -0.24, -0.88, -1.52, -2.18, -2.82]
EQ_X = -6.95
REASON_X = 3.15


class Scene07ProjectionVariance(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 6 — Why the projected variance is uᵀCu")
        tag = scene_tag(7, "Deriving uᵀCu")
        legend = Tex(
            r"$x_i'$ centred observation \quad $u$ unit direction \quad $z_i$ projection",
            font_size=13, color=MUTED,
        ).move_to(DOWN * 3.55)

        self.play(FadeIn(heading), FadeIn(tag), FadeIn(legend), run_time=0.7)
        self.wait(6.4)

        def step(i, eq_tex, reason, font=EQ_FONT):
            e = eq(eq_tex, font_size=font, color=INK)
            e.move_to([EQ_X + e.width / 2, ROWS_Y[i], 0])
            r = note(reason, font_size=REASON_FONT, color=COL_NOTE)
            r.move_to([REASON_X + r.width / 2, ROWS_Y[i], 0])
            self.play(Write(e), FadeIn(r, shift=RIGHT * 0.1), run_time=1.15)
            return e, r

        e1, r1 = step(0, r"z_i = u^T x_i'", "how much of point i lies\nalong u — signed")
        self.wait(4.4)
        e2, r2 = step(1, r"\operatorname{Var}(z) = \frac{1}{n-1} \sum_{i=1}^{n} (z_i - \bar{z})^2",
                      "the sample variance of\nthe projected values")
        self.wait(4.4)
        e3, r3 = step(2, r"\sum_i z_i = u^T \sum_i x_i' = u^T \cdot 0 = 0 \;\Rightarrow\; \bar{z} = 0",
                      "centring made every\ncolumn sum zero —\nso the z's average to 0",
                      font=SMALL_EQ_FONT)
        self.wait(4.4)
        e4, r4 = step(3, r"\operatorname{Var}(z) = \frac{1}{n-1} \sum_{i=1}^{n} z_i^2",
                      "the mean term vanishes — variance\nis now just a sum of squares")
        self.wait(4.4)
        e5, r5 = step(4, r"z_i^2 = (u^T x_i')(u^T x_i') = (u^T x_i')(x_i'^T u)",
                      "a scalar equals its own\ntranspose: (uᵀx)ᵀ = xᵀu",
                      font=15.5)
        self.wait(4.4)
        e6, r6 = step(5, r"z_i^2 = u^T \left( x_i' x_i'^T \right) u",
                      "associativity —\nregroup the brackets",
                      font=SMALL_EQ_FONT)
        self.wait(4.4)
        e7, r7 = step(6, r"\operatorname{Var}(z) = u^T \left( \frac{1}{n-1} \sum_i x_i' x_i'^T \right) u",
                      "u is fixed while we sum,\nso it factors outside",
                      font=SMALL_EQ_FONT)
        self.wait(4.4)

        # step 8: recognise C
        e8 = eq(r"\operatorname{Var}(z) = u^T C u", font_size=30, color=COL_U)
        e8.move_to([EQ_X + e8.width / 2, ROWS_Y[7] - 0.12, 0])
        r8 = note("this is exactly the\ncovariance matrix\nfrom Step 4", font_size=REASON_FONT, color=COL_NOTE)
        r8.move_to([REASON_X + r8.width / 2, ROWS_Y[7] - 0.12, 0])
        self.play(Write(e8), FadeIn(r8), run_time=1.0)
        box8 = SurroundingRectangle(e8, color=COL_U, buff=0.14, corner_radius=0.1)
        self.play(Create(box8), run_time=0.6)
        self.wait(8.9)

        # scatter version
        e9 = eq(r"\text{equivalently:} \quad u^T S u = (n-1)\,\operatorname{Var}(z)", font_size=SMALL_EQ_FONT,
                color=MUTED)
        e9.move_to([EQ_X + e9.width / 2, ROWS_Y[8], 0])
        r9 = note("scatter version — same\nmaximiser, constant factor", font_size=REASON_FONT, color=MUTED)
        r9.move_to([REASON_X + r9.width / 2, ROWS_Y[8], 0])
        self.play(FadeIn(e9), FadeIn(r9), run_time=0.8)
        self.wait(10.4)

        takeaway = MathTex(
            r"\text{Best direction} \;\Rightarrow\; \text{make } u^T C u \text{ as large as possible}",
            font_size=19, color=INK,
        ).move_to(UP * 2.92)
        self.play(FadeIn(takeaway, shift=DOWN * 0.12), run_time=0.8)
        self.wait(10.4)
