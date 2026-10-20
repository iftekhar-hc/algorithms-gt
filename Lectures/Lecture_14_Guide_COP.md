# Lecture 14 Study Guide: Approximation Algorithms and Greedy Methods

The central lesson of **Lecture 14** is not merely “use greedy algorithms.” It is how to **prove** that a polynomial-time solution is close to an unknown optimum, using lower-bound certificates, charging arguments, and structural counting.

The lecture develops this through:

1. two approximation algorithms for **Minimum Vertex Cover**; and
2. a greedy approximation for **directed edge-disjoint paths**.

---

## 1. Approximation Algorithms

Suppose an optimization instance is $I$.

- $\operatorname{OPT}(I)$ is the value of an optimal solution.
- $A(I)$ is the value returned by an approximation algorithm.
- The returned solution must always be **feasible**.

For an $\alpha$-approximation, where $\alpha \ge 1$:

$$
A(I) \le \alpha\operatorname{OPT}(I)
$$

for a minimization problem, and

$$
A(I) \ge \frac{\operatorname{OPT}(I)}{\alpha}
$$

for a maximization problem.

The guarantee must hold for **every instance**, not merely on average.

### Intuition

For minimization:

```text
OPT                    Algorithm's solution
 |---------------------------|
 0        acceptable range   alpha * OPT
```

If $\alpha=2$, the algorithm may return a solution twice as expensive as the optimum, but never worse than that.

For maximization, the direction reverses. If $\alpha=2$, the algorithm guarantees at least half of the optimal value.

### Example

Suppose the optimal minimum vertex cover has size

$$
\operatorname{OPT}=7.
$$

A 2-approximation guarantees

$$
A \le 2\cdot 7=14.
$$

It does **not** claim that the algorithm usually returns 14. It says that 14 is a worst-case upper bound.

---

## 2. PTAS versus FPTAS

A **polynomial-time approximation scheme**, or PTAS, accepts an error parameter $\varepsilon>0$ and, for minimization, returns a $(1+\varepsilon)$-approximation. Its running time is polynomial in the input size when $\varepsilon$ is fixed.

A **fully polynomial-time approximation scheme**, or FPTAS, is stronger: its running time must be polynomial in both

$$
n
\quad\text{and}\quad
\frac{1}{\varepsilon}.
$$

For maximization, a common convention is a guarantee of at least

$$
(1-\varepsilon)\operatorname{OPT}.
$$

### Why the distinction matters

The running time

$$
n^3 2^{1/\varepsilon}
$$

can define a PTAS because it is polynomial in $n$ for fixed $\varepsilon$, but it is not an FPTAS.

By contrast,

$$
\frac{n^3}{\varepsilon^2}
$$

is polynomial in both $n$ and $1/\varepsilon$, so it can satisfy the running-time requirement of an FPTAS.

---

## 3. General Approximation-Proof Template

All three analyses in the lecture follow essentially the same pattern:

```text
1. Construct a feasible solution efficiently.
2. Find a quantity B that bounds OPT.
3. Relate the algorithm's value to B.
4. Eliminate B to obtain a bound involving OPT.
```

For a minimization problem, the useful certificate is usually a **lower bound**:

$$
B\le \operatorname{OPT}.
$$

If the algorithm also satisfies

$$
A\le \alpha B,
$$

then

$$
A\le \alpha B\le \alpha\operatorname{OPT}.
$$

The difficult part is normally finding the right certificate $B$, not performing the final algebra.

---

## 4. Minimum Vertex Cover

Given an undirected graph $G=(V,E)$, a vertex cover is a set

$$
C\subseteq V
$$

such that every edge has at least one endpoint in $C$. The objective is to minimize $|C|$.

Let

$$
n=|V|
\quad\text{and}\quad
m=|E|.
$$

### Visual example

Consider:

```text
       a
      / \
     b---c
     |
     d
```

The edge set is

$$
E=\{(a,b),(a,c),(b,c),(b,d)\}.
$$

The set

$$
C=\{b,c\}
$$

