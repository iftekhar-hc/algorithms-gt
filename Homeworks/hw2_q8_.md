# Walking on the Plane: Earliest Disk Connectivity Problem

## 1. Problem Formulation and Mathematical Foundation

### 1.1 Geometric Model
Let $P = \{p_1, p_2, \dots, p_n\} \subset \mathbb{R}^2$ be a set of $n$ points in the Euclidean plane. At time $t \ge 0$, each point $p_i$ is the center of a closed Euclidean disk:
$$D(p_i, t) = \{ x \in \mathbb{R}^2 : \|x - p_i\| \le t \}$$

The union of these expanding disks at time $t$ is denoted by:
$$U(t) = \bigcup_{i=1}^n D(p_i, t)$$

Two designated vertices $u, v \in P$ are connected at time $t$ if and only if they lie within the same connected component of $U(t)$.

### 1.2 Equivalence to Bottleneck Shortest Path
Two disks $D(p_i, t)$ and $D(p_j, t)$ intersect if and only if the Euclidean distance between their centers satisfies:
$$\|p_i - p_j\| \le 2t$$

Because each disk is convex and thus path-connected, a continuous path exists from $u$ to $v$ in $U(t)$ if and only if there exists a sequence of points in $P$:
$$u = x_0, x_1, x_2, \dots, x_k = v$$
such that every consecutive pair satisfies $\|x_{m-1} - x_m\| \le 2t$.

Consequently, the earliest connection time $t^*$ is governed by the minimax edge length:
$$t^* = \frac{1}{2} \min_{\pi \in \Pi(u, v)} \max_{e \in \pi} w(e)$$
where $\Pi(u, v)$ denotes the set of all simple paths between $u$ and $v$ in the complete geometric graph $K_n = (P, E)$ with edge weights $w(p_i, p_j) = \|p_i - p_j\|$.

---

## 2. Question 1: Modified Dijkstra's Algorithm in $O(n^2 \log n)$ Time

### 2.1 Algorithm Overview
In standard Dijkstra's algorithm, the objective is to minimize an additive path cost $\sum w(e)$. For the earliest connectivity problem, the cost metric is replaced by the bottleneck capacity operator:
$$\text{cost}(\pi) = \max_{e \in \pi} w(e)$$

We define $b[x]$ as the minimum bottleneck value from source $u$ to vertex $x$. The relaxation step is modified from addition to the maximum operation:
$$b[w] \leftarrow \min\Big(b[w],\, \max(b[x], \|x - w\|)\Big)$$

### 2.2 Pseudocode

```text
Algorithm Modified-Dijkstra(P, u, v):
    Input:
        P: Array of n 2D points [p_1, p_2, ..., p_n]
        u: Source vertex index
        v: Target vertex index
    Output:
        Earliest time t* at which u and v become connected

    1. Initialize an array b of size n:
           for each vertex i in P:
               b[i] = +infinity
       b[u] = 0

    2. Initialize a min-priority queue Q
       Insert (u, 0) into Q

    3. Initialize a boolean visited array:
           visited[i] = False for all i

    4. while Q is not empty:
           Extract (x, dist) with minimum dist from Q
           
           if visited[x]:
               continue
           visited[x] = True

           if x == v:
               return b[v] / 2.0

           for each vertex w in P such that w != x:
               if not visited[w]:
                   edge_weight = EuclideanDistance(P[x], P[w])
                   new_bottleneck = max(b[x], edge_weight)
                   
                   if new_bottleneck < b[w]:
                       b[w] = new_bottleneck
                       Insert or Decrease-Key (w, new_bottleneck) in Q

    5. return b[v] / 2.0
```

### 2.3 Correctness Proof
The modified algorithm is correct due to the greedy choice property and optimal substructure of minimax paths:

1. **Optimal Substructure**: Let $\pi$ be a minimax path from $u$ to $x$. Any subpath of $\pi$ from $u$ to an intermediate node $y$ is also a minimax path from $u$ to $y$.
2. **Loop Invariant**: When vertex $x$ is extracted from the priority queue, $b[x]$ equals the exact minimum bottleneck distance $b^*(x)$ from $u$ to $x$.
   - *Proof by contradiction*: Suppose $x$ is the first vertex extracted with $b[x] > b^*(x)$.
   - Consider the optimal minimax path $P^*$ from $u$ to $x$. Let $(y, z)$ be the first edge along $P^*$ where $y$ has already been settled ($y \in S$) and $z$ has not yet been settled ($z \notin S$).
   - Because $y$ was settled earlier and correctly, $b[y] = b^*(y)$.
   - When $y$ was extracted, edge $(y, z)$ was relaxed, ensuring:
     $$b[z] \le \max(b[y], \|y - z\|) \le \text{bottleneck}(P^*) = b^*(x) < b[x]$$
   - Since $b[z] < b[x]$, the min-priority queue would have extracted $z$ prior to $x$, creating a contradiction.
   - Therefore, $b[x] = b^*(x)$ for all extracted vertices.

Dividing the minimax distance $b[v]$ by 2 yields the exact earliest time $t^*$.

### 2.4 Complexity Analysis
- **Graph Size**: The underlying graph is complete with $|V| = n$ and $|E| = \Theta(n^2)$.
- **Priority Queue Operations**:
  - $n$ `Extract-Min` operations take $O(n \log n)$ time.
  - $O(n^2)$ `Decrease-Key` (or push) operations take $O(n^2 \log n)$ time with a standard binary heap.
- **Total Running Time**: $O(n^2 \log n)$.
- *Note*: Using an array-based implementation without an explicit heap reduces the running time to $O(n^2)$.

---

## 3. Question 2: Linear-Time Solution Given a Minimum Spanning Tree

