# Lecture 14 Study Guide: Approximation Algorithms and Greedy Methods

The lecture asks: when finding an exact optimum is computationally difficult, can we efficiently find a feasible solution with a provable quality guarantee?

Its central idea is to compare the algorithm’s output with a **certificate** or structural bound on the unknown optimum. The lecture develops three examples: a logarithmic approximation for Vertex Cover, a stronger matching-based 2-approximation, and an $O(\sqrt m)$-approximation for directed edge-disjoint paths. [Lecture 14]

This guide follows the lecture’s order, expands the proofs, and includes worked examples, text visualizations, pseudocode, quizzes, exam problems, and textbook readings.

> Rendering note: This document uses GitHub-supported inline and display math. View the rendered Markdown on GitHub rather than its raw source. Diagrams and pseudocode use fenced code blocks.

---

## 1. Approximation guarantees: what are we promising?

Let:

- $I$ be a problem instance.
- $\mathrm{OPT}(I)$ be the optimal objective value.
- $\mathrm{ALG}(I)$ be the value returned by an algorithm.
- $\alpha\ge 1$ be its approximation factor.

The algorithm must return a feasible solution; a good objective value does not compensate for violating the constraints. [Lecture 14]

### 1.1 Minimization problems

For minimization, smaller is better. An $\alpha$-approximation guarantees

$$
\mathrm{OPT}(I)\le \mathrm{ALG}(I)\le \alpha\,\mathrm{OPT}(I).
$$

Example: if the minimum vertex cover has size $6$, a 2-approximation must return a valid cover containing between $6$ and $12$ vertices.

```text
Minimization: smaller is better

       OPT                        α · OPT
--------|----------------------------|------------->
        <--- permitted ALG values --->
```

### 1.2 Maximization problems

For maximization, larger is better. An $\alpha$-approximation guarantees

$$
\frac{\mathrm{OPT}(I)}{\alpha}
\le \mathrm{ALG}(I)
\le \mathrm{OPT}(I).
$$

Example: if an optimal routing connects $20$ pairs, a 4-approximation must connect at least $5$.

```text
Maximization: larger is better

       OPT / α                     OPT
----------|--------------------------|------------->
          <--- permitted ALG values ->
```

These are worst-case guarantees: they hold for every valid input, not merely for typical inputs or on average. A factor closer to $1$ is stronger. [Lecture 14]

### 1.3 A guarantee is not a prediction

A 2-approximation can return the exact optimum on many instances. The guarantee says only that its output cannot be worse than twice the optimum in the minimization setting.

Similarly, proving a factor of $2$ for one algorithm does not establish that every polynomial-time algorithm must lose a factor of $2$. That would require a separate hardness-of-approximation result. [Lecture 14]

---

## 2. PTAS versus FPTAS

An approximation scheme takes an accuracy parameter $\varepsilon>0$.

For minimization, the target is

$$
\mathrm{ALG}\le (1+\varepsilon)\mathrm{OPT}.
$$

For maximization, a common convention is

$$
\mathrm{ALG}\ge (1-\varepsilon)\mathrm{OPT},
\qquad 0<\varepsilon<1.
$$

The distinction between PTAS and FPTAS concerns how running time depends on the requested accuracy. [Lecture 14]

| Scheme | Required running-time behavior | Illustrative running time |
|---|---|---|
| PTAS | Polynomial in input size for every fixed $\varepsilon$ | $O(n^{\lceil 1/\varepsilon\rceil})$ |
| FPTAS | Polynomial in both input size and $1/\varepsilon$ | $O(n^3/\varepsilon^2)$ |

For the PTAS example:

- $\varepsilon=0.1$ gives $O(n^{10})$.
- $\varepsilon=0.01$ gives $O(n^{100})$.

Each is polynomial for fixed $\varepsilon$, but the dependence on accuracy is severe.

