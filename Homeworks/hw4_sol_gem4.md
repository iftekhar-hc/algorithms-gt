# Convex Optimization and Approximation Algorithms — Problem Set 4 Guide (CS 6515 / 4540)

This guide provides conceptual explanations, visualizations, concrete examples, step-by-step proofs, textbook references, and suggested video lectures for **Problem Set 4**.

---

## Problem 16: Gradient Descent on a Non-Convex $\beta$-Smooth Function

### 1. Core Concepts & Intuition

#### Why Non-Convex Optimization is Different
When $f(x)$ is **convex**, any local minimum is a global minimum, and Gradient Descent (GD) guarantees that $f(x^T) - f(x^*) \to 0$.

When $f(x)$ is **non-convex** (such as deep neural network loss landscapes), finding the global minimum $x^*$ is generally NP-hard because the landscape can contain many local minima and saddle points. Instead of bounding the function value suboptimality $f(x^T) - f(x^*)$, we prove that **Gradient Descent finds an approximate stationary point**—a point $x'$ where the gradient norm is small ($\|\nabla f(x')\| \le \epsilon$).

#### What is $\beta$-Smoothness?
A differentiable function $f: \mathbb{R}^d \to \mathbb{R}$ is **$\beta$-smooth** if its gradient is $\beta$-Lipschitz continuous:

$$
\|\nabla f(x) - \nabla f(y)\| \le \beta \|x - y\| \quad \forall x, y \in \mathbb{R}^d
$$

Crucially, **$\beta$-smoothness does not require convexity!** Using the Fundamental Theorem of Calculus, $\beta$-smoothness guarantees a **quadratic upper bound** at every point $x$:

$$
f(y) \le f(x) + \nabla f(x)^\top (y - x) + \frac{\beta}{2}\|y - x\|^2 \quad \forall x, y \in \mathbb{R}^d
$$

#### Visualization: The Quadratic Upper Bound & Descent Step
Even if $f(y)$ curves up and down (non-convex), at our current iterate $x^t$, the function $f$ sits *underneath* an upward-opening parabola of curvature $\beta$:

```text
      f(y)
       ^             Quadratic Upper Bound:
       |          .  g(y) = f(x^t) + <grad f(x^t), y - x^t> + (beta/2)||y - x^t||^2
       |         .         .
       |   \    .           .      /
       |    \  .             .    /   <-- True non-convex function f(y)
       |     \._______________.__/
       |      *               *
       |     x^t            x^{t+1} = x^t - eta * grad f(x^t)
       +-------------------------------------> y
```

Because $x^{t+1} = x^t - \eta \nabla f(x^t)$ decreases the quadratic upper bound whenever $\eta \le \frac{1}{\beta}$, and the true function $f(x^{t+1})$ lies **below** that quadratic upper bound, $f(x^{t+1})$ is guaranteed to strictly decrease as long as $\nabla f(x^t) \ne 0$.

#### Concrete Example
Consider $f(x) = \cos(x)$ on $\mathbb{R}$:
- $\nabla f(x) = -\sin(x)$, and $\nabla^2 f(x) = -\cos(x) \in [-1, 1]$.
- Since $|\nabla^2 f(x)| \le 1$ everywhere, $f(x)$ is **$\beta = 1$-smooth** (even though it is non-convex).
- With step size $\eta = \frac{1}{\beta} = 1$, starting at $x^0 = \frac{\pi}{2}$ where $f(x^0) = 0$ and $f'(x^0) = -1$:

$$
x^1 = \frac{\pi}{2} - 1 \cdot (-1) = \frac{\pi}{2} + 1
$$

$$
f(x^1) = \cos\left(\frac{\pi}{2} + 1\right) = -\sin(1) \approx -0.841 \le f(x^0) - \frac{\eta}{2}\|\nabla f(x^0)\|^2 = -0.5
$$

---

### 2. Step-by-Step Solution to Problem 16

