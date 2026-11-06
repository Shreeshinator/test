#!/usr/bin/env python3
"""Generate pca_subtitles.srt from per-scene cue lists.

Timing model: within each scene slot, every cue is shown for a share of the
scene proportional to its word count (a close enough match to 130 wpm speech),
with a 0.25 s gap between cues. Total = 700 s = 11 min 40 s.
"""

SCENES = [  # (start_seconds, [cues])
    (0, [
        "Four observations, two features each.",
        "Call them x and y.",
        "The cloud leans up and to the right.",
        "When x is large,\ny tends to be large too.",
        "Can we find a direction\nalong which they vary most?",
        "That's the whole engine of PCA.",
        "We'll build the answer\nfrom scratch.",
        "No formulas until they're\nforced on us.",
    ]),
    (45, [
        "Meet the data:\n(5,3), (1,1), (4,4), (2,0).",
        "Average x: 12 / 4 = 3.",
        "Average y: 8 / 4 = 2.",
        "μ = (3, 2) — the mean, in red.",
        "We care how the cloud spreads,\nnot where it sits.",
        "Subtract the mean\nfrom every point.",
        "Watch the cloud slide\nto the origin.",
        "Centred: (2,1), (−2,−1), (1,2), (−1,−2).",
        "Same shape — measured\nfrom the middle.",
        "From here on: deviations\nfrom the mean.",
    ]),
    (105, [
        "How spread out are the points?",
        "Start with one variable:\nvariance.",
        "Subtract the mean,\nsquare each deviation.",
        "Squaring kills signs —\nbig gaps count more.",
        "Add them up,\ndivide by n − 1 (sample).",
        "Population variance\ndivides by n instead.",
        "Var(x) = Var(y) = 10/3.",
        "Variance sees only\none axis at a time.",
        "It can't tell x and y\nrise together.",
    ]),
    (155, [
        "Covariance measures\nmoving together.",
        "Positive — both rise together.",
        "Negative — one rises\nas the other falls.",
        "Near zero — no clear\nlinear link.",
        "Multiply each point's\ntwo deviations.",
        "2, 2, 2, 2 — all positive.",
        "Cov(x, y) = 8/3 ≈ 2.67.",
        "Var(x) = Var(y) = 10/3.",
        "These three numbers build\nthe matrix next.",
    ]),
    (215, [
        "Take one centred point\nas a column vector.",
        "Multiply it by its transpose —\nan outer product.",
        "x′x′ᵀ = [[x², xy], [xy, y²]]",
        "The dot product gives\none number.",
        "Do it for every point,\nthen add.",
        "(2,1) and (−2,−1)\ngive the same matrix.",
        "(1,2) and (−1,−2)\ngive the same too.",
        "Entry sums: 10, 8, 8, 10.",
        "That's the scatter matrix S.",
        "Top-left: x spread.\nBottom-right: y spread.",
        "Off-diagonal: joint variation.",
        "C = S / (n − 1) = S / 3.",
        "C = [[10/3, 8/3],\n      [8/3, 10/3]]",
        "S and C carry\nthe same directions.",
        "Dividing by 3 only\nshrinks eigenvalues.",
        "C is symmetric —\nboth cross entries match.",
    ]),
    (295, [
        "Pick any direction — call it u.",
        "Project every point onto u.",
        "z = uᵀx′ — the shadow along u.",
        "Double u → projections double\n→ Var ×4.",
        "That's cheating. So: uᵀu = 1.",
        "Try x: variance = 10/3 ≈ 3.33.",
        "Try y: the same.",
        "Try the diagonal:\nvariance = 6.",
        "What makes one direction\nbetter than another?",
        "The one with greatest\nprojected variance.",
    ]),
    (360, [
        "The projected values: zᵢ = uᵀxᵢ′.",
        "Variance of the z's:\nΣ(zᵢ − z̄)² / (n − 1).",
        "Centring ⇒ the z's\naverage to zero.",
        "So: Var(z) = Σzᵢ² / (n − 1).",
        "zᵢ² = (uᵀxᵢ′)(uᵀxᵢ′)\n      = (uᵀxᵢ′)(xᵢ′ᵀu).",
        "A scalar equals its own transpose.",
        "Regroup: uᵀ(xᵢ′xᵢ′ᵀ)u.",
        "The middle term is\nthe outer product.",
        "Factor the fixed u's\nout of the sum.",
        "The remaining sum is\nthe scatter matrix.",
        "Var(z) = uᵀCu.\nThe key formula.",
        "uᵀSu differs only\nby n − 1.",
    ]),
    (440, [
        "Now the problem is precise:",
        "max uᵀCu  s.t.  uᵀu = 1.",
        "u is the direction we choose.",
        "C holds spread and\njoint variation.",
        "uᵀCu is the variance\nwe're buying.",
        "uᵀu = 1 blocks\nscaling cheats.",
        "Solve the constraint\nwith a multiplier — λ.",
        "L = uᵀCu − λ(uᵀu − 1).",
        "When the constraint holds,\nthat term vanishes.",
    ]),
    (485, [
        "Differentiate. But expand first.",
        "C = [[a, b], [b, d]], u = [p, q].",
        "uᵀCu = ap² + 2bpq + dq².",
        "∂/∂p = 2ap + 2bq.",
        "∂/∂q = 2bp + 2dq.",
        "∇(uᵀCu) = 2Cu —\ncross terms match.",
        "…because C is symmetric.",
        "Same trick: ∇(uᵀu) = 2u.",
        "∇L = 2Cu − 2λu.\nAt a max, ∇L = 0.",
        "Cu = λu.",
    ]),
    (560, [
        "Cu = λu — C stretches u,\nnever rotates it.",
        "That's an eigenvector.\nλ is the eigenvalue.",
        "Our best directions are\neigenvectors of C.",
        "For a unit eigenvector:\nuᵀCu = λ(uᵀu) = λ.",
        "The eigenvalue IS\nthe variance along it.",
        "Eigenvalues are non-negative —\nC is PSD.",
        "Symmetric ⇒ eigenvectors\ncan be perpendicular.",
        "v₁ · v₂ = ½ − ½ = 0.",
        "S = 3C — same vectors,\neigenvalues 18 and 2.",
    ]),
    (615, [
        "det(C − λI) = 0.",
        "(10/3 − λ)² − (8/3)² = 0.",
        "λ₁ = 6,  λ₂ = 2/3.",
        "λ = 6:  v ∝ (1, 1).",
        "v₁ = (1/√2)(1, 1).",
        "λ = 2/3:  v ∝ (1, −1).",
        "v₂ = (1/√2)(1, −1).",
        "Any unit u = av₁ + bv₂,\na² + b² = 1.",
        "uᵀCu = 6a² + (2/3)b² ≤ 6.",
        "Max at b = 0 —\nthe long diagonal wins.",
    ]),
    (655, [
        "Data → centre → S → C.",
        "Project → Var = uᵀCu → max.",
        "Eigenvectors fall out.\nKeep the largest.",
        "PC1 keeps 6/(20/3) = 90%.",
        "PC2 keeps 10%.",
        "Project onto PC1: a 1-D\nsketch keeping 90%.",
        "The other 10% is discarded\non purpose.",
        "90% is this dataset —\nnot a law.",
        "Not an eigenvector trick.",
        "The variance problem\ndemands eigenvectors.",
    ]),
]
SCENE_LEN = [45, 60, 50, 60, 80, 65, 80, 45, 75, 55, 40, 45]  # seconds, sums to 700
GAP = 0.25

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int((s - int(s)) * 1000):03d}"

entries = []
idx = 1
for (start, cues), length in zip(SCENES, SCENE_LEN):
    weights = [max(len(c.split()), 1) for c in cues]
    total_w = sum(weights)
    usable = length - GAP * (len(cues) - 1)
    t = float(start)
    for cue, w in zip(cues, weights):
        dur = usable * w / total_w
        entries.append((idx, t, t + dur, cue))
        t += dur + GAP
        idx += 1

with open("pca_subtitles.srt", "w", encoding="utf-8") as f:
    for idx, a, b, cue in entries:
        f.write(f"{idx}\n{ts(a)} --> {ts(b)}\n{cue}\n\n")

print(f"{len(entries)} cues written; last ends at {entries[-1][2]:.1f}s")
for i, (start, cues) in enumerate(SCENES):
    scene_entries = [e for e in entries if e[1] >= start]
    # count per scene via boundaries
print("total span:", entries[0][1], "->", entries[-1][2])
