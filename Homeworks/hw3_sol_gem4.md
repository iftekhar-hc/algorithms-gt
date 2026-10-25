# Linear Programming and Convex Optimization — Problem Set 3 Study Guide
**Course:** CS 6515 / 4540 (Fall 2026)

This guide explains the underlying concepts, visual intuition, step-by-step derivations, textbook references, and video lectures for all problems in `hw3.tex`. All math is formatted for direct rendering on GitHub.

---

## Problem 10: Linear Programs (Alice's Fruit Party)

### 1. Core Concepts & Visual Intuition
A **Linear Program (LP)** optimizes a linear objective function subject to linear equality and inequality constraints.
- **Decision Variables:** The quantities we control ($x_A, x_B$).
- **Feasible Region:** The set of all $(x_A, x_B)$ satisfying all constraints. Geometrically, each linear inequality $a_1 x_A + a_2 x_B \ge b$ defines a **half-space**, and their intersection forms a **convex polyhedron** (or a polygon in 2D).
- **Certificates of Optimality (Weak Duality):** How do you prove that you cannot spend less than $30$ dollars without testing infinitely many points? By taking a **non-negative linear combination** of the constraints! If $y_1 \ge 0$ and $y_2 \ge 0$, you can multiply Constraint 1 by $y_1$ and Constraint 2 by $y_2$ and add them together. If the left-hand side of the combined inequality is $\le$ your cost function $3x_A + 2x_B$, then the right-hand side gives a **guaranteed lower bound** on the cost. This is the heart of **LP Duality**.

#### ASCII Visualization of Alice's Feasible Region
```text
  x_B (Bundle B)
   ^
20 | * (0, 20)  <-- Cost = 3(0) + 2(20) = 40
   |  \
   |   \  Banana constraint: 2x_A + x_B >= 20
   |    \
   |     \          FEASIBLE REGION
   |      \         (unbounded above and to the right)
   |       \
   |        \
2.67|---\    \
   |     \----\     Orange constraint: x_A + 3x_B >= 8
   |           \---\
   +----------------*----*----> x_A (Bundle A)
   0                8   10
                        ^-- Optimal Vertex (10, 0):
                            Oranges = 10 (>= 8), Bananas = 20 (>= 20)
                            Cost = 3(10) + 2(0) = 30
```

**Geometric Observation:**
- Line 1 (Oranges): $x_A + 3x_B = 8$ passes through $(0, 8/3)$ and $(8, 0)$.
- Line 2 (Bananas): $2x_A + x_B = 20$ passes through $(0, 20)$ and $(10, 0)$.
- Because every point in the first quadrant ($x_A \ge 0, x_B \ge 0$) satisfying $2x_A + x_B \ge 20$ automatically satisfies $x_A + 3x_B \ge \frac{1}{2}(2x_A + x_B) \ge 10 > 8$, the banana constraint completely dominates the orange constraint in the first quadrant!
- Thus, the vertices of the feasible region in the first quadrant are $(0, 20)$ (cost $40$) and $(10, 0)$ (cost $30$).

---

### 2. Step-by-Step Solution

#### Part 1: Formulate and Justify the LP
- **Variables:** Let $x_A \in \mathbb{R}$ be the number of Bundle A's purchased, and $x_B \in \mathbb{R}$ be the number of Bundle B's purchased.
- **Objective:** Bundle A costs $3$ dollars and Bundle B costs $2$ dollars, so total dollars spent is $3x_A + 2x_B$, which Alice wants to minimize.
- **Constraints:**
  - **Oranges:** Bundle A has $1$ orange and Bundle B has $3$ oranges, so total oranges is $x_A + 3x_B \ge 8$.
  - **Bananas:** Bundle A has $2$ bananas and Bundle B has $1$ banana, so total bananas is $2x_A + x_B \ge 20$.
  - **Non-negativity:** Alice cannot buy negative bundles, so $x_A \ge 0$ and $x_B \ge 0$.

$$
\begin{aligned}
\min_{x_A, x_B} \quad & 3x_A + 2x_B \\
\text{s.t.} \quad & x_A + 3x_B \ge 8 \\
& 2x_A + x_B \ge 20 \\
& x_A \ge 0, \quad x_B \ge 0
\end{aligned}
$$

#### Part 2: Show there exists a feasible solution with objective value $30$
Set $x_A = 10$ and $x_B = 0$:
1. **Non-negativity:** $x_A = 10 \ge 0$ and $x_B = 0 \ge 0$.
2. **Orange constraint:** $x_A + 3x_B = 10 + 3(0) = 10 \ge 8$.
3. **Banana constraint:** $2x_A + x_B = 2(10) + 0 = 20 \ge 20$.
4. **Objective value:** $3x_A + 2x_B = 3(10) + 2(0) = 30$.

Since $(x_A, x_B) = (10, 0)$ satisfies all constraints and achieves cost $30$, Alice has to spend at most $30$ dollars.

#### Part 3: Prove every feasible solution has objective value at least $30$
Take a non-negative linear combination of the constraints with weights $\frac{3}{2} \ge 0$ on the banana constraint ($2x_A + x_B \ge 20$), $\frac{1}{2} \ge 0$ on the non-negativity constraint ($x_B \ge 0$), and $0$ on the orange constraint:

$$
\begin{aligned}
3x_A + 2x_B &= \frac{3}{2}(2x_A + x_B) + \frac{1}{2}(x_B) \\
&\ge \frac{3}{2}(20) + \frac{1}{2}(0) \\
&= 30.
\end{aligned}
$$

Therefore, every feasible solution $(x_A, x_B)$ has objective value at least $30$, proving that $(10, 0)$ with value $30$ is optimal.

---

## Problem 11: LP Equivalent Formulation & Farkas' Lemma

### 1. Core Concepts & Visual Intuition

#### Standard Equality Form (LP1) vs. Inequality Form (LP2)
- **LP1:** $\max c^\top x$ subject to $Ax = b, x \ge 0$.
- **LP2:** $\max c^\top x$ subject to $Ax \le b$ (with $x \in \mathbb{R}^n$ unrestricted in sign).

Two standard tricks convert LP2 into LP1:
1. **Splitting Unrestricted Variables ($x_i = x_i^+ - x_i^-$):** Any real number $x_i \in \mathbb{R}$ can be written as the difference of two non-negative numbers $x_i^+ \ge 0$ and $x_i^- \ge 0$.
2. **Slack Variables ($Ax + z = b, z \ge 0$):** An inequality $\sum_{i=1}^n A_{ji} x_i \le b_j$ holds if and only if there exists a non-negative slack $z_j = b_j - \sum_{i=1}^n A_{ji} x_i \ge 0$ such that $\sum_{i=1}^n A_{ji} x_i + z_j = b_j$.

#### Farkas' Lemma (The Theorem of Alternatives)
Geometrically, the set $C = \{Ax : x \ge 0\}$ is a **convex cone** generated by the columns of $A$. Either $b \in C$ (the system $Ax = b, x \ge 0$ is feasible), or there exists a **separating hyperplane** with normal vector $\lambda \in \mathbb{R}^m$ such that every generator column $A_{\cdot, i}$ has non-negative inner product with $\lambda$ ($\lambda^\top A \ge 0$), while $b$ has strictly negative inner product with $\lambda$ ($\lambda^\top b < 0$).

```text
          Columns of A (Convex Cone {Ax : x >= 0})
                \       /
                 \     /
                  \   /
                   \ /
       -------------+------------- Separating Hyperplane (normal vector lambda)
                   /
                  v
                 b  (Outside the cone: lambda^T b < 0, while lambda^T A >= 0)
```

---

### 2. Step-by-Step Solution

#### Part 1: Reducing LP2 to LP1
Given an instance of **LP2**:

$$
\max \sum_{i=1}^n c_i x_i \quad \text{s.t.} \quad \sum_{i=1}^n A_{ji} x_i \le b_j, \quad \forall j \in \{1, \dots, m\}.
$$

**Step 1 (Construction of LP1):**
For each $i \in \{1, \dots, n\}$, replace $x_i$ with $x_i^+ - x_i^-$ where $x_i^+ \ge 0, x_i^- \ge 0$. For each constraint $j \in \{1, \dots, m\}$, introduce a slack variable $z_j \ge 0$. We obtain an instance of **LP1** with $2n + m$ non-negative variables $(x^+, x^-, z)$:

$$
\begin{aligned}
\max \quad & \sum_{i=1}^n c_i x_i^+ - \sum_{i=1}^n c_i x_i^- + \sum_{j=1}^m 0 \cdot z_j \\
\text{s.t.} \quad & \sum_{i=1}^n A_{ji} x_i^+ - \sum_{i=1}^n A_{ji} x_i^- + z_j = b_j, \quad \forall j \in \{1, \dots, m\} \\
& x_i^+ \ge 0, \quad x_i^- \ge 0 \quad \forall i \in \{1, \dots, n\}, \qquad z_j \ge 0 \quad \forall j \in \{1, \dots, m\}.
\end{aligned}
$$

In block-matrix notation, with $\tilde{x} = \begin{bmatrix} x^+ \\ x^- \\ z \end{bmatrix} \in \mathbb{R}^{2n+m}$, $\tilde{c} = \begin{bmatrix} c \\ -c \\ 0 \end{bmatrix}$, and $\tilde{A} = \begin{bmatrix} A & -A & I_m \end{bmatrix} \in \mathbb{R}^{m \times (2n+m)}$, this is $\max \tilde{c}^\top \tilde{x}$ subject to $\tilde{A}\tilde{x} = b, \tilde{x} \ge 0$.

**Step 2 (Correctness and Polynomial-Time Equivalence):**
- **Polynomial Size:** The constructed LP1 has $2n + m$ variables and $m$ equality constraints, so it is constructed in $O(nm)$ time and has size polynomial in the size of LP2.
- **LP2 $\implies$ LP1:** Given any feasible $x \in \mathbb{R}^n$ for LP2, set $x_i^+ = \max(x_i, 0) \ge 0$, $x_i^- = \max(-x_i, 0) \ge 0$, and $z_j = b_j - \sum_{i=1}^n A_{ji} x_i \ge 0$. Then $(x^+, x^-, z)$ is feasible for LP1 and has objective value $\sum_{i=1}^n c_i (x_i^+ - x_i^-) = \sum_{i=1}^n c_i x_i$.
- **LP1 $\implies$ LP2:** Given any feasible $(x^+, x^-, z) \ge 0$ for LP1, set $x_i = x_i^+ - x_i^-$. Since $z_j \ge 0$, we have $\sum_{i=1}^n A_{ji} x_i = b_j - z_j \le b_j$, so $x$ is feasible for LP2 with the exact same objective value $\sum_{i=1}^n c_i x_i$.
- Therefore, both LPs have the same optimal value, and an optimal solution $x^*$ to LP2 can be recovered in $O(n)$ time via $x_i^* = (x_i^+)^* - (x_i^-)^*$ from an optimal solution to LP1.

