# PCA — Complete Storyboard (time-coded)

Video: **Principal Component Analysis — from absolute first principles**

Duration target: 11:00–12:00 (this edit: **11:40**) · 1920×1080 · Manim CE 0.22.1 · 60 fps

Cue numbers refer to `pca_subtitles.srt`. Voiceover text is verbatim from `voiceover.md` (record with those words).

Palette: cyan = original data · red = mean · green = centred data · violet = matrices · amber = test direction u · orange = PC1 · blue = PC2.

---

## Scene 01 — The problem (0:00–0:45)

**Visual / animation:** Title card fades in (1.1 s), subtitle tagline, fade out. Thin 2 pt axes are drawn with `Create`; x and y axis labels fade in. Four cyan dots pop in with a lagged scale-in. Right panel: observation list and the guiding question in bold. A faint amber dashed line along the cloud's long axis appears as a visual promise of what is coming, then fades out.

**On-screen mathematics:**

- `(5,3), (1,1), (4,4), (2,0)`
- `uᵀCu never appears yet — the question is purely geometric`

**Pacing note:** Establish the visual grammar: cyan = data, amber = candidate direction, thin dark axes, left plot / right panel.

**Subtitle cues:** 1–8 (see pca_subtitles.srt)

**Voiceover (exact):**

> Let's start with a tiny dataset. Four observations, two features each — call them x and y.
> There they are. Notice the cloud leans up and to the right: when x is large, y tends to be large too.
> Here's the question we want to answer.
> Can we find a direction along which these points vary as much as possible?
> That single question is the whole engine of Principal Component Analysis.
> Only four points — small enough to verify every step by hand.
> And we're going to build the answer from scratch — no formulas until they're forced on us.

---

## Scene 02 — Centring (0:45–1:45)

**Visual / animation:** Coordinates label each point. Right panel computes μx and μy term by term with `Write`. A red mean marker (dot + ring) grows at (3,2). On 'Watch the cloud slide', all four dots and the mean marker are interpolated to their centred positions over ~2 s; dots recolour cyan → green as they arrive; an origin dot and 'O' label mark (0,0). Centred coordinate labels fade in.

**On-screen mathematics:**

- `μx = (5+1+4+2)/4 = 3, μy = (3+1+4+0)/4 = 2`
- `μ = (3,2)`
- `xᵢ′ = xᵢ − μ`
- `centred: (2,1), (−2,−1), (1,2), (−1,−2)`
- `opposite pairs sum to zero — the cancellation is the point of centring`

**Pacing note:** The entire transformation is a literal translation: the cloud moves, axes do not — 'same shape, new origin' is felt, not asserted.

**Subtitle cues:** 9–18 (see pca_subtitles.srt)

**Voiceover (exact):**

> First, meet the data: five three, one one, four four, and two zero.
> Average x: twelve over four — three. Average y: eight over four — two.
> So the mean is the point three two — here in red.
> Why does the average matter? Because we don't care where the cloud sits — we care how it spreads.
> So we subtract the mean from every point. Watch the cloud slide:
> two one, minus two minus one, one two, minus one minus two.
> Its centre is now the origin. Same shape, same spread — just a better vantage point.
> Notice the two pairs of opposite points — their deviations cancel out, which is exactly why the means are zero.
> Every formula from here on works with deviations from the mean.

---

## Scene 03 — Variance (1:45–2:35)

**Visual / animation:** Centred cloud stays on the left. Right panel: the variance formula appears term by term; the four bullet reasons fade in one by one; the n−1 vs n convention is stated in muted text; the actual sums (Σx′² = 10 → Var = 10/3) are written; the panel pivots from the question to the limitation of variance.

**On-screen mathematics:**

- `Var(x) = 1/(n−1) Σ(xᵢ − x̄)²`
- `Σx′² = 4+4+1+1 = 10 ⇒ Var(x) = 10/3`
- `Σy′² = 1+1+4+4 = 10 ⇒ Var(y) = 10/3`
- `sample uses n−1; population uses n; directions are unchanged by the choice`

**Pacing note:** Variance is introduced as a question ('how spread out?'), built from its four operations, then immediately applied to the real numbers.

**Subtitle cues:** 19–27 (see pca_subtitles.srt)

**Voiceover (exact):**

