# CS 6515 – Exam 2A: Complete Solutions & Concept Guide

**Source Exam:** `/local/mnt/workspace/GaTech/algorithms-gt/Exams/Exam2_SecA.pdf`  
**Course:** CS 6515/4540: Graduate Algorithms (Fall 2026 – Exam 2 – Section A)

---

## Exam Overview

| Question | Topic | Points | Core Concepts Tested |
| :--- | :--- | :---: | :--- |
| **Q1 (a)–(c)** | Linear Programming & Duality | 16 | Weak/Strong Duality, Complementary Slackness, Farkas' Lemma & Geometry of Tight Constraints |
| **Q1 (d)–(e)** | Projected Gradient Descent & Convexity | 16 | Gradient Step, Euclidean Projection onto Simplex/Half-space, First-Order Optimality Condition |
| **Q1 (f)** | Approximation Bounds (Vertex Cover) | 8 | $\alpha$-Approximation Ratios vs. Matching Lower Bounds |
| **Q2 (a)–(c)** | Greedy Approximation (Max Independent Set) | 15 | Greedy Neighborhood Removal, Charging/Partitioning Argument ($\Delta$-approx), Star Graph Tight Instance |
| **Q3 (a)–(c)** | Unconstrained Convex Optimization | 20 | $\beta$-Smoothness, Co-coercivity of Gradient, Monotonicity of $\|\nabla f(x_k)\|_2$, $O(1/\sqrt{k})$ Convergence |
| **Q4 (1)–(4)** | LP Relaxation & Deterministic Rounding | 25 | Set Cover with Frequency $k$, Threshold Rounding ($x_i^* \ge 1/k$), Tight Integrality/Rounding Example |

---

# Question 1: Short Answer Questions (40 points)

---

## Part (a): Primal-Dual Linear Programming Relationships (5 points)

### Question Statement
Consider a feasible primal maximization LP and its feasible dual minimization LP. Select **ALL** statements that are always true:
1. $\bigcirc$ The primal objective value is at most the dual objective value.
2. $\bigcirc$ If a primal-feasible solution and a dual-feasible solution have equal objective values, both are optimal.
3. $\bigcirc$ If $x^*$ is an optimal solution of the primal, every constraint (of the primal) is tight.
4. $\bigcirc$ If the primal has a finite optimal value, the dual has an optimal solution with the same value.

---

### Core Concept: Weak and Strong Duality

For a standard Primal (Maximization) and Dual (Minimization) pair:
$$\text{Primal (P): } \max \{ c^T x \mid Ax \le b, \, x \ge 0 \} \qquad \text{Dual (D): } \min \{ b^T y \mid A^T y \ge c, \, y \ge 0 \}$$

- **Weak Duality Theorem:** For *any* primal-feasible $x$ and *any* dual-feasible $y$:
  $$c^T x \le b^T y$$
  Every primal feasible value is a lower bound on the dual, and every dual feasible value is an upper bound on the primal.
- **Strong Duality Theorem:** If both LPs are feasible (or one has a finite optimum), then both have finite optimal solutions $x^*, y^*$ and their optimal values coincide:
  $$c^T x^* = b^T y^*$$

#### Visualization of Weak & Strong Duality on the Real Number Line
```
   Primal Feasible Values                     Dual Feasible Values
      (Maximization)                             (Minimization)
 ───────────●───────────●─────────★─────────●───────────●───────────► Objective Value
          c^T x_1     c^T x_2   OPT_P=OPT_D  b^T y_2     b^T y_1
                                  ▲
                           Duality Gap = 0
                     (if c^T x = b^T y, both hit ★)
```

---

### Step-by-Step Solution & Justification
- **Statement 1: TRUE.** By **Weak Duality**, for any primal-feasible $x$ and dual-feasible $y$, $c^T x \le b^T y$.
- **Statement 2: TRUE.** By **Weak Duality**, any primal-feasible $x'$ satisfies $c^T x' \le b^T y$, and any dual-feasible $y'$ satisfies $b^T y' \ge c^T x$. If $c^T x = b^T y$, no primal solution can exceed $c^T x$ and no dual solution can be smaller than $b^T y$, so both $x$ and $y$ are optimal.
- **Statement 3: FALSE.** Counterexample: Consider $\max x_1$ subject to $x_1 \le 1$ and $x_1 \le 2$ (with $x_1 \ge 0$). The unique optimal solution is $x_1^* = 1$, where the redundant constraint $x_1 \le 2$ is strictly slack ($1 < 2$, not tight). Even without redundant constraints, in 2D $\max x_1 + 0 x_2$ subject to $x_1 \le 1, x_2 \le 1, x_1, x_2 \ge 0$, $x^* = (1, 0)$ leaves $x_2 \le 1$ slack.
- **Statement 4: TRUE.** By **Strong Duality**, if the primal has a finite optimal value, the dual also has a finite optimal solution with the exact same objective value.

> **Final Answer for 1(a):** Select **1, 2, and 4**.

---

## Part (b): Complementary Slackness (5 points)

### Question Statement
Suppose a primal constraint holds strictly at an optimal primal solution $x^*$. What can we conclude about the corresponding variable in any optimal dual solution?
1. $\bigcirc$ It must equal zero.
2. $\bigcirc$ It must be strictly positive.
3. $\bigcirc$ It can be either positive or zero.
4. $\bigcirc$ The primal optimum cannot be unique.

---

### Core Concept: Complementary Slackness

Let $x^*$ be primal feasible and $y^*$ be dual feasible. By Weak Duality derivation:
$$c^T x^* \le (A^T y^*)^T x^* = (y^*)^T A x^* \le (y^*)^T b = b^T y^*$$
For Strong Duality ($c^T x^* = b^T y^*$) to hold at optimality, both inequalities must be equalities, which implies:
$$\sum_{i=1}^m y_i^* (b_i - a_i^T x^*) = 0$$
Since $y_i^* \ge 0$ and $b_i - a_i^T x^* \ge 0$ for every constraint $i$, each product term must be zero:
$$y_i^* \cdot (b_i - a_i^T x^*) = 0 \quad \forall i$$

