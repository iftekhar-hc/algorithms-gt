# CS 6515 Graduate Algorithms — Lecture 9: Linear Programming: Models and Geometry

This document provides a comprehensive study guide, mathematical explanations, geometric visualizations, algorithms, practice questions, and textbook references based on Lecture 9 of CS 6515.

---

## 1. Overview and Core Mathematical Models

Linear programming (LP) optimizes a linear objective function subject to linear equality and non-strict linear inequality constraints over continuous, real-valued variables.

### Canonical Maximization Form
The canonical maximization form is defined as:

$$\begin{aligned}
\max \quad & \mathbf{c}^\top \mathbf{x} \\
\text{subject to} \quad & A\mathbf{x} \le \mathbf{b} \\
& \mathbf{x} \ge \mathbf{0}
\end{aligned}$$

where:
- $\mathbf{x} \in \mathbb{R}^n$ is the column vector of decision variables: $\mathbf{x} = [x_1, x_2, \dots, x_n]^\top$.
- $\mathbf{c} \in \mathbb{R}^n$ is the objective coefficient vector.
- $A \in \mathbb{R}^{m \times n}$ is the constraint matrix, where row $j$ corresponds to $\sum_{i=1}^n A_{ji} x_i \le b_j$.
- $\mathbf{b} \in \mathbb{R}^m$ is the right-hand side capacity/resource vector.
- Inequalities are interpreted componentwise.

### Feasible Region
The feasible region $\mathcal{P}$ is the set of all points satisfying every constraint simultaneously:

$$\mathcal{P} = \{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} \le \mathbf{b}, \; \mathbf{x} \ge \mathbf{0}\}$$

An optimal solution $\mathbf{x}^* \in \mathcal{P}$ satisfies $\mathbf{c}^\top \mathbf{x}^* \ge \mathbf{c}^\top \mathbf{x}$ for all $\mathbf{x} \in \mathcal{P}$.

---

## 2. Motivating Examples

### The Smoothie Production Problem
A shop produces three smoothie recipes ($x_1, x_2, x_3$) with limited ingredients:
- Oranges: 3 units
- Bananas: 10 units
- Strawberries: 6 units

The ingredient consumption and revenue per liter are summarized below:

| Smoothie | Oranges (units/L) | Bananas (units/L) | Strawberries (units/L) | Revenue (\$/L) |
| :--- | :--- | :--- | :--- | :--- |
| **Smoothie 1 ($x_1$)** | 1 | 2 | 0 | \$5 |
| **Smoothie 2 ($x_2$)** | 0 | 1 | 2 | \$4 |
| **Smoothie 3 ($x_3$)** | 1 | 1 | 1 | \$6 |

The formulation is:

$$\begin{aligned}
\max \quad & 5x_1 + 4x_2 + 6x_3 \\
\text{s.t.} \quad & x_1 + x_3 \le 3 && \text{(Oranges)} \\
& 2x_1 + x_2 + x_3 \le 10 && \text{(Bananas)} \\
& 2x_2 + x_3 \le 6 && \text{(Strawberries)} \\
& x_1, x_2, x_3 \ge 0
\end{aligned}$$

In canonical matrix form:

$$\mathbf{c} = \begin{bmatrix} 5 \\ 4 \\ 6 \end{bmatrix}, \quad A = \begin{bmatrix} 1 & 0 & 1 \\ 2 & 1 & 1 \\ 0 & 2 & 1 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 3 \\ 10 \\ 6 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$

- **Feasible Solution:** Setting $\mathbf{x} = (3, 3, 0)$ gives value $5(3) + 4(3) + 6(0) = 27$. This establishes a lower bound $\text{OPT} \ge 27$.
- **Integer Program Difference:** If smoothies must be sold in whole-unit containers ($x_i \in \mathbb{Z}_{\ge 0}$), the problem becomes an Integer Linear Program (ILP), which is NP-hard.

---

### Maximum Network Flow as an LP
For a directed network $G=(V, E)$ with edge capacities $c_e$ and source-sink pair $(s, t)$, maximum flow is expressed as an LP over edge variables $f_e$:

$$\begin{aligned}
\max \quad & \sum_{(s, v) \in E} f_{sv} - \sum_{(v, s) \in E} f_{vs} \\
\text{s.t.} \quad & \sum_{(u, v) \in E} f_{uv} = \sum_{(v, w) \in E} f_{vw} \quad \forall v \in V \setminus \{s, t\} && \text{(Conservation)} \\
& 0 \le f_e \le c_e \quad \forall e \in E && \text{(Capacities)}
\end{aligned}$$

