# Exam Aid Sheet — Lectures 9–15
CS 6515: Graduate Algorithms

**Core:** Model → solve or relax → certify optimality or bound approximation error.

Notation: \(\mathrm{OPT}\) = integral/exact optimum; \(\mathrm{LP}^*\) = relaxation optimum; \(x^*\) = optimal point.

## Lecture 9 — Linear Programming: Models & Geometry

### Canonical form and conversions

\[
\max c^\top x\quad\text{s.t. }Ax\le b,\;x\ge0.
\]

| Feature | Conversion |
|---|---|
| Minimize \(c^\top x\) | Maximize \(-c^\top x\); negate optimal value |
| \(a^\top x\ge d\) | \(-a^\top x\le-d\) |
| \(a^\top x=d\) | Two opposite inequalities |
| Unrestricted \(z\) | \(z=z^+-z^-\), \(z^+,z^-\ge0\) |
| Slack variables | \(Ax+s=b,\;x,s\ge0\) |

- LPs use real variables, linear objectives, and non-strict linear constraints—not products, quadratic objectives, or integer requirements.
- Feasible regions are convex: segments between feasible points stay feasible.
- Three outcomes: infeasible; unbounded objective; attained finite optimum.
- Vertex in \(\mathbb R^n\): \(n\) linearly independent tight constraint normals. Nonnegativity constraints count.
- Canonical LP + finite optimum ⇒ an optimal vertex exists. Optimum need not be unique.
- Rational LPs are solvable in polynomial time in total binary encoding length—not merely the number of variables/constraints. Enumerating vertices may be exponential.

Exam trap: unbounded feasible region \(\not\Rightarrow\) unbounded objective, e.g. \(\max -x\) subject to \(x\ge0\).

## Lecture 10 — Duality & Max-Flow/Min-Cut

### Primal–dual pair

\[
\begin{array}{ll}
(P):\max c^\top x & (D):\min b^\top y\\
Ax\le b,\;x\ge0 & A^\top y\ge c,\;y\ge0
\end{array}
\]

Weak duality:

\[
c^\top x\le y^\top Ax\le b^\top y.
\]

Feasible \(x,y\) with equal objective values certify both are optimal.

Strong duality: a feasible finite optimum on either side implies attained optima on both sides with equal values. Primal unbounded ⇒ dual infeasible; dual unbounded ⇒ primal infeasible. Both can be infeasible.

### Mixed-sign rulebook: maximization primal

| Primal feature | Dual feature |
|---|---|
| Constraint \(\le\), \(\ge\), \(=\) | Variable \(\ge0\), \(\le0\), unrestricted |
| Variable \(\ge0\), \(\le0\), unrestricted | Constraint \(\ge\), \(\le\), \(=\) |

Transpose \(A\); exchange objective coefficients and right-hand sides.

### Flow dual and exact rounding

Path-flow primal:

\[
\max\sum_p x_p,\qquad \sum_{p\ni e}x_p\le c_e,\quad x_p\ge0.
\]

Dual:

\[
\min\sum_e c_ey_e,\qquad \sum_{e\in p}y_e\ge1\quad\forall s\text{–}t\text{ paths},\quad y_e\ge0.
\]

Interpret \(y_e\) as edge lengths. Define

\[
\ell(v)=\min\{d_y(s,v),1\},\qquad S_r=\{v:\ell(v)\le r\}.
\]

For \(r\in(0,1)\), \(S_r\) is a cut, and

\[
\int_0^1c(\delta^+(S_r))\,dr
=\sum_{(u,v)}c_{uv}\max\{0,\ell(v)-\ell(u)\}
\le\sum_e c_ey_e.
\]

Some cut costs no more than the dual ⇒ max-flow = min-cut. Path formulations may be exponential; shortest paths check dual feasibility without listing all paths.

## Lecture 11 — Farkas’ Lemma & Strong-Duality Proof

### Farkas: exactly one system is feasible

