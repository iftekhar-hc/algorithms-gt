# The Minimax Theorem via LP Duality — Step-by-Step

The main idea is to translate the game into a linear programming (LP) problem, derive its dual, and then use strong LP duality to prove that Alice's best guaranteed payoff equals Bob's best guaranteed upper bound.

We'll build the proof from the ground up, explain the dual derivation carefully, and finish with a numerical example and a visual interpretation.

## 1. Background: What are we trying to prove?

Suppose the payoff matrix is

$$
A=\begin{pmatrix}
A_{11}&\cdots&A_{1n}\\
\vdots&\ddots&\vdots\\
A_{m1}&\cdots&A_{mn}
\end{pmatrix}.
$$

Alice chooses a probability distribution $p$ over the rows, and Bob chooses a probability distribution $q$ over the columns.

Their expected payoff to Alice is

$$
p^\top A q.
$$

There are two ways to approach the game:

- Alice's perspective: Choose $p$ to make her worst-case expected payoff as large as possible.
- Bob's perspective: Choose $q$ to make Alice's best possible response as small as possible.

Mathematically, these are

$$
\underbrace{\max_{p\in\Delta_m}\min_{q\in\Delta_n}
p^\top A q}_{\text{Alice's guarantee}}
$$

and

$$
\underbrace{\min_{q\in\Delta_n}\max_{p\in\Delta_m}
p^\top A q}_{\text{Bob's guarantee}}.
$$

For any function of two variables, we always have the general inequality

$$
\max_p\min_q f(p,q)
\leq
\min_q\max_p f(p,q).
$$

Why? For every fixed pair $p,q$,

$$
\min_{q'}f(p,q')\leq f(p,q)
\leq \max_{p'}f(p',q).
$$

Taking the maximum over $p$ and then the minimum over $q$ gives the inequality.

The hard part is proving equality. The minimax theorem tells us that randomization allows both players to achieve matching guarantees. Strong LP duality will establish precisely this fact.

## 2. Part 1: Understand and formulate the primal LP

### Step 1.1 — Why does Bob's minimum reduce to a single column?

Fix Alice's mixed strategy $p$. Define the expected payoff against each pure column $j$ as

$$
c_j=\sum_{i=1}^{m}A_{ij}p_i.
$$

If Bob plays the mixed strategy $q$, Alice's expected payoff is

$$
p^\top A q=\sum_{j=1}^{n}q_jc_j.
$$

Since $q$ is a probability vector, this is a weighted average of $c_1,\ldots,c_n$. A weighted average cannot be smaller than the smallest number being averaged.

Therefore,

$$
p^\top A q\geq \min_j c_j.
$$

Bob can attain equality by putting probability $1$ on a column that minimizes $c_j$. Hence,

$$
\boxed{
\min_{q\in\Delta_n}p^\top A q
=
\min_{1\leq j\leq n}
\sum_{i=1}^{m}A_{ij}p_i.
}
$$

This is the key observation for Part 1.

### Step 1.2 — Interpret the variable $v$

The primal LP is

$$
\begin{aligned}
\max\quad &v\\
\text{subject to}\quad
&v-\sum_{i=1}^{m}A_{ij}p_i\leq 0,
&&j=1,\ldots,n,\\
&\sum_{i=1}^{m}p_i=1,\\
&p_i\geq0.
\end{aligned}
$$

Rearranging the first constraints gives

$$
v\leq \sum_{i=1}^{m}A_{ij}p_i
\qquad \text{for every }j.
$$

Thus, $v$ must be no greater than Alice's expected payoff against any pure column.

Visual interpretation of the primal

Choose Alice's probabilities

$p\in\Delta_m$

Calculate all column payoffs

$c_j=\sum_i A_{ij}p_i$

Find the smallest payoff

$v\leq \min_j c_j$

Maximize the guarantee

$\max_{p\in\Delta_m}\min_j c_j$

For any fixed $p$, the largest feasible $v$ is exactly $\min_j c_j$. Maximizing $v$ over all feasible $p$ therefore gives

$$
\boxed{
\operatorname{OPT}(P)
=\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.
}
$$

Here, $\operatorname{OPT}(P)$ denotes the optimal value of the primal LP.

### Step 1.3 — Prove feasibility

We must show that at least one feasible solution exists.

Choose any probability vector $p\in\Delta_m$, for example,

$$
p_1=1,\qquad p_2=\cdots=p_m=0.
$$

Now choose

$$
v=\min_{1\leq j\leq n}A_{1j}.
$$

Then $p_i\geq0$, the probabilities sum to $1$, and

$$
v\leq \sum_i A_{ij}p_i
$$

for every column $j$. So all constraints are satisfied.

Thus, the primal LP is feasible.

### Step 1.4 — Prove the objective is bounded above

Let

$$
M=\max_{i,j}A_{ij}.
$$

For every probability vector $p$ and every column $j$,

$$
\sum_i A_{ij}p_i\leq M.
$$

The LP constraints require $v\leq \sum_i A_{ij}p_i$, so $v\leq M$.

Therefore, the primal objective is bounded above. Because the feasible set is nonempty and the objective is bounded, the LP has a finite optimal value, attained by an optimal solution.

Part 1 is complete.

## 3. Part 2: Derive the dual LP

This is the most technical part. The safest approach is to derive the dual one constraint at a time, paying special attention to the unrestricted variable $v$.

### Step 2.1 — Label the primal constraints

Write the primal again:

$$
\begin{aligned}
\max\quad &v\\
\text{s.t.}\quad
&v-\sum_{i=1}^{m}A_{ij}p_i\leq0,
&&j=1,\ldots,n,\\
&\sum_{i=1}^{m}p_i=1,\\
&p_i\geq0,\qquad &v\in\mathbb R.
\end{aligned}
$$

Introduce the dual variables:

- $q_j$ for each of the $n$ inequality constraints.
- $w$ for the equality constraint $\sum_i p_i=1$.

The sign rules for a maximization primal are:

| Primal constraint or variable | Corresponding dual rule |
| --- | --- |
| Constraint $\leq$ | Dual variable $\geq0$ |
| Constraint $=$ | Dual variable unrestricted |
| Primal variable $\geq0$ | Dual constraint $\geq$ |
| Primal variable unrestricted | Dual constraint $=$ |

Applying these rules immediately gives

$$
q_j\geq0\quad(j=1,\ldots,n),
\qquad w\in\mathbb R.
$$

Also, the primal probability constraint $\sum_i p_i=1$ will ensure that $w$ has a meaningful interpretation.

### Step 2.2 — Derive the dual objective

The primal right-hand sides are:

- $0$ for each of the $n$ payoff constraints.
- $1$ for the equality constraint.

The dual objective is the sum of each dual variable multiplied by its corresponding right-hand side:

$$
\min\left(\sum_{j=1}^{n}0q_j+1w\right).
$$

Therefore, the dual objective is simply

$$
\boxed{\min w.}
$$

Notice that the objective is $w$, not $\sum_j q_j$.

### Step 2.3 — Derive the dual constraint corresponding to $v$

This is the most important sign check.

In the primal, the variable $v$ has coefficient $+1$ in every payoff constraint. It also does not appear in the probability equality constraint.

Therefore, the total coefficient of $v$ in the dual constraints is

$$
\sum_{j=1}^{n}q_j.
$$

Because $v$ is unrestricted in sign, its corresponding dual constraint must be an equality. The coefficient of $v$ in the primal objective is $1$, so

$$
\boxed{\sum_{j=1}^{n}q_j=1.}
$$

Together with $q_j\geq0$, this says exactly that

$$
q\in\Delta_n.
$$

This is the mathematical reason Bob's probability distribution appears in the dual.

### Step 2.4 — Derive the dual constraints corresponding to $p_i$

Fix a row $i$. In each payoff constraint

$$
v-\sum_{k=1}^{m}A_{kj}p_k\leq0,
$$

the coefficient of $p_i$ is $-A_{ij}$.

Multiplying these coefficients by their respective dual variables and adding the coefficient $+1$ from the probability equality constraint gives

$$
w-\sum_{j=1}^{n}A_{ij}q_j.
$$

Since $p_i\geq0$ in the primal maximization problem, the corresponding dual constraint must be greater than or equal to the coefficient of $p_i$ in the primal objective. That objective coefficient is $0$.

Thus,

$$
w-\sum_{j=1}^{n}A_{ij}q_j\geq0.
$$

Equivalently,

$$
\boxed{\sum_{j=1}^{n}A_{ij}q_j\leq w,
\qquad i=1,\ldots,m.}
$$

These constraints say that Alice's expected payoff against Bob's strategy $q$, when Alice plays any pure row $i$, is at most $w$.

### Step 2.5 — Write the complete dual

Combining everything, the dual LP is

$$
\boxed{
\begin{aligned}
\text{minimize}\quad &w\\
\text{subject to}\quad
&\sum_{j=1}^{n}A_{ij}q_j\leq w,
&&i=1,\ldots,m,\\
&\sum_{j=1}^{n}q_j=1,\\
&q_j\geq0,
&&j=1,\ldots,n,\\
&w\in\mathbb R.
\end{aligned}
}
$$

All sign restrictions are now explicit:

- $q_j\geq0$ for every $j$.
- $w$ is unrestricted in sign.

In particular, do not impose $w\geq0$. The entries of $A$ may be negative, so the game's value may also be negative.

### A useful way to remember the derivation

1. Payoff inequalities become $q_j\geq0$.

One dual variable for each column constraint.

2. Free primal variable $v$ gives $\sum_jq_j=1$.

This makes $q$ a probability distribution.

3. Each $p_i\geq0$ gives $\sum_j A_{ij}q_j\leq w$.

The variable $w$ upper-bounds Alice's payoff against every pure row.

## 4. Part 3: Interpret the dual and prove minimax

Now we have two LPs. The key is to recognize that they represent the two players' guarantees.

### Step 3.1 — Show that the dual represents Bob's guarantee

The dual is

$$
\begin{aligned}
\min\quad &w\\
\text{s.t.}\quad
&\sum_{j=1}^{n}A_{ij}q_j\leq w,
&&i=1,\ldots,m,\\
&q\in\Delta_n.
\end{aligned}
$$

Fix a probability vector $q$ for Bob. If Alice chooses pure row $i$, her expected payoff is

$$
\sum_{j=1}^{n}A_{ij}q_j.
$$

If Alice instead randomizes using $p$, her expected payoff is

$$
p^\top A q
=\sum_{i=1}^{m}p_i\left(\sum_{j=1}^{n}A_{ij}q_j\right).
$$

Again, this is a weighted average. Its maximum over $p\in\Delta_m$ is attained by a pure row with the largest expected payoff. Therefore,

$$
\boxed{
\max_{p\in\Delta_m}p^\top A q
=\max_{1\leq i\leq m}\sum_{j=1}^{n}A_{ij}q_j.
}
$$

The dual constraints require $w$ to be at least every one of these row payoffs. For fixed $q$, the smallest feasible $w$ is consequently

$$
w=\max_{1\leq i\leq m}\sum_j A_{ij}q_j.
$$

Minimizing over Bob's strategies gives

$$
\boxed{
\operatorname{OPT}(D)
=\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
}
$$

Thus, the dual LP finds Bob's best strategy for minimizing Alice's maximum possible expected payoff.

### Step 3.2 — Apply strong LP duality

We established in Part 1 that the primal is feasible and bounded above. Its dual is also feasible: choose any $q\in\Delta_n$, then choose $w$ sufficiently large to satisfy every dual inequality.

Strong LP duality therefore applies. It states that the primal and dual have optimal solutions and that their optimal objective values are equal:

$$
\operatorname{OPT}(P)=\operatorname{OPT}(D).
$$

Substituting the game interpretations of these values gives

$$
\boxed{
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
}
$$

This proves the minimax equality.

### Step 3.3 — Obtain the optimal strategies and game value

Strong LP duality also guarantees optimal solutions $(p^*,v^*)$ for the primal and $(q^*,w^*)$ for the dual, with

$$
v^*=w^*.
$$

Define

$$
V=v^*=w^*.
$$

Because $(p^*,v^*)$ is primal-feasible,

$$
v^*\leq\sum_i A_{ij}p_i^*
\qquad\text{for every }j.
$$

Multiplying each inequality by $q_j\geq0$ and summing over $j$, using $\sum_jq_j=1$, gives

$$
V\leq (p^*)^\top A q
\qquad\text{for every }q\in\Delta_n.
$$

This is Alice's guarantee.

Similarly, dual feasibility gives

$$
\sum_j A_{ij}q_j^*\leq w^*
\qquad\text{for every }i.
$$

Multiplying by $p_i\geq0$ and summing over $i$, using $\sum_ip_i=1$, gives

$$
p^\top A q^*\leq V
\qquad\text{for every }p\in\Delta_m.
$$

This is Bob's guarantee.

Finally, substitute $q=q^*$ into Alice's guarantee and $p=p^*$ into Bob's guarantee:

$$
V\leq(p^*)^\top A q^*\leq V.
$$

Therefore,

$$
\boxed{(p^*)^\top A q^*=V.}
$$

All the required conclusions follow.

## 5. Numerical example: Matching pennies

Let's see the primal and dual at work on a familiar game.

Suppose the payoff matrix is

$$
A=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
$$

Alice receives $+1$ when the choices match and $-1$ when they differ. Bob wants to minimize Alice's payoff.

PPT - Chapter 13 PowerPoint Presentation, free download - ID:527047

### Step 5.1 — Solve the primal

Let Alice play row 1 with probability $p$ and row 2 with probability $1-p$.

Her expected payoffs against the two columns are

$$
\begin{aligned}
c_1&=p-(1-p)=2p-1,\\
c_2&=-p+(1-p)=1-2p.
\end{aligned}
$$

The primal becomes

$$
\begin{aligned}
\max\quad &v\\
\text{s.t.}\quad
&v\leq2p-1,\\
&v\leq1-2p,\\
&0\leq p\leq1.
\end{aligned}
$$

Alice wants to maximize the smaller of $2p-1$ and $1-2p$.

The two expressions are equal when

$$
2p-1=1-2p
\quad\Longrightarrow\quad p=\frac12.
$$

At that point, both payoffs are zero. Thus,

$$
p^*=\left(\frac12,\frac12\right),
\qquad V=0.
$$

### Step 5.2 — Solve the dual

Let Bob choose column 1 with probability $q$ and column 2 with probability $1-q$.

The dual is

$$
\begin{aligned}
\min\quad &w\\
\text{s.t.}\quad
&2q-1\leq w,\\
&1-2q\leq w,\\
&0\leq q\leq1.
\end{aligned}
$$

The two row payoffs are equal at $q=\frac12$, so Bob also chooses uniformly:

$$
q^*=\left(\frac12,\frac12\right),
\qquad w^*=0.
$$

Consequently, both LPs have optimal value zero, just as strong duality predicts.

### Step 5.3 — Visualize the solution

The following chart shows Alice's two possible column payoffs as her probability $p$ changes.

Matching pennies: Alice's payoff against each column

The guaranteed payoff is the lower of the two lines. Its maximum occurs where the lines intersect.

|  | Column 1 | Column 2 |
| --- | --- | --- |
| 0 | -1 | 1 |
| 0.25 | -0.5 | 0.5 |
| 0.5 | 0 | 0 |
| 0.75 | 0.5 | -0.5 |
| 1 | 1 | -1 |

At $p=\frac12$, Alice's expected payoff is zero against either pure column. If she deviates from this probability, Bob can choose a column that makes her expected payoff negative.

The same reasoning applies to Bob: the uniform strategy prevents Alice from obtaining a positive expected payoff, regardless of which row she chooses.

This illustrates the minimax principle: each player randomizes to make the opponent indifferent between their available pure strategies.

## 6. A second useful example: Why negative payoffs are allowed

Consider the constant matrix

$$
A=\begin{pmatrix}
-3&-3\\
-3&-3
\end{pmatrix}.
$$

Regardless of their strategies, the expected payoff to Alice is $-3$.

The primal has optimal value $V=-3$, and the dual also has optimal value $w=-3$. Any probability vectors $p$ and $q$ are optimal.

This is why the dual variable $w$, like the primal variable $v$, must be unrestricted in sign. Adding the constraint $w\geq0$ would incorrectly exclude the correct solution.

## 7. Common mistakes to avoid

- Mistake 1: Assuming Bob must play a pure strategy. For a fixed $p$, Bob's best response can be chosen as a pure column. But Bob's optimal strategy for the overall game may need to be mixed.
- Mistake 2: Giving $v$ a nonnegativity constraint. The problem explicitly allows negative payoffs, so $v$ must be unrestricted.
- Mistake 3: Forgetting that the dual variable $w$ is unrestricted. It corresponds to the primal equality constraint.
- Mistake 4: Getting the sign of the dual constraints wrong. The primal coefficients of $p_i$ in the payoff constraints are $-A_{ij}$, which is why the dual constraints are $\sum_j A_{ij}q_j\leq w$.
- Mistake 5: Proving only the minimax equality. The problem also asks for optimal strategies satisfying both guarantees. Use optimal primal and dual solutions and the equality of their values to prove those statements.

## 8. Final proof checklist

Use this checklist to check your solution before submitting it.

Proof progress

0 of 7 complete

[ ]Show that a mixed strategy's expected payoff is a weighted average of its pure-column payoffs.

[ ]Interpret the primal as maximizing Alice's minimum payoff.

[ ]Prove primal feasibility and boundedness.

[ ]Derive the dual objective min w and all dual constraints.

[ ]Show that the dual minimizes Alice's maximum payoff over Bob's strategies.

[ ]Apply strong LP duality to equate the two optimal values.

[ ]Use optimal primal and dual solutions to prove both guarantees and equality at (p\*, q\*).

The central insight to remember is that Alice's strategy appears in the primal, Bob's strategy appears in the dual, and strong LP duality forces their optimal guarantees to be equal. That equality is the minimax theorem.
