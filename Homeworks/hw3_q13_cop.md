# Minimax Theorem via LP Duality

This problem connects three important ideas:

1. Mixed strategies turn game payoffs into linear functions.
2. A player’s worst-case guarantee can be written as a linear program.
3. The dual LP describes the opponent’s optimization problem.

The key conclusion is that the two players’ optimal guarantees are equal because the corresponding primal and dual LPs have equal optimal values.

---

## 1. Background: zero-sum matrix games

Let

$$
A \in \mathbb{R}^{m \times n}.
$$

- Alice chooses a row $i$.
- Bob chooses a column $j$.
- Alice receives $A_{ij}$.
- Bob receives $-A_{ij}$.

Because Bob’s payoff is exactly the negative of Alice’s payoff, this is a **zero-sum game**.

If Alice uses $p \in \Delta_m$ and Bob uses $q \in \Delta_n$, the expected payoff to Alice is

$$
p^\top A q.
$$

A useful way to visualize the calculation is

$$
\boxed{p \longrightarrow p^\top A \longrightarrow p^\top A q}
$$

where:

- $p^\top A$ gives Alice’s expected payoff against each pure column;
- multiplying by $q$ averages those column payoffs according to Bob’s probabilities.

Similarly,

$$
\boxed{q \longrightarrow Aq \longrightarrow p^\top A q}
$$

where $Aq$ gives Alice’s expected payoff for each pure row against Bob’s mixed strategy.

---

# Part 1: Alice’s optimization problem

## Step 1. Fix Alice’s mixed strategy

Fix some $p \in \Delta_m$, and define

$$
c_j = \sum_{i=1}^m A_{ij}p_i.
$$

The number $c_j$ is Alice’s expected payoff when:

- Alice uses $p$;
- Bob chooses the pure column $j$.

The complete vector of Alice’s payoffs against Bob’s pure strategies is

$$
p^\top A = (c_1,c_2,\ldots,c_n).
$$

For an arbitrary mixed strategy $q \in \Delta_n$,

$$
p^\top A q = \sum_{j=1}^n q_jc_j.
$$

Because $q_j \ge 0$ and $\sum_j q_j = 1$, this is a convex combination of the numbers

$$
c_1,\ldots,c_n.
$$

Every convex combination is at least the smallest number being combined:

$$
\sum_{j=1}^n q_jc_j \ge \min_{1\le j\le n}c_j.
$$

Therefore,

$$
p^\top A q \ge \min_{1\le j\le n}\sum_{i=1}^m A_{ij}p_i.
$$

Bob can attain equality by placing probability $1$ on a minimizing column. If

$$
j^* \in \operatorname*{arg\,min}_j c_j,
$$

then Bob chooses

$$
q = e_{j^*},
$$

where $e_{j^*}$ is the corresponding unit vector. Consequently,

$$
p^\top A e_{j^*} = c_{j^*} = \min_j c_j.
$$

Hence,

$$
\boxed{
\min_{q\in\Delta_n}p^\top A q
=
\min_{1\le j\le n}\sum_{i=1}^m A_{ij}p_i
}.
$$

### Important principle

When minimizing a linear function over a probability simplex, an optimum occurs at a vertex of the simplex. The vertices of $\Delta_n$ are exactly the pure strategies

$$
e_1,e_2,\ldots,e_n.
$$

Thus, after seeing Alice’s probability vector $p$, Bob never needs to mix in order to compute Alice’s worst-case payoff. He can choose one of his pure columns.

---

## Step 2. Interpret the primal LP

The primal LP is

$$
\begin{aligned}
\text{maximize}\quad &v\\
\text{subject to}\quad
&v-\sum_{i=1}^m A_{ij}p_i\le 0,
&&j=1,\ldots,n,\\
&\sum_{i=1}^m p_i=1,\\
&p_i\ge0,
&&i=1,\ldots,m,\\
&v\in\mathbb{R}.
\end{aligned}
$$

