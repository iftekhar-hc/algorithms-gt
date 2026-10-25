# Linear Programming and Convex Optimization: Solutions and Study Guide

This guide provides complete mathematical solutions, explanations, visualizations, and references for the problems in **Problem Set 3 (CS 6515 / CS 4540)**. Math equations are formatted with GitHub-supported MathJax / LaTeX delimiters (`$` for inline math and `$$` for block display math).

---

## 1. Linear Programming Formulations and Dual Bounds

### Problem Formulation
Alice needs to purchase fruit for a party with the following minimum requirements:
- **Oranges:** At least 8
- **Bananas:** At least 20

The grocery store sells two bundles with fractional quantities permitted:
- **Bundle A:** Costs $3; contains 1 orange and 2 bananas.
- **Bundle B:** Costs $2; contains 3 oranges and 1 banana.

Let $x_A \ge 0$ and $x_B \ge 0$ denote the number of Bundle A and Bundle B purchased, respectively.

### Part 1: Primal Linear Program
The linear program minimizing Alice's expenditure is:

$$\begin{aligned}
\min_{x_A, x_B} \quad & 3x_A + 2x_B \\
\text{subject to} \quad & 1 x_A + 3 x_B \ge 8 \quad &&\text{(Orange requirement)} \\
& 2 x_A + 1 x_B \ge 20 \quad &&\text{(Banana requirement)} \\
& x_A \ge 0, \; x_B \ge 0 \quad &&\text{(Non-negativity)}
\end{aligned}$$

**Justification:**
- The objective function $3x_A + 2x_B$ represents the total dollar cost.
- The constraint $x_A + 3x_B \ge 8$ ensures at least 8 oranges are acquired.
- The constraint $2x_A + x_B \ge 20$ ensures at least 20 bananas are acquired.
- $x_A, x_B \ge 0$ reflects that fractional purchases are allowed but negative quantities are prohibited.

---

### Part 2: Feasible Solution with Cost 30
Consider the point $(x_A, x_B) = (10, 0)$:
1. **Orange constraint:** $1(10) + 3(0) = 10 \ge 8$ (satisfied).
2. **Banana constraint:** $2(10) + 1(0) = 20 \ge 20$ (satisfied).
3. **Non-negativity:** $10 \ge 0$ and $0 \ge 0$ (satisfied).
4. **Objective cost:** $3(10) + 2(0) = 30$.

Because $(10, 0)$ is feasible, Alice can achieve her goal with an expenditure of at most $30.

---

### Part 3: Proof of Optimality via Dual Multipliers
To prove every feasible point satisfies $3x_A + 2x_B \ge 30$, take a non-negative linear combination of the constraints with multipliers $y_1, y_2 \ge 0$:

$$y_1(x_A + 3x_B) + y_2(2x_A + x_B) \ge 8y_1 + 20y_2$$

Regrouping the coefficients of $x_A$ and $x_B$:

$$(y_1 + 2y_2)x_A + (3y_1 + y_2)x_B \ge 8y_1 + 20y_2$$

Choose $y_1 = 0$ and $y_2 = 1.5$:
- Coefficient of $x_A$: $0 + 2(1.5) = 3$.
- Coefficient of $x_B$: $3(0) + 1.5 = 1.5$.
- Right-hand side lower bound: $8(0) + 20(1.5) = 30$.

Thus, for any feasible $(x_A, x_B)$:

$$3x_A + 1.5x_B \ge 30$$

Since $x_B \ge 0$, we have $2x_B \ge 1.5x_B$, which implies:

$$3x_A + 2x_B \ge 3x_A + 1.5x_B \ge 30$$

Every feasible solution has cost at least $30. Combined with the feasible candidate $(10, 0)$ costing exactly $30$, $(x_A^*, x_B^*) = (10, 0)$ is an optimal solution.

```
  xB ^
     |
  20 + \  Constraint 2: 2*xA + xB >= 20
     |  \
     |   \   Feasible Region (unbounded above and to the right)
     |    \
     |     \
 8/3 +      \---... Constraint 1: xA + 3*xB >= 8
     |       \  \
   0 +--------+--+------------------------> xA
     0        8  10 (Optimal point: cost = 30)
```