is a vertex cover:

- $(a,b)$ is covered by $b$;
- $(a,c)$ is covered by $c$;
- $(b,c)$ is covered by both; and
- $(b,d)$ is covered by $b$.

A single vertex cannot cover all four edges, so

$$
\operatorname{OPT}=2.
$$

---

## 5. Greedy Algorithm 1: Maximum Remaining Degree

At every iteration:

1. consider only the currently uncovered edges;
2. select a vertex incident to the largest number of those edges;
3. add it to the cover; and
4. remove every edge incident to it.

Degrees must be recomputed with respect to the **remaining edge set**, not the original graph.

### Pseudocode

```text
GREEDY-DEGREE-COVER(G = (V, E))
    C <- empty set
    E_remaining <- E

    while E_remaining is not empty
        choose v maximizing its degree in E_remaining
        C <- C union {v}
        remove from E_remaining every edge incident to v

    return C
```

### Worked example

For the previous graph, the initial remaining degrees are:

```text
deg(a) = 2
deg(b) = 3
deg(c) = 2
deg(d) = 1
```

Choose $b$. This covers

$$
(a,b),\quad (b,c),\quad (b,d).
$$

Only $(a,c)$ remains. Choose either $a$ or $c$. The algorithm returns a cover of size 2, which happens to be optimal.

### Why it has a logarithmic guarantee

Suppose $r>0$ edges remain and let $C^\star$ be an optimal cover with

$$
|C^\star|=\operatorname{OPT}.
$$

The vertices in $C^\star$ still cover all $r$ remaining edges. By averaging, some vertex in $C^\star$ must therefore be incident to at least

$$
\frac{r}{\operatorname{OPT}}
$$

remaining edges.

Because greedy selects a maximum-degree vertex, it covers at least that many edges. If $r_t$ is the number of remaining edges after $t$ choices, then

$$
r_{t+1}
\le
r_t-\frac{r_t}{\operatorname{OPT}}
=
r_t\left(1-\frac{1}{\operatorname{OPT}}\right).
$$

Repeated application gives

$$
r_t
\le
m\left(1-\frac{1}{\operatorname{OPT}}\right)^t.
$$

Using

$$
1-x\le e^{-x},
$$

we obtain

$$
r_t\le me^{-t/\operatorname{OPT}}.
$$

When

$$
t>\operatorname{OPT}\ln m,
$$

the right-hand side is less than 1. Since $r_t$ is a nonnegative integer, $r_t=0$.

The resulting cover has size at most

$$
\operatorname{OPT}(1+\ln m).
$$

Since a simple graph satisfies $m<n^2$, the algorithm is also an $O(\log n)$-approximation.

### Visualization of the decay

```text
Remaining edges

m       *
        |
        |   *
        |       *
        |           *
        |               *
0       +-------------------------- iterations
```

The reduction is multiplicative rather than additive. Each choice removes at least a $1/\operatorname{OPT}$ fraction of the remaining edges.

### Connection to Set Cover

This is the standard greedy Set Cover analysis:

- universe elements are graph edges;
- the set associated with vertex $v$ consists of the edges incident to $v$; and
- selecting $v$ covers those elements.

---

## 6. Greedy Algorithm 2: Maximal Matching

The second algorithm does something that initially appears less intelligent:

1. pick any remaining edge $(u,v)$;
2. add **both** endpoints to the cover;
3. remove all edges incident to either endpoint; and
4. repeat.

Despite making arbitrary choices, it obtains the stronger factor-2 guarantee.

### Pseudocode

```text
GREEDY-VERTEX-COVER(G = (V, E))
    C <- empty set
    E_remaining <- E
    M <- empty set

    while E_remaining is not empty
        choose any edge (u, v) in E_remaining
        M <- M union {(u, v)}
        C <- C union {u, v}

        remove every edge incident to u or v
        from E_remaining

    return C
```

### Why the selected edges form a matching

Suppose the algorithm selects $(u,v)$. It immediately removes every edge incident to $u$ or $v$.

