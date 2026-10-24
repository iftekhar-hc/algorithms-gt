# Study Guide: Question 3 — Metric Steiner Tree & 2-Approximation via MST
**Course:** CS 6515 / 4540 (Practice Exam 2 — Section 3: Steiner Tree, 19 Points)

---

## 1. The Exam Problem Statement (Question 3)

> Suppose we are given a fully-connected (complete) graph $G = (V, E)$ with nonnegative edge weights satisfying the triangle inequality, and a subset $T \subseteq V$ of vertices that must be connected. Find a minimum-weight subset of edges $F \subseteq E$ that connects all vertices in $T$ (vertices in $V \setminus T$ may or may not be connected).
> *(Note: The optimal solution is a tree because otherwise we can drop a cycle edge while maintaining connectivity. Finding the minimum such tree (known as Steiner tree) is NP-complete.)*
>
> Let $G_T$ be a fully-connected subgraph of $G$ induced by $T$ (i.e., the subgraph where we remove vertices $V \setminus T$). In this problem we will prove that the minimum spanning tree (MST) of $G_T$ is a 2-approximation to the minimum Steiner tree.
>
> 1. **(12 points)** Let $F^*$ denote the subset of edges that form the minimum Steiner tree. Prove how we can use it to form a spanning tree of $G_T$ (note this spanning tree cannot visit any vertex in $V \setminus T$ since $G_T$ only has vertices $T$) of total weight at most twice the total weight of $F^*$.
>    *(Hint: The proof is similar to why MST is a 2-approx for TSP. Recall that $G$ is complete and edge-weights satisfy triangle inequality.)*
> 2. **(7 points)** Using part 1 (even if you have not proved it), deduce that MST of $G_T$ is a 2-approx for minimum Steiner tree.

---

## 2. Core Concepts & Definitions

### 2.1 Minimum Spanning Tree (MST) vs. Minimum Steiner Tree
Suppose you want to build a network of fiber-optic cables of minimum total length:
- **Minimum Spanning Tree (MST):** You are required to connect **every single vertex** in $V$.
  - *Complexity:* Solvable in **polynomial time** using Kruskal's or Prim's algorithm!
- **Steiner Tree Problem:** You are given a subset of required **terminal vertices** $T \subseteq V$ that *must* be connected to each other, and optional **Steiner vertices** (relay/junction points) $V \setminus T$ that you *may* optionally use if routing through them makes the total network cheaper.
  - *Complexity:* **NP-complete**! Why? Because there are $2^{|V \setminus T|}$ subsets of optional Steiner vertices you could choose to include, and finding the best subset is combinatorially hard.

#### Understanding the Exam's Example Diagram:
```
Full Graph G (T = {A, B, C}, Steiner vertex D):
        A
       /|\
     2/ |1\2
     /  D  \
    B 1/ \1 C
     \-----/
        2
```
- **Terminals:** $T = \{A, B, C\}$. Direct edges between $A, B, C$ each cost $2$.
- **Optional Steiner Vertex:** $D \notin T$. Edges $(A,D), (B,D), (C,D)$ each cost $1$.
- **Minimum Steiner Tree $F^*$:** Uses the optional central hub $D$! Connects $A-D, B-D, C-D$ for a total weight of:
  $$w(F^*) = 1 + 1 + 1 = 3.$$
- **Induced Subgraph $G_T$:** Throws away vertex $D$ and its incident edges, leaving only $T = \{A, B, C\}$ and the edges of weight $2$ between them.
- **MST of $G_T$:** Picks any two edges in $G_T$, say $(A, B)$ and $(B, C)$, for a total weight of:
  $$w(\text{MST}(G_T)) = 2 + 2 = 4.$$
- Notice: $4 > 3$ (not optimal, because it ignored hub $D$), **but** $4 \le 2 \times 3 = 6$! In fact, $w(\text{MST}(G_T)) \le 2 \, w(F^*)$ holds for *every* metric graph!

---

### 2.2 Induced Subgraph $G_T$ and Complete Graphs
- **Complete (Fully-Connected) Graph $G = (V, E)$:** Every pair of distinct vertices $u, v \in V$ has a direct edge $(u, v) \in E$.
- **Subgraph Induced by $T$ ($G_T = (T, E_T)$):**
  - Keep **only** the vertices in $T$ (delete all vertices in $V \setminus T$).
  - Keep all edges from $E$ whose **both endpoints** lie in $T$: $E_T = \{(u, v) \in E \mid u \in T \text{ and } v \in T\}$.
  - Since $G$ was complete, $G_T$ is **also a complete graph** on the vertex set $T$! That guarantees that for *any* two terminals $u, v \in T$, the direct edge $(u, v)$ exists in $G_T$.

