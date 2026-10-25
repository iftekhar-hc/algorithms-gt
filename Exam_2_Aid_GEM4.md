# CS 6515 / 4540: Concise Exam Aid Sheet (Lectures 9–15)

> **Scope:** Lectures 9–15 (Linear Programming, Duality, Farkas' Lemma, Convex Optimization, Gradient Descent, Greedy & LP-Rounding Approximation Algorithms) + HW 3–4 & Practice Exam 2.  
> **Format:** High-density, front-of-sheet exam reference with exact formulas, conversion tables, proof templates, and common exam traps.

---

## 0. Master Quick-Reference Table (Lectures 9–15)

| Lec | Topic / Algorithm | Core Formula / Rule | Guarantee / Complexity |
| :-: | :--- | :--- | :--- |
| **9** | **Canonical LP & Vertices** | $\max c^\top x \text{ s.t. } Ax \le b,\, x \ge 0$; vertex $v = A_B^{-1}b_B$ ($n$ indep. tight rows) | Bit-length $\text{poly}(L)$ (Cramer); Ellipsoid/Interior-Pt: $\text{poly}(L)$ time |
| **10** | **LP Duality** | Primal $\max\{c^\top x : Ax \le b, x \ge 0\} \iff$ Dual $\min\{b^\top y : A^\top y \ge c, y \ge 0\}$ | Weak: $c^\top x \le b^\top y$; Strong: $c^\top x^* = b^\top y^*$ (if finite opt) |
| **10** | **Max-Flow = Min-Cut (LP)** | Dual lengths $y_e^* \ge 0$; $\ell(v)=\min\{d_{y^*}(s,v),1\}$; cut $S_r = \{v:\ell(v)\le r\}$ | $\int_0^1 c(\delta^+(S_r))\,dr \le \sum_e c_e y_e^* \implies \exists r^*: c(\delta^+(S_{r^*})) = \text{Max-Flow}$ |
| **11** | **Farkas' Lemma (Cones)** | **Xor:** (I) $\exists \lambda \ge 0,\, M\lambda = p$ $\;\; \veebar \;\;$ (II) $\exists w,\, M^\top w \ge 0 \text{ and } p^\top w < 0$ | Proved via closest point $q = \arg\min_{z \in C}\|z-p\|_2^2$, $w = q - p$ |
| **12** | **Bounded-Gradient GD** | $x_{t+1} = x_t - \eta \nabla f(x_t)$, $\eta = \frac{D}{G\sqrt{T}}$, $\bar{x}_T = \frac{1}{T}\sum_{t=0}^{T-1} x_t$ | $f(\bar{x}_T) - f(x^*) \le \frac{DG}{\sqrt{T}} \implies T = O\!\left(\frac{D^2G^2}{\varepsilon^2}\right)$ |
| **13** | **Projected GD (PGD)** | $y_{t+1} = x_t - \eta \nabla f(x_t),\; x_{t+1} = \Pi_K(y_{t+1}) = \arg\min_{z\in K}\|z-y_{t+1}\|_2$ | Contraction $\|\Pi_K(u)-z\|_2 \le \|u-z\|_2 \implies T = O\!\left(\frac{D^2G^2}{\varepsilon^2}\right)$ |
| **13** | **$\beta$-Smooth Convex GD** | $\|\nabla f(y)-\nabla f(x)\|_2 \le \beta\|y-x\|_2$; step $\eta = \frac{1}{\beta}$ | Descent $\frac{1}{2\beta}\|\nabla f(x_t)\|_2^2 \le f(x_t)-f(x_{t+1})$; $f(x_T)-f(x^*) \le \frac{\beta D^2}{2T}$ ($O(\frac{\beta D^2}{\varepsilon})$) |
| **Ex2** | **$\alpha$-Strong Cvx + $\beta$-Smooth** | $f(y) \ge f(x) + \langle\nabla f(x),y-x\rangle + \frac{\alpha}{2}\|y-x\|_2^2$; step $\eta = \frac{1}{\beta}$ | $f(x_k)-f(x^*) \le \left(1-\frac{\alpha}{\beta}\right)^k(f(x_0)-f(x^*)) \implies T = O\!\left(\frac{\beta}{\alpha}\log\frac{1}{\varepsilon}\right)$ |
| **14** | **Vertex Cover (Greedy)** | **Greedy-Degree:** pick max-degree $v$ $\;\big|\;$ **Maximal Matching:** pick both $\{u,v\}$ | Greedy-Degree: $(1+\ln m)=O(\log n)$-approx $\;\big|\;$ Matching: $2$-approx |
| **14** | **Directed EDP (Greedy)** | Route shortest unrouted $s_i \to t_i$ path with $\le L = \lfloor\sqrt{m}\rfloor$ edges; delete edges | $(2\sqrt{m}+1) = O(\sqrt{m})$-approx (balances $\mathcal{O}_{\text{short}} \le L|A|$ vs. $\mathcal{O}_{\text{long}} < \frac{m}{L}$) |
| **15** | **Weighted VC / Hitting Set** | Solve LP $\min \sum_v w_v x_v$ s.t. $\sum_{v \in e} x_v \ge 1$; round $C = \{v : x_v^* \ge 1/b\}$ ($|e|\le b$) | $b$-approx ($b=2$ for Vertex Cover): $\text{cost}(C) \le b\,\text{OPT}_{\text{LP}} \le b\,\text{OPT}$ |
| **15** | **Metric Facility Location** | LP $\to$ $L_j = \sum_i d_{ij}y_{ij}^*$, ball $B_j = \{i: d_{ij}\le 2L_j\}$, greedy disjoint $B_r$ (sorted $L_j\uparrow$) | $6$-approx: $\text{Open} \le 2F^*$, $\text{Conn} \le 6D^* \implies \text{ALG} \le 6\,\text{OPT}_{\text{LP}} \le 6\,\text{OPT}$ |

---

## 1. Lecture 9: Linear Programming Formulations, Geometry & Solvability

### 1.1 Canonical Form & Standard LP Conversions
$$\text{Canonical Maximization LP:} \qquad \max_{x \in \mathbb{R}^n} \; c^\top x \quad \text{s.t.} \quad Ax \le b, \;\; x \ge 0$$

| Feature / Norm Objective | Linear Program Conversion |
| :--- | :--- |
| **Minimize $c^\top x$** | Maximize $(-c)^\top x$ (then negate optimal objective value) |
| **Constraint $a_i^\top x \ge b_i$** | Multiply by $-1$: $(-a_i)^\top x \le -b_i$ |
| **Equality $a_i^\top x = b_i$** | Replace by two inequalities: $a_i^\top x \le b_i$ **and** $(-a_i)^\top x \le -b_i$ |
| **Unrestricted $x_j \in \mathbb{R}$** | Substitute $x_j = x_j^+ - x_j^-$ with $x_j^+ \ge 0,\; x_j^- \ge 0$ |
| **Minimize $L_\infty$ distance $\|p - q\|_\infty = \max_i |p_i - q_i|$** | Introduce scalar $t \ge 0$: $\min t$ s.t. $-t \le p_i - q_i \le t \;\;\forall i$ (i.e., $p_i - t \le q_i$ and $-p_i - t \le -q_i$) |
| **Minimize $L_1$ distance $\|p - q\|_1 = \sum_{i=1}^d |p_i - q_i|$** | Introduce $t_i \ge 0$: $\min \sum_{i=1}^d t_i$ s.t. $-t_i \le p_i - q_i \le t_i \;\;\forall i$ *(Note: $\|p-q\|_2$ is quadratic $\to$ **not** an LP!)* |
| **Maximize $\min_i (a_i^\top x - b_i)$ / Minimize $\max_i (a_i^\top x - b_i)$** | $\max t \text{ s.t. } t \le a_i^\top x - b_i \;\forall i$ $\;\big/\;$ $\min t \text{ s.t. } t \ge a_i^\top x - b_i \;\forall i$ |


### 1.2 Polyhedral Geometry, Vertices & Polynomial Solvability
- **Polyhedron vs. Convex Set:** Every half-space $\{x : a_i^\top x \le b_i\}$ is convex, so any finite intersection $P = \{x : Ax \le b, x \ge 0\}$ is a **convex polyhedron**.
  - *Exam Trap:* **Not every convex set is a polyhedron!** Example: the Euclidean unit disk $\{x \in \mathbb{R}^2 : x_1^2 + x_2^2 \le 1\}$ has curved boundary and requires infinitely many half-spaces.
- **3 Possible LP Outcomes:** (1) **Infeasible** ($P = \emptyset$), (2) **Unbounded** ($c^\top x \to +\infty$ along a ray in $P$), or (3) **Finite Optimum Achieved**.
- **Tight Constraints & Vertices (Basic Feasible Solutions):** In $\mathbb{R}^n$, a feasible point $v \in P$ is a **vertex** iff it is the unique intersection of **$n$ linearly independent tight constraints** ($A_B v = b_B$ with $A_B \in \mathbb{R}^{n \times n}$ invertible $\implies v = A_B^{-1}b_B$).
- **Fundamental Theorem of LP:** If a canonical LP ($x \ge 0$) is feasible and bounded, the optimum is attained at **at least one vertex**. *(Without $x \ge 0$, an unbounded slab like $0 \le x_1 \le 1$ in $\mathbb{R}^2$ has no vertices.)*
- **Cramer's Rule & Polynomial Bit-Length:** For any integer $n \times n$ invertible submatrix $B = A_B$, vertex coordinates are $x_i = \frac{\det(B_i)}{\det(B)}$, which require only $\text{poly}(L)$ bits (where $L$ is the binary input bit-length). However, there are up to $\binom{m+n}{n}$ vertices (exponential in $n$), so brute-force vertex enumeration is exponential.
- **LP Algorithms:**
  - **Simplex (Dantzig):** Walks along edges from vertex to adjacent vertex improving $c^\top x$; fast in practice, **exponential worst-case** (Klee-Minty cube).
  - **Ellipsoid (Khachiyan) & Interior-Point (Karmarkar):** Run in **polynomial time $\text{poly}(n, m, L)$** in the binary encoding length $L$.

---

## 2. Lecture 10: LP Duality, Shadow Prices & Threshold Cut Rounding

### 2.1 Primal–Dual Construction Recipe
$$\text{Primal }(P): \;\; \max_{x \in \mathbb{R}^n} \; c^\top x \quad \text{s.t.} \quad Ax \le b,\;\; x \ge 0 \qquad \Longleftrightarrow \qquad \text{Dual }(D): \;\; \min_{y \in \mathbb{R}^m} \; b^\top y \quad \text{s.t.} \quad A^\top y \ge c,\;\; y \ge 0$$

| Primal (Maximization, $m$ constraints, $n$ vars) | Dual (Minimization, $n$ constraints, $m$ vars) |
| :--- | :--- |
| Objective vector $c$, RHS vector $b$, constraint matrix $A$ | Objective vector $b$, RHS vector $c$, constraint matrix $A^\top$ |
| $i$-th constraint is $a_i^\top x \le b_i$ | $i$-th dual variable satisfies $y_i \ge 0$ |
| $i$-th constraint is $a_i^\top x = b_i$ | $i$-th dual variable $y_i \in \mathbb{R}$ is **unrestricted** |
| $i$-th constraint is $a_i^\top x \ge b_i$ | $i$-th dual variable satisfies $y_i \le 0$ |
| $j$-th primal variable satisfies $x_j \ge 0$ | $j$-th dual constraint is $(A^\top y)_j \ge c_j$ |
| $j$-th primal variable $x_j \in \mathbb{R}$ is **unrestricted** | $j$-th dual constraint is $(A^\top y)_j = c_j$ |

### 2.2 Duality Theorems, Complementary Slackness & Outcome Matrix
- **Weak Duality:** For any primal-feasible $x$ and dual-feasible $y$,
  $$c^\top x \le (A^\top y)^\top x = y^\top(Ax) \le y^\top b = b^\top y.$$
  - *Consequences:* Any dual-feasible $y$ certifies an upper bound on $\text{OPT}(P)$. If $c^\top x = b^\top y$, both $x$ and $y$ are optimal! If $P$ is unbounded ($+\infty$), $D$ is **infeasible**; if $D$ is unbounded ($-\infty$), $P$ is **infeasible**.
- **Strong Duality:** If $P$ has a finite optimum $x^*$, then $D$ has a finite optimum $y^*$, and **$c^\top x^* = b^\top y^*$**.
- **Complementary Slackness:** Feasible $(x^*, y^*)$ are both optimal $\iff$ $c^\top x^* = b^\top y^*$ $\iff$:
  1. $y_i^*(b_i - a_i^\top x^*) = 0 \;\;\forall i$ *(if dual var $y_i^* > 0$, primal constraint $i$ must be tight)*, and
  2. $x_j^*((A^\top y^*)_j - c_j) = 0 \;\;\forall j$ *(if primal var $x_j^* > 0$, dual constraint $j$ must be tight)*.
- **Shadow Price Interpretation:** $y_i^*$ is the marginal change in $\text{OPT}(P)$ per unit increase in resource $b_i$.

| Primal \ Dual | **Finite Optimum** | **Infeasible** | **Unbounded** |
| :--- | :---: | :---: | :---: |
| **Finite Optimum** | **Possible** ($c^\top x^* = b^\top y^*$) | Impossible | Impossible |
| **Infeasible** | Impossible | **Possible** *(both infeasible!)* | **Possible** |
| **Unbounded** | Impossible | **Possible** | Impossible |


### 2.3 Classic Graph LP Dual Pairs
1. **Maximum Matching LP $\leftrightarrow$ Minimum Fractional Vertex Cover LP:**
   - **Primal (Max Fractional Matching):** $\max \sum_{e \in E} x_e$ s.t. $\sum_{e \in \delta(v)} x_e \le 1 \;\;(\forall v \in V),\; x_e \ge 0$.
   - **Dual (Min Fractional Vertex Cover):** Introduce $y_v \ge 0$ for each vertex $v \in V$. Since each edge $e = (u, v)$ appears in $\delta(u)$ and $\delta(v)$:
     $$\min \sum_{v \in V} y_v \quad \text{s.t.} \quad y_u + y_v \ge 1 \;\;\forall e = (u,v) \in E, \qquad y_v \ge 0 \;\;\forall v \in V.$$
   - **Integrality Gap on Odd Cycles ($K_3$):** On triangle $K_3$, max integral matching is $1$, but $x_e = 1/2$ on all 3 edges is LP-feasible with value $1.5$ (and dual $y_v = 1/2$ gives $1.5$, vs. min integral vertex cover $2$). On **bipartite graphs**, $\text{OPT}_{\text{LP}} = \text{OPT}_{\text{ILP}}$ always!
2. **Path-Based Max-Flow LP $\leftrightarrow$ Fractional Edge-Length Min-Cut Dual:**
   - **Primal ($P_{\text{path}}$):** $\max \sum_{P \in \mathcal{P}} x_P$ s.t. $\sum_{P : e \in P} x_P \le c_e \;\;(\forall e \in E),\; x_P \ge 0$.
   - **Dual ($D_{\text{length}}$):** $\min \sum_{e \in E} c_e y_e$ s.t. $\sum_{e \in P} y_e \ge 1 \;\;(\forall P \in \mathcal{P}),\; y_e \ge 0$ *(every $s \to t$ path has $y$-length $\ge 1$)*.

### 2.4 Proof of Max-Flow = Min-Cut via Threshold Cut Rounding (Strong Duality)
Let $y^* \ge 0$ be an optimal fractional solution to $D_{\text{length}}$. Define $d(v) = \text{dist}_{y^*}(s, v)$ and clip $\ell(v) = \min\{d(v), 1\}$. Then $\ell(s) = 0$ and $\ell(t) = 1$. For threshold $r \in (0, 1)$, define the $s$-$t$ cut $S_r = \{v \in V : \ell(v) \le r\}$.
1. **Shortest-Path Triangle Inequality:** For every edge $e = (u, v)$, $d(v) \le d(u) + y_{uv}^* \implies \ell(v) - \ell(u) \le y_{uv}^*$.
2. **Average Cut Capacity Integral:** Edge $e=(u,v) \in \delta^+(S_r) \iff \ell(u) \le r < \ell(v)$, an interval of length $\max\{0, \ell(v)-\ell(u)\} \le y_{uv}^*$:
   $$\int_0^1 c(\delta^+(S_r))\,dr = \sum_{e=(u,v)\in E} c_e \int_0^1 \mathbf{1}[\ell(u) \le r < \ell(v)]\,dr = \sum_{e=(u,v)\in E} c_e \max\{0, \ell(v)-\ell(u)\} \le \sum_{e \in E} c_e y_e^* = \text{OPT}(D).$$
3. **Existence of Integral Min-Cut:** By averaging, $\exists r^* \in (0, 1)$ with $c(\delta^+(S_{r^*})) \le \text{OPT}(D) = \text{OPT}(P) = \text{Max-Flow} \le \text{Min-Cut}$. $\blacksquare$

---

## 3. Lecture 11: Farkas' Lemma, Convex Separation & Proof of Strong Duality

### 3.1 Farkas' Lemma (Theorem of the Alternatives — All 3 Exam Forms)
| Form | System (I): Feasibility | System (II): Infeasibility Certificate ($y$ or $w$) |
| :--- | :--- | :--- |
| **Cone Form (Lec 11)** | $\exists \lambda \ge 0 \text{ s.t. } M\lambda = p$ ($p \in \text{cone}(a_1,\dots,a_t)$) | $\exists w \in \mathbb{R}^n \text{ s.t. } M^\top w \ge 0 \text{ and } p^\top w < 0$ |
| **Standard Form (Ex 2 / HW 3)** | $\exists x \ge 0 \text{ s.t. } Ax = b$ | $\exists y \in \mathbb{R}^m \text{ s.t. } A^\top y \ge 0 \text{ and } b^\top y < 0$ *(or $A^\top y \le 0, b^\top y > 0$)* |
| **Inequality Form** | $\exists x \in \mathbb{R}^n \text{ s.t. } Ax \le b$ | $\exists y \ge 0 \text{ s.t. } A^\top y = 0 \text{ and } b^\top y < 0$ |

- **How to Solve Exam Infeasibility Questions ($Ax = b, x \ge 0$):** Find vector $y$ such that $A^\top y \ge 0$ and $b^\top y < 0$.
  - *Practice Exam 2 Q1.3 Example:* $A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}, b = \begin{pmatrix} -1 \\ -1 \end{pmatrix}$. Pick $y = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. Then $A^\top y = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \ge 0$ and $b^\top y = -2 < 0 \implies$ Infeasible!