> **Note on Notation:** The problem statement uses both $t$ and $T$ for the iteration count. Below we show the exact steps so the relationship between $t$, $t+1$, and $T$ is completely transparent.

#### Part 1: Show $f(x^{t+1}) \le f(x^t) - \frac{\eta}{2}\|\nabla f(x^t)\|^2$

1. By the $\beta$-smoothness quadratic upper bound evaluated at $y = x^{t+1}$ and $x = x^t$:

$$
f(x^{t+1}) \le f(x^t) + \nabla f(x^t)^\top (x^{t+1} - x^t) + \frac{\beta}{2}\|x^{t+1} - x^t\|^2
$$

*(Note: This property holds for all $\beta$-smooth functions regardless of convexity, because its proof only uses the Lipschitz continuity of $\nabla f$ and the Fundamental Theorem of Calculus.)*

2. Substitute the Gradient Descent update rule $x^{t+1} - x^t = -\eta \nabla f(x^t)$:

$$
f(x^{t+1}) \le f(x^t) - \eta \|\nabla f(x^t)\|^2 + \frac{\beta \eta^2}{2} \|\nabla f(x^t)\|^2 = f(x^t) - \eta \left(1 - \frac{\beta \eta}{2}\right) \|\nabla f(x^t)\|^2
$$

3. Since the step size satisfies $\eta \le \frac{1}{\beta}$, we have $\beta \eta \le 1$, which implies $1 - \frac{\beta \eta}{2} \ge 1 - \frac{1}{2} = \frac{1}{2}$.
4. Substituting this bound into the inequality yields:

$$
f(x^{t+1}) \le f(x^t) - \frac{\eta}{2}\|\nabla f(x^t)\|^2
$$

---

#### Part 2: Show $\sum_{k=0}^t \|\nabla f(x^k)\|^2 \le \frac{2}{\eta}(f(x^0) - f(x^*))$

1. Rearranging the inequality from Part 1 for iteration index $k$ gives:

$$
\frac{\eta}{2}\|\nabla f(x^k)\|^2 \le f(x^k) - f(x^{k+1}) \implies \|\nabla f(x^k)\|^2 \le \frac{2}{\eta}\big(f(x^k) - f(x^{k+1})\big)
$$

2. Summing both sides from $k = 0$ to $t$ produces a **telescoping sum** on the right-hand side:

$$
\sum_{k=0}^t \|\nabla f(x^k)\|^2 \le \frac{2}{\eta} \sum_{k=0}^t \big(f(x^k) - f(x^{k+1})\big) = \frac{2}{\eta}\big(f(x^0) - f(x^{t+1})\big)
$$

3. Since $x^*$ is the global minimum ($f(x^*) = \min_x f(x)$), we have $f(x^*) \le f(x^{t+1})$, or equivalently $-f(x^{t+1}) \le -f(x^*)$. Substituting this gives:

$$
\sum_{k=0}^t \|\nabla f(x^k)\|^2 \le \frac{2}{\eta}\big(f(x^0) - f(x^*)\big)
$$

---

#### Part 3: Show $\min_{k=0\dots t} \|\nabla f(x^k)\| \le \sqrt{\frac{2}{\eta \cdot T}(f(x^0) - f(x^*))}$

1. The minimum over $k \in \{0, \dots, t\}$ is less than or equal to every term in the sum:

$$
\min_{k=0\dots t} \|\nabla f(x^k)\|^2 \le \|\nabla f(x^j)\|^2 \quad \forall j \in \{0, \dots, t\}
$$

2. Summing over all $j = 0, \dots, t$ (where there are $t+1 \ge t = T$ terms) and applying Part 2:

$$
T \cdot \min_{k=0\dots t} \|\nabla f(x^k)\|^2 \le (t + 1) \min_{k=0\dots t} \|\nabla f(x^k)\|^2 \le \sum_{k=0}^t \|\nabla f(x^k)\|^2 \le \frac{2}{\eta}\big(f(x^0) - f(x^*)\big)
$$

