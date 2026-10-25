# CS 6515 / 4540: Approximation, ILP, Duality & Rounding Guide

> **Problems Covered:** 1. Maximum Independent Set (MIS) · 2. Maximum Clique · 3. 0-1 Knapsack · 4. Minimum Hitting Set  
> **Questions Answered for Each Case:**  
> - **(i)** Design a greedy approximation. What constant do you get?  
> - **(ii)** Write it as an Integer Linear Program (ILP), including all necessary constraints, and state its LP relaxation.  
> - **(iii)** Write the Dual of the LP relaxation from part (ii).  
> - **(iv)** Design an approximation algorithm via rounding.

---

## Part 0: Universal Exam Blueprint (How to Answer (i)–(iv) for Any Problem)

1. **(i) Greedy Approximation & Ratio ($\alpha$):**
   - **Maximization** ($\text{Independent Set, Clique, Knapsack}$): An $\alpha$-approximation ($\alpha \ge 1$, or equivalently $\frac{1}{\alpha} \in (0,1]$) must return a feasible solution $\mathrm{ALG}$ satisfying:
     $$\frac{1}{\alpha}\,\mathrm{OPT} \le \mathrm{ALG} \le \mathrm{OPT}$$
   - **Minimization** ($\text{Hitting Set, Vertex Cover}$): An $\alpha$-approximation ($\alpha \ge 1$) must return a feasible solution $\mathrm{ALG}$ satisfying:
     $$\mathrm{OPT} \le \mathrm{ALG} \le \alpha\,\mathrm{OPT}$$
   - **How to prove the ratio:** You never know $\mathrm{OPT}$ directly. Always bound $\mathrm{OPT}$ using a **structural certificate** (e.g., maximum degree $\Delta$, pairwise disjoint sets/matchings, or fractional LP optimum $\mathrm{OPT}_{\mathrm{LP}}$).

2. **(ii) Integer Linear Program (ILP) & LP Relaxation:**
   - Always state: (a) **Decision variables** $x_i \in \{0,1\}$, (b) **Objective function** ($\max$ or $\min$), and (c) **All constraints** (feasibility constraints + binary integrality constraints).
   - **Crucial Exam Trap on $x_i \le 1$:** When you relax $x_i \in \{0,1\}$ to an LP to take the dual in part (iii) or round in part (iv):
     - For **Minimization with $\ge$ constraints and $w_i \ge 0$** (like Hitting Set / Vertex Cover), $x_i \le 1$ is **redundant** at optimality because raising $x_i$ above $1$ only increases cost. So the LP relaxation simply uses $x_i \ge 0$.
     - For **Maximization** (like Knapsack), $x_i \le 1$ is **mandatory**! Without $x_i \le 1$, you could take multiple copies of an item (Unbounded Knapsack). For Independent Set / Clique with at least one incident constraint per vertex, $x_u + x_v \le 1$ together with $x \ge 0$ already implies $x_u \le 1$ (except for isolated vertices).

3. **(iii) Writing the Dual LP:**
   - **Step 1:** Relax the ILP to a **Linear Program (LP)** (LP duality applies to continuous LPs, not discrete ILPs).
   - **Step 2:** Put the Primal LP in **Canonical Form**:
     $$\text{Primal (Max): } \max c^\top x \text{ s.t. } Ax \le b,\, x \ge 0 \quad \Longleftrightarrow \quad \text{Dual (Min): } \min b^\top y \text{ s.t. } A^\top y \ge c,\, y \ge 0$$
   - **Step 3:** Assign **one dual variable per primal functional constraint**, and write **one dual constraint per primal variable $x_i$**.

4. **(iv) Approximation via Rounding:**
   - **Two-step proof template** (Lecture 15 / HW 4 Q18):
     1. **Feasibility:** Prove the rounded integral vector $\hat{x} \in \{0,1\}^n$ satisfies every ILP constraint.
     2. **Approximation Guarantee:** Compare $\mathrm{ALG} = c^\top \hat{x}$ against $\mathrm{OPT}_{\mathrm{LP}} = c^\top x^*$, and use the **LP Sandwich Bound**:
        - Minimization: $\mathrm{ALG} \le \alpha\,\mathrm{OPT}_{\mathrm{LP}} \le \alpha\,\mathrm{OPT}$.
        - Maximization: $\mathrm{ALG} \ge \frac{1}{\alpha}\,\mathrm{OPT}_{\mathrm{LP}} \ge \frac{1}{\alpha}\,\mathrm{OPT}$.

---

## Master Summary Table Across All 4 Cases