Rewrite the payoff constraints as

$$
v\le\sum_{i=1}^mA_{ij}p_i,
\qquad j=1,\ldots,n.
$$

For a fixed $p$, these constraints say

$$
v\le c_j
\qquad\text{for every }j.
$$

Equivalently,

$$
v\le\min_jc_j.
$$

Since the LP maximizes $v$, for a fixed $p$, it will choose

$$
v=\min_jc_j.
$$

Therefore, the primal objective becomes

$$
\max_{p\in\Delta_m}\min_j\sum_iA_{ij}p_i.
$$

Using the result from Step 1,

$$
\max_{p\in\Delta_m}\min_j\sum_iA_{ij}p_i
=
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.
$$

Thus,

$$
\boxed{
\operatorname{OPT}_P
=
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q
}.
$$

This is Alice’s largest guaranteed expected payoff.

---

## Visualization: Alice maximizes the lower envelope

For every column $j$, define

$$
f_j(p)=\sum_iA_{ij}p_i.
$$

Alice’s guaranteed payoff from $p$ is

$$
g(p)=\min_j f_j(p).
$$

Thus, Alice maximizes the lower envelope of several linear functions:

```text
Expected payoff
       ^
       |        / f_1(p)
       |       /
       |------*------ maximum of the lower envelope
       |     / \
       |    /   \ f_2(p)
       |___/_____\________________> Alice's mixed strategy p
           lower envelope
```

The variable $v$ represents the height of this lower envelope:

$$
v\le f_j(p)\qquad\text{for every }j.
$$

Alice pushes $v$ upward as far as possible while keeping it below every payoff function.

---

## Step 3. Show that the primal is feasible

Choose any probability vector, for example,

$$
p_i=\frac1m
\qquad
\text{for all }i.
$$

Now let

$$
v=\min_j\sum_iA_{ij}p_i.
$$

Then

$$
v\le\sum_iA_{ij}p_i
\qquad\text{for every }j.
$$

Therefore, all payoff constraints are satisfied. We also have

$$
p_i\ge0,
\qquad
\sum_ip_i=1.
$$

So the primal LP is feasible.

An even simpler choice is to take $p=e_1$ and then choose

$$
v\le\min_j A_{1j}.
$$

---

## Step 4. Show that the objective is bounded above

Let

$$
M=\max_{i,j}A_{ij}.
$$

For every $p\in\Delta_m$ and every column $j$,

$$
\sum_iA_{ij}p_i\le M,
$$

because this sum is a convex combination of entries from column $j$, each of which is at most $M$.

The primal constraints imply

$$
v\le\sum_iA_{ij}p_i\le M.
$$

Therefore,

$$
\boxed{v\le M}.
$$

So the primal objective is bounded above. Since the primal is feasible and has a finite optimal value, an optimal primal solution exists.

---

# Part 2: Deriving the dual LP

We derive the dual carefully because the primal contains:

- $\le$ constraints;
- an equality constraint;
- nonnegative variables $p_i$;
- an unrestricted variable $v$.

Introduce:

- $q_j\ge0$ for the payoff constraint corresponding to column $j$;
- $w\in\mathbb{R}$ for the equality constraint $\sum_i p_i=1$.

The sign rules are:

- A $\le$ constraint in this maximization formulation receives a nonnegative multiplier $q_j$.
- An equality constraint receives an unrestricted dual variable $w$.
- The unrestricted primal variable $v$ produces an equality constraint in the dual.

---

## Step 1. Form the Lagrangian

Write the constraints as

$$
v-\sum_iA_{ij}p_i\le0
$$

and

$$
1-\sum_ip_i=0.
$$

The Lagrangian is

$$
L(p,v;q,w)
=
v
-
\sum_{j=1}^nq_j
\left(v-\sum_{i=1}^mA_{ij}p_i\right)
+
w\left(1-\sum_{i=1}^mp_i\right).
$$

