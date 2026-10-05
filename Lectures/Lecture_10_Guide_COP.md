# Lecture 10: LP Duality and Max-Flow/Min-Cut

> **Course:** CS 6515: Graduate Algorithms  
> **Lecture:** 10  
> **Topics:** Optimality certificates, LP duality, weak and strong duality, path-based max flow, fractional edge lengths, threshold rounding, and max-flow/min-cut

## 1. Big Picture

The central idea is that an optimization solution becomes convincing only when we can provide a **certificate proving that no better solution exists**.

```text
Feasible primal solution
        ↓
provides a lower bound for a maximization problem

Feasible dual solution
        ↓
provides an upper bound for the same problem

Matching primal and dual values
        ↓
both solutions are optimal
```

For max flow, this becomes:

```text
Feasible flow  → lower bound on maximum flow
s-t cut        → upper bound on maximum flow

flow value = cut capacity
        ↓
maximum flow = minimum cut
```

---

## 2. The Smoothie Example

Consider the primal LP

$$
\begin{aligned}
\text{maximize}\quad
    &5x_1+4x_2+6x_3\\
\text{subject to}\quad
    &x_1+x_3\le 3,\\
    &2x_1+x_2+x_3\le 10,\\
    &2x_2+x_3\le 6,\\
    &x_1,x_2,x_3\ge 0.
\end{aligned}
$$

The constraints represent available oranges, bananas, and strawberries. The objective represents revenue.

Consider

$$
x=(3,3,0).
$$

It is feasible because

$$
3+0\le 3,
$$

$$
2(3)+3+0=9\le 10,
$$

and

$$
2(3)+0=6\le 6.
$$

Its objective value is

$$
5(3)+4(3)+6(0)=27.
$$

Therefore,

$$
\operatorname{OPT}\ge 27.
$$

Feasibility alone does not prove that 27 is optimal. There might be another feasible solution with a larger value.

### 2.1 Constructing an upper bound

Multiply the orange constraint by 5:

$$
5x_1+5x_3\le 15.
$$

Multiply the strawberry constraint by 2:

$$
4x_2+2x_3\le 12.
$$

Adding them gives

$$
5x_1+4x_2+7x_3\le 27.
$$

Because $x_3\ge 0$,

$$
5x_1+4x_2+6x_3
\le
5x_1+4x_2+7x_3
\le 27.
$$

Thus every feasible solution has value at most 27. Since the candidate solution has value 27, it is optimal.

### Key lesson

A feasible maximization solution says:

> Here is a value I can attain.

A certificate says:

> Here is why nobody can attain anything larger.

The dual LP searches for the best such certificate automatically.

---

## 3. Deriving the Canonical Dual

Consider the canonical primal:

$$
\begin{aligned}
(P)\qquad
\text{maximize}\quad &c^Tx\\
\text{subject to}\quad &Ax\le b,\\
&x\ge 0.
\end{aligned}
$$

Suppose $A$ has $m$ rows. Assign a nonnegative multiplier $y_j$ to primal constraint $j$. In vector notation, $y\ge 0$.

Multiplying the inequalities by these weights gives

$$
y^TAx\le y^Tb.
$$

To make this an upper bound on $c^Tx$, require

$$
A^Ty\ge c.
$$

Since $x\ge0$, the componentwise inequality $A^Ty\ge c$ implies

$$
c^Tx\le (A^Ty)^Tx.
$$

Therefore,

$$
c^Tx
\le
x^TA^Ty
=
y^TAx
\le
y^Tb.
$$

Every vector $y$ satisfying

$$
A^Ty\ge c,
\qquad
y\ge0
$$

provides an upper bound $b^Ty$. We therefore minimize that upper bound:

$$
\begin{aligned}
(D)\qquad
\text{minimize}\quad &b^Ty\\
\text{subject to}\quad &A^Ty\ge c,\\
&y\ge0.
\end{aligned}
$$

This is the **dual LP**.

---

## 4. Primal-Dual Correspondence

| Primal | Dual |
|---|---|
| Maximization | Minimization |
| One variable $x_i$ | One dual constraint |
| One constraint $j$ | One dual variable $y_j$ |
| Matrix $A$ | Transposed matrix $A^T$ |
| Objective coefficients $c$ | Dual right-hand side |
| Right-hand side $b$ | Dual objective coefficients |
| $Ax\le b$ | $y\ge0$ |
| $x\ge0$ | $A^Ty\ge c$ |