---

### 2.3 The Triangle Inequality (Metric Graphs)
Edge weights $w : E \to \mathbb{R}_{\ge 0}$ satisfy the **triangle inequality** if for any three vertices $x, y, z \in V$:
$$w(x, z) \le w(x, y) + w(y, z).$$
- **Meaning:** Going directly from $x$ to $z$ via edge $(x, z)$ is never more expensive than taking a detour through $y$.
- **Generalization to Paths (By Induction):** For *any* path $P = (v_0, v_1, v_2, \dots, v_k)$ between $v_0$ and $v_k$ in $G$, the direct edge $(v_0, v_k)$ has weight at most the sum of the edge weights along the path:
  $$w(v_0, v_k) \le \sum_{i=0}^{k-1} w(v_i, v_{i+1}) = w(P).$$
- **Why this is essential:** If our walk in $G$ goes from terminal $u \in T$, passes through several non-terminal vertices in $V \setminus T$ (or already-visited vertices in $T$), and arrives at terminal $v \in T$, we can **shortcut (bypass)** all those intermediate vertices by taking the single direct edge $(u, v) \in E_T$ without increasing the total weight!

---

### 2.4 What is an $\alpha$-Approximation Algorithm?
Let $\text{OPT}$ be the cost/value of the optimal solution to an NP-hard problem, and let $\text{ALG}$ be the cost/value returned by a polynomial-time algorithm:
- **For a Minimization Problem (like Steiner Tree or TSP):**
  An algorithm is a **2-approximation** if for every instance:
  $$\text{OPT} \le \text{ALG} \le 2 \cdot \text{OPT}.$$
  *(Note: Since $\text{ALG}$ outputs a valid feasible solution, $\text{ALG} \ge \text{OPT}$ is automatic for minimization.)*
- **For a Maximization Problem (like Short Answer Q1.6):**
  An algorithm is a **2-approximation** if for every instance:
  $$\frac{1}{2} \cdot \text{OPT} \le \text{ALG} \le \text{OPT}.$$
  *(Connection to Short Answer Q1.6: If $\text{OPT} = 5$ in a maximization problem, any valid solution must have value $\le 5$, and a 2-approx guarantees value $\ge 5/2 = 2.5$. So among $\{2.5, 5, 7, 10\}$, only **A (2.5)** and **B (5)** are possible!)*

---

## 3. The "Double-Tree / DFS Shortcutting" Proof Technique (Part 1)

This is the exact same three-step technique used to prove that MST gives a 2-approximation for Metric TSP! Here is how it adapts to Steiner Tree:

### Step 1: Double the Edges of $F^*$ and Take a DFS Walk (Eulerian Tour)
- Start with the optimal Steiner tree $F^*$. By definition, $F^*$ is a tree in $G$ that spans all terminals $T$ (plus possibly some Steiner vertices $S \subseteq V \setminus T$).
- **Double every edge in $F^*$** (or equivalently, perform a Depth-First Search (DFS) traversal of the tree $F^*$ starting and ending at some terminal $r \in T$).
- In a DFS traversal of a tree, you traverse every edge of $F^*$ **twice** (once going down, once backtracking up).
- This produces a closed walk $W$ that visits every vertex of $F^*$ (and hence **every terminal in $T$**) with total weight:
  $$w(W) = 2 \, w(F^*).$$

#### Illustration on the Exam's Example ($F^*$ has edges $(A,D), (B,D), (C,D)$):
- Start DFS at $A \in T$:
  $$W : \quad A \xrightarrow{1} D \xrightarrow{1} B \xrightarrow{1} D \xrightarrow{1} C \xrightarrow{1} D \xrightarrow{1} A.$$
- Every edge of $F^*$ is traversed twice, so $w(W) = 1+1+1+1+1+1 = 6 = 2 \, w(F^*)$.

### Step 2: Shortcut Past Non-Terminals ($V \setminus T$) and Repeated Terminals
- Walk along $W$ and record the terminals of $T$ in the order they are **visited for the first time**:
  $$t_1, t_2, \dots, t_k \quad (\text{where } k = |T|).$$