### 3.2 Geometric Proof of Farkas' Lemma (Closest-Point Separation)
1. **Not Both:** If $\lambda \ge 0, M\lambda = p$ and $M^\top w \ge 0, p^\top w < 0$, then $0 > p^\top w = \lambda^\top (M^\top w) \ge 0$, contradiction.
2. **If $p \notin C = \{M\lambda : \lambda \ge 0\}$:** Since $C$ is a closed convex cone, let $q = \arg\min_{z \in C} \|z - p\|_2^2$ be the unique closest point in $C$ to $p$, and set $v = p - q \neq 0$.
   - For any $z \in C$ and $t \in (0, 1]$, $(1-t)q + tz \in C \implies \|q - p + t(z-q)\|_2^2 \ge \|q-p\|_2^2 \implies v^\top(z - q) \le 0$.
   - Since $C$ is a cone, $\alpha q \in C$ for $\alpha = 0$ and $\alpha = 2 \implies (\alpha - 1)v^\top q \le 0 \implies v^\top q = 0$, so $v^\top z \le 0 \;\;\forall z \in C$.
   - Then $v^\top p = v^\top(q + v) = \|v\|_2^2 > 0$. Setting $w = -v = q - p$ gives $M^\top w \ge 0$ and $p^\top w = -\|p-q\|_2^2 < 0$. $\blacksquare$

