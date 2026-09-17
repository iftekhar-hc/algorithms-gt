# Bipartite Matching: Forbidden Paths

## 1. Problem Formulation

Let $G = (V, E)$ be a directed graph with vertex set:
$$
V = \{v_1, \ldots, v_n\},
$$
and a forbidden set:
$$
F = \{f_1, \ldots, f_k\} \subset V.
$$

We construct an undirected bipartite graph $\widehat{G} = (L \cup R, \widehat{E})$ as follows:
- $L = \{v_1, \ldots, v_n\}$
- $R = \{v'_1, \ldots, v'_n\}$
- For every $i \in \{1, \ldots, n\}$, add identity edge $\{v_i, v'_i\}$ to $\widehat{E}$.
- For every directed edge $(v_i, v_j) \in E$, add edge $\{v_i, v'_j\}$ to $\widehat{E}$.

Given two distinct vertices $v_s, v_t \in V \setminus F$:
1. Delete $v'_s$ from $R$.
2. Delete $v_t$ from $L$.
3. For each $f_i \in F$, delete $f_i$ from $L$ and $f'_i$ from $R$.
4. Delete all incident edges for any deleted vertex.

### Goal
Prove that a **perfect matching** exists in $\widehat{G}$ if and only if there exists a directed path from $v_s$ to $v_t$ in $G$ that avoids all vertices in $F$.

---

## 2. Vertex and Edge Analysis

Let $U = V \setminus F$ denote the set of permitted vertices. After performing the prescribed deletions:

- **Remaining Left Vertices:**
  $$
  L_{\text{rem}} = V \setminus (F \cup \{v_t\}) = U \setminus \{v_t\}
  $$
- **Remaining Right Vertices:**
  $$
  R_{\text{rem}} = \{u' : u \in V \setminus (F \cup \{v_s\})\} = \{u' : u \in U \setminus \{v_s\}\}
  $$

The sizes match:
$$
|L_{\text{rem}}| = |R_{\text{rem}}| = |V| - |F| - 1 = n - k - 1.
$$

The edges remaining in $\widehat{E}$ are:
1. **Identity / Diagonal Edges:** $\{u, u'\}$ for all $u \in U \setminus \{v_s, v_t\}$.
2. **Directed Graph Edges:** $\{u, w'\}$ for $(u, w) \in E$ where $u \in U \setminus \{v_t\}$ and $w \in U \setminus \{v_s\}$.

---

## 3. Proof: Path $\implies$ Perfect Matching $(\Leftarrow)$

Assume there exists a simple directed path $P$ in $G$ from $v_s$ to $v_t$ avoiding $F$:
$$
P: p_0 \to p_1 \to p_2 \to \cdots \to p_m
$$
where $m \ge 1$, $p_0 = v_s$, $p_m = v_t$, and all $p_i \in U$ are pairwise distinct.

We construct a matching $M \subset \widehat{E}$ as follows:

1. **Path Matching:**
   For each $i \in \{0, 1, \ldots, m-1\}$:
   - $(p_i, p_{i+1}) \in E$ corresponds to the edge $\{p_i, p'_{i+1}\} \in \widehat{E}$.
   - Since $p_i \ne v_t$ for $i < m$, $p_i \in L_{\text{rem}}$.
   - Since $p_{i+1} \ne v_s$ for $i \ge 0$, $p'_{i+1} \in R_{\text{rem}}$.
   - Place $\{p_i, p'_{i+1}\} \in M$.
   This matches vertices $\{p_0, \ldots, p_{m-1}\} \subseteq L_{\text{rem}}$ to $\{p'_1, \ldots, p'_m\} \subseteq R_{\text{rem}}$.

2. **Diagonal Matching:**
   For every vertex $u \in U \setminus \{p_0, p_1, \ldots, p_m\}$ not traversed by $P$:
   - $u \ne v_s$ and $u \ne v_t$, so $u \in L_{\text{rem}}$ and $u' \in R_{\text{rem}}$.
   - Place the identity edge $\{u, u'\} \in M$.

### Verification
- The path vertices cover $\{p_0, \ldots, p_{m-1}\} \subset L_{\text{rem}}$ and $\{p'_1, \ldots, p'_m\} \subset R_{\text{rem}}$.
- The non-path vertices cover the remaining sets $(U \setminus P) \subset L_{\text{rem}}$ and $(U \setminus P)' \subset R_{\text{rem}}$.
- Every vertex in $L_{\text{rem}}$ and $R_{\text{rem}}$ is matched exactly once.

Thus, $M$ is a perfect matching in $\widehat{G}$. $\blacksquare$

---

## 4. Proof: Perfect Matching $\implies$ Path $(\Rightarrow)$

Assume $\widehat{G}$ has a perfect matching $M$.

Define an auxiliary directed graph $H = (U, E_H)$ where:
$$
(u, w) \in E_H \iff \{u, w'\} \in M.
$$

### Degree Analysis in $H$
- **Out-degrees:**
  - For each $u \in U \setminus \{v_t\} = L_{\text{rem}}$, $u$ is incident to exactly one edge in $M$. Hence $\text{out-deg}_H(u) = 1$.
  - Since $v_t \notin L_{\text{rem}}$, $\text{out-deg}_H(v_t) = 0$.
- **In-degrees:**
  - For each $w \in U \setminus \{v_s\}$, $w' \in R_{\text{rem}}$ is incident to exactly one edge in $M$. Hence $\text{in-deg}_H(w) = 1$.
  - Since $v'_s \notin R_{\text{rem}}$, $\text{in-deg}_H(v_s) = 0$.
- **Intermediate Vertices:**
  - For every $u \in U \setminus \{v_s, v_t\}$, $\text{in-deg}_H(u) = \text{out-deg}_H(u) = 1$.

### Structural Decomposition
A graph where every vertex has in-degree $\le 1$ and out-degree $\le 1$ decomposes into disjoint directed paths and cycles:
- $v_s$ has in-degree $0$ and out-degree $1$, so it is the starting point of a directed path.
- $v_t$ has out-degree $0$ and in-degree $1$, so it is the endpoint of a directed path.
- All other vertices have in-degree $1$ and out-degree $1$.

Following the unique outgoing edge from $v_s$:
$$
v_s = q_0 \to q_1 \to q_2 \to \cdots \to q_r
$$
Because the graph is finite and $v_s$ has in-degree 0, this path cannot cycle back to $v_s$ and must terminate at the unique sink $q_r = v_t$.

For every step $q_i \to q_{i+1}$ on this path:
- $q_i \ne q_{i+1}$ (no self-loops on a path between distinct vertices).
- $\{q_i, q'_{i+1}\} \in M$ must be a directed graph edge, implying $(q_i, q_{i+1}) \in E$.

Since all vertices of $H$ lie in $U = V \setminus F$, this yields a directed path from $v_s$ to $v_t$ in $G$ avoiding $F$. $\blacksquare$

---

## 5. Walkthrough Example

Let $V = \{1, 2, 3, 4, 5\}$, $v_s = 1$, $v_t = 4$, and $F = \{5\}$.
- Permitted vertices: $U = \{1, 2, 3, 4\}$.
- Edge set $E = \{(1, 2), (2, 4), (1, 3), (3, 5), (5, 4)\}$.

### Active Sets
- $L_{\text{rem}} = \{1, 2, 3\}$
- $R_{\text{rem}} = \{2', 3', 4'\}$

### Available Edges
- Diagonal edges: $\{2, 2'\}, \{3, 3'\}$
- Graph edges: $\{1, 2'\}, \{2, 4'\}, \{1, 3'\}$ (Edges with $5$ or $5'$ are deleted).

### Perfect Matching
Selecting path $1 \to 2 \to 4$:
- $\{1, 2'\} \in M$ (covers $1 \in L, 2' \in R$)
- $\{2, 4'\} \in M$ (covers $2 \in L, 4' \in R$)
- $\{3, 3'\} \in M$ (covers $3 \in L, 3' \in R$)

All vertices are matched, confirming the equivalence.