---

#### Part 2: Showing Farkas' Lemma A $\implies$ Farkas' Lemma B
Consider the system in **Farkas' Lemma B**:

$$
\sum_{i=1}^n A_{ji} x_i \le b_j \quad \forall j \in \{1, \dots, m\} \quad (x \in \mathbb{R}^n \text{ unconstrained}).
$$

**Step 1:** By the exact variable transformation from Part 1, this inequality system is feasible if and only if the standard-form equality system

$$
\tilde{A}\tilde{x} = b, \quad \tilde{x} \ge 0
$$

is feasible, where $\tilde{A} = \begin{bmatrix} A & -A & I_m \end{bmatrix} \in \mathbb{R}^{m \times (2n+m)}$ and $\tilde{x} = \begin{bmatrix} x^+ \\ x^- \\ z \end{bmatrix} \in \mathbb{R}^{2n+m}$.

**Step 2:** Apply **Farkas' Lemma A** to $\tilde{A}\tilde{x} = b, \tilde{x} \ge 0$. By Farkas' Lemma A, this system is infeasible if and only if there exists $\lambda \in \mathbb{R}^m$ such that:

$$
\sum_{j=1}^m \lambda_j b_j < 0 \qquad \text{and} \qquad \lambda^\top \tilde{A} \ge 0.
$$

**Step 3:** Expand $\lambda^\top \tilde{A} \ge 0$ across the three column blocks of $\tilde{A} = \begin{bmatrix} A & -A & I_m \end{bmatrix}$:
1. From the first $n$ columns ($A$):

$$
\sum_{j=1}^m \lambda_j A_{ji} \ge 0, \quad \forall i \in \{1, \dots, n\}.
$$

2. From the next $n$ columns ($-A$):

$$
\sum_{j=1}^m \lambda_j (-A_{ji}) \ge 0 \iff \sum_{j=1}^m \lambda_j A_{ji} \le 0, \quad \forall i \in \{1, \dots, n\}.
$$

3. From the last $m$ columns ($I_m$):

$$
\lambda_j \ge 0, \quad \forall j \in \{1, \dots, m\}.
$$

Combining (1) and (2) gives $\sum_{j=1}^m \lambda_j A_{ji} = 0$ for all $i \in \{1, \dots, n\}$, and (3) gives $\lambda_j \ge 0$ for all $j \in \{1, \dots, m\}$, together with $\sum_{j=1}^m \lambda_j b_j < 0$. This is precisely **Farkas' Lemma B**.

---

## Problem 12: LP for Regression ($\ell_1$ and $\ell_\infty$) & Duals

### 1. Core Concepts & Visual Intuition
Given $n$ data points $(x_1, y_1), \dots, (x_n, y_n) \in \mathbb{R}^2$, we want to fit a line $y = ax + b$ ($a, b \in \mathbb{R}$):
- **$\ell_1$ Regression (Least Absolute Deviations):** Minimizes $\sum_{i=1}^n |y_i - ax_i - b|$. Because errors are not squared, $\ell_1$ regression is much more **robust to outliers** than least squares.
- **$\ell_\infty$ Regression (Chebyshev / Minimax Fit):** Minimizes $\max_{1 \le i \le n} |y_i - ax_i - b|$, minimizing the worst-case vertical residual across all points.

#### Linearizing Absolute Values via Epigraph Variables
For any residual $r_i = y_i - ax_i - b$, the non-linear expression $|r_i| \le e_i$ is equivalent to two linear inequalities:

$$
-e_i \le y_i - ax_i - b \le e_i \iff \begin{cases} e_i + ax_i + b \ge y_i \\ e_i - ax_i - b \ge -y_i \end{cases}
$$

```text
  y ^
    |          * (x_3, y_3)
    |          |  <-- Vertical residual |y_3 - (a x_3 + b)|
    |        /
    |      /   Fitted line: y = a x + b
    |    * (x_2, y_2)
    |  /
    | * (x_1, y_1)
    +---------------------> x
```

---

### 2. Step-by-Step Solution

#### Part 1: $\ell_1$ Regression LP
Introduce auxiliary variables $e_1, \dots, e_n \in \mathbb{R}$ to upper-bound each absolute residual $|y_i - ax_i - b|$. The decision variables are $a, b \in \mathbb{R}$ and $e_1, \dots, e_n \in \mathbb{R}$ ($n + 2$ variables and $2n$ constraints):

$$
\begin{aligned}
\min_{a, b, e_1, \dots, e_n} \quad & \sum_{i=1}^n e_i \\
\text{s.t.} \quad & e_i + a x_i + b \ge y_i, \quad \forall i \in \{1, \dots, n\} \\
& e_i - a x_i - b \ge -y_i, \quad \forall i \in \{1, \dots, n\} \\
& a, b, e_1, \dots, e_n \in \mathbb{R}.
\end{aligned}
$$