Therefore, no subsequently selected edge can share either endpoint with $(u,v)$. The selected edges are pairwise vertex-disjoint, so they form a **matching** $M$.

### Why the matching is maximal

When the algorithm terminates, no edge remains that is disjoint from all selected matching edges. Otherwise, that edge could be added to $M$.

Thus, $M$ is **maximal**.

Be careful:

- **maximal matching**: no additional edge can be added while preserving the matching property;
- **maximum matching**: a matching with the largest possible number of edges.

A maximal matching need not be maximum.

### Example

```text
a --- b --- c --- d
```

If the first selected edge is $(b,c)$, the resulting matching has one edge and is maximal. However,

$$
\{(a,b),(c,d)\}
$$

is a matching of size two. Therefore, the first matching is not maximum.

### The factor-2 proof

Let $M$ be the matching selected by the algorithm.

Every vertex cover must contain at least one endpoint of each edge in $M$. Since the matching edges are disjoint, one selected vertex cannot cover two different matching edges.

Therefore,

$$
|M|\le \operatorname{OPT}.
$$

The algorithm selects both endpoints of every matching edge, so

$$
|C|=2|M|.
$$

Combining the inequalities,

$$
|C|=2|M|\le 2\operatorname{OPT}.
$$

Thus, the algorithm is a polynomial-time 2-approximation.

### Proof diagram

```text
Selected matching edges:

u1 ----- v1      u2 ----- v2      u3 ----- v3
    edge 1           edge 2           edge 3

Algorithm takes:
{u1,v1,u2,v2,u3,v3}                  size = 6

Any vertex cover must take:
at least one endpoint from each edge   size >= 3

Therefore:
algorithm size <= 2 * optimum
```

### Tight example

For a graph containing only one edge,

```text
u ----- v
```

the algorithm selects both $u$ and $v$, giving

$$
|C|=2.
$$

An optimal cover selects only one endpoint:

$$
\operatorname{OPT}=1.
$$

Hence,

$$
\frac{|C|}{\operatorname{OPT}}=2.
$$

The factor 2 is tight **for this algorithm**. This does not prove that every polynomial-time Vertex Cover approximation must have factor at least 2.

---

## 7. Comparing the Two Vertex Cover Algorithms

| Property | Maximum-degree greedy | Maximal-matching greedy |
|---|---:|---:|
| Choice | Maximum remaining degree | Arbitrary remaining edge |
| Vertices added per iteration | 1 | 2 |
| Proof certificate | Fractional edge reduction | Matching lower bound |
| Guarantee | $1+\ln m$ | $2$ |
| Main proof technique | Multiplicative decay | Combinatorial lower bound |
| Choice sensitivity | Depends on tie-breaking | Guarantee independent of choices |

The surprising lesson is that a locally more aggressive rule does not necessarily produce a better worst-case approximation guarantee. The quality of an approximation algorithm depends on whether its actions expose a useful comparison with $\operatorname{OPT}$.

---

## 8. Directed Edge-Disjoint Paths

We are given:

- a directed graph $G=(V,E)$; and
- terminal pairs $(s_i,t_i)$ for $i=1,\ldots,k$.

We want to route as many terminal pairs as possible, subject to:

1. at most one directed $s_i$-to-$t_i$ path per pair; and
2. every directed edge being used by at most one selected path.

Paths may share vertices, but they may not share edges.

### Example

```text
s1 --> a --> b --> t1
       ^     |
s2 ----+     +--> t2
```

If the route for pair 1 uses $a\to b$, and a route for pair 2 also requires $a\to b$, the two paths cannot both be selected.

---

## 9. Short-Path Greedy Algorithm

Let

$$
m=|E|
$$

and

$$
L=\max\{1,\lfloor\sqrt m\rfloor\}.
$$

Repeatedly:

1. find a remaining terminal pair with a directed path of length at most $L$;
2. select such a path;
3. remove all its edges; and
4. remove that terminal pair.

Breadth-first search can be used to find shortest paths in an unweighted directed graph. The process stops when no currently routable pair has a path of length at most $L$.

