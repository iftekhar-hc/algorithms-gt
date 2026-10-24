# Lecture 15 Study Guide: LP Relaxations and Deterministic Rounding

Your lecture asks how a solution that makes fractional decisions—such as “select half a vertex” or “open half a facility”—can help us construct a good solution using only whole decisions. Its central technique is **rounding**: solve a linear-programming relaxation, then convert the fractional solution into a feasible integral solution while controlling the increase in cost. The lecture proves a 2-approximation for Vertex Cover and introduces an algorithm for metric Facility Location whose 6-approximation proof is deferred to the next lecture.

This guide explains both algorithms, supplies worked examples and text-based visualizations, completes the Facility Location proof, and provides pseudocode, quizzes, exam problems, and recommended resources.

> Lecture source: *Lec_15_Unmarked.pdf*, CS 6515: Graduate Algorithms, Lecture 15: LP Relaxations and Deterministic Rounding, Fall 2026, instructors Sahil Singla and Gerandy Brito. The Facility Location proof and practice exercises below expand on the attached notes. External textbook and video resources are linked in Sections 13–14.
>
> Math formatting: this file uses GitHub-compatible `$...$` for inline mathematics and `$$...$$` for display mathematics. Text visualizations and pseudocode use fenced code blocks.

---

## 1. The big picture: why solve a problem with fractional answers?

### 1.1 Integer programs model the decisions we actually want

An integer program can represent decisions such as:

- Select this vertex or do not select it.
- Open this facility or keep it closed.
- Assign this client to exactly one open facility.

Binary variables encode these choices:

$$
x_i\in\{0,1\}.
$$

The difficulty is that the discrete optimization problem can be computationally hard. The lecture replaces binary constraints with intervals:

$$
0\le x_i\le 1.
$$

