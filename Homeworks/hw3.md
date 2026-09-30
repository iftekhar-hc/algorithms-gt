# Linear Programming and Convex Optimization

## Problem Set 3 - CS 6515/4540 (Fall 2026)

This problem set is due on **Tuesday, October 13th**. Submission is via Gradescope. Your solution must be a typed PDF (e.g., via LaTeX), with no handwritten solutions.

---

## 10. LPs

Alice is trying to get enough oranges and bananas to host a fruit party. To successfully host a party, she needs **at least 8 oranges** and **at least 20 bananas**. Unfortunately, her local grocery store only sells fruit in bundles:

- **Bundle A** costs 3 dollars and contains one orange and two bananas.
- **Bundle B** costs 2 dollars and contains three oranges and one banana.

The grocery store allows Alice to buy fractional bundles. For example, she can buy 2.5 Bundle As to get 2.5 oranges and 5 bananas. However, she cannot buy a negative number of bundles.

Alice would like to buy $x_A$ Bundle As and $x_B$ Bundle Bs to guarantee that she has at least 8 oranges and at least 20 bananas. Moreover, she would like to minimize the amount of money spent.

1. Write a linear program whose solution is the optimal choice of $x_A, x_B$ for Alice's problem, and briefly justify why this is the correct LP.
2. Show that there exists a solution to this linear program with objective value 30, and hence Alice has to spend at most 30 dollars.
3. Prove that every feasible solution to this linear program has value at least 30. Prove this by taking a nonnegative linear combination of the constraints. Conclude that the solution in the previous part is optimal.

---

## 11. LP Equivalent Formulation

### 11.1 Converting LP2 to LP1

Show that the class of LPs on the left, LP1, can efficiently represent any LP on the right, LP2. In other words, if we have a polynomial-time algorithm that solves any instance of LP1, then we can solve any instance of LP2 in polynomial time.

### LP1

$$
\begin{aligned}
\text{maximize} \quad & \sum_{i=1}^{n} c_i x_i \\
\text{subject to} \quad & \sum_{i=1}^{n} A_{ji}x_i = b_j,
&& \forall j \in \{1,\ldots,m\}, \\
& x_i \ge 0,
&& \forall i \in \{1,\ldots,n\}.
\end{aligned}
$$

### LP2

$$
\begin{aligned}
\text{maximize} \quad & \sum_{i=1}^{n} c_i x_i \\
\text{subject to} \quad & \sum_{i=1}^{n} A_{ji}x_i \le b_j,
&& \forall j \in \{1,\ldots,m\}.
\end{aligned}
$$

> **Hint.** You need two ideas:
>
> 1. Replace an unrestricted variable $x$ by
>    $$
>    x = x^+ - x^-, \qquad x^+ \ge 0, \quad x^- \ge 0.
>    $$
> 2. Replace $Ax \le b$ by
>    $$
>    Ax + Z = b
>    $$
>    for some vector $Z \ge 0$.

### 11.2 Farkas' Lemma

Use a similar idea to show that **Farkas' Lemma A** implies **Farkas' Lemma B**.

#### Farkas' Lemma A

The system

$$
\sum_{i=1}^{n} A_{ji}x_i = b_j,
\qquad j \in \{1,\ldots,m\},
$$

with

$$
x_i \ge 0,
\qquad i \in \{1,\ldots,n\},
$$

is infeasible if and only if there exist $\lambda_j$, for $j \in \{1,\ldots,m\}$, such that

$$
\sum_{j=1}^{m} \lambda_j b_j < 0
$$

and

$$
\sum_{j=1}^{m} \lambda_j A_{ji} \ge 0,
\qquad \forall i \in \{1,\ldots,n\}.
$$

#### Farkas' Lemma B

The system

$$
\sum_{i=1}^{n} A_{ji}x_i \le b_j,
\qquad j \in \{1,\ldots,m\},
$$

is infeasible if and only if there exist nonnegative values $\lambda_j \ge 0$, for $j \in \{1,\ldots,m\}$, such that

$$
\sum_{j=1}^{m} \lambda_j b_j < 0
$$

and

$$
\sum_{j=1}^{m} \lambda_j A_{ji} = 0,
\qquad \forall i \in \{1,\ldots,n\}.
$$

---

## 12. LP for Regression

Suppose we are given $n$ points

$$
(x_1,y_1), (x_2,y_2), \ldots, (x_n,y_n) \in \mathbb{R} \times \mathbb{R}.
$$

The goal is to find a line

$$
y = ax + b,
$$

where $a,b \in \mathbb{R}$, that fits these points as closely as possible, where closeness is defined according to an objective function.

Write a polynomial-sized LP for each of the following settings:

1. **$\ell_1$ regression:** Minimize
   $$
   \sum_{i=1}^{n} \left|y_i - ax_i - b\right|.
   $$
2. **$\ell_\infty$ regression:** Minimize
   $$
   \max_{1 \le i \le n} \left|y_i - ax_i - b\right|.
   $$
3. Write the dual LPs for both of the above LPs.

---

## 13. The Minimax Theorem via LP Duality

Consider a two-player game specified by a matrix $A \in \mathbb{R}^{m \times n}$, where $m,n \ge 1$. Alice chooses a row $i \in \{1,\ldots,m\}$ and Bob chooses a column $j \in \{1,\ldots,n\}$ simultaneously. Alice receives payoff $A_{ij}$, while Bob receives payoff $-A_{ij}$. Thus, Alice wants to maximize Alice's payoff, while Bob wants to minimize it. Entries of $A$ may be positive, zero, or negative.