### Pseudocode

```text
SHORT-PATH-GREEDY(G, terminal_pairs)
    m <- number of edges in G
    L <- max(1, floor(sqrt(m)))

    A <- empty set
    G_remaining <- G
    Pairs <- terminal_pairs

    while true
        found <- false

        for each pair (s_i, t_i) in Pairs
            P <- BFS shortest directed path
                 from s_i to t_i in G_remaining

            if P exists and length(P) <= L
                A <- A union {P}
                remove all edges of P from G_remaining
                remove pair (s_i, t_i) from Pairs
                found <- true
                break

        if found = false
            break

    B <- any one feasible path for any terminal pair
         in the original instance, if one exists

    return whichever contains more paths: A or {B}
```

The one-path fallback is essential. Without it, all feasible paths could be longer than $L$, causing the short-path procedure to return zero even when $\operatorname{OPT}>0$.

---

## 10. Analysis by Splitting the Optimum

Let $O$ be an optimal collection of edge-disjoint paths. Divide it into

$$
O_{\text{short}}
=
\{Q\in O: |Q|\le L\}
$$

and

$$
O_{\text{long}}
=
\{Q\in O: |Q|>L\}.
$$

Then

$$
\operatorname{OPT}
=
|O_{\text{short}}|+|O_{\text{long}}|.
$$

This is a common approximation technique:

```text
Optimal objects
      |
      +---- easy/local objects: short paths
      |
      +---- expensive/global objects: long paths
```

The two groups are bounded using different arguments.

### 10.1 Bounding the long optimal paths

Every long path uses at least $L+1$ edges.

Since the optimal paths are edge-disjoint and the graph contains only $m$ edges,

$$
(L+1)|O_{\text{long}}|\le m.
$$

Therefore,

$$
|O_{\text{long}}|
\le
\frac{m}{L+1}.
$$

This is a resource-counting argument: each long path consumes many units of a globally limited resource.

### 10.2 Charging the short optimal paths

Let $Q\in O_{\text{short}}$ be an optimal path for pair $i$.

There are two cases.

#### Case 1: Greedy routes pair $i$

Charge $Q$ to the greedy path that serves the same pair.

A greedy path can receive at most one such same-pair charge.

#### Case 2: Greedy does not route pair $i$

When greedy terminates, $Q$ cannot remain intact. If it did, it would still be a path of length at most $L$, and greedy would not have terminated.

Therefore, some edge of $Q$ must have been removed by a selected greedy path. Charge $Q$ to one such greedy path.

Because the optimal paths are edge-disjoint, each edge of a greedy path can be shared with at most one optimal path. A greedy path has at most $L$ edges, so it receives at most $L$ shared-edge charges.

Adding the possible same-pair charge gives

$$
|O_{\text{short}}|
\le
(L+1)|A|.
$$

### Charging visualization

```text
Optimal short paths       selected greedy path P

Q1 -------------\
Q2 ------\        \
Q3 -------X========X========X----- P
Q4 ----------------/

Each charged path is assigned through a distinct shared edge,
except for at most one additional same-pair charge.
```

---

## 11. Combining the Bounds

From the short- and long-path bounds,

$$
\operatorname{OPT}
\le
(L+1)|A|+\frac{m}{L+1}.
$$

The additive second term causes a problem when $|A|=0$. To obtain a multiplicative guarantee, the algorithm also computes one arbitrary feasible path and returns the better of that one-path solution and $A$.

Let $a$ denote the number of paths returned. If $\operatorname{OPT}>0$, then

$$
a\ge 1
\quad\text{and}\quad
a\ge |A|.
$$

Consequently,

$$
\begin{aligned}
\operatorname{OPT}
&\le (L+1)|A|+\frac{m}{L+1}\\
&\le \left(L+1+\frac{m}{L+1}\right)a.
\end{aligned}
$$

For $L=\lfloor\sqrt m\rfloor$,

$$
L+1>\sqrt m
$$

and

$$
L+1\le \sqrt m+1.
$$