*(Note: Adding the two constraints for $i$ automatically implies $2e_i \ge 0 \implies e_i \ge 0$, and at optimality $e_i = |y_i - ax_i - b|$.)*

#### Part 2: $\ell_\infty$ Regression LP
Introduce a single scalar variable $t \in \mathbb{R}$ to upper-bound the maximum absolute residual $\max_{1 \le i \le n} |y_i - ax_i - b|$. The decision variables are $a, b, t \in \mathbb{R}$ ($3$ variables and $2n$ constraints):

$$
\begin{aligned}
\min_{a, b, t} \quad & t \\
\text{s.t.} \quad & t + a x_i + b \ge y_i, \quad \forall i \in \{1, \dots, n\} \\
& t - a x_i - b \ge -y_i, \quad \forall i \in \{1, \dots, n\} \\
& a, b, t \in \mathbb{R}.
\end{aligned}
$$

#### Part 3: Dual LPs for Both Problems

In a minimization LP with $\ge$ constraints and unrestricted primal variables:
- Every $\ge$ constraint $i$ corresponds to a **non-negative** dual variable.
- Every unrestricted primal variable corresponds to an **equality ($=$)** constraint in the dual.

##### Dual of the $\ell_1$ Regression LP
Let $u_i \ge 0$ be the dual variable for $e_i + ax_i + b \ge y_i$, and $v_i \ge 0$ be the dual variable for $e_i - ax_i - b \ge -y_i$, for $i \in \{1, \dots, n\}$:
- Dual constraint from unrestricted primal variable $e_i$ (objective coefficient $1$): $u_i + v_i = 1$.
- Dual constraint from unrestricted primal variable $a$ (objective coefficient $0$): $\sum_{i=1}^n x_i (u_i - v_i) = 0$.
- Dual constraint from unrestricted primal variable $b$ (objective coefficient $0$): $\sum_{i=1}^n (u_i - v_i) = 0$.

$$
\begin{aligned}
\max_{u, v \in \mathbb{R}^n} \quad & \sum_{i=1}^n y_i (u_i - v_i) \\
\text{s.t.} \quad & u_i + v_i = 1, \quad \forall i \in \{1, \dots, n\} \\
& \sum_{i=1}^n x_i (u_i - v_i) = 0 \\
& \sum_{i=1}^n (u_i - v_i) = 0 \\
& u_i \ge 0, \quad v_i \ge 0, \quad \forall i \in \{1, \dots, n\}.
\end{aligned}
$$

##### Dual of the $\ell_\infty$ Regression LP
Let $u_i \ge 0$ be the dual variable for $t + ax_i + b \ge y_i$, and $v_i \ge 0$ be the dual variable for $t - ax_i - b \ge -y_i$, for $i \in \{1, \dots, n\}$:
- Dual constraint from unrestricted primal variable $t$ (objective coefficient $1$): $\sum_{i=1}^n (u_i + v_i) = 1$.
- Dual constraint from unrestricted primal variable $a$ (objective coefficient $0$): $\sum_{i=1}^n x_i (u_i - v_i) = 0$.
- Dual constraint from unrestricted primal variable $b$ (objective coefficient $0$): $\sum_{i=1}^n (u_i - v_i) = 0$.

$$
\begin{aligned}
\max_{u, v \in \mathbb{R}^n} \quad & \sum_{i=1}^n y_i (u_i - v_i) \\
\text{s.t.} \quad & \sum_{i=1}^n (u_i + v_i) = 1 \\
& \sum_{i=1}^n x_i (u_i - v_i) = 0 \\
& \sum_{i=1}^n (u_i - v_i) = 0 \\
& u_i \ge 0, \quad v_i \ge 0, \quad \forall i \in \{1, \dots, n\}.
\end{aligned}
$$

---

## Problem 13: The Minimax Theorem via LP Duality

### 1. Core Concepts & Visual Intuition
In a two-player **zero-sum matrix game** $A \in \mathbb{R}^{m \times n}$, Alice chooses a probability distribution $p \in \Delta_m$ over the $m$ rows and Bob chooses a probability distribution $q \in \Delta_n$ over the $n$ columns, where

$$
\Delta_k = \left\{ z \in \mathbb{R}^k : z_\ell \ge 0 \text{ for all } \ell, \ \sum_{\ell=1}^k z_\ell = 1 \right\}.
$$

- **Best Response to a Known Mixed Strategy:** If Alice commits to $p \in \Delta_m$, Bob's expected payoff to Alice is $p^\top A q = \sum_{j=1}^n \left(\sum_{i=1}^m A_{ij} p_i\right) q_j$, which is a convex combination of the $n$ column payoffs $c_j = \sum_{i=1}^m A_{ij} p_i$. To minimize a weighted average of numbers, Bob can put $100\%$ of his probability weight on the single smallest column payoff $\min_{1 \le j \le n} c_j$.
- **Von Neumann's Minimax Theorem:** Using Strong LP Duality, Alice's maximin payoff equals Bob's minimax payoff:

$$
\max_{p \in \Delta_m} \min_{q \in \Delta_n} p^\top A q = \min_{q \in \Delta_n} \max_{p \in \Delta_m} p^\top A q = V.
$$

---

### 2. Step-by-Step Solution