A useful memory aid is:

```text
constraints ↔ variables
b           ↔ objective coefficients
c           ↔ right-hand sides
A           ↔ Aᵀ
max         ↔ min
≤           ↔ ≥
```

### 4.1 Why the signs matter

If $a\le b$ and $y\ge0$, then

$$
ya\le yb.
$$

Multiplication by a negative number reverses the inequality. Nonnegative dual weights therefore preserve the directions of the primal $\le$ constraints.

Likewise, if

$$
A^Ty\ge c
$$

componentwise and $x\ge0$, then

$$
x^TA^Ty\ge x^Tc.
$$

If some $x_i$ were negative, multiplying the corresponding coefficient inequality by $x_i$ could reverse its direction.

---

## 5. Weak Duality

### Theorem

For every primal-feasible $x$ and dual-feasible $y$,

$$
c^Tx\le b^Ty.
$$

### Proof

$$
\boxed{
c^Tx
\le
x^TA^Ty
=
y^TAx
\le
y^Tb
}
$$

The first inequality uses

$$
A^Ty\ge c,
\qquad
x\ge0.
$$

The second uses

$$
Ax\le b,
\qquad
y\ge0.
$$

Every dual-feasible solution is therefore an upper-bound certificate for every primal-feasible solution.

### Optimality consequence

If feasible $x$ and $y$ satisfy

$$
c^Tx=b^Ty,
$$

then both are optimal.

---

## 6. The Smoothie Dual

The smoothie dual is

$$
\begin{aligned}
\text{minimize}\quad
&3y_O+10y_B+6y_S\\
\text{subject to}\quad
&y_O+2y_B\ge5,\\
&y_B+2y_S\ge4,\\
&y_O+y_B+y_S\ge6,\\
&y_O,y_B,y_S\ge0.
\end{aligned}
$$

Each dual variable is associated with a resource:

- $y_O$: price of one unit of oranges
- $y_B$: price of one unit of bananas
- $y_S$: price of one unit of strawberries

Each constraint says that the imputed ingredient cost of a smoothie must be at least its revenue. Thus the value of the entire priced inventory is an upper bound on total production revenue.

Take

$$
y=(5,0,2).
$$

The constraints become

$$
5+2(0)=5\ge5,
$$

$$
0+2(2)=4\ge4,
$$

and

$$
5+0+2=7\ge6.
$$

The dual objective is

$$
3(5)+10(0)+6(2)=27.
$$

Since the primal solution $x=(3,3,0)$ also has value 27, weak duality proves both are optimal.

### Lecture exercise

For

$$
y=(3,1,2),
$$

the constraints are

$$
3+2(1)=5,
$$

$$
1+2(2)=5\ge4,
$$

and

$$
3+1+2=6.
$$

It is dual feasible, and its upper bound is

$$
3(3)+10(1)+6(2)=31.
$$

It is a valid certificate, but not the best certificate because the tighter dual certificate gives 27.

---

## 7. Strong Duality

### Theorem

If the primal is feasible and has a finite optimum, then the dual has an optimum and

$$
\max\{c^Tx:Ax\le b,\ x\ge0\}
=
\min\{b^Ty:A^Ty\ge c,\ y\ge0\}.
$$

Weak duality says:

> No primal value can exceed any dual value.

Strong duality adds:

> There exist optimal primal and dual solutions whose values match exactly.

Thus a finite LP optimum has an exact dual certificate.

---

## 8. Infeasible Versus Unbounded

- **Infeasible:** no point satisfies all constraints.
- **Unbounded:** feasible solutions exist, but the objective can improve without limit.

The following implications hold:

$$
\text{primal unbounded above}
\implies
\text{dual infeasible},
$$

and

$$
\text{dual unbounded below}
\implies
\text{primal infeasible}.
$$

Both primal and dual may be infeasible, so the converses do not generally hold.

If the dual contained a feasible $y$, then $b^Ty$ would be a finite upper bound on every primal solution. Hence, the primal could not be unbounded above.

---

## 9. General Duality Rulebook

For a maximization primal:

| Primal feature | Dual feature |
|---|---|
| Constraint $a_j^Tx\le b_j$ | $y_j\ge0$ |
| Constraint $a_j^Tx\ge b_j$ | $y_j\le0$ |
| Constraint $a_j^Tx=b_j$ | $y_j$ unrestricted |
| Variable $x_i\ge0$ | $(A^Ty)_i\ge c_i$ |
| Variable $x_i\le0$ | $(A^Ty)_i\le c_i$ |
| Variable $x_i$ unrestricted | $(A^Ty)_i=c_i$ |

### Why equality means unrestricted

An equality can be multiplied by either a positive or negative number without losing validity. Its dual multiplier may therefore have either sign.

### Why an unrestricted primal variable creates equality

If $x_i$ can be positive or negative, the coefficient comparison must work in both directions. The only possibility is

$$
(A^Ty)_i=c_i.
$$

---

## 10. Max Flow as a Path-Based LP

Let $\mathcal P$ be the set of all simple directed $s$-$t$ paths. Introduce a variable

$$
x_p\ge0
$$

representing the amount of flow routed along path $p$.

The path-based max-flow LP is

$$
\begin{aligned}
\text{maximize}\quad
&\sum_{p\in\mathcal P}x_p\\
\text{subject to}\quad
&\sum_{\substack{p\in\mathcal P\\e\in p}}x_p\le c_e
&&\text{for every }e\in E,\\
&x_p\ge0
&&\text{for every }p\in\mathcal P.
\end{aligned}
$$

The objective is total flow. Each edge constraint says that the combined flow of paths using edge $e$ cannot exceed its capacity.

### Example

Suppose the network has paths

$$
p_1:s\to a\to t,
\qquad
p_2:s\to b\to t,
\qquad
p_3:s\to a\to b\to t.
$$

If edge $(s,a)$ has capacity 5, then

$$
x_{p_1}+x_{p_3}\le5.
$$

If edge $(b,t)$ has capacity 4, then

$$
x_{p_2}+x_{p_3}\le4.
$$

The paths interact because they share edge capacities.

### Important warning

There may be exponentially many simple $s$-$t$ paths. This formulation is mainly a mathematical device for understanding duality, not a recommendation to enumerate all paths.

---

## 11. Flow Decomposition

Any nonnegative feasible flow can be decomposed into:

1. $s$-$t$ path flows, and
2. directed cycle flows.

Cycle flow does not contribute to the net amount delivered from $s$ to $t$. Discarding cycles leaves a path-flow solution with the same value.

### Pseudocode

```text
FLOW-DECOMPOSITION(G, f, s, t):
    path_flows ← empty list

    while there is an s-t path p using only edges with f(e) > 0:
        δ ← minimum f(e) over edges e in p
        append (p, δ) to path_flows

        for each edge e in p:
            f(e) ← f(e) - δ

    while there is a directed cycle C using only edges with f(e) > 0:
        δ ← minimum f(e) over edges e in C

        for each edge e in C:
            f(e) ← f(e) - δ

    return path_flows
```

Each iteration makes at least one positive-flow edge reach zero.

---

## 12. The Dual as Fractional Edge Lengths

There is one primal constraint per edge, so introduce one dual variable $y_e\ge0$ per edge:

$$
\begin{aligned}
\text{minimize}\quad
&\sum_{e\in E}c_ey_e\\
\text{subject to}\quad
&\sum_{e\in p}y_e\ge1
&&\text{for every }p\in\mathcal P,\\
&y_e\ge0
&&\text{for every }e\in E.
\end{aligned}
$$

Interpret $y_e$ as the length assigned to edge $e$. Every $s$-$t$ path must have total length at least 1. The objective minimizes the capacity-weighted total length.

---

## 13. Why Every Cut Gives a Feasible Dual Solution

Let $S\subseteq V$ satisfy

$$
s\in S,
\qquad
t\notin S.
$$

Define

$$
y_e=
\begin{cases}
1,&e\in\delta^+(S),\\
0,&\text{otherwise},
\end{cases}
$$

where

$$
\delta^+(S)=\{(u,v)\in E:u\in S,\ v\notin S\}.
$$

Every $s$-$t$ path must leave $S$ at least once. Therefore,

$$
\sum_{e\in p}y_e\ge1
$$

for every $s$-$t$ path $p$.

The objective value is

$$
\sum_{e\in E}c_ey_e
=
\sum_{e\in\delta^+(S)}c_e
=
c(\delta^+(S)),
$$

