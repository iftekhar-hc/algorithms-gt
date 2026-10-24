# Study Guide: Question 2 — Linear Programming (Polygon & Matching)
**Course:** CS 6515 / 4540 (Practice Exam 2 — Section 2: Linear Programming, 25 Points)

---

# Part I: Question 2.1 — Convex Polygons, Norms, and LP Linearization (10 Points)

## 1. The Exam Problem Statement (2.1 Polygon)

> **Problem 2.1 (Polygon — 10 points):** Let $P$ be a convex polygon given by
> $$a_i x + b_i y \le c_i \quad (i = 1, \dots, m).$$
> Given a fixed point $q = (x_0, y_0)$, find $p = (x_1, y_1) \in P$ minimizing
> $$\|p - q\|_\infty = \max\{|x_1 - x_0|, |y_1 - y_0|\}.$$
> Formulate a Linear Program that computes the minimum $L_\infty$ distance from $q$ to $P$.
> *(Hint: Introduce $t$ with $|x_1 - x_0| \le t, |y_1 - y_0| \le t$ and linearize.)*

---

## 2. Core Concepts for Problem 2.1

### 2.1 Half-Spaces and Convex Polygons (H-Representation)
- **Linear Inequality as a Half-Space:**
  In $\mathbb{R}^2$, a single linear equation $a_i x + b_i y = c_i$ defines a **straight line**.
  The linear inequality
  $$a_i x + b_i y \le c_i$$
  defines a **closed half-plane (half-space)**—all points on one side of that line (including the boundary line itself).
- **Convex Set:**
  A set $S$ is **convex** if for any two points $u, v \in S$, the entire line segment connecting them lies inside $S$.
- **Convex Polygon / Polyhedron:**
  - Every half-space is a convex set.
  - The **intersection of any finite number of half-spaces** is also a convex set, called a **convex polyhedron** (or in 2D, when bounded, a **convex polygon** $P$):
    $$P = \{ (x_1, y_1) \in \mathbb{R}^2 \mid a_i x_1 + b_i y_1 \le c_i \text{ for all } i = 1, \dots, m \}.$$
  - Each inequality $a_i x_1 + b_i y_1 \le c_i$ forms one flat side (edge) of the polygon $P$.
  - **Why this matters for LP:** Membership $p = (x_1, y_1) \in P$ is already a set of $m$ linear constraints!

*(Connection to Short Answer Q1.1 on the exam: A polyhedron is the intersection of finitely many half-spaces, which has flat sides. However, not every convex set is a polyhedron—for example, a circle/disk $x^2 + y^2 \le 1$ is convex but requires infinitely many tangent half-spaces!)*

---

### 2.2 Vector Norms and Distance Metrics ($L_1, L_2, L_\infty$)
Given two points $p = (x_1, y_1)$ and $q = (x_0, y_0)$ in $\mathbb{R}^2$, the difference vector is $p - q = (x_1 - x_0, \; y_1 - y_0)$. How do we measure the "distance" between $p$ and $q$?

| Norm | Formula in 2D | Geometric "Unit Ball" ($\|p - q\| \le t$) | Can it be solved via LP? |
| :--- | :--- | :--- | :--- |
| **$L_2$ (Euclidean)** | $\|p - q\|_2 = \sqrt{(x_1 - x_0)^2 + (y_1 - y_0)^2}$ | Circle of radius $t$ | **No** (quadratic/curved, not linear) |
| **$L_1$ (Manhattan / Taxicab)** | $\|p - q\|_1 = |x_1 - x_0| + |y_1 - y_0|$ | Diamond (rotated square) | **Yes!** (piecewise linear) |
| **$L_\infty$ (Chebyshev / Max)** | $\|p - q\|_\infty = \max\{|x_1 - x_0|, |y_1 - y_0|\}$ | Axis-aligned Square of half-width $t$ | **Yes!** (piecewise linear) |

