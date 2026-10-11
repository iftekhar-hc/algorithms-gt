# Linear Programming for Regression: $\ell_1$ and $\ell_\infty$ Formulations and Duals

In linear regression, given $n$ observations $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n) \in \mathbb{R} \times \mathbb{R}$, we seek model parameters $a, b \in \mathbb{R}$ defining the affine line:

$$
y = ax + b
$$

For each observation $i$, the residual is defined as:

$$
r_i = y_i - (ax_i + b)
$$

Unlike standard Ordinary Least Squares (OLS), which minimizes $\sum_{i=1}^n r_i^2$, $\ell_1$ and $\ell_\infty$ regression optimize non-smooth norms. Because these norms are convex and piecewise linear, both problems can be recast as polynomial-sized Linear Programs (LPs).

---

## 1. $\ell_1$ Regression (Least Absolute Deviations)

### Problem Statement
Minimize the sum of absolute residuals:

$$
\min_{a, b} \sum_{i=1}^{n} |y_i - ax_i - b|
$$

### Primal LP Formulation
Introduce non-negative slack variables $e_i$ representing an upper bound on $|y_i - ax_i - b|$ for each $i \in \{1, \dots, n\}$:

$$
\begin{aligned}
\min_{a, b, e_1, \dots, e_n} \quad & \sum_{i=1}^{n} e_i \\
\text{subject to} \quad & e_i + a x_i + b \ge y_i, \quad i = 1, \dots, n \\
& e_i - a x_i - b \ge -y_i, \quad i = 1, \dots, n \\
& e_i \ge 0, \quad i = 1, \dots, n \\
& a, b \in \mathbb{R}
\end{aligned}
$$

- **Variables:** $n + 2$ (parameters $a, b$ and $n$ error bounds $e_i$).
- **Constraints:** $2n$ inequality bounds (plus non-negativity $e_i \ge 0$).
- **Complexity:** $O(n)$ variables and constraints (linear/polynomial size).

---

## 2. $\ell_\infty$ Regression (Chebyshev / Minimax Approximation)

### Problem Statement
Minimize the maximum peak residual:

$$
\min_{a, b} \max_{1 \le i \le n} |y_i - ax_i - b|
$$

### Primal LP Formulation
Introduce a single scalar variable $t$ that upper bounds all absolute deviations simultaneously:

$$
\begin{aligned}
\min_{a, b, t} \quad & t \\
\text{subject to} \quad & t + a x_i + b \ge y_i, \quad i = 1, \dots, n \\
& t - a x_i - b \ge -y_i, \quad i = 1, \dots, n \\
& t \ge 0 \\
& a, b \in \mathbb{R}
\end{aligned}
$$

- **Variables:** 3 ($a, b, t$).
- **Constraints:** $2n$ linear inequalities.
- **Complexity:** Constant number of variables, $O(n)$ constraints.

---

## 3. Derivations and Dual Formulations

### Dual LP for $\ell_1$ Regression

Assign dual multipliers $u_i \ge 0$ to $e_i + ax_i + b \ge y_i$ and $v_i \ge 0$ to $e_i - ax_i - b \ge -y_i$.

The Lagrangian is:

$$
\mathcal{L}(a, b, e, u, v) = \sum_{i=1}^n e_i - \sum_{i=1}^n u_i (e_i + a x_i + b - y_i) - \sum_{i=1}^n v_i (e_i - a x_i - b + y_i)
$$

Rearranging terms by primal variables:

$$
\mathcal{L} = \sum_{i=1}^n y_i (u_i - v_i) + \sum_{i=1}^n e_i (1 - u_i - v_i) - a \sum_{i=1}^n x_i (u_i - v_i) - b \sum_{i=1}^n (u_i - v_i)
$$

For the infimum over $a, b \in \mathbb{R}$ and $e_i \ge 0$ to be bounded below:
1. $1 - u_i - v_i \ge 0 \implies u_i + v_i \le 1$
2. $\sum_{i=1}^n (u_i - v_i) = 0$
3. $\sum_{i=1}^n x_i (u_i - v_i) = 0$

