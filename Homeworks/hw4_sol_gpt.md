# HW4 Study Guide: Convex Optimization and Approximation Algorithms

This guide follows the three problems in `hw4.tex`. The aim is to understand **why each proof works**, what facts to recognize, and how to reuse the pattern on a new problem.

## Road map

| Problem | Main idea | What the proof must establish |
|---|---|---|
| 1. Smooth non-convex optimization | Smoothness gives a one-step descent bound; sum the bounds | At least one gradient among the iterates is small |
| 2. Greedy load balancing | Compare the last job on the most-loaded machine with the optimal makespan | Greedy makespan is at most `1.5 × OPT` |
| 3. Weighted hitting set | Relax an integer program to an LP, then threshold-round | The rounded set hits every subset and costs at most `b × OPT` |

---

# 1. Gradient descent on a smooth non-convex function

## 1.1 The vocabulary

We want to minimize a differentiable function `f(x)`. In a non-convex problem, the graph may have several valleys, hills, and saddle points. Convexity is **not** assumed in this question.

### β-smoothness

A differentiable function is **β-smooth** when its gradient is β-Lipschitz:

\[
\|\nabla f(x)-\nabla f(y)\|\leq \beta\|x-y\|.
\]

Intuitively, the gradient cannot change arbitrarily sharply. For a twice-differentiable one-dimensional function, a sufficient condition is `|f''(x)| ≤ β` everywhere. In multiple dimensions, the analogous condition bounds the curvature/Hessian operator norm.

A crucial consequence is the **descent lemma**:

\[
f(y)\leq f(x)+\nabla f(x)^\top(y-x)+\frac{\beta}{2}\|y-x\|^2.
\]

This is an upper bound on the function at `y` using the local first-order approximation at `x` plus a curvature allowance. It holds for smooth functions whether or not they are convex.

### Gradient descent and step size

The update is

\[
x^{t+1}=x^t-\eta\nabla f(x^t),
\]

where `η > 0` is the step size. The gradient points uphill locally, so moving in the negative-gradient direction tends to decrease the function. A step that is too large can overshoot; the condition `η ≤ 1/β` is a safe choice for the bound requested here.

### What does a small gradient mean?

A point with `\nabla f(x)=0` is a **stationary point**. It can be a local minimum, local maximum, or saddle point. A small gradient norm is therefore a first-order stationarity guarantee; by itself it does **not** certify a global minimum or even guarantee closeness in distance to a local minimum.

## 1.2 Visual intuition

![A smooth, non-convex function and gradient-descent iterates](hw4_guide_assets/gradient_descent_nonconvex.png)

The curve has more than one bend, so it is not globally convex. Nevertheless, smoothness controls how much the function can curve between the current point and the proposed next point. With a suitable step size, each update decreases the function value.

The plot illustrates one possible trajectory, not a proof that every start reaches the global minimum. The proof below establishes a different, more general guarantee: **among a fixed set of iterates, at least one has a small gradient norm**.

## 1.3 Part (a): prove one-step descent

We need to show

\[
f(x^{t+1})\leq f(x^t)-\frac{\eta}{2}\|\nabla f(x^t)\|^2
\quad\text{when }\eta\leq 1/\beta.
\]

**Step 1: Apply the descent lemma** with `x = x^t` and `y = x^{t+1}`:

\[
f(x^{t+1})\leq f(x^t)+\nabla f(x^t)^\top(x^{t+1}-x^t)
+\frac{\beta}{2}\|x^{t+1}-x^t\|^2.
\]

**Step 2: Substitute the gradient-descent update.** Since

\[
x^{t+1}-x^t=-\eta\nabla f(x^t),
\]

the inner-product term becomes

\[
\nabla f(x^t)^\top(-\eta\nabla f(x^t))
=-\eta\|\nabla f(x^t)\|^2,
\]

and the squared-distance term becomes

\[
\frac{\beta}{2}\|-\eta\nabla f(x^t)\|^2
=\frac{\beta\eta^2}{2}\|\nabla f(x^t)\|^2.
\]

