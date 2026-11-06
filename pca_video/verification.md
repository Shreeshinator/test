# PCA — Independent Mathematical Verification

Every claimed number in the video is re-derived here from scratch, twice:
by hand (exact fractions) and by symbolic/numerical cross-checks (Python + sympy).

**Dataset (column-vector convention, observations as rows in Excel, columns as features):**

\[
(x_i, y_i) \in \{(5,3), (1,1), (4,4), (2,0)\}, \qquad n = 4, \qquad \text{features} = (x, y)
\]

---

## 1. Mean

\[
\mu_x = \frac{5+1+4+2}{4} = \frac{12}{4} = 3, \qquad \mu_y = \frac{3+1+4+0}{4} = \frac{8}{4} = 2
\]
\[
\boxed{\mu = (3,\ 2)}
\]

## 2. Centred observations  (x′ᵢ = xᵢ − μ)

| point | x′ | y′ | x′² | y′² | x′y′ |
|---|---|---|---|---|---|
| (5,3) | 2 | 1 | 4 | 1 | 2 |
| (1,1) | −2 | −1 | 4 | 1 | 2 |
| (4,4) | 1 | 2 | 1 | 4 | 2 |
| (2,0) | −1 | −2 | 1 | 4 | 2 |
| **Σ** | **0** | **0** | **10** | **10** | **8** |

- Column sums are exactly 0 ✓ (centring worked: \(\bar x' = \bar y' = 0\)).
- Opposite pairs (2,1)/(−2,−1) and (1,2)/(−1,−2) are point reflections through the origin.

## 3. Sample variance & covariance (n − 1 = 3)

\[
\operatorname{Var}(x) = \frac{10}{3} \approx 3.333, \quad
\operatorname{Var}(y) = \frac{10}{3} \approx 3.333, \quad
\operatorname{Cov}(x,y) = \frac{8}{3} \approx 2.667
\]

Sanity checks:
- \(|\operatorname{Cov}| \le \sqrt{\operatorname{Var}_x \operatorname{Var}_y} = 10/3\) ✓ (\(8/3 \le 10/3\); equality would mean perfect linear relation).
- \(\operatorname{Cov} > 0\) ✓ consistent with the cloud leaning bottom-left → top-right.
- Population convention (÷4) would give \(\operatorname{Var} = 2.5,\ \operatorname{Cov} = 2\); every matrix scaled by the same factor 3/4 — eigenvectors unchanged. The video states it uses n − 1.

## 4. Scatter matrix  S = Σ x′ᵢ x′ᵢᵀ

Outer products:
\[
(2,1)\!\to\!\begin{bmatrix}4&2\\2&1\end{bmatrix},\quad
(-2,-1)\!\to\!\begin{bmatrix}4&2\\2&1\end{bmatrix},\quad
(1,2)\!\to\!\begin{bmatrix}1&2\\2&4\end{bmatrix},\quad
(-1,-2)\!\to\!\begin{bmatrix}1&2\\2&4\end{bmatrix}
\]
(rows/cols with even sign flips give identical matrices — as shown on screen.)

\[
S = \begin{bmatrix}4+4+1+1 & 2+2+2+2 \\ 2+2+2+2 & 1+1+4+4\end{bmatrix}
= \boxed{\begin{bmatrix}10 & 8 \\ 8 & 10\end{bmatrix}}
\]

Entry meaning: S₁₁ = Σx′² (10), S₂₂ = Σy′² (10), S₁₂ = S₂₁ = Σx′y′ (8).

## 5. Covariance matrix  C = S / (n − 1) = S / 3

\[
\boxed{C = \begin{bmatrix} 10/3 & 8/3 \\[2pt] 8/3 & 10/3 \end{bmatrix}}
\qquad
\operatorname{tr} C = \tfrac{20}{3}, \qquad \det C = \tfrac{100}{9} - \tfrac{64}{9} = \tfrac{36}{9} = 4
\]

