# CS 6515 Study Guide: Graph Algorithms, Matchings, and Maximum Flow

This guide explains Lectures 6–8 with worked examples, text visualizations, pseudocode, proof ideas, complexity analysis, common mistakes, quizzes, and exam-style questions.

## Roadmap

```text
Graph representation
      |
      +--> BFS --------------------> unweighted shortest paths
      |
      +--> Dijkstra ---------------> nonnegative weighted shortest paths
      |
      +--> MST cut property -------> Prim's algorithm
      |
      +--> alternating paths ------> maximum bipartite matching
                                      |
                                      v
                              residual networks
                                      |
                                      v
                              maximum flow / minimum cut
```

The central theme is that a graph algorithm is not just a construction. A complete solution normally includes:

1. a maintained invariant,
2. an operation that makes progress,
3. a proof of correctness or optimality certificate, and
4. a running-time analysis.

---

# Lecture 6: Graphs, BFS, Dijkstra, and MST Foundations

## 1. Graph representations

A graph is written as \(G=(V,E)\), where \(V\) is the vertex set and \(E\) is the edge set. Let

\[
n=|V|, \qquad m=|E|.
\]

Graphs may be directed or undirected, and weighted or unweighted.

### Adjacency matrix

An adjacency matrix is an \(n\times n\) table in which entry \((u,v)\) indicates whether an edge exists.

- Space: \(\Theta(n^2)\)
- Test whether \((u,v)\in E\): \(O(1)\)
- Scan all neighbors of \(u\): \(O(n)\)

### Adjacency list

Each vertex stores a list of its neighbors.

- Space: \(\Theta(n+m)\)
- Scan the neighbors of \(u\): \(\Theta(\deg(u))\)
- Scan the whole graph: \(\Theta(n+m)\)

For an undirected graph,

\[
\sum_{v\in V}\deg(v)=2m,
\]

because every edge contributes one to the degree of each endpoint.

### Example

```text
A -- B -- D
|    |
C -- E
```

Adjacency lists:

```text
A: B, C
B: A, D, E
C: A, E
D: B
E: B, C
```

For a sparse graph, an adjacency matrix wastes space on nonedges, so adjacency lists are usually preferred.

---

## 2. Breadth-first search

### Problem

Given an unweighted graph and source \(s\), find the minimum number of edges from \(s\) to every reachable vertex.

### Main idea

BFS explores vertices in layers:

```text
L0: distance 0 from s
L1: distance 1 from s
L2: distance 2 from s
...
```

A FIFO queue guarantees that vertices are processed in nondecreasing distance order.

### Visualization

```text
             d
             |
s ---- a ---- c
 \     |      |
  \----b------e
```

Starting from \(s\):

```text
L0 = {s}
L1 = {a, b}
L2 = {c, e}
L3 = {d}
```

One possible BFS parent tree is:

```text
s
├── a
│   └── c
│       └── d
└── b
    └── e
```

The original graph may contain extra edges. They do not invalidate the tree distances because BFS records a vertex when it is first reached from the earliest possible layer.

### Pseudocode

```text
BFS(G, s):
    for each vertex v in V:
        dist[v] = infinity
        parent[v] = NIL

    dist[s] = 0
    Q = empty FIFO queue
    enqueue(Q, s)

    while Q is not empty:
        u = dequeue(Q)

        for each v in Adj[u]:
            if dist[v] == infinity:
                dist[v] = dist[u] + 1
                parent[v] = u
                enqueue(Q, v)

    return dist, parent
```

### Why BFS is correct

When BFS first discovers \(v\) from \(u\), it constructs a path of length

\[
\operatorname{dist}[u]+1.
\]

If a shorter path to \(v\) existed, then the predecessor of \(v\) on that path would be in an earlier layer and would have discovered \(v\) first. This contradicts the assumption that the current discovery is not shortest.

### Running time

- Every vertex enters and leaves the queue at most once.
- Every adjacency-list entry is scanned once.

Therefore:

\[
T(n,m)=O(n+m).
\]

### Recovering a shortest path

Follow parent pointers backward from the destination to the source and reverse the sequence.

```text
RECONSTRUCT-PATH(parent, s, t):
    path = empty list
    current = t

    while current != NIL:
        prepend current to path
        if current == s:
            return path
        current = parent[current]

    return "unreachable"
```

