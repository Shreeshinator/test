#!/usr/bin/env python3
"""Generate storyboard.md — the time-coded production plan for the video.

VO text is pulled verbatim from voiceover.md so the two can never drift apart;
this file adds the visual design, on-screen maths and subtitle cue ranges.
"""
import re

vo = open("voiceover.md", encoding="utf-8").read()
sections = re.split(r"\n## ", vo)[1:]
scenes = []
for sec in sections:
    header, rest = sec.split("\n", 1)
    body = rest.split("VO:\n", 1)[1]
    votext, onscreen = body.split("\nOn screen:", 1)
    m = re.match(r"(Scene \d+) — (.+) \((\d+):(\d+)–(\d+):(\d+)\)", header)
    num, name, m1, s1, m2, s2 = m.groups()
    scenes.append({
        "num": int(num.split()[1]),
        "name": name.strip(),
        "start": f"{int(m1)}:{int(s1):02d}",
        "end": f"{int(m2)}:{int(s2):02d}",
        "vo": votext.strip(),
        "on_screen_brief": onscreen.strip(),
    })

DESIGN = {
    1: {
        "visual": ("Title card fades in (1.1 s), subtitle tagline, fade out. "
                   "Thin 2 pt axes are drawn with `Create`; x and y axis labels fade in. "
                   "Four cyan dots pop in with a lagged scale-in. Right panel: observation list "
                   "and the guiding question in bold. A faint amber dashed line along the cloud's "
                   "long axis appears as a visual promise of what is coming, then fades out."),
        "math": ["(5,3), (1,1), (4,4), (2,0)", "uᵀCu never appears yet — the question is purely geometric"],
        "animation": "Establish the visual grammar: cyan = data, amber = candidate direction, thin dark axes, left plot / right panel.",
    },
    2: {
        "visual": ("Coordinates label each point. Right panel computes μx and μy term by term with `Write`. "
                   "A red mean marker (dot + ring) grows at (3,2). On 'Watch the cloud slide', all four dots "
                   "and the mean marker are interpolated to their centred positions over ~2 s; dots recolour "
                   "cyan → green as they arrive; an origin dot and 'O' label mark (0,0). Centred coordinate "
                   "labels fade in."),
        "math": ["μx = (5+1+4+2)/4 = 3, μy = (3+1+4+0)/4 = 2", "μ = (3,2)", "xᵢ′ = xᵢ − μ",
                 "centred: (2,1), (−2,−1), (1,2), (−1,−2)", "opposite pairs sum to zero — the cancellation is the point of centring"],
        "animation": "The entire transformation is a literal translation: the cloud moves, axes do not — 'same shape, new origin' is felt, not asserted.",
    },
    3: {
        "visual": ("Centred cloud stays on the left. Right panel: the variance formula appears term by term; "
                   "the four bullet reasons fade in one by one; the n−1 vs n convention is stated in muted text; "
                   "the actual sums (Σx′² = 10 → Var = 10/3) are written; the panel pivots from the question "
                   "to the limitation of variance."),
        "math": ["Var(x) = 1/(n−1) Σ(xᵢ − x̄)²", "Σx′² = 4+4+1+1 = 10 ⇒ Var(x) = 10/3", "Σy′² = 1+1+4+4 = 10 ⇒ Var(y) = 10/3",
                 "sample uses n−1; population uses n; directions are unchanged by the choice"],
        "animation": "Variance is introduced as a question ('how spread out?'), built from its four operations, then immediately applied to the real numbers.",
    },
    4: {
        "visual": ("Same centred cloud. The two quadrants where deviations share a sign are tinted green "
                   "(upper-right and lower-left) with small '(+,+)' and '(−,−)' tags — positive products live "
                   "there. The three covariance regimes appear as short lines. The four products are written out: "
                   "2, 2, 2, 2. The formula lands, then the result Cov = 8/3 ≈ 2.67 is written in violet. "
                   "The panel closes by staging the three spread numbers that Scene 05 will package into C."),
        "math": ["Cov(x,y) = 1/(n−1) Σ(xᵢ−x̄)(yᵢ−ȳ)", "products: (2)(1) = 2, (−2)(−1) = 2, (1)(2) = 2, (−1)(−2) = 2",
                 "Cov = 8/3 ≈ 2.67 > 0 — the features increase together", "Var(x) = Var(y) = 10/3"],
        "animation": "Geometry first (quadrants), then arithmetic (products), then the formula — never the other way round.",
    },
    5: {
        "visual": ("The cloud is dimmed to a ghost. One centred point is written as a column vector with a "
                   "concrete example (2;1). Its outer product is expanded on screen and explicitly contrasted "
                   "with the dot product. The four outer-product matrices appear one by one in a 2×2 grid with "
                   "captions 'from (2,1)', 'from (−2,−1)', 'from (1,2)', 'from (−1,−2)'. The grid fades, replaced "
                   "by the entry-wise sums (10, 8, 8, 10), then the scatter matrix S appears in a violet "
                   "rounded box. Entry meanings are listed. Finally C = S/3 is derived in two lines and boxed. "
                   "Closing notes cover directional equivalence, symmetry, and the 'CV matrix' terminology."),
        "math": ["x′ᵢ = [xᵢ′; yᵢ′]", "x′x′ᵀ = [[x², xy],[xy, y²]] vs x′ᵀx = x² + y²",
                 "S = Σᵢ x′ᵢx′ᵢᵀ = [[4+4+1+1, 2+2+2+2],[2+2+2+2, 1+1+4+4]] = [[10,8],[8,10]]",
                 "C = S/(n−1) = (1/3)S = [[10/3, 8/3],[8/3, 10/3]]",
                 "S and C differ by the scalar 1/3 — same eigenvectors, eigenvalues scaled; C = Cᵀ (symmetric)"],
        "animation": "Each matrix entry is literally accumulated dot-by-dot on screen: the scatter matrix is assembled, not displayed.",
    },
    6: {
        "visual": ("u is introduced as a free column vector. The projection formula z = uᵀx′ appears with a "
                   "one-line geometric reading. Three trial directions are tested in sequence, each with its own "
                   "1-D projected number line on the right: x-direction (variance 10/3), y-direction (10/3), "
                   "the diagonal (variance 6, projections at ±3/√2, duplicate dots staggered perpendicular to "
                   "the line so pairs are visible). Dashed perpendiculars drop from each point to u; foot dots "
                   "mark the feet. The question 'What makes one direction better?' is asked on screen, then "
                   "answered: greatest projected variance. The doubling cheat is shown (variance ×4), forcing "
                   "uᵀu = 1."),
        "math": ["u = [u_x; u_y]", "z = uᵀx′ — signed shadow length", "uᵀu = u_x² + u_y² = 1 (constraint, not convention)",
                 "u=(1,0): Var=10/3;  u=(0,1): Var=10/3;  u=(1,1)/√2: Var=6"],
        "animation": "The optimisation is discovered empirically on screen before it is stated algebraically — the viewer has seen all three answers.",
    },
    7: {
        "visual": ("The cloud vanishes; the derivation takes the full width. Two columns: algebra on the left, "
                   "the reason for each step on the right in muted type. Nine rows build uᵀCu from the definition "
                   "of variance, using centring (Σx′ = 0 ⇒ z̄ = 0), the scalar-transpose identity, associativity, "
                   "and factoring the fixed u out of the sum. Row 8 recognises C and is boxed in amber; row 9 "
                   "notes the scatter-matrix variant uᵀSu. A bottom legend defines the symbols; a closing line "
                   "hands the viewer the optimisation problem for the next scene."),
        "math": ["Var(z) = 1/(n−1) Σ(zᵢ − z̄)², z̄ = 0", "zᵢ² = (uᵀx′ᵢ)(x′ᵢᵀu)", "Var(z) = uᵀ(1/(n−1) Σ x′ᵢx′ᵢᵀ)u",
                 "= uᵀCu  (boxed);  uᵀSu = (n−1)·Var(z)"],
        "animation": "No step is skipped: every algebraic move carries its justification in the right-hand margin — the derivation is the animation.",
    },
    8: {
        "visual": ("The problem is set large and centred: max of uᵀCu subject to uᵀu = 1. The four players are "
                   "annotated one at a time. The scaling cheat is shown explicitly (u → 2u quadruples uᵀCu). "
                   "Lagrange's idea is introduced in words, then the Lagrangian L(u, λ) is written; λ is defined "
                   "as the price of the constraint; note that L = objective wherever the constraint holds."),
        "math": ["max_u uᵀCu  s.t.  uᵀu = 1", "u → 2u ⇒ uᵀCu → 4uᵀCu", "L(u, λ) = uᵀCu − λ(uᵀu − 1)"],
        "animation": "The constraint is motivated by a concrete cheat, not asserted; the multiplier is introduced as bookkeeping for the constraint.",
    },
    9: {
        "visual": ("Differentiation, done honestly in 2-D. C is written with symmetric a, b, d; u as p, q. "
                   "uᵀCu is expanded to ap² + 2bpq + dq²; partial derivatives are taken by hand; the gradient is "
                   "vectorised and identified as 2Cu — with an explicit note that the cross terms match only "
                   "because C is symmetric. The same computation on uᵀu yields 2u. The Lagrangian is recalled, "
                   "its gradient is set to zero, and the equation is boxed: Cu = λu."),
        "math": ["uᵀCu = ap² + 2bpq + dq²", "∂p = 2ap + 2bq;  ∂q = 2bp + 2dq", "∇u(uᵀCu) = 2Cu (symmetry is essential)",
                 "∇u(uᵀu) = 2u", "∇L = 2Cu − 2λu = 0  ⇒  Cu = λu"],
        "animation": "Matrix-calculus rules are demystified by brute-force expansion before being used — the 'trick' is verified, not trusted.",
    },
    10: {
        "visual": ("Left stage: a unit eigenvector v₁ (amber) is drawn from a common origin; its image under C "
                   "is drawn in orange at the same angle, labelled Cv₁ = 6v₁ — same direction, stretched "
                   "(lengths schematic). A grey non-example arrow at 20° and its rotated image at ≈42° make the "
                   "contrast concrete. Right panel: definition of eigenvector/eigenvalue; the variance-along-"
                   "eigenvector chain uᵀCu = λ(uᵀu) = λ; non-negativity via the sum-of-squares form (PSD); "
                   "v₁·v₂ = 0; and the S = 3C scaling remark."),
        "math": ["Cv = λv", "Var = uᵀCu = uᵀ(λu) = λ(uᵀu) = λ", "uᵀCu = (1/(n−1))Σ(uᵀx′ᵢ)² ≥ 0 ⇒ PSD",
                 "v₁·v₂ = (1)(1)/2 + (1)(−1)/2 = 0", "S = 3C: eigenvectors unchanged, eigenvalues 18 and 2"],
        "animation": "Definition first, then the visual proof of non-rotation, then the λ = Var identity derived live.",
    },
    11: {
        "visual": ("Computation panel on the right; the scatter stays on the left with both PC lines drawn "
                   "through the origin (PC1 amber-orange, PC2 blue). det(C − λI) = 0 is expanded; λ = 6 and λ = 2/3 "
                   "fall out. Each eigenvector is solved from its equation, displayed and rationalised to "
                   "(1/√2)(1,±1). The 'why the largest' argument closes the scene: any unit u = av₁ + bv₂, "
                   "uᵀCu = 6a² + (2/3)b² = 6 − (16/3)b² ≤ 6."),
        "math": ["det(C − λI) = (10/3 − λ)² − (8/3)² = 0", "λ₁ = 6, λ₂ = 2/3", "v₁ = (1/√2)(1,1), v₂ = (1/√2)(1,−1)",
                 "uᵀCu = 6a² + (2/3)b² ≤ 6  (equality iff b = 0)", "PC1 = direction of largest eigenvalue"],
        "animation": "The general theory is cashed out on the actual numbers; the plot and the algebra point at the same diagonal.",
    },
    12: {
        "visual": ("Both PCs drawn over the centred cloud (PC1 bold, PC2 faded). The full chain appears as two "
                   "short rows of steps with arrows. Two horizontal bars materialise, proportional to 0.9 and "
                   "0.1, captioned with the exact fractions and percentages. A three-line takeaway states the "
                   "1-D projection and the honesty note (90% is this dataset). Everything fades to black; the "
                   "closing insight lands; final end card: 'Principal Component Analysis — built from first "
                   "principles — no step skipped.'"),
        "math": ["explained variance: λ₁/(λ₁+λ₂) = 6/(20/3) = 0.90;  λ₂/(λ₁+λ₂) = (2/3)/(20/3) = 0.10",
                 "project onto PC1 ⇒ 1-D representation keeping 90% of variance (this dataset)"],
        "animation": "Synthesis: the whole journey replayed in two rows of text, then the quantitative payoff, then the single-sentence moral.",
    },
}