Expanding and rearranging by primal variable gives

$$
L
=
w
+
v\left(1-\sum_jq_j\right)
+
\sum_i p_i\left(\sum_jA_{ij}q_j-w\right).
$$

In matrix notation,

$$
L
=
w+v(1-\mathbf 1^\top q)
+
\sum_i p_i\left((Aq)_i-w\right).
$$

---

## Step 2. Constraint produced by unrestricted $v$

Because $v\in\mathbb{R}$ is unrestricted, the quantity

$$
v\left(1-\sum_jq_j\right)
$$

is bounded above over $v\in\mathbb{R}$ only if its coefficient is zero. Therefore,

$$
1-\sum_jq_j=0,
$$

or

$$
\boxed{\sum_{j=1}^nq_j=1}.
$$

This is exactly the probability normalization condition for Bob.

---

## Step 3. Constraints produced by $p_i\ge0$

For each $i$, the coefficient of $p_i$ is

$$
\sum_jA_{ij}q_j-w.
$$

Because $p_i\ge0$ and the Lagrangian is being maximized over $p_i$, the supremum is finite only if

$$
\sum_jA_{ij}q_j-w\le0.
$$

Thus,

$$
\boxed{
\sum_{j=1}^nA_{ij}q_j\le w,
\qquad i=1,\ldots,m
}.
$$

Equivalently,

$$
Aq\le w\mathbf 1.
$$

When these conditions hold, the supremum of the Lagrangian over the primal variables equals $w$. Therefore, the dual minimizes $w$.

---

## The dual LP

The dual is

$$
\boxed{
\begin{aligned}
\text{minimize}\quad &w\\
\text{subject to}\quad
&\sum_{j=1}^nA_{ij}q_j\le w,
&&i=1,\ldots,m,\\
&\sum_{j=1}^nq_j=1,\\
&q_j\ge0,
&&j=1,\ldots,n,\\
&w\in\mathbb{R}
&&\text{unrestricted in sign.}
\end{aligned}
}
$$

In compact form,

$$
\begin{aligned}
\text{minimize}\quad &w\\
\text{subject to}\quad
&Aq\le w\mathbf1,\\
&\mathbf1^\top q=1,\\
&q\ge0,\\
&w\text{ unrestricted}.
\end{aligned}
$$

Notice that

$$
q\ge0,
\qquad
\mathbf1^\top q=1
$$

means exactly that

$$
q\in\Delta_n.
$$

So the dual variables corresponding to Alice’s payoff constraints naturally form Bob’s mixed strategy.

---

# Part 3: Bob’s interpretation and the minimax theorem

## Step 1. Bob’s payoff bound for a fixed $q$

Fix $q\in\Delta_n$, and define

$$
r_i=\sum_{j=1}^nA_{ij}q_j=(Aq)_i.
$$

This is Alice’s expected payoff if she chooses pure row $i$ against Bob’s mixed strategy $q$.

For an arbitrary $p\in\Delta_m$,

$$
p^\top A q=\sum_{i=1}^mp_ir_i.
$$

This is a convex combination of $r_1,\ldots,r_m$. Therefore,

$$
p^\top A q\le\max_i r_i.
$$

Alice can attain this maximum by choosing a maximizing row with probability $1$. Thus,

$$
\boxed{
\max_{p\in\Delta_m}p^\top A q
=
\max_{1\le i\le m}\sum_{j=1}^nA_{ij}q_j
}.
$$

---

## Step 2. Interpret the dual objective

The dual constraints are

$$
\sum_jA_{ij}q_j\le w
\qquad \text{for every }i.
$$

Thus,

$$
w\ge\max_i\sum_jA_{ij}q_j.
$$

For a fixed $q$, minimizing $w$ gives

$$
w=\max_i\sum_jA_{ij}q_j.
$$

Therefore,