Thus,

$$
L+1+\frac{m}{L+1}
\le
2\sqrt m+1.
$$

Therefore,

$$
a\ge
\frac{\operatorname{OPT}}{2\sqrt m+1}.
$$

The algorithm is an

$$
O(\sqrt m)
$$

approximation for the maximization problem.

---

## 12. Why Does $\sqrt m$ Appear?

There are two competing losses:

$$
\text{short-path loss}\approx L
$$

and

$$
\text{long-path loss}\approx \frac{m}{L}.
$$

Their sum is approximately

$$
f(L)=L+\frac{m}{L}.
$$

To balance them, solve

$$
L=\frac{m}{L},
$$

which gives

$$
L^2=m
\quad\Longrightarrow\quad
L=\sqrt m.
$$

Equivalently,

$$
f'(L)=1-\frac{m}{L^2}=0
$$

again gives $L=\sqrt m$.

### Visualization

```text
loss
 ^
 | \                   L
 |  \                /
 |   \              /
 |    \            /
 |     \          /
 |      \________/
 |       near sqrt(m)
 +----------------------> L
       m/L decreases
```

### General balancing rule

Whenever an analysis produces

$$
aL+\frac{b}{L},
$$

the balancing choice is

$$
L\approx\sqrt{\frac{b}{a}}.
$$

This pattern occurs frequently in approximation algorithms, data structures, batching, graph decomposition, and parameter tuning.

---

## 13. Common Conceptual Mistakes

### Mistake 1: Confusing feasibility with approximation quality

Showing that every edge is covered proves only that the result is feasible. You must separately compare its size against $\operatorname{OPT}$.

### Mistake 2: Replacing maximal by maximum

The 2-approximation requires only a maximal matching. A maximum matching is not needed for the proof.

### Mistake 3: Claiming $|M|=\operatorname{OPT}$

The correct relationship is

$$
|M|\le\operatorname{OPT}.
$$

A matching is a lower-bound certificate, not generally an optimal cover.

### Mistake 4: Forgetting edge-disjointness in the charging argument

The statement “at most one optimal path can be charged through each edge” follows because the optimal paths are mutually edge-disjoint.

### Mistake 5: Omitting the one-path fallback

The short-path procedure can return zero when all feasible routes are long. The fallback converts an additive bound into a multiplicative approximation guarantee.

### Mistake 6: Treating a tight example as an inapproximability result

A ratio being tight for one specific algorithm does not prove that no better polynomial-time algorithm exists.

---

## 14. Quick Quiz

### Questions

1. For a minimization problem, what does it mean for $A$ to be a 3-approximation?
2. What is the difference between a PTAS and an FPTAS?
3. Why is the maximum-degree Vertex Cover algorithm always feasible?
4. If $r$ edges remain and an optimal cover has size $k$, why must one optimal vertex touch at least $r/k$ remaining edges?
5. What is the difference between a maximal matching and a maximum matching?
6. Why does every vertex cover have size at least $|M|$ for a matching $M$?
7. If the maximal-matching algorithm selects six matching edges, what can you conclude about the returned cover size and the optimal cover size?
8. Why can at most $m/(L+1)$ long optimal paths exist?
9. Why can one greedy path receive at most $L$ shared-edge charges from short optimal paths?
10. Why is there an additional $+1$ in $|O_{\text{short}}|\le(L+1)|A|$?
11. Give an instance where the short-path-only algorithm returns zero although $\operatorname{OPT}>0$.
12. Why is $L\approx\sqrt m$ the natural cutoff?

### Answers

1. It always returns a feasible solution satisfying

   $$
   A(I)\le 3\operatorname{OPT}(I).
   $$

2. A PTAS is polynomial in the input size for every fixed $\varepsilon$. An FPTAS must also be polynomial in $1/\varepsilon$.
3. It terminates only after every edge has been removed because some selected vertex covers it.
4. The $k$ optimal vertices collectively cover all $r$ edges. By averaging, one is incident to at least $r/k$ of them.
5. Maximal means that no edge can be added while preserving a matching. Maximum means largest cardinality among all matchings.
6. Every matching edge requires an endpoint in the cover, and disjoint matching edges require distinct covering vertices.
7. The algorithm returns 12 vertices, and

   $$
   \operatorname{OPT}\ge 6.
   $$