3. Dividing both sides by $T$ (or $t$) and taking the square root on both sides (since norms are non-negative) yields:

$$
\min_{k=0\dots t} \|\nabla f(x^k)\| \le \sqrt{\frac{2}{\eta \cdot T}\big(f(x^0) - f(x^*)\big)}
$$

Letting $x' = \arg\min_{x^k,\, k \in \{0,\dots,t\}} \|\nabla f(x^k)\|$ gives a point satisfying the desired gradient norm bound.

---

## Problem 17: Greedy Approximation Algorithm (Sorted Load Balancing / LPT)

### 1. Core Concepts & Intuition

#### Problem Setup (Makespan Minimization on Identical Machines)
- We have $n$ items (jobs) with weights $w_1, w_2, \dots, w_n$ and $m$ identical bins (machines).
- We want to assign each item to one of the $m$ bins to minimize the **maximum load** across all bins (called the **makespan**).
- Let $\text{OPT}$ denote the minimum possible maximum bin load of any valid assignment.

#### Why Sorting Helps (Graham's LPT Rule)
- **Unsorted Greedy (List Scheduling):** If items arrive in an arbitrary order, a large item might arrive last and be placed on top of a bin that already has a medium load, yielding a $\left(2 - \frac{1}{m}\right)$-approximation.
- **Sorted Greedy (Longest Processing Time / Decreasing Weight):** By sorting $w_1 \ge w_2 \ge \dots \ge w_n$ first, heavy items are distributed evenly across bins early. If the bin that finishes with the maximum load contains at least $2$ items, the **last item placed on it must have index $k \ge m+1$, and therefore must be relatively small**!

#### Three Essential Lower Bounds on $\text{OPT}$
In any approximation algorithm analysis, we relate our algorithm's cost to lower bounds on $\text{OPT}$:

1. **Average Load Bound:** The total weight of all $n$ items is partitioned among $m$ bins, so the maximum bin load in $\text{OPT}$ is at least the average bin load:

$$
\text{OPT} \ge \frac{1}{m}\sum_{i=1}^n w_i
$$

2. **Maximum Item Bound:** Every single item must be placed into some bin, so:

$$
\text{OPT} \ge \max_{1 \le i \le n} w_i
$$

3. **The $(m+1)$-th Largest Item Bound (Pigeonhole Principle):**
   Suppose $n \ge m + 1$ and items are sorted $w_1 \ge w_2 \ge \dots \ge w_n$. Consider the first $m+1$ items $\{1, 2, \dots, m+1\}$.
   By the **Pigeonhole Principle**, in any placement of $m+1$ items into $m$ bins, **at least one bin in the optimal solution must contain at least $2$ items from $\{1, 2, \dots, m+1\}$**.
   Since each of the first $m+1$ items has weight at least $w_{m+1}$, that bin in $\text{OPT}$ has load at least $2w_{m+1}$:

$$
\text{OPT} \ge 2w_{m+1} \implies w_k \le w_{m+1} \le \frac{1}{2}\text{OPT} \quad \forall k \ge m + 1
$$

#### Visualization & Concrete Example
Suppose $m = 2$ bins and sorted weights are $w = [5, 5, 4, 4, 3]$.
- **Items 1 & 2:** Item 1 ($5$) goes to Bin 1; Item 2 ($5$) goes to Bin 2.
- **Item 3 ($k = m+1 = 3$):** Item 3 ($4$) goes to Bin 1 (load becomes $5 + 4 = 9$). Notice that in *any* assignment of the first $3$ items $[5, 5, 4]$ into $2$ bins, two of them must share a bin, so $\text{OPT} \ge 5 + 4 \ge 2 \times 4 = 8$.