### 3.3 Active-Constraint Proof of Strong LP Duality
Stack $Ax \le b$ and $-I_n x \le 0$ as $\bar{A}x \le \bar{b}$. Let $x^*$ be primal optimal and $I = \{r : \bar{a}_r^\top x^* = \bar{b}_r\}$ be the **tight constraints** at $x^*$.
1. **$c \in \text{cone}(\{\bar{a}_r\}_{r \in I})$:** If not, by Farkas' Lemma $\exists v = -w$ with $\bar{a}_r^\top v \le 0 \;\;(\forall r \in I)$ and $c^\top v > 0$. For small $\varepsilon > 0$, $x^* + \varepsilon v$ stays feasible for all tight constraints (since $\bar{a}_r^\top v \le 0$) and all non-tight constraints (strict slack), while $c^\top(x^* + \varepsilon v) > c^\top x^*$, contradicting optimality of $x^*$!
2. **Dual Optimality:** Thus $c = \sum_{i=1}^m y_i a_i + \sum_{j=1}^n \mu_j (-e_j) = A^\top y - \mu$ with $y \ge 0, \mu \ge 0$ supported only on tight constraints ($y_i(b_i - a_i^\top x^*) = 0$ and $\mu_j x_j^* = 0$). Then $A^\top y = c + \mu \ge c$ (dual feasible) and $c^\top x^* = (A^\top y - \mu)^\top x^* = y^\top(Ax^*) - \mu^\top x^* = b^\top y$. $\blacksquare$