Combining them gives

\[
\begin{aligned}
f(x^{t+1})
&\leq f(x^t)-\eta\|\nabla f(x^t)\|^2
+\frac{\beta\eta^2}{2}\|\nabla f(x^t)\|^2\\
&=f(x^t)-\eta\left(1-\frac{\beta\eta}{2}\right)
\|\nabla f(x^t)\|^2.
\end{aligned}
\]

**Step 3: Use the step-size condition.** If `η ≤ 1/β`, then `βη ≤ 1`, so

\[
1-\frac{\beta\eta}{2}\geq \frac12.
\]

Therefore

\[
\boxed{f(x^{t+1})\leq f(x^t)-\frac{\eta}{2}\|\nabla f(x^t)\|^2.}
\]

**Why this works without convexity:** only the descent lemma (which follows from smoothness) and the update rule were used. No line in this derivation assumes a convex graph.

## 1.4 Part (b): sum the per-iteration decreases

Rearrange the result from part (a):

\[
\frac{\eta}{2}\|\nabla f(x^k)\|^2
\leq f(x^k)-f(x^{k+1}).
\]

Sum this inequality over `k = 0, 1, ..., T−1`:

\[
\frac{\eta}{2}\sum_{k=0}^{T-1}\|\nabla f(x^k)\|^2
\leq \sum_{k=0}^{T-1}\bigl(f(x^k)-f(x^{k+1})\bigr).
\]

The right-hand side **telescopes**: every intermediate term cancels:

\[
\begin{aligned}
&[f(x^0)-f(x^1)]+[f(x^1)-f(x^2)]+\cdots\\
&\hspace{2cm}+[f(x^{T-1})-f(x^T)] = f(x^0)-f(x^T).
\end{aligned}
\]

Since `x*` is a global minimizer, `f(x^T) ≥ f(x*)`. Hence

\[
\frac{\eta}{2}\sum_{k=0}^{T-1}\|\nabla f(x^k)\|^2
\leq f(x^0)-f(x^T)
\leq f(x^0)-f(x^*).
\]

Multiplying by `2/η` gives

\[
\boxed{\sum_{k=0}^{T-1}\|\nabla f(x^k)\|^2
\leq \frac{2}{\eta}\bigl(f(x^0)-f(x^*)\bigr).}
\]

**Pattern to remember:** when each iteration pays for a nonnegative quantity (here, the squared gradient norm) by decreasing a bounded-below potential (here, `f`), summing the inequalities gives a bound on the total accumulated quantity.

## 1.5 Part (c): turn the sum bound into a minimum bound

Let

\[
G_k=\|\nabla f(x^k)\|^2.
\]

All `G_k` are nonnegative. The minimum of `T` numbers is no larger than their average:

\[
\min_{0\leq k\leq T-1}G_k
\leq \frac1T\sum_{k=0}^{T-1}G_k.
\]

Use part (b):

\[
\min_{0\leq k\leq T-1}\|\nabla f(x^k)\|^2
\leq \frac{2}{\eta T}\bigl(f(x^0)-f(x^*)\bigr).
\]

Take the square root (both sides are nonnegative):

\[
\boxed{\min_{0\leq k\leq T-1}\|\nabla f(x^k)\|
\leq \sqrt{\frac{2}{\eta T}\bigl(f(x^0)-f(x^*)\bigr)}.}
\]

Choose `x'` to be the iterate attaining this minimum. This proves the requested kind of guarantee.

### An indexing detail in the assignment

If we perform **T updates**, the updates produce `x^1, ..., x^T`, and there are **T gradient evaluations** at `x^0, ..., x^{T−1}`. The denominator is then `T`. If instead the sum/minimum is written over `x^0, ..., x^t`, there are `t+1` points, so the average gives denominator `t+1`. The handout mixes `t` and `T`; the proof is the same once the number of points is counted consistently.

### What rate does this imply?

To guarantee that one of the first `T` gradient norms is at most `ε`, it suffices that