- Instead of following the sub-walk of $W$ between $t_i$ and $t_{i+1}$ (which may pass through non-terminals in $V \setminus T$ and previously visited terminals), replace that sub-walk with the **single direct edge** $(t_i, t_{i+1})$ in $G_T$!
- **Why does $(t_i, t_{i+1})$ exist in $G_T$?** Because $G$ is complete, and both $t_i, t_{i+1} \in T$, so $(t_i, t_{i+1})$ is an edge of $G_T$.
- **Why doesn't the weight increase?** By the **triangle inequality**, the weight of the direct edge $w(t_i, t_{i+1})$ is at most the weight of the sub-walk of $W$ between $t_i$ and $t_{i+1}$!
- Since the sub-walks between consecutive $t_i$ and $t_{i+1}$ are edge-disjoint parts of $W$:
  $$\sum_{i=1}^{k-1} w(t_i, t_{i+1}) \;\le\; w(W) \;=\; 2 \, w(F^*).$$

#### Illustration on the Example:
- Order of first visits to $T = \{A, B, C\}$ in $W$: $t_1 = A$, $t_2 = B$, $t_3 = C$.
  - Shortcut $A \to D \to B$ to direct edge $(A, B)$: $w(A, B) = 2 \le w(A, D) + w(D, B) = 1 + 1 = 2$.
  - Shortcut $B \to D \to C$ to direct edge $(B, C)$: $w(B, C) = 2 \le w(B, D) + w(D, C) = 1 + 1 = 2$.
  - Drop the final return segment $C \to D \to A$ (or if you kept it to form a TSP cycle, drop one cycle edge to get a tree!).

### Step 3: Conclude We Have a Spanning Tree of $G_T$
- The path $H = \{(t_1, t_2), (t_2, t_3), \dots, (t_{k-1}, t_k)\}$ connects all $k = |T|$ vertices in $T$ using $k-1$ edges and no cycles—so **$H$ is a spanning tree of $G_T$** (specifically, a Hamiltonian path on $T$)!
- *(Alternative phrasing: If you also shortcut $t_k \to t_1$ to get a simple cycle on $T$ of weight $\le 2\,w(F^*)$, deleting any one edge from the cycle leaves a spanning tree $H$ of $G_T$ with weight $\le 2\,w(F^*)$ since edge weights are nonnegative.)*
- Either way, we have constructed a spanning tree $H$ of $G_T$ with:
  $$w(H) \le 2 \, w(F^*).$$

---

## 4. Deducing That $\text{MST}(G_T)$ is a 2-Approximation (Part 2)

Once Part 1 gives us *some* spanning tree $H$ of $G_T$ satisfying $w(H) \le 2 \, w(F^*)$, Part 2 is a 3-line deduction!

1. **Why we can't just construct $H$ directly in our algorithm:**
   To build $H$ in Part 1, we started from $F^*$—the optimal Steiner tree, which is NP-hard to find and unknown to the algorithm!
2. **Why $\text{MST}(G_T)$ is even better than $H$:**
   Even though we don't know $H$, we *do* know that **$H$ is a valid spanning tree of $G_T$**.
   By definition, the **Minimum Spanning Tree** $\text{MST}(G_T)$ has the minimum total weight among *all* possible spanning trees of $G_T$. Therefore:
   $$w(\text{MST}(G_T)) \;\le\; w(H).$$
3. **Chain the inequalities together:**
   $$w(\text{MST}(G_T)) \;\le\; w(H) \;\le\; 2 \, w(F^*).$$
   Furthermore, since $G_T$ can be formed and its MST computed in polynomial time (using Kruskal's or Prim's algorithm), and $\text{MST}(G_T)$ connects all vertices in $T$, $\text{MST}(G_T)$ is a polynomial-time **2-approximation** to the minimum Steiner tree!

---

## 5. Model Exam Solutions (Concise & Full Credit)