\[
\boxed{M\lambda=p,\;\lambda\ge0}
\qquad\text{or}\qquad
\boxed{M^\top w\ge0,\;p^\top w<0}.
\]

The second system certifies infeasibility of the first. Separation proof: choose closest \(q\) in a closed convex set to \(p\); \(v=p-q\) gives

\[
v^\top p>v^\top q\ge v^\top z\quad\forall z\text{ in the set}.
\]

### Strong-duality proof skeleton

1. Include all inequalities, especially \(-x_i\le0\).
2. At optimum \(x^*\), \(c\) must be a nonnegative combination of tight normals.
3. Otherwise Farkas gives \(v\) with \(a_r^\top v\le0\) for tight rows and \(c^\top v>0\).
4. A sufficiently small step \(x^*+\varepsilon v\) remains feasible and improves the objective: contradiction.
5. Multipliers yield \(c=A^\top y-z\), \(y,z\ge0\), and \(c^\top x^*=b^\top y\).

Complementary-slackness consequences:

\[
y_j[b_j-(Ax)_j]=0,\qquad x_i[(A^\top y)_i-c_i]=0.
\]

Positive multiplier ⇒ tight constraint; tight constraint does not imply positive multiplier.

## Lectures 12–13 — Convexity & Gradient Descent

### Essential identities

\[
f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y).
\]

For differentiable convex \(f\):

\[
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle.
\]

Thus

\[
f(x)-f(x^*)\le\langle\nabla f(x),x-x^*\rangle.
\]

- Convex objective + convex feasible set ⇒ every local minimum is global.
- Unconstrained: \(\nabla f(x)=0\) certifies optimality. Constrained boundary optimum need not have zero gradient.
- Twice differentiable: convex iff \(\nabla^2f(x)\succeq0\).
- Least squares: \(f(x)=\frac12\|Ax-b\|^2\), \(\nabla f=A^\top(Ax-b)\), Hessian \(A^\top A\succeq0\).

### Updates and guarantees

Let \(\|x_0-x^*\|\le D\).

| Assumptions | Step size | Output | Error bound |
|---|---|---|---|
| Convex; \(\|\nabla f(x_t)\|\le G\) | \(D/(G\sqrt T)\) | Average \(\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t\), or best queried iterate | \(DG/\sqrt T\) |
| Convex, \(\beta\)-smooth; unconstrained | \(1/\beta\) | Last iterate \(x_T\) | \(\beta D^2/(2T)\) |

Basic update:

\[
x_{t+1}=x_t-\eta\nabla f(x_t).
\]

Proof engine, with \(R_t=\|x_t-x^*\|^2\):

\[
f(x_t)-f(x^*)\le\frac{R_t-R_{t+1}}{2\eta}+\frac{\eta G^2}{2}.
\]

Sum, telescope, then use convexity at the average. Required iterations: \(T\ge(DG/\varepsilon)^2\) for bounded gradients; \(T\ge\beta D^2/(2\varepsilon)\) for smooth convex GD.

### Projection and smoothness

Projected GD:

\[
x_{t+1}=\Pi_K(x_t-\eta\nabla f(x_t)).
\]

For nonempty closed convex \(K\), projection is unique and

\[
\|\Pi_K(u)-z\|^2\le\|u-z\|^2-\|u-\Pi_K(u)\|^2,\quad z\in K.
\]

Hence the bounded-gradient proof survives projection. Box projection = coordinate clipping.

Smoothness:

\[
\|\nabla f(y)-\nabla f(x)\|\le\beta\|y-x\|,
\]

\[
f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\frac\beta2\|y-x\|^2.
\]

With \(\eta=1/\beta\):

\[
f(x_{t+1})\le f(x_t)-\frac1{2\beta}\|\nabla f(x_t)\|^2.
\]

Smoothness bounds gradient changes, not gradient magnitude. Include gradient and projection costs in runtime.

## Lecture 14 — Approximation & Greedy Algorithms