---

## 4. Lectures 12 & 13: Convex Optimization & Gradient Descent

### 4.1 Convex Sets, Convex Functions & the "Quadratic Sandwich"
- **Convex Set $K \subseteq \mathbb{R}^d$:** $\forall x, y \in K,\; \lambda \in [0, 1] \implies (1-\lambda)x + \lambda y \in K$.
- **Chord Inequality (Definition of Convex $f$):** $f((1-\lambda)x + \lambda y) \le (1-\lambda)f(x) + \lambda f(y)$ for all $\lambda \in [0, 1]$.
- **Operations Preserving Convexity (HW 3):**
  - Non-negative scaling $a f(x)$ ($a \ge 0$), sum $f(x) + g(x)$, pointwise maximum $\max\{f(x), g(x)\}$, affine composition $f(Ax + b)$ are **always convex**.
  - *Counterexample:* Product $f(x)g(x)$ is **NOT** necessarily convex (e.g., $f(x)=x,\, g(x)=-x \implies f(x)g(x)=-x^2$ is concave!).
- **Every Local Minimum of a Convex Function is a Global Minimum:** And on an unconstrained domain, $x^*$ is a global minimum of differentiable convex $f \iff \nabla f(x^*) = 0$.

| Property | First-Order Inequality ($\forall x, y$) | Second-Order Condition ($C^2$) | Geometric Meaning / Key Consequence |
| :--- | :--- | :--- | :--- |
| **Convex** | $f(y) \ge f(x) + \langle\nabla f(x), y - x\rangle$ | $\nabla^2 f(x) \succeq 0$ | Tangent is global lower bound $\implies f(x)-f(x^*) \le \langle\nabla f(x), x-x^*\rangle$ |
| **$\alpha$-Strongly Convex** ($\alpha>0$) | $f(y) \ge f(x) + \langle\nabla f(x), y - x\rangle + \frac{\alpha}{2}\|y-x\|_2^2$ | $\nabla^2 f(x) \succeq \alpha I$ | Sits above upward parabola; implies $\|\nabla f(x)\|_2^2 \ge 2\alpha(f(x)-f(x^*))$ |
| **$\beta$-Smooth** ($\beta>0$) | $f(y) \le f(x) + \langle\nabla f(x), y - x\rangle + \frac{\beta}{2}\|y-x\|_2^2$ | $-\beta I \preceq \nabla^2 f(x) \preceq \beta I$ *(or $0 \preceq \nabla^2 f \preceq \beta I$ if convex)* | Equivalently $\|\nabla f(y)-\nabla f(x)\|_2 \le \beta\|y-x\|_2$ *(does **not** require convexity!)* |