- **Geometric Intuition of Problem 2.1:**
  The set of points within $L_\infty$ distance $t$ of $q = (x_0, y_0)$ is an **axis-aligned square** centered at $(x_0, y_0)$ with side length $2t$:
  $$[x_0 - t, \; x_0 + t] \times [y_0 - t, \; y_0 + t].$$
  Minimizing $\|p - q\|_\infty$ subject to $p \in P$ means starting with $t = 0$ at $q$ and **inflating this square** until it first touches the polygon $P$!

---

### 2.3 Linearization Techniques (How to Turn Non-Linear $\max$ and $|\cdot|$ into an LP)

In a **Linear Program (LP)**, the objective function and all constraints must be strictly **linear** combinations of the decision variables (no $\max\{\cdot\}$, no $|\cdot|$, no squares).

First, identify **what is fixed (constants)** vs. **what we are solving for (decision variables)**:
- **Constants (given inputs):** $x_0, y_0$ and $a_i, b_i, c_i$ for $i = 1, \dots, m$.
- **Decision Variables:** $x_1, y_1$ (the coordinates of point $p \in P$) and an auxiliary variable $t \in \mathbb{R}$.

#### Trick 1: Linearizing a Minimax Objective ($\min \max\{A, B\}$) — The "Epigraph" Trick
We want to minimize $\max\{|x_1 - x_0|, |y_1 - y_0|\}$.
- Introduce a single new scalar decision variable **$t$** representing the upper bound on the maximum.
- Notice that:
  $$\max\{A, B\} \le t \quad \Longleftrightarrow \quad A \le t \;\;\text{AND}\;\; B \le t.$$
- Why does minimizing $t$ subject to $A \le t$ and $B \le t$ give $t^* = \max\{A, B\}$?
  Because $t$ is forced to be at least as large as *both* $A$ and $B$ (so $t \ge \max\{A, B\}$), and since the objective **minimizes $t$**, at the optimum $t$ will be pushed down until it equals $\max\{A, B\}$!
- Applying this to our problem gives:
  $$\begin{aligned}
  \min \quad & t \\
  \text{s.t.} \quad & |x_1 - x_0| \le t \\
  & |y_1 - y_0| \le t.
  \end{aligned}$$

#### Trick 2: Linearizing Absolute Value Upper Bounds ($|u| \le t$)
An absolute value inequality $|u| \le t$ is equivalent to two simultaneous linear inequalities:
$$|u| \le t \quad \Longleftrightarrow \quad -t \le u \le t \quad \Longleftrightarrow \quad \begin{cases} u \le t \\ -u \le t \end{cases}$$
*(Note: Having both $u \le t$ and $-u \le t$ automatically forces $2t \ge u + (-u) = 0 \implies t \ge 0$!)*

Applying this to $u = x_1 - x_0$ and $u = y_1 - y_0$:
1. $|x_1 - x_0| \le t \iff$
   - $x_1 - x_0 \le t \quad (\text{or } x_1 - t \le x_0)$
   - $-(x_1 - x_0) \le t \iff x_0 - x_1 \le t \quad (\text{or } -x_1 - t \le -x_0)$
2. $|y_1 - y_0| \le t \iff$
   - $y_1 - y_0 \le t \quad (\text{or } y_1 - t \le y_0)$
   - $-(y_1 - y_0) \le t \iff y_0 - y_1 \le t \quad (\text{or } -y_1 - t \le -y_0)$

#### Step 3: Include the Polygon Membership Constraints ($p \in P$)
Since $p = (x_1, y_1)$ must lie inside the convex polygon $P$, $(x_1, y_1)$ must satisfy all $m$ half-space inequalities:
$$a_i x_1 + b_i y_1 \le c_i \quad \text{for } i = 1, \dots, m.$$

---

### 2.4 Model Exam Solution for Problem 2.1 (Polygon — 10 points)