> So how spread out are the points? Start with one variable.
> The variance of x: subtract the mean, square each deviation — signs vanish, and big gaps count more —
> then add them up, and divide by n minus one for sample variance.
> We'll use n minus one throughout; dividing by n instead rescales every variance equally — no direction changes.
> Here, the squared deviations of x are four plus four plus one plus one — ten — so the variance is ten thirds.
> Same for y. But variance only looks along one axis.
> It cannot tell us that x and y rise together.

---

## Scene 04 — Covariance (2:35–3:35)

**Visual / animation:** Same centred cloud. The two quadrants where deviations share a sign are tinted green (upper-right and lower-left) with small '(+,+)' and '(−,−)' tags — positive products live there. The three covariance regimes appear as short lines. The four products are written out: 2, 2, 2, 2. The formula lands, then the result Cov = 8/3 ≈ 2.67 is written in violet. The panel closes by staging the three spread numbers that Scene 05 will package into C.

**On-screen mathematics:**

- `Cov(x,y) = 1/(n−1) Σ(xᵢ−x̄)(yᵢ−ȳ)`
- `products: (2)(1) = 2, (−2)(−1) = 2, (1)(2) = 2, (−1)(−2) = 2`
- `Cov = 8/3 ≈ 2.67 > 0 — the features increase together`
- `Var(x) = Var(y) = 10/3`

**Pacing note:** Geometry first (quadrants), then arithmetic (products), then the formula — never the other way round.

**Subtitle cues:** 28–36 (see pca_subtitles.srt)

**Voiceover (exact):**

> That rising-together relationship is what covariance measures.
> Three regimes: positive — both rise together. Negative — one rises as the other falls. Near zero — no clear linear link.
> For each point, multiply its two deviations.
> All four products are positive: two, two, two, two.
> Had they all come out negative, we'd read negative covariance — one rises, the other falls.
> Here: positive — the features clearly move together.
> The formula: one over n minus one, sum of the products of deviations.
> Plug in: eight thirds — about two point six seven.
> For the record: Var of x is ten thirds, Var of y is ten thirds, covariance is eight thirds.
> These three numbers are the raw material of the matrix we build next.

---

## Scene 05 — The scatter matrix, built by hand (3:35–4:55)

**Visual / animation:** The cloud is dimmed to a ghost. One centred point is written as a column vector with a concrete example (2;1). Its outer product is expanded on screen and explicitly contrasted with the dot product. The four outer-product matrices appear one by one in a 2×2 grid with captions 'from (2,1)', 'from (−2,−1)', 'from (1,2)', 'from (−1,−2)'. The grid fades, replaced by the entry-wise sums (10, 8, 8, 10), then the scatter matrix S appears in a violet rounded box. Entry meanings are listed. Finally C = S/3 is derived in two lines and boxed. Closing notes cover directional equivalence, symmetry, and the 'CV matrix' terminology.

**On-screen mathematics:**

- `x′ᵢ = [xᵢ′; yᵢ′]`
- `x′x′ᵀ = [[x², xy],[xy, y²]] vs x′ᵀx = x² + y²`
- `S = Σᵢ x′ᵢx′ᵢᵀ = [[4+4+1+1, 2+2+2+2],[2+2+2+2, 1+1+4+4]] = [[10,8],[8,10]]`
- `C = S/(n−1) = (1/3)S = [[10/3, 8/3],[8/3, 10/3]]`
- `S and C differ by the scalar 1/3 — same eigenvectors, eigenvalues scaled; C = Cᵀ (symmetric)`

**Pacing note:** Each matrix entry is literally accumulated dot-by-dot on screen: the scatter matrix is assembled, not displayed.

**Subtitle cues:** 37–52 (see pca_subtitles.srt)

**Voiceover (exact):**

> Here's the move that surprises people.
> Take one centred point as a column vector.
> Multiply it by its own transpose — an outer product — and you get a two by two matrix:
> x squared, x y, x y, y squared.
> Not the dot product — that's a single number.
> Do this for every point and add.
> Two one gives four two, two one — and so does minus two minus one; the signs flip twice.
> One two and minus one minus two give one two, two four.
> Add entry by entry: ten; the cross entries, eight; bottom-right, ten.
> That's the scatter matrix S.
> Top-left: squared spread in x. Bottom-right: same for y. Off-diagonal: joint variation.
> Divide by n minus one — three — and you get the covariance matrix C:
> ten thirds, eight thirds; eight thirds, ten thirds.
> Two facts matter. One: S and C carry identical directional information — scaling by a positive number never moves an eigenvector; eigenvalues just shrink.
> Two: C is symmetric — both cross entries are eight thirds.