```text
Before placing the final item k on the heaviest bin B*:

   Bin 1        Bin 2 (B*)     Bin m
  +------+     +------+       +------+
  |      |     |  w_k | <-- Last item placed on B* (since B* has >= 2 items, k >= m+1, so w_k <= 0.5 OPT)
  +------+     +------+
  |      |     |      | <-- Load L' just before item k was added:
  |      |     |  L'  |     Since B* had the LEAST load when k was placed, L' <= Average Load <= OPT!
  |      |     |      |
  +------+     +------+       +------+
```

---

### 2. Step-by-Step Proof of the $1.5$-Approximation

Assume without loss of generality that the items are sorted in non-increasing order of weight:

$$
w_1 \ge w_2 \ge \dots \ge w_n
$$

Let $\text{OPT}$ be the maximum bin load of an optimal placement, and let $L_{\text{ALG}}$ be the maximum bin load produced by the greedy algorithm, achieved by some bin $B^*$.

#### Case 1: Bin $B^*$ contains only $1$ item
If $B^*$ contains only a single item $i$, then:

$$
L_{\text{ALG}} = w_i \le \max_{1 \le j \le n} w_j \le \text{OPT} \le 1.5\,\text{OPT}
$$

In this case, the greedy placement is actually optimal.

#### Case 2: Bin $B^*$ contains at least $2$ items
1. Let item $k$ (with weight $w_k$) be the **last item** placed into bin $B^*$ by the greedy algorithm.
2. During the first $m$ steps of the algorithm, each of the first $m$ items $\{1, 2, \dots, m\}$ is placed into a distinct empty bin (since any empty bin has load $0$). Because bin $B^*$ contains at least $2$ items after item $k$ is added, item $k$ cannot be one of the first $m$ items. Therefore:

$$
k \ge m + 1
$$

3. **Bounding $w_k$:** Consider the first $m+1$ items $\{1, 2, \dots, m+1\}$ in the optimal solution. Since $m+1$ items are placed into $m$ bins, by the **Pigeonhole Principle**, at least one bin in the optimal assignment contains at least two items $a, b \in \{1, 2, \dots, m+1\}$. Because weights are sorted in non-increasing order and $k \ge m+1$:

$$
\text{OPT} \ge w_a + w_b \ge 2w_{m+1} \ge 2w_k \implies w_k \le \frac{1}{2}\text{OPT}
$$

4. **Bounding the load of $B^*$ before item $k$ was added:**
   Let $L'$ denote the load of bin $B^*$ **immediately before** item $k$ was placed into it. Because the greedy algorithm places item $k$ into the bin with the **least current load**, every bin $j \in \{1, \dots, m\}$ had load at least $L'$ at that moment. Summing the loads across all $m$ bins at that moment gives:

$$
m \cdot L' \le \sum_{i=1}^{k-1} w_i \le \sum_{i=1}^n w_i \implies L' \le \frac{1}{m}\sum_{i=1}^n w_i \le \text{OPT}
$$

5. **Combining the bounds:**
   Since item $k$ was the last item placed into $B^*$, the final load of bin $B^*$ is:

$$
L_{\text{ALG}} = L' + w_k \le \text{OPT} + \frac{1}{2}\text{OPT} = 1.5\,\text{OPT}
$$

Thus, the greedy algorithm is a $1.5$-approximation for the minimum makespan problem.

---

## Problem 18: Minimum Hitting Set via Deterministic LP Rounding

### 1. Core Concepts & Intuition

#### What is the Minimum Hitting Set Problem?
- We are given a ground set $[n] = \{1, 2, \dots, n\}$ where each element $i \in [n]$ has a positive weight $w_i > 0$.
- We are given $m$ subsets $B_1, B_2, \dots, B_m \subseteq [n]$, with maximum subset size $b = \max_{1 \le j \le m} |B_j|$.
- We seek a subset $H \subseteq [n]$ of minimum total weight $\sum_{i \in H} w_i$ that "hits" every subset $B_j$ (meaning $H \cap B_j \ne \emptyset$ for all $1 \le j \le m$).
- **Connection to Set Cover and Vertex Cover:**
  - Hitting Set is the exact dual of **Set Cover** (swapping the roles of elements and sets; here $b$ corresponds to the maximum element frequency $f$ in Set Cover).
  - When $b = 2$, each subset $B_j$ has size at most $2$ (an edge in a graph), so Minimum Hitting Set is equivalent to **Minimum Weight Vertex Cover**, and threshold rounding at $\frac{1}{2}$ yields the classic $2$-approximation.

