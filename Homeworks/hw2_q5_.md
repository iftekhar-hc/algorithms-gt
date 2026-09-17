# Minimum Vertex Cover on a Tree (Campus Illumination Problem)

## 1. Problem Overview
The Georgia Tech campus consists of $n$ academic buildings and pathway edges forming a tree $T = (V, E)$. Installing a light on building $B \in V$ illuminates all edges incident to $B$. The objective is to identify a minimum-cardinality subset $S \subseteq V$ such that every edge in $E$ has at least one endpoint in $S$, running in $O(|V|)$ time.

---

## 2. Table Entry Definitions (Subproblems)

Arbitrarily select a vertex $r \in V$ to serve as the root of tree $T$. This establishes a parent-child hierarchy and defines a directed subtree $T_u$ rooted at each vertex $u \in V$.

Let $C(u)$ denote the set of children of vertex $u$. A two-dimensional table $DP[u, b]$ is defined for each vertex $u \in V$ and indicator $b \in \{0, 1\}$:

- **$DP[u, 1]$**: The minimum number of lights needed to illuminate all edges in the subtree $T_u$, given that a light is installed on building $u$.
- **$DP[u, 0]$**: The minimum number of lights needed to illuminate all edges in the subtree $T_u$, given that no light is installed on building $u$.

The optimal solution for the entire campus tree is:
$$\min(DP[r, 0], DP[r, 1])$$

---

## 3. Recurrence Relations and Correctness

For each vertex $u \in V$, the values of $DP[u, 0]$ and $DP[u, 1]$ are computed from the solutions of its children $v \in C(u)$.

### Case 1: No Light on Building $u$ ($b = 0$)
If building $u$ has no light, every incident pathway edge $(u, v)$ to each child $v \in C(u)$ must be covered by installing a light on child building $v$. Therefore, every child must be included in the light set:
$$DP[u, 0] = \sum_{v \in C(u)} DP[v, 1]$$

*Base Case:* If $u$ is a leaf node ($C(u) = \emptyset$), then $DP[u, 0] = 0$.

### Case 2: Light on Building $u$ ($b = 1$)
If building $u$ has a light installed, all incident edges $(u, v)$ to its children are illuminated. Thus, for each child $v \in C(u)$, we can independently choose whether to install a light on $v$ based on which option minimizes the cost for the subtree $T_v$:
$$DP[u, 1] = 1 + \sum_{v \in C(u)} \min(DP[v, 0], DP[v, 1])$$

*Base Case:* If $u$ is a leaf node ($C(u) = \emptyset$), then $DP[u, 1] = 1 + 0 = 1$.

### Correctness
A tree contains no cycles, meaning the subtrees $T_v$ rooted at different children $v \in C(u)$ are completely vertex-disjoint. 
- When $u \notin S$, any edge $(u, v)$ can only be covered by placing $v \in S$, strictly requiring the subproblem state $DP[v, 1]$.
- When $u \in S$, edge $(u, v)$ is already covered, leaving subtree $T_v$ free to independently adopt its optimal local configuration $\min(DP[v, 0], DP[v, 1])$.
Because optimal substructure holds across disjoint subtrees, this recurrence yields the exact global minimum.

---

## 4. Algorithm and Time Complexity

### Pseudocode
```text
Algorithm MinCampusLights(T):
    Root tree T arbitrarily at vertex r
    Compute a post-order traversal sequence of V using DFS
    
    For each vertex u in post-order:
        DP[u, 0] = 0
        DP[u, 1] = 1
        For each child v of u:
            DP[u, 0] = DP[u, 0] + DP[v, 1]
            DP[u, 1] = DP[u, 1] + min(DP[v, 0], DP[v, 1])
            
    Return min(DP[r, 0], DP[r, 1])
```

### Complexity Analysis
1. **Tree Rooting & Traversal:** Running a standard depth-first search (DFS) from root $r$ discovers parent-child relationships and produces a post-order ordering in $O(|V| + |E|)$ time. In any tree, $|E| = |V| - 1$, so this step takes $O(|V|)$ time.
2. **DP State Computation:** For each vertex $u$, calculating $DP[u, 0]$ and $DP[u, 1]$ requires $O(1 + |C(u)|)$ operations. Summed over all vertices:
   $$\sum_{u \in V} O(1 + |C(u)|) = O\left(|V| + \sum_{u \in V} |C(u)|\right) = O(|V| + (|V| - 1)) = O(|V|)$$
3. **Space Complexity:** Storing adjacency lists, parent/child arrays, and the DP table entries requires $O(|V|)$ space.

Total running time is strictly **$O(|V|)$**.

---

## 5. Walkthrough Example

Consider a campus tree with 5 buildings, $V = \{1, 2, 3, 4, 5\}$, rooted at vertex 1:
- Pathway edges from root 1: $(1, 2)$ and $(1, 3)$
- Pathway edges from node 2: $(2, 4)$ and $(2, 5)$
- Leaves: 3, 4, and 5

Evaluating the nodes in post-order order $[4, 5, 2, 3, 1]$:

| Vertex $u$ | Children $C(u)$ | $DP[u, 0]$ | $DP[u, 1]$ | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **4** (leaf) | $\emptyset$ | $0$ | $1$ | Base case |
| **5** (leaf) | $\emptyset$ | $0$ | $1$ | Base case |
| **3** (leaf) | $\emptyset$ | $0$ | $1$ | Base case |
| **2** | $\{4, 5\}$ | $DP[4,1] + DP[5,1] = 1 + 1 = 2$ | $1 + \min(0,1) + \min(0,1) = 1 + 0 = 1$ | Placing light on 2 covers leaves |
| **1** (root) | $\{2, 3\}$ | $DP[2,1] + DP[3,1] = 1 + 1 = 2$ | $1 + \min(2,1) + \min(0,1) = 1 + 1 + 0 = 2$ | Minimum across both choices is 2 |

**Result:** $\min(DP[1, 0], DP[1, 1]) = \min(2, 2) = 2$.
Optimal light placements are $\{2, 1\}$ or $\{2, 3\}$, both requiring exactly 2 lights to illuminate all edges.