---

## 2. LP Equivalent Formulations and Farkas' Lemma

### Part 1: Simulating LP2 using LP1
We are given two canonical forms:
- **LP1 (Standard Equational Form):**
  $$\max \sum_{i=1}^n c_i x_i \quad \text{s.t.} \quad \sum_{i=1}^n A_{ji} x_i = b_j \; (\forall j), \quad x_i \ge 0 \; (\forall i)$$
- **LP2 (Inequality Form with Free Variables):**
  $$\max \sum_{i=1}^n c_i x_i \quad \text{s.t.} \quad \sum_{i=1}^n A_{ji} x_i \le b_j \; (\forall j)$$

To convert any instance of LP2 into an instance of LP1:
1. **Splitting unconstrained variables:** Replace each free variable $x_i \in \mathbb{R}$ with $x_i = x_i^+ - x_i^-$, where $x_i^+ \ge 0$ and $x_i^- \ge 0$.
2. **Slack variables:** Convert inequalities into equalities by introducing non-negative slack variables $s_j \ge 0$ such that:
   $$\sum_{i=1}^n A_{ji}(x_i^+ - x_i^-) + s_j = b_j \quad \forall j \in \{1, \dots, m\}$$

The resulting linear program is:

$$\begin{aligned}
\max \quad & \sum_{i=1}^n c_i x_i^+ - \sum_{i=1}^n c_i x_i^- + \sum_{j=1}^m 0 \cdot s_j \\
\text{s.t.} \quad & \sum_{i=1}^n A_{ji} x_i^+ - \sum_{i=1}^n A_{ji} x_i^- + s_j = b_j \quad \forall j \in \{1, \dots, m\} \\
& x_i^+ \ge 0, \quad x_i^- \ge 0, \quad s_j \ge 0 \quad \forall i, j
\end{aligned}$$

This problem has $2n + m$ non-negative variables and $m$ equality constraints, matching the syntactic form of LP1. Any polynomial-time algorithm for LP1 solves LP2 via the transformation $x_i = x_i^+ - x_i^-$.

---

### Part 2: Farkas' Lemma A Implies Farkas' Lemma B
- **Farkas' Lemma A:** The system $Ax = b, x \ge 0$ is infeasible if and only if there exists $\lambda \in \mathbb{R}^m$ such that:
  $$\lambda^\top b < 0 \quad \text{and} \quad \lambda^\top A \ge 0^\top$$

- **Farkas' Lemma B:** The system $Ax \le b$ is infeasible if and only if there exists $\lambda \ge 0$ such that:
  $$\lambda^\top b < 0 \quad \text{and} \quad \lambda^\top A = 0^\top$$

**Proof:**
1. Express feasibility of $Ax \le b$ in equational form with non-negative variables. Writing $x = x^+ - x^-$ with $x^+, x^- \ge 0$, and adding slack $s \ge 0$:
   $$A(x^+ - x^-) + s = b \iff \begin{bmatrix} A & -A & I_m \end{bmatrix} \begin{bmatrix} x^+ \\ x^- \\ s \end{bmatrix} = b, \quad \begin{bmatrix} x^+ \\ x^- \\ s \end{bmatrix} \ge 0$$
2. Let $\tilde{A} = \begin{bmatrix} A & -A & I_m \end{bmatrix}$ and $\tilde{x} = \begin{bmatrix} x^+ \\ x^- \\ s \end{bmatrix}$. The system $\tilde{A}\tilde{x} = b, \tilde{x} \ge 0$ is in the exact format of Lemma A.
3. By Farkas' Lemma A, this system is infeasible if and only if there exists $\lambda \in \mathbb{R}^m$ such that:
   $$\lambda^\top b < 0 \quad \text{and} \quad \lambda^\top \tilde{A} \ge 0^\top$$
4. Decomposing the condition $\lambda^\top \tilde{A} \ge 0^\top$:
   - $\lambda^\top A \ge 0^\top$
   - $\lambda^\top (-A) \ge 0^\top \iff \lambda^\top A \le 0^\top$
   - $\lambda^\top I_m \ge 0^\top \iff \lambda \ge 0$