Setting $w_i = u_i - v_i$, the constraints $u_i, v_i \ge 0$ and $u_i + v_i \le 1$ simplify to $-1 \le w_i \le 1$.

The dual LP becomes:

$$
\begin{aligned}
\max_{w_1, \dots, w_n} \quad & \sum_{i=1}^{n} y_i w_i \\
\text{subject to} \quad & \sum_{i=1}^{n} w_i = 0 \\
& \sum_{i=1}^{n} x_i w_i = 0 \\
& -1 \le w_i \le 1, \quad i = 1, \dots, n
\end{aligned}
$$

The feasible region is the intersection of an $n$-dimensional hypercube $[-1, 1]^n$ with two hyperplanes.

---

### Dual LP for $\ell_\infty$ Regression

Assign dual multipliers $u_i \ge 0$ and $v_i \ge 0$ to the constraints $t + ax_i + b \ge y_i$ and $t - ax_i - b \ge -y_i$.

The Lagrangian is:

$$
\mathcal{L}(a, b, t, u, v) = t - \sum_{i=1}^n u_i (t + a x_i + b - y_i) - \sum_{i=1}^n v_i (t - a x_i - b + y_i)
$$

Rearranging by primal variables:

$$
\mathcal{L} = \sum_{i=1}^n y_i (u_i - v_i) + t \left(1 - \sum_{i=1}^n (u_i + v_i)\right) - a \sum_{i=1}^n x_i (u_i - v_i) - b \sum_{i=1}^n (u_i - v_i)
$$

For boundedness with $t \ge 0$ and free $a, b$:
1. $1 - \sum_{i=1}^n (u_i + v_i) \ge 0 \implies \sum_{i=1}^n (u_i + v_i) \le 1$
2. $\sum_{i=1}^n (u_i - v_i) = 0$
3. $\sum_{i=1}^n x_i (u_i - v_i) = 0$

Using $w_i = u_i - v_i$ where $u_i, v_i \ge 0$ and $\sum_{i=1}^n (u_i + v_i) \le 1$:

$$
\begin{aligned}
\max_{u, v} \quad & \sum_{i=1}^{n} y_i (u_i - v_i) \\
\text{subject to} \quad & \sum_{i=1}^{n} (u_i + v_i) \le 1 \\
& \sum_{i=1}^{n} (u_i - v_i) = 0 \\
& \sum_{i=1}^{n} x_i (u_i - v_i) = 0 \\
& u_i, v_i \ge 0, \quad i = 1, \dots, n
\end{aligned}
$$

Equivalently, in terms of $w_i = u_i - v_i$, the condition is $\sum_{i=1}^n |w_i| \le 1$ (the unit $\ell_1$ ball / cross-polytope).

---

## 4. Geometric Intuition and Outlier Comparison

```text
y ^
  |              (x4, y4) [Outlier]
  |                 *
  |                                 --- L-infinity line (splits extreme deviation)
  |       * (x2, y2)               --- L-1 line (passes directly through bulk data)
  |   * (x1, y1)      * (x3, y3)
  +-------------------------------------> x
```

### Concrete Numerical Example
Consider four data points: $(0, 0), (1, 1), (2, 2), (2, 5)$.

- **$\ell_1$ Fit:** The line $y = x$ gives errors $|0-0| + |1-1| + |2-2| + |5-2| = 3$. The median-centering property ignores the vertical shift of the outlier.
- **$\ell_\infty$ Fit:** The line $y = 1.75x - 0.25$ yields errors $\le 1.25$ across all points, balancing the worst-case envelope at the expense of average error.

---

## 5. Comparative Summary

| Dimension | $\ell_1$ Regression | $\ell_\infty$ Regression |
| :--- | :--- | :--- |
| **Objective** | Minimize sum of absolute errors | Minimize maximum deviation |
| **Primal Dimension** | $n + 2$ variables, $2n$ constraints | 3 variables, $2n$ constraints |
| **Dual Domain** | Hypercube: $w \in [-1, 1]^n$ | Cross-polytope: $\|w\|_1 \le 1$ |
| **Sensitivity** | Robust to outliers | Highly sensitive to outliers |
| **Equilibrium** | Interpolates at least 2 data points | Equidistant from 3 extreme points |\n