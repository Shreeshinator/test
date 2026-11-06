# PCA — Final Quality Checklist

Ticked items were verified in this project. Items marked **(record)** can only be fully verified after voiceover is recorded.

## Runtime & format
- [x] Video is 11:40 (700 s) — inside the 11:00–12:00 window (sum of the 12 scene slots; layout in README).
- [x] 1920×1080, 16:9, rendered with Manim CE `-qh` (60 fps).
- [x] No external images, stock footage, or fonts — everything is drawn/typeset by Manim + LaTeX.
- [x] Single consistent coordinate system shared by every scatter scene (`pca/common.py: base_axes`); angles are honest (equal x/y scale).
- [x] Background dark (#10151C), axes thin (2 pt), palette consistent: cyan data / red mean / green centred / violet matrices / amber u / orange PC1 / blue PC2.

## Mathematical integrity
- [x] Mean verified: μ = (3, 2) (exact fractions).
- [x] Centred data verified: (2,1), (−2,−1), (1,2), (−1,−2); column sums are exactly 0.
- [x] Scatter matrix verified by entry-wise addition: S = [[10,8],[8,10]].
- [x] Covariance matrix verified: C = S/3 = [[10/3, 8/3],[8/3,10/3]]; symmetric; tr = 20/3; det = 4.
- [x] Eigenvalues verified two ways: characteristic polynomial λ² − (20/3)λ + 4 = 0 ⇒ λ = 6, 2/3; trace/product consistent; sympy confirms factorisation (λ−6)(3λ−2)/3.
- [x] Eigenvectors verified by direct substitution: C·v₁ = 6v₁; C·v₂ = (2/3)v₂; unit norm; orthogonal (½ − ½ = 0); v₁·v₂ = 0.
- [x] Explained ratios verified: 6/(20/3) = 0.90, (2/3)/(20/3) = 0.10.
- [x] Scatter vs covariance distinguished everywhere; S = 3C ⇒ same eigenvectors, eigenvalues 18 & 2 — explicitly stated on screen (Scene 10) and in voiceover.
- [x] "CV matrix" terminology addressed: treated as the same covariance matrix (Scene 05 note on screen + voiceover).
- [x] uᵀCu derivation complete: z̄ = 0 via centring; scalar-transpose identity; associativity; fixed-u factorisation; final boxed Var(z) = uᵀCu (Scene 07). Verified numerically three independent ways (verification.md §8).
- [x] Lagrange derivation complete: quadratic expanded by hand; ∂/∂p, ∂/∂q; ∇(uᵀCu) = 2Cu (symmetry shown as essential); ∇(uᵀu) = 2u; ∇L = 0 ⇒ Cu = λu (Scene 09).
- [x] Eigenvalue = variance along the eigenvector derived (not asserted): uᵀCu = uᵀ(λu) = λ(uᵀu) = λ (Scene 10).
- [x] Largest eigenvalue selected *by proof*, not by declaration: u = av₁ + bv₂, a² + b² = 1 ⇒ uᵀCu = 6a² + (2/3)b² = 6 − (16/3)b² ≤ 6 (Scene 11).
- [x] Positive semidefiniteness derived: uᵀCu = (1/(n−1))Σ(uᵀx′ᵢ)² ≥ 0 (Scene 10).
- [x] 90% is labelled dataset-specific, not a law (Scene 12 voiceover + on-screen text).
- [x] Column-vector convention stated at first use and held consistently; outer product xxᵀ explicitly distinguished from dot product xᵀx (Scene 05); outer product motivated and expanded on screen.
- [x] Sample (n−1) vs population (n) stated; video uses n−1; rescaling effect explained.
- [x] Every identity used is justified at the level of the audience (see verification.md §12 table).

## Pedagogy & structure
- [x] Every concept is introduced before it is used (mean → variance → covariance → S → C → projection → uᵀCu → max → λ → largest λ).
- [x] No step "obvious" claims; each rule (scalar transpose, associativity, symmetry, Fermat, Lagrange) is shown, not cited.
- [x] Outer product built from a concrete 2×2 example before the general sum; scatter matrix assembled dot-by-dot on screen.
- [x] Optimisation problem motivated by a concrete cheat (doubling u quadruples uᵀCu) before the constraint is imposed.
- [x] Constraint uᵀu = 1 presented as honesty, not as a trick; Lagrange introduced only after optimisation need is established.
- [x] Questions drive each scene ("Can we find a direction…?", "What makes one direction better?").
- [x] PCA not presented as "the eigenvector trick" — closing line states eigenvectors are forced by variance maximisation.

## Visual / animation
- [x] Data points one consistent colour per state; cloud physically translated (not swapped) when centring (Scene 02).
- [x] Equations never overlap the scatter plot; derivation scenes use full-width layouts; panels kept inside the frame (verified by frame extraction at 480p).
- [x] Matrices typeset with LaTeX (MathTex); boxed results (S, Cu = λu, Var(z) = uᵀCu, max problem).
- [x] Camera is static throughout (no camera moves); axes never re-created mid-scene.
- [x] Duplicate projections on the 1-D line are staggered perpendicular to the line so overlapping points remain visible.
- [x] 90/10 explained-variance bars drawn to scale (10% bar is exactly 1/9 the 90% bar).
- [x] 1080p legibility: body text ≥ 13.5 pt-equivalent at 1080p; equations 15–58 pt; title hierarchy consistent.
- [x] Transitions use Create / GrowArrow / FadeIn / ReplacementTransform / Transform — no hard cuts inside scenes.

## Narration / subtitles **(record)**
- [x] VO ≈ 1,525 words over 11:40 ≈ 130 wpm (within 125–135 wpm incl. mathematical pauses).
- [x] Tone conversational; numbers spelled as spoken ("ten thirds", "eight over four"); no textbook reading.
- [x] 122 subtitle cues; none exceeds 2 lines; longest line 40 chars; cues match VO content (not equation dumps).
- [x] SRT ends exactly at 11:40; cue timings are word-weighted linear fits to the scene slots.
- [ ] **(record)** Voice recorded per scene, matched to picture; room tone at file ends; re-time cues if a scene is re-cut (edit `make_srt.py`, re-run).
- [ ] **(record)** Spot-check 5 random cues against the spoken audio for sync after recording.

## Known trade-offs (accepted, documented)
- Long static holds (≤ ~10 s) are deliberate: they are where the narration explains the on-screen mathematics; the alternative (narration faster than math) violates the 125–135 wpm constraint.
- The dataset's projections on u are degenerate pairs (by symmetry of the data); the video shows this honestly with staggered dots instead of hiding it.
- 2-D only, as required; the identical argument lifts to p features with a p×p symmetric matrix; the video stays 2-D as specified, and README carries the one-sentence generalisation.

**Verdict: all script-level and render-level checks pass; the only remaining steps are recording the voiceover and a final listen-through.**