This produces a linear-programming relaxation. Every integral feasible solution remains feasible, but fractional solutions become available too. See also [Williamson–Shmoys](https://www.designofapproxalgs.com/book.pdf).

### 1.2 Why the LP provides a lower bound

For a minimization problem, enlarging the feasible region cannot increase the optimum:

$$
\boxed{\mathrm{OPT}_{LP}\le \mathrm{OPT}}.
$$

Here:

- $\mathrm{OPT}_{LP}$ is the optimal fractional objective value.
- $\mathrm{OPT}$ is the optimal integral objective value.

The rounding algorithm must establish a second inequality:

$$
\mathrm{ALG}\le \alpha\,\mathrm{OPT}_{LP}.
$$

Combining them gives:

$$
\boxed{
\mathrm{ALG}
\le \alpha\,\mathrm{OPT}_{LP}
\le \alpha\,\mathrm{OPT}.
}
$$

This is the fundamental approximation argument in the lecture.

### Visualization: the approximation sandwich

```text
Fractional optimum        Integral optimum        Algorithm's solution
      OPT_LP  ----------------> OPT ----------------> ALG
                 lower bound           feasible solution

What we prove:
ALG ≤ α · OPT_LP

Therefore:
ALG ≤ α · OPT
```

The important distinction is that the fractional solution does two jobs:

1. Its objective value provides a benchmark.
2. Its variable values guide the construction of an integral solution.

### 1.3 Generic pseudocode

```text
LP-ROUNDING(instance):
    Formulate the problem as an integer program
    Replace integrality constraints with continuous constraints
    Solve the resulting LP optimally
    Round the fractional solution into a feasible integral solution
    Return the integral solution
```

An analysis must answer three questions:

1. Feasibility: Does rounding satisfy the original constraints?
2. Cost: How much can the objective increase?
3. Efficiency: Can both the LP and rounding steps be performed in polynomial time?

---

## 2. Vertex Cover: the simplest threshold-rounding example

### 2.1 Problem definition

Given an undirected graph $G=(V,E)$, a vertex cover is a subset $C\subseteq V$ such that every edge has at least one endpoint in $C$.

The goal is to minimize $|C|$.

```text
       a
      / \
     b---c

Selecting {a, b} covers every edge:
a-b: covered
a-c: covered by a
b-c: covered by b
```

### 2.2 Integer program and LP relaxation

Let $x_v=1$ mean that vertex $v$ is selected.

The integer program is:

$$
\begin{aligned}
\min \quad &\sum_{v\in V}x_v\\
\text{subject to}\quad
&x_u+x_v\ge 1
&&\text{for every }\{u,v\}\in E,\\
&x_v\in\{0,1\}
&&\text{for every }v\in V.
\end{aligned}
$$

The edge constraint says: “select at least one endpoint.”

The LP replaces $x_v\in\{0,1\}$ with $0\le x_v\le 1$.

### 2.3 Rounding rule

After solving the LP, select every vertex whose fractional value is at least $1/2$:

$$
\boxed{
C=\{v\in V:x_v^*\ge 1/2\}.
}
$$

```text
Fractional value       Rounded decision
     0.00                    0
     0.30                    0
     0.49                    0
     0.50                    1
     0.80                    1
     1.00                    1
```

The equality matters: vertices with value exactly $1/2$ must be included.

### 2.4 Why the rounded solution is feasible

Take any edge $\{u,v\}$.

The LP requires:

$$
x_u^*+x_v^*\ge 1.
$$

Both endpoints cannot have value strictly below $1/2$. Therefore, at least one endpoint is selected by the rounding rule.

Since the argument applies to every edge, $C$ is a vertex cover.

### 2.5 Why the cost increases by at most a factor of 2

Define the indicator:

$$
\mathbf 1[v\in C]
=
\begin{cases}
1,&v\in C,\\
0,&v\notin C.
\end{cases}
$$

For every vertex,

$$
\mathbf 1[v\in C]\le 2x_v^*.
$$

Why?

- If $v$ is selected, $x_v^*\ge 1/2$, so $1\le 2x_v^*$.
- If $v$ is not selected, $0\le 2x_v^*$.

Summing gives:

$$
\begin{aligned}
|C|
&=\sum_v\mathbf 1[v\in C]\\
&\le 2\sum_vx_v^*\\
&=2\mathrm{OPT}_{LP}\\
&\le 2\mathrm{OPT}.
\end{aligned}
$$

Thus threshold rounding is a 2-approximation.

### 2.6 Worked example: a triangle

For the triangle,

$$
x_a=x_b=x_c=\frac12
$$

satisfies every edge constraint and has objective $3/2$.

It is optimal because summing the three edge constraints gives:

$$
2(x_a+x_b+x_c)\ge 3.
$$

The rounding algorithm selects all three vertices.

| Quantity | Value |
|---|---:|
| Fractional optimum | $3/2$ |
| Integral optimum | $2$ |
| Rounded solution cost | $3$ |
| Rounded cost / fractional optimum | $2$ |
| Rounded cost / integral optimum | $3/2$ |

This illustrates an important distinction: a solution can cost exactly twice the LP optimum without costing twice the integral optimum.

### 2.7 Pseudocode

```text
VERTEX-COVER-ROUNDING(G = (V, E)):
    Solve:
        minimize Σ[v in V] x[v]
        subject to:
            x[u] + x[v] ≥ 1     for every edge {u, v}
            0 ≤ x[v] ≤ 1       for every vertex v

    C ← empty set

    for each vertex v:
        if x[v] ≥ 1/2:
            add v to C

    return C
```

After the LP solution is available, the rounding step takes $O(|V|)$ time.

---

## 3. Duality, matching, and the integrality gap

### 3.1 The Vertex Cover dual

Omitting the unnecessary upper bounds $x_v\le 1$, the LP dual is:

$$
\begin{aligned}
\max\quad &\sum_{e\in E}z_e\\
\text{subject to}\quad
&\sum_{e\ni v}z_e\le 1
&&\text{for every }v\in V,\\
&z_e\ge 0
&&\text{for every }e\in E.
\end{aligned}
$$

Interpretation:

- Place nonnegative weight on edges.
- Each vertex can support at most one unit of total incident edge weight.
- Maximize the total edge weight.

A matching gives a feasible dual solution: put weight 1 on matching edges and 0 elsewhere. No vertex belongs to more than one matching edge. Therefore,

$$
|M|\le \mathrm{OPT}_{LP}\le \mathrm{OPT}.
$$

This connects LP rounding with the matching-based approximation algorithm.

One useful distinction: any matching gives a lower bound, but the algorithm that selects both endpoints needs a maximal matching to guarantee that those endpoints cover every edge.

### 3.2 Integrality gap

For a minimization LP relaxation, the integrality gap compares:

$$
\frac{\mathrm{OPT}}{\mathrm{OPT}_{LP}}.
$$

In the complete graph $K_n$, for $n\ge 2$:

- Any vertex cover needs $n-1$ vertices.
- Setting every variable to $1/2$ gives LP value $n/2$.
- Summing all edge constraints proves that this fractional value is optimal.

Therefore,

$$
\frac{\mathrm{OPT}}{\mathrm{OPT}_{LP}}
=
\frac{n-1}{n/2}
=
2-\frac2n.
$$

This approaches 2 as $n$ grows.

### What this does—and does not—mean

It means no algorithm can always return an integral solution satisfying

$$
\mathrm{ALG}\le \alpha\,\mathrm{OPT}_{LP}
$$

for a fixed $\alpha<2$, using this LP value as the benchmark.

It does not, by itself, prove that every possible Vertex Cover approximation algorithm must have approximation factor at least 2. The limitation concerns this relaxation and this LP-relative guarantee.

---

## 4. Facility Location: why independent rounding is not enough

### 4.1 Problem definition

We have:

- Candidate facilities $F$.
- Clients $C$.
- Opening cost $f_i\ge 0$ for facility $i$.
- Connection cost $d_{ij}\ge 0$ between facility $i$ and client $j$.

We choose facilities to open and assign every client to an open facility.

The total cost is:

$$
\sum_{i\in S}f_i
+
\sum_{j\in C}d_{\sigma(j),j},
$$

where $\sigma(j)\in S$ is the facility serving client $j$. The lecture assumes that distances arise from a metric on facilities and clients, so the triangle inequality applies.

A scientific-planning analogy would be choosing laboratory hubs and assigning sample-collection sites to them. This is only an analogy: capacity limits, turnaround-time constraints, and other operational requirements are not included in the lecture’s uncapacitated model.

### 4.2 Integer program

Use:

$$
x_i=
\begin{cases}
1,&\text{facility }i\text{ is open},\\
0,&\text{otherwise},
\end{cases}
$$

and

$$
y_{ij}=
\begin{cases}
1,&\text{client }j\text{ is assigned to }i,\\
0,&\text{otherwise}.
\end{cases}
$$

Then:

$$
\begin{aligned}
\min\quad&
\sum_i f_ix_i+\sum_{i,j}d_{ij}y_{ij}\\
\text{subject to}\quad&
\sum_i y_{ij}=1
&&\forall j,\\
&y_{ij}\le x_i
&&\forall i,j,\\
&x_i,y_{ij}\in\{0,1\}.
\end{aligned}
$$

The first constraint serves each client exactly once. The second prevents assignment to a closed facility.

### A subtle modeling point

There is no constraint

$$
\sum_j y_{ij}\le x_i.
$$

That would impose a capacity restriction. In this model, one open facility may serve arbitrarily many clients.

### 4.3 Fractional interpretation

After relaxation:

- $x_i^*=0.4$ means facility $i$ is fractionally open to extent $0.4$.
- $y_{ij}^*=0.3$ means $30\%$ of client $j$'s assignment goes to facility $i$.

Define:

$$
F^*=\sum_i f_ix_i^*,
\qquad
D^*=\sum_{i,j}d_{ij}y_{ij}^*.
$$

Then:

$$
\mathrm{OPT}_{LP}=F^*+D^*\le \mathrm{OPT}.
$$

The rounding analysis will bound opening cost and connection cost separately.

### Why not just open every facility with $x_i^*\ge 1/2$?

A client can be fractionally served by many facilities, each with opening value below $1/2$.

For example:

$$
x_1=x_2=x_3=\frac13,
\qquad
y_{1j}=y_{2j}=y_{3j}=\frac13.
$$

This is feasible for that client, but thresholding at $1/2$ opens no facility.

Facility Location therefore requires coordinated, rather than independent, rounding.

---

## 5. From fractional assignments to client neighborhoods

### 5.1 Average fractional connection distance

For each client $j$, define:

$$
L_j=\sum_i d_{ij}y_{ij}^*.
$$

Because $\sum_i y_{ij}^*=1$, $L_j$ is a weighted average distance.

The total fractional connection cost is:

$$
D^*=\sum_j L_j.
$$

The lecture defines the nearby-facility set:

$$
\boxed{
B_j=\{i\in F:d_{ij}\le 2L_j\}.
}
$$

Although called a ball, $B_j$ contains candidate facilities, not every point in the underlying metric space.

### 5.2 Why each ball contains substantial fractional opening

We now derive a key lemma needed for the promised approximation proof.

For $L_j>0$, facilities outside $B_j$ have distance greater than $2L_j$. Thus:

$$
L_j
=\sum_i d_{ij}y_{ij}^*
\ge
2L_j\sum_{i\notin B_j}y_{ij}^*.
$$

Therefore:

$$
\sum_{i\notin B_j}y_{ij}^*\le \frac12,
$$

so:

$$
\sum_{i\in B_j}y_{ij}^*\ge \frac12.
$$

Since $y_{ij}^*\le x_i^*$,

$$
\boxed{
\sum_{i\in B_j}x_i^*\ge \frac12.
}
$$

If $L_j=0$, all positive assignment mass lies at distance zero, so the conclusion still holds—in fact, the ball contains assignment mass 1.

### Visualization: filtering distant assignment mass

```text
Client j has fractional assignments totaling 1

             nearby facilities              distant facilities
                 B_j                         outside B_j
          distance ≤ 2L_j                   distance > 2L_j
        ┌──────────────────┐             ┌──────────────────┐
        │ assignment mass  │             │ assignment mass  │
        │     ≥ 1/2        │             │     ≤ 1/2        │
        └──────────────────┘             └──────────────────┘
```

This is a weighted-average argument, closely related to Markov’s inequality. No random choices are required by the algorithm.

---

## 6. The Facility Location rounding algorithm

### 6.1 Algorithm idea

Process clients in nondecreasing order of $L_j$.

For each client:

1. If its ball shares no candidate facility with any representative’s ball, make it a representative and open its cheapest facility.
2. Otherwise, assign it to the facility opened for an overlapping representative.

The selected representatives’ balls are pairwise disjoint. This is the structural property that prevents repeated charging of opening costs.

### Visualization: disjoint representatives, overlapping followers

```text
Candidate-facility sets:

B_r = {a, b}       representative r: open cheapest of {a, b}
B_j = {b, c}       overlaps B_r: use r's opened facility

B_q = {d, e}       disjoint from B_r: create representative q
```

The relevant overlap is a shared candidate facility:

$$
B_j\cap B_r\ne\varnothing.
$$

It is not merely a visual intersection between two drawn circles.

### 6.2 Pseudocode

```text
FACILITY-LOCATION-ROUNDING(F, C, opening_cost, distance):
    Solve the facility-location LP optimally
    Obtain x_star and y_star

    for each client j:
        L[j] ← Σ[i in F] distance[i, j] * y_star[i, j]
        B[j] ← {i in F : distance[i, j] ≤ 2 * L[j]}

    Sort clients by nondecreasing L[j]
    Break ties deterministically

    R ← empty set              // representative clients
    S ← empty set              // open facilities
    opened_for ← empty map
    assignment ← empty map

    for each client j in sorted order:
        Find r in R such that B[j] ∩ B[r] is nonempty

        if no such r exists:
            i ← cheapest facility in B[j]
            Break ties deterministically

            add j to R
            add i to S
            opened_for[j] ← i
            assignment[j] ← i
        else:
            assignment[j] ← opened_for[r]

    return S, assignment
```

The lecture’s algorithm uses these representative assignments. Afterward, assigning every client to its nearest open facility can only decrease connection cost.

With $m=|F|$ and $n=|C|$, a straightforward implementation takes $O(n^2m+n\log n)$ time after solving the LP, using explicit facility-set intersection checks.

---

## 7. Completing the 6-approximation proof

The attached notes stop before this proof. The following derivation completes the analysis of exactly the algorithm in the notes.

We will establish:

$$
\text{opening cost}\le 2F^*
$$

and

$$
\text{connection cost}\le 6D^*.
$$

### 7.1 Opening cost: cheapest facility plus disjoint balls

Let $r$ be a representative, and let $i_r$ be the cheapest facility in $B_r$.

For every $i\in B_r$,

$$
f_{i_r}\le f_i.
$$

Multiply by $x_i^*$ and sum:

$$
f_{i_r}\sum_{i\in B_r}x_i^*
\le
\sum_{i\in B_r}f_ix_i^*.
$$

The ball-mass lemma gives:

$$
\sum_{i\in B_r}x_i^*\ge \frac12.
$$

Therefore:

$$
f_{i_r}
\le
2\sum_{i\in B_r}f_ix_i^*.
$$

Now sum over representatives:

$$
\begin{aligned}
\sum_{r\in R}f_{i_r}
&\le
2\sum_{r\in R}\sum_{i\in B_r}f_ix_i^*\\
&\le
2\sum_{i\in F}f_ix_i^*\\
&=2F^*.
\end{aligned}
$$

The second inequality uses pairwise disjointness: no facility’s fractional opening cost is charged more than once.

### 7.2 Connection cost for a representative

A representative $r$ connects to a facility inside its own ball:

$$
d(r,i_r)\le 2L_r.
$$

So representatives individually satisfy an even stronger bound than the one we need.

### 7.3 Connection cost for a nonrepresentative

Suppose client $j$ overlaps a previously selected representative $r$.

Choose a shared facility:

$$
i\in B_j\cap B_r.
$$

The proof follows a three-segment route:

```text
client j ─────── shared facility i ─────── representative r ─────── open facility i_r
          ≤ 2L_j                    ≤ 2L_r                       ≤ 2L_r
```

By the triangle inequality,

$$
\begin{aligned}
d(j,i_r)
&\le d(j,i)+d(i,r)+d(r,i_r)\\
&\le 2L_j+2L_r+2L_r.
\end{aligned}
$$

Because $r$ was processed before $j$,

$$
L_r\le L_j.
$$

Consequently,

$$
\boxed{
d(j,i_r)\le 6L_j.
}
$$

Summing over clients:

$$
\text{connection cost}
\le
6\sum_jL_j
=
6D^*.
$$

### 7.4 Combine the bounds

$$
\begin{aligned}
\mathrm{ALG}
&\le 2F^*+6D^*\\
&\le 6(F^*+D^*)\\
&=6\mathrm{OPT}_{LP}\\
&\le 6\mathrm{OPT}.
\end{aligned}
$$

Therefore:

$$
\boxed{\mathrm{ALG}\le 6\mathrm{OPT}}.
$$

Notice that we do not add the factors $2+6$. The two coefficients multiply separate components of the LP objective, so their maximum provides a common bound.

### 7.5 What each design choice contributes

| Design choice | Role in the proof |
|---|---|
| Radius $2L_j$ | Ensures at least half the fractional assignment mass lies nearby |
| Cheapest facility in a ball | Bounds the opening cost using fractional opening mass |
| Disjoint representative balls | Prevents double-counting opening-cost charges |
| Increasing order of $L_j$ | Ensures $L_r\le L_j$ |
| Metric distances | Bounds the detour through a shared facility and representative |

These are not incidental implementation choices; each supports a specific inequality.

---

## 8. Worked Facility Location example

The following constructed example uses a six-cycle metric: every displayed edge has length 1, and distances are shortest-path distances.

```text
              client p
             /        \
       facility A    facility B
           |              |
        client r       client q
             \          /
              facility C
```

Equivalently, the cycle is:

```text
A — p — B — q — C — r — A
```

Every facility has opening cost 2.

### 8.1 Distance table

| Facility | Client $p$ | Client $q$ | Client $r$ |
|---|---:|---:|---:|
| $A$ | 1 | 3 | 1 |
| $B$ | 1 | 1 | 3 |
| $C$ | 3 | 1 | 1 |

### 8.2 A fractional solution

Open each facility halfway:

$$
x_A=x_B=x_C=\frac12.
$$

Split each client equally between its two adjacent facilities:

$$
y_{Ap}=y_{Bp}=\frac12,
$$

$$
y_{Bq}=y_{Cq}=\frac12,
$$

$$
y_{Cr}=y_{Ar}=\frac12.
$$

All other assignment variables are zero.

The fractional opening cost is:

$$
F^*=3\cdot 2\cdot \frac12=3.
$$

Each client has average connection distance 1:

$$
L_p=L_q=L_r=1.
$$

Thus:

$$
D^*=3,
\qquad
F^*+D^*=6.
$$

### 8.3 Why this fractional solution is optimal

Let $t=x_A+x_B+x_C$, and let $D$ denote the connection cost of any LP-feasible solution.

All distances are at least 1, so:

$$
D\ge 3.
$$

For each client, assignment to its two nearby facilities costs 1 per unit and assignment to its opposite facility costs 3. Since nearby assignment is bounded by the opening variables, summing over clients gives:

$$
D\ge 9-4t.
$$

Averaging these two lower bounds:

$$
D\ge \frac{3+(9-4t)}2=6-2t.
$$

Opening cost is $2t$, so:

$$
2t+D\ge 6.
$$

The displayed fractional solution attains 6 and is therefore optimal.

### 8.4 Construct the balls and round

Because $2L_j=2$,

$$
B_p=\{A,B\},\qquad
B_q=\{B,C\},\qquad
B_r=\{C,A\}.
$$

Process $p$ first, breaking ties alphabetically.

1. $p$ becomes a representative.
2. Open $A$, breaking the opening-cost tie.
3. $q$'s ball overlaps $B_p$ at $B$, so assign $q$ to $A$.
4. $r$'s ball overlaps $B_p$ at $A$, so assign $r$ to $A$.

The result costs:

$$
2+(1+3+1)=7.
$$

The integral optimum is also 7:

- One open facility costs $2+5=7$.
- Two open facilities cost $4+3=7$.
- Three open facilities cost $6+3=9$.

This instance illustrates why the LP is useful even when its solution is not physically implementable:

$$
\mathrm{OPT}_{LP}=6
<
\mathrm{OPT}=7
=
\mathrm{ALG}.
$$

---

## 9. Common mistakes and how to avoid them

### Mistake 1: Reversing the relaxation inequality

For minimization:

$$
\mathrm{OPT}_{LP}\le\mathrm{OPT},
$$

not the reverse. The LP has more feasible options.

### Mistake 2: Using a strict Vertex Cover threshold

Selecting only vertices with $x_v^*>1/2$ can leave an edge uncovered when both endpoints have value $1/2$.

### Mistake 3: Treating $x_i$ as a facility-capacity budget

The constraint $y_{ij}\le x_i$ applies separately to each client. It does not bound total assignment over all clients.

### Mistake 4: Thinking overlapping balls imply the opened facility lies in both

The shared facility $i$ belongs to both balls. The opened facility $i_r$ need only belong to $B_r$.

That is why the connection proof uses:

$$
j\to i\to r\to i_r.
$$

### Mistake 5: Forgetting the sorting condition

The triangle inequality yields:

$$
d(j,i_r)\le 2L_j+4L_r.
$$

It is the processing order that lets us replace $L_r$ with $L_j$.

### Mistake 6: Claiming the 6 bound is always attained

A 6-approximation is an upper-bound guarantee over all instances. It does not say that typical solutions—or even the worst case of this particular analysis—must achieve ratio exactly 6.

---

## 10. Quick quiz

Try these without looking at the solutions.

### Questions

1. For a minimization problem, why does LP relaxation give a lower bound?

2. An edge has LP endpoint values $0.3$ and $0.7$. Which endpoints does Vertex Cover rounding select?

3. Why is the threshold rule $x_v^*\ge 1/2$, rather than $x_v^*>1/2$?

4. What are the fractional and integral Vertex Cover optima for a triangle?

5. In Facility Location, what does $L_j$ measure?

6. Why must $B_j$ contain at least $1/2$ unit of fractional opening mass?

7. What property of representative balls prevents opening-cost double-counting?

8. Where is increasing order of $L_j$ used?

9. Where is the metric assumption used?

10. If opening cost is at most $2F^*$ and connection cost is at most $6D^*$, why is the overall guarantee 6 rather than 8?

### Answer key

1. Every integral feasible solution is LP-feasible, so the LP minimizes over a larger region.

2. Only the endpoint with value $0.7$.

3. An edge may have both endpoints equal to $1/2$. A strict threshold would select neither.

4. Fractional optimum $3/2$; integral optimum 2.

5. The weighted average distance in client $j$'s fractional assignment:

   $$
   L_j=\sum_i d_{ij}y_{ij}^*.
   $$

6. At most half the assignment mass can lie farther than $2L_j$, and $x_i^*\ge y_{ij}^*$.

7. They are pairwise disjoint as sets of candidate facilities.

8. To establish $L_r\le L_j$ when $j$ joins an earlier representative $r$.

9. To bound the direct connection by the length of the three-segment detour.

10. Because:

    $$
    2F^*+6D^*\le 6(F^*+D^*).
    $$

---

## 11. Exam-style questions

These are original practice questions based on the lecture, not past examination questions.

### Question 1: Weighted Vertex Cover — 15 points

Each vertex $v$ has nonnegative weight $w_v$.

1. Formulate the integer program and LP relaxation.
2. Give a deterministic rounding algorithm.
3. Prove a 2-approximation guarantee.

### Question 2: Integrality gap versus approximation ratio — 15 points

For the standard Vertex Cover LP on $K_n$, $n\ge 2$:

1. Determine $\mathrm{OPT}$.
2. Determine $\mathrm{OPT}_{LP}$.
3. Calculate the integrality-gap ratio.
4. If the LP solution has $x_v=1/2$ for every vertex, calculate the rounded solution cost.
5. Explain why the integrality gap is not itself a universal hardness-of-approximation result.

### Question 3: Execute Facility Location rounding — 20 points

Use the six-cycle example from Section 8.

1. Verify the proposed fractional solution is feasible.
2. Calculate $F^*$, $D^*$, and all $L_j$.
3. Construct all balls.
4. Run the algorithm using client order $p,q,r$ and alphabetical facility tie-breaking.
5. Compute the resulting integral cost.

### Question 4: Reconstruct the approximation proof — 25 points

For the lecture’s Facility Location algorithm, prove:

1. Every ball contains at least $1/2$ unit of fractional opening mass.
2. Total opening cost is at most $2F^*$.
3. Every client’s connection distance is at most $6L_j$.
4. The algorithm is a 6-approximation.

Identify the exact step where each assumption or algorithmic choice is used.

### Question 5: Change the ball radius — 25 points

For a parameter $\beta>1$, define:

$$
B_j^{(\beta)}
=
\{i:d_{ij}\le \beta L_j\}.
$$

Use the same representative-selection algorithm.

1. Prove:

   $$
   \sum_{i\in B_j^{(\beta)}}x_i^*
   \ge 1-\frac1\beta.
   $$

2. Show:

   $$
   \text{opening cost}
   \le
   \frac{\beta}{\beta-1}F^*.
   $$

3. Show:

   $$
   \text{connection cost}
   \le 3\beta D^*.
   $$

4. Find the choice of $\beta$ that minimizes the approximation factor obtained from these bounds.

---

## 12. Exam solution outlines

### Solution 1: Weighted Vertex Cover

The LP is:

$$
\begin{aligned}
\min\quad &\sum_v w_vx_v\\
\text{subject to}\quad&
x_u+x_v\ge 1
&&\forall\{u,v\}\in E,\\
&0\le x_v\le 1.
\end{aligned}
$$

Use the same threshold:

$$
C=\{v:x_v^*\ge 1/2\}.
$$

Feasibility is unchanged.

Since weights are nonnegative,

$$
\begin{aligned}
\sum_{v\in C}w_v
&=\sum_v w_v\mathbf1[v\in C]\\
&\le 2\sum_v w_vx_v^*\\
&\le 2\mathrm{OPT}.
\end{aligned}
$$

### Solution 2: Complete graphs

A cover can omit at most one vertex:

$$
\mathrm{OPT}=n-1.
$$

Summing all edge constraints:

$$
(n-1)\sum_vx_v
\ge
\binom n2.
$$

Therefore:

$$
\sum_vx_v\ge \frac n2.
$$

The all-$1/2$ solution attains this lower bound, so:

$$
\mathrm{OPT}_{LP}=\frac n2.
$$

The gap is:

$$
2-\frac2n.
$$

Threshold rounding of this solution selects all $n$ vertices. Its approximation ratio on the instance is:

$$
\frac{n}{n-1}.
$$

Thus, the LP gap can approach 2 while this particular rounded solution approaches optimality relative to the integer optimum.

### Solution 3: Six-cycle execution

Each client has two assignment values of $1/2$, and each is bounded by the corresponding opening variable $1/2$.

The costs and neighborhoods are:

$$
F^*=3,\qquad D^*=3,\qquad L_p=L_q=L_r=1,
$$

$$
B_p=\{A,B\},\quad B_q=\{B,C\},\quad B_r=\{C,A\}.
$$

The algorithm opens $A$, assigns every client to it, and returns total cost 7.

### Solution 4: Proof skeleton

The sequence to reproduce is:

$$
\text{average distance}
\Longrightarrow
\text{nearby assignment mass}
\Longrightarrow
\text{nearby opening mass}.
$$

Then:

$$
\text{cheapest facility}
+
\text{disjoint balls}
\Longrightarrow
\text{opening cost}\le 2F^*.
$$

Finally:

$$
\text{shared facility}
+
\text{triangle inequality}
+
L_r\le L_j
\Longrightarrow
d(j,i_r)\le 6L_j.
$$

Combine:

$$
\mathrm{ALG}
\le 2F^*+6D^*
\le 6\mathrm{OPT}_{LP}
\le 6\mathrm{OPT}.
$$

### Solution 5: Parameterized radius

This is an extension derived from the lecture’s proof, not a result stated in the attached notes.

The weighted-average argument gives:

$$
\sum_{i\notin B_j^{(\beta)}}y_{ij}^*
\le \frac1\beta.
$$

Hence:

$$
\sum_{i\in B_j^{(\beta)}}x_i^*
\ge 1-\frac1\beta.
$$

For a representative $r$:

$$
f_{i_r}
\left(1-\frac1\beta\right)
\le
\sum_{i\in B_r^{(\beta)}}f_ix_i^*.
$$

Disjointness then gives:

$$
\text{opening cost}
\le
\frac{\beta}{\beta-1}F^*.
$$

For a nonrepresentative $j$:

$$
\begin{aligned}
d(j,i_r)
&\le \beta L_j+\beta L_r+\beta L_r\\
&\le 3\beta L_j.
\end{aligned}
$$

Therefore:

$$
\mathrm{ALG}
\le
\frac{\beta}{\beta-1}F^*
+
3\beta D^*.
$$

A valid common factor is:

$$
\alpha(\beta)
=
\max\left\{
\frac{\beta}{\beta-1},
3\beta
\right\}.
$$

The first expression decreases with $\beta$, while the second increases. Balance them:

$$
\frac{\beta}{\beta-1}=3\beta.
$$

Since $\beta>1$,

$$
\frac1{\beta-1}=3,
\qquad
\beta=\frac43.
$$

Both coefficients become 4:

$$
\boxed{
\mathrm{ALG}\le 4(F^*+D^*)\le 4\mathrm{OPT}.
}
$$

The radius $2L_j$ makes the lecture’s initial proof especially simple, but adjusting the radius improves the guarantee from the same proof framework.

---

## 13. Textbook references

### 13.1 Closest match: Williamson and Shmoys

David P. Williamson and David B. Shmoys, *The Design of Approximation Algorithms*, Cambridge University Press, 2011.

Recommended reading:

| Section | Topic | How it connects |
|---|---|---|
| 1.2 | LP formulations and Set Cover | Develops the relaxation/lower-bound framework |
| 1.3 | Deterministic rounding | Generalizes threshold-rounding ideas |
| 4.5 | Uncapacitated Facility Location | Closest match to the lecture’s main application |
| 5.8 | Randomized rounding for Facility Location | A useful next step after deterministic rounding |
| Appendix A | Linear programming | Reviews the LP background |

The authors provide an [electronic edition](https://www.designofapproxalgs.com/book.pdf), and the table of contents verifies these section numbers.

### 13.2 Complementary treatment: Vazirani

Vijay V. Vazirani, *Approximation Algorithms*, Springer, 2001.

Useful chapters include:

- “Introduction to LP-Duality,” pages 93–107.
- “Rounding Applied to Set Cover,” pages 118–123.
- “Set Cover via the Primal-Dual Schema,” pages 124–129.

These readings help connect the lecture’s rounding arguments to the broader distinction between rounding a fractional solution and constructing primal–dual certificates. See the [publisher’s book page](https://link.springer.com/book/10.1007/978-3-662-04565-7).

Suggested order: read Williamson–Shmoys Sections 1.2–1.3, then Section 4.5; use Vazirani when you want a second explanation of LP-based approximation techniques.

---

## 14. Relevant video lectures

Michael Dinitz’s Johns Hopkins course, *601.435/635 Approximation Algorithms, Spring 2021*, is an unusually close match. Its [course schedule](https://www.cs.jhu.edu/~mdinitz/classes/ApproxAlgorithms/Spring2021/) lists video links alongside lecture notes and textbook readings.

### Recommended sequence

| Order | Lecture | Why watch it |
|---|---|---|
| 1 | January 26: “Intro, Vertex Cover” | Establishes approximation guarantees and the Vertex Cover setting |
| 2 | February 23: “Intro to LPs for Approximation Algorithms” | Reinforces LP relaxations and lower-bound reasoning |
| 3 | February 25: “Deterministic Rounding: Metric Uncapacitated Facility Location” | Directly matches the central topic of your notes |
| 4 | March 2: “Randomized Rounding: Set Cover and UFL” | Shows how randomized methods extend the same LP framework |

These titles and dates appear on the course page; the Facility Location lecture is paired with Williamson–Shmoys Section 4.5.

### How to use the videos actively

After the LP introduction, reconstruct:

$$
\mathrm{OPT}_{LP}\le\mathrm{OPT}.
$$

After the deterministic Facility Location lecture, reproduce these three inequalities without notes:

$$
\sum_{i\in B_j}x_i^*\ge \frac12,
$$

$$
\sum_{r\in R}f_{i_r}\le 2F^*,
$$

$$
d(j,i_r)\le 2L_j+4L_r\le 6L_j.
$$

If you can explain why each inequality holds—and identify where disjointness, sorting, and the metric assumption enter—you understand the core proof rather than merely remembering the final approximation factor.