which is the capacity of the cut.

Thus,

$$
\text{value of any flow}
\le
\text{capacity of any cut}.
$$

This is weak duality specialized to max flow.

---

## 14. Rounding Fractional Lengths into a Cut

A cut corresponds to a $0/1$ length assignment, but the dual permits arbitrary nonnegative real lengths. The lecture converts any feasible fractional solution into an actual cut using shortest-path distances and threshold rounding.

### 14.1 Shortest-path distances

Given feasible dual lengths $y$, let

$$
d(v)=\text{shortest-path distance from }s\text{ to }v.
$$

Define clipped distances

$$
\ell(v)=\min\{d(v),1\}.
$$

Then

$$
\ell(s)=0,
\qquad
\ell(t)=1.
$$

For a threshold $r\in(0,1)$, define

$$
S_r=\{v:\ell(v)\le r\}.
$$

Because $\ell(s)=0$ and $\ell(t)=1$,

$$
s\in S_r,
\qquad
t\notin S_r.
$$

Thus every $S_r$ is an $s$-$t$ cut.

### 14.2 When does an edge cross the threshold cut?

An edge $e=(u,v)$ leaves $S_r$ exactly when

$$
\ell(u)\le r<\ell(v).
$$

As $r$ ranges from 0 to 1, edge $(u,v)$ is included in the cut for an interval whose length is

$$
\max\{0,\ell(v)-\ell(u)\}.
$$

The shortest-path triangle inequality gives

$$
d(v)\le d(u)+y_{uv}.
$$

Clipping cannot increase the positive difference, so

$$
\max\{0,\ell(v)-\ell(u)\}\le y_{uv}.
$$

### 14.3 Averaging the cut capacities

The capacity of threshold cut $S_r$ is

$$
c(\delta^+(S_r))
=
\sum_{(u,v)\in E}
c_{uv}\mathbf 1[\ell(u)\le r<\ell(v)].
$$

Average over $r\in(0,1)$:

$$
\begin{aligned}
\int_0^1 c(\delta^+(S_r))\,dr
&=
\sum_{(u,v)\in E}
c_{uv}\max\{0,\ell(v)-\ell(u)\}\\
&\le
\sum_{(u,v)\in E}c_{uv}y_{uv}.
\end{aligned}
$$

Therefore, the average threshold-cut capacity is no greater than the fractional dual objective. At least one threshold $r$ satisfies

$$
c(\delta^+(S_r))
\le
\sum_{e\in E}c_ey_e.
$$

This converts any feasible fractional dual solution into an actual cut without increasing its cost.

---

## 15. Threshold-Rounding Example

Suppose the clipped distances are

$$
\ell(s)=0,
\qquad
\ell(a)=0.25,
\qquad
\ell(b)=0.65,
\qquad
\ell(t)=1.
$$

```text
0 ------ 0.25 -------- 0.65 -------- 1
s          a              b           t
```

The threshold cuts are:

- $0<r<0.25$: $S_r=\{s\}$
- $0.25\le r<0.65$: $S_r=\{s,a\}$
- $0.65\le r<1$: $S_r=\{s,a,b\}$

Only these distinct cuts need to be checked.

For edge $(a,b)$, the edge crosses a threshold cut when

$$
0.25\le r<0.65.
$$

The interval length is

$$
0.65-0.25=0.40.
$$

The proof guarantees that this is no greater than $y_{ab}$.

---

## 16. Deterministic Threshold-Rounding Pseudocode

```text
ROUND-LENGTHS-TO-CUT(G, c, y, s, t):
    d ← DIJKSTRA(G, source=s, edge_lengths=y)

    for each vertex v:
        if v is unreachable:
            ℓ(v) ← 1
        else:
            ℓ(v) ← min(d(v), 1)

    thresholds ← sorted distinct values ℓ(v) with 0 ≤ ℓ(v) < 1

    best_cut ← null
    best_capacity ← +∞

    for each threshold r in thresholds:
        S ← {v : ℓ(v) ≤ r}

        cut_capacity ← 0
        for each directed edge (u, v):
            if u ∈ S and v ∉ S:
                cut_capacity ← cut_capacity + c(u, v)

        if cut_capacity < best_capacity:
            best_capacity ← cut_capacity
            best_cut ← S

    return best_cut, best_capacity
```

