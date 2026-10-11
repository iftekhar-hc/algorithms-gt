# The Minimax Theorem via Linear Programming Duality — Step-by-Step Proof

The central idea is to **translate the two players' optimization problems into a pair of dual linear programs (LPs)**. Then strong LP duality tells us that their optimal values are equal, which proves the minimax theorem.

We'll build the proof from the ground up, derive the dual carefully, and finish with a numerical example to illustrate what the theorem means.

## 1\. Background: What does the minimax theorem say?

Consider a two-player, zero-sum game represented by a matrix $A\in\mathbb R^{m\times n}$.

- Alice chooses a row and wants to **maximize** the payoff.
- Bob chooses a column and wants to **minimize** Alice's payoff.
- Alice receives $A_{ij}$ when row $i$ and column $j$ are chosen.
- Bob receives $-A_{ij}$.

Because the players can randomize, their strategies are probability vectors:

$$
p\in\Delta_m,\qquad q\in\Delta_n,
$$

where

$$
\Delta_k=\left\{z\in\mathbb R^k:z_\ell\ge 0,\ \sum_{\ell=1}^kz_\ell=1\right\}.
$$

The expected payoff to Alice is

$$
p^\top A q.
$$

### What are the players trying to optimize?

Alice wants to choose a strategy that maximizes her guaranteed payoff:

$$
\boxed{\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.}
$$

Bob wants to choose a strategy that minimizes the largest payoff Alice can obtain against him:

$$
\boxed{\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.}
$$

The minimax theorem states that these two quantities are equal:

$$
\boxed{
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
}
$$

In other words, **Alice's best guaranteed payoff equals Bob's best achievable upper bound on Alice's payoff.**

This common number is the value of the game, denoted by $V$.

### Why is this surprising?

For any function of two variables, we generally have

$$
\max_p\min_q f(p,q)
\le
\min_q\max_p f(p,q).
$$

The left side lets Alice choose her strategy first in the optimization, while the right side lets Bob choose his first. The inequality says Alice's guaranteed payoff cannot exceed Bob's upper bound.

The minimax theorem establishes something stronger: **for finite zero-sum games, the two bounds coincide.**

We will prove this using linear programming.

---

# Part 1. Constructing and interpreting the primal LP

The given primal LP is

$$
\begin{aligned}
\text{maximize}\quad &v\\
\text{subject to}\quad
&v-\sum_{i=1}^m A_{ij}p_i\le 0,
&&j=1,\ldots,n,\\
&\sum_{i=1}^m p_i=1,\\
&p_i\ge 0,
&&i=1,\ldots,m,\\
&v\in\mathbb R.
\end{aligned}
$$

The variables are $p_1,\ldots,p_m$ and $v$.

Let's understand why this LP represents Alice's problem.

## Step 1. Show that the worst column is a pure strategy

Fix Alice's mixed strategy $p\in\Delta_m$.

Define

$$
a_j=\sum_{i=1}^m A_{ij}p_i.
$$

The quantity $a_j$ is Alice's expected payoff if Bob chooses column $j$ with certainty.

If Bob uses a mixed strategy $q\in\Delta_n$, Alice's expected payoff becomes

$$
\begin{aligned}
p^\top A q
&=\sum_{j=1}^n q_j\left(\sum_{i=1}^m A_{ij}p_i\right)\\
&=\sum_{j=1}^n q_j a_j.
\end{aligned}
$$

Since $q_j\ge 0$ and $\sum_j q_j=1$, this is a weighted average of the numbers $a_1,\ldots,a_n$.

A weighted average cannot be smaller than the smallest number being averaged. Therefore,

$$
p^\top A q\ge \min_{1\le j\le n}a_j.
$$

Moreover, Bob can achieve equality by choosing a column $j^*$ that minimizes $a_j$. Specifically, he can set $q_{j^*}=1$ and all other components of $q$ to zero.

Consequently,

$$
\boxed{
\min_{q\in\Delta_n}p^\top A q
=
\min_{1\le j\le n}\sum_{i=1}^m A_{ij}p_i.
}
$$

**Key insight:** For a fixed strategy of Alice, Bob does not need to randomize to minimize Alice's payoff. He can choose a column with the smallest expected payoff.

This does not mean that Bob never needs to randomize in an optimal strategy. It means that for any _fixed_ $p$, at least one pure strategy is a best response.