8. Each long path uses at least $L+1$ edges, the paths are edge-disjoint, and only $m$ edges exist.
9. The greedy path has at most $L$ edges, and edge-disjointness permits at most one optimal path to be associated through each edge.
10. At most one additional optimal path can be charged because the greedy path serves the same terminal pair.
11. A graph containing one feasible $s$-to-$t$ path of length $L+1$, with no shorter feasible path.
12. It balances the two competing terms $L$ and $m/L$.

---

## 15. Exam-Style Questions

### Question 1: Proof reconstruction

Let $G=(V,E)$ contain $m\ge1$ edges. The maximum-remaining-degree algorithm repeatedly chooses a vertex with maximum degree in the graph of uncovered edges.

Prove that it returns a cover of size at most

$$
\operatorname{OPT}(1+\ln m).
$$

Your proof must explicitly establish:

1. feasibility;
2. the averaging lower bound;
3. the recurrence for $r_t$;
4. the exponential bound; and
5. the stopping-time argument.

#### Solution outline

Let $r_t$ be the number of uncovered edges after $t$ selections. If $r_t>0$, an optimal cover of size $\operatorname{OPT}$ covers those edges, so one of its vertices covers at least $r_t/\operatorname{OPT}$. Greedy covers at least as many. Hence,

$$
r_{t+1}
\le
r_t\left(1-\frac1{\operatorname{OPT}}\right).
$$

Induction and $1-x\le e^{-x}$ give

$$
r_t\le me^{-t/\operatorname{OPT}}.
$$

For $t>\operatorname{OPT}\ln m$, this is less than 1. Since $r_t$ is integral, it must be zero. Accounting for integer rounding gives at most $\operatorname{OPT}(1+\ln m)$ choices.

### Question 2: Algorithm execution

Run the maximal-matching Vertex Cover algorithm on

$$
E=\{(a,b),(a,c),(b,c),(b,d),(c,e),(d,e)\}
$$

using $(a,b)$ as the first selected edge.

1. List the removed edges.
2. Identify the remaining graph.
3. Complete the algorithm.
4. State the matching $M$ and cover $C$.
5. Give the lower bound on $\operatorname{OPT}$ supplied by $M$.

#### Expected reasoning

Selecting $(a,b)$ removes every edge incident to $a$ or $b$:

$$
(a,b),(a,c),(b,c),(b,d).
$$

Only $(c,e)$ and $(d,e)$ remain. Selecting either one removes both remaining edges. Thus,

$$
|M|=2,
\qquad
|C|=4,
\qquad
2=|M|\le\operatorname{OPT}.
$$

### Question 3: Maximal versus maximum

Construct a graph and a maximal matching $M$ such that

$$
|M|<|M^\star|,
$$

where $M^\star$ is a maximum matching. Explain why the factor-2 Vertex Cover proof remains valid.

#### Suggested answer

Use the path

$$
a-b-c-d.
$$

The matching $\{(b,c)\}$ is maximal, but the maximum matching

$$
\{(a,b),(c,d)\}
$$

has size 2. The proof needs only:

1. the selected edges to be disjoint, yielding $|M|\le\operatorname{OPT}$; and
2. maximality, ensuring that the endpoints cover every graph edge.

It does not require $M$ to be maximum.

### Question 4: Charging argument

In the directed edge-disjoint paths algorithm, prove

$$
|O_{\text{short}}|\le(L+1)|A|.
$$

Clearly identify the two kinds of charges and explain where edge-disjointness is used.

#### Solution outline

For each short optimal path $Q_i$:

- if greedy routes pair $i$, charge $Q_i$ to that greedy path;
- otherwise, $Q_i$ must contain an edge removed by some greedy path, or it would remain an available short path at termination.