- **Standard Matrix Calculus Example (Ridge / Least-Squares):** For $f(x) = \frac{1}{2}\|Ax - b\|_2^2 + \frac{\mu}{2}\|x\|_2^2$ ($\mu \ge 0$):
  $$\nabla f(x) = A^\top(Ax - b) + \mu x, \qquad \nabla^2 f(x) = A^\top A + \mu I \implies \alpha = \lambda_{\min}(A^\top A) + \mu, \quad \beta = \lambda_{\max}(A^\top A) + \mu.$$

### 4.2 Master Comparison of All 5 Gradient Descent Regimes
Update rule: $x_{t+1} = x_t - \eta \nabla f(x_t)$ (or $x_{t+1} = \Pi_K(x_t - \eta \nabla f(x_t))$ for constrained $x \in K$), where $\|x_0 - x^*\|_2 \le D$.

| Regime & Assumptions | Step Size $\eta$ | Output | Convergence Bound | Iteration Complexity for $\varepsilon$ |
| :--- | :---: | :---: | :--- | :---: |
| **1. Bounded-Gradient Convex** ($\|\nabla f(x)\|_2 \le G$) | $\eta = \frac{D}{G\sqrt{T}}$ | $\bar{x}_T = \frac{1}{T}\sum_{t=0}^{T-1} x_t$ | $f(\bar{x}_T) - f(x^*) \le \frac{DG}{\sqrt{T}}$ | $T = O\!\left(\frac{D^2 G^2}{\varepsilon^2}\right)$ |
| **2. Projected GD on Convex $K$** ($\|\nabla f(x)\|_2 \le G$) | $\eta = \frac{D}{G\sqrt{T}}$ | $\bar{x}_T = \frac{1}{T}\sum_{t=0}^{T-1} x_t$ | $f(\bar{x}_T) - f(x^*) \le \frac{DG}{\sqrt{T}}$ | $T = O\!\left(\frac{D^2 G^2}{\varepsilon^2}\right)$ |
| **3. $\beta$-Smooth Convex** ($\nabla^2 f(x) \preceq \beta I$) | $\eta = \frac{1}{\beta}$ | Last iterate $x_T$ | $f(x_T) - f(x^*) \le \frac{\beta D^2}{2T}$ | $T = O\!\left(\frac{\beta D^2}{\varepsilon}\right)$ |
| **4a. $\alpha$-Strongly Convex + $\beta$-Smooth** (Exam 2 Q4) | $\eta = \frac{1}{\beta}$ | Last iterate $x_T$ | $f(x_T)-f(x^*) \le \left(1-\frac{\alpha}{\beta}\right)^T (f(x_0)-f(x^*))$ | $T = O\!\left(\frac{\beta}{\alpha}\log\frac{f(x_0)-f(x^*)}{\varepsilon}\right)$ |
| **4b. $\alpha$-Strongly Convex + $G$-Lipschitz** (HW 3 Q15) | $\eta_t = \frac{1}{\alpha(t+1)}$ | $\bar{x}_T = \frac{1}{T}\sum_{t=1}^T x_t$ | $f(\bar{x}_T) - f(x^*) \le \frac{G^2(1+\ln T)}{2\alpha T}$ | $T = \tilde{O}\!\left(\frac{G^2}{\alpha\varepsilon}\right)$ |
| **5. $\beta$-Smooth Non-Convex** (HW 4 Q16, $f(x) \ge f^*$) | $\eta \le \frac{1}{\beta}$ | Best $\arg\min_{0\le k \le T} \|\nabla f(x_k)\|_2$ | $\min_{0\le k\le T}\|\nabla f(x_k)\|_2 \le \sqrt{\frac{2(f(x_0)-f^*)}{\eta(T+1)}}$ | $T = O\!\left(\frac{\beta(f(x_0)-f^*)}{\varepsilon^2}\right)$ *(for $\|\nabla f\| \le \varepsilon$)* |


### 4.3 Essential Gradient Descent Proof Templates (Memorize for Written Proofs!)

1. **Fundamental Distance Expansion + Telescoping (Lec 12 — Bounded Gradient):**
   - Expand $R_{t+1} = \|x_{t+1} - x^*\|_2^2 = \|x_t - \eta \nabla f(x_t) - x^*\|_2^2 = R_t - 2\eta\langle\nabla f(x_t), x_t - x^*\rangle + \eta^2\|\nabla f(x_t)\|_2^2$.
   - Rearrange & apply convexity $f(x_t) - f(x^*) \le \langle\nabla f(x_t), x_t - x^*\rangle$ and $\|\nabla f(x_t)\|_2 \le G$:
     $$f(x_t) - f(x^*) \le \frac{R_t - R_{t+1}}{2\eta} + \frac{\eta}{2}\|\nabla f(x_t)\|_2^2 \le \frac{R_t - R_{t+1}}{2\eta} + \frac{\eta G^2}{2}.$$
   - Average over $t = 0,\dots,T-1$ (telescoping $R_0 - R_T \le D^2$) and apply Jensen's inequality $f(\bar{x}_T) \le \frac{1}{T}\sum_{t=0}^{T-1} f(x_t)$:
     $$f(\bar{x}_T) - f(x^*) \le \frac{D^2}{2\eta T} + \frac{\eta G^2}{2} \xrightarrow{\eta = \frac{D}{G\sqrt{T}}} \frac{DG}{\sqrt{T}}. \quad \blacksquare$$