### Common mistake

BFS gives shortest paths only when all edges have the same effective length. It does not solve a general weighted shortest-path problem.

---

## 3. Weighted shortest paths and pseudo-polynomial expansion

Suppose every edge has a positive integer weight. An edge of weight \(w\) could be replaced by a chain of \(w\) unit edges.

```text
u --(3)--> v

becomes

u --1--> x --1--> y --1--> v
```

BFS on the expanded graph finds the correct weighted distance. However, the graph size depends on the numerical value of \(w\), not on the number of bits needed to encode \(w\).

For example, the number \(2^{100}\) requires only 101 binary digits but would require roughly \(2^{100}\) unit edges. Thus this method is pseudo-polynomial, not polynomial in the input length.

---

## 4. Dijkstra's algorithm

### Problem

Find shortest paths from a source in a weighted graph where every edge weight is nonnegative.

### Main idea

Maintain a tentative distance \(d[v]\). Repeatedly settle the unsettled vertex with the smallest tentative distance, then relax its outgoing edges.

Relaxation checks whether going through \(u\) improves \(v\):

\[
\text{if } d[u]+w(u,v)<d[v],
\]

then set

\[
d[v]\leftarrow d[u]+w(u,v).
\]

### Worked example

```text
       4
   s ------> a
   |         |
  1|         |1
   v    2    v
   b ------> c
   |         ^
  5|         |1
   v         |
   d --------+
```

Start:

```text
d[s]=0, d[a]=d[b]=d[c]=d[d]=infinity
```

Settle \(s\):

```text
d[a]=4
d[b]=1
```

Settle \(b\), since it has the minimum key:

```text
d[c]=3
d[d]=6
```

Settle \(c\): no improvement is needed.

Settle \(a\): its path to \(c\) has cost \(5\), so \(d[c]=3\) remains.

Final distances:

```text
s: 0
b: 1
c: 3
a: 4
d: 6
```

### Pseudocode

```text
DIJKSTRA(G, w, s):
    for each vertex v in V:
        d[v] = infinity
        parent[v] = NIL

    d[s] = 0
    PQ = min-priority queue containing all vertices, keyed by d

    while PQ is not empty:
        u = EXTRACT-MIN(PQ)

        for each outgoing edge (u, v):
            if v is still in PQ and d[u] + w(u, v) < d[v]:
                d[v] = d[u] + w(u, v)
                parent[v] = u
                DECREASE-KEY(PQ, v, d[v])

    return d, parent
```

### Correctness idea

When \(u\) is extracted, suppose it is the first vertex settled incorrectly. Consider a true shortest path from \(s\) to \(u\), and let \((x,y)\) be the first edge that leaves the settled set.

- \(x\) was settled correctly.
- Relaxing \((x,y)\) made \(d[y]\) no greater than the shortest-path prefix to \(y\).
- Because weights are nonnegative, this prefix cannot be longer than the complete shortest path to \(u\).
- Since \(u\) has minimum tentative distance, \(d[u]\le d[y]\).

The tentative value is also the length of a real path, so it cannot be below the true optimum. Therefore \(d[u]\) is correct.

### Where nonnegativity is essential

A later path cannot become cheaper by adding a negative edge. With a negative edge, a settled distance can later need revision.

#### Counterexample

```text
s --1--> a
s --2--> b
b --(-3)--> a
```

Dijkstra settles \(a\) with distance 1 before \(b\). But the true shortest path is

\[
s\to b\to a
\]

with cost \(2-3=-1\).

### Complexity

Using adjacency lists and a binary heap:

\[
O((n+m)\log n).
\]

Using a Fibonacci heap gives the theoretical bound

\[
O(m+n\log n).
\]

---

## 5. Minimum spanning trees and the cut property

### MST objective

For a connected undirected weighted graph, find a spanning tree \(T\) minimizing

\[
w(T)=\sum_{e\in T}w(e).
\]

A spanning tree has exactly \(n-1\) edges.

### MST versus shortest-path tree

- A shortest-path tree minimizes the route from one source to each vertex.
- An MST minimizes the total weight of the selected edges.

Neither objective generally implies the other.

### Cut

For a nonempty proper subset \(S\subset V\), the cut \((S,V\setminus S)\) consists of edges with one endpoint inside \(S\) and the other outside.