Each selected greedy path has at most $L$ edges. Since optimal paths are edge-disjoint, at most one optimal path can charge through each such edge. This gives at most $L$ intersection charges, plus at most one same-pair charge.

### Question 5: Optimize the cutoff

Suppose an analysis gives

$$
\operatorname{OPT}
\le
\left(L+c+\frac{m}{L}\right)A,
$$

where $c$ is a fixed constant and $L>0$.

1. Choose $L$ to minimize the leading asymptotic bound.
2. State the resulting approximation factor.

#### Answer

Ignore the additive constant while choosing the asymptotic optimizer:

$$
f(L)=L+\frac{m}{L}.
$$

Then

$$
f'(L)=1-\frac{m}{L^2}=0
$$

implies

$$
L=\sqrt m.
$$

The resulting factor is

$$
2\sqrt m+c=O(\sqrt m).
$$

### Question 6: Identify a proof flaw

A student writes:

> Every selected greedy path has at most $L$ edges, so it can intersect at most $L$ other paths.

Explain why this claim is incomplete and repair it.

#### Answer

A single edge can lie on arbitrarily many paths in a general path collection. The claim becomes valid only because the paths in the fixed optimal solution $O$ are pairwise edge-disjoint. Therefore, each edge of the greedy path belongs to at most one optimal path, giving at most $L$ shared-edge charges.

### Question 7: Design problem

Suppose each directed edge has a positive integer capacity $c_e$, and up to $c_e$ selected paths may use edge $e$.

Describe how the long-path counting and short-path charging arguments would need to change.

#### Expected direction

Treat total edge capacity as the global resource:

$$
C_{\mathrm{tot}}=\sum_{e\in E}c_e.
$$

A long path still consumes at least $L+1$ units of capacity, so a capacity-respecting optimal solution contains at most approximately

$$
\frac{C_{\mathrm{tot}}}{L+1}
$$

long paths. For charging, an edge $e$ may support up to $c_e$ optimal paths, so a selected path $P$ may receive as many as

$$
\sum_{e\in P}c_e
$$

intersection charges. A useful approximation guarantee would require either bounded capacities or an adjusted path-length or resource measure.

---

## 16. Suggested Textbook References

1. **Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, _Introduction to Algorithms_, Chapter 35.**  
   Particularly relevant for approximation definitions, the maximal-matching 2-approximation for Vertex Cover, Set Cover, approximation schemes, and related methods.

2. **David P. Williamson and David B. Shmoys, _The Design of Approximation Algorithms_.**  
   Especially useful for greedy algorithms, local search, dynamic programming, LP rounding, randomized rounding, primal-dual methods, cuts, and hardness of approximation.

3. **Vijay V. Vazirani, _Approximation Algorithms_.**  
   A theory-oriented treatment of combinatorial approximation algorithms, LP-based methods, and hardness of approximation.

### Recommended reading order

```text
Lecture note
    |
    v
CLRS Chapter 35
    |
    v
Williamson and Shmoys: greedy and local-search chapters
    |
    v
Vazirani: combinatorial and LP-based methods
```

---

## 17. Final Memory Map

```text
Approximation algorithms
|
+-- Guarantee
|   +-- minimization: A <= alpha * OPT
|   +-- maximization: A >= OPT / alpha
|
+-- Vertex Cover: maximum degree
|   +-- averaging over an optimal cover
|   +-- multiplicative decay
|   +-- 1 + ln(m) approximation
|
+-- Vertex Cover: maximal matching
|   +-- matching gives |M| <= OPT
|   +-- endpoints give |C| = 2|M|
|   +-- 2-approximation
|
+-- Directed edge-disjoint paths
    +-- short/long optimum split
    +-- charge short paths
    +-- count long paths
    +-- add one-path fallback
    +-- balance L and m/L at L approximately sqrt(m)
```

The key exam-level principle is

$$
\boxed{
\text{Approximation proof}
=
\text{feasible construction}
+
\text{certificate for }\operatorname{OPT}
+
\text{comparison argument}
}.
$$