\[
T\geq \frac{2\bigl(f(x^0)-f(x^*)\bigr)}{\eta\varepsilon^2}.
\]

With `η = 1/β`, this is an `O(β(f(x^0)-f(x*))/ε²)` iteration bound. Notice what it **does not** say: it does not guarantee that every iterate has a small gradient, that `x^T` itself is the best iterate, or that the point is globally optimal.

### Quick check

Suppose the total decrease available is `f(x⁰) − f(x*) = 8`, the step size is `η = 0.25`, and there are `T = 16` gradient evaluations. The theorem gives

\[
\min_k\|\nabla f(x^k)\|\leq \sqrt{\frac{2}{0.25\cdot16}\cdot8}=2.
\]

This is an **upper bound**, not a claim that a gradient norm equals 2.

---

# 2. Greedy approximation for load balancing

## 2.1 Understand the optimization problem

There are `n` jobs with processing times/weights `w₁, ..., wₙ` and `m` identical machines (the bins). A schedule assigns every job to one machine. The load of a machine is the sum of the jobs assigned to it. The **makespan** is the maximum machine load.

The goal is to minimize the makespan. Let `OPT` denote that minimum possible value.

The specified greedy algorithm is **LPT** (Longest Processing Time first):

1. Sort jobs so `w₁ ≥ w₂ ≥ ... ≥ wₙ`.
2. Assign each next job to a currently least-loaded machine.

A `1.5`-approximation means the schedule it creates has makespan at most `1.5 OPT`. It does not necessarily return the best schedule.

## 2.2 Example visualization

![LPT greedy schedule compared with an optimal schedule](hw4_guide_assets/lpt_scheduling.png)

For jobs `10, 9, 8, 7, 6, 5, 4` on three machines, LPT can finish with loads `19, 15, 15`; an optimal schedule has loads `17, 17, 15`. The example is not close to the worst-case ratio, but shows why a greedy placement and an optimal placement need not match.

## 2.3 Proof of the 1.5 approximation

Let `C` be the makespan of the LPT schedule, and choose a machine whose final load is `C`. Let `p` be the **last job placed on that machine**, and let `L` be that machine's load immediately before `p` was assigned. Then

\[
C=L+p.
\]

We bound `L` and `p` separately.

### Bound 1: the load before the last job is at most OPT

When `p` was assigned, the algorithm chose a least-loaded machine. Thus that machine's prior load `L` was no greater than the average load across all `m` machines at that moment. The total weight of jobs already assigned is at most the total weight of all jobs, so

\[
L\leq \frac{\sum_{i=1}^n w_i}{m}\leq OPT.
\]

The last inequality is a standard lower bound: any schedule's maximum load is at least the average load, so `OPT ≥ (Σwᵢ)/m`.

### Bound 2: the last job has weight at most OPT/2

If the critical machine has only one job, then `C` is just that job's weight and `C ≤ OPT`; we are done.

Otherwise it has at least two jobs. The first `m` jobs in the sorted list go to different machines: while fewer than `m` jobs have been placed, an empty machine has load zero and is chosen before any positive-load machine. Therefore the critical machine's **last** job cannot be among the first `m` jobs. Its sorted index is at least `m+1`, so

\[
p\leq w_{m+1}.
\]

Now consider an optimal schedule. Look at the `m+1` largest jobs, `w₁, ..., w_{m+1}`. There are only `m` machines, so by the pigeonhole principle at least two of these jobs must share a machine. Each of those two jobs weighs at least `w_{m+1}`. Hence that machine's load, and therefore the optimal makespan, is at least `2w_{m+1}`:

\[
OPT\geq 2w_{m+1}\quad\Longrightarrow\quad w_{m+1}\leq \frac{OPT}{2}.
\]

It follows that `p ≤ OPT/2`.

### Combine the bounds

\[
C=L+p\leq OPT+\frac{OPT}{2}=\frac32 OPT.
\]

Therefore

\[
\boxed{C\leq 1.5\,OPT.}
\]