## Step 2. Interpret the payoff constraints

The primal LP imposes the constraints

$$
v-\sum_{i=1}^m A_{ij}p_i\le 0
\qquad j=1,\ldots,n.
$$

Rearranging gives

$$
v\le \sum_{i=1}^m A_{ij}p_i
\qquad j=1,\ldots,n.
$$

Thus, $v$ must be no greater than Alice's expected payoff against every pure column of Bob.

Equivalently,

$$
v\le \min_{1\le j\le n}\sum_{i=1}^m A_{ij}p_i.
$$

For any fixed $p$, the largest feasible value of $v$ is therefore

$$
v=\min_{1\le j\le n}\sum_{i=1}^m A_{ij}p_i.
$$

Maximizing $v$ over all feasible probability vectors $p$ gives

$$
\begin{aligned}
\max v
&=\max_{p\in\Delta_m}
\min_{1\le j\le n}\sum_{i=1}^m A_{ij}p_i\\
&=\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.
\end{aligned}
$$

Hence,

$$
\boxed{
\text{Primal optimal value}
=
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.
}
$$

The primal LP computes Alice's largest guaranteed expected payoff.

## Step 3. Show that the primal LP is feasible

An LP is feasible if there is at least one assignment of its variables satisfying every constraint.

Choose any probability vector $p\in\Delta_m$. For example,

$$
p_i=\frac1m,\qquad i=1,\ldots,m.
$$

Define

$$
v=\min_{1\le j\le n}\sum_{i=1}^m A_{ij}p_i.
$$

Because $A$ has finitely many real entries, this minimum exists and is finite.

By construction,

$$
v\le\sum_{i=1}^m A_{ij}p_i
\qquad\text{for every }j.
$$

Also, $p_i\ge 0$ and $\sum_i p_i=1$.

Thus, every primal constraint is satisfied.

Therefore,

$$
\boxed{\text{The primal LP is feasible.}}
$$

## Step 4. Show that the primal objective is bounded above

Let

$$
M=\max_{1\le i\le m,\ 1\le j\le n}|A_{ij}|.
$$

Since $A$ is a finite matrix, $M<\infty$.

For every probability vector $p\in\Delta_m$ and every column $j$,

$$
-M\le\sum_{i=1}^m A_{ij}p_i\le M.
$$

Indeed, the sum is a weighted average of entries in column $j$.

Every feasible solution must satisfy

$$
v\le\sum_{i=1}^m A_{ij}p_i
$$

for every $j$. In particular,

$$
v\le M.
$$

Therefore, the primal objective is bounded above.

We have established that the primal LP is feasible and has a finite optimal value.

Furthermore, because the feasible probability simplex is compact and the minimum of finitely many continuous functions is continuous, Alice's maximum is attained by some $p^*\in\Delta_m$.

Thus, the primal LP has an optimal solution.

---

# Part 2. Deriving the dual LP

This is the most algebraically important part of the proof.

The primal is

$$
\begin{aligned}
\text{maximize}\quad &v\\
\text{subject to}\quad
&v-\sum_{i=1}^m A_{ij}p_i\le 0,
&&j=1,\ldots,n,\\
&\sum_{i=1}^m p_i=1,\\
&p_i\ge 0,\\
&v\text{ unrestricted}.
\end{aligned}
$$

We will derive its dual using the standard rules for linear programming.

## Step 1. Introduce dual variables

There are two types of constraints in the primal.

**Type 1: The****$n$****payoff constraints**

$$
v-\sum_{i=1}^m A_{ij}p_i\le 0,
\qquad j=1,\ldots,n.
$$

Associate a dual variable $q_j$ with each constraint.

Because the primal is a maximization problem with $\le$ constraints, the corresponding dual variables satisfy

$$
\boxed{q_j\ge 0,\qquad j=1,\ldots,n.}
$$

**Type 2: The probability normalization constraint**

$$
\sum_{i=1}^m p_i=1.
$$

Associate the dual variable $w$ with this equality.

An equality constraint produces an unrestricted dual variable, so

$$
\boxed{w\in\mathbb R.}
$$

The dual variables are therefore

$$
q_1,\ldots,q_n\ge 0,\qquad w\in\mathbb R.
$$

## Step 2. Construct the dual objective

The right-hand sides of the primal constraints are:

- $0$ for each of the $n$ payoff constraints;
- $1$ for the equality constraint.