**Symmetric** ✓ (\(C_{12} = C_{21}\), unavoidable for \(xx^T\)-type sums).
**Positive semidefinite** ✓ (\(u^{\top}Cu = \frac{1}{n-1}\sum_i (u^{\top}x'_i)^2 \ge 0\) — a scaled sum of squares; used on screen).

## 6. Eigenvalues — from the characteristic polynomial

\[
\det(C - \lambda I) = \left(\tfrac{10}{3} - \lambda\right)^2 - \left(\tfrac{8}{3}\right)^2
= \lambda^2 - \tfrac{20}{3}\lambda + \tfrac{100}{9} - \tfrac{64}{9}
= \lambda^2 - \tfrac{20}{3}\lambda + 4 = 0
\]

\[
\lambda = \frac{\tfrac{20}{3} \pm \sqrt{\tfrac{400}{9} - 16}}{2}
= \frac{\tfrac{20}{3} \pm \sqrt{\tfrac{256}{9}}}{2}
= \frac{\tfrac{20}{3} \pm \tfrac{16}{3}}{2}
\;\Rightarrow\;
\boxed{\lambda_1 = 6, \qquad \lambda_2 = \tfrac{2}{3}}
\]

Consistency checks:
- Sum: \(6 + \tfrac{2}{3} = \tfrac{20}{3} = \operatorname{tr} C\) ✓
- Product: \(6 \times \tfrac{2}{3} = 4 = \det C\) ✓
- Characteristic polynomial factors as \((\lambda - 6)(3\lambda - 2)/3\) (sympy) ✓

**Scatter matrix** (same exercise): \((10-\lambda)^2 - 64 = 0 \Rightarrow 10-\lambda = \pm 8 \Rightarrow \lambda = 18, 2\).
Exactly \(3 \times\) the C-eigenvalues ✓ — the video's claim "S = 3C scales eigenvalues, eigenvectors unchanged" holds.

## 7. Eigenvectors — from (C − λI)v = 0

**λ₁ = 6:**
\[
C - 6I = \begin{bmatrix}-8/3 & 8/3 \\ 8/3 & -8/3\end{bmatrix}
\Rightarrow -\tfrac{8}{3} v_x + \tfrac{8}{3} v_y = 0 \Rightarrow v_x = v_y \Rightarrow v \parallel (1,1)
\]
\[
\boxed{v_1 = \frac{1}{\sqrt 2}\begin{bmatrix}1 \\ 1\end{bmatrix}}, \qquad |v_1| = 1 ✓
\]

**λ₂ = 2/3:**
\[
C - \tfrac{2}{3} I = \begin{bmatrix}8/3 & 8/3 \\ 8/3 & 8/3\end{bmatrix}
\Rightarrow v_x + v_y = 0 \Rightarrow v \parallel (1,-1)
\]
\[
\boxed{v_2 = \frac{1}{\sqrt 2}\begin{bmatrix}1 \\ -1\end{bmatrix}}, \qquad |v_2| = 1 ✓
\]

Verify directly:
\[
C v_1 = \frac{1}{\sqrt2}\begin{bmatrix} 10/3 + 8/3 \\ 8/3 + 10/3 \end{bmatrix} = \frac{1}{\sqrt2}\begin{bmatrix}6 \\ 6\end{bmatrix} = 6 v_1 ✓
\]
\[
C v_2 = \frac{1}{\sqrt2}\begin{bmatrix} 10/3 - 8/3 \\ 8/3 - 10/3 \end{bmatrix} = \frac{1}{\sqrt2}\begin{bmatrix}2/3 \\ -2/3\end{bmatrix} = \tfrac{2}{3} v_2 ✓
\]

**Orthogonality (C symmetric ⇒ eigenvectors can be chosen perpendicular):**
\[
v_1 \cdot v_2 = \frac{1}{2} - \frac{1}{2} = 0 ✓
\]

**S·v:** \(S v_1 = (18, 18) = 18 v_1\) ✓, \(S v_2 = (2, -2) = 2 v_2\) ✓.

## 8. Projection variance — verified three independent ways

**Way 1 — the formula uᵀCu (derived on screen):**

For u = v₁ = (1/√2)(1,1):
\[
u^{T} C u = \frac{1}{2}\left[\,(1,1)
\begin{bmatrix} 10/3 & 8/3 \\ 8/3 & 10/3 \end{bmatrix}
\binom{1}{1}\right]
= \frac{1}{2}\left( \tfrac{10}{3} + \tfrac{8}{3} + \tfrac{8}{3} + \tfrac{10}{3} \right)
= \frac{1}{2} \cdot \frac{36}{3} = 6 ✓
\]

For u = v₂ = (1/√2)(1,−1):
\[
u^{T} C u = \frac{1}{2}\left( \tfrac{10}{3} - \tfrac{8}{3} - \tfrac{8}{3} + \tfrac{10}{3} \right)
= \frac{1}{2} \cdot \frac{4}{3} = \tfrac{2}{3} ✓
\]

**Way 2 — directly from the projections (no matrix at all):**

Projected coordinates \(z_i = u \cdot x'_i\):

- u = v₁: z = (3/√2, −3/√2, 3/√2, −3/√2);  z̄ = 0;  \(\operatorname{Var} = \frac{(4.5)\cdot 4}{3} = 6\) ✓
- u = v₂: z = (1/√2, −1/√2, −1/√2, 1/√2); z̄ = 0;  \(\operatorname{Var} = \frac{(1/2)\cdot 4}{3} = \tfrac{2}{3}\) ✓
- u = (1,0): z = (2, −2, 1, −1); z̄ = 0; Var = (4+4+1+1)/3 = 10/3 ✓
- u = (0,1): z = (1, −1, 2, −2); z̄ = 0; Var = 10/3 ✓

**Way 3 — scatter version:** \(u^{T} S u = (n-1) \operatorname{Var}(z) = 18\) and \(2\) for v₁, v₂ ✓.

## 9. λ = Var uᵀCu for any unit eigenvector

\[
u^{T} C u = u^{T} (\lambda u) = \lambda (u^{T} u) = \lambda \cdot 1 = \lambda ✓
\]
(uses \(Cu = \lambda u\) and \(u^{T}u = 1\)).  Hence eigenvalues are non-negative here, since
\(u^{T}Cu = \frac{1}{n-1}\sum_i (u^{T}x'_i)^2 \ge 0\) — the PSD argument shown on screen.

## 10. Why the largest eigenvalue wins (the a–b argument)

Any unit u in span{v₁, v₂}: u = a v₁ + b v₂, a² + b² = 1. Since C vᵢ = λᵢ vᵢ and v₁ ⊥ v₂:
\[
C u = a \lambda_1 v_1 + b \lambda_2 v_2
\Rightarrow
u^{T} C u = \lambda_1 a^2 + \lambda_2 b^2 = 6a^2 + \tfrac{2}{3} b^2
= 6 - \tfrac{16}{3} b^2 \le 6
\]
Equality iff b = 0 ⇔ u = ±v₁ ✓. So the maximum of uᵀCu over the unit circle is exactly 6, at the
first principal component. Second place: λ₂ = 2/3 at v₂.

## 11. Explained variance ratios

\[
\frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{6}{6 + 2/3} = \frac{6}{20/3} = \frac{18}{20}
= \boxed{0.90 = 90\%}
\qquad
\frac{\lambda_2}{\lambda_1 + \lambda_2} = \frac{2/3}{20/3} = \boxed{0.10 = 10\%}
\]

These are this dataset only; no general 90% law is claimed (and the video says so explicitly).

## 12. Derivation chain — every identity used, verified

| Step | Identity | Why valid here |
|---|---|---|
| zᵢ = uᵀx′ᵢ | projection definition | dot product = signed shadow length |
| z̄ = 0 | Σx′ᵢ = 0 ⇒ Σzᵢ = uᵀΣx′ᵢ = 0 | centring (linearity) |
| Var(z) = Σzᵢ²/(n−1) | z̄ = 0 | definition of variance |
| zᵢ² = (uᵀx′ᵢ)(x′ᵢᵀu) | scalar equals its transpose | (uᵀx)ᵀ = xᵀu |
| zᵢ² = uᵀ(x′ᵢx′ᵢᵀ)u | associativity of matrix product | parentheses regroup freely |
| uᵀ(Σ…)u | u fixed ⇒ factor | constant with respect to the index i |
| Σx′ᵢx′ᵢᵀ = S; S/(n−1) = C | definitions | scatter vs covariance |
| ∇ₚ(uᵀCu) = 2ap + 2bq, etc. | direct expansion | a, b, d, p, q are scalars |
| ∇u(uᵀCu) = 2Cu | vectorise the two partials; needs C = Cᵀ | covariance matrices are symmetric |
| ∇u(uᵀu) = 2u | same computation with C = I | special case |
| ∇L = 0 at interior extremum | Fermat's theorem | constrained via Lagrangian |
| Cu = λu | divide by 2 | λ arbitrary scalar |

Sympy cross-checks (session):

```
charpoly(C, λ).factor()      -> (λ - 6)*(3*λ - 2)/3
eigenvects(C)                -> [(2/3, 1, [[-1],[1]]), (6, 1, [[1],[1]])]   (λ=2/3 vector ∝ (1,-1))
eigenvects(S)                -> [(2, 1, [[-1],[1]]), (18, 1, [[1],[1]])]
simplify(u1'*C*u1)           -> 6        simplify(u2'*C*u2) -> 2/3
explained ratios             -> 9/10, 1/10
```

## 13. Convention notes

- **Column vectors** are used for observations in all algebra; when the video lists data as `(5,3)` it is shorthand for `[5; 3]`.
- **Sample vs population**: sample (n−1) is used throughout; using n would scale S and C by the same factor — eigenvalues rescale, eigenvectors and all conclusions are unchanged. The video states this.
- **Scatter vs covariance vs "CV matrix"**: scatter = Σx′x′ᵀ; covariance = scatter/(n−1); "CV matrix" is treated as the same object as the covariance matrix. Directions identical; eigenvalues scaled.
- **Explained variance** is the Rayleigh-quotient value at each eigenvector; the 90/10 split is not universal.
- **PSD**: all eigenvalues ≥ 0 (shown via \(u^{T}Cu = \tfrac{1}{n-1}\sum (u^{T}x'_i)^2 \geq 0\)).

**Conclusion: every number, identity and implication in the video is verified. The four observations, the mean, the centring, S, C, the eigenvalues 6 and 2/3, the eigenvectors (1,1)/√2 and (1,−1)/√2, and the 90/10 split are all correct.**
