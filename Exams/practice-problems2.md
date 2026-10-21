# CS 6515/4540 (Fall 2026)

# Exam 2 - Practice

**Name:** ____________________

**GTID:** ____________________

**GT Username:** ____________________

## Instructions

1. When the exam starts, write your name (or GT ID or GT Username) on each page.
2. Bringing two pages of notes is permitted.
3. No books, calculators, or other electronic devices permitted.
4. Make your answers clear and concise.
5. Only write on the **front** of each sheet. Backs will not be scanned.
6. You may refer to standard algorithms from class without giving full pseudocode.

---

# 1. Short Answer Questions (36 points)

Each part is worth 6 points.

Unless explicitly mentioned, a short 1–2 line justification is required.

## 1. LP

Every convex set can be written as an intersection of a finite number of half-spaces (linear inequalities).

- True
- False

## 2. Facility Location

$$
\min \sum_{i \in I} f_i y_i + \sum_{i \in I}\sum_{j \in J} d_{ij} x_{ij}
$$

subject to

$$
\sum_{i \in I} x_{ij}=1 \quad \forall j\in J
$$

$$
x_{ij}\le y_i \quad \forall i,j
$$

$$
x_{ij},y_i\ge 0
$$

Suppose all opening costs are zero:

$$
f_i=0 \quad \forall i.
$$

(A) The optimal LP value is 0.

(B) Every client connects to its nearest facility.

(C) The LP becomes unbounded.

(D) The LP value equals the total connection cost of the MST.

## 3. Farkas' Lemma

$$
A=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad
b=\begin{pmatrix}-1\\-1\end{pmatrix}.
$$

Use Farkas' Lemma to show that

$$
Ax=b,\qquad x\ge0
$$

is infeasible.

## 4. Gradient Descent

When running gradient descent on a $\beta$-smooth convex function, we will converge to the optimum regardless of step size or initial point chosen.

- True
- False

## 5. Convex Bodies

We can run Gradient Descent to solve LPs in polynomial time, assuming the feasible region is a bounded convex set and the objective is linear.

- True
- False

## 6. Approximation Algorithms

A 2-approximation algorithm is applied to a maximization problem, and the optimal solution is known to be 5.

Choose all that apply:

- A. 2.5
- B. 5
- C. 7
- D. 10
- E. None of the above

---

# 2. Linear Programming (25 points)

## 1. Polygon (10 points)

Let $P$ be a convex polygon given by

$$
a_i x + b_i y \le c_i, \qquad i=1,\ldots,m.
$$

Given a fixed point $q=(x_0,y_0)$, find $p=(x_1,y_1)\in P$ minimizing

$$
\|p-q\|_\infty=\max\{|x_1-x_0|,|y_1-y_0|\}.
$$

Formulate an LP computing the minimum $L_\infty$ distance.

## 2. Matching

$$
\max \sum_{e\in E} x_e
$$

subject to

$$
\sum_{e\in\delta(v)}x_e\le 1 \quad \forall v\in V
$$

$$
x_e\ge0 \quad \forall e\in E.
$$

### (a) LP Relaxation

Prove the LP optimum is at least the maximum matching size.

### (b) Integrality Gap

Give a graph where the LP value exceeds the maximum matching size.

### (c) Dual of the LP

Write the dual.

---

# 3. Steiner Tree (19 Points)

Suppose $G=(V,E)$ is complete with nonnegative edge weights satisfying the triangle inequality, and $T\subseteq V$ are required terminals.

Let $F^*$ denote the minimum Steiner tree.

## 1. (12 points)

Show how to construct a spanning tree of $G_T$ with weight at most $2\,w(F^*)$.

## 2. (7 points)

Using part 1, deduce that the MST of $G_T$ is a 2-approximation algorithm for Steiner Tree.

---

# 4. Convex Optimization (20 Points)

## Definition (Strong Convexity)

A differentiable function $f$ is $\alpha$-strongly convex if

$$
f(y)\ge f(x)+\langle \nabla f(x), y-x\rangle + \frac{\alpha}{2}\|y-x\|^2.
$$

Consider an $\alpha$-strongly convex and $\beta$-smooth function with minimizer $x^*$.

Gradient descent uses

$$
x_{k+1}=x_k-\frac1\beta\nabla f(x_k).
$$

### 1. (8 points)

Show that

$$
\frac{1}{2\beta}\|\nabla f(x_k)\|^2\le f(x_k)-f(x_{k+1}).
$$

### 2. (6 points)

Assuming

$$
\|\nabla f(x_k)\|^2\ge 2\alpha(f(x_k)-f(x^*))
$$

show that

$$
f(x_{k+1})-f(x^*)\le\left(1-\frac{\alpha}{\beta}\right)(f(x_k)-f(x^*)).
$$

### 3. (6 points)

Show that

$$
f(x_k)-f(x^*)\le\left(1-\frac{\alpha}{\beta}\right)^k(f(x_0)-f(x^*)).
$$

Thus gradient descent converges exponentially fast.

---

# END OF EXAM