The dual objective is the weighted sum of these right-hand sides:

$$
\min\left(\sum_{j=1}^n 0q_j+1w\right).
$$

Hence, the dual objective is simply

$$
\boxed{\text{Minimize }w.}
$$

## Step 3. Derive the dual constraint associated with $v$

The variable $v$ appears in every payoff constraint with coefficient $1$.

Thus, its coefficients across the $n$ payoff constraints are

$$
(1,1,\ldots,1).
$$

Since $v$ is unrestricted in sign in the primal, its corresponding dual constraint must be an equality.

The resulting constraint is

$$
\boxed{\sum_{j=1}^n q_j=1.}
$$

Notice that this is exactly the condition that $q$ is a probability vector, once we also impose $q_j\ge 0$.

Therefore,

$$
q\in\Delta_n.
$$

## Step 4. Derive the dual constraints associated with $p_i$

Consider a fixed primal variable $p_i$.

In the payoff constraint indexed by $j$, its coefficient is $-A_{ij}$. Its coefficient in the normalization constraint is $1$.

The dual constraint corresponding to $p_i$ is therefore

$$
-\sum_{j=1}^n A_{ij}q_j+w\ge 0.
$$

Why is the inequality $\ge$?

The primal is a maximization problem, and $p_i\ge 0$. A nonnegative primal variable in a maximization problem produces a $\ge$ dual constraint.

Rearranging gives

$$
\boxed{
w\ge\sum_{j=1}^n A_{ij}q_j,
\qquad i=1,\ldots,m.
}
$$

These constraints say that $w$ must be at least Alice's expected payoff against Bob's strategy $q$, no matter which pure row Alice chooses.

## Step 5. Write the complete dual LP

Combining everything, we obtain

$$
\boxed{
\begin{aligned}
\text{minimize}\quad &w\\
\text{subject to}\quad
&\sum_{j=1}^n A_{ij}q_j\le w,
&&i=1,\ldots,m,\\
&\sum_{j=1}^n q_j=1,\\
&q_j\ge 0,
&&j=1,\ldots,n,\\
&w\in\mathbb R.
\end{aligned}
}
$$

This is the required dual LP.

### Summary of the duality rules used

| Primal feature | Dual consequence |
| --- | --- |
| Maximization objective | Dual is a minimization problem |
| Constraint $\le$ | Corresponding dual variable is nonnegative |
| Equality constraint | Corresponding dual variable is unrestricted |
| Nonnegative primal variable | Corresponding dual constraint is $\ge$ |
| Unrestricted primal variable | Corresponding dual constraint is an equality |

These rules explain every sign restriction and equality in the derived dual.

---

# Part 3. Interpreting the dual as Bob's optimization problem

We have derived the dual LP:

$$
\begin{aligned}
\text{minimize}\quad &w\\
\text{subject to}\quad
&\sum_{j=1}^n A_{ij}q_j\le w,
&&i=1,\ldots,m,\\
&q\in\Delta_n,\\
&w\in\mathbb R.
\end{aligned}
$$

Now we show that its optimal value is Bob's smallest guaranteed upper bound on Alice's payoff.

## Step 1. Interpret the constraints

Fix Bob's mixed strategy $q\in\Delta_n$.

If Alice chooses pure row $i$, her expected payoff is

$$
\sum_{j=1}^n A_{ij}q_j.
$$

The dual constraints require

$$
\sum_{j=1}^n A_{ij}q_j\le w
\qquad\text{for every }i.
$$

Thus, $w$ must be at least Alice's expected payoff against every pure row.

Equivalently,

$$
w\ge\max_{1\le i\le m}\sum_{j=1}^n A_{ij}q_j.
$$

For fixed $q$, the smallest feasible value of $w$ is therefore

$$
w=\max_{1\le i\le m}\sum_{j=1}^n A_{ij}q_j.
$$

## Step 2. Show that a pure row suffices for Alice's best response

For any mixed strategy $p\in\Delta_m$,

$$
\begin{aligned}
p^\top A q
&=\sum_{i=1}^m p_i\left(\sum_{j=1}^n A_{ij}q_j\right).
\end{aligned}
$$

This is a weighted average of Alice's expected payoffs from the individual rows.

A weighted average cannot exceed the largest number being averaged. Therefore,