#### Part 1: Pure Best Response, Primal LP Interpretation, Feasibility & Boundedness

**1. Proof that $\min_{q \in \Delta_n} p^\top A q = \min_{1 \le j \le n} \sum_{i=1}^m A_{ij} p_i$:**
For a fixed $p \in \Delta_m$, let $c_j = \sum_{i=1}^m A_{ij} p_i$ for each $j \in \{1, \dots, n\}$, and let $c_{\min} = \min_{1 \le j \le n} c_j$.
- **($\ge$ direction):** For any $q \in \Delta_n$, since $q_j \ge 0$ and $\sum_{j=1}^n q_j = 1$:

$$
p^\top A q = \sum_{j=1}^n c_j q_j \ge \sum_{j=1}^n c_{\min} q_j = c_{\min} \sum_{j=1}^n q_j = c_{\min}.
$$

  Taking the minimum over all $q \in \Delta_n$ yields $\min_{q \in \Delta_n} p^\top A q \ge c_{\min}$.
- **($\le$ direction):** Let $j^* \in \arg\min_{1 \le j \le n} c_j$ and choose the standard basis vector $q = e_{j^*} \in \Delta_n$. Then $p^\top A e_{j^*} = c_{j^*} = c_{\min}$, so $\min_{q \in \Delta_n} p^\top A q \le c_{\min}$.
- Combining both inequalities establishes the identity.

**2. Why the Primal LP's optimal value equals Alice's largest guaranteed expected payoff:**
In the primal LP, $p_i \ge 0$ and $\sum_{i=1}^m p_i = 1$ mean $p \in \Delta_m$. The constraints $v - \sum_{i=1}^m A_{ij} p_i \le 0$ for $j = 1, \dots, n$ are equivalent to:

$$
v \le \min_{1 \le j \le n} \sum_{i=1}^m A_{ij} p_i = \min_{q \in \Delta_n} p^\top A q.
$$

For any fixed $p \in \Delta_m$, maximizing $v$ sets $v = \min_{q \in \Delta_n} p^\top A q$. Maximizing over all $p \in \Delta_m$ therefore gives $\max_{p \in \Delta_m} \min_{q \in \Delta_n} p^\top A q$.

**3. Feasibility and Boundedness of the Primal LP:**
- **Feasible:** Choose $p = (1, 0, \dots, 0)^\top \in \Delta_m$ and $v = \min_{1 \le j \le n} A_{1j}$. All constraints are satisfied.
- **Bounded Above:** Let $M = \max_{i,j} A_{ij}$. For any feasible $(p, v)$, since $p \in \Delta_m$,

$$
v \le \sum_{i=1}^m A_{i1} p_i \le \sum_{i=1}^m M p_i = M < \infty.
$$

---

#### Part 2: Deriving the Dual LP
Write the Primal LP with variables $p_1, \dots, p_m \ge 0$ and $v \in \mathbb{R}$ (unrestricted):

$$
\begin{aligned}
\max_{p, v} \quad & 0^\top p + 1 \cdot v \\
\text{s.t.} \quad & -\sum_{i=1}^m A_{ij} p_i + v \le 0, \quad \text{for } j = 1, \dots, n \quad (\text{dual variables } q_j \ge 0) \\
& \sum_{i=1}^m p_i + 0 \cdot v = 1 \quad (\text{dual variable } w \in \mathbb{R}) \\
& p_i \ge 0 \quad \text{for } i = 1, \dots, m, \qquad v \in \mathbb{R}.
\end{aligned}
$$

Applying the LP duality rules gives the **Dual LP**:

$$
\begin{aligned}
\min_{q_1, \dots, q_n, w} \quad & w \\
\text{s.t.} \quad & w - \sum_{j=1}^n A_{ij} q_j \ge 0, \quad \text{for } i = 1, \dots, m, \\
& \sum_{j=1}^n q_j = 1, \\
& q_j \ge 0, \quad \text{for } j = 1, \dots, n, \\
& w \in \mathbb{R} \quad (\text{unrestricted in sign}).
\end{aligned}
$$

---

#### Part 3: Dual Interpretation, Strong LP Duality & Saddle-Point Guarantees

1. **Dual Optimal Value:** In the dual LP, $q_j \ge 0$ and $\sum_{j=1}^n q_j = 1$ mean $q \in \Delta_n$. By the symmetric argument to Part 1, for a fixed $q \in \Delta_n$, $\max_{p \in \Delta_m} p^\top A q = \max_{1 \le i \le m} \sum_{j=1}^n A_{ij} q_j$. The constraints $w \ge \sum_{j=1}^n A_{ij} q_j$ for all $i$ are equivalent to $w \ge \max_{p \in \Delta_m} p^\top A q$. Minimizing $w$ over $q \in \Delta_n$ yields $\min_{q \in \Delta_n} \max_{p \in \Delta_m} p^\top A q$.
2. **Strong LP Duality:** Since the primal LP is feasible and bounded above, Strong LP Duality guarantees optimal primal and dual solutions $(p^*, v^*)$ and $(q^*, w^*)$ with equal optimal values:

$$
\max_{p \in \Delta_m} \min_{q \in \Delta_n} p^\top A q = v^* = w^* = \min_{q \in \Delta_n} \max_{p \in \Delta_m} p^\top A q.
$$