---

## Scene 06 — Trying a direction (4:55–6:00)

**Visual / animation:** u is introduced as a free column vector. The projection formula z = uᵀx′ appears with a one-line geometric reading. Three trial directions are tested in sequence, each with its own 1-D projected number line on the right: x-direction (variance 10/3), y-direction (10/3), the diagonal (variance 6, projections at ±3/√2, duplicate dots staggered perpendicular to the line so pairs are visible). Dashed perpendiculars drop from each point to u; foot dots mark the feet. The question 'What makes one direction better?' is asked on screen, then answered: greatest projected variance. The doubling cheat is shown (variance ×4), forcing uᵀu = 1.

**On-screen mathematics:**

- `u = [u_x; u_y]`
- `z = uᵀx′ — signed shadow length`
- `uᵀu = u_x² + u_y² = 1 (constraint, not convention)`
- `u=(1,0): Var=10/3;  u=(0,1): Var=10/3;  u=(1,1)/√2: Var=6`

**Pacing note:** The optimisation is discovered empirically on screen before it is stated algebraically — the viewer has seen all three answers.

**Subtitle cues:** 53–62 (see pca_subtitles.srt)

**Voiceover (exact):**

> Now the real question. Pick any direction — call it u.
> Project every point onto u: the projection coordinate is z equals u transpose x prime.
> Geometrically: how much of each point lies along u — the signed length of its shadow.
> Unit length matters — double u, every z doubles, and the variance quadruples.
> That's not a better direction, just a bigger vector. So we demand u transpose u equals one.
> Try the x direction: projections two, minus two, one, minus one — variance ten thirds.
> Try the y direction: the same.
> Try the diagonal: the points land at plus or minus three over root two — wider spread, and the variance is six.
> So — what makes one direction better than another?
> The one whose projected points have the greatest variance.

---

## Scene 07 — Deriving Var(z) = uᵀCu (6:00–7:20)

**Visual / animation:** The cloud vanishes; the derivation takes the full width. Two columns: algebra on the left, the reason for each step on the right in muted type. Nine rows build uᵀCu from the definition of variance, using centring (Σx′ = 0 ⇒ z̄ = 0), the scalar-transpose identity, associativity, and factoring the fixed u out of the sum. Row 8 recognises C and is boxed in amber; row 9 notes the scatter-matrix variant uᵀSu. A bottom legend defines the symbols; a closing line hands the viewer the optimisation problem for the next scene.

**On-screen mathematics:**

- `Var(z) = 1/(n−1) Σ(zᵢ − z̄)², z̄ = 0`
- `zᵢ² = (uᵀx′ᵢ)(x′ᵢᵀu)`
- `Var(z) = uᵀ(1/(n−1) Σ x′ᵢx′ᵢᵀ)u`
- `= uᵀCu  (boxed);  uᵀSu = (n−1)·Var(z)`

**Pacing note:** No step is skipped: every algebraic move carries its justification in the right-hand margin — the derivation is the animation.

**Subtitle cues:** 63–74 (see pca_subtitles.srt)

**Voiceover (exact):**

> Now the key algebra — slowly.
> Projected values: z sub i equals u transpose x sub i prime.
> Their variance: one over n minus one, sum of z sub i minus z-bar, squared.
> After centring, the z's average to zero — the sum of the x-prime vectors is the zero vector.
> So variance is one over n minus one times the sum of z sub i squared.
> Rewrite z sub i squared — a scalar times itself.
> A scalar equals its own transpose — so the second factor becomes x prime transpose u.
> Regroup — associativity: u transpose, x prime x prime transpose, u.
> That middle piece is exactly the outer product from before.
> Factor the fixed u's out of the sum: u transpose, one over n minus one times the sum of outer products, u.
> That sum is the scatter matrix — so this is u transpose S u over n minus one — which is u transpose C u.
> The scatter version differs only by the constant n minus one — same maximiser.

---

## Scene 08 — The optimisation problem (7:20–8:05)

