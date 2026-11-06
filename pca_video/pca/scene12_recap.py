"""Scene 12 (10:55-11:40) — what we accomplished; 90/10 split; the chain; the insight."""

from manim import *
from pca.common import (
    BG, INK, MUTED, COL_CENTR, COL_MATRIX, COL_NOTE, COL_PC1, COL_PC2,
    base_axes, axes_labels, make_dots, screen_title, scene_tag, eq, note, pc_line, CENTERED,
)


class Scene12Recap(Scene):
    def construct(self):
        self.camera.background_color = BG
        heading = screen_title("Step 11 — What we actually accomplished")
        tag = scene_tag(12, "Recap & takeaway")
        axes = base_axes()
        labels = axes_labels(axes)
        dots = make_dots(axes, CENTERED, COL_CENTR)
        pc1 = pc_line(axes, (1, 1), 2.8, COL_PC1, stroke_width=6)
        pc2 = pc_line(axes, (1, -1), 2.1, COL_PC2, stroke_width=4).set_opacity(0.85)

        self.play(FadeIn(heading), FadeIn(tag), run_time=0.5)
        self.play(Create(axes), FadeIn(labels), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.12), run_time=1.0)
        self.play(Create(pc1), Create(pc2), run_time=0.9)
        self.wait(1.8)

        # --- the chain ---------------------------------------------------------
        head = Tex("The whole chain, in one breath", font_size=18, color=COL_MATRIX)
        head.move_to(RIGHT * 3.6 + UP * 2.25)
        chainA = Text("Data → Centre → S → C", font_size=19, color=INK)
        chainB = MathTex(r"\mathrm{Var}(z) = u^T C u \;\Rightarrow\; \max \;\Rightarrow\; C u = \lambda u \;\Rightarrow\; \lambda_1",
                       font_size=16.5, color=INK)
        chainA.move_to(RIGHT * 3.6 + UP * 1.62)
        chainB.move_to(RIGHT * 3.6 + UP * 1.08)
        self.play(FadeIn(head), run_time=0.4)
        self.play(FadeIn(chainA, shift=RIGHT * 0.15), run_time=0.6)
        self.play(FadeIn(chainB, shift=RIGHT * 0.15), run_time=0.6)
        self.wait(3.4)

        # --- explained variance bars --------------------------------------------
        var_head = note("How much variation does each axis keep?", font_size=16, color=COL_NOTE)
        var_head.move_to(RIGHT * 3.6 + UP * 0.32)
        self.play(FadeIn(var_head), run_time=0.5)

        bar_x = 0.55
        bar_w_full = 4.35
        bar1 = Rectangle(width=bar_w_full, height=0.36, fill_color=COL_PC1,
                         fill_opacity=0.9, stroke_width=0)
        bar1.move_to([bar_x + bar_w_full / 2, -0.28, 0])
        bar1_lbl = MathTex(r"\frac{6}{6 + 2/3} = 0.90 \;\; \Rightarrow \;\; 90\%", font_size=17,
                           color=COL_PC1)
        bar1_lbl.move_to([bar_x + bar1_lbl.width / 2, -0.72, 0])
        bar1_name = MathTex("PC1", font_size=19, color=COL_PC1).next_to(bar1, LEFT, buff=0.14)
        bar2 = Rectangle(width=bar_w_full * 0.1, height=0.36, fill_color=COL_PC2,
                         fill_opacity=0.9, stroke_width=0)
        bar2.move_to([bar_x + bar_w_full * 0.1 / 2, -1.32, 0])
        bar2_lbl = MathTex(r"\frac{2/3}{6 + 2/3} = 0.10 \;\; \Rightarrow \;\; 10\%", font_size=17,
                           color=COL_PC2)
        bar2_lbl.move_to([bar_x + bar2_lbl.width / 2, -1.76, 0])
        bar2_name = MathTex("PC2", font_size=19, color=COL_PC2).next_to(bar2, LEFT, buff=0.14)
        self.play(FadeIn(bar1_name), GrowFromEdge(bar1, LEFT), run_time=0.9)
        self.play(FadeIn(bar1_lbl), run_time=0.5)
        self.play(FadeIn(bar2_name), GrowFromEdge(bar2, LEFT), run_time=0.6)
        self.play(FadeIn(bar2_lbl), run_time=0.5)
        self.wait(4.2)

        takeaway = note("Project onto PC1 → a 1-D sketch keeping 90% of the variation.\n"
                        "The other 10% is discarded on purpose — PCA trades\n"
                        "detail for simplicity. 90% is this dataset, not a law.",
                        font_size=15, color=INK)
        takeaway.move_to(RIGHT * 3.6 + DOWN * 2.75)
        self.play(FadeIn(takeaway), run_time=0.9)
        self.wait(7.0)

        # --- closing insight ----------------------------------------------------
        chain_out = VGroup(head, chainA, chainB, var_head, bar1, bar1_lbl, bar1_name,
                           bar2, bar2_lbl, bar2_name, takeaway)
        self.play(FadeOut(chain_out), FadeOut(axes), FadeOut(labels),
                  FadeOut(dots), FadeOut(pc1), FadeOut(pc2), FadeOut(heading), run_time=0.9)

        final1 = Tex("PCA is not an eigenvector trick.", font_size=44, color=INK)
        final2 = Text("Eigenvectors are what the variance-maximising\nproblem forces to the surface.",
                      font_size=24, color=COL_PC1, line_spacing=1.1)
        final1.move_to(UP * 0.55)
        final2.next_to(final1, DOWN, buff=0.4)
        self.play(Write(final1), run_time=1.3)
        self.play(FadeIn(final2, shift=UP * 0.15), run_time=0.9)
        self.wait(7.3)
        self.play(FadeOut(final1), FadeOut(final2), run_time=0.7)

        end_mark = VGroup(
            Text("Principal Component Analysis", font_size=40, weight="BOLD", color=INK),
            Text("built from first principles — no step skipped", font_size=19, color=MUTED),
        ).arrange(DOWN, buff=0.25)
        self.play(FadeIn(end_mark, shift=UP * 0.2), run_time=1.0)
        self.wait(11.7)