Because the constraint matrix of directed network flows is totally unimodular, integral capacities guarantee an integral optimal solution.

---

## 3. LP Transformations and Equivalence

Any general linear program can be translated into canonical form using polynomial transformations:

| Original Formulation Feature | Canonical Form Equivalent |
| :--- | :--- |
| **Minimization:** $\min \mathbf{c}^\top \mathbf{x}$ | $\max (-\mathbf{c})^\top \mathbf{x}$, then negate the optimal objective value |
| **Greater-than inequality:** $\mathbf{a}_i^\top \mathbf{x} \ge d_i$ | Negate both sides: $(-\mathbf{a}_i)^\top \mathbf{x} \le -d_i$ |
| **Equality constraint:** $\mathbf{a}_i^\top \mathbf{x} = d_i$ | Replace with two inequalities: $\mathbf{a}_i^\top \mathbf{x} \le d_i$ and $-\mathbf{a}_i^\top \mathbf{x} \le -d_i$ |
| **Unrestricted variable:** $z \in \mathbb{R}$ | Substitute $z = z^+ - z^-$, with $z^+ \ge 0, z^- \ge 0$ |
| **Slack form:** $A\mathbf{x} \le \mathbf{b}$ | Add non-negative slacks: $A\mathbf{x} + \mathbf{s} = \mathbf{b}, \mathbf{s} \ge \mathbf{0}$ |

### What is NOT a Linear Program?
- Strict inequalities: e.g., $x < 1$ (the supremum may exist, but no maximizing point is attained).
- Multiplicative terms: e.g., $x_1 x_2 \le 1$.
- Non-linear objectives: e.g., $\max (x_1^2 + x_2^2)$.
- Discrete domain constraints: e.g., $x_i \in \{0, 1\}$.

---

## 4. Polyhedral Geometry and Vertices

### Convexity of Feasible Regions
A set $\mathcal{P} \subseteq \mathbb{R}^n$ is convex if:

$$\forall \mathbf{x}, \mathbf{y} \in \mathcal{P}, \; \forall \lambda \in [0, 1]: \quad \lambda \mathbf{x} + (1-\lambda)\mathbf{y} \in \mathcal{P}$$

**Theorem:** The feasible region $\mathcal{P} = \{\mathbf{x} : A\mathbf{x} \le \mathbf{b}, \mathbf{x} \ge \mathbf{0}\}$ is convex.

*Proof:*
Let $\mathbf{x}, \mathbf{y} \in \mathcal{P}$ and $\lambda \in [0, 1]$. Then:

$$A(\lambda \mathbf{x} + (1-\lambda)\mathbf{y}) = \lambda A\mathbf{x} + (1-\lambda)A\mathbf{y} \le \lambda \mathbf{b} + (1-\lambda)\mathbf{b} = \mathbf{b}$$

Nonnegativity is similarly preserved: $\lambda \mathbf{x} + (1-\lambda)\mathbf{y} \ge \mathbf{0}$.

---

### Geometric Visualization (2D Triangle Example)
Consider:

$$\begin{aligned}
\max \quad & 2x_1 + 3x_2 \\
\text{s.t.} \quad & x_1 + x_2 \le 5 \\
& x_1 \ge 1 \iff -x_1 \le -1 \\
& x_2 \ge 0
\end{aligned}$$

```text
x2 ^
   |
 4 |   (1,4) Optimal Point (Value = 14)
   |    * \
 3 |    |  \
   |    |   \
 2 |    |    \   Feasible Region P
   |    |     \
 1 |    |      \
   |    |       \
 0 +----+--------*--------> x1
   0    1 (1,0)  5 (5,0)
```

- Level sets of the objective are lines $2x_1 + 3x_2 = q$.
- The gradient vector $\mathbf{c} = (2, 3)$ defines the direction of steepest increase.
- Moving the level line in direction $\mathbf{c}$ reaches the maximum feasible value $q = 14$ at vertex $(1, 4)$.

---

### Vertices and Basic Feasible Solutions
- **Tight Constraint:** An inequality $\mathbf{a}_i^\top \mathbf{x} \le b_i$ is tight at $\mathbf{x}$ if $\mathbf{a}_i^\top \mathbf{x} = b_i$.
- **Vertex (Basic Feasible Solution):** A feasible point $\mathbf{x} \in \mathbb{R}^n$ is a vertex if the normal vectors of its tight constraints contain a linearly independent subset of size $n$ (spanning $\mathbb{R}^n$).
- **Fundamental Theorem of Linear Programming:** Every feasible and bounded LP in canonical form attains its optimum at a vertex.

