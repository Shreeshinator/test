# PCA — Voiceover Script (record this)

Total: ~1,480 words ≈ 11 min 40 s at 125–135 wpm with mathematical pauses.
Each scene below lists its screen slot, the exact lines to record, and the
maths on screen. Record one take per scene, leaving ~0.5 s of room tone at
both ends of each file.

---
## Scene 01 — The problem (0:00–0:45)

VO:
Let's start with a tiny dataset. Four observations, two features each — call them x and y.
There they are. Notice the cloud leans up and to the right: when x is large, y tends to be large too.
Here's the question we want to answer.
Can we find a direction along which these points vary as much as possible?
That single question is the whole engine of Principal Component Analysis.
Only four points — small enough to verify every step by hand.
And we're going to build the answer from scratch — no formulas until they're forced on us.

On screen: title card → axes, four cyan dots → the dashed amber hint along the long axis → the question.

## Scene 02 — Centring (0:45–1:45)

VO:
First, meet the data: five three, one one, four four, and two zero.
Average x: twelve over four — three. Average y: eight over four — two.
So the mean is the point three two — here in red.
Why does the average matter? Because we don't care where the cloud sits — we care how it spreads.
So we subtract the mean from every point. Watch the cloud slide:
two one, minus two minus one, one two, minus one minus two.
Its centre is now the origin. Same shape, same spread — just a better vantage point.
Notice the two pairs of opposite points — their deviations cancel out, which is exactly why the means are zero.
Every formula from here on works with deviations from the mean.

On screen: μx, μy, μ = (3,2) computed → red mean dot → cloud animates to the origin → centred list appears.

## Scene 03 — Variance (1:45–2:35)

VO:
So how spread out are the points? Start with one variable.
The variance of x: subtract the mean, square each deviation — signs vanish, and big gaps count more —
then add them up, and divide by n minus one for sample variance.
We'll use n minus one throughout; dividing by n instead rescales every variance equally — no direction changes.
Here, the squared deviations of x are four plus four plus one plus one — ten — so the variance is ten thirds.
Same for y. But variance only looks along one axis.
It cannot tell us that x and y rise together.

On screen: Var(x) formula → the four terms → Var(x) = Var(y) = 10/3 → the pivot line.

## Scene 04 — Covariance (2:35–3:35)

VO:
That rising-together relationship is what covariance measures.
Three regimes: positive — both rise together. Negative — one rises as the other falls. Near zero — no clear linear link.
For each point, multiply its two deviations.
All four products are positive: two, two, two, two.
Had they all come out negative, we'd read negative covariance — one rises, the other falls.
Here: positive — the features clearly move together.
The formula: one over n minus one, sum of the products of deviations.
Plug in: eight thirds — about two point six seven.
For the record: Var of x is ten thirds, Var of y is ten thirds, covariance is eight thirds.
These three numbers are the raw material of the matrix we build next.

On screen: shaded (+,+)/(−,−) quadrants → the three regimes → products 2,2,2,2 → Cov = 8/3.

## Scene 05 — The scatter matrix, built by hand (3:35–4:55)

VO:
Here's the move that surprises people.
Take one centred point as a column vector.
Multiply it by its own transpose — an outer product — and you get a two by two matrix:
x squared, x y, x y, y squared.
Not the dot product — that's a single number.
Do this for every point and add.
Two one gives four two, two one — and so does minus two minus one; the signs flip twice.
One two and minus one minus two give one two, two four.
Add entry by entry: ten; the cross entries, eight; bottom-right, ten.
That's the scatter matrix S.
Top-left: squared spread in x. Bottom-right: same for y. Off-diagonal: joint variation.
Divide by n minus one — three — and you get the covariance matrix C:
ten thirds, eight thirds; eight thirds, ten thirds.
Two facts matter. One: S and C carry identical directional information — scaling by a positive number never moves an eigenvector; eigenvalues just shrink.
Two: C is symmetric — both cross entries are eight thirds.

On screen: column vector → outer vs dot product → four outer products grid → entry-wise sums → S boxed → C = S/3 → the two facts.

## Scene 06 — Trying a direction (4:55–6:00)

VO:
Now the real question. Pick any direction — call it u.
Project every point onto u: the projection coordinate is z equals u transpose x prime.
Geometrically: how much of each point lies along u — the signed length of its shadow.
Unit length matters — double u, every z doubles, and the variance quadruples.
That's not a better direction, just a bigger vector. So we demand u transpose u equals one.
Try the x direction: projections two, minus two, one, minus one — variance ten thirds.
Try the y direction: the same.
Try the diagonal: the points land at plus or minus three over root two — wider spread, and the variance is six.
So — what makes one direction better than another?
The one whose projected points have the greatest variance.

On screen: u introduced → projection formula → three trial directions with 1-D axes → the cheating example → uᵀu = 1.