#### Economic / Physical Intuition (Shadow Prices)
- $y_i^*$ is the **shadow price** (marginal value) of resource $i$.
- If the $i$-th primal constraint holds **strictly** ($a_i^T x^* < b_i$), we have leftover capacity of resource $i$ ($b_i - a_i^T x^* > 0$).
- Buying more of a resource you aren't even fully using gives zero benefit! Therefore, its shadow price must be zero: $y_i^* = 0$.

---

### Step-by-Step Solution & Justification
By **Complementary Slackness**, for every constraint $i$ and any optimal primal-dual pair $(x^*, y^*)$, $y_i^*(b_i - a_i^T x^*) = 0$. Since constraint $i$ holds strictly ($a_i^T x^* < b_i$, so $b_i - a_i^T x^* > 0$), we must have $y_i^* = 0$.

> **Final Answer for 1(b):** Select **1 (It must equal zero)**.

---

## Part (c): Geometry of LP Optimality & Farkas' Lemma (6 points)

### Question Statement
Consider the linear program:
$$\max c^T x \quad \text{s.t.} \quad Ax \le b, \quad x \in \mathbb{R}^n \text{ unrestricted in sign.}$$
Let $x^*$ be a feasible solution, and let $S = \{i \mid a_i^T x^* = b_i\}$ denote the set of constraints **tight** at $x^*$. Write $a_i^T$ for row $i$ of $A$. Suppose there **do not** exist coefficients $\lambda_i \ge 0$ such that:
$$c = \sum_{i \in S} \lambda_i a_i$$
Select **ALL** statements that must be true:
1. $\bigcirc$ There exists a direction $v$ such that $c^T v > 0$ and $a_i^T v \le 0$ for all $i \in S$.
2. $\bigcirc$ There exists a direction $v$ and $\varepsilon > 0$ such that $x^* + \varepsilon v$ is feasible and has strictly larger objective value.
3. $\bigcirc$ The linear program must be unbounded.
4. $\bigcirc$ Every constraint not in $S$ at $x^*$ remains satisfied under all sufficiently small perturbations of $x^*$.

---

### Core Concept: Cone of Active Normals & Improving Directions

At a feasible point $x^*$:
- **Tight constraints ($i \in S$):** $a_i^T x^* = b_i$. Moving from $x^*$ along direction $v$ by step $\varepsilon > 0$ keeps constraint $i$ satisfied iff:
  $$a_i^T(x^* + \varepsilon v) \le b_i \iff \varepsilon (a_i^T v) \le 0 \iff a_i^T v \le 0$$
- **Slack constraints ($i \notin S$):** $a_i^T x^* < b_i$. There is a strictly positive slack $\delta_i = b_i - a_i^T x^* > 0$. As long as $\varepsilon > 0$ is small enough (specifically, $\varepsilon a_i^T v \le \delta_i$), moving in *any* direction $v$ will not violate constraint $i$.
- **Farkas' Lemma:** Given vectors $\{a_i\}_{i \in S}$ and target vector $c$, **exactly one** of the following holds:
  1. $c$ lies in the conic hull of $\{a_i\}_{i \in S}$: $\exists \lambda_i \ge 0$ such that $c = \sum_{i \in S} \lambda_i a_i$ (meaning $x^*$ is already optimal!).
  2. There is a separating hyperplane / improving direction $v \in \mathbb{R}^n$ such that $a_i^T v \le 0$ for all $i \in S$ and $c^T v > 0$.

#### Visualization: Active Cone vs. Improving Direction
```
                     a_1 (normal to tight constraint 1)
                      ▲
                       \      Cone of active normals:
                        \     { Σ λ_i a_i : λ_i ≥ 0 }
                         \
              x* ●────────► a_2 (normal to tight constraint 2)
                / \
   Feasible    /   \  v (improving direction: a_1^T v ≤ 0, a_2^T v ≤ 0, c^T v > 0)
   Polytope   /     ▼
             /       c (objective vector outside active cone)
```

---

### Step-by-Step Solution & Justification
- **Statement 1: TRUE.** This is the exact statement of **Farkas' Lemma**: since $c = \sum_{i \in S} \lambda_i a_i$ has no solution with $\lambda_i \ge 0$, there must exist a vector $v$ with $a_i^T v \le 0$ for all $i \in S$ and $c^T v > 0$.
- **Statement 4: TRUE.** For every $j \notin S$, $a_j^T x^* < b_j$ (strict inequality). Each strict half-space $\{x : a_j^T x < b_j\}$ is an open set, and the intersection of finitely many open sets is open, so an open ball around $x^*$ satisfies all constraints $j \notin S$.
- **Statement 2: TRUE.** Combining Statements 1 and 4: taking $v$ from Statement 1, for any $\varepsilon > 0$ and $i \in S$, $a_i^T(x^* + \varepsilon v) = b_i + \varepsilon a_i^T v \le b_i$. By Statement 4, for sufficiently small $\varepsilon > 0$, all slack constraints $j \notin S$ remain satisfied. Moreover, $c^T(x^* + \varepsilon v) = c^T x^* + \varepsilon (c^T v) > c^T x^*$.
- **Statement 3: FALSE.** The condition only says $x^*$ is **not optimal** (we can locally improve $x^*$). As we move along $v$, we can eventually hit a currently slack constraint $j \notin S$ in a bounded polytope. (Counterexample: $\max x_1$ s.t. $x_1 \le 1$, at $x^* = 0$: $S = \emptyset$, $c = 1$ cannot be written as an empty sum, $v = 1$ improves $x^*$, yet the LP is bounded by $1$).

> **Final Answer for 1(c):** Select **1, 2, and 4**.

---

## Part (d): Projected Gradient Descent Step (10 points)

### Question Statement
Consider the constrained optimization problem:
$$\min f(x_1, x_2) = \frac{1}{2}(x_1^2 + 4x_2^2) - 2x_1 - 4x_2$$
$$\text{s.t. } x_1 + x_2 \le 2, \quad x_1, x_2 \ge 0.$$
Starting at $x^{(0)} = (0, 0)$, take one gradient descent step with $\eta = 1$. If the resulting point is infeasible, find the feasible point closest to it in Euclidean distance. Show your work.

---

### Core Concept: Projected Gradient Descent (PGD)