Here, the certificates are a matching, multiplicative edge reduction, edge capacity, and a charging map. Those proof objects are more important than the superficial fact that each algorithm is “greedy.”

## 18. Video Lectures

Best match for your Lecture 14 material
1. MIT 6.046J Lecture 17: Complexity and Approximation Algorithms

Start here. This 81-minute lecture closely matches your notes: approximation ratios, Vertex Cover, greedy analysis, Set Cover, Partition, PTAS, and FPTAS. The Vertex Cover discussion begins around 10 minutes, Set Cover around 25 minutes, and approximation schemes around 45 minutes.

Why it fits: Your lecture’s maximum-degree Vertex Cover proof is essentially the Set Cover greedy analysis, while the maximal-matching algorithm is the standard 2-approximation covered here.

2. DAA 27: Approximation Algorithms and 2-Approximation for Vertex Cover

This focused 45-minute lecture covers formal approximation guarantees, cardinality Vertex Cover using maximal matching, tight examples, weighted Vertex Cover, LP relaxation, and threshold rounding.

Why it fits: The first half reinforces your current maximal-matching proof. The LP-rounding portion previews the next topic mentioned at the end of your lecture note.

3. Rounding LP Solutions: Minimum Vertex Cover

This 17-minute Carnegie Mellon University CS Theory Toolkit lecture develops the Vertex Cover integer program, LP relaxation, integrality gap, rounding rule, 2-approximation proof, and half-integrality.

Why it fits: Watch this immediately after mastering the combinatorial maximal-matching argument. It explains how an LP optimum becomes a lower-bound certificate for $\operatorname{OPT}$.

For broader and more visual coverage
4. Approximation Algorithms: Vertex Cover, TSP, and Set Cover

This lecture covers approximation ratios, the maximal-matching Vertex Cover algorithm, metric TSP, greedy Set Cover, and inapproximability. It also advertises interactive demonstrations for experimenting with graphs and comparing approximate solutions with optimal ones.

Best use: Watch after the MIT 6.046J lecture if you want more visual intuition before redoing the proofs.

5. NPTEL Approximation Algorithms

For a complete graduate-level sequence, this course covers deterministic, dual, and randomized rounding; LP duality; greedy and primal-dual Set Cover; scheduling; $k$-center; metric TSP; Knapsack FPTAS; makespan PTAS; bin packing; facility location; MAX-SAT; and MAX-CUT.

For your immediate material, prioritize:

Lectures 1–8: approximation foundations and Set Cover
Lectures 11–12: greedy scheduling and approximation analysis
Lectures 17–18: pseudopolynomial Knapsack and FPTAS
Lectures 32–35: randomized approximation and derandomization

The published course outline does not specifically list directed edge-disjoint paths, so use this primarily for the underlying techniques rather than that exact problem.

Recommended viewing sequence

MIT 6.046J Lecture 17
 Build the core framework: feasible solution, approximation ratio, lower bound, and comparison with $\operatorname{OPT}$.

DAA 27
 Revisit maximal-matching Vertex Cover, then continue into weighted Vertex Cover and LP rounding.

CMU LP Rounding: Minimum Vertex Cover
 Study the LP lower bound, rounding proof, and integrality gap.

Approximation Algorithms: Vertex Cover, TSP, and Set Cover
 Reinforce the algorithms through visual and interactive examples.

NPTEL Approximation Algorithms
 Continue into primal-dual algorithms, randomized rounding, PTAS/FPTAS, and broader graduate-level topics.

While watching

For each algorithm, write down these five items:

1. What is the feasible solution?
2. What quantity bounds OPT?
3. Is it an upper or lower bound?
4. How is the algorithm's value related to that bound?
5. Which example makes the analysis tight?


For the directed edge-disjoint paths section in your note, add:

6. How is OPT partitioned into short and long paths?
7. What is charged to each greedy path?
8. Where is edge-disjointness used?
9. Why is the one-path fallback necessary?
10. Why does balancing L and m/L produce L approximately sqrt(m)?