Because the cut changes only when the threshold passes a vertex distance, checking the distinct clipped distances is sufficient.

---

## 17. Verifying Exponentially Many Path Constraints

The dual contains one constraint for every $s$-$t$ path:

$$
\sum_{e\in p}y_e\ge1.
$$

There may be exponentially many such paths, but all constraints are satisfied exactly when the shortest $s$-$t$ path has length at least 1.

```text
VERIFY-DUAL-LENGTHS(G, y, s, t):
    d, parent ← DIJKSTRA(G, source=s, edge_lengths=y)

    if d(t) ≥ 1 or t is unreachable:
        return "All path constraints are satisfied"
    else:
        p ← reconstruct path from parent pointers
        return "Violated constraint", p
```

If $d(t)<1$, the shortest path itself is a violated constraint. If $d(t)\ge1$, every other $s$-$t$ path is at least as long.

---

## 18. Completing Max-Flow/Min-Cut

The proof combines three facts.

### Fact 1: Every flow is bounded by every cut

$$
\text{maximum-flow value}
\le
\text{minimum-cut capacity}.
$$

### Fact 2: Threshold rounding converts fractional lengths to a cut

$$
\text{minimum-cut capacity}
\le
\text{optimal length-dual value}.
$$

### Fact 3: Strong LP duality

$$
\text{optimal length-dual value}
=
\text{maximum-flow value}.
$$

Together,

$$
\text{maximum flow}
\le
\text{minimum cut}
\le
\text{optimal dual}
=
\text{maximum flow}.
$$

The endpoints are equal, so every inequality is equality:

$$
\boxed{
\text{maximum-flow value}
=
\text{minimum-cut capacity}
}
$$

---

## 19. What Is Integral Here?

The rounding argument proves that the fractional length dual has an optimal $0/1$ solution corresponding to a cut, even if capacities are arbitrary nonnegative real numbers.

This differs from flow integrality:

- **Cut-side integrality:** an optimal dual length solution can be chosen as a $0/1$ cut indicator.
- **Flow integrality:** an integral maximum flow is guaranteed when capacities are integral.

These are distinct statements.

---

## 20. Conceptual Connections

### 20.1 Certificate perspective

| Problem | Candidate solution | Certificate |
|---|---|---|
| Smoothie LP | Production quantities $x$ | Resource prices $y$ |
| Max flow | Feasible flow | Cut or fractional edge lengths |
| Primal maximization | Feasible $x$ | Dual-feasible $y$ |

A proposed solution is optimal when its value matches the certificate's bound.

### 20.2 Economic interpretation

The primal asks:

> How should limited resources be consumed to maximize reward?

The dual asks:

> How should each resource be priced so that every activity costs at least the reward it generates?

The optimal dual variables are often called **shadow prices**. A scarce, fully used resource may receive a positive price. A resource whose availability is not limiting may receive price zero.

This intuition anticipates complementary slackness:

- unused resource $\Rightarrow$ often zero dual price;
- produced activity $\Rightarrow$ often a tight dual constraint.

### 20.3 Approximation-algorithm preview

Max-flow/min-cut rounding loses nothing:

$$
\text{rounded cut value}
\le
\text{fractional objective}.
$$

For other combinatorial problems, rounding may introduce a bounded loss. A common template is:

```text
1. Formulate a discrete problem as an integer program.
2. Relax integrality to obtain an LP.
3. Solve or reason about the fractional LP.
4. Round the fractional solution.
5. Bound the loss caused by rounding.
```

---

# Quiz Questions

## A. Concept Checks

1. What does a primal-feasible solution provide for a maximization LP?
2. What does a dual-feasible solution provide?
3. State weak duality.
4. Why must the multipliers for canonical $\le$ constraints be nonnegative?
5. If feasible $x$ and $y$ satisfy $c^Tx=b^Ty$, what can you conclude?
6. What is the difference between weak and strong duality?
7. Does primal infeasibility necessarily imply dual unboundedness?
8. Why does one primal constraint correspond to one dual variable?
9. Why does one primal variable correspond to one dual constraint?
10. What does the transpose $A^T$ accomplish in the dual?
11. In the smoothie example, what is the economic meaning of $y_B=0$?
12. Why is the path-based flow LP potentially exponential in size?
13. What does the path-flow variable $x_p$ represent?
14. What does the dual variable $y_e$ represent?
15. Why does every $s$-$t$ path cross an $s$-$t$ cut?
16. Why is every cut indicator a feasible length-dual solution?
17. Why is Dijkstra sufficient to verify every dual path constraint?
18. What role does clipping $d(v)$ at 1 play?
19. Why is every $S_r$ an $s$-$t$ cut?
20. Explain the statement, “At least one value is no larger than the average.”