#### Three Possible LP Outcomes:
1. **Infeasible:** $\mathcal{P} = \emptyset$ (e.g., $x \ge 2$ and $x \le 1$).
2. **Unbounded Objective:** Feasible points achieve arbitrarily large objective values (e.g., $\max x$ s.t. $x \ge 0$). An unbounded feasible region does not necessarily imply an unbounded objective (e.g., $\max -x$ s.t. $x \ge 0$ has optimal value 0).
3. **Feasible with Finite Optimum:** Attains its optimum at one or more vertices.

---

## 5. Algorithmic Solvability and Bit Complexity

- **Polynomial-Time Solvability:** Linear programs can be solved in polynomial time relative to their total binary encoding length using interior-point or ellipsoid methods.
- **Cramer's Rule & Solution Bit Length:** At any vertex, $n$ linearly independent tight constraints form a non-singular system $B\mathbf{x} = \mathbf{d}$. By Cramer's rule:

$$x_i = \frac{\det(B_i)}{\det(B)}$$

Because determinants of integer submatrices grow polynomially with bit length, vertex coordinates can be represented using polynomially bounded bit lengths.

---

## 6. Optimality Certificates and Duality

To certify that a candidate solution $\mathbf{x}^* = (3, 3, 0)$ with objective value 27 is optimal for the smoothie problem, construct a matching upper bound:

Multiply the orange constraint by $y_1 = 5$, banana constraint by $y_2 = 0$, and strawberry constraint by $y_3 = 2$:

$$5(x_1 + x_3) + 0(2x_1 + x_2 + x_3) + 2(2x_2 + x_3) \le 5(3) + 0(10) + 2(6)$$

$$5x_1 + 4x_2 + 7x_3 \le 27$$

Since $x_3 \ge 0$, the objective function satisfies:

$$5x_1 + 4x_2 + 6x_3 \le 5x_1 + 4x_2 + 7x_3 \le 27$$

Thus:

$$\text{Lower Bound } (27) \le \text{OPT} \le 27 \text{ (Upper Bound)} \implies \text{OPT} = 27$$

Finding the optimal multipliers $\mathbf{y} \ge \mathbf{0}$ defines the **Dual LP**:

$$\begin{aligned}
\min \quad & \mathbf{b}^\top \mathbf{y} \\
\text{s.t.} \quad & A^\top \mathbf{y} \ge \mathbf{c} \\
& \mathbf{y} \ge \mathbf{0}
\end{aligned}$$

---

## 7. Algorithms and Pseudocode

### Vertex Verification Algorithm

```text
Algorithm Check-If-Vertex(A, b, x, n, m)
Input: Matrix A (m x n), Vector b (m), Candidate x (n)
Output: Boolean (True if x is a vertex, False otherwise)

1. For j = 1 to m:
2.     If dot_product(A[j], x) > b[j]:
3.         return False
4. For i = 1 to n:
5.     If x[i] < 0:
6.         return False

7. Active_Normals = []
8. For j = 1 to m:
9.     If dot_product(A[j], x) == b[j]:
10.        Active_Normals.append(A[j])

11. For i = 1 to n:
12.    If x[i] == 0:
13.        Let e_i be standard basis vector in R^n
14.        Active_Normals.append(-e_i)

15. If rank(Active_Normals) == n:
16.    return True
17. Else:
18.    return False
```

### Naive Vertex Enumeration Solver

```text
Algorithm Naive-Vertex-Solver(c, A, b, n, m)
Input: Objective c (n), Constraints A (m x n), RHS b (m)
Output: Optimal vertex x* and value, or Infeasible

1. Form combined constraint matrix:
      M = [ A ; -I_n ]  (size (m + n) x n)
      h = [ b ;  0_n ]  (size (m + n))

2. Best_Val = -infinity
3. Best_x = NULL

4. For each subset S of {1, 2, ..., m + n} with |S| == n:
5.     M_S = rows of M indexed by S
6.     h_S = entries of h indexed by S
7.     
8.     If det(M_S) != 0:
9.         x_candidate = solve_linear_system(M_S, h_S)
10.        
11.        // Check feasibility against all (m + n) inequalities
12.        If M * x_candidate <= h:
13.            val = dot_product(c, x_candidate)
14.            If val > Best_Val:
15.                Best_Val = val
16.                Best_x = x_candidate

17. If Best_x == NULL:
18.    return "Infeasible"
19. Else:
20.    return Best_x, Best_Val
```

---

## 8. Quiz and Exam Questions

### Conceptual Quiz

1. **Question:** Can an LP have an unbounded feasible region but still have a finite optimal objective value?
   - **Answer:** Yes. For example, $\max -x$ subject to $x \ge 0$. The feasible region $[0, \infty)$ is unbounded, but the maximum value is $0$ at $x = 0$.