In constrained optimization over a convex set $K \subseteq \mathbb{R}^n$, one iteration of **Projected Gradient Descent** consists of two steps:
1. **Unconstrained Gradient Step:**
   $$y^{(k+1)} = x^{(k)} - \eta \nabla f(x^{(k)})$$
2. **Euclidean Projection onto $K$:**
   $$x^{(k+1)} = \Pi_K(y^{(k+1)}) = \arg\min_{x \in K} \|x - y^{(k+1)}\|_2$$

#### Visualization of the Step and Projection
```
    x_2
     ▲
   4 ┼           ● y^(1) = (2, 4)  [Unconstrained GD step]
     │          /
   3 ┼         /  Perpendicular projection onto x_1 + x_2 = 2
     │        /   (normal vector is (1,1), so move along (-1,-1))
   2 ★───────/ (0, 2) = x^(1)  [Closest feasible point!]
     │\     /
   1 ┼ \   /   Feasible Region K:
     │  \ /    Triangle with vertices (0,0), (2,0), (0,2)
   0 ●───●───────► x_1
   (0,0) (2,0)
```

---

### Step-by-Step Calculation

1. **Compute the gradient $\nabla f(x_1, x_2)$:**
   $$\frac{\partial f}{\partial x_1} = x_1 - 2, \qquad \frac{\partial f}{\partial x_2} = 4x_2 - 4$$
   $$\nabla f(x_1, x_2) = \begin{pmatrix} x_1 - 2 \\ 4x_2 - 4 \end{pmatrix}$$

2. **Evaluate at $x^{(0)} = (0, 0)$ and take the gradient step ($\eta = 1$):**
   $$\nabla f(0, 0) = (-2, -4)$$
   $$y^{(1)} = x^{(0)} - \eta \nabla f(x^{(0)}) = (0, 0) - 1 \cdot (-2, -4) = (2, 4)$$

3. **Check feasibility of $y^{(1)} = (2, 4)$:**
   - $x_1 = 2 \ge 0$, $x_2 = 4 \ge 0$ (non-negativity holds).
   - $x_1 + x_2 = 2 + 4 = 6 > 2$ (**violates** $x_1 + x_2 \le 2$, so $(2, 4)$ is **infeasible**).

4. **Project $y^{(1)} = (2, 4)$ onto the feasible region $K = \{(x_1, x_2) \mid x_1 + x_2 \le 2, \, x_1, x_2 \ge 0\}$:**
   - First, project $(2, 4)$ orthogonally onto the boundary line $x_1 + x_2 = 2$.
   - The normal vector to the line $x_1 + x_2 = 2$ is $n = (1, 1)$. Any orthogonal projection onto this line has the form $(2, 4) - t(1, 1) = (2 - t, 4 - t)$.
   - Plugging into $x_1 + x_2 = 2$:
     $$(2 - t) + (4 - t) = 2 \implies 6 - 2t = 2 \implies t = 2$$
   - This gives the point $(2 - 2, 4 - 2) = (0, 2)$.
   - Check if $(0, 2)$ satisfies the remaining constraints $x_1 \ge 0, x_2 \ge 0$: Yes, $0 \ge 0$ and $2 \ge 0$!
   - *(Alternative 1D check)*: On the boundary $x_2 = 2 - x_1$ with $x_1 \in [0, 2]$, minimize squared distance:
     $$D(x_1) = (x_1 - 2)^2 + ((2 - x_1) - 4)^2 = (x_1 - 2)^2 + (x_1 + 2)^2 = 2x_1^2 + 8$$
     Over $x_1 \in [0, 2]$, $2x_1^2 + 8$ is minimized at $x_1 = 0$, giving $x_2 = 2 - 0 = 2$.

> **Final Answer for 1(d):**
> - Unconstrained step: $y^{(1)} = (2, 4)$ (infeasible since $2 + 4 = 6 > 2$).
> - Closest feasible point: **$x^{(1)} = (0, 2)$**.

---

## Part (e): First-Order Optimality Condition on a Convex Set (6 points)

### Question Statement
Let $f : K \to \mathbb{R}$ be a differentiable and convex function defined on a convex domain $K$. Let $x \in K$ be such that for any $y \in K$,
$$\langle \nabla f(x), y - x \rangle \ge 0.$$
Prove that $x$ is a global minimizer of $f$.

---

### Core Concept: First-Order Characterization of Convexity

A differentiable function $f : K \to \mathbb{R}$ on a convex set $K$ is **convex** if and only if its tangent hyperplane at any point $x \in K$ is a global under-estimator of the function:
$$f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle \quad \forall x, y \in K$$

#### Visualization of Tangent Hyperplane and Constrained Minimum
```
      f(y)
       ▲            /
       │           /   f(y) (convex curve)
       │          /
       │         ●──────Tangent line: f(x) + ∇f(x)(y - x)
       │        /|      Slope ≥ 0 into K means tangent goes UP for all y ∈ K!
       │       / |
       └──────★──┴──────────► K
              x  y
         (Boundary of K)
```
Geometrically, $\langle \nabla f(x), y - x \rangle \ge 0$ says that $-\nabla f(x)$ (the direction of steepest descent) points **outward** from $K$—any feasible movement $y - x$ into $K$ makes an acute/right angle with $\nabla f(x)$, so $f$ cannot decrease inside $K$.

---

### Step-by-Step Proof
1. Let $y \in K$ be an arbitrary point in the domain $K$.
2. Since $f$ is differentiable and convex on the convex domain $K$, the first-order convexity inequality holds:
   $$f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle$$
3. By the given hypothesis, $\langle \nabla f(x), y - x \rangle \ge 0$ for all $y \in K$.
4. Substituting this into the inequality above yields:
   $$f(y) \ge f(x) + 0 = f(x)$$
5. Since $f(y) \ge f(x)$ holds for all $y \in K$, $x$ is a global minimizer of $f$ on $K$. $\blacksquare$

---

## Part (f): Vertex Cover Approximation & Matching Bounds (8 points)

### Question Statement
Suppose a greedy $2$-approximation algorithm for Vertex Cover returns a vertex cover of size $20$, and you know that the graph contains a matching of size $8$. What are the strongest lower and upper bound on the size of the minimum vertex cover that follows from this information? Briefly justify your answer.