> **Solution:**
> **Decision Variables:** $x_1, y_1, t \in \mathbb{R}$ (where $p = (x_1, y_1) \in P$ is the point in the polygon and $t$ bounds the $L_\infty$ distance).
> *(Note: $x_1, y_1$ are unrestricted in sign, and $t \ge 0$ is implied by the constraints below.)*
>
> **Linear Program:**
> $$\begin{aligned}
> \min_{x_1, y_1, t} \quad & t \\
> \text{s.t.} \quad & x_1 - x_0 \le t \\
> & x_0 - x_1 \le t \\
> & y_1 - y_0 \le t \\
> & y_0 - y_1 \le t \\
> & a_i x_1 + b_i y_1 \le c_i \quad \text{for } i = 1, \dots, m \\
> & t \ge 0.
> \end{aligned}$$
> *(Equivalently, putting variables on the LHS and constants on the RHS:)*
> $$\begin{aligned}
> \min_{x_1, y_1, t} \quad & t \\
> \text{s.t.} \quad & x_1 - t \le x_0 \\
> & -x_1 - t \le -x_0 \\
> & y_1 - t \le y_0 \\
> & -y_1 - t \le -y_0 \\
> & a_i x_1 + b_i y_1 \le c_i \quad \text{for } i = 1, \dots, m.
> \end{aligned}$$

---

### 2.5 Common Exam Variations to Watch Out For!
1. **What if the problem asked for the $L_1$ (Manhattan) distance $\|p - q\|_1 = |x_1 - x_0| + |y_1 - y_0|$?**
   - Introduce **two** auxiliary variables: $t_x$ for $|x_1 - x_0|$ and $t_y$ for $|y_1 - y_0|$.
   - **Objective:** $\min \; t_x + t_y$
   - **Constraints:**
     - $x_1 - x_0 \le t_x$ and $x_0 - x_1 \le t_x$
     - $y_1 - y_0 \le t_y$ and $y_0 - y_1 \le t_y$
     - $a_i x_1 + b_i y_1 \le c_i \quad \forall i = 1, \dots, m$.
2. **Why doesn't this trick work for MAXIMIZING distance ($\max \|p - q\|_\infty$)?**
   - If you tried $\max t$ subject to $x_1 - x_0 \le t$, you could make $t \to +\infty$ without changing $x_1$!
   - Also, for $|u| \ge t$, that means $u \ge t$ **OR** $-u \ge t$. An **OR** condition is a union of half-spaces, which is **non-convex** and cannot be written as linear inequalities in a single LP.

---
---

# Part II: Question 2.2 — Matchings, LP Relaxation, Integrality Gap, and Duality (15 Points)

## 3. The Exam Problem Statement (2.2 Matching)

> **Problem 2.2 (Matching — 15 points):** Consider the (non-bipartite) maximum matching LP relaxation on $G = (V, E)$ with $\delta(v)$ denoting all the edges incident to any vertex $v \in V$:
> $$\max \sum_{e \in E} x_e \quad \text{s.t.} \quad \sum_{e \in \delta(v)} x_e \le 1 \;\;\forall v \in V, \qquad x_e \ge 0 \;\;\forall e \in E.$$
> - **(a) LP Relaxation (5 pts):** Prove that for any graph $G = (V, E)$, the optimal value of this LP relaxation is at least the size of the maximum matching in $G$.
> - **(b) Integrality Gap (5 pts):** Give an example of a graph $G$ where the LP relaxation value is strictly more than the size of the maximum matching on $G$. *(Hint: There is a graph already on just 3 vertices.)*
> - **(c) Dual of the LP (5 pts):** Write the dual of the above max-matching LP relaxation.

---

## 4. Foundational Concepts for Problem 2.2

### 4.1 Graphs and Incidence Notation $\delta(v)$
- Let $G = (V, E)$ be an undirected graph with vertex set $V$ and edge set $E$.
- For any vertex $v \in V$, **$\delta(v)$** denotes the set of edges **incident** to $v$ (all edges having $v$ as an endpoint):
  $$\delta(v) = \{ e \in E \mid v \in e \}.$$