### Part 1 (12 points)
> **Model Exam Solution:**
> 1. **Double edges / DFS walk:** Perform a depth-first search (DFS) traversal of the minimum Steiner tree $F^*$ starting and ending at some terminal $t_1 \in T$. Since the traversal crosses every edge of $F^*$ exactly twice, this produces a closed walk $W$ that visits all vertices in $T$ with total weight
>    $$w(W) = 2 \, w(F^*).$$
> 2. **Shortcut via Triangle Inequality:** Let $t_1, t_2, \dots, t_k$ (where $k = |T|$) be the vertices of $T$ ordered by their **first appearance** along the walk $W$. For each $i = 1, \dots, k-1$, replace the sub-walk of $W$ from $t_i$ to $t_{i+1}$ (which may pass through vertices in $V \setminus T$ or already-visited vertices in $T$) with the single direct edge $(t_i, t_{i+1})$.
> 3. **Validity and Weight Bound:** Since $G$ is complete and $t_i, t_{i+1} \in T$, every direct edge $(t_i, t_{i+1})$ belongs to $G_T$. By the **triangle inequality**, $w(t_i, t_{i+1})$ is at most the weight of the sub-walk of $W$ between $t_i$ and $t_{i+1}$.
>    Let $H = \{(t_1, t_2), (t_2, t_3), \dots, (t_{k-1}, t_k)\}$ (dropping the remaining portion of $W$ from $t_k$ back to $t_1$, which has nonnegative weight). Then $H$ is a path visiting every vertex in $T$ exactly once—hence **$H$ is a spanning tree of $G_T$**—and its total weight satisfies:
>    $$w(H) = \sum_{i=1}^{k-1} w(t_i, t_{i+1}) \le w(W) = 2 \, w(F^*). \quad \blacksquare$$

---

### Part 2 (7 points)
> **Model Exam Solution:**
> By Part 1, there exists a spanning tree $H$ of $G_T$ whose total weight satisfies $w(H) \le 2 \, w(F^*)$.
> Let $M$ be a Minimum Spanning Tree (MST) of $G_T$. By definition of the MST, $M$ has the minimum weight among all spanning trees of $G_T$; since $H$ is a spanning tree of $G_T$, we must have:
> $$w(M) \le w(H).$$
> Combining this with Part 1 yields:
> $$w(M) \le w(H) \le 2 \, w(F^*).$$
> Since $M$ connects all vertices of $T$ (so it is a valid Steiner tree) and has weight at most $2 \, w(F^*)$ (and can be computed in polynomial time via Kruskal's/Prim's algorithm), the MST of $G_T$ is a **2-approximation** for the minimum Steiner tree. $\blacksquare$

---

## 6. Self-Assessment Questions

Use these questions to test your mastery of Question 3:

1. **Why We Need $\text{MST}(G_T)$ Instead of Just Using $H$:** In Part 1, we showed how to construct a spanning tree $H$ of $G_T$ with weight $\le 2 \, w(F^*)$. Why can't our polynomial-time approximation algorithm just output $H$ directly instead of computing $\text{MST}(G_T)$?
2. **Role of the Triangle Inequality:** Where specifically in the proof of Part 1 would the argument fail if the edge weights of $G$ did **not** satisfy the triangle inequality? Give a tiny modification of the exam's 4-vertex example ($A, B, C, D$) where the triangle inequality is violated and $w(\text{MST}(G_T)) > 100 \, w(F^*)$.
3. **Role of Nonnegative Weights:** Where in the proof do we use the fact that edge weights are **nonnegative** ($w(e) \ge 0$)?
4. **Tighter Analysis on the Star Graph:** Suppose $G$ has $k$ terminals $T = \{t_1, \dots, t_k\}$ and one central Steiner vertex $D \notin T$, where $w(t_i, D) = 1$ for all $i$ and $w(t_i, t_j) = 2$ for all $i \ne j$ (generalizing the exam's example from $k=3$ to any $k$).
   - What is $w(F^*)$ in terms of $k$?
   - What is $w(\text{MST}(G_T))$ in terms of $k$?
   - What happens to the ratio $\frac{w(\text{MST}(G_T))}{w(F^*)}$ as $k \to \infty$?
5. **Connection to Short Answer Q1.6:** In Question 3, our 2-approximation algorithm returns a solution of cost $\text{ALG}$ satisfying $\text{OPT} \le \text{ALG} \le 2 \cdot \text{OPT}$. In Short Answer Q1.6, a 2-approximation algorithm is run on a **maximization** problem with $\text{OPT} = 5$. What is the range of possible values $\text{ALG}$ can take, and which choices among $\{2.5, 5, 7, 10\}$ are possible?