$$
\begin{aligned}
\operatorname{OPT}_D
&=\min_{q\in\Delta_n}\max_i\sum_jA_{ij}q_j\\
&=\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
\end{aligned}
$$

Hence,

$$
\boxed{
\operatorname{OPT}_D
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q
}.
$$

This is Bob’s smallest guaranteed upper bound on Alice’s payoff.

---

# Weak duality: why Alice cannot guarantee more than Bob allows

Suppose $(p,v)$ is primal feasible and $(q,w)$ is dual feasible.

Primal feasibility gives

$$
v\le\sum_iA_{ij}p_i
\qquad\text{for every }j.
$$

Multiply the $j$-th inequality by $q_j\ge0$ and sum over $j$:

$$
v\sum_jq_j
\le
\sum_jq_j\sum_iA_{ij}p_i.
$$

Since $\sum_jq_j=1$,

$$
v\le p^\top A q.
$$

Dual feasibility gives

$$
\sum_jA_{ij}q_j\le w
\qquad\text{for every }i.
$$

Multiply by $p_i\ge0$ and sum over $i$:

$$
p^\top A q\le w\sum_ip_i.
$$

Since $\sum_ip_i=1$,

$$
p^\top A q\le w.
$$

Combining the inequalities,

$$
\boxed{v\le p^\top A q\le w}.
$$

Therefore,

$$
\boxed{v\le w}.
$$

This is weak duality.

In game language:

```text
Alice's guaranteed value     actual expected payoff     Bob's upper bound
             v          <=          p^T A q          <=         w
```

Alice cannot guarantee a payoff larger than Bob’s guaranteed upper bound.

---

# Applying strong LP duality

The primal LP is feasible and bounded above. Its dual is also feasible. For example, choose any $q\in\Delta_n$ and take

$$
w\ge\max_i(Aq)_i.
$$

Strong LP duality therefore gives

$$
\operatorname{OPT}_P=\operatorname{OPT}_D.
$$

Using the game interpretations of the primal and dual,

$$
\boxed{
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q
}.
$$

This proves the minimax equality.

---

# Constructing $p^*$, $q^*$, and $V$

Let $(p^*,v^*)$ be an optimal primal solution, and let $(q^*,w^*)$ be an optimal dual solution.

By strong duality,

$$
v^*=w^*.
$$

Define

$$
\boxed{V=v^*=w^*}.
$$

We now prove the two guarantees.

## Alice’s guarantee

Primal feasibility says that, for every column $j$,

$$
V=v^*\le\sum_{i=1}^mA_{ij}p_i^*.
$$

Equivalently,

$$
(p^*)^\top Ae_j\ge V.
$$

Now let $q\in\Delta_n$ be arbitrary. Multiply the $j$-th inequality by $q_j\ge0$ and sum. Since $\sum_jq_j=1$,

$$
\boxed{
(p^*)^\top A q\ge V
\qquad\text{for every }q\in\Delta_n
}.
$$

Thus, Alice can guarantee at least $V$.

## Bob’s guarantee

Dual feasibility says that, for every row $i$,

$$
\sum_{j=1}^nA_{ij}q_j^*\le w^*=V.
$$

Equivalently,

$$
e_i^\top A q^*\le V.
$$

For arbitrary $p\in\Delta_m$, multiply the $i$-th inequality by $p_i\ge0$ and sum. Since $\sum_ip_i=1$,

$$
\boxed{
p^\top A q^*\le V
\qquad\text{for every }p\in\Delta_m
}.
$$

Thus, Bob can guarantee that Alice receives at most $V$.

## Payoff when both use optimal strategies

Apply Alice’s guarantee with $q=q^*$:

$$
(p^*)^\top A q^*\ge V.
$$

Apply Bob’s guarantee with $p=p^*$:

$$
(p^*)^\top A q^*\le V.
$$

Therefore,