For the FPTAS example, reducing $\varepsilon$ by a factor of $10$ increases the displayed running-time bound by a factor of $100$, with $n$ held fixed. These examples illustrate the definitions; the runtime alone is not enough—the algorithm must also satisfy the approximation guarantee. [CLRS, Chapter 35](http://cs.bme.hu/thalg/approx.pdf)

---

## 3. Vertex Cover: understanding the problem

Given an undirected graph $G=(V,E)$, a vertex cover is a set $C\subseteq V$ such that every edge has at least one endpoint in $C$.

The objective is to minimize $|C|$. [Lecture 14]

### Example: a star

```text
        a
        |
    b---c---d
        |
        e
```

The edges are

$$
E=\{(a,c),(b,c),(c,d),(c,e)\}.
$$

Two possible covers are:

- $\{c\}$, of size $1$.
- $\{a,b,d,e\}$, of size $4$.

Thus

$$
\mathrm{OPT}=1.
$$

The center covers every edge at once. This makes “choose the highest-degree vertex” seem like a natural greedy strategy.

---

## 4. Algorithm 1: choose the largest remaining degree

### 4.1 The greedy rule

Repeatedly select the vertex incident to the most currently uncovered edges.

The word “currently” matters: degrees must be recomputed or updated after edges are covered. Original degrees are not the correct selection criterion. [Lecture 14]

### Pseudocode

```text
GREEDY-DEGREE-COVER(G = (V, E)):
    C ← empty set
    R ← copy of E

    while R is not empty:
        choose v maximizing
            number of edges in R incident to v

        add v to C

        remove from R every edge incident to v

    return C
```

### 4.2 Worked example: a locally best choice can be suboptimal

Consider the path

```text
a --- b --- c --- d --- e
```

Initially:

$$
\deg(a)=\deg(e)=1,
\qquad
\deg(b)=\deg(c)=\deg(d)=2.
$$

Suppose ties are broken by choosing $c$.

| Step | Choice | Newly covered edges | Remaining edges |
|---|---|---|---|
| 1 | $c$ | $(b,c),(c,d)$ | $(a,b),(d,e)$ |
| 2 | $b$ | $(a,b)$ | $(d,e)$ |
| 3 | $d$ | $(d,e)$ | None |

The algorithm returns

$$
C=\{b,c,d\},
\qquad |C|=3.
$$

But

$$
C^*=\{b,d\}
$$

covers all four edges. Moreover, the disjoint edges $(a,b)$ and $(d,e)$ require at least two cover vertices, so $\mathrm{OPT}=2$.

The ratio on this run is therefore

$$
\frac{3}{2}.
$$

This illustrates a general warning: maximizing immediate progress need not minimize the final number of choices.

### 4.3 Why the algorithm always returns a valid cover

Maintain the invariant:

> Every edge removed from the remaining graph has an endpoint in $C$.

When the algorithm stops, no edges remain. Therefore every original edge is covered.

Feasibility is straightforward; bounding the number of selected vertices is the main challenge. [Lecture 14]

---

## 5. Why degree-greedy has a logarithmic guarantee

The lecture proves that, for $m=|E|\ge1$,

$$
|C|\le \mathrm{OPT}(1+\ln m).
$$

For simple graphs, this gives an $O(\log n)$-approximation. [Lecture 14]

### 5.1 The key averaging argument

Let $C^*$ be an optimal cover, and write

$$
k=|C^*|=\mathrm{OPT}.
$$

Suppose $r$ uncovered edges remain.

The vertices in $C^*$ still cover all $r$ remaining edges. Consequently, the total number of incidences between remaining edges and vertices in $C^*$ is at least $r$.

Some vertex in $C^*$ must therefore touch at least

$$
\frac{r}{k}
$$

remaining edges.

Since greedy chooses a maximum-degree vertex, it covers at least that many.

```text
r remaining edges
        |
        | all are covered by the k optimum vertices
        v
At least one optimum vertex covers ≥ r/k edges
        |
        | greedy chooses a vertex at least as good
        v
Greedy removes ≥ r/k edges
```

We use the existence of $C^*$ in the proof; the algorithm does not need to know it. [Lecture 14]

### 5.2 Deriving the recurrence

Let $r_t$ be the number of uncovered edges after $t$ selections. Then

$$
r_{t+1}
\le r_t-\frac{r_t}{k}
=
r_t\left(1-\frac1k\right).
$$

Starting from $r_0=m$,

$$
r_t
\le
m\left(1-\frac1k\right)^t
\le
me^{-t/k},
$$

where the final step uses $1-x\le e^{-x}$. [Lecture 14]

This is multiplicative shrinkage:

```text
m
  × (1 − 1/k)
  × (1 − 1/k)
  × (1 − 1/k)
  ...
```

### 5.3 Why “less than one” finishes the proof

If

$$
t>k\ln m,
$$

then

$$
me^{-t/k}<1.
$$

But $r_t$ is a nonnegative integer. Thus $r_t<1$ implies $r_t=0$.

The number of selections is at most

$$
\lfloor k\ln m\rfloor+1
\le k(1+\ln m).
$$

Therefore,

$$
\boxed{|C|\le (1+\ln m)\mathrm{OPT}.}
$$

The integer argument is essential: exponential decay alone only says the upper bound approaches zero; integrality converts that into actual termination. [Lecture 14]

### 5.4 Connection to Set Cover

Vertex Cover is a special case of Set Cover:

| Vertex Cover object | Set Cover interpretation |
|---|---|
| Edge | Element to be covered |
| Vertex $v$ | Set of edges incident to $v$ |
| Selected vertices | Selected sets |
| Maximum remaining degree | Largest number of uncovered elements |

This explains why the analysis resembles greedy Set Cover. [Lecture 14; Kleinberg and Tardos, Chapter 11](https://nscpolteksby.ac.id/ebook/files/Ebook/Computer%20Engineering/Algorithm%20Design%20(2005)/12.%20Chapter%2011%20-%20Approximation%20Algorithms.pdf)

### 5.5 Running time

A straightforward implementation that scans all vertices and remaining edges on each iteration runs in

$$
O(n(n+m)),
$$

because there are at most $n$ selections.

The lecture’s guarantee concerns solution quality, not an optimal implementation of this greedy rule.

---

## 6. Algorithm 2: take both endpoints of an uncovered edge

The second algorithm makes an apparently less sophisticated choice:

1. Pick any uncovered edge $(u,v)$.
2. Add both $u$ and $v$ to the cover.
3. Remove every edge incident to either endpoint.
4. Repeat.

Despite not optimizing the immediate number of covered edges, it has the stronger constant-factor guarantee

$$
|C|\le 2\mathrm{OPT}.
$$

Its analysis exploits matching structure. [Lecture 14]

### 6.1 Pseudocode: a linear-time implementation

Instead of explicitly deleting edges, scan the edge list and keep track of vertices already matched.

```text
MATCHING-VERTEX-COVER(G = (V, E)):
    matched[v] ← false for every v in V
    M ← empty set
    C ← empty set

    for each edge (u, v) in E:
        if matched[u] = false and matched[v] = false:
            add (u, v) to M

            matched[u] ← true
            matched[v] ← true

            add u and v to C

    return C, M
```

This constructs a maximal matching and returns its endpoints. With an edge list or adjacency-list representation, the running time is

$$
O(n+m).
$$

The standard endpoint-selection algorithm admits this linear-time implementation. [CLRS, Chapter 35](http://cs.bme.hu/thalg/approx.pdf)

### 6.2 Worked example

Again consider

```text
a --- b --- c --- d --- e
```

Suppose the first selected edge is $(b,c)$.

```text
Selected matching edge:

a --- [b === c] --- d --- e
```

Both $b$ and $c$ enter the cover. The edges touching them are covered, leaving $(d,e)$. Select that edge next.

Thus

$$
M=\{(b,c),(d,e)\},
$$

and

$$
C=\{b,c,d,e\}.
$$

Here:

$$
|C|=4,
\qquad \mathrm{OPT}=2,
$$

so the factor $2$ is attained.

### 6.3 Matching, maximal matching, maximum matching

A matching is a set of edges sharing no endpoints.

A maximal matching cannot be enlarged by adding another edge.

A maximum matching has the largest possible number of edges. [Lecture 14]

These are different:

```text
a --- b --- c --- d
```

- $\{(b,c)\}$ is maximal: neither remaining edge can be added.
- $\{(a,b),(c,d)\}$ is maximum: it has two edges.

The approximation algorithm requires maximality, not maximum cardinality.

---

## 7. The 2-approximation proof

There are three ingredients.

### 7.1 The selected edges form a matching

Once $(u,v)$ is chosen, later selected edges cannot touch $u$ or $v$.

Therefore no two selected edges share an endpoint. [Lecture 14]

### 7.2 The endpoints cover every edge

Suppose an edge $(x,y)$ had neither endpoint among the matching endpoints.

Then it could be added to the matching, contradicting maximality.

Therefore the endpoints of a maximal matching form a vertex cover. [Lecture 14]

### 7.3 Every cover needs at least one vertex per matching edge

Visualize the selected matching:

```text
u1 === v1      u2 === v2      u3 === v3
```

Any vertex cover must select at least one endpoint of each displayed edge.

Because the edges have disjoint endpoints, these requirements need distinct vertices. Hence

$$
|M|\le \mathrm{OPT}.
$$

The algorithm selects exactly two endpoints per matching edge:

$$
|C|=2|M|.
$$

Combining,

$$
\boxed{|C|=2|M|\le 2\mathrm{OPT}.}
$$

This is the lecture’s simplest example of proving an approximation without computing the optimum. [Lecture 14]

### 7.4 Why choosing only one endpoint fails

Consider:

```text
a --- b --- c
```

Choose edge $(a,b)$, but add only $a$.

Then $(b,c)$ remains uncovered. If the algorithm nevertheless removes all edges incident to both $a$ and $b$, it can incorrectly terminate.

Taking both endpoints is what makes that deletion rule safe.

### 7.5 Comparing the two algorithms

| Feature | Degree-greedy | Matching-based |
|---|---|---|
| Choice | Highest remaining degree | Any available edge |
| Vertices added per step | One | Two |
| Lecture guarantee | $1+\ln m$ | $2$ |
| Proof structure | Averaging and shrinkage | Matching lower bound |
| Can return an optimum? | Yes | Yes |
| Must outperform the other on every graph? | No | No |

A stronger worst-case guarantee does not mean uniformly better output on every instance. On the star, degree-greedy returns one vertex, while the matching-based algorithm returns two. [Lecture 14]

---

## 8. Directed edge-disjoint paths

### 8.1 Problem definition

The input consists of:

- A directed graph $G=(V,E)$.
- Terminal pairs $(s_i,t_i)$, for $i=1,\ldots,k$.

Choose paths connecting as many distinct pairs as possible, subject to:

1. Each path follows edge directions.
2. At most one path is selected per pair.
3. No directed edge is used by two selected paths.

The objective is the number of routed pairs—not total path length or the number of edges used. [Lecture 14]

### 8.2 Edge-disjoint does not mean vertex-disjoint

These two paths share a vertex but no edges:

```text
s1 ----> x ----> t1
         ^
         |
s2 ------+
         |
         v
         t2
```

Their edge sets are

$$
\{(s_1,x),(x,t_1)\}
$$

and

$$
\{(s_2,x),(x,t_2)\}.
$$

Sharing $x$ is allowed. Sharing the same directed edge is not.

### 8.3 Why favor short paths?

A long chosen path consumes many edges that might otherwise support several requests.

Short paths use fewer resources, but a locally shortest choice can still block a better global arrangement. The lecture’s goal is therefore an approximation, not a proof of exact optimality. [Lecture 14]

---

## 9. The short-path greedy algorithm—and its necessary fallback

Let $m=|E|\ge1$, and set

$$
L=\max\{1,\lfloor\sqrt m\rfloor\}.
$$

Repeatedly route any remaining pair with a residual path of at most $L$ edges.

After selecting a path:

- Delete its edges.
- Remove its pair from consideration.

Breadth-first search finds shortest paths when length means number of edges. [Lecture 14]

### 9.1 A subtle but essential repair

The cutoff-only algorithm can return zero even though a feasible request exists.

Example:

```text
s ---> a ---> b ---> t
```

There are $m=3$ edges, so $L=1$. The only $s$-to-$t$ path has length $3$, and the cutoff algorithm rejects it.

Thus

$$
|A|=0,
\qquad \mathrm{OPT}=1.
$$

No finite multiplicative approximation factor allows zero output when the optimum is positive.

The lecture fixes this by separately finding one arbitrary feasible path in the original graph, if one exists, and returning whichever is larger:

- The short-path greedy solution.
- That one-path fallback solution. [Lecture 14]

The solutions are alternatives; do not combine them, because they may share edges.

### 9.2 Complete pseudocode

Assume each terminal pair has distinct endpoints, so every routed path uses at least one edge.

```text
APPROX-EDGE-DISJOINT-PATHS(G, terminal_pairs):
    m ← number of edges in G

    if m = 0:
        return empty collection

    L ← max(1, floor(sqrt(m)))

    fallback ← empty collection

    for each pair i:
        P ← BFS path from s[i] to t[i] in the original G
        if P exists:
            fallback ← {(i, P)}
            break

    H ← copy of G
    R ← all terminal-pair indices
    A ← empty collection

    while true:
        chosen ← NONE

        for each i in R:
            P ← shortest s[i]-to-t[i] path in H using BFS

            if P exists and length(P) ≤ L:
                chosen ← (i, P)
                break

        if chosen = NONE:
            break

        add chosen to A
        remove the edges of chosen.P from H
        remove chosen.i from R

    if |A| ≥ |fallback|:
        return A
    else:
        return fallback
```

The fallback is present in the proof discussion in the notes; writing it explicitly in the algorithm prevents a mismatch between the algorithm and its theorem. [Lecture 14]

### 9.3 Worked example: greedy routes one, optimum routes two

Let the graph contain exactly these seven edges:

```text
s1 -> a -> b -> t1 -> t2
 |              ^
 v              |
 v -------------+
 ^
 |
s2
```

Here the vertex named $v$ is the lower junction. The edge list is

$$
\begin{aligned}
E=\{&
(s_1,a),(a,b),(b,t_1),(t_1,t_2),\\
& (s_1,v),(v,t_1),(s_2,v)\}.
\end{aligned}
$$

The requested pairs are

$$
(s_1,t_1),\qquad (s_2,t_2).
$$

Since $m=7$,

$$
L=\lfloor\sqrt7\rfloor=2.
$$

Greedy selects the two-edge path

$$
s_1\to v\to t_1.
$$

Deleting its edges destroys the only route for the second pair, so greedy returns one path.

But an optimal solution uses

$$
s_1\to a\to b\to t_1
$$

and

$$
s_2\to v\to t_1\to t_2.
$$

These paths share vertex $t_1$, but no edge. Hence

$$
\mathrm{ALG}=1,
\qquad \mathrm{OPT}=2.
$$

The example shows why local resource efficiency does not imply global optimality.

---

## 10. Proving the O(√m) approximation

Let:

- $O$ be an optimal collection of paths.
- $A$ be the cutoff-greedy collection.
- $a$ be the number of paths returned after comparison with the fallback.

If $\mathrm{OPT}>0$, then

$$
a\ge1,
\qquad a\ge |A|.
$$

Partition the optimum:

$$
O=O_{\text{short}}\cup O_{\text{long}},
$$

where short paths have at most $L$ edges and long paths have more than $L$. [Lecture 14]

### 10.1 Long optimal paths: count their edge usage

Every long optimal path uses at least $L+1$ edges.

Since optimal paths are edge-disjoint,

$$
(L+1)|O_{\text{long}}|\le m.
$$

Therefore,

$$
\boxed{|O_{\text{long}}|\le \frac{m}{L+1}.}
$$

```text
Total edge budget: m

[ long path: ≥ L+1 edges ]
[ long path: ≥ L+1 edges ]
[ long path: ≥ L+1 edges ]
...
```

The graph cannot contain too many mutually edge-disjoint long paths. [Lecture 14]

### 10.2 Short optimal paths: charge them to greedy paths

Consider a short optimal path $Q$ for pair $i$.

There are two cases.

1. Greedy routed pair $i$. Charge $Q$ to the greedy path serving that pair.
2. Greedy did not route pair $i$. If all edges of $Q$ survived, $Q$ would still be an available path of length at most $L$, contradicting termination. Thus $Q$ shares an edge with some selected greedy path; charge it to one such path. [Lecture 14]

This use of termination is crucial. The algorithm does not stop because no route of any length exists; it stops because no eligible short route remains.

### 10.3 Why each greedy path receives at most L+1 charges

Take a greedy path $P$. It contains at most $L$ edges.

Because paths in $O$ are edge-disjoint, each edge of $P$ belongs to at most one optimal path. Therefore at most $L$ optimal paths can be charged to $P$ through shared edges.

There can also be one additional charge for the same terminal pair.

```text
Greedy path P:

v0 --e1--> v1 --e2--> ... --eL--> vL
      ↑          ↑                  ↑
   ≤1 charge  ≤1 charge          ≤1 charge

Plus at most one same-pair charge
```

Hence

$$
\boxed{|O_{\text{short}}|\le (L+1)|A|.}
$$

The extra $1$ is necessary: the optimal route for a pair could be completely different from—and edge-disjoint from—the greedy route for that same pair. [Lecture 14]

### 10.4 Combine the two bounds

We have

$$
\begin{aligned}
\mathrm{OPT}
&=|O_{\text{short}}|+|O_{\text{long}}|\\
&\le (L+1)|A|+\frac{m}{L+1}.
\end{aligned}
$$

Using $|A|\le a$ and $a\ge1$,

$$
\begin{aligned}
\mathrm{OPT}
&\le (L+1)a+\frac{m}{L+1}a\\
&=
\left(L+1+\frac{m}{L+1}\right)a.
\end{aligned}
$$

For $L=\lfloor\sqrt m\rfloor$,

$$
L+1\le \sqrt m+1,
\qquad
\frac{m}{L+1}<\sqrt m.
$$

Consequently,

$$
\mathrm{OPT}\le (2\sqrt m+1)a,
$$

or

$$
\boxed{
a\ge \frac{\mathrm{OPT}}{2\sqrt m+1}.
}
$$

This is the claimed $O(\sqrt m)$-approximation. The case $\mathrm{OPT}=0$ is immediate. [Lecture 14]

### 10.5 Why a square root appears

Ignoring rounding and additive constants, the factor behaves like

$$
f(L)=L+\frac{m}{L}.
$$

The two terms move in opposite directions:

| Threshold $L$ | Charging cost $L$ | Long-path bound $m/L$ |
|---|---|---|
| Small | Small | Large |
| Large | Large | Small |
| Near $\sqrt m$ | Near $\sqrt m$ | Near $\sqrt m$ |

Balance them:

$$
L\approx \frac{m}{L}
\quad\Longrightarrow\quad
L\approx \sqrt m.
$$

This “split into small and large objects, bound each differently, then balance” pattern is the main reusable technique in this proof. [Lecture 14]

### 10.6 Running time

For the straightforward pseudocode:

- One BFS costs $O(n+m)$.
- One search round examines at most $k$ pairs.
- There are at most $k$ successful rounds and one unsuccessful round.

A valid polynomial upper bound is therefore

$$
O(k^2(n+m)).
$$

This bound is for the simple implementation above, not a claim of optimal implementation efficiency.

---

## 11. Bridge to linear programming

The lecture ends by asking whether an LP relaxation can replace a matching as the lower-bound tool. [Lecture 14]

For unweighted Vertex Cover, introduce a variable $x_v$ for every vertex:

$$
\begin{aligned}
\text{minimize}\quad
&\sum_{v\in V}x_v\\
\text{subject to}\quad
&x_u+x_v\ge1
&&\text{for every }(u,v)\in E,\\
&x_v\ge0
&&\text{for every }v.
\end{aligned}
$$

Every integral cover gives a feasible LP solution, so

$$
\mathrm{OPT}_{LP}\le\mathrm{OPT}.
$$

Round by selecting

$$
C=\{v:x_v\ge\tfrac12\}.
$$

For every edge, $x_u+x_v\ge1$, so at least one endpoint is selected. Also,

$$
|C|
\le 2\sum_v x_v
=
2\mathrm{OPT}_{LP}
\le 2\mathrm{OPT}.
$$

This produces another 2-approximation, now using an LP lower bound rather than an integral matching. LP rounding for Vertex Cover is developed in the textbook treatments of approximation algorithms. [CLRS, Chapter 35](http://cs.bme.hu/thalg/approx.pdf); [Vazirani](https://www.ics.uci.edu/~vazirani/book.pdf).

---

## 12. Quick quiz

Try these before reading the answer key.

### Questions

1. A minimization problem has $\mathrm{OPT}=8$. What output values are permitted for a 3-approximation?

2. A maximization problem has $\mathrm{OPT}=30$. What minimum output does a 5-approximation guarantee?

3. Why does degree-greedy measure degrees among remaining edges rather than original edges?

4. In the degree-greedy proof, why does some vertex cover at least $r/\mathrm{OPT}$ remaining edges?

5. True or false: every maximal matching is maximum.

6. Does the endpoint set of every matching form a vertex cover? Explain.

7. Why is $|M|$ a lower bound on minimum vertex-cover size?

8. Can edge-disjoint paths share vertices?

9. Why can cutoff-only path greedy fail to have any finite multiplicative approximation factor?

10. Where does the $+1$ in the short-path charging bound $L+1$ come from?

11. Why does the long-path bound use $m/(L+1)$, rather than $m/L$?

12. An approximation scheme runs in $O(n^{1/\varepsilon})$. Is that runtime polynomial in both $n$ and $1/\varepsilon$?

### Answer key

1. A feasible output value between $8$ and $24$.

2. At least $30/5=6$.

3. Only uncovered edges represent new progress. Original degrees can overcount already covered edges.

4. The $\mathrm{OPT}$ vertices of an optimum cover collectively cover all $r$ remaining edges. Averaging gives the claim.

5. False. The middle edge of a four-vertex path is a maximal matching of size one; a maximum matching has size two.

6. No. An arbitrary matching can leave a separate edge untouched. Maximality ensures its endpoints cover every edge.

7. Every matching edge needs a cover endpoint, and disjoint matching edges require distinct cover vertices.

8. Yes. They must not share directed edges.

9. It can return zero while $\mathrm{OPT}>0$, as when every feasible route exceeds the cutoff.

10. At most one optimal path can be charged because it serves the same terminal pair, separately from shared-edge charges.

11. An integer-length path longer than $L$ has at least $L+1$ edges.

12. No. It is polynomial in $n$ for fixed $\varepsilon$, but this runtime does not meet the FPTAS requirement.

The quiz tests the definitions and proof mechanisms developed in the lecture. [Lecture 14]

---

## 13. Exam-style problems

These original problems are designed around the lecture’s main techniques.

### Problem 1: trace and compare the algorithms — 15 points

Consider

```text
a --- b --- c --- d --- e
```

1. Run degree-greedy with $c$ selected first.
2. Run matching-based Vertex Cover with $(b,c)$ selected first.
3. Find an optimal cover and prove its optimality.
4. Compute the two observed approximation ratios.

### Problem 2: reconstruct the logarithmic proof — 20 points

Let $G$ have $m\ge1$ edges and minimum vertex-cover size $k$.

1. Prove that degree-greedy covers at least $r/k$ edges when $r$ edges remain.
2. Derive a recurrence for $r_t$.
3. Show $r_t\le me^{-t/k}$.
4. Deduce a bound of $k(1+\ln m)$ selections.
5. Identify precisely where integrality is used.

### Problem 3: distinguish maximality from maximum size — 15 points

A student proposes:

> Find any matching $M$, then return all its endpoints.

1. Give a counterexample to feasibility.
2. State the missing property.
3. Prove feasibility after adding that property.
4. Prove the factor-2 guarantee.

### Problem 4: analyze an arbitrary path threshold — 25 points

Modify the cutoff algorithm to use any integer threshold $L\ge1$, retaining the one-path fallback.

Prove that its approximation factor is at most

$$
L+1+\frac{m}{L+1}.
$$

Then explain how to choose $L$ to obtain an $O(\sqrt m)$ factor.

Your proof must address:

- Feasibility.
- Short optimal paths.
- Long optimal paths.
- The case of positive optimum but empty cutoff solution.

### Problem 5: diagnose a flawed proof — 15 points

A student writes:

> Every short optimal path intersects a selected greedy path. A greedy path has at most $L$ edges, so at most $L$ short optimal paths can be charged to it. Therefore $\mathrm{OPT}\le L|A|+m/(L+1)$, which immediately gives a multiplicative approximation.

Identify two distinct gaps and repair them.

### Problem 6: LP-rounding extension — 10 points

For the Vertex Cover LP in Section 11:

1. Prove that selecting vertices with $x_v\ge1/2$ produces a cover.
2. Prove the output has size at most $2\mathrm{OPT}_{LP}$.
3. Explain why $\mathrm{OPT}_{LP}\le\mathrm{OPT}$.

---

## 14. Exam solutions and grading checkpoints

### Solution 1

Degree-greedy:

$$
c\;\rightarrow\; b\;\rightarrow\;d,
$$

producing $\{b,c,d\}$, of size $3$.

Matching-based:

$$
(b,c)\;\rightarrow\;(d,e),
$$

producing $\{b,c,d,e\}$, of size $4$.

The cover $\{b,d\}$ has size $2$. The matching

$$
\{(a,b),(d,e)\}
$$

proves every cover needs at least two vertices. Thus $\mathrm{OPT}=2$.

Observed ratios:

$$
\frac32
\quad\text{and}\quad
2.
$$

Checkpoint: providing a size-two cover proves an upper bound; the matching supplies the lower bound needed to establish optimality.

### Solution 2

The optimal cover’s $k$ vertices cover all $r$ remaining edges. Some vertex therefore touches at least $r/k$, and greedy does at least as well.

Thus

$$
r_{t+1}\le r_t(1-1/k),
$$

and

$$
r_t\le m(1-1/k)^t\le me^{-t/k}.
$$

Choose

$$
t=\lfloor k\ln m\rfloor+1.
$$

Then $t>k\ln m$, so $r_t<1$. Since $r_t$ is an integer, $r_t=0$.

Finally,

$$
t\le k\ln m+1\le k(1+\ln m),
$$

using $k\ge1$. This is the lecture’s shrinkage proof. [Lecture 14]

### Solution 3

Counterexample:

```text
a --- b       c --- d
```

Taking only $M=\{(a,b)\}$ leaves $(c,d)$ uncovered.

The missing property is maximality.

If an edge had neither endpoint in the endpoint set of a maximal matching, that edge could be added, contradicting maximality. Therefore the endpoint set is a cover.

For the approximation:

$$
|C|=2|M|\le2\mathrm{OPT}.
$$

Checkpoint: maximality proves feasibility; matching disjointness proves the lower bound. These are separate logical roles. [Lecture 14]

### Solution 4

Feasibility follows because selected paths use only residual edges, and their pairs are removed after selection.

For the fixed optimum $O$,

$$
|O_{\text{short}}|\le(L+1)|A|,
$$

by shared-edge charging plus at most one same-pair charge per greedy path.

Also,

$$
|O_{\text{long}}|\le\frac{m}{L+1},
$$

by edge-disjointness and minimum long-path length.

If $\mathrm{OPT}>0$, the fallback ensures $a\ge1$, while selecting the larger solution ensures $a\ge|A|$. Therefore

$$
\begin{aligned}
\mathrm{OPT}
&\le(L+1)|A|+\frac{m}{L+1}\\
&\le
\left(L+1+\frac{m}{L+1}\right)a.
\end{aligned}
$$

Balance $L+1$ against $m/(L+1)$, choosing $L+1$ near $\sqrt m$. The lecture’s $L=\lfloor\sqrt m\rfloor$ gives the stated $2\sqrt m+1$ bound. [Lecture 14]

### Solution 5

First gap: not every short optimal path must intersect a greedy path.

If greedy already served that pair using a different route, the optimal route might remain edge-disjoint from all selected paths. Repair this with a same-pair charge, increasing the bound to

$$
|O_{\text{short}}|\le(L+1)|A|.
$$

Second gap: an additive bound does not immediately imply a multiplicative guarantee when $|A|=0$.

Repair this with the one-path fallback. Then positive optimum implies $a\ge1$, allowing

$$
\frac{m}{L+1}
\le
\frac{m}{L+1}a.
$$

Both repairs are required. [Lecture 14]

### Solution 6

For every edge,

$$
x_u+x_v\ge1.
$$

If both endpoints were below $1/2$, their sum would be below $1$, a contradiction. So rounding covers every edge.

For each selected vertex, $1\le2x_v$. Hence

$$
|C|
=
\sum_{v\in C}1
\le
2\sum_{v\in C}x_v
\le
2\sum_{v\in V}x_v
=
2\mathrm{OPT}_{LP}.
$$

Every integral cover has a feasible $0$-$1$ representation in the LP, so

$$
\mathrm{OPT}_{LP}\le\mathrm{OPT}.
$$

Therefore $|C|\le2\mathrm{OPT}$. This is the standard LP-rounding argument. [CLRS, Chapter 35](http://cs.bme.hu/thalg/approx.pdf)

---

## 15. Textbook reading guide

### 15.1 Kleinberg and Tardos — Algorithm Design

Jon Kleinberg and Éva Tardos, *Algorithm Design*, Chapter 11, “Approximation Algorithms.”

Most relevant sections:

- Section 11.3: “Set Cover: A General Greedy Heuristic.”
- Section 11.4: “The Pricing Method: Vertex Cover.”
- Section 11.5: “Maximization via the Pricing Method: The Disjoint Paths Problem.”
- Section 11.6: “Linear Programming and Rounding: An Application to Vertex Cover.”

[Read Chapter 11](https://nscpolteksby.ac.id/ebook/files/Ebook/Computer%20Engineering/Algorithm%20Design%20(2005)/12.%20Chapter%2011%20-%20Approximation%20Algorithms.pdf).

This is the closest overall match to the lecture, especially for the disjoint-paths analysis. The textbook presents a globally shortest available path algorithm, whereas the lecture makes the short/long split explicit using a cutoff and fallback. Keep these algorithm variants distinct when reproducing a proof. [Lecture 14; linked chapter]

### 15.2 Vazirani — Approximation Algorithms

Vijay V. Vazirani, *Approximation Algorithms*, Springer, 2001.

Relevant readings:

- Section 1.1: “Lower bounding OPT.”
- Section 1.1.1: “An approximation algorithm for cardinality vertex cover.”
- Chapter 2, especially Section 2.1: greedy Set Cover.
- Chapter 8, especially Section 8.2: an FPTAS for Knapsack.
- Chapter 12: LP duality and LP-based approximation techniques.
- Chapter 14, especially Section 14.3: half-integrality of Vertex Cover.

[Read the book](https://www.ics.uci.edu/~vazirani/book.pdf).

This is particularly useful for understanding why lower bounds on an unknown optimum are central to approximation design.

### 15.3 Cormen, Leiserson, Rivest, and Stein — Introduction to Algorithms

In the third edition of CLRS, use Chapter 35, “Approximation Algorithms”:

- Section 35.1: Vertex Cover.
- Section 35.3: Set Cover.
- Section 35.4: randomization and linear programming, including weighted Vertex Cover.
- Section 35.5: the Subset Sum approximation scheme.

[Read Chapter 35](http://cs.bme.hu/thalg/approx.pdf).

The Vertex Cover section closely parallels the matching proof. Exercise 35.1-3 asks for a graph showing that highest-degree greedy is not a 2-approximation—a useful further challenge beyond the small example in this guide. These section numbers are edition-specific.

---

## 16. Final revision checklist

Before an exam, practice explaining these points without looking at the notes:

1. Write the approximation inequality in the correct direction for minimization and maximization.
2. Separate feasibility from solution-quality analysis.
3. Derive the $r/\mathrm{OPT}$ averaging bound.
4. Explain why exponential shrinkage yields logarithmically many selections.
5. Distinguish maximal from maximum matching.
6. Explain why maximality gives a cover but disjointness gives the lower bound.
7. Reproduce

   $$
   |C|=2|M|\le2\mathrm{OPT}.
   $$

8. Explain why cutoff-only path greedy needs a fallback.
9. Justify both components of the $L+1$ charging bound.
10. Derive the long-path bound from the edge budget.
11. Explain exactly where $a\ge1$ is used.
12. Balance $L$ against $m/L$ to obtain the square root.

These are the lecture’s core proof skills: averaging, lower-bound construction, charging, counting, and balancing competing losses. [Lecture 14]

> Source note: “Lecture 14” refers to the supplied *Lec_14_Unmarked.pdf*, CS 6515: Graduate Algorithms, “Approximation Algorithms and Greedy Methods,” Sahil Singla and Gerandy Brito, Fall 2026. Textbook sources are linked inline and in Section 15. Worked examples and practice problems expand on the lecture for study purposes.

## 17. Video Lectures
Start with **MIT’s Lecture 17**, then watch Tim Roughgarden’s Lecture 17 for a deeper treatment of the proofs and their connection to linear programming. These are the closest matches to your current material on Vertex Cover, greedy Set Cover, and approximation guarantees. [ocw.mit](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/a4a7f356ba3e65a00ad2bdcfed6e0f35_MIT6_046JS15_lec17.pdf)

### 1. MIT 6.046J — “17. Complexity: Approximation Algorithms”
Instructor: Srinivas Devadas  
[Watch on YouTube](https://www.youtube.com/watch?v=MEz1J9wY2iM)

The best starting point for reviewing your lecture. It covers approximation definitions, the matching-based 2-approximation for Vertex Cover, greedy Set Cover, and Partition. The Vertex Cover algorithm is the same “pick an uncovered edge and take both endpoints” approach from your notes. [ocw.mit](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/a4a7f356ba3e65a00ad2bdcfed6e0f35_MIT6_046JS15_lec17.pdf)

Focus on:
- Why the selected edges provide a lower bound on the optimum.
- Why choosing both endpoints gives a factor of \(2\).
- How greedy Set Cover relates to choosing the highest remaining degree in Vertex Cover.

### 2. Tim Roughgarden, Stanford CS261 — “Lecture 17: Linear Programming and Approximation Algorithms”
[Watch on YouTube](https://www.youtube.com/watch?v=bCsnLNZaoPQ) · Approximately 79 minutes

The strongest follow-up for your proof-based study. It covers greedy Set Cover, a dual interpretation of the greedy algorithm, LP rounding, and primal–dual approximation algorithms for Vertex Cover. [timroughgarden](https://timroughgarden.org/w16/w16.html)

Focus on:
- How to compare an algorithm with an unknown optimum.
- Why greedy Set Cover has a logarithmic approximation guarantee.
- How an LP relaxation supplies a lower bound.
- Why rounding Vertex Cover variables at \(1/2\) produces a 2-approximation.

This is especially relevant to the transition from your approximation lecture to LP rounding. [youtube](https://www.youtube.com/watch?v=bCsnLNZaoPQ)

### 3. Tim Roughgarden, Stanford CS261 — “Lecture 15: Introduction to Approximation Algorithms”
[Watch on YouTube](https://www.youtube.com/watch?v=OacQnsvauZs) · Approximately 80 minutes

Choose this for a broader introduction before diving into the LP-based analysis. It discusses approximation algorithms through scheduling, Knapsack, Steiner Tree, set coverage, and influence maximization. [timroughgarden](https://timroughgarden.org/w16/w16.html)

Focus on:
- What a worst-case approximation guarantee actually promises.
- How the algorithm and its analysis depend on the problem’s structure.
- The distinction between covering every element and maximizing coverage under a constraint.

One terminology caution: “Set Cover” and “set coverage” are different optimization problems; do not transfer a guarantee from one to the other without checking the objective and constraints. Roughgarden’s course treats them in different contexts. [timroughgarden](https://timroughgarden.org/w16/w16.html)

### 4. “Knapsack FPTAS”
[Watch on YouTube](https://www.youtube.com/watch?v=GyDTT3PxFP4)

A focused supplement for the approximation-schemes portion of your notes. The video develops a fully polynomial-time approximation scheme for Knapsack and explains how the solution can approach the optimum arbitrarily closely. [youtube](https://www.youtube.com/watch?v=GyDTT3PxFP4)

Use it to reinforce:
- The role of the accuracy parameter \(\varepsilon\).
- Why “polynomial for each fixed \(\varepsilon\)” differs from “polynomial in both input size and \(1/\varepsilon\).”
- How an approximation scheme differs from a fixed-factor algorithm.

### 5. Tim Roughgarden, Stanford CS261 — “Lecture 16: The Traveling Salesman Problem”
[Watch on YouTube](https://www.youtube.com/watch?v=muHfx-nqLFc)

An optional next step once the Vertex Cover proofs feel comfortable. The lecture covers inapproximability for general TSP, the minimum-spanning-tree heuristic for metric TSP, Christofides’s algorithm, and asymmetric TSP. [timroughgarden](https://timroughgarden.org/w16/w16.html)

Its value is seeing the same proof strategy in another setting: construct a feasible solution, identify a structural lower bound on the optimum, and relate the two. It also illustrates why assumptions such as the triangle inequality matter to an approximation guarantee. [timroughgarden](https://timroughgarden.org/w16/w16.html)

## What about edge-disjoint paths?

For an advanced extension, watch [“FSTTCS L37: Edge Disjoint Paths in Networks”](https://www.youtube.com/watch?v=qP7_WiOR_uQ). It discusses approximation through multicommodity-flow LP relaxations and routing with congestion. [youtube](https://www.youtube.com/watch?v=qP7_WiOR_uQ)

Treat this as a research-level extension, not a direct replacement for your lecture’s short-path greedy proof. Parts of the talk allow congestion—an edge may be used by more than one routed path—which changes the strict edge-disjointness requirement you have been studying. [youtube](https://www.youtube.com/watch?v=qP7_WiOR_uQ)

## Suggested viewing order

For your current lecture, I would use this sequence:

1. MIT Lecture 17 — establish the basic guarantees and matching argument.
2. Roughgarden Lecture 17 — deepen the logarithmic analysis and connect it to LP rounding.
3. Knapsack FPTAS — review PTAS versus FPTAS.
4. Roughgarden Lecture 15 — broaden your examples.
5. Roughgarden Lecture 16 — practice recognizing approximation-proof patterns in a new problem.

After each lecture, close the video and reconstruct three things from memory: the algorithm, the bound on \(\mathrm{OPT}\), and the inequality connecting the output to that bound. That exercise aligns directly with the proof skills emphasized in these lectures. [ocw.mit](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/a4a7f356ba3e65a00ad2bdcfed6e0f35_MIT6_046JS15_lec17.pdf)