---

### Core Concept: Relating Matchings, OPT, and $2$-Approximations

Let $\text{OPT}$ be the size of the **Minimum Vertex Cover**, $C$ be the vertex cover returned by the $2$-approximation algorithm ($|C| = 20$), and $M$ be any matching ($|M| = 8$).

1. **From the $2$-Approximation Algorithm ($|C| = 20$):**
   By definition of a $2$-approximation for a minimization problem:
   $$\text{OPT} \le |C| \le 2 \cdot \text{OPT}$$
   Substituting $|C| = 20$:
   $$\text{OPT} \le 20 \quad \text{and} \quad 20 \le 2 \cdot \text{OPT} \implies \text{OPT} \ge 10$$
   So the $2$-approximation alone tells us:
   $$10 \le \text{OPT} \le 20$$

2. **From the Matching ($|M| = 8$):**
   - **Lower Bound:** Since edges in a matching $M$ share no endpoints, any vertex cover must pick at least one vertex from each edge in $M$. Thus:
     $$\text{OPT} \ge |M| = 8$$
     Comparing the two lower bounds $\text{OPT} \ge 10$ and $\text{OPT} \ge 8$, the **stronger (tighter) lower bound is $10$**.
   - **Why $|M| = 8$ does NOT give an upper bound of $16$:**
     Taking both endpoints of a matching gives a vertex cover of size $2|M| = 16$ **only if $M$ is a *maximal* matching!** The problem statement only says *"the graph contains a matching of size 8"* (not necessarily maximal—there could be other edges not touched by $M$). Therefore, $2|M| = 16$ is **not** guaranteed to cover all edges.

---

### Step-by-Step Solution & Justification
- **Upper Bound = $20$:** The algorithm returns a valid vertex cover of size $20$, so the minimum vertex cover has size at most $20$. (Note: Because the matching of size $8$ is not guaranteed to be *maximal*, taking all $16$ of its endpoints does not necessarily form a vertex cover, so $16$ is not a valid upper bound.)
- **Lower Bound = $10$:**
  - Because the algorithm is a $2$-approximation, $|C| \le 2 \cdot \text{OPT} \implies 20 \le 2 \cdot \text{OPT} \implies \text{OPT} \ge 10$.
  - A matching of size $8$ implies $\text{OPT} \ge 8$ (since no vertex can cover two edges of a matching), which is weaker than $\text{OPT} \ge 10$.
- Combining the strongest bounds gives $\text{OPT} \in [10, 20]$.

> **Final Answer for 1(f):** **Lower bound = $10$, Upper bound = $20$**.

---

# Question 2: Approximation Algorithm – Greedy Independent Set (15 points)

### Problem Statement
Let $G = (V, E)$ be an undirected graph with maximum degree $\Delta \ge 1$. An **Independent Set (IS)** is a set $S \subseteq V$ of vertices such that no edge $e \in E$ connects two vertices in $S$. The goal is to find an IS of maximum size.

```
Algorithm 1: Greedy Independent Set
1: S ← ∅
2: while V(G) ≠ ∅ do
3:     Choose an arbitrary vertex v ∈ V(G)
4:     S ← S ∪ {v}
5:     Remove v and all its neighbors from G
6: end while
7: return S
```

---

## Part (a): Prove that the algorithm returns an independent set (5 points)

### Step-by-Step Proof (by Contradiction)
1. Suppose for the sake of contradiction that the returned set $S$ is **not** an independent set.
2. Then there exist two distinct vertices $u, v \in S$ such that $\{u, v\} \in E$.
3. Since the `while` loop adds only one vertex to $S$ per iteration, one of $u$ or $v$ must have been added to $S$ before the other. Without loss of generality, assume $u$ was added to $S$ in an earlier iteration than $v$.
4. In the iteration when $u$ is chosen and added to $S$ (Line 4), Line 5 immediately removes $u$ and **all of its neighbors** from $G$.
5. Because $\{u, v\} \in E$, $v$ is a neighbor of $u$, so $v$ is removed from $V(G)$ during that iteration.
6. Consequently, $v$ is no longer in $V(G)$ in any subsequent iteration and could never have been chosen and added to $S$—contradicting $v \in S$.
7. Therefore, no two vertices in $S$ share an edge, so $S$ is a valid independent set. $\blacksquare$

---

## Part (b): Prove that the algorithm is a $\Delta$-approximation for Maximum Independent Set (8 points)

### Core Concept: Neighborhood Partitioning / Charging Argument

> **Watch out for the $(\Delta + 1)$ trap!**
> A naive argument says: "Each step removes $v$ and at most $\Delta$ neighbors (at most $\Delta+1$ vertices total), so $|S| \ge \frac{|V|}{\Delta+1} \ge \frac{\text{OPT}}{\Delta+1}$." That only proves a $(\Delta+1)$-approximation!
> To prove the tighter **$\Delta$-approximation** ($\text{OPT} \le \Delta |S|$, or $|S| \ge \frac{\text{OPT}}{\Delta}$), we bound how many vertices of $\text{OPT}$ can lie in each removed closed neighborhood $N[v]$.

#### Visualization of the Removed Neighborhood $N[v]$
Suppose in one iteration the algorithm picks $v$ and removes its closed neighborhood $N[v] = \{v\} \cup N(v)$, where $|N(v)| \le \Delta$:
```
            Removed in iteration when v is chosen: N[v]
         ┌───────────────────────────────────────────────┐
         │                      v (chosen by Greedy)     │
         │                    / | \                      │
         │                   /  |  \   (at most Δ edges) │
         │                  u_1 u_2 ... u_Δ              │
         └───────────────────────────────────────────────┘
```
How many vertices from the optimal independent set $S^*$ ($\text{OPT} = |S^*|$) can be inside $N[v]$?
- **Case 1 ($v \in S^*$):** Since $S^*$ is an independent set and $v$ is connected to every $u_i \in N(v)$, **none** of $u_1, \dots, u_\Delta$ can be in $S^*$. Thus $|S^* \cap N[v]| = 1 \le \Delta$ (since $\Delta \ge 1$).
- **Case 2 ($v \notin S^*$):** Then $S^* \cap N[v] \subseteq N(v)$. Since $v$ has at most $\Delta$ neighbors, $|S^* \cap N[v]| \le |N(v)| \le \Delta$.