**Visual / animation:** The problem is set large and centred: max of uᵀCu subject to uᵀu = 1. The four players are annotated one at a time. The scaling cheat is shown explicitly (u → 2u quadruples uᵀCu). Lagrange's idea is introduced in words, then the Lagrangian L(u, λ) is written; λ is defined as the price of the constraint; note that L = objective wherever the constraint holds.

**On-screen mathematics:**

- `max_u uᵀCu  s.t.  uᵀu = 1`
- `u → 2u ⇒ uᵀCu → 4uᵀCu`
- `L(u, λ) = uᵀCu − λ(uᵀu − 1)`

**Pacing note:** The constraint is motivated by a concrete cheat, not asserted; the multiplier is introduced as bookkeeping for the constraint.

**Subtitle cues:** 75–83 (see pca_subtitles.srt)

**Voiceover (exact):**

> So the problem is now precise.
> Maximise u transpose C u — the variance along u — subject to u transpose u equals one.
> U is the direction we choose.
> C holds the spread and joint variation of the data.
> u transpose C u is the variance we're buying.
> The constraint blocks cheating by scaling.
> How do you maximise with a constraint?
> Fold it into the objective with a new unknown, lambda — the Lagrange multiplier.
> L equals u transpose C u minus lambda times u transpose u minus one.
> When the constraint holds, the second term is zero — so an ordinary maximum of L is exactly our constrained maximum.

---

## Scene 09 — The gradient gives Cu = λu (8:05–9:20)

**Visual / animation:** Differentiation, done honestly in 2-D. C is written with symmetric a, b, d; u as p, q. uᵀCu is expanded to ap² + 2bpq + dq²; partial derivatives are taken by hand; the gradient is vectorised and identified as 2Cu — with an explicit note that the cross terms match only because C is symmetric. The same computation on uᵀu yields 2u. The Lagrangian is recalled, its gradient is set to zero, and the equation is boxed: Cu = λu.

**On-screen mathematics:**

- `uᵀCu = ap² + 2bpq + dq²`
- `∂p = 2ap + 2bq;  ∂q = 2bp + 2dq`
- `∇u(uᵀCu) = 2Cu (symmetry is essential)`
- `∇u(uᵀu) = 2u`
- `∇L = 2Cu − 2λu = 0  ⇒  Cu = λu`

**Pacing note:** Matrix-calculus rules are demystified by brute-force expansion before being used — the 'trick' is verified, not trusted.

**Subtitle cues:** 84–93 (see pca_subtitles.srt)

**Voiceover (exact):**

> To find that maximum, differentiate.
> First — what is the gradient of u transpose C u?
> Don't trust matrix calculus blindly. Expand it in two dimensions.
> C equals a b, b d; u equals p q.
> Then u transpose C u is a p squared plus two b p q plus d q squared — an ordinary quadratic in p and q.
> Differentiate: two a p plus two b q — and two b p plus two d q.
> Vectorise that: two times a b, b d, times p q — exactly two C u.
> The cross terms match only because C is symmetric — which every covariance matrix is.
> The same trick on u transpose u gives two u.
> So the gradient of L is two C u minus two lambda u.
> At a maximum, the gradient vanishes: two C u equals two lambda u.
> Divide by two.
> C u equals lambda u.

---

## Scene 10 — What Cu = λu means (9:20–10:15)

**Visual / animation:** Left stage: a unit eigenvector v₁ (amber) is drawn from a common origin; its image under C is drawn in orange at the same angle, labelled Cv₁ = 6v₁ — same direction, stretched (lengths schematic). A grey non-example arrow at 20° and its rotated image at ≈42° make the contrast concrete. Right panel: definition of eigenvector/eigenvalue; the variance-along-eigenvector chain uᵀCu = λ(uᵀu) = λ; non-negativity via the sum-of-squares form (PSD); v₁·v₂ = 0; and the S = 3C scaling remark.

**On-screen mathematics:**

- `Cv = λv`
- `Var = uᵀCu = uᵀ(λu) = λ(uᵀu) = λ`
- `uᵀCu = (1/(n−1))Σ(uᵀx′ᵢ)² ≥ 0 ⇒ PSD`
- `v₁·v₂ = (1)(1)/2 + (1)(−1)/2 = 0`
- `S = 3C: eigenvectors unchanged, eigenvalues 18 and 2`