#### Concrete Example
Suppose $n = 3$, weights $w = (10, 10, 10)$, and $B_1 = \{1, 2, 3\}$ so $b = 3$:
- **LP Relaxation:** Instead of forcing binary decisions $x_i \in \{0, 1\}$, we allow fractional values $x_i \in [0, 1]$ subject to $\sum_{i \in B_j} x_i \ge 1$.
- For $B_1 = \{1, 2, 3\}$, the LP can set $x^*_1 = \frac{1}{3}, x^*_2 = \frac{1}{3}, x^*_3 = \frac{1}{3}$, achieving an LP objective of $10\left(\frac{1}{3} + \frac{1}{3} + \frac{1}{3}\right) = 10$.
- **Why threshold at $\frac{1}{b}$?** Since $B_j$ has at most $b$ elements and their fractional values sum to at least $1$, **not all of them can be strictly less than $\frac{1}{b}$**. By the averaging principle, at least one element $i \in B_j$ must satisfy $x^*_i \ge \frac{1}{b}$.
- Rounding every $x^*_i \ge \frac{1}{b}$ up to $1$ increases each variable by **at most a factor of $b$**, costing at most $b \cdot \text{OPT}_{\text{LP}} \le b \cdot \text{OPT}$.

#### Visualization of the LP Relaxation & Rounding Pipeline

```text
+-----------------------+      Relaxation      +-----------------------+      Rounding       +-----------------------+
|   Optimal Integer     | -------------------> |  Optimal Fractional   | ------------------> |   Rounded Integer     |
|     Hitting Set       |                      |     LP Solution       |   (Threshold 1/b)   |     Solution H'       |
|      Cost: OPT        |    OPT_LP <= OPT     |     Cost: OPT_LP      |  Cost <= b * OPT_LP |   Cost <= b * OPT     |
+-----------------------+                      +-----------------------+                     +-----------------------+
```

---

### 2. Step-by-Step Solution to Problem 18

#### Part 1: LP Formulation

1. **Decision Variables:**
   For each $i \in \{1, 2, \dots, n\}$, let $x_i \in \mathbb{R}$ represent the fractional inclusion of element $i$ in the hitting set $H$ (relaxing the binary indicator $x_i \in \{0, 1\}$).

2. **Objective Function:**
   Minimize the total weight of the selected elements:

$$
\min \sum_{i=1}^n w_i x_i
$$

3. **Constraints:**
   - **Hitting set constraints:** Every subset $B_j$ ($1 \le j \le m$) must be fractionally hit by at least $1$:

$$
\sum_{i \in B_j} x_i \ge 1 \quad \forall j \in \{1, 2, \dots, m\}
$$

   - **Relaxed variable bounds:**

$$
0 \le x_i \le 1 \quad \forall i \in \{1, 2, \dots, n\}
$$

---

#### Part 2: Prove that $H' = \{i \mid \hat{x}_i = 1\}$ is a Hitting Set

We must show that for every $j \in \{1, 2, \dots, m\}$, $H' \cap B_j \ne \emptyset$.

1. Fix an arbitrary subset $B_j$ ($1 \le j \le m$). Because $x^*$ is a feasible solution to the LP relaxation, it satisfies the constraint for $B_j$:

$$
\sum_{i \in B_j} x^*_i \ge 1
$$

2. Suppose for the sake of contradiction that $H' \cap B_j = \emptyset$. By the definition of the deterministic rounding rule:

$$
\hat{x}_i = \begin{cases} 1 & \text{if } x^*_i \ge b^{-1} \\ 0 & \text{otherwise} \end{cases}
$$

having $H' \cap B_j = \emptyset$ means that $\hat{x}_i = 0$, and hence $x^*_i < \frac{1}{b}$, for every $i \in B_j$.

3. Summing over all $i \in B_j$ and using the fact that $|B_j| \le b = \max_{1 \le k \le m} |B_k|$ gives:

$$
\sum_{i \in B_j} x^*_i < \sum_{i \in B_j} \frac{1}{b} = \frac{|B_j|}{b} \le \frac{b}{b} = 1
$$

4. This implies $\sum_{i \in B_j} x^*_i < 1$, which contradicts the LP feasibility constraint $\sum_{i \in B_j} x^*_i \ge 1$.
5. Therefore, for every $j \in \{1, \dots, m\}$, there exists at least one element $i \in B_j$ with $x^*_i \ge \frac{1}{b}$, so $\hat{x}_i = 1$ and $i \in H' \cap B_j$. Thus, $H'$ is a valid hitting set.

---

#### Part 3: Prove that the Deterministic Rounding Yields a $b$-Approximation

Let $H^*$ be an optimal hitting set of minimum weight $\text{OPT} = \sum_{i \in H^*} w_i$.

1. **Relate the LP optimum to $\text{OPT}$:**
   The indicator vector of $H^*$ (setting $x_i = 1$ if $i \in H^*$ and $x_i = 0$ otherwise) is a feasible solution to the relaxed LP. Since $x^*$ is an optimal solution to the relaxed LP:

$$
\sum_{i=1}^n w_i x^*_i \le \text{OPT}
$$

2. **Bound $\hat{x}_i$ in terms of $x^*_i$:**
   For each $i \in \{1, 2, \dots, n\}$:
   - If $x^*_i \ge \frac{1}{b}$, then $\hat{x}_i = 1 \le b \cdot x^*_i$.
   - If $x^*_i < \frac{1}{b}$, then $\hat{x}_i = 0 \le b \cdot x^*_i$ (since $x^*_i \ge 0$ and $b \ge 1$).

   Hence, for every $i \in \{1, 2, \dots, n\}$:

$$
\hat{x}_i \le b \cdot x^*_i
$$

3. **Bound the total weight of $H'$:**
   Since the weights $w_i > 0$ are positive, multiplying by $w_i$ and summing over all $i \in \{1, \dots, n\}$ yields:

$$
\sum_{i \in H'} w_i = \sum_{i=1}^n w_i \hat{x}_i \le \sum_{i=1}^n w_i (b \cdot x^*_i) = b \sum_{i=1}^n w_i x^*_i \le b \cdot \text{OPT}
$$

Since $H'$ is a valid hitting set (by Part 2) and its total weight is at most $b \cdot \text{OPT}$, the deterministic rounding algorithm achieves a $b$-approximation.

---

## Textbook References & Suggested Video Lectures

### 1. Textbook References

#### For Problem 16 (Non-Convex Smooth Gradient Descent)
1. **Sébastien Bubeck**, *Convex Optimization: Algorithms and Complexity* (Foundations and Trends in Machine Learning, 2015).
   - **Section 3.2 (Smooth functions):** Covers the Descent Lemma $f(x^{t+1}) \le f(x^t) - \frac{1}{2\beta}\|\nabla f(x^t)\|^2$ and how $\beta$-smoothness provides a quadratic upper bound.
2. **Yurii Nesterov**, *Lectures on Convex Optimization* (2nd Edition, Springer, 2018).
   - **Section 1.2.3 (Gradient Method for Smooth Non-Convex Functions):** Derives the exact $\min_{0 \le k \le t} \|\nabla f(x^k)\| \le \mathcal{O}(1/\sqrt{T})$ bound for general smooth functions (see Inequality 1.2.13).
3. **Prateek Jain & Purushottam Kar**, *Non-Convex Optimization for Machine Learning* (Foundations and Trends in Machine Learning, 2017).
   - **Chapter 2 (Stationary Points and Gradient Descent):** Gives a dedicated walkthrough of this 3-step proof for non-convex gradient descent.

#### For Problem 17 (Greedy Load Balancing / LPT Scheduling)
1. **Jon Kleinberg & Éva Tardos**, *Algorithm Design* (Pearson, 2005).
   - **Section 11.1 (Load Balancing, pp. 600–606):** Covers this exact problem step-by-step, proving the $2$-approximation for unsorted greedy and the **$1.5$-approximation** for sorted greedy using the $w_{m+1} \le \frac{1}{2}\text{OPT}$ pigeonhole argument.
2. **David P. Williamson & David B. Shmoys**, *The Design of Approximation Algorithms* (Cambridge University Press, 2011).
   - **Section 2.3 (Scheduling Jobs on Identical Parallel Machines):** Discusses local search, greedy list scheduling, and Longest Processing Time (LPT).
3. **Vijay V. Vazirani**, *Approximation Algorithms* (Springer, 2001).
   - **Chapter 10 (Scheduling on Identical Machines).**

#### For Problem 18 (Hitting Set / Set Cover via Deterministic LP Rounding)
1. **David P. Williamson & David B. Shmoys**, *The Design of Approximation Algorithms* (Cambridge University Press, 2011).
   - **Section 1.2 (Deterministic Rounding for Set Cover):** Shows the $f$-approximation via thresholding at $x^*_i \ge \frac{1}{f}$, which is identical to the $b$-approximation for Hitting Set.
2. **Jon Kleinberg & Éva Tardos**, *Algorithm Design* (Pearson, 2005).
   - **Section 11.6 (LP Rounding: Vertex Cover and Set Cover):** Explains LP relaxation, why the LP optimum lower-bounds the integer optimum, and threshold rounding.
3. **Vijay V. Vazirani**, *Approximation Algorithms* (Springer, 2001).
   - **Chapter 14 (Rounding Applied to Set Cover).**

---

### 2. Suggested Video Lectures

1. **Problem 16 (Non-Convex Smooth Gradient Descent):**
   - **Constantine Caramanis (UT Austin, EE 381V) — "Optimization: Smoothness & Gradient Descent":** Walks through the quadratic upper bound and the telescoping sum proof visually.
   - **Ryan Tibshirani (CMU 10-725 Convex Optimization) — "Gradient Descent":** Detailed coverage of the Descent Lemma and why step size $\eta \le \frac{1}{\beta}$ guarantees descent even without convexity.
   - **Sébastien Bubeck (MSR / Princeton Lectures) — "Non-Convex Optimization":** Explains why we measure $\|\nabla f(x)\|$ instead of $f(x) - f(x^*)$ in non-convex optimization.

2. **Problem 17 (Greedy Load Balancing):**
   - **Tim Roughgarden (Stanford / Columbia, *Algorithms Illuminated Part 4*) — "Makespan Minimization & Greedy Load Balancing":** Explains Graham's greedy algorithm and the sorted $1.5$-approximation proof with concrete examples.
   - **MIT 6.046J (Design and Analysis of Algorithms, Erik Demaine / Srini Devadas) — "Approximation Algorithms":** Covers Greedy Load Balancing and LP rounding in a single lecture.

3. **Problem 18 (LP Relaxation & Deterministic Rounding):**
   - **Ryan O'Donnell / Anupam Gupta (CMU 15-451 / 15-859) — "Linear Programming & Approximation Algorithms (Vertex Cover / Set Cover / Hitting Set)":** Covers LP relaxations and deterministic threshold rounding.
   - **Shayan Oveis Gharan (UW CSE 521) — "LP Relaxation and Deterministic Rounding":** Walks through formulating Set Cover / Hitting Set LPs and proving feasibility and the $b$-approximation ratio.