3. **Saddle-Point Guarantees:** Set $V = v^* = w^*$.
   - Primal feasibility of $(p^*, V)$ gives $\sum_{i=1}^m A_{ij} p_i^* \ge V$ for all $j$. For any $q \in \Delta_n$, $(p^*)^\top A q = \sum_{j=1}^n q_j \left(\sum_{i=1}^m A_{ij} p_i^*\right) \ge \sum_{j=1}^n q_j V = V$.
   - Dual feasibility of $(q^*, V)$ gives $\sum_{j=1}^n A_{ij} q_j^* \le V$ for all $i$. For any $p \in \Delta_m$, $p^\top A q^* = \sum_{i=1}^m p_i \left(\sum_{j=1}^n A_{ij} q_j^*\right) \le \sum_{i=1}^m p_i V = V$.
   - Setting $q = q^*$ and $p = p^*$ gives $V \le (p^*)^\top A q^* \le V \implies (p^*)^\top A q^* = V$.

---

## Problem 14: Convex Sets and Convex Functions

### 1. Core Concepts & Visual Intuition
- **Convex Set $K \subseteq \mathbb{R}^n$:** For all $x, y \in K$ and $\theta \in [0, 1]$, the point $\theta x + (1-\theta)y \in K$.
- **Convex Function $f : \mathbb{R} \to \mathbb{R}$:** For all $x, y \in \mathbb{R}$ and $\theta \in [0, 1]$, **Jensen's Inequality** holds:

$$
f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y).
$$

*(Note: Do not assume differentiability! Use the definition of convexity directly.)*

```text
  Intersection of Convex Sets (CONVEX)        Union of Convex Sets (NOT CONVEX)
       +-------+                                 +---+           +---+
       |   K   |                                 | K |           | L |
       |   +---+---+                             | x *-----------* y |
       |   |K n L  |                             +---+  segment  +---+
       +---+-------+                                   leaves K u L!
           |   L   |
           +-------+
```

---

### 2. Step-by-Step Solution

#### Part 1: Intersection and Union of Convex Sets $K, L \subseteq \mathbb{R}^n$
1. **Must $K \cap L$ be convex? YES.**
   - **Proof:** Let $x, y \in K \cap L$ and $\theta \in [0, 1]$. Since $x, y \in K$ and $K$ is convex, $\theta x + (1-\theta)y \in K$. Since $x, y \in L$ and $L$ is convex, $\theta x + (1-\theta)y \in L$. Therefore $\theta x + (1-\theta)y \in K \cap L$, so $K \cap L$ is convex.
2. **Must $K \cup L$ be convex? NO.**
   - **Counterexample:** Let $K = \{0\} \subseteq \mathbb{R}^n$ and $L = \{e_1\} \subseteq \mathbb{R}^n$, where $e_1 = (1, 0, \dots, 0)^\top$. Both singleton sets $K$ and $L$ are convex. However, for $x = 0 \in K \cup L$, $y = e_1 \in K \cup L$, and $\theta = \frac{1}{2}$, the convex combination $\frac{1}{2}x + \frac{1}{2}y = \frac{1}{2}e_1 \notin K \cup L$. Thus $K \cup L$ is not convex.

#### Part 2: Sum of Convex Functions $f + g$
**Must $f + g$ be convex? YES.**
- **Proof:** Let $x, y \in \mathbb{R}$ and $\theta \in [0, 1]$. By convexity of $f$ and $g$:

$$
\begin{aligned}
(f+g)(\theta x + (1-\theta)y) &= f(\theta x + (1-\theta)y) + g(\theta x + (1-\theta)y) \\
&\le \big[\theta f(x) + (1-\theta)f(y)\big] + \big[\theta g(x) + (1-\theta)g(y)\big] \\
&= \theta (f+g)(x) + (1-\theta)(f+g)(y).
\end{aligned}
$$

Thus $f + g$ is convex.

#### Part 3: Pointwise Product of Convex Functions $h(x) = f(x)g(x)$
**Must $h(x) = f(x)g(x)$ be convex? NO.**
- **Counterexample:** Let $f(x) = x$ and $g(x) = -x$. Both $f$ and $g$ are linear and therefore convex on $\mathbb{R}$. Their product is $h(x) = -x^2$. Taking $x = -1, y = 1$, and $\theta = \frac{1}{2}$:

$$
h\left(\frac{1}{2}(-1) + \frac{1}{2}(1)\right) = h(0) = 0 > -1 = \frac{1}{2}h(-1) + \frac{1}{2}h(1).
$$

Hence $h$ violates Jensen's inequality and is not convex.

#### Part 4: Pointwise Maximum of Convex Functions $h(x) = \max\{f(x), g(x)\}$
**Must $h(x) = \max\{f(x), g(x)\}$ be convex? YES.**
- **Proof:** Let $x, y \in \mathbb{R}$ and $\theta \in [0, 1]$. By definition of $h$, $f(x) \le h(x), f(y) \le h(y), g(x) \le h(x)$, and $g(y) \le h(y)$. Since $\theta \ge 0$ and $1-\theta \ge 0$:

$$
f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y) \le \theta h(x) + (1-\theta)h(y),
$$

$$
g(\theta x + (1-\theta)y) \le \theta g(x) + (1-\theta)g(y) \le \theta h(x) + (1-\theta)h(y).
$$