5. The two conditions $\lambda^\top A \ge 0^\top$ and $\lambda^\top A \le 0^\top$ together imply $\lambda^\top A = 0^\top$.
6. Therefore, infeasibility of $Ax \le b$ is equivalent to the existence of $\lambda \ge 0$ with $\lambda^\top b < 0$ and $\lambda^\top A = 0^\top$, proving Farkas' Lemma B.

---

## 3. LP Formulations for Regression and Their Duals

Given $n$ observations $(x_1, y_1), \dots, (x_n, y_n) \in \mathbb{R}^2$, fit a linear model $y = ax + b$ with parameters $a, b \in \mathbb{R}$.

### Part 1: $\ell_1$ Regression (Least Absolute Deviations)
Minimize $\sum_{i=1}^n |y_i - ax_i - b|$. Introduce auxiliary variables $t_i \ge |y_i - ax_i - b|$:

$$\begin{aligned}
\min_{a, b, t_1, \dots, t_n} \quad & \sum_{i=1}^n t_i \\
\text{subject to} \quad & t_i + a x_i + b \ge y_i \quad \forall i \in \{1, \dots, n\} \\
& t_i - a x_i - b \ge -y_i \quad \forall i \in \{1, \dots, n\}
\end{aligned}$$
*(Variables $a, b \in \mathbb{R}$ are unconstrained; $t_i \ge 0$ is implied).*

---

### Part 2: $\ell_\infty$ Regression (Chebyshev / Minimax Residual)
Minimize $\max_{1 \le i \le n} |y_i - ax_i - b|$. Introduce a single scalar bound $t$:

$$\begin{aligned}
\min_{a, b, t} \quad & t \\
\text{subject to} \quad & t + a x_i + b \ge y_i \quad \forall i \in \{1, \dots, n\} \\
& t - a x_i - b \ge -y_i \quad \forall i \in \{1, \dots, n\}
\end{aligned}$$

---

### Part 3: Dual Linear Programs
Assign dual variables $u_i \ge 0$ to the $+ (ax_i + b)$ constraints and $v_i \ge 0$ to the $-(ax_i + b)$ constraints.

#### Dual of $\ell_1$ Regression:
$$\begin{aligned}
\max_{u, v \ge 0} \quad & \sum_{i=1}^n y_i (u_i - v_i) \\
\text{subject to} \quad & u_i + v_i \le 1 \quad \forall i \in \{1, \dots, n\} \\
& \sum_{i=1}^n x_i (u_i - v_i) = 0 \\
& \sum_{i=1}^n (u_i - v_i) = 0
\end{aligned}$$

Setting $w_i = u_i - v_i \in [-1, 1]$ gives the equivalent formulation:

$$\max_{w \in [-1, 1]^n} \sum_{i=1}^n y_i w_i \quad \text{s.t.} \quad \sum_{i=1}^n w_i = 0, \quad \sum_{i=1}^n x_i w_i = 0$$

#### Dual of $\ell_\infty$ Regression:
$$\begin{aligned}
\max_{u, v \ge 0} \quad & \sum_{i=1}^n y_i (u_i - v_i) \\
\text{subject to} \quad & \sum_{i=1}^n (u_i + v_i) \le 1 \\
& \sum_{i=1}^n x_i (u_i - v_i) = 0 \\
& \sum_{i=1}^n (u_i - v_i) = 0
\end{aligned}$$

Setting $w_i = u_i - v_i$, this maximizes $y^\top w$ subject to $\|w\|_1 \le 1$, $\sum_{i=1}^n w_i = 0$, and $\sum_{i=1}^n x_i w_i = 0$.

---

## 4. The Minimax Theorem via LP Duality

Consider a zero-sum game with payoff matrix $A \in \mathbb{R}^{m \times n}$. Alice chooses $p \in \Delta_m$ (row strategy), and Bob chooses $q \in \Delta_n$ (column strategy). The expected payoff to Alice is $p^\top A q$.

### Part 1: Best Pure-Strategy Response and Primal Equivalence
For any fixed $p \in \Delta_m$:

$$\min_{q \in \Delta_n} p^\top A q = \min_{q \in \Delta_n} \sum_{j=1}^n q_j (A^\top p)_j$$