CUE_RANGES = [(1,8),(9,18),(19,27),(28,36),(37,52),(53,62),(63,74),(75,83),(84,93),(94,102),(103,112),(113,122)]

out = []
out.append("# PCA — Complete Storyboard (time-coded)\n")
out.append("Video: **Principal Component Analysis — from absolute first principles**\n")
out.append("Duration target: 11:00–12:00 (this edit: **11:40**) · 1920×1080 · Manim CE 0.22.1 · 60 fps\n")
out.append("Cue numbers refer to `pca_subtitles.srt`. Voiceover text is verbatim from `voiceover.md` (record with those words).\n")
out.append("Palette: cyan = original data · red = mean · green = centred data · violet = matrices · amber = test direction u · orange = PC1 · blue = PC2.\n")
out.append("---\n")
for sc in scenes:
    d = DESIGN[sc["num"]]
    c0, c1 = CUE_RANGES[sc["num"] - 1]
    out.append(f"## Scene {sc['num']:02d} — {sc['name']} ({sc['start']}–{sc['end']})\n")
    out.append(f"**Visual / animation:** {d['visual']}\n")
    out.append("**On-screen mathematics:**\n")
    for mline in d["math"]:
        out.append(f"- `{mline}`")
    out.append(f"\n**Pacing note:** {d['animation']}\n")
    out.append(f"**Subtitle cues:** {c0}–{c1} (see pca_subtitles.srt)\n")
    out.append(f"**Voiceover (exact):**\n\n> {sc['vo'].replace(chr(10), chr(10) + '> ')}\n")
    out.append("---\n")

open("storyboard.md", "w", encoding="utf-8").write("\n".join(out))
print("storyboard.md written,", len("\n".join(out).splitlines()), "lines")