Taking the maximum of the left-hand sides gives:

$$
h(\theta x + (1-\theta)y) = \max\big\{f(\theta x + (1-\theta)y), g(\theta x + (1-\theta)y)\big\} \le \theta h(x) + (1-\theta)h(y).
$$

Thus $h(x) = \max\{f(x), g(x)\}$ is convex.

---

## Problem 15: Gradient Descent for Strongly-Convex Functions

### 1. Core Concepts & Visual Intuition
A differentiable function $f : \mathbb{R}^n \to \mathbb{R}$ is **$\alpha$-strongly convex** ($\alpha > 0$) if for all $x, y \in \mathbb{R}^n$:

$$
f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle + \frac{\alpha}{2}\|y - x\|_2^2.
$$

- Geometrically, $f$ grows at least as fast as a quadratic bowl of curvature $\alpha$ above every tangent hyperplane.
- In standard convex gradient descent, regret scales as $O(1/\sqrt{T})$. With $\alpha$-strong convexity, the extra $-\frac{\alpha}{2}\|x_t - x^*\|_2^2$ term allows us to use a **time-varying potential function** $\Phi(t) = \frac{t\alpha}{2}\|x_t - x^*\|_2^2$ with step size $\eta_t = \frac{1}{\alpha(t+1)}$ so the quadratic distances telescope!

```text
  Standard Convex (Flat bottom)         alpha-Strongly Convex (Quadratic lower bound)
       \               /                        \         /
        \             /                          \       /
         \___________/                            \  *  /   <-- Always curves up at least
               *                                   \___/        as fast as (alpha/2)||y-x||^2
```

---

### 2. Step-by-Step Solution

#### Step 1: One-Step Distance Expansion
With the gradient descent update $x_{t+1} = x_t - \eta_t \nabla f(x_t)$, expand $\|x_{t+1} - x^*\|_2^2$:

$$
\|x_{t+1} - x^*\|_2^2 = \|x_t - x^*\|_2^2 - 2\eta_t \langle \nabla f(x_t), x_t - x^* \rangle + \eta_t^2 \|\nabla f(x_t)\|_2^2.
$$

Rearranging for $\langle \nabla f(x_t), x_t - x^* \rangle$ and using $\|\nabla f(x_t)\|_2 \le G$:

$$
\langle \nabla f(x_t), x_t - x^* \rangle \le \frac{\|x_t - x^*\|_2^2 - \|x_{t+1} - x^*\|_2^2}{2\eta_t} + \frac{\eta_t G^2}{2}.
$$

#### Step 2: Combine with $\alpha$-Strong Convexity and $\Phi(t)$
Evaluating the $\alpha$-strong convexity inequality at $x = x_t$ and $y = x^*$ gives:

$$
f(x_t) - f(x^*) \le \langle \nabla f(x_t), x_t - x^* \rangle - \frac{\alpha}{2}\|x_t - x^*\|_2^2.
$$

Substitute the bound from Step 1 with $\eta_t = \frac{1}{\alpha(t+1)}$ (so $\frac{1}{2\eta_t} = \frac{\alpha(t+1)}{2}$):

$$
\begin{aligned}
f(x_t) - f(x^*) &\le \frac{\alpha(t+1)}{2}\Big(\|x_t - x^*\|_2^2 - \|x_{t+1} - x^*\|_2^2\Big) - \frac{\alpha}{2}\|x_t - x^*\|_2^2 + \frac{G^2}{2\alpha(t+1)} \\
&= \frac{t\alpha}{2}\|x_t - x^*\|_2^2 - \frac{(t+1)\alpha}{2}\|x_{t+1} - x^*\|_2^2 + \frac{G^2}{2\alpha(t+1)} \\
&= \Phi(t) - \Phi(t+1) + \frac{G^2}{2\alpha(t+1)},
\end{aligned}
$$

where $\Phi(t) = \frac{t\alpha}{2}\|x_t - x^*\|_2^2$.

#### Step 3: Telescope and Apply Jensen's Inequality
Summing over the $T$ steps (for $t = 0, 1, \dots, T-1$, or equivalently shifting $\Phi(t) = \frac{(t-1)\alpha}{2}\|x_t - x^*\|_2^2$ for $t = 1, \dots, T$):

$$
\begin{aligned}
\sum_{t} \big(f(x_t) - f(x^*)\big) &\le \Phi(0) - \Phi(T) + \frac{G^2}{2\alpha} \sum_{k=1}^T \frac{1}{k} \\
&\le 0 - 0 + \frac{G^2 (1 + \log T)}{2\alpha},
\end{aligned}
$$

where we used $\Phi(0) = 0$, $\Phi(T) \ge 0$, and the harmonic sum bound $\sum_{k=1}^T \frac{1}{k} \le 1 + \log T$.