The players may independently randomize their choices. A **mixed strategy** for Alice is a probability vector $p \in \Delta_m$, where

$$
\Delta_k = \left\{z \in \mathbb{R}^k : z_\ell \ge 0 \text{ for all } \ell,\; \sum_{\ell=1}^{k} z_\ell = 1\right\}.
$$

Similarly, Bob's mixed strategy is $q \in \Delta_n$. Their expected payoff to Alice is

$$
p^\top A q
= \sum_{i=1}^{m}\sum_{j=1}^{n} p_i A_{ij}q_j.
$$

Alice's largest guaranteed expected payoff is

$$
\max_{p \in \Delta_m}\min_{q \in \Delta_n} p^\top A q.
$$

Bob's smallest guaranteed upper bound on Alice's expected payoff is

$$
\min_{q \in \Delta_n}\max_{p \in \Delta_m} p^\top A q.
$$

These guarantees allow an opponent to know the chosen probability vector, but not the outcome of the random choice.

### Minimax Theorem

For every real matrix $A$,

$$
\max_{p \in \Delta_m}\min_{q \in \Delta_n} p^\top A q
=
\min_{q \in \Delta_n}\max_{p \in \Delta_m} p^\top A q.
$$

Moreover, there are mixed strategies $p^* \in \Delta_m$, $q^* \in \Delta_n$, and a real number $V$ such that

$$
(p^*)^\top A q \ge V
\qquad \text{for every } q \in \Delta_n,
$$

and

$$
p^\top A q^* \le V
\qquad \text{for every } p \in \Delta_m.
$$

Consequently,

$$
(p^*)^\top A q^* = V.
$$

The number $V$ is called the **value of the game**.

Your goal is to prove this theorem using strong LP duality. Consider the following primal LP, whose variables are $p_1,\ldots,p_m$ and $v$:

$$
\begin{aligned}
\text{maximize} \quad & v \\
\text{subject to} \quad
& v - \sum_{i=1}^{m} A_{ij}p_i \le 0,
&& j=1,\ldots,n, \\
& \sum_{i=1}^{m} p_i = 1, \\
& p_i \ge 0,
&& i=1,\ldots,m, \\
& v \in \mathbb{R}
&& \text{(unrestricted in sign).}
\end{aligned}
$$

1. For a fixed $p \in \Delta_m$, show that
   $$
   \min_{q \in \Delta_n} p^\top A q
   =
   \min_{1 \le j \le n}\sum_{i=1}^{m} A_{ij}p_i.
   $$
   Use this to explain why the primal LP's optimal value equals Alice's largest guaranteed expected payoff. Show that the LP is feasible and that its objective is bounded above.

2. Derive the dual LP, using $q_1,\ldots,q_n$ for the dual variables corresponding to the payoff constraints and $w$ for the variable corresponding to $\sum_i p_i=1$. State all sign restrictions.

   > **Hint.** In a maximization primal, an equality constraint gives an unrestricted dual variable, and an unrestricted primal variable gives an equality constraint in the dual.

3. Explain why the dual LP's optimal value equals Bob's smallest guaranteed upper bound on Alice's expected payoff. Apply strong LP duality to prove the displayed minimax equality. Finally, use optimal primal and dual solutions to obtain $p^*,q^*,V$ satisfying both guarantees in the theorem.

---

## 14. Convex Sets and Convex Functions

For each part, give a proof or a counterexample. You may not assume that convex functions are differentiable.

1. If $K,L \subseteq \mathbb{R}^n$ are convex sets, must $K \cap L$ be convex? Must $K \cup L$ be convex? Answer both questions.
2. If $f,g : \mathbb{R} \to \mathbb{R}$ are convex functions, must $f+g$ be convex?
3. If $f,g : \mathbb{R} \to \mathbb{R}$ are convex functions, must their pointwise product
   $$
   h(x)=f(x)g(x)
   $$
   be convex?
4. If $f,g : \mathbb{R} \to \mathbb{R}$ are convex functions, must
   $$
   h(x)=\max\{f(x),g(x)\}
   $$
   be convex?

---

## 15. Gradient Descent for Strongly Convex Functions

A differentiable function $f$ is **$\alpha$-strongly convex**, for $\alpha>0$, if for all $x,y \in \mathbb{R}^n$,

$$
f(y)
\ge
f(x)+\langle \nabla f(x),y-x\rangle
+\frac{\alpha}{2}\lVert y-x\rVert_2^2.
$$

Consider an $\alpha$-strongly convex differentiable function $f$ whose gradient always has 2-norm bounded by $G$. The goal is to minimize $f$, and let $x^*$ denote its minimizer.

Show that the gradient descent algorithm with step size

$$
\eta_t = \frac{1}{\alpha(t+1)}
$$

satisfies

$$
f\left(\frac{\sum_{t=1}^{T} x_t}{T}\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
$$

Thus, strong convexity allows us to obtain a $1/T$ dependence in regret instead of the $1/\sqrt{T}$ dependence for general convex functions.

> **Hint.** Change the potential function used in the analysis from class to
> $$
> \Phi(t)=\frac{t\alpha}{2}\lVert x_t-x^*\rVert_2^2.
> $$
> Also, use
> $$
> \sum_{t=1}^{T}\frac{1}{t}\le 1+\log T.
> $$