- **Crucial observation:** Every edge $e = (u, v) \in E$ has **two** endpoints, $u$ and $v$. Therefore, edge $e$ appears in **exactly two** vertex constraint sums: $\delta(u)$ and $\delta(v)$.

### 4.2 What is a Matching?
- A **matching** $M \subseteq E$ is a subset of edges such that **no two edges share a common vertex**.
- Equivalently, every vertex $v \in V$ has **at most one** incident edge in $M$:
  $$|M \cap \delta(v)| \le 1 \quad \forall v \in V.$$
- A **maximum matching** $M^*$ is a matching of maximum cardinality $|M^*|$.

### 4.3 Bipartite Graphs vs. Non-Bipartite (General) Graphs
- A graph $G = (V, E)$ is **bipartite** if $V$ can be partitioned into two disjoint sets $L, R$ such that every edge connects a vertex in $L$ to a vertex in $R$.
- **Characterization Theorem:** A graph is bipartite $\iff$ it contains **no odd cycles** (cycles of length $3, 5, 7, \dots$).
- **Why does this distinction matter for LP relaxations?**
  - **In Bipartite Graphs:** The LP relaxation of maximum matching is **exact** ($\text{OPT}_{\text{LP}} = \text{Max Matching}$), because the vertex-edge incidence matrix of a bipartite graph is *totally unimodular*, guaranteeing integral $(0/1)$ corner points.
  - **In Non-Bipartite Graphs:** Odd cycles (like $K_3$) create **fractional corner points** ($x_e = 1/2$ on every edge of an odd cycle), causing $\text{OPT}_{\text{LP}} > \text{Max Matching}$.

---

## 5. From Integer Program (ILP) to LP Relaxation (Part (a))