Because the objective is linear in $q$ and $\Delta_n$ is the probability simplex, the minimum occurs at one of the vertices $e_j$:

$$\min_{q \in \Delta_n} p^\top A q = \min_{1 \le j \le n} (A^\top p)_j = \min_{1 \le j \le n} \sum_{i=1}^m A_{ij} p_i$$

The primal LP is:

$$\begin{array}{ll}
\text{maximize} & v \\
\text{subject to} & v - \sum_{i=1}^m A_{ij} p_i \le 0 \quad \forall j \in \{1, \dots, n\} \\
& \sum_{i=1}^m p_i = 1 \\
& p_i \ge 0 \; (\forall i), \quad v \in \mathbb{R}
\end{array}$$

For any fixed valid probability distribution $p$, the optimal choice of $v$ is $\min_{1 \le j \le n} \sum_{i=1}^m A_{ij} p_i$. Maximizing over all $p \in \Delta_m$ gives:

$$v^* = \max_{p \in \Delta_m} \min_{q \in \Delta_n} p^\top A q$$

**Feasibility and Boundedness:**
- Feasible: Choose $p = (1/m, \dots, 1/m)$ and $v = \min_j \frac{1}{m}\sum_i A_{ij}$.
- Bounded: $v \le \sum_{i=1}^m A_{ij} p_i \le \max_{i, j} A_{ij}$, which is finite.

---

### Part 2: Deriving the Dual LP
Form the Lagrangian using multipliers $q_j \ge 0$ for inequality constraints and $w \in \mathbb{R}$ for the equality constraint:

$$L(v, p, q, w) = v + \sum_{j=1}^n q_j \left(\sum_{i=1}^m A_{ij} p_i - v\right) + w \left(1 - \sum_{i=1}^m p_i\right)$$

Rearranging by primal variables:

$$L(v, p, q, w) = w + v \left(1 - \sum_{j=1}^n q_j\right) + \sum_{i=1}^m p_i \left(\sum_{j=1}^n A_{ij} q_j - w\right)$$

To ensure $\sup_{v, p_i \ge 0} L < \infty$:
1. Coefficient of $v$ must vanish: $\sum_{j=1}^n q_j = 1$.
2. Coefficient of each $p_i$ must be non-positive: $\sum_{j=1}^n A_{ij} q_j - w \le 0 \implies w \ge \sum_{j=1}^n A_{ij} q_j$.

**Dual Linear Program:**

$$\begin{array}{ll}
\text{minimize} & w \\
\text{subject to} & w - \sum_{j=1}^n A_{ij} q_j \ge 0 \quad \forall i \in \{1, \dots, m\} \\
& \sum_{j=1}^n q_j = 1 \\
& q_j \ge 0 \; (\forall j), \quad w \in \mathbb{R}
\end{array}$$

---

### Part 3: Strong Duality and the Minimax Theorem
1. For fixed $q \in \Delta_n$, the smallest admissible $w$ is $\max_{1 \le i \le m} (A q)_i = \max_{p \in \Delta_m} p^\top A q$.
2. The dual LP therefore finds Bob's optimal strategy:

   $$w^* = \min_{q \in \Delta_n} \max_{p \in \Delta_m} p^\top A q$$

3. Both primal and dual are feasible and bounded. By **strong LP duality**, their optimal objective values are equal:

   $$\max_{p \in \Delta_m} \min_{q \in \Delta_n} p^\top A q = v^* = w^* = \min_{q \in \Delta_n} \max_{p \in \Delta_m} p^\top A q = V$$

4. Let $p^* \in \Delta_m$ and $q^* \in \Delta_n$ denote optimal solutions for primal and dual, respectively. Then:
   - For every $q \in \Delta_n$: $(p^*)^\top A q \ge \min_j (A^\top p^*)_j = v^* = V$.
   - For every $p \in \Delta_m$: $p^\top A q^* \le \max_i (A q^*)_i = w^* = V$.
   - Evaluating at $(p^*, q^*)$ forces $(p^*)^\top A q^* = V$, establishing von Neumann's minimax theorem.

---

## 5. Convex Sets and Convex Functions