Finally, by convexity of $f$ (Jensen's inequality) applied to the average iterate $\bar{x}_T = \frac{1}{T}\sum_t x_t$:

$$
f\left(\frac{\sum_t x_t}{T}\right) - f(x^*) \le \frac{1}{T}\sum_t \big(f(x_t) - f(x^*)\big) \le \frac{G^2(1 + \log T)}{2\alpha T}.
$$

---

## Recommended Textbooks & Video Lectures

### 1. Textbook References (By Problem)

| Problem / Topic | Primary Textbook Reference | Secondary / Advanced Reference |
| :--- | :--- | :--- |
| **Problems 10 & 11:** LP Formulations, Standard Form, Certificates & Farkas' Lemma | **Dasgupta, Papadimitriou, Vazirani (DPV)**, *Algorithms*, **Chapter 7** (Sections 7.1, 7.2, 7.4 on Linear Programming & Duality)<br>**Matoušek & Gärtner**, *Understanding and Using Linear Programming*, **Chapters 4 & 6** (Section 6.5 covers Farkas' Lemma in detail) | **Bertsimas & Tsitsiklis**, *Introduction to Linear Optimization*, **Chapter 1** (Equivalence of LP forms) & **Section 4.6** (Farkas' Lemma and theorems of alternatives) |
| **Problem 12:** $\ell_1$ and $\ell_\infty$ Regression via LP & Duals | **Boyd & Vandenberghe**, *Convex Optimization* (free PDF at `stanford.edu/~boyd/cvxbook`), **Section 1.2.2** (Least-norm and Chebyshev approximation) & **Section 6.1** (Norm approximation & robust regression) | **Vanderbei**, *Linear Programming: Foundations and Extensions*, **Chapter 12** ($\ell_1$ and $\ell_\infty$ regression and their duals) |
| **Problem 13:** Zero-Sum Games & Minimax Theorem via LP Duality | **Dasgupta, Papadimitriou, Vazirani (DPV)**, *Algorithms*, **Section 7.5** (Zero-Sum Games)<br>**Matoušek & Gärtner**, **Section 6.3** (Game Theory and the Minimax Theorem) | **Boyd & Vandenberghe**, *Convex Optimization*, **Section 5.2.5** (Matrix games and LP duality) |
| **Problem 14:** Convex Sets & Operations Preserving Convexity | **Boyd & Vandenberghe**, *Convex Optimization*, **Section 2.3.1** (Intersection of convex sets) & **Section 3.2** (Operations that preserve convexity: nonnegative weighted sums, pointwise maximum) | **Bubeck**, *Convex Optimization: Algorithms and Complexity*, **Chapter 1** (Basic properties of convex sets and functions) |
| **Problem 15:** Gradient Descent for Strongly Convex Functions | **Hazan**, *Introduction to Online Convex Optimization* (free PDF at `ocobook.cs.princeton.edu`), **Section 3.3** (Online Gradient Descent for Strongly Convex Functions — derives this exact $\frac{G^2(1+\log T)}{2\alpha T}$ bound) | **Bubeck**, *Convex Optimization: Algorithms and Complexity* (`arXiv:1405.4980`), **Sections 3.1 & 3.4** (Subgradient/GD for strongly convex functions with $1/(\alpha t)$ step size) |

---

### 2. Suggested Video Lectures

1. **Linear Programming, Duality, Farkas' Lemma & Zero-Sum Games (Problems 10–13):**
   - **Ryan O'Donnell & Anupam Gupta (CMU 15-451 / 15-859 — Linear Programming & CS Theory Toolkit):**
     - Search YouTube for *"Ryan O'Donnell Linear Programming Lecture"*. His lectures on **LP Duality, Certificates of Optimality, Farkas' Lemma, and the Minimax Theorem** follow the exact geometric and algebraic perspective of Problems 10, 11, and 13.
   - **Tim Roughgarden (Stanford CS261 / Columbia COMS 4995 — A Second Course in Algorithms):**
     - Search YouTube for *"Tim Roughgarden Linear Programming Duality"* and *"Zero-Sum Games and the Minimax Theorem"*. Lectures 8–11 walk step-by-step through LP equivalences, Farkas' Lemma, and proving von Neumann's Minimax Theorem via LP Duality.
   - **MIT 6.046J (Design and Analysis of Algorithms — Erik Demaine / Srini Devadas):**
     - *Lecture 15: Linear Programming: LP, reductions, Simplex, Duality* (MIT OpenCourseWare on YouTube). Clear walkthrough of standard-form reductions and $\ell_1$/$\ell_\infty$ LP formulations.

2. **Convex Sets, Convex Functions & Regression LPs (Problems 12 & 14):**
   - **Stephen Boyd (Stanford EE364a — Convex Optimization I):**
     - Available on the *Stanford Online* YouTube channel:
       - **Lecture 2:** *Convex Sets* (intersections, half-spaces, polyhedra).
       - **Lectures 3 & 4:** *Convex Functions* (Jensen's inequality, sums, pointwise maximums, and epigraphs).
       - **Lectures 9 & 10:** *Approximation and Fitting* ($\ell_1$ and $\ell_\infty$ norm approximation and LP reformulations).

3. **Gradient Descent for Strongly Convex Functions (Problem 15):**
   - **Elad Hazan / Constantine Caramanis (Online & Convex Optimization Lectures):**
     - Search YouTube for *"Elad Hazan Online Convex Optimization Lecture"* or *"Constantine Caramanis Convex Optimization Strong Convexity"* (UT Austin EE 381V playlist). They derive the exact telescoping potential proof with step size $\eta_t = \frac{1}{\alpha(t+1)}$ and explain why strong convexity improves convergence from $O(1/\sqrt{T})$ to $O\left(\frac{\log T}{T}\right)$.