## B. Quiz Answers

1. A lower bound on the optimal value.
2. An upper bound on the optimal value.
3. For primal-feasible $x$ and dual-feasible $y$, $c^Tx\le b^Ty$.
4. Negative multiplication would reverse an inequality.
5. Both solutions are optimal.
6. Weak duality provides an inequality; strong duality says finite optimal values match.
7. No. Both LPs may be infeasible.
8. Each primal constraint receives a multiplier.
9. The weighted constraint coefficients must dominate the objective coefficient of each variable.
10. It converts row multipliers into one coefficient condition per primal variable.
11. Bananas are not the limiting resource at the displayed optimum.
12. A graph may contain exponentially many simple $s$-$t$ paths.
13. Flow routed along path $p$.
14. A nonnegative edge length or price.
15. The path begins in $S$ and ends outside $S$.
16. Every path has at least one cut edge and hence length at least 1.
17. The shortest $s$-$t$ path is the minimum left-hand side among all path constraints.
18. It restricts thresholds to $[0,1]$ without increasing relevant positive distance differences.
19. $s$ has clipped distance 0 and $t$ has clipped distance 1.
20. If every value exceeded the average, their average would also exceed itself.

---

# Exam-Style Questions

## Question 1: Constructing a Dual

Consider

$$
\begin{aligned}
\text{maximize}\quad&4x_1+7x_2\\
\text{subject to}\quad
&2x_1+x_2\le8,\\
&x_1+3x_2\le9,\\
&x_1,x_2\ge0.
\end{aligned}
$$

### Tasks

1. Write the dual.
2. Find primal- and dual-feasible solutions with matching objective values.
3. Use weak duality to prove optimality.

### Solution outline

The dual is

$$
\begin{aligned}
\text{minimize}\quad&8y_1+9y_2\\
\text{subject to}\quad
&2y_1+y_2\ge4,\\
&y_1+3y_2\ge7,\\
&y_1,y_2\ge0.
\end{aligned}
$$

Solving the two tight primal constraints gives

$$
x_1=3,
\qquad
x_2=2,
$$

with value

$$
4(3)+7(2)=26.
$$

Solving the two tight dual constraints gives

$$
y_1=1,
\qquad
y_2=2,
$$

with value

$$
8(1)+9(2)=26.
$$

Since the feasible objective values match, both solutions are optimal.

## Question 2: Mixed Constraint Directions

Construct the dual of

$$
\begin{aligned}
\text{maximize}\quad&3x_1-2x_2\\
\text{subject to}\quad
&x_1+x_2\le5,\\
&2x_1-x_2\ge1,\\
&x_1\ge0,\quad x_2\text{ unrestricted}.
\end{aligned}
$$

### Expected answer

Let $y_1\ge0$ correspond to the $\le$ constraint and $y_2\le0$ correspond to the $\ge$ constraint. Then

$$
\begin{aligned}
\text{minimize}\quad&5y_1+y_2\\
\text{subject to}\quad
&y_1+2y_2\ge3,\\
&y_1-y_2=-2,\\
&y_1\ge0,\quad y_2\le0.
\end{aligned}
$$

The equality in the second dual constraint results from $x_2$ being unrestricted.

## Question 3: Weak-Duality Proof

Prove weak duality for

$$
\max\{c^Tx:Ax\le b,\ x\ge0\}
$$

and

$$
\min\{b^Ty:A^Ty\ge c,\ y\ge0\}.
$$

Identify exactly where each feasibility condition is used.

### Expected structure

$$
c^Tx
\le
(A^Ty)^Tx
=
y^TAx
\le
y^Tb.
$$

Explain:

- $A^Ty\ge c$ and $x\ge0$ justify the first inequality;
- $Ax\le b$ and $y\ge0$ justify the second.

## Question 4: Path-Flow LP and Dual

Given a directed capacitated graph $G=(V,E)$, derive the path-based maximum-flow LP and its dual. Interpret each dual variable and each dual constraint.