2. **Projection Contraction Inequality (Lec 13 — PGD):**
   - For $p = \Pi_K(u) = \arg\min_{w \in K} \frac{1}{2}\|w - u\|_2^2$ and any $z \in K$, first-order optimality on $K$ gives $\langle p - u, z - p \rangle \ge 0 \iff \langle u - p, z - p \rangle \le 0$.
   - Expand $\|u - z\|_2^2 = \|(u - p) + (p - z)\|_2^2 = \|u - p\|_2^2 + \|p - z\|_2^2 - 2\langle u - p, z - p \rangle \ge \|u - p\|_2^2 + \|p - z\|_2^2 \implies \|x_{t+1} - x^*\|_2^2 \le \|y_{t+1} - x^*\|_2^2$.
   - *Box Projection Formula:* On $K = \prod_{i=1}^d [a_i, b_i]$, $(\Pi_K(u))_i = \min\{b_i, \max\{a_i, u_i\}\}$.

3. **Sufficient Decrease Lemma under $\beta$-Smoothness (Lec 13 / Exam 2 Q4.1 / HW 4 Q16.1):**
   - Plug $y = x_{k+1} = x_k - \eta \nabla f(x_k)$ (so $y - x_k = -\eta \nabla f(x_k)$) into the $\beta$-smooth quadratic upper bound:
     $$f(x_{k+1}) \le f(x_k) + \langle\nabla f(x_k), -\eta\nabla f(x_k)\rangle + \frac{\beta}{2}\|-\eta\nabla f(x_k)\|_2^2 = f(x_k) - \eta\left(1 - \frac{\beta\eta}{2}\right)\|\nabla f(x_k)\|_2^2.$$
   - For **$\eta = \frac{1}{\beta}$** (or any $\eta \le \frac{1}{\beta}$ where $\eta(1-\frac{\beta\eta}{2}) \ge \frac{\eta}{2}$):
     $$f(x_{k+1}) \le f(x_k) - \frac{1}{2\beta}\|\nabla f(x_k)\|_2^2 \iff \frac{1}{2\beta}\|\nabla f(x_k)\|_2^2 \le f(x_k) - f(x_{k+1}). \quad \blacksquare$$

4. **Exponential Convergence under $\alpha$-Strong Convexity + $\beta$-Smoothness (Exam 2 Q4.2–4.3):**
   - Given $\|\nabla f(x_k)\|_2^2 \ge 2\alpha(f(x_k) - f(x^*))$ and $f(x_{k+1}) \le f(x_k) - \frac{1}{2\beta}\|\nabla f(x_k)\|_2^2$, subtract $f(x^*)$ from both sides:
     $$f(x_{k+1}) - f(x^*) \le f(x_k) - f(x^*) - \frac{1}{2\beta}\big(2\alpha(f(x_k) - f(x^*))\big) = \left(1 - \frac{\alpha}{\beta}\right)\big(f(x_k) - f(x^*)\big).$$
   - Unrolling by induction from $k$ to $0$: $f(x_k) - f(x^*) \le \left(1 - \frac{\alpha}{\beta}\right)^k (f(x_0) - f(x^*)) \le e^{-(\alpha/\beta)k}(f(x_0) - f(x^*))$. $\blacksquare$

---

## 5. Lectures 14 & 15: Approximation Algorithms (Greedy & LP Rounding)

### 5.1 Approximation Ratio Convention ($\alpha \ge 1$ Always!)
- **Minimization Problem:** $\text{OPT} \le \text{ALG} \le \alpha \cdot \text{OPT}$. *(To prove: lower-bound $\text{OPT} \ge \text{LB}$, then show $\text{ALG} \le \alpha \cdot \text{LB}$.)*
- **Maximization Problem:** $\frac{1}{\alpha}\text{OPT} \le \text{ALG} \le \text{OPT}$ $\iff$ $\text{OPT} \le \alpha \cdot \text{ALG}$. *(Exam 2 Q1.6 Trap: If $\alpha = 2$ on a maximization problem with $\text{OPT} = 5$, then $\text{ALG} \in [2.5, 5]$, so **only $2.5$ and $5$** are possible—never $7$ or $10$!)*

### 5.2 Master Summary of All Course Approximation Algorithms

| Problem | Algorithm | Approx Ratio | Key Certificate / Lower Bound Used in Proof |
| :--- | :--- | :---: | :--- |
| **Unweighted Vertex Cover** (Lec 14) | **Greedy-Degree** (pick max-degree $v$ in residual $G_t$) | $1 + \ln m = O(\log n)$ | $\exists u \in C^*: \deg_{G_{t-1}}(u) \ge \frac{r_{t-1}}{k} \implies r_t \le \left(1-\frac{1}{k}\right)^t m$ |
| **Unweighted Vertex Cover** (Lec 14) | **Maximal Matching** (pick uncovered $e=\{u,v\}$, add **both** $u,v$) | **$2$** | Disjoint edges $M$: $\text{OPT} \ge |M|$ and $|C| = 2|M| \le 2\,\text{OPT}$ |
| **Weighted Vertex Cover** (Lec 15) | **LP Threshold Rounding:** $C = \{v \in V : x_v^* \ge 1/2\}$ | **$2$** | $x_u^* + x_v^* \ge 1 \implies \max\{x_u^*, x_v^*\} \ge 1/2$; $\text{cost}(C) \le 2\,\text{OPT}_{\text{LP}}$ |
| **Weighted Hitting Set / Set Cover** (HW 4 Q18) | **LP Threshold Rounding:** $H = \{i : x_i^* \ge 1/b\}$ (where $|S_j| \le b$) | **$b$** | $\sum_{i \in S_j} x_i^* \ge 1 \implies \max_{i \in S_j} x_i^* \ge 1/b$; $\text{cost}(H) \le b\,\text{OPT}_{\text{LP}}$ |
| **Directed Edge-Disjoint Paths (EDP)** (Lec 14) | **Short-Path Greedy:** route shortest path of length $\le L = \lfloor\sqrt{m}\rfloor$ | $2\sqrt{m}+1 = O(\sqrt{m})$ | Partition $\mathcal{O}\setminus A$: $|\mathcal{O}_{\text{short}}| \le L|A|$ and $|\mathcal{O}_{\text{long}}| < \frac{m}{L}$ |
| **Metric Steiner Tree** (Exam 2 Q3) | **MST on Terminal Subgraph $G_T$** | **$2$** | Double $F^*$ (Euler/DFS walk $2w(F^*)$) + shortcut via Triangle Ineq |
| **Greedy Load Balancing** (HW 4 Q17) | **Unsorted List Scheduling** vs. **LPT Sorted ($w_1 \ge \dots \ge w_n$)** | **$2$** (unsorted) / **$1.5$** (sorted) | $\text{OPT} \ge \frac{1}{m}\sum_i w_i$ and $\text{OPT} \ge w_j$ (plus $w_{m+1} \le \frac{1}{2}\text{OPT}$ if sorted) |
| **Metric Facility Location** (Lec 15) | **LP Ball-Clustering Rounding** ($B_j = \{i: d_{ij} \le 2L_j\}$, sort $L_j \uparrow$) | **$6$** | Markov $\sum_{i\in B_j}x_i^* \ge 1/2 \implies \text{Open} \le 2F^*$; Triangle Ineq $\implies \text{Conn} \le 6D^*$ |