### 3.1 MST Bottleneck Property
**Theorem**: Let $T = (V, E_T)$ be any Minimum Spanning Tree of a connected, weighted graph $G = (V, E)$. For any two vertices $u, v \in V$, the unique simple path $P_T(u, v)$ in $T$ between $u$ and $v$ is a minimax bottleneck path in $G$.

**Proof**:
1. Let $e^* = (a, b)$ be an edge of maximum weight on the tree path $P_T(u, v)$, so:
   $$w(e^*) = \max_{e \in P_T(u, v)} w(e)$$
2. Removing $e^*$ divides $T$ into two disjoint connected components, inducing a cut $(S, V \setminus S)$ such that $u \in S$ and $v \in V \setminus S$.
3. Let $P$ be any arbitrary path from $u$ to $v$ in $G$. Because $u \in S$ and $v \in V \setminus S$, path $P$ must contain at least one edge $e'$ crossing the cut $(S, V \setminus S)$.
4. By the fundamental cut property of MSTs, $e^*$ is a minimum-weight edge crossing $(S, V \setminus S)$. If $w(e') < w(e^*)$, replacing $e^*$ with $e'$ would produce a spanning tree of strictly lower total weight, contradicting the optimality of $T$.
5. Therefore, $w(e') \ge w(e^*)$, which implies:
   $$\max_{e \in P} w(e) \ge w(e') \ge w(e^*)$$
6. Since this inequality holds for every path $P$ in $G$, the tree path $P_T(u, v)$ achieves the absolute minimum bottleneck edge weight.

### 3.2 Linear-Time Search Algorithm
When the MST $T$ is provided as an adjacency list:
- The tree contains $n$ vertices and $n - 1$ edges.
- A single graph traversal (Breadth-First Search or Depth-First Search) starting from $u$ identifies the unique path to $v$ while computing the maximum edge weight encountered.

### 3.3 Traversal Pseudocode

```text
Algorithm MST-Earliest-Time(T, u, v):
    Input:
        T: Adjacency list of the MST with edge weights
        u: Source vertex
        v: Target vertex
    Output:
        Earliest connection time t*

    1. Initialize visited array of size n with False
    2. Initialize max_bottleneck array of size n with 0
    3. Initialize a queue Q
    
    4. Q.enqueue(u)
       visited[u] = True
       max_bottleneck[u] = 0

    5. while Q is not empty:
           current = Q.dequeue()
           
           if current == v:
               return max_bottleneck[v] / 2.0

           for each neighbor (w, weight) of current in T:
               if not visited[w]:
                   visited[w] = True
                   max_bottleneck[w] = max(max_bottleneck[current], weight)
                   Q.enqueue(w)

    6. return max_bottleneck[v] / 2.0
```

### 3.4 Complexity
- **Time Complexity**: BFS visits each of the $n$ vertices and traverses each of the $2(n - 1)$ directed edges in the adjacency list at most once. The total time is $O(|V| + |E|) = O(n + (n - 1)) = O(n)$.
- **Space Complexity**: $O(n)$ auxiliary memory for the queue, visited array, and bottleneck tracking.

---

## 4. Worked Numerical Example

Consider four points on the Cartesian coordinate plane:
- $p_1 = (0, 0)$ (Vertex $u$)
- $p_2 = (3, 0)$
- $p_3 = (3, 4)$
- $p_4 = (0, 4)$ (Vertex $v$)

### 4.1 Pairwise Distances
- $\|p_1 - p_2\| = 3$
- $\|p_2 - p_3\| = 4$
- $\|p_3 - p_4\| = 3$
- $\|p_4 - p_1\| = 4$
- $\|p_1 - p_3\| = 5$
- $\|p_2 - p_4\| = 5$

### 4.2 Candidate Paths from $u = p_1$ to $v = p_4$
1. **Direct Path**: $p_1 \to p_4$
   - Edge length: $4$
   - Bottleneck: $4$
2. **Path via $p_2$ and $p_3$**: $p_1 \to p_2 \to p_3 \to p_4$
   - Edge lengths: $3, 4, 3$
   - Bottleneck: $\max(3, 4, 3) = 4$
3. **Diagonal Path**: $p_1 \to p_3 \to p_4$
   - Edge lengths: $5, 3$
   - Bottleneck: $\max(5, 3) = 5$

The global minimum bottleneck distance is $4$. The disks must reach radius $t^* = 4 / 2 = 2.0$.

### 4.3 Verification via MST
The Minimum Spanning Tree contains edges:
- $(p_1, p_2)$ with weight $3$
- $(p_3, p_4)$ with weight $3$
- One edge of weight $4$, e.g., $(p_1, p_4)$ or $(p_2, p_3)$

If $E_T = \{(p_1, p_2), (p_3, p_4), (p_1, p_4)\}$:
- The path between $p_1$ and $p_4$ in $T$ is the direct edge $(p_1, p_4)$ with weight $4$.
- The maximum edge weight is $4$, confirming $t^* = 4 / 2 = 2.0$.

---

## 5. Algorithmic Comparison

| Criterion | Modified Dijkstra | Given MST Traversal | Delaunay Triangulation Approach |
| :--- | :--- | :--- | :--- |
| **Input Required** | Point coordinates $P$ | Point coordinates + MST | Point coordinates $P$ |
| **Time Complexity** | $O(n^2 \log n)$ or $O(n^2)$ | $O(n)$ | $O(n \log n)$ |
| **Space Complexity** | $O(n)$ or $O(n^2)$ | $O(n)$ | $O(n)$ |
| **Graph Density** | Complete ($O(n^2)$ edges) | Tree ($n-1$ edges) | Planar ($O(n)$ edges) |
| **Optimality** | From-scratch baseline | Optimal for precomputed MST | Optimal from-scratch algorithm |