## Scene 07 — Deriving Var(z) = uᵀCu (6:00–7:20)

VO:
Now the key algebra — slowly.
Projected values: z sub i equals u transpose x sub i prime.
Their variance: one over n minus one, sum of z sub i minus z-bar, squared.
After centring, the z's average to zero — the sum of the x-prime vectors is the zero vector.
So variance is one over n minus one times the sum of z sub i squared.
Rewrite z sub i squared — a scalar times itself.
A scalar equals its own transpose — so the second factor becomes x prime transpose u.
Regroup — associativity: u transpose, x prime x prime transpose, u.
That middle piece is exactly the outer product from before.
Factor the fixed u's out of the sum: u transpose, one over n minus one times the sum of outer products, u.
That sum is the scatter matrix — so this is u transpose S u over n minus one — which is u transpose C u.
The scatter version differs only by the constant n minus one — same maximiser.

On screen: the nine-step derivation, each line with its reason on the right.

## Scene 08 — The optimisation problem (7:20–8:05)

VO:
So the problem is now precise.
Maximise u transpose C u — the variance along u — subject to u transpose u equals one.
U is the direction we choose.
C holds the spread and joint variation of the data.
u transpose C u is the variance we're buying.
The constraint blocks cheating by scaling.
How do you maximise with a constraint?
Fold it into the objective with a new unknown, lambda — the Lagrange multiplier.
L equals u transpose C u minus lambda times u transpose u minus one.
When the constraint holds, the second term is zero — so an ordinary maximum of L is exactly our constrained maximum.

On screen: the boxed max problem → the four annotations → the scaling cheat → the Lagrangian.

## Scene 09 — The gradient gives Cu = λu (8:05–9:20)

VO:
To find that maximum, differentiate.
First — what is the gradient of u transpose C u?
Don't trust matrix calculus blindly. Expand it in two dimensions.
C equals a b, b d; u equals p q.
Then u transpose C u is a p squared plus two b p q plus d q squared — an ordinary quadratic in p and q.
Differentiate: two a p plus two b q — and two b p plus two d q.
Vectorise that: two times a b, b d, times p q — exactly two C u.
The cross terms match only because C is symmetric — which every covariance matrix is.
The same trick on u transpose u gives two u.
So the gradient of L is two C u minus two lambda u.
At a maximum, the gradient vanishes: two C u equals two lambda u.
Divide by two.
C u equals lambda u.

On screen: the 2-D expansion → ∂/∂p, ∂/∂q → ∇(uᵀCu) = 2Cu → ∇(uᵀu) = 2u → L, ∇L = 0 → boxed Cu = λu.

## Scene 10 — What Cu = λu means (9:20–10:15)

VO:
That equation should ring a bell.
C times u equals lambda times u — a nonzero vector that C merely stretches, never rotates: an eigenvector.
Lambda is its eigenvalue.
Our candidates for the best direction are exactly the eigenvectors of C.
And watch the payoff:
for a unit eigenvector, u transpose C u equals u transpose lambda u — equals lambda times u transpose u — equals lambda.
The eigenvalue is the variance along its eigenvector.
Eigenvalues are non-negative — a sum of squares — so C is positive semidefinite.
And because C is symmetric, these eigenvectors can be chosen perpendicular — ours: a half minus a half, zero.
S is 3C — same eigenvectors, eigenvalues eighteen and two.

On screen: v₁ stretch demo + rotating non-example → definition → λ = Var chain → psd → orthogonality → S = 3C.

## Scene 11 — Solving for our data (10:15–10:55)

VO:
Now just compute.
Determinant of C minus lambda I: ten thirds minus lambda, squared, minus eight thirds squared — zero.
So lambda is six, or two thirds.
For six: v x equals v y — v one is one over root two, one one.
For two thirds: v x equals minus v y — one over root two, one minus one.
Why the largest? Any unit direction is a v-one plus b v-two — a squared plus b squared one.
Its variance: six a squared plus two thirds b squared — at most six.
The biggest eigenvalue wins.

On screen: det expansion → λ = 6, 2/3 → both eigenvector solves → PC1/PC2 on the scatter → the a²+b² argument.

## Scene 12 — What we accomplished (10:55–11:40)

VO:
Look what we did.
Data. Centre it. Scatter matrix. Covariance matrix. Project.
Derive u transpose C u. Maximise.
And eigenvectors fell out — keep the largest.
Here, PC one carries six over six plus two thirds — ninety percent of the total variance; PC two keeps ten.
Project onto PC one and you get a one-dimensional sketch that keeps ninety percent —
the rest is discarded on purpose. That's the trade PCA always makes.
Ninety percent is this dataset, not a law.
And notice how we got here.
Not by an eigenvector trick — eigenvectors are simply what the variance-maximising problem demands.
That's PCA.

On screen: chain recap → 90/10 bars → the 1-D projection claim → closing insight → end card.