### 5.3 Step-by-Step Approximation Proof Skeletons (Memorize for Exam!)

1. **Greedy-Degree Vertex Cover ($O(\log n)$-Approx) vs. Maximal Matching ($2$-Approx) (Lec 14):**
   - **Greedy-Degree:** Let $k = \text{OPT} = |C^*|$ and $r_t = |E_t|$ be uncovered edges after $t$ steps. Since $C^*$ covers $E_{t-1}$, $\sum_{u \in C^*} \deg_{G_{t-1}}(u) \ge r_{t-1} \implies \max_{u \in C^*} \deg_{G_{t-1}}(u) \ge r_{t-1}/k$. Picking max-degree $v_t$ gives $r_t \le (1 - 1/k)r_{t-1} \le (1 - 1/k)^t m \le e^{-t/k}m < 1$ after $t = \lceil k \ln m \rceil$ steps $\implies |C| \le \text{OPT}(1 + \ln m)$.
   - **Maximal Matching:** Pick uncovered edges $M$ greedily (adding **both** endpoints to $C$, deleting incident edges). Since edges in $M$ are vertex-disjoint, any cover $C^*$ needs $\ge 1$ vertex per edge of $M$: $|C| = 2|M| \le 2|C^*| = 2\,\text{OPT}$.

2. **Directed Edge-Disjoint Paths (EDP) via Short-Path Greedy ($O(\sqrt{m})$-Approx — Lec 14):**
   - **Rule:** Repeatedly route the shortest unrouted $s_i \to t_i$ path $P_i$ having **$\le L = \lfloor\sqrt{m}\rfloor$ edges** and delete $E(P_i)$ (if none exist, route $1$ arbitrary path).
   - **Proof:** Partition unrouted optimal paths $\mathcal{O} \setminus A$ into $\mathcal{O}_{\text{short}}$ ($\le L$ edges) and $\mathcal{O}_{\text{long}}$ ($> L$ edges):
     - Each $Q \in \mathcal{O}_{\text{short}}$ shares $\ge 1$ edge with some $P \in A$. Since $\mathcal{O}$ is edge-disjoint and $|E(P)| \le L$, $|\mathcal{O}_{\text{short}}| \le \sum_{P \in A} |E(P)| \le L|A|$.
     - Since paths in $\mathcal{O}_{\text{long}}$ are edge-disjoint and each uses $> L$ edges, $|\mathcal{O}_{\text{long}}| < m / L \le \sqrt{m} \le \sqrt{m}|A|$.
     - Total: $\text{OPT} = |\mathcal{O}| \le |A| + |\mathcal{O}_{\text{short}}| + |\mathcal{O}_{\text{long}}| \le (1 + 2\sqrt{m})|A|$. $\blacksquare$

3. **Metric Steiner Tree via $\text{MST}(G_T)$ ($2$-Approx — Practice Exam 2 Q3):**
   - **Part 1 (Constructing Spanning Tree $H$ of $G_T$ with $w(H) \le 2w(F^*)$):** Perform a DFS traversal (or double edges for an Eulerian tour) of the optimal Steiner tree $F^*$, traversing each edge of $F^*$ twice to get a closed walk $W$ visiting all terminals $T$ with $w(W) = 2w(F^*)$. Order $T = \{t_1,\dots,t_k\}$ by **first appearance** along $W$ and shortcut each sub-walk $t_i \leadsto t_{i+1}$ to the direct edge $(t_i, t_{i+1}) \in G_T$. By the **triangle inequality** and nonnegativity of edge weights, the path $H = \{(t_1,t_2),\dots,(t_{k-1},t_k)\}$ is a spanning tree of $G_T$ with $w(H) \le w(W) = 2w(F^*)$.
   - **Part 2 (Why $\text{MST}(G_T)$ is a $2$-Approx):** Since $\text{MST}(G_T)$ has minimum weight among **all** spanning trees of $G_T$ and $H$ is a spanning tree of $G_T$, $w(\text{MST}(G_T)) \le w(H) \le 2w(F^*)$. $\blacksquare$

4. **Greedy Load Balancing / Makespan Minimization (HW 4 Q17):**
   - **Two Universal Lower Bounds:** (1) $\text{OPT} \ge \frac{1}{m}\sum_{i=1}^n w_i$ (average load), and (2) $\text{OPT} \ge \max_i w_i$ (largest single job).
   - **Proof:** Let $M_i$ be the machine achieving makespan $T$, and let $j$ be the **last job** assigned to $M_i$. Before job $j$ arrived, $M_i$ had the minimum load among all $m$ machines, so $\text{load}(M_i) - w_j \le \frac{1}{m}\sum_{k \neq j} w_k < \frac{1}{m}\sum_{k=1}^n w_k \le \text{OPT}$.
     - **Unsorted ($2$-Approx):** $w_j \le \text{OPT} \implies T = (\text{load}(M_i) - w_j) + w_j \le \text{OPT} + \text{OPT} = 2\,\text{OPT}$.
     - **Sorted $w_1 \ge \dots \ge w_n$ ($1.5$-Approx):** If $j \le m$, $M_i$ only has job $j$ so $T = w_j \le \text{OPT}$. If $j \ge m+1$, by Pigeonhole among the $m+1$ jobs $w_1 \ge \dots \ge w_{m+1}$ on $m$ machines, $\text{OPT} \ge 2 w_{m+1} \ge 2 w_j \implies w_j \le \frac{1}{2}\text{OPT} \implies T \le 1.5\,\text{OPT}$. $\blacksquare$