$$
\boxed{(p^*)^\top A q^*=V}.
$$

This completes the proof.

---

# Complete logical flow

```text
Alice chooses p
      |
      v
Payoff against column j:
sum_i A_ij p_i
      |
      v
Worst column payoff:
min_j sum_i A_ij p_i
      |
      v
Primal LP maximizes this value
      |
      | strong LP duality
      v
Dual LP minimizes w
      |
      v
w bounds every row payoff:
sum_j A_ij q_j <= w
      |
      v
Bob minimizes Alice's best response
```

Symbolically,

$$
\begin{aligned}
\operatorname{OPT}_P
&=\max_{p\in\Delta_m}\min_j (p^\top A)_j\\
&=\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top Aq\\
&=\operatorname{OPT}_D\\
&=\min_{q\in\Delta_n}\max_i(Aq)_i\\
&=\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top Aq.
\end{aligned}
$$

---

# Example 1: matching pennies

Consider

$$
A=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
$$

Let Alice use

$$
p=
\begin{pmatrix}
x\\
1-x
\end{pmatrix},
\qquad 0\le x\le1.
$$

Her expected payoff against Bob’s first column is

$$
x(1)+(1-x)(-1)=2x-1.
$$

Against Bob’s second column, it is

$$
x(-1)+(1-x)(1)=1-2x.
$$

Therefore, Alice’s guaranteed payoff is

$$
g(x)=\min\{2x-1,1-2x\}.
$$

The first expression increases with $x$, while the second decreases:

```text
Payoff
  1 | \           /
    |  \         /
  0 |---\---*---/--------> x
    |    \ /
 -1 |     X
    0    1/2    1
```

The lower envelope reaches its maximum when

$$
2x-1=1-2x.
$$

Solving,

$$
4x=2,
\qquad
x=\frac12.
$$

The value is

$$
V=2\left(\frac12\right)-1=0.
$$

Thus,

$$
p^*=
\begin{pmatrix}
1/2\\
1/2
\end{pmatrix}.
$$

By symmetry,

$$
q^*=
\begin{pmatrix}
1/2\\
1/2
\end{pmatrix}.
$$

The game value is

$$
\boxed{V=0}.
$$

Neither player should use a deterministic strategy because the opponent could exploit it.

## Primal LP for matching pennies

The primal is

$$
\begin{aligned}
\text{maximize}\quad &v\\
\text{subject to}\quad
&v\le p_1-p_2,\\
&v\le-p_1+p_2,\\
&p_1+p_2=1,\\
&p_1,p_2\ge0.
\end{aligned}
$$

At the optimum, both payoff constraints are tight:

$$
v=p_1-p_2=-p_1+p_2.
$$

Thus,

$$
p_1=p_2=\frac12,
\qquad
v=0.
$$

---

# Example 2: a game with a pure-strategy saddle point

Consider

$$
A=
\begin{pmatrix}
3&1\\
4&2
\end{pmatrix}.
$$

Alice’s minimum payoff from each pure row is

$$
\begin{aligned}
\text{row 1:}&\quad \min\{3,1\}=1,\\
\text{row 2:}&\quad \min\{4,2\}=2.
\end{aligned}
$$

So Alice chooses row $2$ and guarantees $2$.

Bob examines the maximum payoff in each column:

$$
\begin{aligned}
\text{column 1:}&\quad \max\{3,4\}=4,\\
\text{column 2:}&\quad \max\{1,2\}=2.
\end{aligned}
$$

So Bob chooses column $2$, guaranteeing that Alice receives at most $2$.

Therefore,

$$
p^*=
\begin{pmatrix}
0\\
1
\end{pmatrix},
\qquad
q^*=
\begin{pmatrix}
0\\
1
\end{pmatrix},
\qquad
V=2.
$$

The entry $A_{22}=2$ is a saddle point:

$$
A_{i2}\le A_{22}\le A_{2j}
$$