2. **Question:** What is the maximum number of basic solutions in an LP with $n$ variables and $m$ inequalities $A\mathbf{x} \le \mathbf{b}$ plus nonnegativity $\mathbf{x} \ge \mathbf{0}$?
   - **Answer:** $\binom{m+n}{n}$, which is the number of ways to select $n$ tight boundary hyperplanes from the $m+n$ total half-spaces.

3. **Question:** Why can strict inequalities like $x < 1$ not be used in an LP?
   - **Answer:** Feasible sets with open boundaries may fail to attain an optimal solution. For example, $\max x$ subject to $x < 1$ has supremum 1, but no point inside the feasible set achieves it.

---

### Exam-Style Problems

#### Problem 1: Canonical Form Conversion
Convert the following optimization problem into canonical maximization form ($\max \mathbf{c}^\top \mathbf{z}$ s.t. $M\mathbf{z} \le \mathbf{h}, \mathbf{z} \ge \mathbf{0}$):

$$\begin{aligned}
\min \quad & 3x_1 - 4x_2 + |x_3| \\
\text{s.t.} \quad & x_1 + 2x_2 \ge 4 \\
& x_1 - x_3 = 2 \\
& x_1 \ge 0, \; x_2 \le 0, \; x_3 \in \mathbb{R}
\end{aligned}$$

**Solution:**
1. Split $x_3$ into non-negative parts: $x_3 = x_3^+ - x_3^-$, where $x_3^+, x_3^- \ge 0$, so $|x_3| = x_3^+ + x_3^-$.
2. Substitute non-positive $x_2$: set $x_2 = -x_2'$ with $x_2' \ge 0$.
3. Convert minimization to maximization:
   $$\min (3x_1 + 4x_2' + x_3^+ + x_3^-) \implies \max (-3x_1 - 4x_2' - x_3^+ - x_3^-)$$
4. Transform constraints:
   - $x_1 - 2x_2' \ge 4 \implies -x_1 + 2x_2' \le -4$
   - $x_1 - x_3^+ + x_3^- = 2 \implies (x_1 - x_3^+ + x_3^- \le 2)$ and $(-x_1 + x_3^+ - x_3^- \le -2)$
5. Canonical variables: $\mathbf{z} = [x_1, x_2', x_3^+, x_3^-]^\top \ge \mathbf{0}$.

---

#### Problem 2: Polyhedral Sparsity (Lecture Exercise)
**Problem:** An LP has $n$ variables with box constraints $0 \le x_i \le 1$ for all $i \in \{1, \dots, n\}$, along with $k$ additional linear inequalities $\mathbf{a}_j^\top \mathbf{x} \le b_j$ ($j = 1, \dots, k$). Prove that at any vertex $\mathbf{x}^*$, at most $k$ variables can be strictly fractional (strictly between 0 and 1).

**Proof:**
1. By definition, a point $\mathbf{x}^* \in \mathbb{R}^n$ is a vertex if and only if it has at least $n$ linearly independent tight constraints.
2. Let $F = \{i \in \{1, \dots, n\} : 0 < x_i^* < 1\}$ be the set of strictly fractional coordinates, and let $|F| = p$.
3. For any index $i \in F$, neither $x_i \ge 0$ nor $x_i \le 1$ is tight.
4. Therefore, box constraints can contribute at most $n - p$ tight inequalities (only from coordinates where $x_i^* \in \{0, 1\}$).
5. To attain $n$ linearly independent tight constraints, the remaining constraints must be supplied by the general linear inequalities:
   $$\text{tight general constraints} \ge n - (n - p) = p$$
6. Since there are only $k$ general linear inequalities available:
   $$p \le k$$
Hence, at most $k$ coordinates can be strictly fractional.

---

## 9. Textbook References

1. **Algorithms** by Sanjoy Dasgupta, Christos Papadimitriou, and Umesh Vazirani (McGraw-Hill):
   - **Chapter 7 (Linear Programming and Reductions):** Canonical forms, max-flow reductions, geometric intuitions, and duality certificates.
2. **Introduction to Algorithms (CLRS)** by Cormen, Leiserson, Rivest, and Stein (MIT Press):
   - **Chapter 29 (Linear Programming):** Standard forms, slack forms, algebraic formulation transformations, and duality fundamentals.
3. **Introduction to Linear Optimization** by Dimitris Bertsimas and John N. Tsitsiklis (Athena Scientific):
   - **Chapters 1 & 2:** Rigorous geometric foundations, extreme points, basic feasible solutions, polyhedral convexity, and bit-complexity analysis.