### 5.1 Exact ILP vs. LP Relaxation
Assign binary variable $x_e \in \{0, 1\}$ to each edge $e \in E$ ($1$ if $e \in M$, $0$ otherwise):
- **Exact ILP:** $\max \sum_{e \in E} x_e$ s.t. $\sum_{e \in \delta(v)} x_e \le 1 \;\forall v \in V$, and $x_e \in \{0, 1\} \;\forall e \in E$.
- **LP Relaxation:** Replace $x_e \in \{0, 1\}$ with $x_e \ge 0$.
  *(Note: $x_e \le 1$ is automatically implied because $\sum_{e' \in \delta(u)} x_{e'} \le 1$ and $x_{e'} \ge 0$.)*

### 5.2 Why $\text{OPT}_{\text{LP}} \ge \text{OPT}_{\text{ILP}}$
Relaxing $x_e \in \{0, 1\}$ to $x_e \ge 0$ **expands** the feasible region: every valid integer matching is also a valid fractional matching. Maximizing the same objective over a superset yields a value at least as large.

---

## 6. Integrality Gap & Odd Cycles (Part (b))

Consider the triangle graph $G = K_3$ on 3 vertices $V = \{u, v, w\}$ with 3 edges $E = \{(u,v), (v,w), (w,u)\}$:
1. **Maximum Matching ($|M^*| = 1$):** Any two edges share a vertex, so at most 1 edge can be chosen.
2. **LP Relaxation ($\text{OPT}_{\text{LP}} = 1.5$):** Set $x_e = 1/2$ on all 3 edges. Each vertex has two incident edges, so $\sum_{e \in \delta(v)} x_e = 1/2 + 1/2 = 1 \le 1$. Objective value $= 1/2 + 1/2 + 1/2 = 1.5 > 1$.

---

## 7. LP Duality & Minimum Vertex Cover (Part (c))

| Primal (Max Fractional Matching) | Dual (Min Fractional Vertex Cover) |
| :--- | :--- |
| Objective: $\max \sum_{e \in E} 1 \cdot x_e$ | Objective: $\min \sum_{v \in V} 1 \cdot y_v$ |
| 1 constraint per vertex $v \in V$: $\sum_{e \in \delta(v)} x_e \le 1$ | 1 variable per vertex $v \in V$: $y_v \ge 0$ |
| 1 variable per edge $e = (u,v) \in E$: $x_e \ge 0$ | 1 constraint per edge $e = (u,v) \in E$: $y_u + y_v \ge 1$ |

### Model Exam Solutions for Problem 2.2 (Matching — 15 points)

- **Part (a) (5 pts):** Let $M^* \subseteq E$ be a maximum matching in $G$. Define $x^*_e = 1$ if $e \in M^*$ and $0$ otherwise. Then $x^*_e \ge 0$, and since $M^*$ is a matching, at most one edge in $M^*$ is incident to any $v \in V$, so $\sum_{e \in \delta(v)} x^*_e = |M^* \cap \delta(v)| \le 1$. Thus $x^*$ is feasible for the LP with objective value $\sum_{e \in E} x^*_e = |M^*|$. Since the LP maximizes over all feasible solutions, $\text{OPT}_{\text{LP}} \ge |M^*|$.
- **Part (b) (5 pts):** Let $G = K_3$ (triangle on 3 vertices $V=\{1,2,3\}$). Any two edges share a vertex, so the maximum matching has size **$1$**. In the LP, setting $x_e = 1/2$ for all 3 edges satisfies $\sum_{e \in \delta(v)} x_e = 1/2 + 1/2 = 1 \le 1$ for every vertex and achieves LP objective value $3 \times (1/2) = \mathbf{1.5} > 1$.
- **Part (c) (5 pts):** Introducing dual variable $y_v$ for each vertex $v \in V$:
  $$\min \sum_{v \in V} y_v \quad \text{s.t.} \quad y_u + y_v \ge 1 \;\;\forall e = (u, v) \in E, \quad y_v \ge 0 \;\;\forall v \in V.$$

---

# Part III: Comprehensive Self-Assessment Questions

### Questions on Problem 2.1 (Polygon & Norms)
1. **Variables vs. Constants:** In Problem 2.1, why is $a_i x_1 + b_i y_1 \le c_i$ considered a *linear* constraint, and what would make it non-linear? Which symbols in the LP are decision variables, and which are given constants?
2. **Concrete Calculation:** Suppose $P$ is the square $[0, 2] \times [0, 2]$ (defined by $x_1 \le 2, -x_1 \le 0, y_1 \le 2, -y_1 \le 0$) and the query point is $q = (5, 3)$.
   - What is the closest point $p = (x_1, y_1) \in P$ to $q$ in $L_\infty$ norm?
   - What is the optimal value $t^*$ of the LP? Is the optimal point $p \in P$ unique in the $L_\infty$ norm here?
3. **$L_1$ Distance Formulation:** How would you modify the LP in Problem 2.1 if the exam instead asked you to minimize the **$L_1$ (Manhattan) distance** $\|p - q\|_1 = |x_1 - x_0| + |y_1 - y_0|$ for $p \in P$?
4. **Why Not $L_2$ or Maximization?**
   - (a) Why can't we use the same trick to write a Linear Program for the Euclidean distance $\|p - q\|_2 = \sqrt{(x_1 - x_0)^2 + (y_1 - y_0)^2}$?
   - (b) What goes wrong if we just change $\min t$ to $\max t$ in our LP from Problem 2.1 to try to find the *farthest* point in $P$ from $q$?

### Questions on Problem 2.2 (Matching & Duality)
5. **Missing Constraint:** Why doesn't the Max-Matching LP need the explicit constraint $x_e \le 1$?
6. **Bipartite vs. Odd Cycle:** What is the maximum matching size and optimal LP value for $C_4$ (square) vs. $C_5$ (pentagon)?
7. **Dual Optimality Proof:** How can you use a feasible solution to the Dual LP in 2.2(c) to prove that $\text{OPT}_{\text{LP}}$ on $K_3$ cannot exceed $1.5$?
8. **Weighted $b$-Matching Dual:** If the primal LP is $\max \sum_{e \in E} w_e x_e$ subject to $\sum_{e \in \delta(v)} x_e \le b_v$ and $x_e \ge 0$, what is its Dual LP?