### Definitions

For \(\alpha\ge1\): minimization requires \(\mathrm{ALG}\le\alpha\mathrm{OPT}\); maximization requires \(\mathrm{ALG}\ge\mathrm{OPT}/\alpha\). Solutions must be feasible.

PTAS: polynomial input-size runtime for each fixed \(\varepsilon\). FPTAS: polynomial in input size and \(1/\varepsilon\). These multiplicative guarantees differ from GD’s additive error.

### Vertex Cover

- Maximum remaining degree greedy: \((1+\ln m)\)-approximation.

  \[
  r_{t+1}\le r_t(1-1/\mathrm{OPT})
  \implies r_t\le me^{-t/\mathrm{OPT}}.
  \]

- Pick any uncovered edge and take both endpoints: 2-approximation. Selected edges form a maximal matching \(M\):

  \[
  |M|\le\mathrm{OPT},\qquad |C|=2|M|.
  \]

  Maximal ≠ maximum; maximal suffices.

### Directed edge-disjoint paths

Set \(L=\max\{1,\lfloor\sqrt m\rfloor\}\). Repeatedly route an available pair along a path of length \(\le L\); delete its edges and pair.

Crucial fallback: also find one arbitrary feasible path, if any; return the larger solution. Without it, short-path greedy may return zero.

Charging/counting:

\[
|\mathcal O_{\rm short}|\le(L+1)|A|,\qquad
|\mathcal O_{\rm long}|\le\frac m{L+1}.
\]

Returned count \(a\) satisfies

\[
\mathrm{OPT}\le\left(L+1+\frac m{L+1}\right)a
\le(2\sqrt m+1)a.
\]

Balance losses \(L\) and \(m/L\) ⇒ \(O(\sqrt m)\)-approximation.

## Lecture 15 — LP Relaxations & Deterministic Rounding

### Template and Vertex Cover

Minimization: formulate IP → relax → solve LP → round feasibly:

\[
\mathrm{cost(rounded)}\le\alpha\mathrm{LP}^*\le\alpha\mathrm{OPT}.
\]

Vertex Cover LP:

\[
\min\sum_vx_v,\qquad x_u+x_v\ge1\quad\forall\{u,v\}\in E,\quad0\le x_v\le1.
\]

Round \(C=\{v:x_v^*\ge1/2\}\). Every edge is covered and

\[
|C|\le2\sum_vx_v^*=2\mathrm{LP}^*\le2\mathrm{OPT}.
\]

Dual without redundant upper bounds:

\[
\max\sum_ey_e,\qquad\sum_{e\ni v}y_e\le1,\quad y_e\ge0.
\]

Integrality gap on \(K_n\): \((n-1)/(n/2)=2-2/n\to2\).

### Metric Facility Location

\[
\min\sum_if_ix_i+\sum_{i,j}d_{ij}y_{ij},
\qquad \sum_i y_{ij}=1,\quad y_{ij}\le x_i,\quad0\le x_i,y_{ij}\le1.
\]

Here \(x_i\) opens facility \(i\); \(y_{ij}\) assigns client \(j\). Distances satisfy the triangle inequality.

Rounding:

1. Compute \(L_j=\sum_i d_{ij}y_{ij}^*\), \(B_j=\{i:d_{ij}\le2L_j\}\).
2. Process clients in nondecreasing \(L_j\).
3. If \(B_j\) is disjoint from all representative balls, make \(j\) a representative and open its cheapest facility.
4. Otherwise assign \(j\) to the facility of an overlapping earlier representative.

Key structure: representative balls are pairwise disjoint; metric distances control reassignment. Lecture 15 announces a 6-approximation but defers its proof to the next lecture.

---

Source: Lecture_9_15_Merged.pdf (Lectures 9–15). Mathematical notation uses LaTeX inline delimiters `\( ... \)` and display delimiters `\[ ... \]`; rendering requires a Markdown viewer with math support.