$$
p^\top A q
\le
\max_{1\le i\le m}\sum_{j=1}^n A_{ij}q_j.
$$

Alice can attain equality by choosing a row that maximizes her expected payoff.

Hence,

$$
\boxed{
\max_{p\in\Delta_m}p^\top A q
=
\max_{1\le i\le m}\sum_{j=1}^n A_{ij}q_j.
}
$$

## Step 3. Identify the dual optimal value

For each fixed $q$, minimizing $w$ gives

$$
w=\max_{p\in\Delta_m}p^\top A q.
$$

Then minimizing over $q\in\Delta_n$ gives

$$
\begin{aligned}
\min w
&=\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
\end{aligned}
$$

Therefore,

$$
\boxed{
\text{Dual optimal value}
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
}
$$

This is precisely Bob's smallest guaranteed upper bound on Alice's expected payoff.

---

# Part 4. Apply strong LP duality

We now have two optimization problems.

The primal LP has optimal value

$$
P^*=\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.
$$

The dual LP has optimal value

$$
D^*=\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
$$

From Part 1, the primal LP is feasible and its objective is bounded above. From Part 2, the dual is its correctly constructed dual LP.

The **strong duality theorem for linear programming** states that if a primal LP has a finite optimal value, then its dual also attains an optimal solution and the two optimal objective values are equal.

Consequently,

$$
P^*=D^*.
$$

Substituting their game-theoretic interpretations gives

$$
\boxed{
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
}
$$

This proves the minimax equality.

**The essential argument is that Alice's optimization is the primal LP and Bob's optimization is its dual. Strong duality forces their optimal values to coincide.**

Notice that the proof does not require the entries of $A$ to be positive. The argument works for every real matrix because the expected payoffs remain finite and the probability constraints are well-defined.

---

# Part 5. Prove the existence of optimal strategies $p^*,q^*$

The theorem also asserts the existence of strategies $p^*,q^*$ and a number $V$ such that

$$
(p^*)^\top A q\ge V
\qquad\text{for every }q\in\Delta_n,
$$

and

$$
p^\top A q^*\le V
\qquad\text{for every }p\in\Delta_m.
$$

Let's obtain these from the optimal solutions of the primal and dual LPs.

## Step 1. Choose optimal primal and dual solutions

Let

$$
(p^*,V)
$$

be an optimal solution of the primal LP.

Then

$$
p^*\in\Delta_m
$$

and $V$ is the optimal primal objective value.

Similarly, let

$$
(q^*,w^*)
$$

be an optimal solution of the dual LP.

Then

$$
q^*\in\Delta_n.
$$

By strong duality,

$$
\boxed{V=w^*.}
$$

We can therefore use the same number $V$ for both optimal values.

## Step 2. Prove Alice's guarantee

Because $(p^*,V)$ is primal feasible, its constraints imply

$$
V-\sum_{i=1}^m A_{ij}p_i^*\le 0
\qquad\text{for every }j.
$$

Equivalently,

$$
\sum_{i=1}^m A_{ij}p_i^*\ge V
\qquad\text{for every }j.
$$

Thus, Alice obtains an expected payoff of at least $V$ against every pure column.

Now let Bob use any mixed strategy $q\in\Delta_n$. Then

$$
\begin{aligned}
(p^*)^\top A q
&=\sum_{j=1}^n q_j
\left(\sum_{i=1}^m A_{ij}p_i^*\right)\\
&\ge \sum_{j=1}^n q_j V\\
&=V\sum_{j=1}^n q_j\\
&=V.
\end{aligned}
$$

Therefore,

$$
\boxed{
(p^*)^\top A q\ge V
\qquad\forall q\in\Delta_n.
}
$$

Alice guarantees a payoff of at least $V$.

## Step 3. Prove Bob's guarantee

Because $(q^*,V)$ is dual feasible, its constraints imply

$$
\sum_{j=1}^n A_{ij}q_j^*\le V
\qquad\text{for every }i.
$$

Thus, against Bob's strategy $q^*$, every pure row gives Alice an expected payoff of at most $V$.

Now let Alice use any mixed strategy $p\in\Delta_m$. Then

$$
\begin{aligned}
p^\top A q^*
&=\sum_{i=1}^m p_i
\left(\sum_{j=1}^n A_{ij}q_j^*\right)\\
&\le \sum_{i=1}^m p_i V\\
&=V\sum_{i=1}^m p_i\\
&=V.
\end{aligned}
$$