A complete answer should include:

- one variable $x_p$ per simple $s$-$t$ path;
- one capacity constraint per edge;
- dual variable $y_e$ interpreted as edge length;
- one dual constraint per path requiring length at least 1;
- objective $\sum_e c_ey_e$;
- an explanation of why a cut creates a feasible $0/1$ dual solution.

## Question 5: Threshold-Rounding Proof

Let $y$ be a feasible solution of the length dual. Define

$$
\ell(v)=\min\{d_y(s,v),1\}
$$

and

$$
S_r=\{v:\ell(v)\le r\}.
$$

Prove that some threshold $r\in(0,1)$ satisfies

$$
c(\delta^+(S_r))
\le
\sum_e c_ey_e.
$$

### Expected proof steps

1. Show $\ell(s)=0$ and $\ell(t)=1$.
2. Conclude that every $S_r$ is an $s$-$t$ cut.
3. Show edge $(u,v)$ crosses exactly for thresholds satisfying $\ell(u)\le r<\ell(v)$.
4. Bound the interval length by $y_{uv}$.
5. Integrate the cut capacity over $r\in(0,1)$.
6. Apply the fact that some value is at most the average.

## Question 6: Separation Procedure

The length dual contains exponentially many path constraints. Design an algorithm that either verifies all constraints or returns a violated path constraint.

### Expected answer

Run Dijkstra using $y_e$ as edge lengths.

- If $d(s,t)\ge1$, every path constraint is satisfied.
- If $d(s,t)<1$, return the shortest path as a violated constraint.

## Question 7: Integrality Distinction

Explain why these statements are different:

1. The length dual has an optimal $0/1$ solution.
2. The maximum-flow LP has an integral optimal solution when capacities are integral.

A strong answer should identify that the first concerns cut indicators and holds for nonnegative real capacities, while the second concerns the primal flow variables and requires integral capacities.

---

# Textbook and Supplementary References

1. Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms*, 4th ed. MIT Press. See the chapters on linear programming and maximum flow.  
   <https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/>

2. Ravindra K. Ahuja, Thomas L. Magnanti, and James B. Orlin, *Network Flows: Theory, Algorithms, and Applications*. Pearson.  
   <https://www.pearson.com/en-us/subject-catalog/p/network-flows-theory-algorithms-and-applications/P200000003456/9780136175490>

3. Luca Trevisan, *Notes on LP Duality*, Stanford Theory Group.  
   <https://theory.stanford.edu/~trevisan/cs170/notes/lecture20.pdf>

4. Luca Trevisan, *Lecture 15: The LP of Maximum Flow and Its Dual*, Stanford CS261.  
   <https://theory.stanford.edu/~trevisan/cs261/lecture15.pdf>

5. Rajat Mittal, *Max Flow Problem Using Linear Programming*, IIT Kanpur.  
   <https://www.cse.iitk.ac.in/users/rmittal/prev_course/f23/reports/5primaldual.pdf>

6. Mykel J. Kochenderfer and Tim A. Wheeler, *Algorithms for Optimization*. MIT Press.  
   <https://mitpress.mit.edu/9780262039420/algorithms-for-optimization/>

---

# Concise Exam Aid

```text
CANONICAL PRIMAL
max cᵀx
s.t. Ax ≤ b
     x ≥ 0

CANONICAL DUAL
min bᵀy
s.t. Aᵀy ≥ c
     y ≥ 0

WEAK DUALITY
cᵀx ≤ bᵀy

OPTIMALITY CERTIFICATE
primal feasible + dual feasible + equal values
⇒ both optimal

STRONG DUALITY
finite primal optimum = finite dual optimum

PATH-FLOW PRIMAL
max Σp xp
s.t. Σp:e∈p xp ≤ ce
     xp ≥ 0

LENGTH DUAL
min Σe ce ye
s.t. Σe∈p ye ≥ 1 for every s-t path
     ye ≥ 0

CUT AS DUAL SOLUTION
ye = 1 if e leaves S, otherwise 0

ROUNDING
1. Compute shortest-path distances using ye.
2. Clip distances at 1.
3. Define Sr = {v : ℓ(v) ≤ r}.
4. Check distinct threshold cuts.
5. Some threshold cut costs at most Σe ce ye.

CONCLUSION
max flow = optimal length dual = min cut
```