| Statement | Status | Proof / Counterexample |
| :--- | :--- | :--- |
| **Intersection $K \cap L$ of convex sets** | **Always convex** | Let $x, y \in K \cap L$ and $\theta \in [0, 1]$. Since $x, y \in K$, convexity of $K$ implies $\theta x + (1-\theta)y \in K$. Similarly, $\theta x + (1-\theta)y \in L$. Thus $\theta x + (1-\theta)y \in K \cap L$. |
| **Union $K \cup L$ of convex sets** | **Not necessarily convex** | Let $K = [0, 1]$ and $L = [2, 3]$ in $\mathbb{R}$. Both sets are convex intervals. The midpoint of $1 \in K$ and $2 \in L$ is $1.5 \notin K \cup L$. |
| **Sum $f + g$ of convex functions** | **Always convex** | $(f+g)(\theta x + (1-\theta)y) = f(\theta x + (1-\theta)y) + g(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y) + \theta g(x) + (1-\theta)g(y) = \theta(f+g)(x) + (1-\theta)(f+g)(y)$. |
| **Product $fg$ of convex functions** | **Not necessarily convex** | Let $f(x) = x$ and $g(x) = -x$ on $\mathbb{R}$. Both are linear and therefore convex. Their product is $h(x) = -x^2$, which has $h''(x) = -2 < 0$, making it strictly concave. |
| **Pointwise max $\max\{f, g\}$** | **Always convex** | Let $h(x) = \max\{f(x), g(x)\}$. Since $f(x) \le h(x)$ and $g(x) \le h(x)$, we have $f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y) \le \theta h(x) + (1-\theta)h(y)$. Similarly, $g(\theta x + (1-\theta)y) \le \theta h(x) + (1-\theta)h(y)$. Taking the maximum of the left-hand sides yields $h(\theta x + (1-\theta)y) \le \theta h(x) + (1-\theta)h(y)$. |

---

## 6. Gradient Descent for Strongly Convex Functions

### Setup and Definitions
- **Strong Convexity:** For all $x, y \in \mathbb{R}^n$:
  $$f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle + \frac{\alpha}{2} \|y - x\|^2$$
- **Bounded Gradients:** $\|\nabla f(x)\|_2 \le G$ for all $x$.
- **Update Rule:** $x_{t+1} = x_t - \eta_t \nabla f(x_t)$ with $\eta_t = \frac{1}{\alpha(t+1)}$.
- **Potential Function:** $\Phi(t) = \frac{t \alpha}{2} \|x_t - x^*\|^2$.

---

### Telescoping Convergence Proof
1. **One-step iterate distance expansion:**
   $$\|x_{t+1} - x^*\|^2 = \|x_t - x^* - \eta_t \nabla f(x_t)\|^2 = \|x_t - x^*\|^2 - 2\eta_t \langle \nabla f(x_t), x_t - x^* \rangle + \eta_t^2 \|\nabla f(x_t)\|^2$$

2. **Lower bounding the gradient inner product via strong convexity:**
   Setting $y = x^*$ and $x = x_t$:
   $$f(x^*) \ge f(x_t) + \langle \nabla f(x_t), x^* - x_t \rangle + \frac{\alpha}{2} \|x_t - x^*\|^2$$
   $$\implies \langle \nabla f(x_t), x_t - x^* \rangle \ge f(x_t) - f(x^*) + \frac{\alpha}{2} \|x_t - x^*\|^2$$

3. **Substituting into distance expansion:**
   $$\|x_{t+1} - x^*\|^2 \le \|x_t - x^*\|^2 - 2\eta_t \left(f(x_t) - f(x^*) + \frac{\alpha}{2} \|x_t - x^*\|^2\right) + \eta_t^2 G^2$$

   Substitute $\eta_t = \frac{1}{\alpha(t+1)}$:
   $$\|x_{t+1} - x^*\|^2 \le \left(1 - \frac{1}{t+1}\right) \|x_t - x^*\|^2 - \frac{2}{\alpha(t+1)} (f(x_t) - f(x^*)) + \frac{G^2}{\alpha^2 (t+1)^2}$$

   Note that $1 - \frac{1}{t+1} = \frac{t}{t+1}$. Multiply both sides by $\frac{(t+1)\alpha}{2}$:
   $$\frac{(t+1)\alpha}{2} \|x_{t+1} - x^*\|^2 \le \frac{t\alpha}{2} \|x_t - x^*\|^2 - (f(x_t) - f(x^*)) + \frac{G^2}{2\alpha(t+1)}$$