Therefore,

$$
\boxed{
p^\top A q^*\le V
\qquad\forall p\in\Delta_m.
}
$$

Bob guarantees that Alice's expected payoff is at most $V$.

## Step 4. Show that the payoff at the optimal strategies equals $V$

The two guarantees give

$$
(p^*)^\top A q\ge V
\qquad\forall q\in\Delta_n
$$

and

$$
p^\top A q^*\le V
\qquad\forall p\in\Delta_m.
$$

Set $q=q^*$ in Alice's guarantee:

$$
(p^*)^\top A q^*\ge V.
$$

Set $p=p^*$ in Bob's guarantee:

$$
(p^*)^\top A q^*\le V.
$$

Combining these inequalities yields

$$
\boxed{(p^*)^\top A q^*=V.}
$$

This completes the proof of the minimax theorem, including the existence of optimal strategies.

---

# Part 6. A numerical example

Let's illustrate the entire argument with a simple $2\times2$ game:

$$
A=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
$$

This is the payoff matrix for a matching-pennies-type game.

- If Alice and Bob choose the same index, Alice receives $1$.
- If they choose different indices, Alice receives $-1$.

Neither player can guarantee a positive payoff by choosing a single action.

## Step 1. Solve the primal LP

Let Alice choose row 1 with probability $p$ and row 2 with probability $1-p$, where

$$
0\le p\le 1.
$$

Against column 1, her expected payoff is

$$
p(1)+(1-p)(-1)=2p-1.
$$

Against column 2, her expected payoff is

$$
p(-1)+(1-p)(1)=1-2p.
$$

The primal LP is therefore equivalent to

$$
\begin{aligned}
\text{maximize}\quad &v\\
\text{subject to}\quad
&v\le 2p-1,\\
&v\le 1-2p,\\
&0\le p\le 1.
\end{aligned}
$$

Alice wants to maximize the smaller of $2p-1$ and $1-2p$.

At $p=\tfrac12$, the two expected payoffs are both zero:

$$
2\left(\frac12\right)-1=0,
$$

$$
1-2\left(\frac12\right)=0.
$$

Therefore, $v=0$ is feasible.

Could Alice guarantee a payoff greater than zero? That would require

$$
v\le 2p-1
\quad\text{and}\quad
v\le 1-2p
$$

with $v>0$. These inequalities would imply

$$
p>\frac12
\quad\text{and}\quad
p<\frac12,
$$

which is impossible.

Thus, the primal optimal solution is

$$
\boxed{p^*=\left(\frac12,\frac12\right),\qquad V=0.}
$$

## Step 2. Solve the dual LP

Let Bob choose column 1 with probability $q$ and column 2 with probability $1-q$.

If Alice chooses row 1, her expected payoff is

$$
q(1)+(1-q)(-1)=2q-1.
$$

If Alice chooses row 2, her expected payoff is

$$
q(-1)+(1-q)(1)=1-2q.
$$

The dual LP becomes

$$
\begin{aligned}
\text{minimize}\quad &w\\
\text{subject to}\quad
&2q-1\le w,\\
&1-2q\le w,\\
&0\le q\le 1.
\end{aligned}
$$

Bob wants to minimize the larger of $2q-1$ and $1-2q$.

At $q=\tfrac12$, both are zero. Hence $w=0$ is feasible.

No smaller value is possible because the two quantities sum to zero:

$$
(2q-1)+(1-2q)=0.
$$

Their maximum must therefore be nonnegative.

Consequently,

$$
\boxed{q^*=\left(\frac12,\frac12\right),\qquad w^*=0.}
$$

The primal and dual optimal values agree:

$$
\boxed{V=w^*=0.}
$$

## Step 3. Visualize the optimization

The following table shows Alice's expected payoff against each pure column when she uses probability $p$ for row 1.

| Alice's probability $p$ | Payoff against column 1 | Payoff against column 2 | Guaranteed payoff |
| --- | --- | --- | --- |
| $0$ | $-1$ | $1$ | $-1$ |
| $0.25$ | $-0.5$ | $0.5$ | $-0.5$ |
| $0.5$ | $0$ | $0$ | $0$ |
| $0.75$ | $0.5$ | $-0.5$ | $-0.5$ |
| $1$ | $1$ | $-1$ | $-1$ |