In **both cases**, at most $\Delta$ vertices of $S^*$ are removed in each iteration!

---

### Step-by-Step Proof
1. Let $S^*$ be a maximum independent set of $G$, so $\text{OPT} = |S^*|$, and let $S = \{v_1, v_2, \dots, v_k\}$ be the set of $k = |S|$ vertices returned by the algorithm.
2. For each $v_i \in S$, define $N[v_i]$ to be the set of vertices removed from $G$ in iteration $i$ (namely $v_i$ and its remaining neighbors in $G$, which is a subset of $v_i$ and its original neighbors in $G$).
3. Because the algorithm terminates only when $V(G) = \emptyset$, every vertex in $V$ (and hence every vertex in $S^*$) belongs to $N[v_i]$ for some $i \in \{1, \dots, k\}$:
   $$S^* = \bigcup_{i=1}^k (S^* \cap N[v_i])$$
4. For any $i \in \{1, \dots, k\}$, consider how many vertices of $S^*$ can be in $N[v_i]$:
   - $N[v_i]$ consists of $v_i$ and at most $\Delta$ neighbors of $v_i$ (since the maximum degree of $G$ is $\Delta$).
   - If $v_i \in S^*$, then no neighbor of $v_i$ can belong to $S^*$ (because $S^*$ is an independent set), so $|S^* \cap N[v_i]| = 1 \le \Delta$ (as $\Delta \ge 1$).
   - If $v_i \notin S^*$, then $S^* \cap N[v_i]$ can only contain neighbors of $v_i$, of which there are at most $\Delta$, so $|S^* \cap N[v_i]| \le \Delta$.
   - Thus, in all cases, $|S^* \cap N[v_i]| \le \Delta$.
5. Summing over all $k = |S|$ iterations:
   $$\text{OPT} = |S^*| = \sum_{i=1}^k |S^* \cap N[v_i]| \le \sum_{i=1}^k \Delta = \Delta |S|$$
6. Rearranging gives $|S| \ge \frac{\text{OPT}}{\Delta}$, proving that the greedy algorithm is a $\Delta$-approximation. $\blacksquare$

---

## Part (c): Tight Family of Graphs Where Algorithm Returns $\text{OPT}/\Delta$ (2 points)

### Core Concept & Visualization: The Star Graph $K_{1, \Delta}$

```
          u_1 (leaf, deg 1)
            \
             \
  u_2 ──────── c (center, deg Δ) ──────── u_3
             /
            /
          u_Δ (leaf, deg 1)

  • Optimal Independent Set S* = {u_1, u_2, ..., u_Δ}  --> OPT = Δ
  • Bad Greedy Choice: Pick center vertex c first!
    --> Removes c and ALL leaves u_1, ..., u_Δ in step 1!
    --> Greedy returns S = {c} of size 1 = OPT / Δ.
```

### Step-by-Step Answer
- **Graph Family:** For any $\Delta \ge 1$, let $G = K_{1, \Delta}$ be the **star graph** with $\Delta + 1$ vertices: one center vertex $c$ connected to $\Delta$ leaf vertices $u_1, u_2, \dots, u_\Delta$ (with no edges among the leaves). The maximum degree of $G$ is $\deg(c) = \Delta$.
- **Optimal Solution:** The set of all $\Delta$ leaves $S^* = \{u_1, \dots, u_\Delta\}$ has no edges between them, so $\text{OPT} = \Delta$.
- **Greedy Algorithm Choice:** In the first iteration, if the greedy algorithm chooses the center vertex $c$, it adds $c$ to $S$ and removes $c$ along with all $\Delta$ of its neighbors $u_1, \dots, u_\Delta$. The graph becomes empty, and the algorithm terminates and returns $S = \{c\}$ of size $1 = \frac{\Delta}{\Delta} = \frac{\text{OPT}}{\Delta}$.

---

# Question 3: Convex Optimization (20 points)

### Problem Statement
Consider running unconstrained gradient descent over $\mathbb{R}^n$ on a convex, $\beta$-smooth function $f : \mathbb{R}^n \to \mathbb{R}$ where $\beta > 0$. Starting at $x_0 \in \mathbb{R}^n$, define the update rule:
$$x_{k+1} = x_k - \frac{1}{\beta} \nabla f(x_k)$$

---

## Core Concepts for Question 3

Before solving (a), (b), and (c), let's review the three fundamental properties of convex, $\beta$-smooth functions used across this problem:

1. **Quadratic Upper Bound ($\beta$-Smoothness):**
   For any $x, y \in \mathbb{R}^n$:
   $$f(y) \le f(x) + \langle \nabla f(x), y - x \rangle + \frac{\beta}{2} \|y - x\|_2^2$$
2. **Co-coercivity of the Gradient (given in Hint 1 of Part (a)):**
   For any convex, $\beta$-smooth function $f$ and any $x, y \in \mathbb{R}^n$:
   $$\langle \nabla f(x) - \nabla f(y), x - y \rangle \ge \frac{1}{\beta} \|\nabla f(x) - \nabla f(y)\|_2^2$$
3. **Sufficient Decrease / Telescoping Sum (given in Hint of Part (b)):**
   Plugging $y = x_{i+1} = x_i - \frac{1}{\beta}\nabla f(x_i)$ into the quadratic upper bound gives:
   $$f(x_{i+1}) \le f(x_i) - \frac{1}{2\beta}\|\nabla f(x_i)\|_2^2 \implies \|\nabla f(x_i)\|_2^2 \le 2\beta\big(f(x_i) - f(x_{i+1})\big)$$
   Summing from $i = 0$ to $k$ telescopes to:
   $$\sum_{i=0}^k \|\nabla f(x_i)\|_2^2 \le 2\beta \big(f(x_0) - f(x_{k+1})\big) \le 2\beta \big(f(x_0) - f(x^*)\big)$$

---

## Part (a): Show $\|\nabla f(x_{k+1})\|_2 \le \|\nabla f(x_k)\|_2$ (8 points)