```text
      S                 V - S
  {a, b, c} | {d, e, f}
             ^
          cut boundary
```

A light edge is a minimum-weight edge crossing a cut.

### Cut property

For any cut, a light crossing edge belongs to some MST. If it is uniquely light, it belongs to every MST.

### Exchange argument

Let \(e\) be a light crossing edge and let \(T\) be an MST that omits it.

1. Add \(e\) to \(T\). This creates exactly one cycle.
2. The cycle must cross the cut again on some edge \(f\in T\).
3. Since \(e\) is light, \(w(e)\le w(f)\).
4. Replace \(f\) by \(e\).

Then

\[
T'=T\cup\{e\}\setminus\{f\}
\]

is a spanning tree and

\[
w(T')=w(T)+w(e)-w(f)\le w(T).
\]

Because \(T\) was already optimal, \(T'\) is also an MST.

---

# Lecture 7: Prim's Algorithm and Matchings

## 6. Prim's algorithm

### Main idea

Grow one connected tree. At every step, choose the cheapest edge crossing from the visited set \(S\) to the unvisited vertices.

### Example

```text
       2       3
   A-------B-------C
   |       |       |
  6|      1|      5|
   |       |       |
   D-------E-------F
       4       2
```

Start at \(A\):

1. \(S=\{A\}\). Choose \((A,B)\) of weight 2.
2. \(S=\{A,B\}\). Choose \((B,E)\) of weight 1.
3. \(S=\{A,B,E\}\). Choose \((E,F)\) of weight 2.
4. Next choose \((B,C)\) of weight 3.
5. Finally choose \((E,D)\) of weight 4.

Total weight:

\[
2+1+2+3+4=12.
\]

### Pseudocode

```text
PRIM(G, w, r):
    for each vertex v in V:
        key[v] = infinity
        parent[v] = NIL

    key[r] = 0
    PQ = min-priority queue containing all vertices, keyed by key
    T = empty set

    while PQ is not empty:
        u = EXTRACT-MIN(PQ)

        if parent[u] != NIL:
            add (parent[u], u) to T

        for each edge (u, v) incident to u:
            if v is still in PQ and w(u, v) < key[v]:
                key[v] = w(u, v)
                parent[v] = u
                DECREASE-KEY(PQ, v, key[v])

    return T
```

### Correctness invariant

After every iteration, some MST contains all edges selected by Prim so far.

The next edge is light across the cut between visited and unvisited vertices. The exchange argument replaces an appropriate MST edge if necessary, while retaining all prior Prim choices.

### Prim versus Dijkstra

The implementations look similar, but their keys have different meanings:

- Dijkstra: \(d[v]\) is the length of the best known entire path from the source.
- Prim: \(key[v]\) is the cheapest single edge connecting \(v\) to the current tree.

When scanning \((u,v)\):

```text
Dijkstra candidate = d[u] + w(u,v)
Prim candidate     = w(u,v)
```

Prim can work with negative edge weights. Dijkstra cannot.

### Complexity

With adjacency lists and a binary heap:

\[
O((n+m)\log n)=O(m\log n)
\]

for a connected graph.

---

## 7. Matchings

A matching \(M\subseteq E\) is a set of edges that do not share endpoints.

### Maximal versus maximum

- Maximal: no additional edge can be added directly.
- Maximum: has the largest possible number of edges.

Every maximum matching is maximal, but a maximal matching may not be maximum.

### Example

```text
v1 -- v2 -- v3 -- v4
```

If the matching is \(M=\{(v2,v3)\}\), it is maximal: neither remaining edge can be added without conflict. But \(\{(v1,v2),(v3,v4)\}\) has size 2, so the original matching is not maximum.

---

## 8. Augmenting paths

An augmenting path relative to \(M\):

- is simple,
- begins and ends at unmatched vertices,
- alternates between unmatched and matched edges.

### Visualization

```text
unmatched   matched   unmatched   matched   unmatched
   - - -      ===       - - -       ===       - - -
 v1 ----- v2 ===== v3 ----- v4 ===== v5 ----- v6
```

Flipping the membership of every path edge gives:

```text
 v1 ===== v2 ----- v3 ===== v4 ----- v5 ===== v6
```

The new matching has one more edge because the path contains one more unmatched edge than matched edge.

Formally, augment using the symmetric difference:

\[
M' = M\triangle E(P).
\]

### Why flipping preserves a matching

- Every internal vertex loses one matched edge and gains one.
- Each endpoint was unmatched and gains one matched edge.
- Vertices outside the path are unchanged.

Thus feasibility is preserved and \(|M'|=|M|+1\).

---

## 9. Berge's theorem

A matching \(M\) is maximum if and only if there is no augmenting path relative to \(M\).

### Easy direction

If an augmenting path exists, flipping it makes a larger matching. Therefore \(M\) was not maximum.

### Converse through symmetric difference

Suppose \(M^*\) is larger than \(M\). Consider

\[
M\triangle M^*.
\]

Every vertex has degree at most 2 in this subgraph, so each component is an alternating path or alternating cycle.

- An alternating cycle has equal numbers of edges from both matchings.
- An even alternating path also has equal numbers.
- Since \(|M^*|>|M|\), some component must contain one more edge from \(M^*\).

That component begins and ends with edges from \(M^*\), so its endpoints are unmatched by \(M\). It is an augmenting path for \(M\).

---

## 10. Bipartite matching by graph search

For a bipartite graph \(V=A\cup B\):

- orient unmatched edges from \(A\) to \(B\),
- orient matched edges from \(B\) to \(A\),
- begin search from every unmatched vertex in \(A\),
- stop when an unmatched vertex in \(B\) is reached.

### Example

Current matching:

\[
M=\{(a_2,b_1),(a_3,b_2)\}.
\]

Directed alternating path:

```text
a1 -> b1 -> a2 -> b2 -> a3 -> b3
```

Flipping gives:

\[
M'=\{(a_1,b_1),(a_2,b_2),(a_3,b_3)\}.
\]

### Pseudocode

```text
MAX-BIPARTITE-MATCHING(G = (A union B, E)):
    M = empty matching

    while true:
        orient each unmatched edge from A to B
        orient each matched edge from B to A
        connect super-source s to every unmatched vertex in A

        use BFS or DFS to find a path from s
        to an unmatched vertex in B

        if no such path exists:
            return M

        remove s from the recovered path
        M = M symmetric-difference edges(path)
```

### Complexity of the simple method

Each search takes \(O(n+m)\). Each augmentation raises the matching size by one, and there are at most \(n/2\) augmentations. Thus:

\[
O(n(n+m)).
\]

Odd cycles make the corresponding search harder in general, nonbipartite graphs. Edmonds' blossom algorithm handles that case.

---

# Lecture 8: Maximum Flow and Minimum Cut

## 11. Flow networks

A flow network is a directed graph with:

- capacity \(c_e\ge 0\) on each edge,
- source \(s\),
- sink \(t\).

A feasible flow \(f\) satisfies:

### Capacity constraint

\[
0\le f_e\le c_e.
\]

### Flow conservation

For every \(v\notin\{s,t\}\):

\[
\sum_{(u,v)\in E}f_{uv}
=
\sum_{(v,w)\in E}f_{vw}.
\]

The flow value is net flow leaving the source:

\[
|f|=
\sum_{(s,v)\in E}f_{sv}
-
\sum_{(v,s)\in E}f_{vs}.
\]

### Example

```text
         2/3
     s --------> a
     |            |
  1/2|            |2/2
     v    1/1     v
     b ---------> t
      \---------->
          0/1
```

Labels are flow/capacity. A validity check must verify every capacity and conservation at each internal vertex.

---

## 12. Bipartite matching as maximum flow

Given bipartition \(A,B\):

1. Add source \(s\) and edge \((s,a)\) of capacity 1 for every \(a\in A\).
2. Direct every original edge from \(A\) to \(B\) with capacity 1.
3. Add edge \((b,t)\) of capacity 1 for every \(b\in B\).

```text
          capacity 1        capacity 1
s --> vertices in A --> vertices in B --> t
```

An integral unit of flow through \(a\to b\) selects matched edge \((a,b)\). Capacity 1 ensures that no vertex is used twice.

---

## 13. Residual graphs

A residual graph records how the current flow can be changed.

For original edge \((u,v)\) with capacity \(c_{uv}\) and flow \(f_{uv}\):

- forward residual capacity:

\[
c_f(u,v)=c_{uv}-f_{uv},
\]

- reverse residual capacity:

\[
c_f(v,u)=f_{uv}.
\]

### Example

If an edge has flow/capacity \(2/5\):

```text
Original: u --2/5--> v

Residual:
u --3--> v
u <--2-- v
```

The reverse edge does not represent a new original route. It represents permission to cancel up to two units of previously sent flow.

### Why reverse edges matter

Suppose an early route uses a middle edge that blocks two better routes. A reverse residual edge lets the algorithm undo that choice and reroute flow.

This is the flow version of flipping an alternating matching path.

---

## 14. Augmenting flow

An \(s\)-to-\(t\) path in the residual graph is an augmenting path.

Its bottleneck is

\[
\Delta = \min_{e\in P} c_f(e).
\]

Augment by \(\Delta\):

- add \(\Delta\) to original edges traversed forward,
- subtract \(\Delta\) from original edges traversed backward.

### Why feasibility remains valid

- The bottleneck prevents exceeding a forward capacity.
- Reverse capacity prevents reducing an original flow below zero.
- At every internal path vertex, one residual edge enters and one leaves, so conservation remains true.
- Flow value increases by \(\Delta\).

---

## 15. Ford-Fulkerson method

```text
FORD-FULKERSON(G, c, s, t):
    set f[e] = 0 for every edge e

    while residual graph G_f contains an s-to-t path P:
        Delta = minimum residual capacity on P

        for each residual edge e on P:
            if e corresponds to a forward original edge:
                increase its original flow by Delta
            else:
                decrease the linked original flow by Delta

    return f
```

For integer capacities, every augmentation raises flow value by at least 1. If the maximum flow value is \(|f^*|\), a basic running-time bound is

\[
O((n+m)(1+|f^*|)).
\]

This is pseudo-polynomial because \(|f^*|\) can be exponentially larger than the number of bits used to encode capacities.

### Edmonds-Karp variant

Always choose an augmenting path with the fewest residual edges, using BFS. Capacities are not treated as edge lengths. The criterion is merely the number of residual edges.

This produces a polynomial-time algorithm independent of the magnitude of the capacities.

---

## 16. Minimum \(s\)-\(t\) cut

An \(s\)-\(t\) cut is a partition \((X,V\setminus X)\) such that

\[
s\in X, \qquad t\notin X.
\]

The cut capacity counts only original directed edges leaving \(X\):

\[
c(X,V\setminus X)
=
\sum_{u\in X,\,v\notin X}c_{uv}.
\]

Incoming capacities are not counted.

### Flow-cut upper bound

For every feasible flow and every \(s\)-\(t\) cut,

\[
|f|\le c(X,V\setminus X).
\]

Reason: summing conservation equations over vertices in \(X\setminus\{s\}\) cancels internal flows. Net flow crossing the cut equals the flow value, and outgoing flow cannot exceed outgoing capacity.

---

## 17. Max-flow min-cut theorem

The maximum flow value equals the minimum cut capacity.

### Certificate produced when augmentation stops

When no augmenting path exists, let \(X\) be the vertices reachable from \(s\) in the final residual graph.

Then:

- \(s\in X\),
- \(t\notin X\),
- every original edge leaving \(X\) is saturated,
- every original edge entering \(X\) carries zero flow.

Therefore:

\[
|f|=c(X,V\setminus X).
\]

Since every flow is at most every cut capacity, equality proves simultaneously that:

- \(f\) is a maximum flow,
- \((X,V\setminus X)\) is a minimum cut.

### Checkable certificate

To convince someone that a proposed flow is maximum, provide:

1. the flow on every edge,
2. evidence that capacities and conservation hold,
3. a cut \(X\) containing \(s\) but not \(t\),
4. the equality \(|f|=c(X,V\setminus X)\).

The verifier does not need to rerun the algorithm.

---

# 18. Unified comparison

| Algorithm | Goal | Main state/key | Progress step | Correctness tool | Can revise earlier choices? |
|---|---|---|---|---|---|
| BFS | Fewest-edge paths | Distance layer | Discover next layer | Layer invariant | No need |
| Dijkstra | Nonnegative shortest paths | Best tentative path length | Settle minimum key | First-crossing argument | Tentative values yes, settled values no |
| Prim | Minimum-weight spanning tree | Cheapest connecting edge | Add light cut edge | Exchange argument | Choice is irrevocable |
| Bipartite matching | Maximum matching | Current matching | Flip augmenting path | Berge's theorem | Yes |
| Maximum flow | Maximum routed quantity | Current flow and residual graph | Augment residual path | Max-flow min-cut | Yes |

## Dijkstra and Prim: the most important distinction

```text
Dijkstra asks:
What is the cheapest complete route from the source to v?

Prim asks:
What is the cheapest single edge that attaches v to the current tree?
```

## Matching and flow: the most important connection

```text
Matching flip:
unmatched, matched, unmatched, ...

Flow augmentation:
forward residual, reverse residual, forward residual, ...
```

Both mechanisms allow the algorithm to undo an earlier local decision.

---

# 19. Common exam traps

1. **Using BFS on arbitrary weighted graphs.** BFS minimizes edge count, not total weight.
2. **Using Dijkstra with a negative edge.** A settled vertex may later need a better distance.
3. **Confusing an MST with a shortest-path tree.** Their objectives differ.
4. **Claiming every light cut edge belongs to every MST.** This is true only when it is uniquely light.
5. **Proving Prim using each cut independently.** The proof must preserve compatibility with all previously chosen edges.
6. **Confusing maximal and maximum matching.** Maximal only means locally unextendable.
7. **Forgetting that augmenting path endpoints are unmatched.** Alternation alone is insufficient.
8. **Treating reverse residual edges as original edges.** They represent cancellation.
9. **Adding capacities of both directions in a directed cut.** Only edges leaving the source side count.
10. **Saying Ford-Fulkerson is always polynomial.** Its simple integer-capacity analysis depends on the numerical maximum-flow value.
11. **Running BFS in Edmonds-Karp using capacities as distances.** BFS counts residual edges.
12. **Providing an answer without a correctness argument or complexity analysis.** Graduate algorithms questions usually require all three.

---

# 20. Short quiz

## Multiple choice

### Q1
Which representation is usually best for scanning all edges of a sparse graph?

A. Adjacency matrix  
B. Adjacency lists  
C. An \(n\times n\) distance table  
D. A binary search tree containing all vertex pairs

### Q2
BFS computes shortest paths when:

A. weights are all nonnegative  
B. the graph is acyclic  
C. every edge has the same unit length  
D. the graph is undirected

### Q3
Which algorithm becomes invalid in the presence of a negative edge?

A. Prim  
B. BFS on an unweighted graph  
C. Dijkstra  
D. Ford-Fulkerson with integer capacities

### Q4
A light edge of an arbitrary cut:

A. belongs to every MST  
B. belongs to some MST  
C. is always the globally cheapest edge  
D. must be selected by every run of Prim

### Q5
Which statement is true?

A. Every maximal matching is maximum.  
B. Every maximum matching is maximal.  
C. A maximum matching has exactly \(n/2\) edges.  
D. A maximal matching has an augmenting path.

### Q6
The reverse residual capacity of original edge \((u,v)\) equals:

A. \(c_{uv}\)  
B. \(c_{uv}-f_{uv}\)  
C. \(f_{uv}\)  
D. \(-f_{uv}\)

### Q7
In Edmonds-Karp, BFS finds a path minimizing:

A. total capacity  
B. bottleneck capacity  
C. number of residual edges  
D. original edge weight

### Q8
A cut capacity in a directed flow network counts:

A. all edges crossing in either direction  
B. only edges entering \(X\)  
C. only edges leaving \(X\)  
D. only saturated edges

## True or false

1. A non-tree edge discovered during BFS can invalidate a previously assigned BFS distance.
2. Dijkstra may safely settle a vertex if every edge weight is nonnegative.
3. Prim and Dijkstra use priority queues with semantically identical keys.
4. An augmenting path increases matching size by exactly one.
5. A reverse residual edge allows cancellation of existing flow.
6. If a feasible flow has the same value as some cut capacity, it is maximum.

## Short answer

1. Why is the unit-edge expansion for integer weighted shortest paths pseudo-polynomial?
2. State the invariant used to prove Prim's algorithm.
3. Give a four-vertex example of a maximal matching that is not maximum.
4. Why does flipping an augmenting path preserve the matching property?
5. What must be true of edges leaving the reachable set in a final residual graph?
6. Explain the connection between alternating matched edges and reverse residual edges.

---

# 21. Quiz answer key

## Multiple choice

1. **B**. Scanning all adjacency lists takes \(\Theta(n+m)\).
2. **C**. BFS minimizes the number of edges.
3. **C**. Dijkstra relies on nonnegative weights.
4. **B**. A light edge belongs to some MST; uniqueness is needed for every MST.
5. **B**. Maximum implies maximal, but not conversely.
6. **C**. Reverse capacity is the amount that can be canceled.
7. **C**. BFS chooses the path with the fewest residual edges.
8. **C**. Only capacity directed out of the source side is counted.

## True or false

1. **False**. First discovery already gives the minimum layer.
2. **True**.
3. **False**. Dijkstra stores complete path length; Prim stores one connecting-edge weight.
4. **True**.
5. **True**.
6. **True**. Every flow is bounded by every cut, so equality certifies optimality.

---

# 22. Exam-style questions

## Question 1: BFS execution and proof, 12 points

Consider the undirected graph with adjacency lists:

```text
s: a, b
a: s, c, d
b: s, d
c: a, e
d: a, b, e
e: c, d
```

Assume neighbors are scanned alphabetically.

1. Run BFS from \(s\). Show the queue after each dequeue.
2. Give \(dist\) and \(parent\) for every vertex.
3. Recover one shortest path from \(s\) to \(e\).
4. Explain why edge \((d,e)\), if not selected as a tree edge, does not invalidate the distance to \(e\).
5. State the running time using adjacency lists.

### Solution sketch

Layers are \(L_0=\{s\}\), \(L_1=\{a,b\}\), \(L_2=\{c,d\}\), and \(L_3=\{e\}\). Depending on discovery order, \(e\)'s parent is \(c\) or \(d\). The distance remains 3 because no vertex in an earlier layer has an edge to \(e\).

---

## Question 2: Dijkstra counterexample, 10 points

Construct the smallest directed graph you can in which Dijkstra settles an incorrect distance because of a negative edge. Show the extraction order and identify exactly where the correctness proof fails.

### Solution sketch

Use edges \(s\to a\) of weight 1, \(s\to b\) of weight 2, and \(b\to a\) of weight \(-3\). Dijkstra settles \(a\) at 1 before \(b\), although the true distance is \(-1\). The proof fails when it claims that a shortest-path prefix cannot exceed the full path length.

---

## Question 3: Prim trace, 15 points

For the graph below, run Prim from \(A\). Break ties alphabetically by endpoint.

```text
(A,B,2), (A,C,3), (B,C,1), (B,D,4),
(C,D,2), (C,E,5), (D,E,1)
```

For each iteration, report:

1. visited set \(S\),
2. extracted vertex,
3. selected tree edge,
4. key and parent of every unvisited vertex.

Then give the total MST weight and state the invariant used in the proof.

### Solution sketch

One selection order is \((A,B),(B,C),(C,D),(D,E)\), with total cost \(2+1+2+1=6\). The invariant is that some MST contains every edge selected so far.

---

## Question 4: MST cut reasoning, 12 points

Prove or disprove each statement.

1. Every light edge of every cut belongs to every MST.
2. Every unique light edge of a cut belongs to every MST.
3. An MST is always a shortest-path tree from every root.
4. Prim remains correct with negative edge weights.

### Solution sketch

1. False because ties may allow alternative MSTs.
2. True by the strict version of the exchange argument.
3. False because total tree weight and root-to-vertex distances are different objectives.
4. True. The cut exchange proof compares weights but does not require nonnegativity.

---

## Question 5: Augmenting-path matching, 15 points

Let

\[
A=\{a_1,a_2,a_3,a_4\},\qquad
B=\{b_1,b_2,b_3,b_4\},
\]

and let the edges be

\[
\{(a_1,b_1),(a_1,b_2),(a_2,b_1),(a_2,b_3),
(a_3,b_2),(a_3,b_4),(a_4,b_3)\}.
\]

Current matching:

\[
M=\{(a_1,b_1),(a_3,b_2),(a_4,b_3)\}.
\]

1. Orient matched and unmatched edges for augmenting-path search.
2. Find an augmenting path beginning at \(a_2\).
3. Flip it and write the new matching.
4. Explain why its cardinality rises by exactly one.

### Solution sketch

One augmenting path is

\[
a_2,b_1,a_1,b_2,a_3,b_4.
\]

After flipping:

\[
M'=\{(a_2,b_1),(a_1,b_2),(a_3,b_4),(a_4,b_3)\}.
\]

---

## Question 6: Berge's theorem proof, 15 points

Prove the difficult direction of Berge's theorem: if \(M\) is not maximum, then an augmenting path exists relative to \(M\).

Your proof must explain:

1. why components of \(M\triangle M^*\) are paths or cycles,
2. why edges alternate,
3. why some component favors \(M^*\),
4. why that component is an augmenting path for \(M\).

---

## Question 7: Residual graph update, 15 points

A network contains the path

```text
s --4--> a --3--> b --5--> t
```

and the current flows are respectively 2, 1, and 1.

1. List forward and reverse residual capacities for every edge.
2. Find the bottleneck of this path in the residual graph.
3. Augment along the forward path and list the new flows.
4. Explain why conservation remains valid at \(a\) and \(b\).

### Solution sketch

Forward residual capacities are 2, 2, and 4; reverse capacities are 2, 1, and 1. The bottleneck is 2. Augmentation gives flows 4, 3, and 3, assuming these are the only path contributions relevant to the stated local update.

---

## Question 8: Reverse-edge rerouting, 15 points

Design a unit-capacity network where an initial augmenting path creates a flow of value 1, and a second augmentation must use a reverse residual edge to reach value 2.

1. Draw the original network.
2. Show the first flow.
3. Draw the residual graph.
4. Identify the reverse edge used by the second augmenting path.
5. Show the final flow.

### Grading focus

A full-credit answer must clearly distinguish original edges from residual reverse edges and show which original flow is canceled.

---

## Question 9: Max-flow min-cut certificate, 18 points

A student claims that a flow of value 11 is maximum. They provide a cut \((X,V\setminus X)\) whose outgoing edge capacities are 4, 2, and 5.

1. Is this enough to prove optimality if the proposed flow is feasible?
2. What additional feasibility checks must be performed?
3. What can be concluded about the cut?
4. Explain the result using weak duality.

### Solution sketch

The cut capacity is \(4+2+5=11\). Once flow feasibility is verified, the flow reaches the upper bound supplied by the cut. Therefore the flow is maximum and the cut is minimum.

---

## Question 10: Integrated comparison, 18 points

For each of Dijkstra, Prim, bipartite matching by augmenting paths, and maximum flow:

1. identify the maintained state,
2. state the progress operation,
3. state the correctness argument or optimality certificate,
4. give the running time discussed in the lectures,
5. say whether an earlier choice can be revised.

A strong answer should explicitly compare Dijkstra's path-length key with Prim's one-edge key, and compare matching flips with reverse residual edges.

---

# 23. Additional oral-exam prompts

1. Why does the cut property prove the existence of an MST containing a chosen edge rather than immediately proving that all individually safe edges are mutually compatible?
2. Explain pseudo-polynomial time without using the phrase “the number is large.”
3. Why is a failed search useful in both matching and flow?
4. How does the final residual reachable set turn algorithm failure into an optimality certificate?
5. In what sense is max-flow min-cut an example of weak duality becoming equality?
6. Why can Prim make irrevocable choices, while matching and flow sometimes need to undo earlier choices?
7. If a maximum-flow implementation stores original edges in both directions, how should residual edges be labeled to avoid ambiguous updates?
8. Why does integrality matter in the reduction from bipartite matching to flow?

---

# 24. Revision checklist

Before an exam, make sure you can do all of the following without notes:

- derive \(O(n+m)\) for BFS from adjacency-list scans;
- state exactly why Dijkstra requires nonnegative weights;
- distinguish numerical value from bit-length input size;
- reproduce the MST cut exchange proof;
- state Prim's compatibility invariant;
- explain maximal versus maximum matching using a counterexample;
- flip an augmenting path using symmetric difference;
- prove Berge's theorem using components of \(M\triangle M^*\);
- construct a bipartite matching flow network;
- compute forward and reverse residual capacities;
- augment along a path containing a reverse edge;
- calculate a directed cut capacity correctly;
- prove \(|f|\le c(X,V\setminus X)\);
- derive a minimum cut from final residual reachability;
- provide solution, correctness proof, and running-time analysis together.