If there are fewer than `m` jobs, each can be put on a different machine and the greedy schedule is optimal; this handles the small edge case where `w_{m+1}` is not defined.

## 2.4 How to recognize this proof pattern

The useful trick is to inspect the **last job on a critical (most-loaded) machine**. Its final load splits into a prior load plus one final job:

\[
\text{makespan}=\underbrace{\text{prior load}}_{\leq OPT}
+\underbrace{\text{last job}}_{\leq OPT/2}.
\]

The greedy rule controls the prior load; sorting plus the pigeonhole principle controls the last job. This “critical machine + last job” argument is common in scheduling approximation proofs.

---

# 3. Minimum weighted hitting set by LP rounding

## 3.1 What is a hitting set?

The ground set is `[n] = {1, ..., n}`. We are given subsets `B₁, ..., Bₘ`. A hitting set `H` must choose at least one element from every subset:

\[
H\cap B_j\neq\varnothing\qquad\text{for every }j.
\]

Each element `i` has a positive cost `wᵢ`. We want the minimum-cost hitting set. Assume every `Bⱼ` is nonempty; an empty set cannot be hit, so that instance would be infeasible.

Let

\[
b=\max_j |B_j|
\]

be the maximum size of any input subset. Since a hitting-set instance has nonempty subsets, `b ≥ 1`.

## 3.2 Part (a): write the integer program and its LP relaxation

Introduce one binary variable for each ground-set element:

\[
x_i=\begin{cases}1,&\text{if element }i\text{ is chosen},\\0,&\text{otherwise.}\end{cases}
\]

The objective is the total cost:

\[
\min \sum_{i=1}^{n}w_i x_i.
\]

Every set must contain at least one selected element, so for each `j = 1, ..., m`, impose

\[
\sum_{i\in B_j}x_i\geq 1.
\]

The integer program is

\[
\begin{aligned}
\min\quad &\sum_{i=1}^n w_i x_i\\
\text{s.t.}\quad &\sum_{i\in B_j}x_i\geq 1 &&j=1,\ldots,m,\\
&x_i\in\{0,1\} &&i=1,\ldots,n.
\end{aligned}
\]

To get the **LP relaxation**, allow fractional selections:

\[
\boxed{0\leq x_i\leq 1\quad\text{instead of }x_i\in\{0,1\}.}
\]

A fractional value like `xᵢ = 0.4` is not itself a valid yes/no selection, but it can make the linear optimization problem easier to solve. Since the relaxation allows every integral solution as a special case, its optimal cost `LP*` is no greater than the integer optimum `OPT`:

\[
LP^*\leq OPT.
\]

This direction matters for the approximation proof.

## 3.3 Part (b): why threshold rounding hits every set

Take an optimal LP solution `x*` and define

\[
\hat{x}_i=\begin{cases}1,&x_i^*\geq 1/b,\\0,&x_i^*<1/b.\end{cases}
\]

Then choose

\[
H'=\{i:\hat{x}_i=1\}.
\]

We need to prove every `Bⱼ` contains a selected element.

**Proof by contradiction for an arbitrary set `Bⱼ`:** suppose the rounding selected no element from `Bⱼ`. Then `xᵢ* < 1/b` for every `i ∈ Bⱼ`, giving

\[
\sum_{i\in B_j}x_i^* < \frac{|B_j|}{b}\leq\frac{b}{b}=1.
\]

But LP feasibility requires `Σᵢ∈Bⱼ xᵢ* ≥ 1`. Contradiction. Therefore at least one element in every `Bⱼ` has `xᵢ* ≥ 1/b`, and it is selected. So `H'` is a hitting set.

**The two facts that make this proof work are** (i) every LP constraint has right-hand side 1 and (ii) each set contains at most `b` elements. If every value were strictly below `1/b`, their sum could not reach 1.

## 3.4 Part (c): bound the rounded cost

For every element `i`,

\[
\hat{x}_i\leq b x_i^*.
\]

