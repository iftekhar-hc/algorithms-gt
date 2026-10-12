## 13. Minimax Theorem via LP Duality
### 13.1 Primal LP
For a fixed $p\in\Delta_m$, the expected payoff for Alice against a pure column $j$ as:

$$
c_j=\sum_{i=1}^{m}A_{ij}p_i.
$$

For a mixed strategy $q$ by Bob, the expected payoff for Alice is:

$$
p^\top A q=\sum_{j=1}^{n}q_jc_j.
$$

The above is a weighted average of $c_1,\ldots,c_n$ with $q$ being a probability vector. The weighted average must be at least as large as the smallest number. Hence,

$$
p^\top A q\geq \min_j c_j.
$$

Bob may choose a column with probability $1.0$ that minimizes $c_j$. This gives
us:
$$
\min_{q\in\Delta_n}p^\top A q
=
\min_{1\leq j\leq n}
\sum_{i=1}^{m}A_{ij}p_i.
$$

The primal LP is:

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

Rewriting the first constraint as:

$$
v\le\sum_{i=1}^mA_{ij}p_i,
\qquad j=1,\ldots,n.
$$

For a fixed $p$, we have $v\le c_j$ for every $j$. Hence,

$$
v\le\min_jc_j.
$$

Since the goal is to maximize $v$ for a fixed $p$, we choose:

$$
v=\min_jc_j.
$$

The primal LP objective is then:

$$
\max_{p\in\Delta_m}\min_j\sum_iA_{ij}p_i.
$$

Using the previous result, we obtain the following:

$$
\max_{p\in\Delta_m}\min_j\sum_iA_{ij}p_i
=
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q.
$$

The above gives the largest expected payoff for Alice.

To show feasibility, we let:

$$
v=\min_j\sum_iA_{ij}p_i \qquad\text{where } p_i=\frac1m \text{for all }i.
$$

Then all payoff constraints are satisfied since:

$$
v\le\sum_iA_{ij}p_i
\qquad\text{for every }j.
$$

We also have:

$$
p_i\ge0,
\qquad
\sum_ip_i=1.
$$

Therefore, the primal LP is feasible.

To show the objective is bounded above, we let:

$$
M=\max_{i,j}A_{ij}.
$$

We note that for all column $j$ and $p\in\Delta_m$, the following holds:

$$
\sum_iA_{ij}p_i\le M,
$$

because each entry in column $j$ is at most $M$ and the sum is a convex combination of the entries.

Since the primal constraints imply:

$$
v\le\sum_iA_{ij}p_i\le M.
$$

Therefore,

$$
v\le M.
$$

### 13.2 Dual LP

We introduce the following dual variables:

- $q_j$ for each of the $n$ inequality constraints.
- $w$ for the equality constraint.

We construct the dual objective by noting the following in the primal
right-hand side:

- $0$ for each of the $n$ inequality constraints.
- $1$ for the equality constraint.

The dual objective can be written as:
$$
\min\left(\sum_{j=1}^{n}0q_j+1w\right).
$$
Simplifying, we get the dual objective:
$$
\min w.
$$

To derive the dual constraint corresponding to $v$, we note that in the primal
LP, the variable $v$ has coefficient $+1$ in all inequality constraints.

Hence, the corresponding dual constraints are:
$$
\sum_{j=1}^{n}q_j.
$$

Since $v$ is unrestricted in sign, its corresponding dual constraint must be an equality. The coefficient of $v$ in the primal objective is $1$. Hence,

$$
\sum_{j=1}^{n}q_j=1.
$$

To derive the dual constraints corresponding to $p_i$, we note the following:

For a fixed row $i$ in $v-\sum_{k=1}^{m}A_{kj}p_k\leq0$, the coefficient of $p_i$ is $-A_{ij}$.

Multiplying these coefficients by their respective dual variables, we get:

$$
w-\sum_{j=1}^{n}A_{ij}q_j.
$$

Since the coefficient of $p_i$ is $0$ in the primal objective, the above is
constrained as follows:

$$
w-\sum_{j=1}^{n}A_{ij}q_j\geq0.
$$

Re-arranging we get:
$$
\sum_{j=1}^{n}A_{ij}q_j\leq w, \qquad i=1,\ldots,m.
$$

Putting everything together, the dual LP is:

$$
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
$$

### 13.3 Minimax Theorem and Optimality

For a fixed $q\in\Delta_n$, we define:

$$
r_i=\sum_{j=1}^nA_{ij}q_j=(Aq)_i.
$$

This is Alice’s expected payoff if she chooses pure row $i$ against Bob’s mixed strategy $q$.

For an arbitrary $p\in\Delta_m$,

$$
p^\top A q=\sum_{i=1}^mp_ir_i.
$$

This is a weighted average of $r_1,\ldots,r_m$. Hence,

$$
p^\top A q\le\max_i r_i.
$$

Alice can choose a row with probability $1$ to obtain the maximum. Thus,

$$
\max_{p\in\Delta_m}p^\top A q
=
\max_{1\le i\le m}\sum_{j=1}^nA_{ij}q_j.
$$

From the dual constraints, we have:

$$
\sum_jA_{ij}q_j\le w
\qquad \text{for every }i.
$$

Re-writing the above, we get:

$$
w\ge\max_i\sum_jA_{ij}q_j.
$$

For a fixed $q$, minimizing $w$ gives:

$$
w=\max_i\sum_jA_{ij}q_j.
$$

Therefore,

$$
\begin{aligned}
\min w
&=\min_{q\in\Delta_n}\max_i\sum_jA_{ij}q_j.
\end{aligned}
$$

Finally,

$$
\min w
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
$$

The above is Bob’s smallest guaranteed upper bound on Alice’s expected payoff.

From Part 1, we know that the primal LP is feasible and bounded above. From
Part 2, we have the corresponding dual LP.

The above allows us to apply strong LP duality which states that the primal and
dual have optimal solutions and optimal objective values are equal:

$$
\max_{p\in\Delta_m}\min_{q\in\Delta_n}p^\top A q
=
\min_{q\in\Delta_n}\max_{p\in\Delta_m}p^\top A q.
$$

This proves the minimax equality.

Strong LP duality also guarantees optimal solutions $(p^*,v^*)$ for the primal and $(q^*,w^*)$ for the dual, with:

$$
v^*=w^*.
$$

We define:

$$
V=v^*=w^*.
$$

Since $(p^*,V)$ is primal feasible, its constraints imply:

$$
V-\sum_{i=1}^m A_{ij}p_i^*\le 0
\qquad\text{for every }j.
$$

Equivalently,

$$
\sum_{i=1}^m A_{ij}p_i^*\ge V
\qquad\text{for every }j.
$$

Hence, Alice obtains an expected payoff of at least $V$ against every pure column.

Now, for any mixed strategy $q\in\Delta_n$ Bob uses, we have:

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

Hence,

$$
(p^*)^\top A q\ge V
\qquad\forall q\in\Delta_n.
$$

Based on the above, Alice guarantees a payoff of at least $V$.

Similarly, since $(q^*,V)$ is dual feasible, its constraints imply:

$$
\sum_{j=1}^n A_{ij}q_j^*\le V
\qquad\text{for every }i.
$$

Against Bob's strategy $q^*$, every pure row gives Alice an expected payoff of at most $V$.

Now, for any mixed strategy $p\in\Delta_m$ Alice uses, we have:

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

Hence,

$$
p^\top A q^*\le V
\qquad\forall p\in\Delta_m.
$$

Based on the above, Bob guarantees that Alice's expected payoff is at most $V$.