The guaranteed payoff is

$$
g(p)=\min\{2p-1,1-2p\}.
$$

Equivalently,

$$
g(p)=-|2p-1|.
$$

Its graph has a peak at $p=\tfrac12$:

```
Guaranteed
 payoff
   0             /\
                /  \
               /    \
  -0.5        /      \
             /        \
   -1       /          \
           +------------+
           0    0.5     1
             Probability p
```

The maximum of this graph is zero, achieved when Alice randomizes uniformly.

Bob's corresponding optimization is to minimize

$$
h(q)=\max\{2q-1,1-2q\}=|2q-1|.
$$

This graph has a minimum at $q=\tfrac12$.

```
Upper bound
 on payoff
    1       \          /
             \        /
   0.5        \      /
               \    /
    0           \  /
                 \/
           +------------+
           0    0.5     1
             Probability q
```

Both optimal values are zero.

This illustrates the minimax theorem: Alice maximizes her guaranteed payoff, while Bob minimizes the upper bound on Alice's payoff, and both arrive at the same value.

---

# Part 7. Why the theorem works even when entries are negative

The matrix entries need not be nonnegative.

For example, consider

$$
A=
\begin{pmatrix}
-3&-1\\
-2&-4
\end{pmatrix}.
$$

Every entry is negative, so Alice's payoff is always negative regardless of the strategies.

The minimax theorem still applies because:

1. Each expected payoff is a finite weighted average of real entries.
2. The probability vectors belong to compact simplices.
3. The primal LP is feasible and has a finite optimal value.
4. Its dual is the LP derived above.
5. Strong LP duality equates their optimal values.

The common value $V$ is simply negative in this case.

There is no requirement that the game be favorable to Alice or that the payoff matrix contain positive entries. The theorem concerns the equality of the two optimization values, not the sign of that value.

---

# Part 8. A useful geometric interpretation

The primal and dual can also be understood geometrically.

## Alice's perspective

For each column $j$, define the expected payoff

$$
g_j(p)=\sum_{i=1}^m A_{ij}p_i.
$$

Each $g_j(p)$ is a linear function of $p$.

Alice wants to maximize

$$
\min_j g_j(p).
$$

The primal LP introduces a variable $v$ and asks:

> How high can we raise the level $v$ while ensuring that every $g_j(p)$ stays at least $v$?

The feasible region is described by linear inequalities, so this is a linear programming problem.

## Bob's perspective

For each row $i$, define

$$
h_i(q)=\sum_{j=1}^n A_{ij}q_j.
$$

Bob wants to minimize

$$
\max_i h_i(q).
$$

The dual LP introduces a variable $w$ and asks:

> How low can we lower the level $w$ while ensuring that every $h_i(q)$ stays at most $w$?

This is also a linear programming problem.

The primal raises a lower bound on all relevant payoffs; the dual lowers an upper bound on all relevant payoffs.

Weak duality tells us that the primal lower bound cannot exceed the dual upper bound:

$$
v\le w.
$$

Strong duality tells us that, at optimality, the two bounds meet:

$$
\boxed{v^*=w^*=V.}
$$

This is the geometric and optimization-theoretic heart of the minimax theorem.

---

# Part 9. Common mistakes to avoid

### Mistake 1: Assuming Bob's optimal strategy must be pure

For a fixed $p$,

$$
\min_{q\in\Delta_n}p^\top A q
=
\min_j\sum_i A_{ij}p_i.
$$

This means Bob can use a pure best response to any fixed strategy $p$.

It does **not** mean Bob always has an optimal pure strategy for the overall game. An optimal mixed strategy may be necessary to minimize Alice's maximum payoff.

### Mistake 2: Treating $v$ as nonnegative

The primal variable $v$ is unrestricted:

$$
v\in\mathbb R.
$$

This is essential because the game value may be negative.

Likewise, the dual variable $w$ is unrestricted:

$$
w\in\mathbb R.
$$

### Mistake 3: Giving the wrong sign to the dual constraints

The primal payoff constraints are $\le$, so the associated dual variables satisfy

$$
q_j\ge 0.
$$

The primal variables $p_i$ are nonnegative, so their dual constraints are $\ge$ in the standard form:

$$
-\sum_j A_{ij}q_j+w\ge 0.
$$

Equivalently,

$$
\sum_j A_{ij}q_j\le w.
$$