| Problem | Type | (i) Greedy Algorithm & Factor | (ii) Primal LP Relaxation | (iii) Dual LP | (iv) Rounding Algorithm & Guarantee |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **1. Independent Set (MIS)** | Max | Pick min-degree $v$, delete $\{v\} \cup N(v)$:<br>**$(\Delta+1)$-approx** (or **$\Delta$-approx** on connected graphs with $\Delta \ge 1$; $n$-approx in general) | $\max \sum_{v \in V} w_v x_v$<br>s.t. $x_u + x_v \le 1 \;\forall (u,v)\in E$<br>$x_v \ge 0 \;\forall v\in V$ | $\min \sum_{e \in E} y_e$<br>s.t. $\sum_{e \in \delta(v)} y_e \ge w_v \;\forall v$<br>$y_e \ge 0 \;\forall e\in E$<br>*(Fractional Edge Cover)* | **Integrality gap is $n/2$** in general ($K_n$ has $x_v^*=1/2$).<br>- **Bipartite / Trees:** LP is integral ($1$-approx).<br>- **LP + Nemhauser–Trotter / Randomized Rounding:** picks $x_v^* > 1/2$ exactly; $O(\Delta)$-approx on bounded-degree graphs. |
| **2. Clique** | Max | Complement of MIS ($G \to \bar{G}$):<br>Pick max-degree $v$, restrict to $N(v)$:<br>**$(\bar{\Delta}+1)$-approx** (where $\bar{\Delta} = n - 1 - \delta(G)$; $n$-approx in general) | $\max \sum_{v \in V} w_v x_v$<br>s.t. $x_u + x_v \le 1 \;\forall \{u,v\}\notin E$<br>$x_v \ge 0 \;\forall v\in V$ | $\min \sum_{\bar{e} \in \bar{E}} y_{\bar{e}}$<br>s.t. $\sum_{\bar{e} \in \delta_{\bar{G}}(v)} y_{\bar{e}} \ge w_v \;\forall v$<br>$y_{\bar{e}} \ge 0 \;\forall \bar{e}\in \bar{E}$ | Identical to MIS on $\bar{G}$ ($\bar{E} = \binom{V}{2}\setminus E$).<br>**Integrality gap is $n/2$** on empty graph $\bar{K}_n$.<br>Rounding on $\bar{G}$ with max non-degree $\bar{\Delta}$ gives $O(\bar{\Delta})$-approx. |
| **3. 0-1 Knapsack** | Max | **Modified Greedy:** Sort by $v_i/s_i \downarrow$; take $\max\{\text{Greedy}, \max_i v_i\}$:<br>**$2$-approx** ($\mathrm{ALG} \ge \frac{1}{2}\mathrm{OPT}$)<br>*(Naive greedy alone is unbounded!)* | $\max \sum_{i=1}^n v_i x_i$<br>s.t. $\sum_{i=1}^n s_i x_i \le B$<br>$0 \le x_i \le 1 \;\forall i$ | $\min B\alpha + \sum_{i=1}^n \beta_i$<br>s.t. $s_i\alpha + \beta_i \ge v_i \;\forall i$<br>$\alpha \ge 0,\, \beta_i \ge 0 \;\forall i$ | **1. LP Split-Item Rounding:** Basic opt $x^*$ has $\le 1$ fractional item $k$; take $\max\{\lfloor x^*\rfloor, \{k\}\} \implies$ **$2$-approx**.<br>**2. Value-Rounding (FPTAS, Lec 4–5):** $\hat{v}_i = \lfloor \frac{v_i}{K}\rfloor$, $K = \frac{\varepsilon V_{\max}}{n}$ + DP $\implies$ **$(1-\varepsilon)$-approx**. |
| **4. Hitting Set** ($|B_j| \le b$) | Min | **1. Disjoint Set Matching:** Pick disjoint $B_j$, take all elements $\implies$ **$b$-approx** (unweighted).<br>**2. Greedy Max-Coverage:** **$H_m = O(\log m)$-approx**. | $\min \sum_{i=1}^n w_i x_i$<br>s.t. $\sum_{i \in B_j} x_i \ge 1 \;\forall j$<br>$x_i \ge 0 \;\forall i$ | $\max \sum_{j=1}^m y_j$<br>s.t. $\sum_{j : i \in B_j} y_j \le w_i \;\forall i$<br>$y_j \ge 0 \;\forall j$<br>*(Fractional Set Packing)* | **Deterministic Threshold Rounding (Lec 15 / HW 4 Q18):**<br>$H = \{i : x_i^* \ge 1/b\}$<br>**$b$-approx** ($\mathrm{ALG} \le b\,\mathrm{OPT}_{\mathrm{LP}} \le b\,\mathrm{OPT}$).<br>*(Special case $b=2$ is Vertex Cover!)* |

---

## Case 1: Maximum Independent Set (MIS)

**Problem Setup:** Given an undirected graph $G = (V, E)$ with $|V| = n$, $|E| = m$, maximum degree $\Delta$, and optional vertex weights $w_v \ge 0$ ($w_v = 1$ in the unweighted case), find a subset $S \subseteq V$ of mutually non-adjacent vertices ($\forall (u,v) \in E,\, \{u,v\} \not\subseteq S$) maximizing $\sum_{v \in S} w_v$ (or $|S|$).

> **Note on Complexity:** On general graphs, Maximum Independent Set is NP-hard to approximate within $n^{1-\varepsilon}$ for any $\varepsilon > 0$ (unless $\mathrm{P}=\mathrm{NP}$). Therefore, **constant-factor approximations exist when the maximum degree $\Delta$ is bounded by a constant** (or on special graph classes like trees/bipartite/planar graphs). On an exam, always state the bound in terms of **both $\Delta$ (constant when $\Delta = O(1)$) and $n$**.

### (i) Greedy Approximation & Constant