### Hints Provided
- **Hint 1:** $\langle \nabla f(x) - \nabla f(y), x - y \rangle \ge \frac{1}{\beta} \|\nabla f(x) - \nabla f(y)\|_2^2$.
- **Hint 2:** Plug in $x = x_k$ and $y = x_{k+1} = x_k - \frac{1}{\beta} \nabla f(x_k)$.

### Step-by-Step Proof
Let $g_k = \nabla f(x_k)$ and $g_{k+1} = \nabla f(x_{k+1})$ for clean notation.
1. From the gradient descent update rule $x_{k+1} = x_k - \frac{1}{\beta} g_k$, we have:
   $$x_k - x_{k+1} = \frac{1}{\beta} g_k$$
2. Substitute $x = x_k$ and $y = x_{k+1}$ into the co-coercivity inequality from Hint 1:
   $$\left\langle g_k - g_{k+1}, \frac{1}{\beta} g_k \right\rangle \ge \frac{1}{\beta} \|g_k - g_{k+1}\|_2^2$$
3. Multiply both sides by $\beta > 0$:
   $$\langle g_k - g_{k+1}, g_k \rangle \ge \|g_k - g_{k+1}\|_2^2$$
4. Expand both sides using inner product linearity ($\|u - v\|_2^2 = \|u\|_2^2 - 2\langle u, v \rangle + \|v\|_2^2$):
   $$\|g_k\|_2^2 - \langle g_{k+1}, g_k \rangle \ge \|g_k\|_2^2 - 2\langle g_k, g_{k+1} \rangle + \|g_{k+1}\|_2^2$$
5. Subtract $\|g_k\|_2^2$ and add $2\langle g_k, g_{k+1} \rangle$ to both sides:
   $$\langle g_k, g_{k+1} \rangle \ge \|g_{k+1}\|_2^2$$
6. Apply the **Cauchy-Schwarz Inequality** ($\langle g_k, g_{k+1} \rangle \le \|g_k\|_2 \|g_{k+1}\|_2$):
   $$\|g_{k+1}\|_2^2 \le \langle g_k, g_{k+1} \rangle \le \|g_k\|_2 \|g_{k+1}\|_2$$
7. If $\|g_{k+1}\|_2 = 0$, then $\|\nabla f(x_{k+1})\|_2 = 0 \le \|\nabla f(x_k)\|_2$ holds trivially. Otherwise, divide both sides by $\|g_{k+1}\|_2 > 0$:
   $$\|\nabla f(x_{k+1})\|_2 \le \|\nabla f(x_k)\|_2 \quad \blacksquare$$

---

## Part (b): Prove $\|\nabla f(x_k)\|_2 \le \sqrt{\frac{2\beta}{k+1}(f(x_0) - f(x^*))}$ (6 points)

### Hint Provided
You may use $\sum_{i=0}^k \|\nabla f(x_i)\|_2^2 \le 2\beta (f(x_0) - f(x^*))$ without proof.

### Core Trick: Bounding a Sum Below by $(k+1)$ Times Its Smallest Term
Since Part (a) showed that $\|\nabla f(x_0)\|_2 \ge \|\nabla f(x_1)\|_2 \ge \dots \ge \|\nabla f(x_k)\|_2$, the last term $\|\nabla f(x_k)\|_2^2$ is the **smallest** of the $k+1$ terms in the sum!

```
  ||∇f(x_i)||_2^2
    ▲
    │  ███
    │  ███  ███
    │  ███  ███  ███
    │  ███  ███  ███  ...  ███  ◄── Height ||∇f(x_k)||_2^2
    │  ███  ███  ███  ...  ███
    └───┴────┴────┴─────────┴───► Iteration i
       i=0  i=1  i=2       i=k
       \_____________________/
            k + 1 terms
   Sum of bars ≥ (k + 1) × (height of shortest bar at i = k)
```

### Step-by-Step Proof
1. By Part (a), the sequence of gradient norms is non-increasing: $\|\nabla f(x_{i+1})\|_2 \le \|\nabla f(x_i)\|_2$ for all $i \ge 0$. Since norms are non-negative, their squares are also non-increasing:
   $$\|\nabla f(x_k)\|_2^2 \le \|\nabla f(x_i)\|_2^2 \quad \text{for all } i \in \{0, 1, \dots, k\}$$
2. Summing this inequality from $i = 0$ to $k$ (note there are $k + 1$ terms in total):
   $$(k + 1)\|\nabla f(x_k)\|_2^2 = \sum_{i=0}^k \|\nabla f(x_k)\|_2^2 \le \sum_{i=0}^k \|\nabla f(x_i)\|_2^2$$
3. Applying the inequality from the hint:
   $$(k + 1)\|\nabla f(x_k)\|_2^2 \le 2\beta \big(f(x_0) - f(x^*)\big)$$
4. Divide both sides by $k + 1 > 0$ and take the square root of both sides:
   $$\|\nabla f(x_k)\|_2 \le \sqrt{\frac{2\beta}{k+1}\big(f(x_0) - f(x^*)\big)} \quad \blacksquare$$

---

## Part (c): Show $\|\nabla f(x_k)\|_2 \le \frac{\beta D}{\sqrt{k+1}}$ where $D = \|x_0 - x^*\|_2$ (6 points)

### Hint Provided
Use Part (b) + definition of $\beta$-smooth function.

### Step-by-Step Proof
1. Since $x^* \in \arg\min_{x \in \mathbb{R}^n} f(x)$ is an unconstrained global minimizer of a differentiable function $f$, its gradient vanishes:
   $$\nabla f(x^*) = 0$$
2. By the definition of $\beta$-smoothness applied at base point $x^*$ and target point $x_0$:
   $$f(x_0) \le f(x^*) + \langle \nabla f(x^*), x_0 - x^* \rangle + \frac{\beta}{2}\|x_0 - x^*\|_2^2$$
3. Substitute $\nabla f(x^*) = 0$ and $D = \|x_0 - x^*\|_2$:
   $$f(x_0) \le f(x^*) + 0 + \frac{\beta}{2}D^2 \implies f(x_0) - f(x^*) \le \frac{\beta D^2}{2}$$