4. **Potential representation:**
   Using $\Phi(t) = \frac{t\alpha}{2} \|x_t - x^*\|^2$:
   $$f(x_t) - f(x^*) \le \Phi(t) - \Phi(t+1) + \frac{G^2}{2\alpha(t+1)}$$

5. **Summing from $t = 1$ to $T$:**
   $$\sum_{t=1}^T (f(x_t) - f(x^*)) \le \Phi(1) - \Phi(T+1) + \frac{G^2}{2\alpha} \sum_{t=1}^T \frac{1}{t+1}$$

   Since $\Phi(T+1) \ge 0$ and $\Phi(1) = \frac{\alpha}{2}\|x_1 - x^*\|^2$:
   $$\sum_{t=1}^T (f(x_t) - f(x^*)) \le \frac{\alpha}{2} \|x_1 - x^*\|^2 + \frac{G^2}{2\alpha} \sum_{t=2}^{T+1} \frac{1}{t}$$

   Using standard initial conditions where $\|x_1 - x^*\|^2 \le \frac{G^2}{\alpha^2}$ (since $\alpha \|x_1 - x^*\| \le \|\nabla f(x_1)\| \le G$), the initial term $\frac{\alpha}{2}\|x_1 - x^*\|^2 \le \frac{G^2}{2\alpha}$. Combining the terms yields:
   $$\sum_{t=1}^T (f(x_t) - f(x^*)) \le \frac{G^2}{2\alpha} \sum_{t=1}^T \frac{1}{t} \le \frac{G^2(1 + \log T)}{2\alpha}$$

6. **Applying Jensen's inequality to the average iterate $\bar{x} = \frac{1}{T}\sum_{t=1}^T x_t$:**
   $$f(\bar{x}) - f(x^*) \le \frac{1}{T} \sum_{t=1}^T (f(x_t) - f(x^*)) \le \frac{G^2 (1 + \log T)}{2\alpha T}$$

This establishes the $O\left(\frac{\log T}{T}\right)$ convergence rate for strongly convex objectives.

---

## 7. Textbook References and Video Lectures

### Textbooks
1. **Stephen Boyd and Lieven Vandenberghe**, *Convex Optimization*, Cambridge University Press.
   - Chapter 2: Convex sets, separating hyperplanes, supporting hyperplanes.
   - Chapter 3: Convex functions and operations preserving convexity.
   - Chapters 4–5: Linear programming, duality theory, Slater's condition, and minimax games.
2. **Dimitris Bertsimas and John N. Tsitsiklis**, *Introduction to Linear Optimization*, Athena Scientific.
   - Chapters 2–3: Standard and canonical forms, geometry of linear programming.
   - Chapter 4: Duality, Farkas' Lemma variants, and certificates of infeasibility.
   - Chapter 7: Zero-sum matrix games and LP duality.
3. **Sébastien Bubeck**, *Convex Optimization: Algorithms and Complexity*, Foundations and Trends in Machine Learning.
   - Chapter 3: First-order methods, gradient descent rates for convex ($O(1/\sqrt{T})$) versus strongly convex ($O(1/T)$) objectives.

### Video Lectures
1. **Stanford EE364A: Convex Optimization I (Prof. Stephen Boyd)**
   - Lectures 1–4: Convex sets, convex functions, and operations preserving convexity.
   - Lectures 6–8: Duality, minimax formulation, and optimality conditions.
2. **MIT 6.046J / 18.410J: Design and Analysis of Algorithms (Prof. Erik Demaine & Prof. Srini Devadas)**
   - Lectures on Linear Programming and Duality.
3. **Carnegie Mellon University 10-725: Convex Optimization (Prof. Ryan Tibshirani)**
   - Lectures on Gradient Descent, Subgradient Methods, and Convergence Analysis for Strongly Convex Functions.