Why? If `i` is not selected, the left side is zero. If `i` is selected, then `xᵢ* ≥ 1/b`, so `b xᵢ* ≥ 1 = \hat{x}_i`.

Multiply by its positive weight `wᵢ` and sum over all elements:

\[
\sum_{i=1}^n w_i\hat{x}_i
\leq b\sum_{i=1}^n w_i x_i^*
=b\,LP^*\leq b\,OPT.
\]

The left side is the cost of the rounded hitting set, so

\[
\boxed{w(H')\leq b\,OPT.}
\]

Thus deterministic threshold rounding is a **b-approximation**.

## 3.5 Visual intuition for the threshold

![Illustration of threshold rounding at 1/b](hw4_guide_assets/hitting_set_rounding.png)

With `b = 3`, the threshold is `1/3`. Every fractional variable at or above the dashed line is rounded up to 1; every variable below it becomes 0. The bars are illustrative values for understanding the cutoff, not a claim about a particular LP optimum.

Two separate proofs are necessary:

- **Feasibility:** no input set can have all its fractional values below `1/b`, because then their sum would be below 1.
- **Cost:** every chosen item had fractional LP value at least `1/b`, so its cost can be charged to at most `b` times its fractional contribution.

An approximation proof usually needs both: a feasible answer and a bound on its objective value.

## 3.6 The general LP-rounding recipe

This problem illustrates a common algorithm-design template:

1. Model the combinatorial problem with binary variables and linear constraints.
2. Relax integrality so the problem becomes an LP.
3. Solve the LP (conceptually, in a proof, let `x*` be the optimal fractional solution).
4. Round fractional variables using a threshold or another rule.
5. Prove **feasibility** of the rounded answer.
6. Prove its cost is within a multiplicative factor of the LP cost; then use `LP* ≤ OPT`.

Do not combine steps 5 and 6: an inexpensive rounded set is no help if it fails to hit some subset.

---

# Common proof tools used throughout HW4

## Telescoping sums

Whenever you have `aₖ ≤ fₖ − fₖ₊₁`, sum across iterations. The internal `f` terms cancel, leaving only the first and last values.

## Average lower bounds

For load balancing, any schedule has maximum load at least its average load:

\[
OPT\geq \frac{\sum_i w_i}{m}.
\]

## Pigeonhole principle

Placing `m+1` objects into `m` bins forces at least two objects into the same bin. In Problem 2, use the `m+1` largest jobs to create a lower bound on `OPT`.

## Relaxation comparison

For a minimization problem, the LP relaxation is allowed more solutions than the integer program, so

\[
LP^*\leq OPT.
\]

Be careful: this direction reverses for neither the feasible-set logic nor the cost comparison. A relaxed minimization objective is a lower bound on the integer optimum.

---

# Self-test

Try these before checking the answers below.

1. In Problem 1, which exact line uses the condition `η ≤ 1/β`?
2. Why does a small gradient norm not imply that a point is a global minimizer?
3. In Problem 2, why can the last job on a machine with at least two jobs not be among the first `m` jobs?
4. In Problem 2, why are at least two of the `m+1` largest jobs on one optimal machine?
5. In Problem 3, what contradiction proves that the rounded solution hits `Bⱼ`?
6. Why is `LP* ≤ OPT`, and how does that inequality enter the final approximation guarantee?

## Self-test answers

1. It lets us bound `1 − βη/2 ≥ 1/2` in the descent-lemma calculation.
2. Non-convex functions can have local minima, local maxima, and saddle points; zero gradient is only a first-order stationarity condition.
3. The first `m` jobs are assigned one per machine because an empty machine remains least-loaded until each has received one job.
4. There are `m+1` jobs but only `m` machines, so the pigeonhole principle forces a collision.
5. If no element were selected, every value in that set would be strictly less than `1/b`, so the sum would be `< |Bⱼ|/b ≤ 1`, contradicting the LP constraint that the sum is at least 1.
6. The LP feasible region contains all integral solutions, so minimizing over it can only lower the optimum. Rounding costs at most `b LP*`, which is therefore at most `b OPT`.