#### Algorithm (Minimum-Degree Greedy)
1. Initialize $S \leftarrow \emptyset$ and active graph $G' \leftarrow G$.
2. While $V(G') \ne \emptyset$:
   - Pick a vertex $v \in V(G')$ of **minimum degree** in $G'$ (or in the weighted case, maximum ratio $\frac{w_v}{\deg_{G'}(v)+1}$, or any vertex $v$).
   - Add $v$ to $S$: $S \leftarrow S \cup \{v\}$.
   - Delete $v$ and all of its neighbors $N_{G'}(v)$ from $G'$ (since none of $N(v)$ can be in $S$).
3. Return $S$.

#### Approximation Guarantee: $(\Delta + 1)$-Approximation ($\Delta$-Approximation for $\Delta \ge 1$; $n$-Approximation in general)
- **Feasibility:** Whenever $v$ is added to $S$, all neighbors $N_{G'}(v)$ are immediately deleted from $G'$. Thus no two vertices in $S$ share an edge, so $S$ is a valid independent set.
- **Approximation Ratio Proof:**
  - In each iteration, adding $v$ to $S$ removes $\{v\} \cup N_{G'}(v)$ from $G'$, which contains at most $\deg(v) + 1 \le \Delta + 1$ vertices in total.
  - Consider the optimal independent set $S^*$ ($|S^*| = \mathrm{OPT}$). In each step where $v$ is chosen:
    - If $v \in S^*$, then no neighbor $u \in N_{G'}(v)$ can belong to $S^*$, so deleting $\{v\} \cup N_{G'}(v)$ removes only $1$ vertex of $S^*$.
    - If $v \notin S^*$, then at most $\deg_{G'}(v) \le \Delta$ neighbors of $v$ can belong to $S^*$.
  - Thus, each iteration deletes at most $\max\{1, \Delta\} \le \Delta + 1$ vertices of $S^*$. Across all $|S|$ iterations, every vertex of $S^*$ is deleted, so:
    $$\mathrm{OPT} = |S^*| \le (\Delta + 1)|S| \implies |S| \ge \frac{1}{\Delta + 1}\,\mathrm{OPT} \quad \left(\text{and } |S| \ge \frac{1}{\Delta}\,\mathrm{OPT} \text{ whenever } \Delta \ge 1\right).$$
  - **What constant do you get?**
    - If maximum degree $\Delta$ is bounded by a constant, you get a **$\Delta$-approximation** (or **$(\Delta+1)$-approximation** in the weighted case).
    - In an arbitrary graph with no degree bound ($\Delta \le n-1$), $|S| \ge 1 \ge \frac{1}{n}\,\mathrm{OPT}$, giving an **$n$-approximation**.

---

### (ii) Integer Linear Programming (ILP) Formulation

#### Decision Variables
For each vertex $v \in V$, introduce a binary indicator variable:
$$x_v = \begin{cases} 1 & \text{if } v \in S, \\ 0 & \text{if } v \notin S. \end{cases}$$

#### ILP Formulation
$$\begin{aligned}
\max \quad & \sum_{v \in V} w_v x_v \quad \left(\text{or } \sum_{v \in V} x_v \text{ if unweighted}\right) \\
\text{subject to} \quad & x_u + x_v \le 1 \qquad \forall (u,v) \in E \quad \text{(at most one endpoint of any edge can be chosen)} \\
& x_v \in \{0, 1\} \qquad \forall v \in V \quad \text{(binary integrality constraint)}
\end{aligned}$$
*(Note: If the graph can have **isolated vertices** with degree $0$, also include $x_v \le 1 \;\forall v \in V$ when relaxing to an LP so isolated vertices remain bounded by $1$.)*

---

### (iii) Dual of the LP Relaxation

#### Step 1: Write the Primal LP Relaxation in Canonical Form
Assuming every vertex has at least one incident edge (otherwise include $x_v \le 1$), $x_u + x_v \le 1$ and $x_v \ge 0$ automatically enforce $x_v \le 1$. Thus the **Primal LP** is:
$$\begin{aligned}
\max \quad & \sum_{v \in V} w_v x_v \\
\text{subject to} \quad & x_u + x_v \le 1 \qquad \forall e = (u,v) \in E \qquad \text{[Dual variable: } y_e \ge 0\text{]} \\
& x_v \ge 0 \qquad \forall v \in V
\end{aligned}$$

#### Step 2: Formulate the Dual LP
- **Dual Variables:** Associate $y_e \ge 0$ with each edge constraint $e = (u,v) \in E$.
- **Dual Objective:** Minimize $\sum_{e \in E} 1 \cdot y_e$.
- **Dual Constraints:** For each primal variable $x_v$ ($v \in V$), sum the dual variables of all edges incident to $v$, denoted $\delta(v) = \{e \in E : v \in e\}$:
$$\begin{aligned}
\min \quad & \sum_{e \in E} y_e \\
\text{subject to} \quad & \sum_{e \in \delta(v)} y_e \ge w_v \qquad \forall v \in V \\
& y_e \ge 0 \qquad \forall e \in E
\end{aligned}$$
*(Combinatorial Interpretation: This is the **Fractional Minimum Edge Cover** problem. If you also included $x_v \le 1$ with dual variable $z_v \ge 0$, the dual objective is $\min \sum_{e \in E} y_e + \sum_{v \in V} z_v$ subject to $z_v + \sum_{e \in \delta(v)} y_e \ge w_v$ and $y_e, z_v \ge 0$.)*

---

### (iv) Approximation Algorithm via Rounding

#### Important Exam Insight: Why Naive Threshold Rounding Fails on General Graphs
- On a complete graph $K_n$ (or odd triangle $K_3$), $\mathrm{OPT} = 1$, whereas setting $x_v^* = \frac{1}{2}$ for all $v \in V$ satisfies $x_u^* + x_v^* = 1 \le 1$ and gives $\mathrm{OPT}_{\mathrm{LP}} = \frac{n}{2}$.
- Thus the **integrality gap is $\frac{n}{2}$**, and rounding $\hat{x}_v = 1 \iff x_v^* \ge 1/2$ would pick **all $n$ vertices**, violating every edge constraint!

#### Approach A: Strict Threshold Rounding ($x_v^* > \frac{1}{2}$) + Nemhauser–Trotter Property
1. Solve the LP relaxation to obtain an extreme-point optimal solution $x^* \in \{0, \frac{1}{2}, 1\}^V$ (by the Nemhauser–Trotter Theorem, every basic optimal solution of the MIS LP is **half-integral**: $x_v^* \in \{0, \frac{1}{2}, 1\}$).
2. Round:
   $$S_1 = \left\{v \in V : x_v^* > \frac{1}{2}\right\} = \{v \in V : x_v^* = 1\}.$$
   - **Feasibility:** For any edge $(u,v) \in E$, if both $u, v \in S_1$, then $x_u^* > 1/2$ and $x_v^* > 1/2 \implies x_u^* + x_v^* > 1$, contradicting $x_u^* + x_v^* \le 1$. Thus $S_1$ is always a feasible independent set.
3. For the remaining half-integral subgraph $V_{1/2} = \{v \in V : x_v^* = 1/2\}$, run Greedy MIS on $G[V_{1/2}]$ to obtain $S_2$, and return $S = S_1 \cup S_2$.
   - Since $\sum_{v \in V_{1/2}} w_v x_v^* = \frac{1}{2}w(V_{1/2})$ and Greedy obtains at least $\frac{1}{\Delta+1}w(V_{1/2}) = \frac{2}{\Delta+1}\sum_{v \in V_{1/2}} w_v x_v^*$, the combined solution achieves a **$\frac{\Delta+1}{2}$-approximation**.

#### Approach B: Scaled Randomized Rounding with Alteration (Bounded Degree $\Delta$)
1. Solve the LP relaxation to get $x^*$ with $\sum_{v \in V} x_v^* = \mathrm{OPT}_{\mathrm{LP}} \ge \mathrm{OPT}$.
2. Independently sample each vertex $v \in V$ into a candidate set $R$ with probability $p_v = \frac{x_v^*}{2\Delta}$.
3. **Alteration (Conflict Resolution):** For every edge $e = (u,v) \in E$, if both $u \in R$ and $v \in R$, remove $u$ and $v$. Let $S \subseteq R$ be the surviving vertices.
4. **Guarantee:** $S$ is feasible, and for each $v$, $\Pr[v \in S] \ge \Pr[v \in R] - \sum_{u \in N(v)} \Pr[u \in R \wedge v \in R] = \frac{x_v^*}{2\Delta}\left(1 - \sum_{u \in N(v)} \frac{x_u^*}{2\Delta}\right) \ge \frac{x_v^*}{2\Delta}\left(1 - \frac{\Delta}{2\Delta}\right) = \frac{x_v^*}{4\Delta}$. By linearity of expectation:
   $$\mathbb{E}[|S|] \ge \sum_{v \in V} \frac{x_v^*}{4\Delta} = \frac{\mathrm{OPT}_{\mathrm{LP}}}{4\Delta} \ge \frac{1}{4\Delta}\,\mathrm{OPT} \quad \text{(a } 4\Delta\text{-approximation in expectation)}.$$

---

## Case 2: Maximum Clique

**Problem Setup:** Given an undirected graph $G = (V, E)$, find a subset $C \subseteq V$ of mutually adjacent vertices ($\forall u \ne v \in C,\, (u,v) \in E$) maximizing $\sum_{v \in C} w_v$ (or $|C|$).

> **Key Duality with Independent Set:** A subset $C \subseteq V$ is a **Clique in $G = (V, E)$** if and only if $C$ is an **Independent Set in the complement graph $\bar{G} = (V, \bar{E})$**, where:
> $$\bar{E} = \left\{\{u,v\} \subseteq V : u \ne v \text{ and } (u,v) \notin E\right\}$$
> consists of all **non-edges** of $G$. Every result for Independent Set transfers directly to Clique by replacing $E$ with $\bar{E}$ and degree $\deg_G(v)$ with non-degree $\deg_{\bar{G}}(v) = (n - 1) - \deg_G(v)$.

### (i) Greedy Approximation & Constant

#### Algorithm (Maximum-Degree Neighborhood Greedy)
1. Initialize $C \leftarrow \emptyset$ and candidate vertex set $U \leftarrow V$.
2. While $U \ne \emptyset$:
   - Pick a vertex $v \in U$ with **maximum degree in $G[U]$** (equivalently, minimum degree in $\bar{G}[U]$).
   - Add $v$ to $C$: $C \leftarrow C \cup \{v\}$.
   - Restrict candidates to vertices adjacent to $v$: $U \leftarrow U \cap N_G(v)$ (equivalently, delete $v$ and its non-neighbors $N_{\bar{G}}(v)$).
3. Return $C$.

#### Approximation Guarantee
- Let $\bar{\Delta} = \max_{v \in V} \deg_{\bar{G}}(v) = n - 1 - \delta(G)$ be the maximum number of non-neighbors of any vertex (where $\delta(G)$ is the minimum degree of $G$).
- By the exact same analysis as Independent Set on $\bar{G}$, each step deletes $v$ and at most $\bar{\Delta}$ non-neighbors from $U$, eliminating at most $\bar{\Delta} + 1$ vertices of the optimal clique $C^*$:
  $$|C| \ge \frac{1}{\bar{\Delta} + 1}\,\mathrm{OPT} = \frac{1}{n - \delta(G)}\,\mathrm{OPT}.$$
- **What constant do you get?**
  - If $\bar{\Delta}$ is bounded by a constant (dense graphs where every vertex misses at most $\bar{\Delta}$ edges), Greedy achieves a **$(\bar{\Delta}+1)$-approximation** (or **$\bar{\Delta}$-approximation** for $\bar{\Delta} \ge 1$).
  - In a general graph, picking any vertex (or any edge) gives an **$n$-approximation** (or $n/2$-approximation).

---

### (ii) Integer Linear Programming (ILP) Formulation

#### Decision Variables
For each vertex $v \in V$, let $x_v \in \{0, 1\}$ indicate whether $v \in C$.

#### Constraint Logic
Two distinct vertices $u \ne v$ **cannot both belong to the clique $C$** if and only if they do **not** share an edge in $G$, i.e., $\{u,v\} \notin E$ (equivalently, $\{u,v\} \in \bar{E}$).

#### ILP Formulation
$$\begin{aligned}
\max \quad & \sum_{v \in V} w_v x_v \quad \left(\text{or } \sum_{v \in V} x_v\right) \\
\text{subject to} \quad & x_u + x_v \le 1 \qquad \forall \{u, v\} \notin E \;\; (u \ne v) \quad \text{(non-adjacent vertices cannot both be in } C\text{)} \\
& x_v \in \{0, 1\} \qquad \forall v \in V
\end{aligned}$$
*(Note: Include $x_v \le 1 \;\forall v \in V$ in the LP relaxation if a vertex can be adjacent to all other vertices in $G$, i.e., isolated in $\bar{G}$.)*

---

### (iii) Dual of the LP Relaxation

#### Step 1: Primal LP Relaxation
Let $\bar{E} = \{\{u,v\} : u \ne v,\, (u,v) \notin E\}$ denote the set of non-edges.
$$\begin{aligned}
\max \quad & \sum_{v \in V} w_v x_v \\
\text{subject to} \quad & x_u + x_v \le 1 \qquad \forall \bar{e} = \{u,v\} \in \bar{E} \qquad \text{[Dual variable: } y_{\bar{e}} \ge 0\text{]} \\
& x_v \ge 0 \qquad \forall v \in V
\end{aligned}$$

#### Step 2: Dual LP Formulation
Introduce a dual variable $y_{\bar{e}} \ge 0$ for each non-edge $\bar{e} = \{u,v\} \in \bar{E}$:
$$\begin{aligned}
\min \quad & \sum_{\bar{e} \in \bar{E}} y_{\bar{e}} \\
\text{subject to} \quad & \sum_{\bar{e} \in \bar{E} : v \in \bar{e}} y_{\bar{e}} \ge w_v \qquad \forall v \in V \\
& y_{\bar{e}} \ge 0 \qquad \forall \bar{e} \in \bar{E}
\end{aligned}$$

---

### (iv) Approximation Algorithm via Rounding

Because the Clique LP is identical to the Independent Set LP on $\bar{G} = (V, \bar{E})$:
1. **Integrality Gap Warning:** On an empty graph $G = (V, \emptyset)$, $\mathrm{OPT} = 1$, while $x_v^* = 1/2 \;\forall v$ satisfies all non-edge constraints $x_u + x_v \le 1$, giving $\mathrm{OPT}_{\mathrm{LP}} = n/2$ (integrality gap $n/2$).
2. **Half-Integral / Strict Threshold Rounding ($x_v^* > 1/2$):**
   - Solve the Clique LP relaxation for a basic optimal solution $x^* \in \{0, \frac{1}{2}, 1\}^V$.
   - Set $C_1 = \{v \in V : x_v^* > 1/2\}$.
   - **Feasibility Proof:** For any two distinct vertices $u, v \in C_1$, we have $x_u^* > 1/2$ and $x_v^* > 1/2 \implies x_u^* + x_v^* > 1$. If $\{u,v\} \notin E$, the LP constraint $x_u^* + x_v^* \le 1$ would be violated. Hence $\{u,v\} \in E$ for every pair in $C_1$, so $C_1$ is a valid clique.
   - Augmenting $C_1$ with Greedy Clique on $V_{1/2} = \{v : x_v^* = 1/2\}$ yields a **$\frac{\bar{\Delta}+1}{2}$-approximation**.
3. **Randomized Rounding with Alteration:** Sampling $v \in R$ independently with probability $p_v = \frac{x_v^*}{2\bar{\Delta}}$ and deleting non-edge conflicts $\{u,v\} \in \bar{E}$ gives a **$4\bar{\Delta}$-approximation** in expectation.

---

## Case 3: 0-1 Knapsack

**Problem Setup:** Given $n$ items where each item $i \in \{1, \dots, n\}$ has size (weight) $s_i \in (0, B]$ and value $v_i > 0$, and a knapsack capacity $B > 0$, choose a subset $S \subseteq \{1, \dots, n\}$ with $\sum_{i \in S} s_i \le B$ maximizing $\sum_{i \in S} v_i$. *(Assume $s_i \le B$ for all $i$; any item with $s_i > B$ can never be packed and is discarded immediately.)*

### (i) Greedy Approximation & Constant

#### Common Exam Trap: Why Naive Greedy by Density Fails
If you only sort items by value-to-size density $\frac{v_1}{s_1} \ge \frac{v_2}{s_2} \ge \dots \ge \frac{v_n}{s_n}$ and pack greedily, the approximation ratio is **unbounded**!
- *Counterexample:* Capacity $B = W$. Item 1 has $v_1 = 2,\, s_1 = 1$ (density $2$). Item 2 has $v_2 = W,\, s_2 = W$ (density $1$). Naive greedy picks Item 1 (value $2$) and cannot fit Item 2 (value $W$), giving ratio $W/2 \to \infty$.

#### Correct Algorithm: Modified Greedy (Best of Greedy Prefix and Max Single Item)
1. Sort items in non-increasing order of value density:
   $$\frac{v_1}{s_1} \ge \frac{v_2}{s_2} \ge \dots \ge \frac{v_n}{s_n}.$$
2. Let $k$ be the largest index such that $\sum_{i=1}^k s_i \le B$ (the prefix packed by Greedy), and let $G = \{1, 2, \dots, k\}$. (If $k = n$, return $G$, which is optimal.)
3. Let $i_{\max} = \arg\max_{i \in \{1,\dots,n\}} v_i$ (or specifically item $k+1$, the first item that did not fit).
4. **Return the better of the two feasible solutions:**
   $$S_{\text{alg}} = \arg\max\left\{v(G),\; v_{i_{\max}}\right\}.$$

#### Approximation Guarantee: **$2$-Approximation** ($\mathrm{ALG} \ge \frac{1}{2}\,\mathrm{OPT}$)
- **Proof via Fractional Knapsack Upper Bound:**
  - The LP relaxation (Fractional Knapsack) is solved optimally by taking items $1, \dots, k$ completely ($x_1^* = \dots = x_k^* = 1$) and taking a fraction $x_{k+1}^* = \frac{B - \sum_{i=1}^k s_i}{s_{k+1}} \in (0, 1]$ of the "split item" $k+1$.
  - Therefore, the optimal fractional value $\mathrm{OPT}_{\mathrm{LP}}$ satisfies:
    $$\mathrm{OPT} \le \mathrm{OPT}_{\mathrm{LP}} = \sum_{i=1}^k v_i + x_{k+1}^* v_{k+1} < \underbrace{\sum_{i=1}^k v_i}_{v(G)} + \underbrace{v_{k+1}}_{\le v_{i_{\max}}}.$$
  - Since $v(G) + v_{i_{\max}} > \mathrm{OPT}$, the larger of the two terms must be at least half their sum:
    $$\mathrm{ALG} = \max\left\{v(G),\; v_{i_{\max}}\right\} \ge \frac{1}{2}\left(v(G) + v_{i_{\max}}\right) > \frac{1}{2}\,\mathrm{OPT}_{\mathrm{LP}} \ge \frac{1}{2}\,\mathrm{OPT}.$$
- **What constant do you get?** You get a **$2$-approximation** (returning at least $\frac{1}{2}\,\mathrm{OPT}$).

---

### (ii) Integer Linear Programming (ILP) Formulation

#### Decision Variables
For each item $i \in \{1, \dots, n\}$, let $x_i \in \{0, 1\}$ indicate whether item $i$ is placed in the knapsack.

#### ILP Formulation
$$\begin{aligned}
\max \quad & \sum_{i=1}^n v_i x_i \\
\text{subject to} \quad & \sum_{i=1}^n s_i x_i \le B \qquad \text{(knapsack capacity constraint)} \\
& x_i \in \{0, 1\} \qquad \forall i \in \{1, \dots, n\} \quad \text{(0-1 integrality constraint)}
\end{aligned}$$

#### LP Relaxation (Crucial: Must Include $x_i \le 1$!)
When relaxing $x_i \in \{0,1\}$ to continuous variables, we **must** include $x_i \le 1$:
$$\begin{aligned}
\max \quad & \sum_{i=1}^n v_i x_i \\
\text{subject to} \quad & \sum_{i=1}^n s_i x_i \le B \qquad \text{[Dual variable: } \alpha \ge 0\text{]} \\
& x_i \le 1 \qquad \forall i \in \{1, \dots, n\} \qquad \text{[Dual variables: } \beta_i \ge 0\text{]} \\
& x_i \ge 0 \qquad \forall i \in \{1, \dots, n\}
\end{aligned}$$

---

### (iii) Dual of the LP Relaxation

- **Dual Variables:**
  - $\alpha \ge 0$ for the capacity constraint $\sum_{i=1}^n s_i x_i \le B$ (marginal value per unit of capacity).
  - $\beta_i \ge 0$ for each upper-bound constraint $x_i \le 1$ ($i = 1, \dots, n$).
- **Dual Objective:** Minimize $B\alpha + \sum_{i=1}^n 1 \cdot \beta_i$.
- **Dual Constraints:** One constraint per primal variable $x_i$ ($i = 1, \dots, n$):
$$\begin{aligned}
\min \quad & B\alpha + \sum_{i=1}^n \beta_i \\
\text{subject to} \quad & s_i \alpha + \beta_i \ge v_i \qquad \forall i \in \{1, \dots, n\} \\
& \alpha \ge 0 \\
& \beta_i \ge 0 \qquad \forall i \in \{1, \dots, n\}
\end{aligned}$$
*(Intuition: For a fixed unit-capacity price $\alpha$, each item $i$ sets $\beta_i = \max\{0,\, v_i - s_i \alpha\}$, the "surplus value" of item $i$ above its capacity cost $s_i\alpha$.)*

---

### (iv) Approximation Algorithm via Rounding

Below are **both** standard rounding algorithms for Knapsack covered in CS 6515:

#### Method 1: Extreme-Point LP Rounding ($2$-Approximation)
1. Solve the Knapsack LP relaxation to find an **extreme-point (basic) optimal solution** $x^* \in [0,1]^n$.
2. **Structural Property of Basic Solutions (Lecture 9):** The LP has $n$ variables and only $1$ functional constraint ($\sum_{i=1}^n s_i x_i \le B$) plus box constraints $0 \le x_i \le 1$. Any vertex in $\mathbb{R}^n$ is defined by $n$ linearly independent tight constraints. Since at most $1$ tight constraint can come from $\sum_i s_i x_i = B$, at least $n-1$ tight constraints must come from $x_i = 0$ or $x_i = 1$.
3. Therefore, **$x^*$ has at most one fractional variable** $x_k^* \in (0, 1)$, and all other variables are already integral ($x_i^* \in \{0, 1\}$ for $i \ne k$).
4. **Rounding Rule:** Let $S_{\text{floor}} = \{i : x_i^* = 1\}$ (obtained by rounding down $\hat{x}_i = \lfloor x_i^* \rfloor$) and let $S_{\text{split}} = \{k\}$ (the single fractional item). Both $S_{\text{floor}}$ and $S_{\text{split}}$ are feasible. Return the one with larger value:
   $$S_{\text{alg}} = \arg\max\left\{v(S_{\text{floor}}),\; v_k\right\}.$$
5. **Approximation Proof:**
   $$\mathrm{OPT} \le \mathrm{OPT}_{\mathrm{LP}} = \sum_{i \in S_{\text{floor}}} v_i + x_k^* v_k < v(S_{\text{floor}}) + v_k \le 2 \max\{v(S_{\text{floor}}),\, v_k\} = 2\,\mathrm{ALG} \implies \mathrm{ALG} \ge \frac{1}{2}\,\mathrm{OPT}.$$

#### Method 2: Value Scaling & Rounding + DP (FPTAS, $(1-\varepsilon)$-Approximation — Lectures 4–5)
1. Let $V_{\max} = \max_i v_i$. Given accuracy parameter $\varepsilon \in (0,1)$, set scaling factor $K = \frac{\varepsilon V_{\max}}{n}$ and round each item's value down:
   $$\hat{v}_i = \left\lfloor \frac{v_i}{K} \right\rfloor.$$
2. Run the value-indexed Dynamic Programming algorithm on the rounded values $\hat{v}_i$ (where $\sum_i \hat{v}_i \le n \lfloor V_{\max}/K \rfloor \le \lfloor n^2/\varepsilon \rfloor$) to find the exact optimal subset $\hat{S}$ for $\hat{v}$ in $O(n^3/\varepsilon)$ time.
3. **Guarantee:** Every item loses at most $K$ in value ($K\hat{v}_i \le v_i \le K(\hat{v}_i + 1)$), so for optimal set $S^*$:
   $$v(\hat{S}) \ge K\hat{v}(\hat{S}) \ge K\hat{v}(S^*) \ge v(S^*) - |S^*|K \ge \mathrm{OPT} - n\left(\frac{\varepsilon V_{\max}}{n}\right) = \mathrm{OPT} - \varepsilon V_{\max} \ge (1 - \varepsilon)\,\mathrm{OPT}.$$

---
## Case 4: Minimum Hitting Set (Lectures 14–15 & HW 4 Q18)

**Problem Setup:** Given a ground set of elements $U = \{1, 2, \dots, n\}$ where element $i$ has nonnegative weight $w_i \ge 0$ ($w_i = 1$ if unweighted), and a collection of subsets $B_1, B_2, \dots, B_m \subseteq U$ where each subset has size at most $b$ ($1 \le |B_j| \le b$ for all $j$), find a minimum-weight subset $H \subseteq U$ that "hits" every $B_j$ (i.e., $H \cap B_j \ne \emptyset$ for all $j = 1, \dots, m$).

> **Connection to Vertex Cover & Set Cover:**
> - When $b = 2$ (each $B_j = \{u,v\}$ is an edge), Minimum Hitting Set is **identical to Minimum Vertex Cover**.
> - Minimum Hitting Set is dual/equivalent to **Minimum Set Cover** where each element appears in at most $f = b$ sets.

### (i) Greedy Approximation & Constant

#### Algorithm 1: Maximal Disjoint-Set Greedy (Constant $b$-Approximation for Unweighted Hitting Set)
*(Direct generalization of Lecture 14's Maximal Matching $2$-approximation for Vertex Cover)*
1. Initialize $H \leftarrow \emptyset$ and collection of disjoint sets $\mathcal{M} \leftarrow \emptyset$.
2. While there is an unhit set $B_j$ (i.e., $B_j \cap H = \emptyset$):
   - Add $B_j$ to $\mathcal{M}$: $\mathcal{M} \leftarrow \mathcal{M} \cup \{B_j\}$.
   - Add **all** elements of $B_j$ to $H$: $H \leftarrow H \cup B_j$.
3. Return $H$.

- **Proof of $b$-Approximation:**
  - **Feasibility:** The loop terminates only when every set $B_j$ has $B_j \cap H \ne \emptyset$.
  - **Lower Bound on $\mathrm{OPT}$:** Every set $B_j \in \mathcal{M}$ was unhit when chosen, so the sets in $\mathcal{M}$ are **pairwise disjoint**. Any valid hitting set $H^*$ must pick at least one distinct element from each $B_j \in \mathcal{M}$:
    $$\mathrm{OPT} = |H^*| \ge |\mathcal{M}|.$$
  - **Upper Bound on $\mathrm{ALG}$:** For each $B_j \in \mathcal{M}$, the algorithm adds $|B_j| \le b$ elements to $H$:
    $$\mathrm{ALG} = |H| = \sum_{B_j \in \mathcal{M}} |B_j| \le b\,|\mathcal{M}| \le b\,\mathrm{OPT}.$$
- **What constant do you get?** You get a **$b$-approximation** (when $b=2$ for Vertex Cover, this is a **$2$-approximation**).
- *(Note: If instead you use the **Greedy Max-Coverage** rule—repeatedly picking the element $i$ that hits the maximum number of remaining unhit sets—you get an $H_m = \sum_{k=1}^m \frac{1}{k} \le 1 + \ln m = O(\log m)$ approximation.)*

---

### (ii) Integer Linear Programming (ILP) Formulation (HW 4 Q18)

#### Decision Variables
For each element $i \in \{1, \dots, n\}$, let:
$$x_i = \begin{cases} 1 & \text{if } i \in H, \\ 0 & \text{if } i \notin H. \end{cases}$$

#### ILP Formulation
$$\begin{aligned}
\min \quad & \sum_{i=1}^n w_i x_i \\
\text{subject to} \quad & \sum_{i \in B_j} x_i \ge 1 \qquad \forall j \in \{1, \dots, m\} \quad \text{(every set } B_j \text{ must contain at least one chosen element)} \\
& x_i \in \{0, 1\} \qquad \forall i \in \{1, \dots, n\}
\end{aligned}$$

#### LP Relaxation
Replace $x_i \in \{0,1\}$ with $x_i \ge 0$ (since $w_i \ge 0$ and we are minimizing, $x_i \le 1$ is redundant):
$$\begin{aligned}
\min \quad & \sum_{i=1}^n w_i x_i \\
\text{subject to} \quad & \sum_{i \in B_j} x_i \ge 1 \qquad \forall j \in \{1, \dots, m\} \qquad \text{[Dual variable: } y_j \ge 0\text{]} \\
& x_i \ge 0 \qquad \forall i \in \{1, \dots, n\}
\end{aligned}$$

---

### (iii) Dual of the LP Relaxation

- **Dual Variables:** Associate one dual variable $y_j \ge 0$ with each set constraint $B_j$ ($j = 1, \dots, m$).
- **Dual Objective:** Maximize $\sum_{j=1}^m 1 \cdot y_j$.
- **Dual Constraints:** One constraint per primal variable $x_i$ ($i = 1, \dots, n$). Variable $x_i$ appears in constraint $j$ if and only if $i \in B_j$:
$$\begin{aligned}
\max \quad & \sum_{j=1}^m y_j \\
\text{subject to} \quad & \sum_{j : i \in B_j} y_j \le w_i \qquad \forall i \in \{1, \dots, n\} \\
& y_j \ge 0 \qquad \forall j \in \{1, \dots, m\}
\end{aligned}$$
*(Combinatorial Interpretation: This is the **Fractional Set Packing** problem—assigning nonnegative dual prices $y_j \ge 0$ to sets $B_j$ so that the total price of sets containing any element $i$ never exceeds that element's weight $w_i$.)*

---

### (iv) Approximation Algorithm via Rounding (Lecture 15 & HW 4 Q18)

#### Deterministic Threshold Rounding Algorithm
1. Solve the LP relaxation in polynomial time to obtain an optimal fractional solution $x^* = (x_1^*, \dots, x_n^*)$.
2. **Threshold Rounding Rule:** Let $b = \max_{1 \le j \le m} |B_j|$. Round each variable using threshold $\frac{1}{b}$:
   $$\hat{x}_i = \begin{cases} 1 & \text{if } x_i^* \ge \frac{1}{b}, \\ 0 & \text{if } x_i^* < \frac{1}{b}, \end{cases} \qquad \text{so} \qquad H = \left\{i \in \{1, \dots, n\} : x_i^* \ge \frac{1}{b}\right\}.$$
3. Return $H$.

#### Complete 2-Part Proof (Feasibility + $b$-Approximation)

1. **Part 1: Proof of Feasibility ($H$ is a valid hitting set)**
   - Fix any subset $B_j$ ($j \in \{1, \dots, m\}$).
   - Because $x^*$ is feasible for the LP relaxation, $\sum_{i \in B_j} x_i^* \ge 1$.
   - Since $B_j$ contains $|B_j| \le b$ elements, by the **pigeonhole / averaging principle**, at least one element $i^* \in B_j$ must be at least the average:
     $$\max_{i \in B_j} x_i^* \ge \frac{1}{|B_j|} \sum_{i \in B_j} x_i^* \ge \frac{1}{b} \cdot 1 = \frac{1}{b}.$$
   - Therefore, that element $i^* \in B_j$ satisfies $x_{i^*}^* \ge \frac{1}{b}$ and is included in $H$, so $H \cap B_j \ne \emptyset$ for every $j$. Thus $H$ is feasible.

2. **Part 2: Proof of $b$-Approximation Guarantee ($\mathrm{ALG} \le b\,\mathrm{OPT}$)**
   - For every element $i \in H$, the rounding rule guarantees $x_i^* \ge \frac{1}{b}$, which rearranges to:
     $$1 = \hat{x}_i \le b\,x_i^*.$$
   - For $i \notin H$, $\hat{x}_i = 0 \le b\,x_i^*$ since $x_i^* \ge 0$.
   - Since $w_i \ge 0$ for all $i$, summing over all elements gives:
     $$\mathrm{ALG} = \sum_{i \in H} w_i = \sum_{i=1}^n w_i \hat{x}_i \le \sum_{i=1}^n w_i \left(b\,x_i^*\right) = b \sum_{i=1}^n w_i x_i^* = b\,\mathrm{OPT}_{\mathrm{LP}}.$$
   - Because every integral hitting set is also a feasible solution to the LP relaxation, $\mathrm{OPT}_{\mathrm{LP}} \le \mathrm{OPT}$. Chaining the inequalities yields:
     $$\mathrm{ALG} \le b\,\mathrm{OPT}_{\mathrm{LP}} \le b\,\mathrm{OPT}. \quad \blacksquare$$

---

## Quick Checklist of Common Exam Pitfalls to Avoid

1. **Don't confuse $\mathrm{OPT}_{\mathrm{LP}} \le \mathrm{OPT}$ (Minimization) vs. $\mathrm{OPT}_{\mathrm{LP}} \ge \mathrm{OPT}$ (Maximization):**
   - In **Minimization** (Hitting Set), relaxing $\{0,1\}$ to $[0,1]$ enlarges the feasible region, so $\mathrm{OPT}_{\mathrm{LP}} \le \mathrm{OPT}$.
   - In **Maximization** (Independent Set, Clique, Knapsack), enlarging the feasible region increases the maximum, so $\mathrm{OPT}_{\mathrm{LP}} \ge \mathrm{OPT}$.
2. **Don't threshold-round Independent Set or Clique at $x_v^* \ge 1/2$:**
   - For Hitting Set ($\sum_{i \in B_j} x_i \ge 1$), rounding **up** at $x_i^* \ge 1/b$ preserves $\ge 1$ covering constraints.
   - For Independent Set / Clique ($x_u + x_v \le 1$), rounding **up** at $x_v^* \ge 1/2$ **violates** the $\le 1$ packing constraint whenever $x_u^* = x_v^* = 1/2$. You must either use strict threshold $x_v^* > 1/2$ (which preserves feasibility) or scaled randomized rounding with conflict deletion.
3. **Don't omit $x_i \le 1$ in the Knapsack LP Relaxation:**
   - Without $x_i \le 1$, the LP relaxation solves **Unbounded Knapsack** (putting all capacity $B$ into the single highest-density item even if $B > s_i$), and the dual would be missing the $\beta_i$ variables.