4. Substitute this upper bound on $f(x_0) - f(x^*)$ into the inequality from Part (b):
   $$\|\nabla f(x_k)\|_2 \le \sqrt{\frac{2\beta}{k+1} \cdot \frac{\beta D^2}{2}} = \sqrt{\frac{\beta^2 D^2}{k+1}} = \frac{\beta D}{\sqrt{k+1}} \quad \blacksquare$$

---

# Question 4: Approximation Algorithms – Deterministic Rounding for Set Cover (25 points)

*(Note: The header on page 9 prints "30 points" as a typo on the exam sheet, while the cover table and individual parts $6+6+8+5$ sum to **25 points**.)*

### Problem Statement
Let $U = \{u_1, \dots, u_n\}$ be a universe of elements, and let $S_1, \dots, S_m \subseteq U$ be subsets whose union is $U$. Assume that **every element belongs to at most $k$ sets**, where $k \ge 1$. The goal is to select the minimum number of sets whose union is $U$. For each set $S_i$, introduce a variable $x_i$ indicating whether $S_i$ is selected.

---

## Part 1: Write an Integer Linear Program (ILP) for this problem (6 points)

### Core Concept: Translating Combinatorial Set Cover into an ILP
- **Decision Variables:** For each set $S_i$ ($i \in \{1, \dots, m\}$), let $x_i \in \{0, 1\}$, where $x_i = 1$ if $S_i$ is selected and $x_i = 0$ otherwise.
- **Objective Function:** Minimize the total number of selected sets: $\min \sum_{i=1}^m x_i$.
- **Coverage Constraints:** Every element $u_j \in U$ ($j \in \{1, \dots, n\}$) must be covered by at least one selected set. That means the sum of $x_i$ over all sets $S_i$ containing $u_j$ must be at least $1$.

### Complete ILP Formulation
$$\begin{aligned}
\min \quad & \sum_{i=1}^m x_i \\
\text{s.t.} \quad & \sum_{i : u_j \in S_i} x_i \ge 1 \quad \forall j \in \{1, \dots, n\} \\
& x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, m\}
\end{aligned}$$
*(Note: The LP relaxation simply replaces $x_i \in \{0, 1\}$ with $0 \le x_i \le 1$, or $x_i \ge 0$.)*

---

## Part 2: Prove that the Rounded Collection Covers $U$ (6 points)

### Question Statement
Let $x^*$ be an optimal solution to the LP relaxation. Consider the deterministic rounding rule:
$$\hat{x}_i = \begin{cases} 1 & \text{if } x_i^* \ge 1/k, \\ 0 & \text{otherwise.} \end{cases}$$
Prove that the collection $\{S_i \mid \hat{x}_i = 1\}$ covers $U$.

---

### Core Concept: The Pigeonhole / Averaging Principle
Suppose an element $u_j$ appears in $\ell \le k$ sets. In the LP relaxation, the fractional weights $x_i^*$ of those $\ell$ sets must add up to at least $1$:
$$\underbrace{x_{i_1}^* + x_{i_2}^* + \dots + x_{i_\ell}^*}_{\ell \text{ terms, where } \ell \le k} \ge 1$$
Could **all** $\ell$ of these variables be strictly less than $1/k$?
**No!** If every single one had $x_{i_r}^* < 1/k$, their sum would be strictly less than $\ell \cdot \frac{1}{k} \le k \cdot \frac{1}{k} = 1$, violating the LP constraint!

#### Visualization of Threshold Rounding ($k = 3$)
```
  Suppose element u_j is in 3 sets: S_1, S_2, S_3.
  LP constraint requires: x_1* + x_2* + x_3* ≥ 1.

  x_i*
   ▲
   │              ███ (x_2* = 0.50 ≥ 1/3) ──► Rounds to x̂_2 = 1 (Covers u_j!)
1/3┼──────────────███───────────────────────── Threshold = 1/k = 1/3
   │     ███      ███      ███
   │   (0.25)   (0.50)   (0.25)
   └──────┴────────┴────────┴────► Sets containing u_j
         S_1      S_2      S_3
```

---

### Step-by-Step Proof
1. Consider any element $u_j \in U$. Let $I_j = \{i \in \{1, \dots, m\} \mid u_j \in S_i\}$ be the indices of the sets containing $u_j$.
2. By the problem assumption, every element belongs to at most $k$ sets, so $1 \le |I_j| \le k$.
3. Since $x^*$ is a feasible solution to the LP relaxation, it satisfies the coverage constraint for $u_j$:
   $$\sum_{i \in I_j} x_i^* \ge 1$$
4. Because the sum of $|I_j|$ numbers is at least $1$, the maximum of these numbers must be at least their average:
   $$\max_{i \in I_j} x_i^* \ge \frac{1}{|I_j|} \sum_{i \in I_j} x_i^* \ge \frac{1}{|I_j|} \ge \frac{1}{k}$$
   (where the last inequality follows from $|I_j| \le k$).
5. Therefore, there exists at least one index $i^* \in I_j$ such that $x_{i^*}^* \ge 1/k$.
6. By the rounding rule, $\hat{x}_{i^*} = 1$, which means $S_{i^*}$ is included in $\{S_i \mid \hat{x}_i = 1\}$ and covers $u_j$.
7. Since $u_j \in U$ was arbitrary, every element of $U$ is covered. $\blacksquare$

---

## Part 3: Prove that the Rounding Algorithm is a $k$-Approximation (8 points)

### Core Concept: The LP-Rounding Bridge
Every LP rounding approximation proof follows a 3-step chain of inequalities:
$$\text{ALG} = \sum_{i=1}^m \hat{x}_i \;\stackrel{(1)}{\le}\; k \sum_{i=1}^m x_i^* = k \cdot \text{OPT}_{\text{LP}} \;\stackrel{(2)}{\le}\; k \cdot \text{OPT}_{\text{ILP}}$$
1. **Step (1) (Component-wise Rounding Bound):** Each variable $\hat{x}_i$ increases by a factor of **at most $k$** compared to $x_i^*$ ($\hat{x}_i \le k x_i^*$).
2. **Step (2) (LP Relaxation Lower Bound):** Since the LP relaxation expands the feasible region of a minimization problem ($\{0, 1\} \subseteq [0, 1]$), its minimum value is at most the true integral optimum: $\text{OPT}_{\text{LP}} \le \text{OPT}_{\text{ILP}}$.