**Pacing note:** Definition first, then the visual proof of non-rotation, then the λ = Var identity derived live.

**Subtitle cues:** 94–102 (see pca_subtitles.srt)

**Voiceover (exact):**

> That equation should ring a bell.
> C times u equals lambda times u — a nonzero vector that C merely stretches, never rotates: an eigenvector.
> Lambda is its eigenvalue.
> Our candidates for the best direction are exactly the eigenvectors of C.
> And watch the payoff:
> for a unit eigenvector, u transpose C u equals u transpose lambda u — equals lambda times u transpose u — equals lambda.
> The eigenvalue is the variance along its eigenvector.
> Eigenvalues are non-negative — a sum of squares — so C is positive semidefinite.
> And because C is symmetric, these eigenvectors can be chosen perpendicular — ours: a half minus a half, zero.
> S is 3C — same eigenvectors, eigenvalues eighteen and two.

---

## Scene 11 — Solving for our data (10:15–10:55)

**Visual / animation:** Computation panel on the right; the scatter stays on the left with both PC lines drawn through the origin (PC1 amber-orange, PC2 blue). det(C − λI) = 0 is expanded; λ = 6 and λ = 2/3 fall out. Each eigenvector is solved from its equation, displayed and rationalised to (1/√2)(1,±1). The 'why the largest' argument closes the scene: any unit u = av₁ + bv₂, uᵀCu = 6a² + (2/3)b² = 6 − (16/3)b² ≤ 6.

**On-screen mathematics:**

- `det(C − λI) = (10/3 − λ)² − (8/3)² = 0`
- `λ₁ = 6, λ₂ = 2/3`
- `v₁ = (1/√2)(1,1), v₂ = (1/√2)(1,−1)`
- `uᵀCu = 6a² + (2/3)b² ≤ 6  (equality iff b = 0)`
- `PC1 = direction of largest eigenvalue`

**Pacing note:** The general theory is cashed out on the actual numbers; the plot and the algebra point at the same diagonal.

**Subtitle cues:** 103–112 (see pca_subtitles.srt)

**Voiceover (exact):**

> Now just compute.
> Determinant of C minus lambda I: ten thirds minus lambda, squared, minus eight thirds squared — zero.
> So lambda is six, or two thirds.
> For six: v x equals v y — v one is one over root two, one one.
> For two thirds: v x equals minus v y — one over root two, one minus one.
> Why the largest? Any unit direction is a v-one plus b v-two — a squared plus b squared one.
> Its variance: six a squared plus two thirds b squared — at most six.
> The biggest eigenvalue wins.

---

## Scene 12 — What we accomplished (10:55–11:40)

**Visual / animation:** Both PCs drawn over the centred cloud (PC1 bold, PC2 faded). The full chain appears as two short rows of steps with arrows. Two horizontal bars materialise, proportional to 0.9 and 0.1, captioned with the exact fractions and percentages. A three-line takeaway states the 1-D projection and the honesty note (90% is this dataset). Everything fades to black; the closing insight lands; final end card: 'Principal Component Analysis — built from first principles — no step skipped.'

**On-screen mathematics:**

- `explained variance: λ₁/(λ₁+λ₂) = 6/(20/3) = 0.90;  λ₂/(λ₁+λ₂) = (2/3)/(20/3) = 0.10`
- `project onto PC1 ⇒ 1-D representation keeping 90% of variance (this dataset)`

**Pacing note:** Synthesis: the whole journey replayed in two rows of text, then the quantitative payoff, then the single-sentence moral.

**Subtitle cues:** 113–122 (see pca_subtitles.srt)

**Voiceover (exact):**

> Look what we did.
> Data. Centre it. Scatter matrix. Covariance matrix. Project.
> Derive u transpose C u. Maximise.
> And eigenvectors fell out — keep the largest.
> Here, PC one carries six over six plus two thirds — ninety percent of the total variance; PC two keeps ten.
> Project onto PC one and you get a one-dimensional sketch that keeps ninety percent —
> the rest is discarded on purpose. That's the trade PCA always makes.
> Ninety percent is this dataset, not a law.
> And notice how we got here.
> Not by an eigenvector trick — eigenvectors are simply what the variance-maximising problem demands.
> That's PCA.

---