for all rows $i$ and columns $j$.

Mixed strategies are permitted, but they are not needed in this example.

---

# Complementary slackness interpretation

Complementary slackness provides additional game-theoretic insight.

The primal payoff constraints have slacks

$$
s_j=(p^*)^\top Ae_j-V\ge0.
$$

Complementary slackness gives

$$
q_j^*s_j=0.
$$

Therefore,

$$
q_j^*>0
\quad\Longrightarrow\quad
(p^*)^\top Ae_j=V.
$$

So every column that Bob uses with positive probability gives Alice exactly $V$ against $p^*$.

Similarly, the dual constraint slack for row $i$ is

$$
t_i=V-e_i^\top Aq^*\ge0.
$$

Complementary slackness gives

$$
p_i^*t_i=0.
$$

Thus,

$$
p_i^*>0
\quad\Longrightarrow\quad
e_i^\top Aq^*=V.
$$

So every row that Alice uses with positive probability gives her exactly $V$ against $q^*$.

In summary:

$$
\boxed{p_i^*>0\implies (Aq^*)_i=V}
$$

and

$$
\boxed{q_j^*>0\implies ((p^*)^\top A)_j=V}.
$$

Strategies outside the support may perform worse for the player who could choose them, but every strategy used with positive probability must be optimal against the opponent’s equilibrium strategy.

---

# Common pitfalls

## 1. Confusing $\min_q$ with averaging over all columns

For fixed $p$,

$$
\min_{q\in\Delta_n}p^\top Aq
$$

does not mean Bob must average all columns. Bob can choose a pure strategy because pure strategies belong to $\Delta_n$.

## 2. Reversing the dual inequality

The dual constraint is

$$
\sum_jA_{ij}q_j\le w.
$$

The number $w$ is an upper bound on Alice’s payoff for every row, which is exactly what Bob wants to minimize.

## 3. Forgetting that $v$ and $w$ are unrestricted

Because entries of $A$ can be negative, the value of the game can be negative. Therefore, imposing

$$
v\ge0
\quad\text{or}\quad
w\ge0
$$

would incorrectly change the problem.

## 4. Forgetting the equality $\sum_jq_j=1$

The primal variable $v$ is unrestricted. Consequently, its corresponding dual constraint is an equality:

$$
\sum_jq_j=1.
$$

This is what turns the dual variables $q_j$ into a probability distribution.

---

# Final proof summary

1. For fixed $p$,

   $$
   \min_{q\in\Delta_n}p^\top Aq
   =
   \min_j\sum_iA_{ij}p_i.
   $$

2. Therefore, the primal LP computes

   $$
   \max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top Aq.
   $$

3. The dual LP is

   $$
   \begin{aligned}
   \text{minimize}\quad&w\\
   \text{subject to}\quad&Aq\le w\mathbf1,\\
   &\mathbf1^\top q=1,\\
   &q\ge0,\\
   &w\in\mathbb R.
   \end{aligned}
   $$

4. For fixed $q$,

   $$
   \max_{p\in\Delta_m}p^\top Aq
   =
   \max_i(Aq)_i.
   $$

5. Therefore, the dual computes

   $$
   \min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top Aq.
   $$

6. Strong LP duality gives

   $$
   \boxed{
   \max_p\min_q p^\top Aq
   =
   \min_q\max_p p^\top Aq
   }.
   $$

7. Optimal primal and dual solutions give $p^*,q^*$, and $V$ satisfying

   $$
   (p^*)^\top Aq\ge V
   \quad\text{for every }q,
   $$

   and

   $$
   p^\top Aq^*\le V
   \quad\text{for every }p.
   $$

8. In particular,

   $$
   \boxed{(p^*)^\top Aq^*=V}.
   $$

The central insight is that the primal protects Alice against every column, while the dual protects Bob against every row. Strong LP duality proves that the best lower guarantee and the best upper guarantee meet at the same value.