5. **LP Threshold Rounding for Weighted Vertex Cover ($b=2$) & $b$-Hitting Set / $f$-Set Cover (Lec 15 / HW 4 Q18):**
   - **LP Relaxation:** $\min \sum_i w_i x_i$ s.t. $\sum_{i \in S_j} x_i \ge 1 \;\;(\forall j),\; x_i \ge 0$, where $|S_j| \le b$. Since every integral cover is LP-feasible, $\text{OPT}_{\text{LP}} \le \text{OPT}$.
   - **Threshold Rule:** Round $H = \{i : x_i^* \ge 1/b\}$.
     - *Feasibility:* Since $\sum_{i \in S_j} x_i^* \ge 1$ and $|S_j| \le b$, the average is $\ge 1/b$, so $\max_{i \in S_j} x_i^* \ge 1/b \implies |H \cap S_j| \ge 1$.
     - *Cost ($b$-Approx):* For $i \in H$, $1 \le b\,x_i^*$, so $\sum_{i \in H} w_i \le \sum_{i \in H} w_i (b\,x_i^*) \le b \sum_i w_i x_i^* = b\,\text{OPT}_{\text{LP}} \le b\,\text{OPT}$. $\blacksquare$

6. **Metric Uncapacitated Facility Location via LP Ball-Clustering ($6$-Approx — Lec 15):**
   - **LP:** $\min \sum_{i \in F} f_i x_i + \sum_{j \in C}\sum_{i \in F} d_{ij} y_{ij}$ s.t. $\sum_{i \in F} y_{ij} = 1 \;\;(\forall j),\; y_{ij} \le x_i \;\;(\forall i,j),\; x_i, y_{ij} \ge 0$. Write $\text{OPT}_{\text{LP}} = F^* + D^* \le \text{OPT}$.
   - **Algorithm:** Set $L_j = \sum_{i \in F} d_{ij} y_{ij}^*$ (so $\sum_j L_j = D^*$) and ball $B_j = \{i \in F : d_{ij} \le 2L_j\}$.
     1. *Markov Mass $\ge 1/2$:* If $\sum_{i \in B_j} y_{ij}^* < 1/2$, then $> 1/2$ of $y_{ij}^*$ has $d_{ij} > 2L_j \implies L_j > \frac{1}{2}(2L_j) = L_j$, contradiction! Since $x_i^* \ge y_{ij}^*$, $\sum_{i \in B_j} x_i^* \ge 1/2$.
     2. *Greedy Disjoint Balls:* Sort clients in **nondecreasing order of $L_j$**. Greedily pick $r \in R$ if $B_r \cap B_{r'} = \emptyset$ for all prior $r' \in R$. Open cheapest $\hat{i}_r = \arg\min_{i \in B_r} f_i$ in each selected $B_r$.
     3. *Opening Cost $\le 2F^*$:* $f_{\hat{i}_r} \le 2\sum_{i \in B_r} f_i x_i^*$. Since $\{B_r\}_{r \in R}$ are **disjoint**, $\sum_{r \in R} f_{\hat{i}_r} \le 2\sum_{i \in F} f_i x_i^* = 2F^*$.
     4. *Connection Cost $\le 6D^*$:* If $j \in R$, $d(\hat{i}_j, j) \le 2L_j \le 6L_j$. If $j \notin R$, $B_j$ hit some earlier $B_r$ ($L_r \le L_j$) at $i' \in B_r \cap B_j$; by **triangle inequality**, $d(\hat{i}_r, j) \le d(\hat{i}_r, r) + d(i', r) + d(i', j) \le 2L_r + 2L_r + 2L_j \le 6L_j$. Summing gives $\le 2F^* + 6D^* \le 6\,\text{OPT}$. $\blacksquare$

---

## 6. High-Yield True/False & Short-Answer Exam Traps (Practice Exam 2 Checklist)

- **"Every convex set is an intersection of finitely many half-spaces." $\to$ FALSE.** Only *polyhedra* are; a circle/ball $x_1^2 + x_2^2 \le 1$ is convex but requires infinitely many half-spaces.
- **"In Facility Location LP, if all opening costs $f_i = 0$, what happens?" $\to$ Every client connects to its nearest facility.** Setting $y_i = 1$ for all $i$ costs $0$, decoupling clients so each $j$ puts $x_{i^*(j), j} = 1$ on $\arg\min_i d_{ij}$.
- **"GD on a $\beta$-smooth convex function converges regardless of step size $\eta$." $\to$ FALSE.** Requires $0 < \eta < \frac{2}{\beta}$ (standard $\eta = \frac{1}{\beta}$). On $f(x) = \frac{1}{2}x^2$ ($\beta=1$), $\eta = 2$ oscillates forever and $\eta > 2$ diverges to $\infty$.
- **"We can run Projected GD to solve LPs in polynomial time." $\to$ FALSE.** PGD takes $O(D^2G^2/\varepsilon^2)$ steps, which is **pseudo-polynomial** in $1/\varepsilon$ (exponential in the bit-length $\log_2(1/\varepsilon)$ needed to round to an exact vertex).
- **"Can both Primal and Dual LPs be infeasible?" $\to$ TRUE.** Weak duality forbids (Unbounded, Unbounded) and (Finite Opt, Infeasible), but (Infeasible, Infeasible) is possible!
- **"A $2$-approximation algorithm on a maximization problem with $\text{OPT} = 5$ can return $7$ or $10$." $\to$ FALSE.** For maximization, $\frac{1}{2}\text{OPT} \le \text{ALG} \le \text{OPT} \implies 2.5 \le \text{ALG} \le 5$.