---

### Step-by-Step Proof
1. Let $\text{OPT}_{\text{ILP}}$ denote the value of an optimal integral solution to the ILP, and let $\text{OPT}_{\text{LP}} = \sum_{i=1}^m x_i^*$ denote the optimal objective value of the LP relaxation.
2. Since every feasible solution to the ILP is also feasible for the LP relaxation (and this is a minimization problem), we have:
   $$\text{OPT}_{\text{LP}} = \sum_{i=1}^m x_i^* \le \text{OPT}_{\text{ILP}}$$
3. Next, we claim that for every $i \in \{1, \dots, m\}$, $\hat{x}_i \le k \cdot x_i^*$:
   - **Case 1 ($\hat{x}_i = 0$):** Since $x_i^* \ge 0$ and $k \ge 1$, $\hat{x}_i = 0 \le k \cdot x_i^*$ holds trivially.
   - **Case 2 ($\hat{x}_i = 1$):** By the rounding rule, $\hat{x}_i = 1$ only when $x_i^* \ge 1/k$. Multiplying both sides by $k$ gives $k \cdot x_i^* \ge 1 = \hat{x}_i$.
4. Summing $\hat{x}_i \le k \cdot x_i^*$ over all $i = 1, \dots, m$, the number of sets selected by the rounding algorithm is:
   $$\text{ALG} = \sum_{i=1}^m \hat{x}_i \le \sum_{i=1}^m k \cdot x_i^* = k \sum_{i=1}^m x_i^* = k \cdot \text{OPT}_{\text{LP}} \le k \cdot \text{OPT}_{\text{ILP}}$$
5. Together with Part 2 (which proved feasibility), this proves the algorithm is a $k$-approximation. $\blacksquare$

---

## Part 4: Construct a Tight Instance for $k = 3$ (5 points)

### Question Statement
Construct an instance with $k = 3$ and an optimal fractional LP solution $x^*$ for which the rounding algorithm selects **three** sets, while an optimal integral solution selects only **one** set. Specify the universe, the sets, and the fractional solution.

---

### Core Idea
If we have $3$ sets that all cover the universe $U$, we can split the fractional weight equally among all $3$ sets: $x^* = (1/3, 1/3, 1/3)$.
- Total fractional cost: $1/3 + 1/3 + 1/3 = 1$, which matches the minimum possible LP cost (since any element needs sum $\ge 1$).
- Because every $x_i^* = 1/3 \ge 1/3$, the rounding rule rounds **all three** sets up to $\hat{x}_i = 1$ (selecting $3$ sets), whereas picking just $S_1$ alone covers $U$ with $1$ set!

### Concrete Construction
- **Universe:** $U = \{u_1\}$ (or $U = \{1, 2, 3\}$).
- **Subsets ($m = 3$):**
  $$S_1 = U, \quad S_2 = U, \quad S_3 = U$$
  Every element in $U$ belongs to $3 \le k$ sets ($k = 3$).
- **Optimal Integral Solution:** Select only $S_1$, i.e., $x_{\text{int}} = (1, 0, 0)$, which covers $U$ using **$1$ set** ($\text{OPT}_{\text{ILP}} = 1$).
- **Optimal Fractional LP Solution:**
  $$x^* = \left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}\right)$$
  - *Why $x^*$ is LP-optimal:* For every element $u \in U$, $x_1^* + x_2^* + x_3^* = \frac{1}{3} + \frac{1}{3} + \frac{1}{3} = 1 \ge 1$ (feasible), and the objective value is $\sum_{i=1}^3 x_i^* = 1$. Since any feasible solution must satisfy $x_1 + x_2 + x_3 \ge 1$, no feasible solution can achieve a smaller objective value than $1$.
- **Rounded Solution:** Since $x_1^* = x_2^* = x_3^* = \frac{1}{3} \ge \frac{1}{3}$, the rounding rule sets:
  $$\hat{x} = (1, 1, 1)$$
  which selects **all $3$ sets** ($\text{ALG} = 3 = 3 \cdot \text{OPT}_{\text{ILP}}$).

---

# Quick Exam-Day Cheat Sheet Summary

1. **Duality & Complementary Slackness (Q1a, Q1b):**
   - Weak Duality: $\text{Max Primal} \le \text{Min Dual}$. Equal values $\implies$ both optimal.
   - Strict inequality in Primal constraint $i$ ($a_i^T x^* < b_i$) $\implies$ Dual variable $y_i^* = 0$.
2. **Active Constraints & Farkas' Lemma (Q1c):**
   - A feasible point $x^*$ is optimal iff $c = \sum_{i \in S} \lambda_i a_i$ for some $\lambda_i \ge 0$ (where $S$ is the set of tight constraints). Otherwise, there is a feasible improving direction $v$.
3. **Projected Gradient Descent & Convexity (Q1d, Q1e, Q3):**
   - PGD step: $y = x^{(0)} - \eta \nabla f(x^{(0)})$, then project orthogonally onto violated constraint boundary.
   - First-order convexity: $f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle$.
   - $\beta$-smoothness at $x^*$ (where $\nabla f(x^*) = 0$): $f(x_0) - f(x^*) \le \frac{\beta}{2}\|x_0 - x^*\|_2^2$.
4. **Approximation Algorithms (Q1f, Q2, Q4):**
   - Vertex cover $2$-approx returning $20 \implies \text{OPT} \in [10, 20]$; non-maximal matching $M$ only gives $\text{OPT} \ge |M|$.
   - Greedy IS removes $N[v]$ per step; at most $\Delta$ vertices of $\text{OPT}$ can be in $N[v] \implies \text{OPT} \le \Delta |S|$.
   - Set Cover with frequency $\le k$: at least one set covering $u_j$ has $x_i^* \ge 1/k$, and $\hat{x}_i \le k x_i^* \implies \text{ALG} \le k \cdot \text{OPT}_{\text{LP}} \le k \cdot \text{OPT}_{\text{ILP}}$.