### Mistake 4: Forgetting the normalization constraint

The primal equality

$$
\sum_i p_i=1
$$

produces the unrestricted dual variable $w$.

The unrestricted primal variable $v$ produces the dual equality

$$
\sum_j q_j=1.
$$

Both are necessary to obtain the two probability simplices.

### Mistake 5: Proving equality but not existence

Strong duality establishes equality of the optimal values. To prove the full theorem, we must also establish the existence of optimal primal and dual solutions.

The primal is feasible and has a finite optimal value. Standard LP existence and strong duality results therefore give optimal solutions on both sides.

Their feasibility constraints then provide the two guarantees.

---

# Part 10. The complete proof in a compact form

Here is a concise version suitable for an exam or written assignment.

**Proof.**

For any fixed $p\in\Delta_m$, the expression

$$
p^\top A q
=
\sum_{j=1}^n q_j\sum_{i=1}^m A_{ij}p_i
$$

is a convex combination of the column payoffs. Therefore,

$$
\min_{q\in\Delta_n}p^\top A q
=
\min_j\sum_i A_{ij}p_i.
$$

It follows that the given primal LP,

$$
\begin{aligned}
\max\quad &v\\
\text{subject to}\quad
&v-\sum_i A_{ij}p_i\le0,\quad j=1,\ldots,n,\\
&\sum_i p_i=1,\qquad p_i\ge0,\qquad v\in\mathbb R,
\end{aligned}
$$

has optimal value

$$
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.
$$

The primal is feasible by choosing any $p\in\Delta_m$ and taking $v=\min_j\sum_i A_{ij}p_i$. Its objective is bounded above because all expected payoffs are bounded by $\max_{i,j}|A_{ij}|$.

Introduce nonnegative dual variables $q_j$ for the payoff constraints and an unrestricted dual variable $w$ for the equality constraint. Since $v$ is unrestricted, its dual constraint is an equality. Since $p_i\ge0$, its dual constraints are inequalities of type $\ge$ in the standard form. Thus, the dual LP is

$$
\begin{aligned}
\min\quad &w\\
\text{subject to}\quad
&-\sum_j A_{ij}q_j+w\ge0,\quad i=1,\ldots,m,\\
&\sum_j q_j=1,\qquad q_j\ge0,\qquad w\in\mathbb R.
\end{aligned}
$$

Equivalently,

$$
\begin{aligned}
\min\quad &w\\
\text{subject to}\quad
&\sum_j A_{ij}q_j\le w,\quad i=1,\ldots,m,\\
&q\in\Delta_n.
\end{aligned}
$$

For fixed $q$, the smallest feasible $w$ is

$$
w=\max_i\sum_j A_{ij}q_j
=\max_{p\in\Delta_m}p^\top A q.
$$

Hence, the dual optimal value is

$$
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
$$

By strong LP duality, the primal and dual optimal values are equal. Therefore,

$$
\boxed{
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
}
$$

Finally, let $p^*$ and $(q^*,w^*)$ be optimal primal and dual solutions, and set $V=v^*=w^*$. Primal feasibility gives

$$
(p^*)^\top A q\ge V
\qquad\forall q\in\Delta_n,
$$

while dual feasibility gives

$$
p^\top A q^*\le V
\qquad\forall p\in\Delta_m.
$$

Taking $q=q^*$ in the first inequality and $p=p^*$ in the second yields

$$
(p^*)^\top A q^*\ge V
\quad\text{and}\quad
(p^*)^\top A q^*\le V.
$$

Thus,

$$
\boxed{(p^*)^\top A q^*=V.}
$$

This proves the minimax theorem and the existence of optimal mixed strategies. $\square$

---

## Final takeaway

The proof rests on three ideas:

1. **Expected payoffs are weighted averages.** For a fixed opponent strategy, the best response can be chosen as a pure action, which lets us express the game in terms of finitely many linear inequalities.
2. **The primal and dual LPs represent the two players' objectives.** Alice's primal maximizes a guaranteed lower bound $v$, while Bob's dual minimizes an upper bound $w$.
3. **Strong duality makes the bounds coincide.** At optimality,

$$
v^*=w^*=V,
$$

so Alice can guarantee at least $V$, Bob can hold Alice to at most $V$, and their optimal strategies yield expected payoff exactly $V$.

That is the fundamental connection between linear programming duality and the minimax theorem.
