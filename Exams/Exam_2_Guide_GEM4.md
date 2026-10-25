# CS 6515: Graduate Algorithms — Comprehensive Study Guide (Lectures 1–15)

> **Course:** CS 6515: Graduate Algorithms (Georgia Tech, Fall 2026)  
> **Instructors:** Prof. Sahil Singla & Prof. Gerandy Brito  
> **Scope:** Complete coverage of `Lec_1_Unmarked.pdf` through `Lec_15_Unmarked.pdf`  

---

## Table of Contents

- [0. Course Roadmap, Synthesis & Master Reference Table](#0-course-roadmap-synthesis--master-reference-table)
- [Module 1: Asymptotic Notation, Recurrences & Divide-and-Conquer (Lectures 1–3)](#module-1-asymptotic-notation-recurrences--divide-and-conquer-lectures-13)
  - [Lecture 1: Course Overview, Asymptotic Notation & Merge Sort](#lecture-1-course-overview-asymptotic-notation--merge-sort)
  - [Lecture 2: Strong Induction, Master Theorem & Maximum Difference](#lecture-2-strong-induction-master-theorem--maximum-difference)
  - [Lectures 2 & 3: Deterministic Linear-Time Selection (Median-of-Medians)](#lectures-2--3-deterministic-linear-time-selection-median-of-medians)
- [Module 2: Dynamic Programming, FPTAS & Markov Decision Processes (Lectures 3–5)](#module-2-dynamic-programming-fptas--markov-decision-processes-lectures-35)
  - [Lecture 3: Dynamic Programming Recipe, Largest Contiguous Sum & LCS](#lecture-3-dynamic-programming-recipe-largest-contiguous-sum--lcs)
  - [Lecture 4: Tree DP (Maximum Independent Set) & 0-1 Knapsack](#lecture-4-tree-dp-maximum-independent-set--0-1-knapsack)
  - [Lectures 4 & 5: Knapsack FPTAS via Value Scaling](#lectures-4--5-knapsack-fptas-via-value-scaling)
  - [Lecture 5: Finite-Horizon Markov Decision Processes (MDPs)](#lecture-5-finite-horizon-markov-decision-processes-mdps)
- [Module 3: Graph Algorithms — Search, Shortest Paths, MSTs, Matchings & Max-Flow (Lectures 6–8)](#module-3-graph-algorithms--search-shortest-paths-msts-matchings--max-flow-lectures-68)
  - [Lecture 6: Graph Representations, BFS, Dijkstra's Algorithm & MST Cut Property](#lecture-6-graph-representations-bfs-dijkstras-algorithm--mst-cut-property)
  - [Lecture 7: Prim's MST Algorithm, Matchings & Berge's Theorem](#lecture-7-prims-mst-algorithm-matchings--berges-theorem)
  - [Lecture 8: Maximum Flow, Residual Networks, Ford-Fulkerson & Max-Flow Min-Cut](#lecture-8-maximum-flow-residual-networks-ford-fulkerson--max-flow-min-cut)
- [Module 4: Linear Programming, Duality Theory & Farkas' Lemma (Lectures 9–11)](#module-4-linear-programming-duality-theory--farkas-lemma-lectures-911)
  - [Lecture 9: LP Formulations, Convex Geometry, Vertices & Polynomial Solvability](#lecture-9-lp-formulations-convex-geometry-vertices--polynomial-solvability)
  - [Lecture 10: LP Duality, Shadow Prices & Max-Flow/Min-Cut via Threshold Rounding](#lecture-10-lp-duality-shadow-prices--max-flowmin-cut-via-threshold-rounding)
  - [Lecture 11: Farkas' Lemma, Convex Separation & Proof of Strong Duality](#lecture-11-farkas-lemma-convex-separation--proof-of-strong-duality)
- [Module 5: Convex Optimization & Gradient Descent (Lectures 12–13)](#module-5-convex-optimization--gradient-descent-lectures-1213)
  - [Lecture 12: Convex Functions, First/Second-Order Conditions & Bounded-Gradient Descent](#lecture-12-convex-functions-firstsecond-order-conditions--bounded-gradient-descent)
  - [Lecture 13: Projected Gradient Descent & $\beta$-Smooth Gradient Descent](#lecture-13-projected-gradient-descent--beta-smooth-gradient-descent)
- [Module 6: Approximation Algorithms — Greedy Methods & LP Rounding (Lectures 14–15)](#module-6-approximation-algorithms--greedy-methods--lp-rounding-lectures-1415)
  - [Lecture 14: Approximation Guarantees, Greedy Vertex Cover & Edge-Disjoint Paths](#lecture-14-approximation-guarantees-greedy-vertex-cover--edge-disjoint-paths)
  - [Lecture 15: LP Relaxations, Deterministic Rounding & Metric Facility Location](#lecture-15-lp-relaxations-deterministic-rounding--metric-facility-location)
- [7. Self-Test Quiz Bank (30 Questions with Solutions)](#7-self-test-quiz-bank-30-questions-with-solutions)
- [8. Comprehensive Exam Practice Problems (12 Multi-Part Problems with Rubric Solutions)](#8-comprehensive-exam-practice-problems-12-multi-part-problems-with-rubric-solutions)
- [9. Textbook References & Curated Video Lectures](#9-textbook-references--curated-video-lectures)

---

## 0. Course Roadmap, Synthesis & Master Reference Table

### 0.1 The Unifying Theme of CS 6515

An algorithm is a sequence of instructions that accomplishes a task while minimizing resources (time, space, or communication). Rather than memorizing isolated tricks, CS 6515 develops **general algorithmic paradigms** paired with **mathematical certificates of correctness and optimality**:

```text
+-----------------------------------------------------------------------------------+
|                        PART I: COMBINATORIAL ALGORITHMS                           |
|                                                                                   |
|  Divide & Conquer (Lec 1-3) ---> Dynamic Programming (Lec 3-5) ---> Graphs (6-8)  |
|  - Split into independent        - Overlapping subproblems          - Layers/Cuts |
|    subproblems                   - State remembers just enough      - Exchange    |
|  - Enrich return values            to extend a partial solution     - Augmenting  |
|  - Prune by good pivots          - Compress state via rounding        paths/flows |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                  PART II: OPTIMIZATION & APPROXIMATION ALGORITHMS                 |
|                                                                                   |
|  Linear Programming (Lec 9-11) -> Convex Opt (Lec 12-13) -> Approximation (14-15) |
|  - Separate modeling & solving    - Local gradient bounds   - Compare to lower    |
|  - Dual = best upper-bound          global error via          bound certificates: |
|    certificate (Farkas' Lemma)      convexity                 matchings, counting |
|  - Threshold rounding (Min-Cut)   - Projection & smoothness   or LP relaxations   |
+-----------------------------------------------------------------------------------+
```

### 0.2 Master Algorithm Reference Table (Lectures 1–15)

| Lec | Problem / Algorithm | Paradigm | Core Invariant / Certificate | Time Complexity | Space | Poly vs. Pseudo-Poly |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Merge Sort** | Divide & Conquer | Two halves sorted; merge scans fronts | $\Theta(n \log n)$ | $O(n)$ | Polynomial |
| **2** | **Max Difference** ($A[i]-A[j]$, $i \le j$) | Divide & Conquer | Return `(bestDiff, max, min)` per half | $\Theta(n)$ | $O(\log n)$ | Polynomial |
| **2–3** | **Deterministic Selection** (BFPRT) | Divide & Conquer | Pivot $p$ eliminates $\ge \frac{3}{10}n$ elements | $O(n)$ | $O(\log n)$ | Polynomial |
| **3** | **Largest Contiguous Sum** | Dynamic Prog. | $M[i]$ = best sum ending *exactly* at $i$ | $O(n)$ | $O(1)$ aux | Polynomial |
| **3–4** | **Longest Common Subsequence** | Dynamic Prog. | $D[i,j]$ = LCS of prefixes $A_{1..i}, B_{1..j}$ | $O(nm)$ | $O(nm)$ | Polynomial |
| **4** | **Tree Max Independent Set** | Tree DP | $M[v]$ (or $I[v], X[v]$) on subtree $T_v$ | $O(\lvert V\rvert)$ | $O(\lvert V\rvert)$ | Polynomial |
| **4–5** | **0-1 Knapsack (Value-Indexed)** | Dynamic Prog. | $D[i,v]$ = min size for exact value $v$ | $O(n V_{\text{sum}}) = O(n^2 V_{\max})$ | $O(n V_{\text{sum}})$ | **Pseudo-polynomial** |
| **4–5** | **Knapsack FPTAS** | DP + Scaling | Scale $\hat{v}_i = \lfloor v_i / K \rfloor$, $K = \varepsilon V_{\max}/n$ | $O(n^3 / \varepsilon)$ | $O(n^2 / \varepsilon)$ | **FPTAS** |
| **5** | **Finite-Horizon MDP** | Stochastic DP | Bellman eq. $V^*(s,t)$ with $t$ steps left | $O(T\lvert A\rvert\lvert S\rvert^2)$ | $O(T\lvert S\rvert)$ | Polynomial in table |
| **6** | **Breadth-First Search (BFS)** | Graph Search | Queue processes distance layers $L_0, L_1, \dots$ | $O(n+m)$ | $O(n)$ | Polynomial |
| **6** | **Dijkstra's Algorithm** ($w_e \ge 0$) | Greedy / Graph | Settled vertices have exact $d[u] = \text{dist}(s,u)$ | $O((n+m)\log n)$ (bin. heap)<br>$O(m+n\log n)$ (Fib. heap) | $O(n)$ | Polynomial |
| **6–7** | **Prim's MST Algorithm** | Greedy / Cut | $T \subseteq T^*$ for some MST $T^*$ via Cut Property | $O(m \log n)$ (bin. heap)<br>$O(m+n\log n)$ (Fib. heap) | $O(n)$ | Polynomial |
| **7** | **Bipartite Max Matching** | Augmenting Path | Berge's Theorem: max $\iff$ no aug. path | $O(nm)$ | $O(n+m)$ | Polynomial |
| **8** | **Ford-Fulkerson Max-Flow** (int $c_e$) | Augmenting Path | Residual graph $G_f$; reachable cut $X$ | $O((m+n)(1+\lvert f^*\rvert))$ | $O(n+m)$ | **Pseudo-polynomial** |
| **8** | **Edmonds-Karp Max-Flow** | Shortest Aug. Path | BFS in $G_f$ (fewest edges) | $\text{poly}(n,m)$ ($O(nm^2)$) | $O(n+m)$ | Strongly Polynomial |
| **9–11** | **Linear Programming (Rational)** | Polyhedral Opt. | Primal $x$ & Dual $y$ with $c^\top x = b^\top y$ | $\text{poly}(\text{bit length})$ | $\text{poly}$ | Poly in bit length |
| **12** | **Gradient Descent (Bounded $\nabla f$)** | Convex Opt. | Potential $R_t = \lVert x_t-x^*\rVert_2^2$; return $\bar{x}_T$ | $T = O(D^2G^2/\varepsilon^2)$ calls | $O(d)$ | Additive error $\varepsilon$ |
| **13** | **Projected Gradient Descent** | Constrained Convex | Projection $\Pi_K$ contracts distance to $x^* \in K$ | $T = O(D^2G^2/\varepsilon^2)$ steps | $O(d)$ | Additive error $\varepsilon$ |
| **13** | **$\beta$-Smooth Gradient Descent** | Smooth Convex | Descent lemma $f(x_{t+1}) \le f(x_t) - \frac{1}{2\beta}\lVert\nabla f\rVert_2^2$ | $T = O(\beta D^2/\varepsilon)$ calls | $O(d)$ | Last-iterate error $\varepsilon$ |
| **14** | **Greedy-Degree Vertex Cover** | Greedy Approx. | Remaining edges shrink by $(1 - 1/\text{OPT})$ | $O(m+n)$ | $O(n+m)$ | $(1+\ln m)$-approx |
| **14** | **Maximal-Matching Vertex Cover** | Greedy Approx. | Disjoint matching certificate $\lvert M\rvert \le \text{OPT}$ | $O(n+m)$ | $O(n+m)$ | $2$-approximation |
| **14** | **Directed Edge-Disjoint Paths** | Greedy + Cutoff | Short paths ($\le \lfloor\sqrt{m}\rfloor$) + counting | $\text{poly}(n,m,k)$ | $O(n+m)$ | $(2\sqrt{m}+1)$-approx |
| **15** | **Vertex Cover Threshold Rounding** | LP Rounding | $C = \{v : x_v^* \ge 1/2\}$, $\text{LP}^* \le \text{OPT}$ | LP solve + $O(n)$ | $\text{poly}$ | $2$-approximation |
| **15** | **Metric Facility Location Rounding** | LP Rounding + Balls | Disjoint balls $B_r$ of radius $2L_r$, sorted $L_j$ | LP solve + $\text{poly}(\lvert F\rvert,\lvert C\rvert)$ | $\text{poly}$ | $6$-approximation |

---

## Module 1: Asymptotic Notation, Recurrences & Divide-and-Conquer (Lectures 1–3)

### Lecture 1: Course Overview, Asymptotic Notation & Merge Sort

#### 1.1 Asymptotic Notation

For an input of size $n \in \mathbb{N}$, let $f, g : \mathbb{N} \to \mathbb{R}_{\ge 0}$ measure resource usage (typically elementary operations assuming $O(1)$-word arithmetic).

| Notation | Formal Definition | Limit Test (when limit exists) | Intuition |
| :--- | :--- | :--- | :--- |
| **$f(n) = O(g(n))$** | $\exists c > 0, n_0 \in \mathbb{N} \text{ s.t. } \forall n \ge n_0,\; f(n) \le c\,g(n)$ | $\lim_{n\to\infty} \frac{f(n)}{g(n)} < \infty$ | $f$ grows **no faster** than $g$ ($\le$) |
| **$f(n) = \Omega(g(n))$** | $\exists c > 0, n_0 \in \mathbb{N} \text{ s.t. } \forall n \ge n_0,\; f(n) \ge c\,g(n)$ | $\lim_{n\to\infty} \frac{f(n)}{g(n)} > 0$ | $f$ grows **at least as fast** as $g$ ($\ge$) |
| **$f(n) = \Theta(g(n))$** | $f(n) = O(g(n))$ **and** $f(n) = \Omega(g(n))$ | $0 < \lim_{n\to\infty} \frac{f(n)}{g(n)} < \infty$ | $f$ and $g$ grow at the **same rate** ($=$) |
| **$f(n) = o(g(n))$** | $\forall c > 0,\; \exists n_0 \in \mathbb{N} \text{ s.t. } \forall n \ge n_0,\; f(n) < c\,g(n)$ | $\lim_{n\to\infty} \frac{f(n)}{g(n)} = 0$ | $f$ grows **strictly slower** than $g$ ($<$) |
| **$f(n) = \omega(g(n))$** | $g(n) = o(f(n))$ | $\lim_{n\to\infty} \frac{f(n)}{g(n)} = \infty$ | $f$ grows **strictly faster** than $g$ ($>$) |

**Standard Growth Hierarchy:**

$$
1 = o(\log \log n) = o(\log n) = o(n^{0.1}) = o(n) = o(n \log n) = o(n^2) = o(2^n) = o(n!) = o(n^n) = o(2^{n^2})
$$

**Worked Proof 1 ($n! = o(n^n)$):**

$$
\frac{n^n}{n!} = \prod_{i=1}^n \frac{n}{i} \ge \frac{n}{1} = n \xrightarrow{n \to \infty} \infty \implies \lim_{n\to\infty} \frac{n!}{n^n} = 0 \implies n! = o(n^n)
$$

**Worked Proof 2 ($\log(n!) = \Theta(n \log n)$ — Lecture 1 Exercise):**
- **Upper bound $O(n \log n)$:** Since each of the $n$ factors in $n! = 1 \cdot 2 \cdots n$ is at most $n$, we have $n! \le n^n$. Taking base-2 logarithms yields:

$$
\log_2(n!) \le \log_2(n^n) = n \log_2 n = O(n \log n)
$$

- **Lower bound $\Omega(n \log n)$:** Keep only the largest $\lceil n/2 \rceil$ factors in $n!$, each of which is at least $n/2$:

$$
n! = \prod_{i=1}^n i \ge \prod_{i=\lceil n/2 \rceil}^n i \ge \left(\frac{n}{2}\right)^{n/2}
$$

Taking logarithms gives:

$$
\log_2(n!) \ge \frac{n}{2} \log_2\left(\frac{n}{2}\right) = \frac{n}{2}(\log_2 n - 1) \ge \frac{1}{4} n \log_2 n \quad (\text{for } n \ge 4)
$$

Hence $\log(n!) = \Omega(n \log n)$, and combining both bounds gives $\log(n!) = \Theta(n \log n)$. $\square$

---

#### 1.2 Divide-and-Conquer & Merge Sort

The **Divide-and-Conquer** paradigm consists of three steps:
1. **Divide:** Break the problem instance into smaller subproblems.
2. **Conquer:** Solve each subproblem recursively (or directly if at a base case).
3. **Combine:** Assemble the subproblem solutions into a solution for the original instance.

##### Case Study: Merge Sort
- **Input:** Array $A[0..n-1]$ of $n$ comparable numbers.
- **Goal:** Rearrange $A$ in nondecreasing order.
- **Algorithm (`Merge-Sort(A)`):**
  1. If $n \le 1$, return $A$.
  2. Split $A$ into left half $A[0..\lfloor n/2 \rfloor - 1]$ and right half $A[\lfloor n/2 \rfloor .. n-1]$.
  3. Recursively sort both halves.
  4. **Merge:** Repeatedly compare the smallest unmerged element at the front of each sorted half, append the smaller one to the output array, and append the remaining suffix when one half becomes empty.

- **Correctness (by Induction on $n$):**
  - *Base Case ($n \le 1$):* A 0- or 1-element array is trivially sorted.
  - *Inductive Step:* By the inductive hypothesis, the two recursive calls return sorted permutations of the left and right halves. At each step of `Merge`, the minimum of all remaining unmerged elements must sit at the front of one of the two halves. Because `Merge` selects the smaller front element at every step and outputs every element exactly once, the combined output is a nondecreasing permutation of $A$.

- **Running Time & Recursion Tree Visualization:**
  For $n = 2^k$, the recurrence is $T(n) = 2T(n/2) + cn$ with $T(1) = \Theta(1)$:

```text
Level 0:                     [       cn       ]                  -> Total work: cn
                            /                  \
Level 1:             [   cn/2   ]          [   cn/2   ]          -> Total work: 2(cn/2) = cn
                      /        \            /        \
Level 2:         [ cn/4 ]    [ cn/4 ]  [ cn/4 ]    [ cn/4 ]      -> Total work: 4(cn/4) = cn
                   ...         ...       ...         ...
Level i:         2^i subproblems, each of size n/2^i             -> Total work: 2^i(cn/2^i) = cn
                   ...         ...       ...         ...
Level log_2(n):  [O(1)] [O(1)] ... (n leaves of size 1)          -> Total work: Theta(n)
```

Summing across all $\log_2 n$ non-leaf levels plus the leaf level:

$$
T(n) = \sum_{i=0}^{\log_2 n - 1} cn + \Theta(n) = cn \log_2 n + \Theta(n) = \Theta(n \log n)
$$

---
### Lecture 2: Strong Induction, Master Theorem & Maximum Difference

#### 2.1 Proving Recurrence Bounds by Strong Induction

Recursion trees help us *guess* asymptotic bounds, while **strong induction** proves them rigorously for all integers $n$ (without assuming $n$ is a power of 2 and naturally handling floors, ceilings, and unequal splits).

##### Theorem 1: Merge-Sort Recurrence with Floors and Ceilings
Suppose $c > 0$, $T(1) > 0$, and for every integer $n \ge 2$:

$$
T(n) = T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + cn
$$

Then $T(n) = O(n \log n)$.

**Proof (Strong Induction):**
- **Inductive Hypothesis:** $T(m) \le K m \log_2 m$ for every integer $2 \le m < n$.
- **Base Cases ($m = 2, 3$):** Choose constant $K > 0$ large enough that $T(2) \le 2K \log_2 2$, $T(3) \le 3K \log_2 3$, and $K \log_2(3/2) \ge c$.
- **Inductive Step ($n \ge 4$):** Let $a = \lfloor n/2 \rfloor$ and $b = \lceil n/2 \rceil$. Then $a + b = n$, $2 \le a, b < n$, and crucially for all $n \ge 4$, both $a, b \le \frac{2n}{3}$. Applying the strong inductive hypothesis:

$$
\begin{aligned}
T(n) &\le K a \log_2 a + K b \log_2 b + cn
\\ &\le K (a + b) \log_2\left(\frac{2n}{3}\right) + cn
\\ &= K n \log_2 n + K n \log_2\left(\frac{2}{3}\right) + cn
\\ &= K n \log_2 n - \left(K \log_2(3/2) - c\right) n
\\ &\le K n \log_2 n
\end{aligned}
$$

*(Note: For the matching lower bound $T(n) = \Omega(n \log n)$, use $\lfloor n/2 \rfloor, \lceil n/2 \rceil \ge n/3$ for $n \ge 2$.)* $\square$

##### Theorem 2: Unequal-Split Selection Recurrence
Suppose $c > 0$, $T$ is bounded on constant-size inputs, and for all sufficiently large $n$:

$$
T(n) \le T(\lceil n/5 \rceil) + T(\lceil 7n/10 \rceil) + cn
$$

Then $T(n) = O(n)$.

**Proof (Strong Induction):**
- **Inductive Hypothesis:** $T(m) \le A m$ for all $1 \le m < n$.
- **Base Cases:** Pick $A \ge 20c$, and enlarge $A$ if needed so $T(m) \le Am$ holds for all small $m < n_0$ (where $n_0 = 40$ ensures $2A \le \frac{1}{20}An$ and $cn \le \frac{1}{20}An$).
- **Inductive Step ($n \ge n_0$):** Since $\lceil x \rceil < x + 1$, we have:

$$
\begin{aligned}
T(n) &\le A\lceil n/5 \rceil + A\lceil 7n/10 \rceil + cn
\\ &\le A\left(\frac{n}{5} + 1\right) + A\left(\frac{7n}{10} + 1\right) + cn
\\ &= \frac{9}{10} A n + 2A + cn
\\ &\le \frac{9}{10} A n + \frac{1}{20} A n + \frac{1}{20} A n = A n
\end{aligned}
$$

> **Why it works:** The subproblem fractions sum to $\frac{1}{5} + \frac{7}{10} = \frac{9}{10} < 1$. The "slack" $\frac{1}{10}An$ absorbs both the $cn$ linear work and the $+2A$ ceiling rounding overhead! $\square$

---

#### 2.2 The Master Theorem

For constants $a \ge 1$, $b > 1$, $d \ge 0$, and the recurrence $T(n) = aT(n/b) + \Theta(n^d)$ with $T(1) = \Theta(1)$:

$$
T(n) = \begin{cases}
\Theta(n^d) & \text{if } d > \log_b a \quad \text{(root work dominates: geometrically shrinking work per level)},
\\ \Theta(n^d \log n) & \text{if } d = \log_b a \quad \text{(balanced: equal } \Theta(n^d) \text{ work across all } \log_b n \text{ levels)},
\\ \Theta(n^{\log_b a}) & \text{if } d < \log_b a \quad \text{(leaf work dominates: geometrically growing work per level)}.
\end{cases}
$$

---

#### 2.3 Maximum Difference Problem: Enriching Recursive Return Values

- **Input:** Array $A[0..n-1]$ of numbers.
- **Goal:** Find indices $0 \le i \le j < n$ maximizing $A[i] - A[j]$ (the largest drop from an earlier element to a later element).
  - *Example:* For $A = [2, 5, 1, 7, 3, 2, 4, 6]$, the optimal drop is $A[3] - A[5] = 7 - 2 = 5$.

##### Approach 1: Return Only the Best Difference (Slow Combine)
Split $A$ into $A_{\text{left}}$ and $A_{\text{right}}$. The optimal pair $(i, j)$ either lies entirely in $A_{\text{left}}$, entirely in $A_{\text{right}}$, or crosses the midpoint ($i \in \text{left}, j \in \text{right}$), where the best crossing value is $\max(A_{\text{left}}) - \min(A_{\text{right}})$.
- If the recursive call returns *only* the best difference, we must scan $A_{\text{left}}$ and $A_{\text{right}}$ in $\Theta(n)$ time to find $\max(A_{\text{left}})$ and $\min(A_{\text{right}})$.
- Recurrence: $T(n) = 2T(n/2) + \Theta(n) \implies T(n) = \Theta(n \log n)$ (no faster than Merge Sort).

##### Approach 2: Strengthen the Recursive Return Triple (Fast $O(1)$ Combine)
Have each recursive call on subarray $A'$ return the **triple** $(\text{best}(A'), \max(A'), \min(A'))$:
1. **Base case ($n=1$):** Return $(0, A[0], A[0])$.
2. **Recurse:** Compute $(d_L, M_L, m_L)$ on $A_{\text{left}}$ and $(d_R, M_R, m_R)$ on $A_{\text{right}}$.
3. **Combine in $O(1)$ time:**

$$
d = \max\{d_L,\; d_R,\; M_L - m_R\}, \qquad M = \max\{M_L, M_R\}, \qquad m = \min\{m_L, m_R\}
$$

- **Runtime Analysis:** Now the combine step does $O(1)$ work! By the Master Theorem ($a=2, b=2, d=0 < \log_2 2 = 1$):

$$
T(n) = 2T(n/2) + O(1) \implies T(n) = \Theta(n^{\log_2 2}) = \Theta(n)
$$

---
### Lectures 2 & 3: Deterministic Linear-Time Selection (Median-of-Medians)

- **Input:** Array $A[0..n-1]$ of $n$ distinct numbers and a target rank $k \in \{1, 2, \dots, n\}$.
- **Goal:** Find the $k$-th smallest element (which has $k-1$ smaller elements and $n-k$ larger elements) in deterministic $O(n)$ worst-case time.

#### 3.1 Why Pivot Quality Matters
If we partition $A$ around a pivot $p$ into $L = \{x \in A : x < p\}$, $\{p\}$, and $G = \{x \in A : x > p\}$ in $O(n)$ time, we only need to recurse on one side:
- If $k \le |L|$, recurse on $L$ with rank $k$.
- If $k = |L| + 1$, return $p$.
- If $k > |L| + 1$, recurse on $G$ with rank $k - |L| - 1$.

If $p$ is chosen poorly (e.g., the minimum element), the recursive call has size $n-1$, giving $T(n) \le T(n-1) + cn = \Theta(n^2)$.
- **Definition (Good Pivot):** A pivot $p$ is **good** if both $|L| \le \frac{7}{10}n + O(1)$ and $|G| \le \frac{7}{10}n + O(1)$ (equivalently, at least $\frac{3}{10}n - O(1)$ elements are $\le p$ and at least $\frac{3}{10}n - O(1)$ elements are $\ge p$).

#### 3.2 The Median-of-Medians Algorithm (BFPRT)
1. **Group into 5s:** Partition $A$ into $\lceil n/5 \rceil$ groups of 5 elements each (plus at most one partial group).
2. **Find Group Medians:** Sort each 5-element group in $O(1)$ time (total $O(n)$ time) and extract its median $m_i$.
3. **Median of Medians:** Recursively call `Select` on the $\lceil n/5 \rceil$ group medians to find their exact median $p$. (Takes $T(\lceil n/5 \rceil)$ time.)
4. **Partition & Recurse:** Partition $A$ around $p$ into $L, \{p\}, G$ in $O(n)$ time and recurse on the side containing rank $k$ (at most $\frac{7}{10}n + O(1)$ elements).

#### 3.3 Visual Grid & Counting Proof for the $3n/10$ Bound

Imagine arranging the $n/5$ groups as columns of 5 elements sorted bottom-to-top, and ordering the columns left-to-right by their medians (this ordering is only for visualization):

```text
       Groups with median <= p       Pivot       Groups with median >= p
         (n/10 columns)              Group         (n/10 columns)

  [  o  ]   [  o  ]   ...   [  o  ]  [  *  ]  [  *  ]   ...   [  *  ]  <- top 2 in right
  [  o  ]   [  o  ]   ...   [  o  ]  [  *  ]  [  *  ]   ...   [  *  ]     half are >= p
  -------------------------------------------------------------------
  [ <=p ]   [ <=p ]   ...   [ <=p ]  [  p  ]  [ >=p ]   ...   [ >=p ]  <- Group Medians
  -------------------------------------------------------------------
  [  #  ]   [  #  ]   ...   [  #  ]  [  #  ]  [  o  ]   ...   [  o  ]  <- bottom 2 in left
  [  #  ]   [  #  ]   ...   [  #  ]  [  #  ]  [  o  ]   ...   [  o  ]     half are <= p

  Legend:
  [ * ] and [ >=p ] : At least 3 * (1/2)*(n/5) = 3n/10 elements are >= p  (thus |L| <= 7n/10)
  [ # ] and [ <=p ] : At least 3 * (1/2)*(n/5) = 3n/10 elements are <= p  (thus |G| <= 7n/10)
```

**Proof of Claim:**
- At least half of the $\lfloor n/5 \rfloor$ full group medians (i.e., $\ge \frac{1}{2} \cdot \frac{n}{5} = \frac{n}{10}$ groups, up to $O(1)$ rounding) are $\ge p$.
- In each of those groups, the group median and the 2 elements above it are all $\ge p$ (3 elements per group).
- Therefore, at least $3 \cdot \frac{1}{2} \cdot \frac{n}{5} = \frac{3n}{10}$ elements are $\ge p$, meaning $|L| \le \frac{7n}{10} + O(1)$.
- By symmetry, at least $\frac{3n}{10}$ elements are $\le p$, meaning $|G| \le \frac{7n}{10} + O(1)$.
- Thus $T(n) \le T(\lceil n/5 \rceil) + T(\lceil 7n/10 \rceil + O(1)) + cn = O(n)$ by Theorem 2. $\square$

> **Why Groups of 5?**
> - If we used **groups of 3**, each half-group contributes 2 elements, eliminating $\frac{2}{6}n = \frac{1}{3}n$, so the recursive sizes are $n/3$ and $2n/3$. Since $\frac{1}{3} + \frac{2}{3} = 1$, the recurrence $T(n) = T(n/3) + T(2n/3) + cn$ solves to $\Theta(n \log n)$, not $O(n)$!
> - **Groups of 5** is the smallest odd group size where $\frac{1}{g} + \left(1 - \frac{(g+1)/2}{2g}\right) < 1$ ($\frac{1}{5} + \frac{7}{10} = \frac{9}{10} < 1$).

---
## Module 2: Dynamic Programming, FPTAS & Markov Decision Processes (Lectures 3–5)

### Lecture 3: Dynamic Programming Recipe, Largest Contiguous Sum & LCS

#### 3.4 The 4-Step Dynamic Programming Design Recipe
Unlike Divide-and-Conquer (which solves independent subproblems), **Dynamic Programming (DP)** solves problems whose recursive breakdown repeatedly visits the **same overlapping subproblems**:
1. **Define Subproblems (State):** Specify in plain English what each table entry represents (including boundary constraints, such as "ending *exactly* at index $i$").
2. **Write the Recurrence (Bellman Equation):** Express each subproblem in terms of smaller subproblems by conditioning on the last local decision.
3. **Specify Base Cases & Evaluation Order:** Order the states so that all dependencies of a state are computed before the state itself.
4. **Extract Objective & Traceback:** Identify how to get the final answer from the table and how to reconstruct the optimal structure by following winning choices backward.

---

#### 3.5 Largest Contiguous Subarray Sum (Kadane's Algorithm)
- **Input:** Array $A[1..n]$ of real (possibly negative) numbers.
- **Goal:** Find indices $1 \le j \le i \le n$ maximizing $\sum_{k=j}^i A[k]$.
- **Why Naive Prefix DP Fails to Extend:** If we define $S[i]$ as the best contiguous sum *anywhere* in $A[1..i]$, we cannot extend $S[i-1]$ by adding $A[i]$ unless the optimal subarray in $A[1..i-1]$ actually ends at index $i-1$.
- **Correct Subproblem Definition:** Let $M[i]$ be the maximum sum of a contiguous subarray that **ends at index $i$**:

$$
M[i] = \max_{1 \le j \le i} \sum_{k=j}^i A[k]
$$

- **Recurrence:** An optimal subarray ending at $i$ either starts fresh at $i$ ($j=i$) or extends an optimal subarray ending at $i-1$ ($j \le i-1$):

$$
M[1] = A[1], \qquad M[i] = \max\{\, A[i],\; A[i] + M[i-1] \,\} \quad \text{for } i = 2, \dots, n
$$

- **Final Answer:** $\text{OPT} = \max_{1 \le i \le n} M[i]$.
- **Endpoint Recovery:** Let $i^* = \arg\max_{1 \le i \le n} M[i]$. Maintain $L[i]$ (start index): set $L[i] = i$ when $A[i] \ge A[i] + M[i-1]$, and $L[i] = L[i-1]$ when $A[i] + M[i-1] > A[i]$.
- **Worked Trace on Lecture 3 Example:** $A = [5, 15, -30, 10, -5, 40, 10]$

| Index $i$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$A[i]$** | $5$ | $15$ | $-30$ | $10$ | $-5$ | $40$ | $10$ |
| **$M[i]$** | $5$ | $20$ | $-10$ | $10$ | $5$ | $45$ | **$55$** |
| **Start $L[i]$** | $1$ | $1$ | $1$ | $4$ | $4$ | $4$ | **$4$** |

Maximum sum is $M[7] = 55$, achieved by subarray $A[4..7] = [10, -5, 40, 10]$.
- **Complexity:** $O(n)$ time and $O(n)$ space (or $O(1)$ auxiliary space by keeping only the previous value $M[i-1]$ and running best).

---

#### 3.6 Longest Common Subsequence (LCS)
- **Input:** Two strings $A = a_1 a_2 \dots a_n$ and $B = b_1 b_2 \dots b_m$.
- **Goal:** Find the length (and sequence) of the longest sequence that appears left-to-right (not necessarily contiguously) in both $A$ and $B$.
- **Subproblem State:** For $0 \le i \le n$ and $0 \le j \le m$, let $D[i, j]$ be the length of the LCS of prefixes $A_{1..i}$ and $B_{1..j}$.
- **Base Cases:** $D[i, 0] = 0$ for all $0 \le i \le n$, and $D[0, j] = 0$ for all $0 \le j \le m$.
- **Recurrence (for $i, j \ge 1$):**

$$
D[i, j] = \begin{cases}
1 + D[i-1, j-1] & \text{if } a_i = b_j,
\\ \max\{\, D[i-1, j],\; D[i, j-1] \,\} & \text{if } a_i \neq b_j.
\end{cases}
$$

- **Correctness Proof (Case Analysis on Last Characters $a_i, b_j$):**
  1. *If $a_i = b_j$:* Some optimal LCS of $A_{1..i}$ and $B_{1..j}$ pairs $a_i$ with $b_j$; removing this common final character leaves an LCS of $A_{1..i-1}$ and $B_{1..j-1}$ of length $D[i-1, j-1]$.
  2. *If $a_i \neq b_j$:* No common subsequence can use both $a_i$ and $b_j$ as its final character, so any LCS of $A_{1..i}$ and $B_{1..j}$ is either contained in $A_{1..i-1}$ vs. $B_{1..j}$ (length $\le D[i-1, j]$) or in $A_{1..i}$ vs. $B_{1..j-1}$ (length $\le D[i, j-1]$).
- **Traceback & Complexity:** Start at $(n, m)$. If $a_i = b_j$, output $a_i$ and move diagonally to $(i-1, j-1)$; otherwise move to whichever of $(i-1, j)$ or $(i, j-1)$ has the larger table value.
  - **Time:** $O(nm)$ to fill $(n+1)(m+1)$ cells in $O(1)$ per cell, plus $O(n+m)$ for traceback. **Space:** $O(nm)$.

**Worked Example (Lectures 3 & 4):** $A = \text{ABCDEFG}$ ($n=7$), $B = \text{BCDGKAB}$ ($m=7$).
- Optimal LCS has length $D[7, 7] = 4$, corresponding to `BCDG`.

---
### Lecture 4: Tree DP (Maximum Independent Set) & 0-1 Knapsack

#### 4.1 Maximum Independent Set (MIS) on a Tree
- **Input:** An undirected tree $T = (V, E)$.
- **Goal:** Find a maximum-cardinality subset $S \subseteq V$ containing no two adjacent vertices ($\forall (u, v) \in E,\; \{u, v\} \not\subseteq S$).
  - *(General graphs: MIS is NP-hard, but on trees removing a vertex splits the tree into independent subtrees!)*
- **Rooting the Tree:** Pick an arbitrary root $r \in V$. For each vertex $v$, let $T_v$ be the subtree rooted at $v$, $C(v)$ be the children of $v$, and $G(v) = \bigcup_{u \in C(v)} C(u)$ be the grandchildren of $v$.

##### Formulation A (1-State Subtree DP)
- **Subproblem:** Let $M[v]$ be the size of the maximum independent set in $T_v$.
- **Recurrence:** Either $v \notin S$ (we can independently pick the best MIS in each child subtree $T_u$) or $v \in S$ (no child $u \in C(v)$ can be picked, so we pick the best MIS in each grandchild subtree $T_w$):

$$
M[v] = \max\left\{\, \sum_{u \in C(v)} M[u],\; 1 + \sum_{w \in G(v)} M[w] \,\right\}
$$

- **Base Case:** If $v$ is a leaf ($C(v) = \emptyset$), $M[v] = 1$.

##### Formulation B (2-State Include/Exclude DP)
- **Subproblems:** Let $I[v]$ be the max independent set size in $T_v$ **including** $v$, and $X[v]$ be the max independent set size in $T_v$ **excluding** $v$.
- **Recurrences:**

$$
I[v] = 1 + \sum_{u \in C(v)} X[u], \qquad X[v] = \sum_{u \in C(v)} \max\{I[u], X[u]\}, \qquad M[v] = \max\{I[v], X[v]\}
$$

- **Evaluation Order & Runtime:** Process vertices in **bottom-up postorder** (leaves to root $r$). Each vertex $v$ sums over its children (and grandchildren), so each edge is touched $O(1)$ times:

$$
\text{Time} = O\left(\sum_{v \in V} (1 + \deg(v))\right) = O(|V|), \qquad \text{Space} = O(|V|)
$$

---

#### 4.2 0-1 Knapsack & Pseudo-Polynomial Time
- **Input:** $n$ items with integer sizes $s_1, \dots, s_n \in \mathbb{Z}_{>0}$, integer values $v_1, \dots, v_n \in \mathbb{Z}_{>0}$, and knapsack capacity $B \in \mathbb{Z}_{>0}$.
- **Goal:** Choose a subset $S \subseteq \{1, \dots, n\}$ with $\sum_{i \in S} s_i \le B$ maximizing $\sum_{i \in S} v_i$.

##### Two Dual DP Formulations for 0-1 Knapsack

| Feature | Capacity-Indexed DP | Value-Indexed DP (Used for FPTAS) |
| :--- | :--- | :--- |
| **State Definition** | $K[i, b]$ = max value using a subset of $\{1..i\}$ with total size $\le b$ | $D[i, v]$ = **minimum total size** of a subset of $\{1..i\}$ achieving **exact** value $v$ |
| **Index Ranges** | $0 \le i \le n$, $0 \le b \le B$ | $0 \le i \le n$, $0 \le v \le V_{\text{sum}} = \sum_{k=1}^n v_k \le n V_{\max}$ |
| **Base Cases** | $K[0, b] = 0$ for all $0 \le b \le B$ | $D[0, 0] = 0$, and $D[0, v] = +\infty$ for all $v > 0$ |
| **Recurrence** | $K[i, b] = \max\{K[i-1, b],\; v_i + K[i-1, b-s_i]\}$ (if $s_i \le b$) | $D[i, v] = \min\{D[i-1, v],\; s_i + D[i-1, v-v_i]\}$ (if $v_i \le v$) |
| **Answer Extraction** | $\text{OPT} = K[n, B]$ | $\text{OPT} = \max\{v \in [0, V_{\text{sum}}] : D[n, v] \le B\}$ |
| **Running Time** | $O(nB)$ | $O(n V_{\text{sum}}) = O(n^2 V_{\max})$ |

**Worked Example (Lecture 4):** Items $(s_1, v_1) = (6, 30)$, $(s_2, v_2) = (3, 14)$, $(s_3, v_3) = (4, 16)$, $(s_4, v_4) = (2, 9)$, capacity $B = 10$.
- Feasible exact values at row $i=4$ with $D[4, v] \le 10$:
  - $D[4, 44] = s_1 + s_2 = 6 + 3 = 9 \le 10$ (items $\{1, 2\}$)
  - $D[4, 46] = s_1 + s_3 = 6 + 4 = 10 \le 10$ (items $\{1, 3\}$)
  - $D[4, 48] = s_1 + s_2 + s_4 = 6 + 3 + 2 = 11 > 10$ (infeasible!)
- Largest $v$ with $D[4, v] \le 10$ is $\text{OPT} = 46$ (items $\{1, 3\}$).

##### Why Both DPs Are Pseudo-Polynomial (Not Polynomial)
In complexity theory, an input integer $X$ is encoded in binary using $\ell = \Theta(\log_2 X)$ bits, so $X = \Theta(2^\ell)$ is **exponential** in its bit length:
- $O(nB) = O(n \cdot 2^{\log_2 B})$ is exponential in $\log_2 B$.
- $O(n^2 V_{\max}) = O(n^2 \cdot 2^{\log_2 V_{\max}})$ is exponential in $\log_2 V_{\max}$.
An algorithm whose runtime is polynomial in the *numerical magnitude* of input integers (unary encoding) rather than their *bit length* (binary encoding) is called **pseudo-polynomial**.

---
### Lectures 4 & 5: Knapsack FPTAS via Value Scaling

#### 4.3 PTAS vs. FPTAS Definitions
For a maximization problem with optimal value $\text{OPT}$ and error parameter $\varepsilon \in (0, 1)$:
- **$(1 - \varepsilon)$-Approximation Algorithm:** Always outputs a feasible solution with value $\text{ALG} \ge (1 - \varepsilon)\text{OPT}$.
- **PTAS (Polynomial-Time Approximation Scheme):** For every fixed $\varepsilon > 0$, runs in time polynomial in input bit-size (e.g., $O(n^{1/\varepsilon})$ is a PTAS, though not polynomial in $1/\varepsilon$).
- **FPTAS (Fully Polynomial-Time Approximation Scheme):** Runs in time polynomial in **both** the input bit-size **and** $1/\varepsilon$ (e.g., $O(n^3/\varepsilon)$).

#### 4.4 The Knapsack Value-Scaling Algorithm (`Knapsack-FPTAS`)
**Core Idea:** Since the value-indexed DP runs in $O(n^2 V_{\max})$ time, we can make $V_{\max}$ small ($O(n/\varepsilon)$) by rounding down item values to multiples of a scaling unit $K$:
1. Remove any item with $s_i > B$. Let $V_{\max} = \max_{1 \le i \le n} v_i$.
2. Define the **scaling factor** and **rounded values**:

$$
K = \frac{\varepsilon V_{\max}}{n}, \qquad \hat{v}_i = \left\lfloor \frac{v_i}{K} \right\rfloor \quad \text{for } i = 1, \dots, n
$$

3. Run the **exact value-indexed Knapsack DP** using original sizes $s_i$, capacity $B$, and scaled integer values $\hat{v}_i$.
4. Return the item subset $\hat{S}$ that achieves the maximum scaled value.

#### 4.5 Complete Proof of Runtime and $(1-\varepsilon)$-Approximation Guarantee

**1. Running Time is $O(n^3/\varepsilon)$ (Fully Polynomial):**
Each scaled value satisfies $\hat{v}_i = \lfloor v_i / K \rfloor \le \frac{V_{\max}}{\varepsilon V_{\max} / n} = \frac{n}{\varepsilon}$, so the maximum possible scaled sum is:

$$
\hat{V}_{\text{sum}} = \sum_{i=1}^n \hat{v}_i \le n \cdot \frac{n}{\varepsilon} = \frac{n^2}{\varepsilon}
$$

Running the value-indexed DP on $n$ items and $\hat{V}_{\text{sum}} + 1$ value columns takes:

$$
\text{Time} = O(n \cdot \hat{V}_{\text{sum}}) = O\left(\frac{n^3}{\varepsilon}\right)
$$

**2. Approximation Proof ($v(\hat{S}) \ge (1-\varepsilon)\text{OPT}$):**
Let $S^*$ be an optimal subset for the original values ($\text{OPT} = \sum_{i \in S^*} v_i$) and $\hat{S}$ be the subset output by the scaled DP.
- For every item $i$, properties of the floor function $\frac{v_i}{K} - 1 \le \lfloor \frac{v_i}{K} \rfloor \le \frac{v_i}{K}$ imply:

$$
v_i - K \le K \hat{v}_i \le v_i
$$

- Because $\hat{S}$ is optimal for the scaled instance $\hat{v}$ and $S^*$ is also a feasible subset ($\sum_{i \in S^*} s_i \le B$), we have $\sum_{i \in \hat{S}} \hat{v}_i \ge \sum_{i \in S^*} \hat{v}_i$.
- Chaining these inequalities together:

$$
\begin{aligned}
v(\hat{S}) = \sum_{i \in \hat{S}} v_i &\ge \sum_{i \in \hat{S}} K \hat{v}_i && \text{(since } v_i \ge K \hat{v}_i\text{)}
\\ &\ge \sum_{i \in S^*} K \hat{v}_i && \text{(by optimality of } \hat{S} \text{ for } \hat{v}\text{)}
\\ &\ge \sum_{i \in S^*} (v_i - K) && \text{(since } K \hat{v}_i \ge v_i - K\text{)}
\\ &= \text{OPT} - |S^*| K
\\ &\ge \text{OPT} - n K && \text{(since } |S^*| \le n\text{)}
\\ &= \text{OPT} - \varepsilon V_{\max} && \text{(since } K = \varepsilon V_{\max}/n\text{)}
\\ &\ge (1 - \varepsilon)\text{OPT} && \text{(since single best item } V_{\max} \le \text{OPT}\text{).} \quad \square
\end{aligned}
$$

> **Why we round VALUES, not SIZES:** Rounding item sizes $s_i$ could cause a subset that looks feasible in the rounded table to **violate the hard capacity constraint** $\sum_{i \in \hat{S}} s_i \le B$. Rounding values preserves exact capacity feasibility while losing at most $K$ value per item ($\le nK = \varepsilon V_{\max}$ total).

---
### Lecture 5: Finite-Horizon Markov Decision Processes (MDPs)

#### 5.1 Formal MDP Model
A finite-horizon Markov Decision Process models sequential decision-making under known transition probabilities:
1. **State Space $S$:** Finite set of environment configurations.
2. **Action Space $A$:** Finite set of actions available at each step.
3. **Transition Kernel $p_a(s, s')$:** Probability of moving from state $s$ to state $s'$ when taking action $a$, satisfying $\sum_{s' \in S} p_a(s, s') = 1$.
4. **Immediate Reward $r_a(s) \in \mathbb{R}$:** Immediate reward earned upon taking action $a$ in state $s$.
5. **Horizon $T \in \mathbb{Z}_{\ge 0}$:** Total number of decision steps remaining.

#### 5.2 Two Foundational Lecture 5 Examples

##### Example 1: Optimal Action Depends on Remaining Horizon $T$

```text
          a1: reward 0               a1/a2: reward 2 (absorbing)
  ( s1 ) --------------> ( s2 ) -----\
   |  ^                              | (self-loop: +2 per step)
   \__/                              v
  a2: reward 1                     ( s2 )
```

Starting at $s_1$:
- **$T = 1$ step left:** Action $a_2$ gives $1$; action $a_1$ gives $0$. Optimal first action is **$a_2$** (total reward $1$).
- **$T = 2$ steps left:** Playing $a_2$ twice gives $1 + 1 = 2$; playing $a_1$ then $a_1$ gives $0 + 2 = 2$. Both tie at $2$.
- **$T = 3$ steps left:** Playing $a_2$ three times gives $1 + 1 + 1 = 3$; playing $a_1$ to reach $s_2$ and then collecting $+2$ twice gives $0 + 2 + 2 = 4$. Optimal first action is **$a_1$**!
- **Takeaway:** A policy in a finite-horizon MDP must be indexed by **both current state $s$ and remaining steps $t$**: $\pi = (\pi_t)_{t=1}^T$.

##### Example 2: Stochastic Transitions & Expected Value
From $s_1$ with $T = 2$ steps left (initial reward $0$ at step 1):
- **Action $a_1$ (Lottery):** Goes to $s_2$ (reward $2$) with probability $0.5$ and to $s_3$ (reward $0$) with probability $0.5$. Expected total reward = $0 + 0.5(2) + 0.5(0) = 1.0$.
- **Action $a_2$ (Safe):** Deterministically goes to $s_4$ (reward $1.5$). Expected total reward = $0 + 1(1.5) = 1.5$.
- **Takeaway:** Even though $s_2$ has the highest individual state reward ($2$), maximizing **expected** cumulative reward selects $a_2$ ($1.5 > 1.0$).

#### 5.3 The Bellman Optimality Equation & DP Algorithm
- **Subproblem State:** For every $s \in S$ and remaining horizon $t \in \{0, 1, \dots, T\}$, let $V^*(s, t)$ be the maximum expected reward achievable starting from state $s$ with $t$ steps remaining.
- **Base Case ($t = 0$):**

$$
V^*(s, 0) = 0 \quad \forall s \in S
$$

- **Bellman Optimality Recurrence ($t = 1, \dots, T$):** By linearity of expectation and the Markov property (future transitions depend only on the next state $s'$ and the $t-1$ steps left, not past history):

$$
V^*(s, t) = \max_{a \in A} \left\{\, r_a(s) + \sum_{s' \in S} p_a(s, s')\, V^*(s', t-1) \,\right\}
$$

- **Optimal Policy Recovery:** Record the maximizing action at each cell:

$$
\pi^*(s, t) \in \arg\max_{a \in A} \left\{\, r_a(s) + \sum_{s' \in S} p_a(s, s')\, V^*(s', t-1) \,\right\}
$$

- **Structural Consequence:** There always exists an optimal policy that is **deterministic** and **Markovian** (depends only on $(s, t)$, never needing randomization or full history).
- **Complexity:**
  - **Table cells:** $(T+1)|S|$.
  - **Work per cell $(s, t)$:** Evaluates $|A|$ actions, each summing over $|S|$ next states $\implies O(|A||S|)$.
  - **Total Time:** $O(T |A| |S|^2)$. **Total Space:** $O(T|S|)$ (or $O(|S|)$ if only values are needed).

---
## Module 3: Graph Algorithms — Search, Shortest Paths, MSTs, Matchings & Max-Flow (Lectures 6–8)

### Lecture 6: Graph Representations, BFS, Dijkstra's Algorithm & MST Cut Property

#### 6.1 Graph Basics & Representations
Let $G = (V, E)$ with $n = |V|$ vertices and $m = |E|$ edges.
- **Handshaking Lemma (Undirected Graphs):** Every edge $\{u, v\}$ contributes $1$ to $\deg(u)$ and $1$ to $\deg(v)$:

$$
\sum_{v \in V} \deg(v) = 2m \quad \text{(and for directed graphs, } \sum_{v \in V} \deg^{\text{out}}(v) = \sum_{v \in V} \deg^{\text{in}}(v) = m\text{)}
$$

| Operation / Resource | Adjacency Matrix ($n \times n$ array $A[u,v]$) | Adjacency Lists ($\text{Adj}[u]$ list of neighbors) |
| :--- | :--- | :--- |
| **Space Complexity** | $\Theta(n^2)$ | $\Theta(n + m)$ |
| **Check if edge $(u, v) \in E$** | $O(1)$ | $O(\deg(u))$ |
| **Iterate over neighbors of $u$** | $\Theta(n)$ | $\Theta(\deg(u))$ |
| **Full Graph Traversal** | $\Theta(n^2)$ | $\Theta(n + m)$ (vastly faster on sparse graphs $m \ll n^2$) |

---

#### 6.2 Breadth-First Search (BFS) for Unweighted Shortest Paths
- **Algorithm:** Initialize `dist[s] = 0`, `dist[v] = +inf` for $v \neq s$, and push $s$ into a FIFO queue $Q$. While $Q$ is non-empty, pop $u$; for each neighbor $v \in \text{Adj}[u]$, if `dist[v] == +inf`, set `dist[v] = dist[u] + 1`, `parent[v] = u`, and push $v$ to $Q$.
- **Layer Invariant:** BFS discovers vertices in nondecreasing distance layers $L_k = \{v \in V : \text{dist}_G(s, v) = k\}$:

```text
Layer L_0          Layer L_1          Layer L_2          Layer L_3
  [ s ] ---------> [ a ] ---------> [ c ] ---------> [ e ]
    |                |                ^
    +------------> [ b ] -------------+
  dist = 0           dist = 1           dist = 2           dist = 3
```

- **Correctness Proof (Induction on distance $k$):** Suppose $L_0, \dots, L_k$ are popped in layer order with exact `dist` values. Every $v \in L_{k+1}$ has no edge from $L_{<k}$ (by definition of shortest path) and at least one edge $(u, v)$ from some $u \in L_k$. When the first such $u \in L_k$ is popped, `dist[v]` is set to $k+1$ and $v$ is enqueued after all remaining $L_k$ vertices.
- **Running Time:** Each vertex is enqueued/dequeued at most once ($O(n)$), and each adjacency list is scanned at most once ($\sum_u \deg(u) = O(m)$), giving **$O(n + m)$ time and $O(n)$ space**.

---

#### 6.3 Nonnegative Weighted Shortest Paths & Dijkstra's Algorithm
- **Why Unit-Edge Expansion is Only Pseudo-Polynomial:** Replacing each integer-weight edge $w_e$ by a path of $w_e$ unit edges and running BFS takes $O(n + \sum_e w_e) = O(n + m W)$ time, which is **pseudo-polynomial** (exponential in $\log_2 W$).
- **Dijkstra's Algorithm ($w_e \ge 0$):**
  Maintain tentative distances $d[v]$ ($d[s]=0, d[v]=\infty$ for $v \neq s$) and a settled set $R$ (initially $\emptyset$). At each step, extract unsettled $u \notin R$ minimizing $d[u]$, add $u$ to $R$, and **relax** all outgoing edges $(u, v) \in E$:

$$
\text{if } d[u] + w(u, v) < d[v] \text{ then set } d[v] \leftarrow d[u] + w(u, v), \;\text{parent}[v] \leftarrow u
$$

- **Correctness Proof (Induction on $|R|$):**
  Suppose all $x \in R$ have $d[x] = \text{dist}(s, x)$, and let $u \notin R$ be extracted with minimum $d[u]$. Let $P^*$ be a true shortest $s \to u$ path, and let $(x, y)$ be the **first edge on $P^*$ that exits $R$** ($x \in R, y \notin R$):

```text
   Settled Set R                        Unsettled V \ R
  +-------------------+
  |  [ s ] ~~> [ x ] -|-----(x, y)-----> [ y ] ~~(w >= 0)~~> [ u ]
  +-------------------+
```

  1. Because $x \in R$, by induction $d[x] = \text{dist}(s, x)$, and when $x$ was settled, edge $(x, y)$ was relaxed, so $d[y] \le \text{dist}(s, x) + w(x, y) = \text{dist}(s, y)$.
  2. Since $y \notin R$ and Dijkstra picked $u \notin R$ with minimum key, $d[u] \le d[y]$.
  3. Since **all remaining edges on $P^*$ from $y$ to $u$ have nonnegative weight $w_e \ge 0$**, $\text{dist}(s, y) \le \text{dist}(s, u)$.
  4. Chaining: $d[u] \le d[y] \le \text{dist}(s, y) \le \text{dist}(s, u) \le d[u] \implies d[u] = \text{dist}(s, u)$. $\square$

- **Where Negative Edges Break Dijkstra:** Consider $s \xrightarrow{2} a$, $s \xrightarrow{3} b$, $b \xrightarrow{-2} a$. Dijkstra settles $a$ first with $d[a]=2$, missing the path $s \to b \to a$ of length $3 + (-2) = 1$ because step (3) fails when $w(b,a) < 0$.
- **Priority Queue Complexity ($n$ `Extract-Min` + $m$ `Decrease-Key`):**
  - **Binary Heap:** $O((n + m)\log n)$ time.
  - **Fibonacci Heap:** $O(m + n \log n)$ time.
  - *(Modern frontiers mentioned in Lecture 6: Duan et al. deterministic $O(m \log^{2/3} n)$ comparison-addition shortest paths; Bernstein-Nanongkai-Wulff-Nilsen near-linear negative-weight shortest paths.)*

---

#### 6.4 Minimum Spanning Trees (MST) & The Cut Property
- **Problem:** Given connected undirected $G = (V, E)$ with edge weights $w_e \in \mathbb{R}$, find a spanning tree $T \subseteq E$ ($|T| = n-1$, connected, acyclic) minimizing $w(T) = \sum_{e \in T} w_e$.
- **Theorem (Cut Property):** Let $\emptyset \subsetneq S \subsetneq V$ be any cut, and let $e^* = \{u, v\} \in \delta(S)$ be a minimum-weight edge crossing the cut ($w(e^*) = \min_{e \in \delta(S)} w(e)$). If weights are distinct, $e^*$ belongs to every MST; in general, given any forest $F \subseteq T^*$ for some MST $T^*$ with $F \cap \delta(S) = \emptyset$, there exists an MST $\tilde{T}$ containing $F \cup \{e^*\}$.
- **Exchange Proof:** If $e^* \notin T^*$, adding $e^*$ to $T^*$ creates a unique fundamental cycle $C$. Since $e^*$ crosses $(S, V \setminus S)$, the cycle $C$ must cross back across $(S, V \setminus S)$ on at least one other edge $e' \in C \cap \delta(S)$ (with $e' \notin F$). Swapping $e^*$ for $e'$ yields a spanning tree $\tilde{T} = (T^* \setminus \{e'\}) \cup \{e^*\}$ with weight $w(\tilde{T}) = w(T^*) + w(e^*) - w(e') \le w(T^*)$. Since $T^*$ was an MST, $\tilde{T}$ is also an MST containing $F \cup \{e^*\}$. $\square$

---
### Lecture 7: Prim's MST Algorithm, Matchings & Berge's Theorem

#### 7.1 Prim's Algorithm for Minimum Spanning Tree
- **Algorithm:** Start with an arbitrary root $s \in V$, set $S = \{s\}$ and $T = \emptyset$. In each of $n-1$ iterations, pick a minimum-weight edge $e = \{u, v\} \in \delta(S)$ with $u \in S, v \notin S$, add $v$ to $S$, and add $e$ to $T$.
- **Why Tie-Breaking Requires a Global Invariant:** On a triangle $K_3$ with all edge weights equal to $1$, every edge is a minimum-weight edge across some cut, yet picking all three edges forms a cycle! Thus we maintain the **Global Invariant**: *At the end of every step, the chosen edge set $T$ is contained in at least one MST $T^*$ of $G$ ($T \subseteq T^*$)*.
- **Exchange Proof Preserving $T \subseteq T^*$:**
  Suppose $T \subseteq T^*$ holds before adding $e = \{u, v\} \in \delta(S)$. If $e \in T^*$, then $T \cup \{e\} \subseteq T^*$ immediately. Otherwise, adding $e$ to $T^*$ creates a unique cycle $C \subseteq T^* \cup \{e\}$. Since $e$ has one endpoint in $S$ and one in $V \setminus S$, the path $C \setminus \{e\} \subseteq T^*$ must cross the cut $(S, V \setminus S)$ on some other edge $e' \in C \cap \delta(S)$.
  - Because all edges of $T$ have *both* endpoints inside $S$, $T \cap \delta(S) = \emptyset$, so $e' \notin T$.
  - Because Prim chose $e$ as a minimum-weight edge in $\delta(S)$, $w(e) \le w(e')$.
  - Therefore $T' = (T^* \setminus \{e'\}) \cup \{e\}$ is a spanning tree with $w(T') = w(T^*) + w(e) - w(e') \le w(T^*)$, so $T'$ is an MST and $T \cup \{e\} \subseteq T'$. $\square$
- **Priority Queue Implementation:** For each $v \notin S$, maintain $\text{key}[v] = \min_{u \in S} w(u, v)$ and $\text{parent}[v] = \arg\min_{u \in S} w(u, v)$. Performing $n$ `Extract-Min` and at most $2m$ `Decrease-Key` operations takes **$O(m \log n)$ time with a binary heap** (or $O(m + n \log n)$ with a Fibonacci heap).

---

#### 7.2 Matchings, Alternating Paths & Berge's Theorem
- **Definitions:**
  - A **matching** $M \subseteq E$ is a set of edges sharing no common vertices ($\forall v \in V$, at most one edge of $M$ is incident to $v$).
  - **Maximal matching:** No edge $e \in E \setminus M$ can be added without violating the matching property. (Can be half the size of OPT: on path $a-b-c-d$, $M = \{\{b,c\}\}$ has size $1$, whereas $M^* = \{\{a,b\}, \{c,d\}\}$ has size $2$.)
  - **Maximum matching:** Matching of maximum cardinality $|M|$ over all matchings in $G$.
  - **Perfect matching:** Matching that saturates every vertex ($|M| = n/2$).
  - **$M$-Alternating path:** Simple path whose edges alternate between $E \setminus M$ and $M$.
  - **$M$-Augmenting path:** An $M$-alternating path whose **both endpoints are unmatched (free)** under $M$.

```text
  M-Augmenting Path P (=== is in M, --- is in E \ M):
  [free u1] --- (v1) === (u2) --- (v2) === (u3) --- [free v3]

  Flip P via Symmetric Difference M' = M (+) P:
  (u1) === (v1) --- (u2) === (v2) --- (u3) === (v3)   (|M'| = |M| + 1)
```

##### Theorem (Berge's Theorem)
A matching $M$ in an undirected graph $G$ is a **maximum matching** if and only if $G$ contains **no $M$-augmenting path**.

**Proof:**
- **$(\Rightarrow)$ If an $M$-augmenting path $P$ exists, $M$ is not maximum:** Let $M' = M \oplus P = (M \setminus P) \cup (P \setminus M)$. Since $P$ starts and ends on unmatched edges and alternates, $P$ has $k+1$ edges in $E \setminus M$ and $k$ edges in $M$. Every internal vertex of $P$ keeps degree $1$ in $M'$, and the two free endpoints gain degree $1$ in $M'$. Thus $M'$ is a valid matching with $|M'| = |M| + 1$.
- **$(\Leftarrow)$ If $|M^*| > |M|$, then an $M$-augmenting path exists:** Consider the symmetric difference subgraph $H = (V, M \oplus M^*)$. Since each vertex has degree $\le 1$ in $M$ and $\le 1$ in $M^*$, every vertex has **degree $\le 2$ in $H$**. Thus every connected component of $H$ is an isolated vertex, an alternating even cycle (equal number of $M$ and $M^*$ edges), or an alternating path. Since $|M^* \setminus M| > |M \setminus M^*|$, at least one component must have strictly more $M^*$ edges than $M$ edges; this component must be an alternating path that starts and ends with edges of $M^* \setminus M$, which is an $M$-augmenting path! $\square$

---

#### 7.3 Bipartite Maximum Matching via Directed Alternating Search
In a bipartite graph $G = (L \cup R, E)$ (which has no odd cycles):
1. Orient all **unmatched edges** $e \in E \setminus M$ from $L \to R$, and orient all **matched edges** $e \in M$ from $R \to L$.
2. Let $L_{\text{free}} \subseteq L$ and $R_{\text{free}} \subseteq R$ be the unmatched vertices.
3. Run BFS/DFS from $L_{\text{free}}$ in this directed graph: a directed path from $L_{\text{free}}$ to $R_{\text{free}}$ is **precisely an $M$-augmenting path**!
4. Each augmentation takes $O(n + m)$ time and increases $|M|$ by $1$; since $|M^*| \le n/2$, total runtime is **$O(n(n+m)) = O(nm)$**.

---
### Lecture 8: Maximum Flow, Residual Networks, Ford-Fulkerson & Max-Flow Min-Cut

#### 8.1 Flow Networks & Reduction from Bipartite Matching
- **Flow Network:** Directed graph $G = (V, E)$ with source $s \in V$, sink $t \in V$, and capacities $c_e \ge 0$. An **$s$-$t$ flow** $f : E \to \mathbb{R}_{\ge 0}$ satisfies:
  1. **Capacity Constraint:** $0 \le f_e \le c_e$ for all $e \in E$.
  2. **Flow Conservation:** $\sum_{e \in \delta^{\text{in}}(v)} f_e = \sum_{e \in \delta^{\text{out}}(v)} f_e$ for all $v \in V \setminus \{s, t\}$.
- **Flow Value:** $|f| = \sum_{e \in \delta^{\text{out}}(s)} f_e - \sum_{e \in \delta^{\text{in}}(s)} f_e$.
- **Bipartite Matching $\le_P$ Max-Flow:** Add source $s$ with unit-capacity edges $(s, u)$ for all $u \in L$, orient original edges $u \to v$ ($u \in L, v \in R$) with capacity $1$, and add sink $t$ with unit-capacity edges $(v, t)$ for all $v \in R$. An **integral** flow $f \in \{0, 1\}^E$ of value $k$ corresponds bijectively to a matching $M = \{(u, v) \in E : f_{uv} = 1\}$ of size $k$.

---

#### 8.2 Why Naive Greedy Path Packing Fails & The Residual Network $G_f$
Consider the 4-vertex diamond network with all capacities equal to $1$:

```text
           ( u )
         1/  |  \1
        /    |1   \
  ( s )      v     ( t )
        \    |    /
         1\  |  /1
           ( v )
```

- If a naive greedy step sends $1$ unit along $s \to u \to v \to t$, no capacity remains in the original graph, getting stuck at flow $1$.
- Yet the true maximum flow is **$2$** (along $s \to u \to t$ and $s \to v \to t$). We need a way to **undo/redirect** the flow on $(u, v)$!

##### Definition (Residual Network $G_f$)
Given flow $f$, for each original edge $e = (u, v) \in E$, the residual network $G_f = (V, E_f)$ includes:
- **Forward residual edge $(u, v)$** with residual capacity $c_f(u, v) = c_{uv} - f_{uv}$ (if $c_{uv} - f_{uv} > 0$: unused capacity).
- **Backward residual edge $(v, u)$** with residual capacity $c_f(v, u) = f_{uv}$ (if $f_{uv} > 0$: allows canceling previously sent flow).

##### Augmentation Step
Given any simple $s \to t$ path $P$ in $G_f$ with **bottleneck capacity** $\Delta = \min_{e \in P} c_f(e) > 0$, update $f$ to $f'$:
- If $(u, v) \in P$ is a forward edge, set $f'_{uv} = f_{uv} + \Delta$.
- If $(v, u) \in P$ is a backward edge, set $f'_{uv} = f_{uv} - \Delta$.
Then $f'$ is a valid flow with $|f'| = |f| + \Delta$.

---

#### 8.3 Ford-Fulkerson, Integrality & Edmonds-Karp
- **Ford-Fulkerson Algorithm:** Start with $f = 0$. While there exists an $s \to t$ path $P$ in $G_f$ (found via DFS/BFS), augment $f$ along $P$.
- **Integrality Theorem:** If all capacities $c_e$ are integers, then in every iteration $\Delta \ge 1$ is an integer, so Ford-Fulkerson terminates in at most $|f^*|$ augmentations and outputs an **integral maximum flow** in time:

$$
O((n + m)(1 + |f^*|)) \quad \text{(pseudo-polynomial in } \log_2 C\text{)}
$$

- **Edmonds-Karp Algorithm:** Always augment along a **shortest $s \to t$ path in $G_f$ (fewest edges, found via BFS)**. Runs in strongly polynomial time $O(nm^2)$ even for irrational capacities.

---

#### 8.4 Directed $s$-$t$ Cuts & The Max-Flow Min-Cut Theorem
- **$s$-$t$ Cut:** A partition $(X, V \setminus X)$ with $s \in X$ and $t \notin X$. Its **capacity** counts **only outgoing edges** from $X$ to $V \setminus X$:

$$
c(X, V \setminus X) = \sum_{e \in \delta^{\text{out}}(X)} c_e
$$

- **Net Flow Lemma:** Summing flow conservation over all $v \in X$ cancels internal edges (whose head and tail both lie in $X$), leaving:

$$
|f| = f^{\text{out}}(X) - f^{\text{in}}(X) \le f^{\text{out}}(X) + 0 \le \sum_{e \in \delta^{\text{out}}(X)} c_e = c(X, V \setminus X)
$$

*(Weak Duality: Every flow value is $\le$ every $s$-$t$ cut capacity.)*

##### Theorem (Max-Flow Min-Cut Theorem)
For any flow network, the following three statements are equivalent:
1. $f$ is a maximum flow.
2. The residual network $G_f$ contains no $s \to t$ augmenting path.
3. $|f| = c(X, V \setminus X)$ for some $s$-$t$ cut $(X, V \setminus X)$.

**Proof ($(2) \implies (3)$):** Suppose $G_f$ has no $s \to t$ path, and let $X = \{v \in V : v \text{ is reachable from } s \text{ in } G_f\}$. Then $s \in X$ and $t \notin X$, so $(X, V \setminus X)$ is a valid $s$-$t$ cut.
- For every outgoing edge $e = (u, v) \in \delta^{\text{out}}(X)$, $(u, v) \notin E_f$ (otherwise $v$ would be reachable), so $c_e - f_e = 0 \implies f_e = c_e$ (**outgoing edges are saturated**).
- For every incoming edge $e = (v, u) \in \delta^{\text{in}}(X)$ with $v \notin X, u \in X$, the reverse residual edge $(u, v)$ cannot be in $E_f$ (otherwise $v$ would be reachable), so $f_e = 0$ (**incoming edges carry zero flow**).
- By the Net Flow Lemma, $|f| = f^{\text{out}}(X) - f^{\text{in}}(X) = c(X, V \setminus X) - 0 = c(X, V \setminus X)$. Combined with $|f'| \le c(X, V \setminus X)$, $f$ is maximum and $(X, V \setminus X)$ is a minimum cut! $\square$

---
## Module 4: Linear Programming, Duality Theory & Farkas' Lemma (Lectures 9–11)

### Lecture 9: LP Formulations, Convex Geometry, Vertices & Polynomial Solvability

#### 9.1 Canonical Form & Standard Modeling Conversions
A **Linear Program (LP)** optimizes a linear objective subject to linear equality and inequality constraints. Its **Canonical Maximization Form** is:

$$
\max_{x \in \mathbb{R}^n} \; c^\top x \quad \text{subject to} \quad Ax \le b, \;\; x \ge 0
$$

| Non-Canonical Feature | Equivalent Canonical Conversion |
| :--- | :--- |
| **Minimize $c^\top x$** | Maximize $(-c)^\top x$ (and negate optimal value) |
| **Greater-than constraint $a_i^\top x \ge b_i$** | Multiply by $-1$: $(-a_i)^\top x \le -b_i$ |
| **Equality constraint $a_i^\top x = b_i$** | Replace with two inequalities: $a_i^\top x \le b_i$ **and** $(-a_i)^\top x \le -b_i$ |
| **Unrestricted variable $z \in \mathbb{R}$** | Substitute $z = z^+ - z^-$ with $z^+ \ge 0,\; z^- \ge 0$ |
| **Slack Form** | Introduce slack variables $s = b - Ax \ge 0$ so $Ax + s = b,\; x, s \ge 0$ |

**Worked Modeling Example (Smoothie Production — Lecture 9):**
Produce quantities $x_1, x_2, x_3 \ge 0$ of three smoothies with profits $(6, 3, 5)$ subject to:
- Total production: $x_1 + x_2 + x_3 \le 6$
- Berry supply: $x_2 + 2x_3 \le 6$
- Acai supply: $x_1 + x_3 \le 3$
Evaluating extreme points yields optimal vertex $x^* = (3, 3, 0)$ with profit $6(3) + 3(3) + 5(0) = 27$.

---

#### 9.2 Convex Polyhedra, Tight Constraints & Vertices (Basic Feasible Solutions)
- **Convexity of Feasible Region:** Let $P = \{x \in \mathbb{R}^n : Ax \le b,\; x \ge 0\}$. Each linear inequality defines a closed half-space; as an intersection of half-spaces, $P$ is a **convex polyhedron** (if $x, y \in P$ and $\lambda \in [0, 1]$, then $A(\lambda x + (1-\lambda)y) = \lambda Ax + (1-\lambda)Ay \le \lambda b + (1-\lambda)b = b$).
- **Three Possible Outcomes for any LP:**
  1. **Infeasible:** $P = \emptyset$ (e.g., $x_1 \le 1$ and $x_1 \ge 2$).
  2. **Unbounded:** Objective $c^\top x \to +\infty$ along a feasible ray in $P$ (e.g., $\max x_1$ s.t. $x_1 - x_2 \le 0, x \ge 0$).
  3. **Finite Optimum Achieved:** A finite maximum value $v^*$ is attained at some $x^* \in P$.
- **Tight Constraints & Vertices:** In $\mathbb{R}^n$, a constraint is **tight (active)** at $x$ if it holds with equality ($a_i^\top x = b_i$ or $x_j = 0$). A feasible point $v \in P$ is a **vertex (basic feasible solution)** if it is uniquely determined as the intersection of **$n$ linearly independent tight constraints** ($A_B v = b_B$ where $A_B \in \mathbb{R}^{n \times n}$ is invertible, so $v = A_B^{-1} b_B$).
- **Fundamental Theorem of LP:** For a canonical LP ($x \ge 0$) that is feasible and bounded, the maximum objective is **always attained at at least one vertex** of $P$. *(Without $x \ge 0$, a polyhedron like the slab $\{(x_1, x_2) : 0 \le x_1 \le 1\}$ has no vertices, which is why canonical form enforces $x \ge 0$.)*

---

#### 9.3 Cramer's Rule & Polynomial Solvability of LPs
Why can't we just enumerate all $\binom{m+n}{n}$ potential vertices? Because $\binom{m+n}{n}$ is exponential in $n$! However:
- **Polynomial Bit-Length of Vertices (Cramer's Rule):** For any invertible $n \times n$ integer submatrix $B = A_B$, each coordinate of the vertex $x = B^{-1}b_B$ is a rational number:

$$
x_i = \frac{\det(B_i)}{\det(B)}
$$

Because determinants of integer matrices have polynomially bounded bit-length in the input encoding size $L$, every vertex can be written down in $\text{poly}(L)$ bits!
- **Algorithms for Solving LPs:**
  - **Simplex Method (Dantzig):** Walks from vertex to adjacent vertex along edges improving $c^\top x$; very fast in practice, but exponential worst-case time on pathological polytopes (Klee-Minty cube).
  - **Ellipsoid & Interior-Point Methods (Khachiyan; Karmarkar):** Solve any rational LP in **polynomial time in the binary bit-length $L$** of $(A, b, c)$.

---
### Lecture 10: LP Duality, Shadow Prices & Max-Flow/Min-Cut via Threshold Rounding

#### 10.1 Deriving the Dual LP from Upper-Bound Certificates
Given the canonical **Primal LP ($P$)**: $\max\{c^\top x : Ax \le b,\; x \ge 0\}$, how can we certify an upper bound on $\text{OPT}(P)$?
Take nonnegative multipliers $y_1, \dots, y_m \ge 0$ on the rows of $Ax \le b$. If $y \ge 0$ satisfies $\sum_{i=1}^m y_i A_{ij} \ge c_j$ for each variable $x_j \ge 0$ (i.e., $A^\top y \ge c$), then for **every** primal-feasible $x$:

$$
c^\top x \le (A^\top y)^\top x = y^\top (Ax) \le y^\top b = b^\top y
$$

Minimizing this upper bound $b^\top y$ over all valid multipliers $y$ defines the **Dual LP ($D$)**:

$$
\text{Primal } (P): \quad \max_{x \in \mathbb{R}^n} \;\; c^\top x \quad \text{s.t.} \quad Ax \le b, \;\; x \ge 0 \qquad \Longleftrightarrow \qquad \text{Dual } (D): \quad \min_{y \in \mathbb{R}^m} \;\; b^\top y \quad \text{s.t.} \quad A^\top y \ge c, \;\; y \ge 0
$$

- **Smoothie Dual & Shadow Prices:** For the Smoothie LP, multipliers $y^* = (5, 0, 2)$ satisfy $A^\top y^* = (5+2, 5, 5+2) = (7, 5, 7) \ge (6, 3, 5) = c$ and give upper bound $b^\top y^* = 6(5) + 6(0) + 3(2) = 36$; solving the dual LP exactly finds $y^{\text{opt}} = (3, 0, 3)$ with $b^\top y^{\text{opt}} = 6(3) + 6(0) + 3(3) = 27 = c^\top x^*$. Each $y_i^*$ represents the **marginal value (shadow price)** of one additional unit of resource $b_i$.

| Primal (Maximization) | Dual (Minimization) |
| :--- | :--- |
| $m$ constraints, $n$ variables | $n$ constraints, $m$ variables |
| Objective vector $c$, RHS vector $b$, matrix $A$ | Objective vector $b$, RHS vector $c$, matrix $A^\top$ |
| $i$-th constraint is $\le b_i$ | $i$-th dual variable satisfies $y_i \ge 0$ |
| $i$-th constraint is $= b_i$ | $i$-th dual variable $y_i \in \mathbb{R}$ is unrestricted |
| $j$-th primal variable satisfies $x_j \ge 0$ | $j$-th dual constraint is $(A^\top y)_j \ge c_j$ |
| $j$-th primal variable $x_j \in \mathbb{R}$ is unrestricted | $j$-th dual constraint is $(A^\top y)_j = c_j$ |

---

#### 10.2 Weak Duality, Strong Duality & Outcome Table
- **Weak Duality Theorem:** For any primal-feasible $x$ and dual-feasible $y$, $c^\top x \le b^\top y$. Consequently:
  - If $c^\top x^* = b^\top y^*$, then $x^*$ is primal-optimal and $y^*$ is dual-optimal.
  - If Primal is unbounded ($+\infty$), Dual must be infeasible; if Dual is unbounded ($-\infty$), Primal must be infeasible.
- **Strong Duality Theorem:** If the Primal LP has a finite optimal solution $x^*$, then the Dual LP also has a finite optimal solution $y^*$, and **$\max_x c^\top x = \min_y b^\top y$**.

| Primal \ Dual | **Finite Optimum** | **Infeasible** | **Unbounded** |
| :--- | :---: | :---: | :---: |
| **Finite Optimum** | **Possible** ($c^\top x^* = b^\top y^*$) | Impossible | Impossible |
| **Infeasible** | Impossible | **Possible** (both infeasible) | **Possible** |
| **Unbounded** | Impossible | **Possible** | Impossible |

---

#### 10.3 Path-Based Max-Flow LP & Proving Max-Flow = Min-Cut via Threshold Rounding
Let $\mathcal{P}$ be the set of all simple $s \to t$ paths in $G = (V, E)$.
- **Path-Flow Primal LP ($P_{\text{path}}$):** Assign flow $x_P \ge 0$ to each path $P \in \mathcal{P}$:

$$
\max \sum_{P \in \mathcal{P}} x_P \quad \text{s.t.} \quad \sum_{P \in \mathcal{P} : e \in P} x_P \le c_e \;\;\forall e \in E, \qquad x_P \ge 0 \;\;\forall P \in \mathcal{P}
$$

- **Dual LP ($D_{\text{length}}$ — Fractional Edge Lengths):** Introduce dual variable $y_e \ge 0$ for each edge $e \in E$:

$$
\min \sum_{e \in E} c_e y_e \quad \text{s.t.} \quad \sum_{e \in P} y_e \ge 1 \;\;\forall P \in \mathcal{P}, \qquad y_e \ge 0 \;\;\forall e \in E
$$

*(Interpretation: Assign nonnegative length $y_e$ to each edge so that **every $s \to t$ path has length at least $1$**.)*
- Note that any $s$-$t$ cut $(S, V \setminus S)$ gives an integral solution $y_e = \mathbf{1}[e \in \delta^+(S)] \in \{0, 1\}$ with cost $c(\delta^+(S))$. What if the optimal dual solution $y^*$ is **fractional**?

##### Threshold Cut Rounding Proof (Strong Duality $\implies$ Max-Flow Min-Cut)
Let $y^* \ge 0$ be an optimal fractional dual solution. Define $d(v)$ as the shortest-path distance from $s$ to $v$ under edge lengths $y^*$, and clip it to $[0, 1]$ via $\ell(v) = \min\{d(v), 1\}$. Then $\ell(s) = 0$ and $\ell(t) = 1$ (since every $s \to t$ path has length $\ge 1$).
For any threshold $r \in (0, 1)$, define the **level-set cut**:

$$
S_r = \{v \in V : \ell(v) \le r\} \qquad (s \in S_r,\; t \notin S_r)
$$

```text
  l(v):   0.0         0.3              r             0.8         1.0
          [s] -------> [u] ----------- | -----------> [v] ------> [t]
          \_______ in S_r _______/     |     \_____ in V \ S_r _____/
                                  threshold r
          Edge (u,v) is cut by S_r  <==>  l(u) <= r < l(v)
```

1. **Triangle Inequality Bound:** By shortest-path definition, $d(v) \le d(u) + y_{uv}^*$ for every edge $e = (u, v) \in E$, which survives clipping at $1$: $\ell(v) - \ell(u) \le y_{uv}^*$.
2. **Integrating over $r \in (0, 1)$:** An edge $e = (u, v)$ is in $\delta^+(S_r)$ if and only if $\ell(u) \le r < \ell(v)$, an interval of length $\max\{0, \ell(v) - \ell(u)\} \le y_{uv}^*$. Integrating the cut capacity over $r \in (0, 1)$:

$$
\int_0^1 c(\delta^+(S_r))\, dr = \sum_{e=(u,v)\in E} c_e \int_0^1 \mathbf{1}[\ell(u) \le r < \ell(v)]\, dr = \sum_{e=(u,v)\in E} c_e \max\{0, \ell(v) - \ell(u)\} \le \sum_{e \in E} c_e y_e^*
$$

3. **Conclusion:** Since the average of $c(\delta^+(S_r))$ over $r \in (0, 1)$ is at most $\sum_e c_e y_e^*$, there exists some threshold $r^* \in (0, 1)$ whose integral cut $S_{r^*}$ satisfies $c(\delta^+(S_{r^*})) \le \sum_e c_e y_e^* = \text{OPT}(D) = \text{OPT}(P) = \text{Max-Flow}$! $\square$

---
### Lecture 11: Farkas' Lemma, Convex Separation & Proof of Strong Duality

#### 11.1 Active Outward Normals & Conic Combinations
Rewrite the canonical LP $\max\{c^\top x : Ax \le b,\; x \ge 0\}$ as a single inequality system $\bar{A}x \le \bar{b}$ by stacking $Ax \le b$ above $-I_n x \le 0$ (where nonnegativity $x_j \ge 0$ has outward normal $-e_j$).
- At a primal optimal point $x^*$, let $I(x^*) = \{r : \bar{a}_r^\top x^* = \bar{b}_r\}$ be the set of **tight (active) constraints** (including active nonnegativity constraints $x_j^* = 0$).
- Geometrically, $x^*$ cannot move in any direction $v$ that stays inside all tight half-spaces ($\bar{a}_r^\top v \le 0$ for all $r \in I(x^*)$) while strictly increasing the objective ($c^\top v > 0$). Why does this force $c$ to be a nonnegative combination of the active outward normals $\{\bar{a}_r\}_{r \in I(x^*)}$? Because of **Farkas' Lemma**!

---

#### 11.2 Farkas' Lemma (Theorem of the Alternatives for Cones)
Let $M = [a_1 \;\dots\; a_t] \in \mathbb{R}^{n \times t}$ and $p \in \mathbb{R}^n$. Define the **convex cone** generated by the columns of $M$:

$$
C = \text{cone}(a_1, \dots, a_t) = \left\{\, \sum_{i=1}^t \lambda_i a_i : \lambda_1, \dots, \lambda_t \ge 0 \,\right\} = \{M\lambda : \lambda \ge 0\}
$$

##### Theorem (Farkas' Lemma)
Exactly one of the following two linear systems has a solution:
- **System (I) [Cone Membership Certificate]:** $\exists \lambda \in \mathbb{R}^t$ such that $M\lambda = p$ and $\lambda \ge 0$ (i.e., $p \in C$).
- **System (II) [Separating Hyperplane Certificate]:** $\exists w \in \mathbb{R}^n$ such that $M^\top w \ge 0$ (i.e., $a_i^\top w \ge 0 \;\forall i$) and $p^\top w < 0$.

```text
                p = (0, 1)  [Outside Cone C]
                    ^
                    |       /  a_2 = (1, 1)
         w = (1,-1) |      /
              \     |     /   Cone C = { lambda_1 a_1 + lambda_2 a_2 >= 0 }
               \    |    /
                \   |   /
                 \  |  /
                  \ | /
  ------------------+------------------> a_1 = (1, 0)
                     \
                      \  Separating hyperplane { z : w^T z = 0 }
                         has w^T a_1 = 1 >= 0, w^T a_2 = 0 >= 0, but w^T p = -1 < 0!
```

##### Geometric Proof of Farkas' Lemma
1. **Not Both:** If both $\lambda \ge 0$ with $M\lambda = p$ and $w$ with $M^\top w \ge 0, p^\top w < 0$ existed, then $0 > p^\top w = (M\lambda)^\top w = \lambda^\top (M^\top w) \ge 0$, a contradiction.
2. **If (I) Fails ($p \notin C$), Then (II) Holds:** Since $C$ is a nonempty, closed, convex cone and $p \notin C$, let $q \in C$ be the **unique closest point in $C$ to $p$**, minimizing $\|z - p\|_2^2$ over $z \in C$, and define the nonzero vector $v = p - q \neq 0$:
   - **Supporting Hyperplane Inequality:** For any $z \in C$ and $t \in [0, 1]$, convexity gives $(1-t)q + tz \in C$, so $\|q - p + t(z - q)\|_2^2 \ge \|q - p\|_2^2$. Expanding and dividing by $t \to 0^+$ yields $v^\top (z - q) \le 0$, i.e., $v^\top q \ge v^\top z$ for all $z \in C$.
   - **Ray Scaling forces $v^\top q = 0$ and $v^\top z \le 0$:** Because $C$ is a cone, for any $\alpha \ge 0$, $\alpha q \in C$, so $v^\top(\alpha q - q) = (\alpha - 1)v^\top q \le 0$ for both $\alpha = 0$ and $\alpha = 2$, forcing **$v^\top q = 0$** and hence $v^\top z \le 0$ for all $z \in C$.
   - **Strict Separation of $p$:** $v^\top p = v^\top(q + v) = v^\top q + \|v\|_2^2 = \|p - q\|_2^2 > 0$.
   - Setting $w = -v = q - p$ gives $a_i^\top w = -v^\top a_i \ge 0$ for all $i$ and $p^\top w = -v^\top p = -\|p - q\|_2^2 < 0$. $\square$

---

#### 11.3 Active-Constraint Proof of Strong LP Duality
Let $x^*$ be an optimal solution of the canonical primal LP $\max\{c^\top x : Ax \le b,\; x \ge 0\}$.
1. **Claim ($c$ lies in the cone of active outward normals at $x^*$):** Let $I = I(x^*)$ be the tight rows of $\bar{A}x \le \bar{b}$ at $x^*$. Suppose for contradiction $c \notin \text{cone}(\{\bar{a}_r\}_{r \in I})$. By Farkas' Lemma, there exists $w \in \mathbb{R}^n$ with $\bar{a}_r^\top w \ge 0$ for all $r \in I$ and $c^\top w < 0$. Set $v = -w$; then:
   - $\bar{a}_r^\top v \le 0$ for all tight constraints $r \in I$ (so $x^* + \varepsilon v$ keeps all tight constraints satisfied for any $\varepsilon > 0$),
   - For all non-tight constraints $r \notin I$, strict slack $\bar{a}_r^\top x^* < \bar{b}_r$ persists for sufficiently small $\varepsilon > 0$,
   - And $c^\top(x^* + \varepsilon v) = c^\top x^* + \varepsilon c^\top v > c^\top x^*$, contradicting optimality of $x^*$!
2. **Constructing Dual Optimal $y^*$:** Therefore $c \in \text{cone}(\{\bar{a}_r\}_{r \in I})$. Assign $\lambda_r \ge 0$ for $r \in I$ and $\lambda_r = 0$ for non-tight $r \notin I$ (so **complementary slackness** $\lambda_r(\bar{b}_r - \bar{a}_r^\top x^*) = 0$ holds for every row!). Splitting $\lambda = (y, \mu)$ into multipliers $y \in \mathbb{R}_{\ge 0}^m$ on $Ax \le b$ and $\mu \in \mathbb{R}_{\ge 0}^n$ on $-x \le 0$:

$$
c = \sum_{i=1}^m y_i a_i + \sum_{j=1}^n \mu_j (-e_j) = A^\top y - \mu \implies A^\top y = c + \mu \ge c \quad (\text{since } \mu \ge 0)
$$

Thus $y \ge 0$ is **dual feasible**! Finally, using complementary slackness $y_i(b_i - a_i^\top x^*) = 0$ and $\mu_j x_j^* = 0$:

$$
c^\top x^* = (A^\top y - \mu)^\top x^* = y^\top(Ax^*) - \mu^\top x^* = \sum_{i=1}^m y_i (a_i^\top x^*) - 0 = \sum_{i=1}^m y_i b_i = b^\top y
$$

Thus $b^\top y = c^\top x^*$, proving **Strong Duality**! $\square$

---
## Module 5: Convex Optimization & Gradient Descent (Lectures 12–13)

### Lecture 12: Convex Functions, First/Second-Order Conditions & Bounded-Gradient Descent

#### 12.1 Convex Sets & Convex Functions
- **Convex Set $K \subseteq \mathbb{R}^d$:** For all $x, y \in K$ and $\lambda \in [0, 1]$, $(1-\lambda)x + \lambda y \in K$.
- **Convex Function $f : K \to \mathbb{R}$ (Chord Inequality):** For all $x, y \in K$ and $\lambda \in [0, 1]$:

$$
f((1-\lambda)x + \lambda y) \le (1-\lambda)f(x) + \lambda f(y)
$$

- **First-Order Characterization (Differentiable $f$):** $f$ is convex on $K$ if and only if its tangent hyperplane is a global underestimator:

$$
f(y) \ge f(x) + \langle \nabla f(x),\, y - x \rangle \quad \forall x, y \in K
$$

  - **Crucial Consequence for Optimization:** Plugging in $y = x^*$ gives the upper bound on suboptimality at $x$:

$$
f(x) - f(x^*) \le \langle \nabla f(x),\, x - x^* \rangle
$$

- **Second-Order Characterization (Twice Differentiable $f$):** $f$ is convex on open convex $K$ iff its Hessian is positive semidefinite everywhere:

$$
\nabla^2 f(x) \succeq 0 \quad (\text{i.e., } v^\top \nabla^2 f(x) v \ge 0 \;\;\forall v \in \mathbb{R}^d)
$$

  - **Least-Squares Example:** For $f(x) = \frac{1}{2}\|Ax - b\|_2^2$, we have $\nabla f(x) = A^\top(Ax - b)$ and $\nabla^2 f(x) = A^\top A$. Since $v^\top (A^\top A) v = \|Av\|_2^2 \ge 0$ for all $v$, $f$ is convex!
- **Theorem (Every Local Minimum is Global):** If $x$ is a local minimum of convex $f$, then for any $y \in K$ and small $\lambda > 0$, $f(x) \le f((1-\lambda)x + \lambda y) \le (1-\lambda)f(x) + \lambda f(y) \implies f(x) \le f(y)$.

---

#### 12.2 Gradient Descent & Step-Size Behavior
The **Gradient Descent (GD)** update with step size (learning rate) $\eta > 0$ is:

$$
x_{t+1} = x_t - \eta \nabla f(x_t)
$$

**Step-Size Regimes on $f(x) = \frac{1}{2}x^2$ ($f'(x) = x$, so $x_{t+1} = (1-\eta)x_t$):**
- $\eta = 1/2$: $x_t = 2^{-t}x_0 \to 0$ monotonically.
- $\eta = 1$: $x_1 = 0$ in a single step.
- $\eta = 2$: $x_{t+1} = -x_t$ oscillates forever between $x_0$ and $-x_0$ with no decrease in $f$.
- $\eta > 2$: $|1-\eta| > 1$, so $|x_t| \to \infty$ diverges!

---

#### 12.3 Convergence Theorem for Bounded-Gradient (Lipschitz) Convex Functions
**Assumptions:** $f : \mathbb{R}^d \to \mathbb{R}$ is convex, $x^*$ is a minimizer with initial distance $\|x_0 - x^*\|_2 \le D$, and $\|\nabla f(x_t)\|_2 \le G$ for all $t$.

##### Theorem (Bounded-Gradient GD Guarantee)
Running Gradient Descent for $T$ iterations with constant step size $\eta = \frac{D}{G\sqrt{T}}$ and returning the **average iterate** $\bar{x}_T = \frac{1}{T}\sum_{t=0}^{T-1} x_t$ (or best iterate $x_{t^*}$) satisfies:

$$
f(\bar{x}_T) - f(x^*) \le \frac{DG}{\sqrt{T}} \qquad \left(\text{so } T \ge \frac{D^2 G^2}{\varepsilon^2} \text{ iterations suffice for } \varepsilon\text{-optimality}\right)
$$

**Proof (Potential Function + Telescoping + Jensen):**
1. **Expand Squared Distance Potential $R_t = \|x_t - x^*\|_2^2$:**

$$
\begin{aligned}
\|x_{t+1} - x^*\|_2^2 &= \|x_t - \eta \nabla f(x_t) - x^*\|_2^2
\\ &= \|x_t - x^*\|_2^2 - 2\eta \langle \nabla f(x_t),\, x_t - x^* \rangle + \eta^2 \|\nabla f(x_t)\|_2^2
\end{aligned}
$$

2. **Bound Per-Step Suboptimality via Convexity:** Using $f(x_t) - f(x^*) \le \langle \nabla f(x_t), x_t - x^* \rangle$ and $\|\nabla f(x_t)\|_2 \le G$:

$$
f(x_t) - f(x^*) \le \langle \nabla f(x_t),\, x_t - x^* \rangle = \frac{\|x_t - x^*\|_2^2 - \|x_{t+1} - x^*\|_2^2}{2\eta} + \frac{\eta}{2}\|\nabla f(x_t)\|_2^2 \le \frac{R_t - R_{t+1}}{2\eta} + \frac{\eta G^2}{2}
$$

3. **Average & Telescope over $t = 0, \dots, T-1$:**

$$
\frac{1}{T}\sum_{t=0}^{T-1} \left(f(x_t) - f(x^*)\right) \le \frac{R_0 - R_T}{2\eta T} + \frac{\eta G^2}{2} \le \frac{D^2}{2\eta T} + \frac{\eta G^2}{2} \quad (\text{since } R_0 \le D^2,\; R_T \ge 0)
$$

4. **Apply Jensen's Inequality & Optimize $\eta$:** By convexity of $f$, $f(\bar{x}_T) \le \frac{1}{T}\sum_{t=0}^{T-1} f(x_t)$. Setting $\frac{D^2}{2\eta T} = \frac{\eta G^2}{2}$ gives $\eta = \frac{D}{G\sqrt{T}}$ and bound $\frac{DG}{\sqrt{T}}$. $\square$
- *(Note: The exact same proof holds for non-differentiable convex functions like $f(x) = |x|$ by replacing $\nabla f(x_t)$ with any **subgradient** $g_t \in \partial f(x_t)$ satisfying $f(y) \ge f(x_t) + \langle g_t, y - x_t \rangle$ and $\|g_t\|_2 \le G$.)*

---
### Lecture 13: Projected Gradient Descent & $\beta$-Smooth Gradient Descent

#### 13.1 Constrained Convex Optimization & Projected Gradient Descent (PGD)
To minimize a convex function $f(x)$ subject to $x \in K$ (where $K \subseteq \mathbb{R}^d$ is nonempty, closed, and convex), an unconstrained gradient step $y_{t+1} = x_t - \eta \nabla f(x_t)$ may leave $K$.
- **Euclidean Projection Operator $\Pi_K$:**

$$
\Pi_K(u) = \arg\min_{z \in K} \|z - u\|_2 \equiv \arg\min_{z \in K} \frac{1}{2}\|z - u\|_2^2
$$

  - *Example (Box Constraints $K = \prod_{i=1}^d [a_i, b_i]$):* $\Pi_K(u)$ decouples coordinate-wise and clips each coordinate in $O(d)$ time: $(\Pi_K(u))_i = \min\{b_i, \max\{a_i, u_i\}\}$.
- **Projected Gradient Descent Update:**

$$
y_{t+1} = x_t - \eta \nabla f(x_t), \qquad x_{t+1} = \Pi_K(y_{t+1})
$$

##### Lemma (Projection Contraction Inequality)
For any nonempty closed convex set $K \subseteq \mathbb{R}^d$, any $u \in \mathbb{R}^d$ with $p = \Pi_K(u)$, and any $z \in K$:

$$
\|p - z\|_2^2 \le \|u - z\|_2^2 - \|u - p\|_2^2 \le \|u - z\|_2^2
$$

**Proof:** Since $p$ minimizes $h(w) = \frac{1}{2}\|w - u\|_2^2$ over $K$ and $\nabla h(p) = p - u$, moving from $p$ toward $z \in K$ cannot decrease $h$, so $\langle p - u, z - p \rangle \ge 0$, or equivalently **$\langle u - p, z - p \rangle \le 0$** (obtuse angle at $p$). Expanding $\|u - z\|_2^2$:

$$
\|u - z\|_2^2 = \|(u - p) + (p - z)\|_2^2 = \|u - p\|_2^2 + \|p - z\|_2^2 - 2\underbrace{\langle u - p, z - p \rangle}_{\le 0} \ge \|u - p\|_2^2 + \|p - z\|_2^2 \quad \square
$$

- **PGD Convergence:** Applying $\|x_{t+1} - x^*\|_2^2 = \|\Pi_K(y_{t+1}) - x^*\|_2^2 \le \|y_{t+1} - x^*\|_2^2$ inside the Lecture 12 proof yields the exact same bound: $f(\bar{x}_T) - f(x^*) \le \frac{DG}{\sqrt{T}}$ in $T = O(D^2G^2/\varepsilon^2)$ steps!

---

#### 13.2 $\beta$-Smooth Convex Functions & The Quadratic Upper Bound (Descent Lemma)
Why did $f(x) = \frac{1}{2}x^2$ fail the global bounded-gradient assumption ($\|f'(x)\| = |x| \to \infty$), and how can we improve $O(1/\varepsilon^2)$ to $O(1/\varepsilon)$? By exploiting **smoothness** (Lipschitz-continuous gradients)!
- **Definition ($\beta$-Smoothness):** A differentiable function $f : \mathbb{R}^d \to \mathbb{R}$ is **$\beta$-smooth** ($\beta > 0$) if its gradient is $\beta$-Lipschitz:

$$
\|\nabla f(y) - \nabla f(x)\|_2 \le \beta \|y - x\|_2 \quad \forall x, y \in \mathbb{R}^d \qquad \left(\text{for } C^2 \text{ convex } f:\;\; 0 \preceq \nabla^2 f(x) \preceq \beta I\right)
$$

  - *Least-Squares Example:* For $f(x) = \frac{1}{2}\|Ax - b\|_2^2$, $\nabla^2 f(x) = A^\top A$, so $f$ is $\beta$-smooth with $\beta = \lambda_{\max}(A^\top A) = \|A\|_2^2$.

##### Lemma (Quadratic Upper Bound / Descent Lemma)
If $f$ is $\beta$-smooth, then for all $x, y \in \mathbb{R}^d$:

$$
f(y) \le f(x) + \langle \nabla f(x),\, y - x \rangle + \frac{\beta}{2}\|y - x\|_2^2
$$

**Proof (Fundamental Theorem of Calculus along the segment $x_t = x + t(y-x)$):**

$$
\begin{aligned}
f(y) - f(x) - \langle \nabla f(x), y - x \rangle &= \int_0^1 \langle \nabla f(x + t(y-x)) - \nabla f(x),\, y - x \rangle\, dt
\\ &\le \int_0^1 \|\nabla f(x + t(y-x)) - \nabla f(x)\|_2 \|y - x\|_2\, dt
\\ &\le \int_0^1 (\beta t \|y - x\|_2)\|y - x\|_2\, dt = \frac{\beta}{2}\|y - x\|_2^2 \quad \square
\end{aligned}
$$

##### Safe Step Size $\eta = 1/\beta$ & Sufficient Decrease
Substituting the GD step $y = x_{t+1} = x_t - \eta \nabla f(x_t)$ (so $y - x_t = -\eta \nabla f(x_t)$) into the Descent Lemma gives:

$$
f(x_{t+1}) \le f(x_t) - \eta\left(1 - \frac{\beta\eta}{2}\right)\|\nabla f(x_t)\|_2^2
$$

Choosing **$\eta = \frac{1}{\beta}$** maximizes the multiplier $\eta(1 - \beta\eta/2) = \frac{1}{2\beta}$, guaranteeing **monotonic per-step descent**:

$$
f(x_{t+1}) \le f(x_t) - \frac{1}{2\beta}\|\nabla f(x_t)\|_2^2 \Longleftrightarrow \|\nabla f(x_t)\|_2^2 \le 2\beta\left(f(x_t) - f(x_{t+1})\right)
$$

##### Theorem (Smooth Convex GD — $O(1/T)$ Last-Iterate Rate)
If $f$ is convex and $\beta$-smooth and $\|x_0 - x^*\|_2 \le D$, then GD with $\eta = 1/\beta$ satisfies:

$$
f(x_T) - f(x^*) \le \frac{\beta D^2}{2T} \qquad \left(\text{so } T = O\left(\frac{\beta D^2}{\varepsilon}\right) \text{ iterations suffice for } \varepsilon\text{-optimality}\right)
$$

**Proof:** Using $\eta = 1/\beta$ in the potential identity and plugging in $\|\nabla f(x_t)\|_2^2 \le 2\beta(f(x_t) - f(x_{t+1}))$:

$$
f(x_t) - f(x^*) \le \frac{\beta}{2}(R_t - R_{t+1}) + \frac{1}{2\beta}\|\nabla f(x_t)\|_2^2 \le \frac{\beta}{2}(R_t - R_{t+1}) + \left(f(x_t) - f(x_{t+1})\right)
$$

Summing over $t = 0, \dots, T-1$ and using monotonicity $f(x_T) \le f(x_t)$ gives $T(f(x_T) - f(x^*)) \le \frac{\beta}{2}R_0 + f(x_0) - f(x_T) - (f(x_0) - f(x_T)) = \frac{\beta D^2}{2}$ (or directly telescoping the $\frac{\beta}{2}(R_t - R_{t+1})$ terms), yielding $f(x_T) - f(x^*) \le \frac{\beta D^2}{2T}$. $\square$

---
## Module 6: Approximation Algorithms — Greedy Methods & LP Rounding (Lectures 14–15)

### Lecture 14: Approximation Guarantees, Greedy Vertex Cover & Edge-Disjoint Paths

#### 14.1 Approximation Ratios ($\alpha \ge 1$ Convention)
When an optimization problem is NP-hard, we design a polynomial-time **$\alpha$-approximation algorithm** ($\alpha \ge 1$, possibly a function $\alpha(n)$ of input size) that outputs a feasible solution with value $\text{ALG}$ satisfying:
- **Minimization Problem:** $\text{OPT} \le \text{ALG} \le \alpha \cdot \text{OPT}$.
- **Maximization Problem:** $\frac{1}{\alpha}\text{OPT} \le \text{ALG} \le \text{OPT}$ (equivalently $\text{OPT} \le \alpha \cdot \text{ALG}$).
- **Key Proof Technique:** Because computing $\text{OPT}$ is NP-hard, we compare $\text{ALG}$ against a polynomial-time **lower bound certificate** (for minimization) or **upper bound certificate** (for maximization).

---

#### 14.2 Minimum Vertex Cover: Greedy-Degree vs. Maximal-Matching
- **Problem:** Given undirected $G = (V, E)$, find a minimum-cardinality vertex subset $C \subseteq V$ covering every edge ($\forall \{u, v\} \in E,\; \{u, v\} \cap C \neq \emptyset$).

##### Algorithm 1: `Greedy-Degree-Cover` — $(1 + \ln m) = O(\log n)$-Approximation
- **Rule:** Repeatedly pick a vertex $v$ of **maximum degree in the remaining uncovered graph**, add $v$ to $C$, and delete $v$ and its incident edges until no edges remain.
- **Why it is NOT a $O(1)$-Approximation:** On a harmonic bipartite graph $H_k$ (or star-of-matchings), `Greedy-Degree` picks high-degree vertices on the wrong side first, using $\Theta(k \log k)$ vertices when $\text{OPT} = k$.
- **Proof of $(1 + \ln m) = O(\log n)$ Approximation:**
  Let $k = \text{OPT} = |C^*|$, and let $r_t = |E_t|$ be the number of uncovered edges after $t$ steps ($r_0 = m$).
  1. Since $C^*$ covers all $r_{t-1}$ edges of $G_{t-1}$, $\sum_{u \in C^*} \deg_{G_{t-1}}(u) \ge r_{t-1}$.
  2. By averaging, at least one $u \in C^*$ has $\deg_{G_{t-1}}(u) \ge r_{t-1}/k$.
  3. Since the algorithm picks $v_t$ of maximum degree in $G_{t-1}$, $\deg_{G_{t-1}}(v_t) \ge r_{t-1}/k$, so:

$$
r_t = r_{t-1} - \deg_{G_{t-1}}(v_t) \le \left(1 - \frac{1}{k}\right)r_{t-1} \implies r_t \le \left(1 - \frac{1}{k}\right)^t m \le e^{-t/k} m
$$

  4. After $t = \lceil k \ln m \rceil$ steps, $r_t < 1$, so $|C| \le \text{OPT}(1 + \ln m) = O(\log n)\text{OPT}$. $\square$

##### Algorithm 2: `Maximal-Matching-Cover` — $2$-Approximation
- **Rule:** Initialize $C = \emptyset, M = \emptyset$. While an uncovered edge $e = \{u, v\}$ remains, add $e$ to $M$, add **both endpoints $u$ and $v$** to $C$, and delete all edges incident to $u$ or $v$.
- **Proof of $2$-Approximation (in $O(n+m)$ time):**
  1. **Feasibility:** The loop ends only when no uncovered edges remain, so $C$ is a valid vertex cover.
  2. **Disjointness Certificate:** The chosen edges $M$ form a **matching** (pairwise vertex-disjoint). Any valid vertex cover $C^*$ must pick at least one distinct vertex from each edge in $M$:

$$
\text{OPT} = |C^*| \ge |M| \quad \text{and} \quad |C| = 2|M| \implies |C| \le 2\,\text{OPT} \quad \square
$$

---

#### 14.3 Directed Edge-Disjoint Paths (EDP) — $O(\sqrt{m})$-Approximation
- **Problem:** Given directed $G = (V, E)$ with $m = |E|$ edges and $k$ terminal pairs $(s_i, t_i)$, route a maximum number of pairs along **pairwise edge-disjoint** directed paths $P_i$.
- **Why Unrestricted Greedy Fails ($\Omega(m)$ bad):** Routing one $m$-edge path $P_1$ can share one edge with each of $m$ unit-length optimal paths, getting $1$ instead of $\text{OPT} = m$.
- **Algorithm (`Short-Path-Greedy` with Cutoff $L = \max\{1, \lfloor\sqrt{m}\rfloor\}$):**
  1. Initialize $A = \emptyset$. While some unrouted pair $(s_i, t_i)$ has a path $P_i$ in the remaining graph using **at most $L$ edges**, pick the shortest such path $P_i$, add $i$ to $A$, and delete all edges of $P_i$ from $G$.
  2. *(Fallback)* If $A = \emptyset$ and some pair has any path in $G$, route that single path ($|A| = 1$).
- **Proof of $(2\sqrt{m} + 1) = O(\sqrt{m})$ Approximation:**
  Let $\mathcal{O}$ be an optimal solution ($\text{OPT} = |\mathcal{O}|$). Partition $\mathcal{O} \setminus A$ into:
  - **Short optimal paths $\mathcal{O}_{\text{short}} = \{Q \in \mathcal{O} \setminus A : |E(Q)| \le L\}$:** Each $Q \in \mathcal{O}_{\text{short}}$ was not routed, so it must share at least one edge with some $P \in A$. Since $\mathcal{O}$ is edge-disjoint and each $P \in A$ has $\le L$ edges, $|\mathcal{O}_{\text{short}}| \le L|A|$.
  - **Long optimal paths $\mathcal{O}_{\text{long}} = \{Q \in \mathcal{O} \setminus A : |E(Q)| \ge L + 1\}$:** Since paths in $\mathcal{O}_{\text{long}}$ are edge-disjoint and each uses $\ge L+1$ edges out of $m$ total edges:

$$
(L + 1)|\mathcal{O}_{\text{long}}| \le m \implies |\mathcal{O}_{\text{long}}| \le \frac{m}{L + 1} \le \sqrt{m}
$$

  - **Total Bound (for $|A| \ge 1$):**

$$
\text{OPT} = |\mathcal{O} \cap A| + |\mathcal{O}_{\text{short}}| + |\mathcal{O}_{\text{long}}| \le |A| + L|A| + \sqrt{m} \le (1 + \sqrt{m})|A| + \sqrt{m}|A| = (2\sqrt{m} + 1)|A| \quad \square
$$

---
### Lecture 15: LP Relaxations, Deterministic Rounding & Metric Facility Location

#### 15.1 The 4-Step LP-Rounding Template
1. **Formulate Exact Integer Program (IP):** Express the combinatorial problem with binary variables $x \in \{0, 1\}^n$.
2. **Relax to Linear Program (LP):** Replace $x_i \in \{0, 1\}$ with continuous intervals $0 \le x_i \le 1$. Since every integral solution is LP-feasible, **$\text{OPT}_{\text{LP}} \le \text{OPT}_{\text{IP}}$** (for minimization) provides an automatic lower bound!
3. **Solve the LP in Polynomial Time:** Obtain an optimal fractional solution $x^*$.
4. **Round $x^*$ to an Integral Solution $\hat{x} \in \{0, 1\}^n$:** Prove $\hat{x}$ is feasible and $\text{cost}(\hat{x}) \le \alpha \cdot \text{OPT}_{\text{LP}} \le \alpha \cdot \text{OPT}_{\text{IP}}$.

---

#### 15.2 Weighted Vertex Cover via Threshold Rounding ($2$-Approximation)
- **LP Relaxation:** Given vertex weights $w_v \ge 0$:

$$
\min \sum_{v \in V} w_v x_v \quad \text{s.t.} \quad x_u + x_v \ge 1 \;\;\forall \{u, v\} \in E, \qquad x_v \ge 0 \;\;\forall v \in V
$$

- **Deterministic Threshold Rounding:** Solve the LP for $x^*$ and output $C = \{v \in V : x_v^* \ge 1/2\}$.
  1. **Feasibility:** For every edge $\{u, v\} \in E$, $x_u^* + x_v^* \ge 1 \implies \max\{x_u^*, x_v^*\} \ge 1/2$, so at least one endpoint is in $C$.
  2. **Cost Bound ($2$-Approximation):** For every $v \in C$, $1 \le 2 x_v^*$, so:

$$
\sum_{v \in C} w_v \le \sum_{v \in V} w_v (2 x_v^*) = 2\,\text{OPT}_{\text{LP}} \le 2\,\text{OPT}
$$

- **Integrality Gap on $K_n$:** Setting $x_v = 1/2$ for all $v \in K_n$ gives $\text{OPT}_{\text{LP}} = n/2$, whereas any integral vertex cover of $K_n$ requires $n-1$ vertices. Thus the integrality gap is $\frac{n-1}{n/2} = 2 - \frac{2}{n} \to 2$.

---

#### 15.3 Metric Uncapacitated Facility Location ($6$-Approximation)
- **Input:** Candidate facilities $F$ with opening costs $f_i \ge 0$ ($i \in F$), clients $C$, and connection distances $d_{ij} \ge 0$ satisfying the **metric triangle inequality** ($d_{ij} \le d_{i'j} + d_{i'j'} + d_{ij'}$).
- **LP Relaxation:** Variables $x_i \ge 0$ (opening facility $i$) and $y_{ij} \ge 0$ (assigning client $j$ to facility $i$):

$$
\min \sum_{i \in F} f_i x_i + \sum_{j \in C} \sum_{i \in F} d_{ij} y_{ij} \quad \text{s.t.} \quad \sum_{i \in F} y_{ij} = 1 \;\;\forall j \in C, \;\; y_{ij} \le x_i \;\;\forall i, j, \;\; x_i, y_{ij} \ge 0
$$

Let $(x^*, y^*)$ be an optimal LP solution with facility cost $F^* = \sum_{i \in F} f_i x_i^*$ and connection cost $D^* = \sum_{j \in C} \sum_{i \in F} d_{ij} y_{ij}^*$, so $\text{OPT}_{\text{LP}} = F^* + D^* \le \text{OPT}$.

##### Clustering & Rounding Algorithm
1. **Average LP Connection Radius $L_j$:** For each client $j \in C$, define $L_j = \sum_{i \in F} d_{ij} y_{ij}^*$ (so $\sum_{j \in C} L_j = D^*$).
2. **Candidate Ball $B_j$ of Radius $2L_j$:** Define $B_j = \{i \in F : d_{ij} \le 2L_j\}$.
   - **Mass Claim ($\sum_{i \in B_j} x_i^* \ge 1/2$):** By Markov's inequality, if $\sum_{i \in B_j} y_{ij}^* < 1/2$, then $> 1/2$ of the fractional assignment of client $j$ lies outside $B_j$ at distance $> 2L_j$, forcing $L_j = \sum_{i \in F} d_{ij} y_{ij}^* > \frac{1}{2}(2L_j) = L_j$, a contradiction! Since $x_i^* \ge y_{ij}^*$, we have $\sum_{i \in B_j} x_i^* \ge \sum_{i \in B_j} y_{ij}^* \ge \frac{1}{2}$.
3. **Greedy Disjoint-Ball Selection:** Sort clients in **nondecreasing order of $L_j$**. Scan clients in this order; select client $r$ into center set $R$ if $B_r$ is **disjoint** from $B_{r'}$ for all previously selected $r' \in R$.
4. **Open Cheapest Facility per Selected Ball:** In each selected ball $B_r$ ($r \in R$), open the single cheapest facility $\hat{i}_r = \arg\min_{i \in B_r} f_i$, and set $\hat{F} = \{\hat{i}_r : r \in R\}$.

```text
  Selected Center r in R                  Unselected Client j
       ( L_j >= L_r )
  +-----------------------+             +-----------------------+
  |  Ball B_r (rad 2L_r)  |             |  Ball B_j (rad 2L_j)  |
  |   [i_r] <--- (r)      |   [ i' ]    |      (j)              |
  +-----------------------+      ^      +-----------------------+
                                 |
                    Shared facility i' in B_r intersect B_j
  Triangle Inequality: d(i_r, j) <= d(i_r, r) + d(i', r) + d(i', j)
                                 <=   2L_r    +   2L_r   +   2L_j   <= 6 L_j
```

##### Complete Proof of the $6$-Approximation Guarantee
- **Facility Opening Cost $\le 2 F^*$:** Inside each selected ball $B_r$, $\hat{i}_r$ is the cheapest facility and $\sum_{i \in B_r} x_i^* \ge 1/2$, so $f_{\hat{i}_r} \le 2 \sum_{i \in B_r} f_i x_i^*$. Because the balls $\{B_r\}_{r \in R}$ are **pairwise disjoint**:

$$
\sum_{r \in R} f_{\hat{i}_r} \le 2 \sum_{r \in R} \sum_{i \in B_r} f_i x_i^* \le 2 \sum_{i \in F} f_i x_i^* = 2 F^*
$$

- **Client Connection Cost $\le 6 D^*$:**
  - If $j \in R$ was selected, its distance to $\hat{i}_j \in B_j$ is at most $2 L_j \le 6 L_j$.
  - If $j \notin R$ was not selected, its ball $B_j$ intersected $B_r$ at some shared facility $i' \in B_r \cap B_j$ for an earlier selected client $r \in R$ with **$L_r \le L_j$**. By the metric triangle inequality:

$$
d(\hat{i}_r, j) \le d(\hat{i}_r, r) + d(i', r) + d(i', j) \le 2L_r + 2L_r + 2L_j \le 6L_j
$$

  Summing over all $j \in C$ gives $\sum_{j \in C} d(\hat{F}, j) \le 6 \sum_{j \in C} L_j = 6 D^*$.
- **Total Cost:** $2F^* + 6D^* \le 6(F^* + D^*) = 6\,\text{OPT}_{\text{LP}} \le 6\,\text{OPT}$. $\square$

---
## 7. Self-Test Quiz Bank (30 Questions with Solutions)

### 7.1 Part I Quiz: Divide & Conquer, Dynamic Programming & Graphs (Questions 1–15)

**Q1 (Lec 1 — Asymptotics):** True or False: $2^{n+1} = \Theta(2^n)$ and $2^{2n} = \Theta(2^n)$.
<details><summary>Solution</summary>

**False.** First part is True since $2^{n+1} = 2 \cdot 2^n = \Theta(2^n)$. Second part is False because $\frac{2^{2n}}{2^n} = 2^n \to \infty$, so $2^{2n} = \omega(2^n)$.

</details>

**Q2 (Lec 1 — Merge Sort):** How many comparisons does `Merge` perform in the worst case to merge two sorted arrays of sizes $n_1$ and $n_2$?
<details><summary>Solution</summary>

**$n_1 + n_2 - 1$ comparisons.** Every comparison appends one element to the output, and when the last element of one array is appended, the remaining suffix of the other array ($\ge 1$ element) is copied with $0$ additional comparisons.

</details>

**Q3 (Lec 2 — Master Theorem):** Solve $T(n) = 4T(n/2) + \Theta(n^2)$ and $T(n) = 3T(n/2) + \Theta(n)$.
<details><summary>Solution</summary>

- $T(n) = 4T(n/2) + \Theta(n^2)$: $a=4, b=2, d=2 = \log_2 4 \implies T(n) = \Theta(n^2 \log n)$.
- $T(n) = 3T(n/2) + \Theta(n)$: $a=3, b=2, d=1 < \log_2 3 \implies T(n) = \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$.

</details>

**Q4 (Lec 2 — Max Difference):** Why did changing the recursive return value in Maximum Difference from `bestDiff` to `(bestDiff, max, min)` reduce the runtime from $\Theta(n \log n)$ to $\Theta(n)$?
<details><summary>Solution</summary>

It reduced the **Combine** step at each node from $\Theta(n)$ (scanning both halves for max and min) to $O(1)$ (`maxLeft - minRight`), shifting the Master Theorem regime from $d = 1 = \log_2 2$ ($\Theta(n \log n)$) to $d = 0 < \log_2 2$ ($\Theta(n)$).

</details>

**Q5 (Lec 2–3 — Selection):** In Median-of-Medians, what is the recurrence if we partition into **groups of 7** instead of groups of 5? Is it still $O(n)$?
<details><summary>Solution</summary>

**Yes, still $O(n)$.** With groups of 7, at least $4$ elements in each of $\frac{1}{2}\frac{n}{7}$ groups are $\ge p$ (and $\le p$), eliminating $\frac{4}{14}n = \frac{2}{7}n$ elements. Thus $T(n) \le T(\lceil n/7 \rceil) + T(\lceil 5n/7 \rceil) + cn$. Since $\frac{1}{7} + \frac{5}{7} = \frac{6}{7} < 1$, strong induction gives $T(n) = O(n)$.

</details>

**Q6 (Lec 3 — Contiguous Sum):** In Kadane's algorithm, what goes wrong if we define $M[i]$ as the maximum contiguous subarray sum *anywhere* in $A[1..i]$?
<details><summary>Solution</summary>

If $M[i-1]$ does not end at index $i-1$, appending $A[i]$ to it creates a **non-contiguous** subset! Requiring $M[i]$ to end *exactly* at $i$ ensures $M[i-1] + A[i]$ is always a contiguous subarray.

</details>

**Q7 (Lec 3–4 — LCS):** Can we compute the **length** of the LCS of two strings of lengths $n$ and $m$ in $O(\min\{n, m\})$ space?
<details><summary>Solution</summary>

**Yes.** Row $i$ of $D[i, j]$ depends only on row $i-1$ and row $i$, so keeping only two rows uses $O(\min\{n, m\})$ space.

</details>

**Q8 (Lec 4 — Tree MIS):** Why does the Tree MIS DP fail on a general graph containing cycles?
<details><summary>Solution</summary>

Removing a vertex from a tree disconnects its subtrees into **independent** subproblems with no edges between them. In a graph with cycles, subtrees share vertices and cross-edges, so independent subtree choices can pick two adjacent vertices.

</details>

**Q9 (Lec 4 — Knapsack):** Suppose $n = 100$ and $B = 2^{100}$. What is the binary input size of $B$, and why is $O(nB)$ not polynomial?
<details><summary>Solution</summary>

The binary encoding of $B = 2^{100}$ uses $\log_2 B + 1 = 101$ bits, whereas $O(nB) = O(100 \cdot 2^{100})$ operations is **exponential** in the $101$-bit input size.

</details>

**Q10 (Lec 4–5 — Knapsack FPTAS):** Why must the Knapsack FPTAS scale and round **values** $v_i$ rather than **sizes** $s_i$?
<details><summary>Solution</summary>

$\sum_{i \in S} s_i \le B$ is a **hard feasibility constraint**: rounding sizes could output an infeasible subset whose true size exceeds $B$. Rounding values preserves exact capacity feasibility while losing at most $nK = \varepsilon V_{\max} \le \varepsilon\,\text{OPT}$ in value.

</details>


**Q11 (Lec 5 — MDPs):** In a finite-horizon MDP, can a randomized or history-dependent policy ever achieve a strictly higher expected total reward than the optimal deterministic Markov policy $\pi^*(s, t)$?
<details><summary>Solution</summary>

**No.** At every step $t$, any randomized distribution over actions $a \in A$ achieves a convex combination of their Q-values, which is $\le \max_{a \in A} Q(s, a, t)$, and future transition probabilities depend only on $(s, t)$.

</details>

**Q12 (Lec 6 — Dijkstra):** Does adding a large positive constant $+M$ to every edge weight in a graph with negative edges make Dijkstra's algorithm return the correct shortest paths?
<details><summary>Solution</summary>

**No!** A path $P$ with $k$ edges has its weight increased by $+kM$, penalizing paths with more edges more heavily than paths with fewer edges and changing the shortest path.

</details>

**Q13 (Lec 7 — Prim's Algorithm):** If a connected graph has distinct edge weights, how many Minimum Spanning Trees can it have?
<details><summary>Solution</summary>

**Exactly one unique MST.** Whenever weights are distinct, the minimum-weight edge across any cut is unique and must belong to *every* MST by the Cut Property.

</details>

**Q14 (Lec 7 — Berge's Theorem):** In the proof of Berge's Theorem, why does every connected component of the symmetric difference $M \oplus M^*$ have maximum degree at most $2$?
<details><summary>Solution</summary>

Because $M$ and $M^*$ are matchings, each vertex is incident to $\le 1$ edge of $M$ and $\le 1$ edge of $M^*$, so $\le 2$ edges in $M \oplus M^*$.

</details>

**Q15 (Lec 8 — Cuts & Flows):** For an $s$-$t$ cut $(X, V \setminus X)$ where an incoming edge $e = (v, u)$ ($v \notin X, u \in X$) has capacity $c_e = 10$ and flow $f_e = 4$, how much does $e$ contribute to the cut capacity $c(X, V \setminus X)$ and to the net flow across the cut?
<details><summary>Solution</summary>

It contributes **$0$ to the cut capacity** $c(X, V \setminus X)$ (which sums only *outgoing* edges from $X$ to $V \setminus X$), and **$-4$ to the net flow** $|f| = f^{\text{out}}(X) - f^{\text{in}}(X)$.

</details>

---

### 7.2 Part II Quiz: Linear Programming, Convex Optimization & Approximation (Questions 16–30)

**Q16 (Lec 9 — LP Conversion):** When converting an unrestricted variable $z \in \mathbb{R}$ into $z = z^+ - z^-$ with $z^+, z^- \ge 0$, how many variables are added?
<details><summary>Solution</summary>

$1$ unrestricted variable is replaced by **$2$ nonnegative variables** ($z^+, z^- \ge 0$), increasing the variable count by $1$.

</details>

**Q17 (Lec 9 — LP Geometry):** Can the set of optimal solutions of a Linear Program consist of **exact two isolated vertices** $v_1 \neq v_2$ with no optimal points between them?
<details><summary>Solution</summary>

**No.** Both the feasible region $P$ and the optimal hyperplane $\{x : c^\top x = v^*\}$ are convex, so their intersection is **convex**: every point on the segment $\lambda v_1 + (1-\lambda)v_2$ ($\lambda \in [0, 1]$) is also optimal.

</details>

**Q18 (Lec 9 — Vertices):** In $\mathbb{R}^n$, how many linearly independent tight constraints are required to define a vertex of $P = \{x \in \mathbb{R}^n : Ax \le b, x \ge 0\}$?
<details><summary>Solution</summary>

**$n$ linearly independent tight constraints** (chosen from the $m$ rows of $Ax \le b$ and the $n$ nonnegativity rows $x_j \ge 0$).

</details>

**Q19 (Lec 10 — Weak Duality):** Suppose the Primal LP $\max\{c^\top x : Ax \le b, x \ge 0\}$ has a feasible $x$ with $c^\top x = 15$, and the Dual LP has a feasible $y$ with $b^\top y = 15$. What can you conclude?
<details><summary>Solution</summary>

By Weak Duality, $c^\top x' \le b^\top y'$ for all feasible $x', y'$. Thus **both $x$ is primal-optimal and $y$ is dual-optimal**, with $\text{OPT}(P) = \text{OPT}(D) = 15$.

</details>

**Q20 (Lec 10 — Dual Feasibility):** If a Primal LP is **infeasible**, what are the possible states of its Dual LP?
<details><summary>Solution</summary>

The Dual LP is either **unbounded** or **also infeasible** (never finite optimal, by Strong Duality).

</details>

**Q21 (Lec 11 — Farkas' Lemma):** Suppose $M \in \mathbb{R}^{n \times t}$ and $p \notin \text{cone}(M)$. In the geometric proof of Farkas' Lemma, how is the separating vector $v$ constructed from $p$ and $C = \text{cone}(M)$?
<details><summary>Solution</summary>

Let $q = \arg\min_{z \in C} \|z - p\|_2^2$ be the unique closest point in the closed convex cone $C$ to $p$, and set $v = p - q$ (or $w = q - p$). Then $v^\top q = 0$, $v^\top z \le 0$ for all $z \in C$, and $v^\top p = \|p - q\|_2^2 > 0$.

</details>

**Q22 (Lec 11 — Complementary Slackness):** If $x^*$ is primal optimal and $y^*$ is dual optimal, and the $i$-th primal constraint has strict slack ($a_i^\top x^* < b_i$), what must be the value of the $i$-th dual variable $y_i^*$?
<details><summary>Solution</summary>

**$y_i^* = 0$.** By complementary slackness (and the active-constraint proof of Strong Duality), only **tight** primal constraints at $x^*$ can have nonzero dual multipliers $y_i^* > 0$.

</details>

**Q23 (Lec 12 — Convexity):** Give the first-order and second-order conditions for a twice-differentiable function $f : \mathbb{R}^d \to \mathbb{R}$ to be convex.
<details><summary>Solution</summary>

- **First-order:** $f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle$ for all $x, y \in \mathbb{R}^d$.
- **Second-order:** $\nabla^2 f(x) \succeq 0$ ($v^\top \nabla^2 f(x) v \ge 0$ for all $v \in \mathbb{R}^d$) for all $x \in \mathbb{R}^d$.

</details>

**Q24 (Lec 12 — Bounded-Gradient GD):** For a convex function with $\|x_0 - x^*\|_2 \le D$ and $\|\nabla f(x)\|_2 \le G$, how does the number of iterations $T$ scale with target accuracy $\varepsilon$? What step size $\eta$ is used?
<details><summary>Solution</summary>

$T = \Theta\left(\frac{D^2 G^2}{\varepsilon^2}\right)$ iterations (an $O(1/\sqrt{T})$ convergence rate), using step size $\eta = \frac{D}{G\sqrt{T}} = \frac{\varepsilon}{G^2}$.

</details>

**Q25 (Lec 13 — Projection Contraction):** Why does Euclidean projection $x_{t+1} = \Pi_K(y_{t+1})$ onto a convex set $K$ not break the potential-function analysis of Gradient Descent?
<details><summary>Solution</summary>

Because the Projection Contraction Inequality guarantees $\|x_{t+1} - x^*\|_2^2 = \|\Pi_K(y_{t+1}) - x^*\|_2^2 \le \|y_{t+1} - x^*\|_2^2$ for every $x^* \in K$, so projection **never increases** the distance to $x^*$.

</details>

**Q26 (Lec 13 — Smoothness vs. Lipschitz):** How does adding $\beta$-smoothness ($0 \preceq \nabla^2 f(x) \preceq \beta I$) improve Gradient Descent compared to only assuming bounded gradients?
<details><summary>Solution</summary>

With step size $\eta = 1/\beta$, each step guarantees sufficient decrease $f(x_{t+1}) \le f(x_t) - \frac{1}{2\beta}\|\nabla f(x_t)\|_2^2$, improving the convergence rate from $O(1/\sqrt{T})$ to **$O(1/T)$** ($T = O(\beta D^2 / \varepsilon)$ iterations) and holding for the **last iterate $x_T$**.

</details>

**Q27 (Lec 14 — Vertex Cover):** Why does `Maximal-Matching-Cover` pick **both** endpoints of each chosen edge $\{u, v\} \in M$ instead of just one?
<details><summary>Solution</summary>

We do not know *which* of the two endpoints $u$ or $v$ belongs to the optimal vertex cover $C^*$. Picking **both** guarantees that at least one of the two chosen vertices is in $C^*$, losing at most a factor of $2$.

</details>

**Q28 (Lec 14 — Edge-Disjoint Paths):** In `Short-Path-Greedy` for Directed EDP, why is the path-length cutoff set to $L = \lfloor \sqrt{m} \rfloor$?
<details><summary>Solution</summary>

A cutoff of $L$ causes each chosen path to block at most $L$ short optimal paths ($|\mathcal{O}_{\text{short}}| \le L|A|$), while at most $m/(L+1)$ edge-disjoint long optimal paths can fit in $m$ edges ($|\mathcal{O}_{\text{long}}| \le m/(L+1)$). Balancing $L \approx \frac{m}{L}$ chooses $L = \lfloor \sqrt{m} \rfloor$, minimizing the approximation ratio at $O(\sqrt{m})$.

</details>

**Q29 (Lec 15 — LP Rounding):** Why does simple threshold rounding $C = \{v : x_v^* \ge 1/2\}$ give a $2$-approximation for Vertex Cover, what would happen if we used threshold $1/3$, and why can't we use threshold $2/3$?
<details><summary>Solution</summary>

- At threshold $1/2$: $x_u^* + x_v^* \ge 1 \implies \max\{x_u^*, x_v^*\} \ge 1/2$ guarantees feasibility, and $1 \le 2x_v^*$ gives cost $\le 2\,\text{OPT}_{\text{LP}}$.
- At threshold $1/3$: Still feasible, but cost bound degrades to $3\,\text{OPT}_{\text{LP}}$.
- At threshold $2/3$: **Infeasible!** An edge with $x_u^* = x_v^* = 1/2$ satisfies $x_u^* + x_v^* = 1$ in the LP, yet neither endpoint has $x^* \ge 2/3$.

</details>

**Q30 (Lec 15 — Facility Location):** In the Metric Facility Location LP-rounding algorithm, why must we sort clients in **nondecreasing order of $L_j$** when greedily selecting disjoint balls $B_r$?
<details><summary>Solution</summary>

When an unselected client $j \notin R$ has its ball $B_j$ blocked by an already-selected ball $B_r$ ($B_r \cap B_j \neq \emptyset$), sorting by nondecreasing $L_j$ ensures **$L_r \le L_j$**. That way, the triangle inequality bound $d(\hat{i}_r, j) \le 4L_r + 2L_j$ is at most $6L_j$.

</details>

---
## 8. Comprehensive Exam Practice Problems (12 Multi-Part Problems with Rubric Solutions)

### Exam Problem 1: Divide-and-Conquer — Counting Significant Inversions (Lectures 1–2)
Given an array $A[0..n-1]$ of $n$ real numbers, a **significant inversion** is a pair of indices $(i, j)$ such that $i < j$ and $A[i] > 2 A[j]$.
1. **(a)** Design an $O(n \log n)$ divide-and-conquer algorithm to count the total number of significant inversions in $A$.
2. **(b)** Prove the correctness of your algorithm and analyze its running time using a recurrence relation.

<details><summary>Full Rubric Solution</summary>

1. **Algorithm (`Count-Sig-Inv(A)`):**
   - **Base case:** If $n \le 1$, return $(0, A)$.
   - **Divide & Conquer:** Split $A$ into $L = A[0..\lfloor n/2 \rfloor - 1]$ and $R = A[\lfloor n/2 \rfloor .. n-1]$. Recursively compute $(c_L, L_{\text{sorted}})$ and $(c_R, R_{\text{sorted}})$.
   - **Count Cross-Inversions in $O(n)$ via Two Pointers:** Initialize pointer $q = 0$ in $R_{\text{sorted}}$ and $c_{\text{cross}} = 0$. For each $p = 0, \dots, |L|-1$: advance $q$ while $q < |R|$ and $L_{\text{sorted}}[p] > 2 R_{\text{sorted}}[q]$; then add $q$ to $c_{\text{cross}}$.
   - **Merge:** Standard `Merge` of $L_{\text{sorted}}$ and $R_{\text{sorted}}$ into $A_{\text{sorted}}$ in $O(n)$ time. Return $(c_L + c_R + c_{\text{cross}}, A_{\text{sorted}})$.
2. **Correctness:** Every significant inversion $(i, j)$ lies either entirely in $L$ (counted in $c_L$), entirely in $R$ (counted in $c_R$), or crosses from $L$ to $R$. Since $L_{\text{sorted}}$ and $R_{\text{sorted}}$ are nondecreasing, if $L_{\text{sorted}}[p] > 2 R_{\text{sorted}}[q]$, then $L_{\text{sorted}}[p'] > 2 R_{\text{sorted}}[q]$ for all $p' \ge p$, so pointer $q$ never needs to move backward.
3. **Runtime:** The counting pass advances $p$ and $q$ at most $n$ times ($O(n)$) and `Merge` takes $O(n)$. Thus $T(n) = 2T(n/2) + \Theta(n) \implies T(n) = \Theta(n \log n)$ by the Master Theorem ($a=2, b=2, d=1$).

</details>

---

### Exam Problem 2: Recurrences & Median-of-Medians Variant (Lectures 2–3)
1. **(a)** Prove by strong induction that $T(n) \le T(\lfloor n/4 \rfloor) + T(\lceil 2n/3 \rceil) + cn$ satisfies $T(n) = O(n)$.
2. **(b)** Explain mathematically why modifying Median-of-Medians to use **groups of 3** fails to run in $O(n)$ time, and determine its actual asymptotic complexity.

<details><summary>Full Rubric Solution</summary>

1. **Part (a) — Strong Induction Proof:**
   - **Inductive Hypothesis:** $T(m) \le A m$ for all $1 \le m < n$.
   - Since $\frac{1}{4} + \frac{2}{3} = \frac{11}{12} < 1$, there is $\frac{1}{12}An$ slack. Using $\lceil 2n/3 \rceil \le \frac{2n}{3} + 1$:

     $\displaystyle T(n) \le A\left(\frac{n}{4}\right) + A\left(\frac{2n}{3} + 1\right) + cn = \frac{11}{12}An + A + cn = An - \left(\frac{1}{12}An - A - cn\right) \le An$

   for $A \ge 24c$ and $n \ge 24$.
2. **Part (b) — Groups of 3 Analysis:**
   - With groups of 3, each group median has only $1$ element above it and $1$ element below it (so $2$ elements $\ge p$ per group in the upper half of $\frac{1}{2}\frac{n}{3} = \frac{n}{6}$ groups).
   - Thus only $2 \cdot \frac{n}{6} = \frac{n}{3}$ elements are guaranteed $\ge p$ (and $\le p$), leaving up to $\frac{2n}{3}$ elements in the recursive call.
   - The recurrence is $T(n) = T(n/3) + T(2n/3) + cn$. Because $\frac{1}{3} + \frac{2}{3} = 1$, every complete level of the recursion tree performs $\Theta(n)$ work across $\Theta(\log n)$ levels, yielding $T(n) = \Theta(n \log n)$.

</details>

---
### Exam Problem 3: Dynamic Programming on Strings & Arrays (Lectures 3–4)
Given an array $A[1..n]$ of positive and negative integers, design an $O(n)$ Dynamic Programming algorithm to find the maximum sum of a contiguous subarray when you are allowed to **delete at most one element** from the chosen contiguous subarray (the resulting subarray must still contain at least one element).

<details><summary>Full Rubric Solution</summary>

1. **Subproblem Definitions:** For each $i \in \{1, \dots, n\}$:
   - Let $M_0[i]$ = maximum sum of a contiguous subarray ending at index $i$ with **0 deletions**.
   - Let $M_1[i]$ = maximum sum of a contiguous subarray ending at index $i$ with **1 deletion** already used.
2. **Base Cases ($i = 1, 2$):**
   - $M_0[1] = A[1]$, $M_1[1] = -\infty$ (cannot delete the only element).
   - For $i \ge 2$:
3. **Recurrences:**

   $\displaystyle M_0[i] = \max\{\, A[i],\; A[i] + M_0[i-1] \,\}$

   $\displaystyle M_1[i] = \max\{\, M_0[i-1] \;\text{(delete } A[i]\text{)},\; A[i] + M_1[i-1] \;\text{(keep } A[i]\text{ after earlier deletion)} \,\}$

4. **Final Answer & Complexity:** Return $\max_{1 \le i \le n} \max\{M_0[i], M_1[i]\}$. Filling $2n$ states takes $O(1)$ per index, giving **$O(n)$ time** and $O(n)$ (or $O(1)$) space.

</details>

---

### Exam Problem 4: Tree DP — Minimum Weight Vertex Cover on a Tree (Lecture 4)
Given an undirected tree $T = (V, E)$ with positive vertex weights $w_v > 0$, design an $O(|V|)$-time Dynamic Programming algorithm to find the **Minimum Weight Vertex Cover** of $T$.

<details><summary>Full Rubric Solution</summary>

1. **Root the Tree:** Root $T$ at an arbitrary vertex $r \in V$. For each $v \in V$, let $C(v)$ be its children in the rooted subtree $T_v$.
2. **Subproblem States:**
   - $I[v]$ = minimum weight of a vertex cover of subtree $T_v$ that **includes** $v$.
   - $X[v]$ = minimum weight of a vertex cover of subtree $T_v$ that **excludes** $v$.
3. **Bellman Recurrences (Bottom-Up Postorder):**
   - If $v$ is excluded ($X[v]$), every edge $(v, u)$ to a child $u \in C(v)$ must be covered by **including $u$**:

     $\displaystyle X[v] = \sum_{u \in C(v)} I[u]$

   - If $v$ is included ($I[v]$), all edges $(v, u)$ are already covered by $v$, so each child $u \in C(v)$ may independently be included or excluded:

     $\displaystyle I[v] = w_v + \sum_{u \in C(v)} \min\{I[u], X[u]\}$

4. **Base Case & Answer:** At any leaf $\ell$, $X[\ell] = 0$ and $I[\ell] = w_\ell$. Final answer at root $r$ is $\min\{I[r], X[r]\}$ in $O(|V|)$ time.

</details>

---
### Exam Problem 5: Knapsack with Cardinality Constraint & FPTAS (Lectures 4–5)
Suppose you are given $n$ items with integer sizes $s_i > 0$ and integer values $v_i > 0$, capacity $B$, and an additional constraint that you may select **at most $k$ items** ($1 \le k \le n$).
1. **(a)** Modify the **value-indexed DP** from Lecture 4 to solve this problem exactly in $O(n k V_{\text{sum}})$ time.
2. **(b)** Design an FPTAS with approximation factor $(1 - \varepsilon)$ running in $O(n k^2 / \varepsilon)$ time.

<details><summary>Full Rubric Solution</summary>

1. **Part (a) — Value-Indexed DP:**
   - **State:** Let $D[i, j, v]$ be the minimum total size of a subset of items from $\{1, \dots, i\}$ using **at most $j$ items** ($0 \le j \le k$) that achieves **exact value $v$** ($0 \le v \le k V_{\max}$).
   - **Base Cases:** $D[0, j, 0] = 0$ for all $0 \le j \le k$, and $D[0, j, v] = +\infty$ for all $v > 0$; $D[i, 0, v] = +\infty$ for all $v > 0$.
   - **Recurrence:**

     $\displaystyle D[i, j, v] = \min\left\{\, D[i-1, j, v],\; \begin{cases} s_i + D[i-1, j-1, v - v_i] & \text{if } j \ge 1 \text{ and } v_i \le v \\ +\infty & \text{otherwise} \end{cases} \,\right\}$

   - **Output & Runtime:** $\max\{v : D[n, k, v] \le B\}$. Table has $O(n \cdot k \cdot k V_{\max})$ states, each computed in $O(1)$ time.
2. **Part (b) — FPTAS Scaling:**
   - Since any feasible solution uses at most $k$ items, set the scaling factor to **$K = \frac{\varepsilon V_{\max}}{k}$** and $\hat{v}_i = \lfloor v_i / K \rfloor$.
   - Then $\hat{v}_i \le \frac{k}{\varepsilon}$, so the maximum scaled value of at most $k$ items is $\hat{V}_{\text{sum}} \le k \cdot \frac{k}{\varepsilon} = \frac{k^2}{\varepsilon}$.
   - Running the DP from Part (a) takes $O(n \cdot k \cdot \hat{V}_{\text{sum}}) = O(n k^3 / \varepsilon)$ time (or $O(n k^2 / \varepsilon)$ if only tracking exact value sums), and loses at most $|S^*| K \le k K = \varepsilon V_{\max} \le \varepsilon\,\text{OPT}$!

</details>

---

### Exam Problem 6: Finite-Horizon MDP Policy & Value Iteration (Lecture 5)
Consider an MDP with states $S = \{s_1, s_2\}$, actions $A = \{\text{Stay}, \text{Switch}\}$, and horizon $T = 2$:
- In $s_1$: `Stay` gives reward $2$ and stays in $s_1$ w.p. $1$; `Switch` gives reward $0$ and moves to $s_2$ w.p. $0.8$ or stays in $s_1$ w.p. $0.2$.
- In $s_2$: `Stay` gives reward $5$ and stays in $s_2$ w.p. $1$; `Switch` gives reward $1$ and moves to $s_1$ w.p. $1$.
Compute $V^*(s, t)$ and $\pi^*(s, t)$ for all $s \in \{s_1, s_2\}$ and $t \in \{0, 1, 2\}$.

<details><summary>Full Rubric Solution</summary>

1. **Base Case ($t = 0$):** $V^*(s_1, 0) = 0$, $V^*(s_2, 0) = 0$.
2. **Step $t = 1$:**
   - $V^*(s_1, 1) = \max\{\underbrace{2 + 0}_{\text{Stay}},\, \underbrace{0 + 0}_{\text{Switch}}\} = 2$, with $\pi^*(s_1, 1) = \text{Stay}$.
   - $V^*(s_2, 1) = \max\{\underbrace{5 + 0}_{\text{Stay}},\, \underbrace{1 + 0}_{\text{Switch}}\} = 5$, with $\pi^*(s_2, 1) = \text{Stay}$.
3. **Step $t = 2$:**
   - At $s_1$:
     - `Stay`: $2 + 1.0 \cdot V^*(s_1, 1) = 2 + 2 = 4$.
     - `Switch`: $0 + 0.2 \cdot V^*(s_1, 1) + 0.8 \cdot V^*(s_2, 1) = 0 + 0.2(2) + 0.8(5) = 0.4 + 4.0 = 4.4$.
     - Therefore **$V^*(s_1, 2) = 4.4$** and **$\pi^*(s_1, 2) = \text{Switch}$**!
   - At $s_2$:
     - `Stay`: $5 + V^*(s_2, 1) = 5 + 5 = 10$.
     - `Switch`: $1 + V^*(s_1, 1) = 1 + 2 = 3$.
     - Therefore **$V^*(s_2, 2) = 10$** and **$\pi^*(s_2, 2) = \text{Stay}$**.

</details>

---
### Exam Problem 7: Shortest Paths & Minimum Spanning Trees (Lectures 6–7)
Let $G = (V, E)$ be a connected undirected graph with positive edge weights $w_e > 0$.
1. **(a)** Suppose we **square** every edge weight: $w'_e = (w_e)^2$. Does the Minimum Spanning Tree of $G$ necessarily remain an MST under $w'$? Does the shortest $s$-$t$ path necessarily remain a shortest path under $w'$? Prove or give counterexamples.
2. **(b)** Design an $O((n+m)\log n)$ modification of Dijkstra's algorithm to compute, for every vertex $v \in V$, the **number of distinct shortest $s \to v$ paths** (`count[v]`) in a directed graph with strictly positive edge weights $w_e > 0$.

<details><summary>Full Rubric Solution</summary>

1. **Part (a):**
   - **MST is preserved (True):** Squaring $x \mapsto x^2$ is strictly increasing on $x > 0$, so the relative order of all edge weights is unchanged ($w_e \le w_f \iff w_e^2 \le w_f^2$). By the Cut Property / Prim's algorithm, any MST under $w$ remains an MST under $w'$.
   - **Shortest path is NOT preserved (False):** Consider $s - a - t$ with $w(s,a)=2, w(a,t)=2$ (total weight $2+2=4$) vs. direct edge $(s,t)$ with $w(s,t)=3$. Under $w$, $s \to t$ is shorter ($3 < 4$). Under $w'_e = w_e^2$, $s \to a \to t$ has weight $2^2 + 2^2 = 8$, while $s \to t$ has weight $3^2 = 9$, flipping the shortest path!
2. **Part (b) — Counting Shortest Paths in Dijkstra:**
   - Initialize `dist[s] = 0, count[s] = 1`, and `dist[v] = +inf, count[v] = 0` for $v \neq s$.
   - When relaxing edge $(u, v)$ after extracting $u$:
     - If `dist[u] + w(u,v) < dist[v]`: set `dist[v] = dist[u] + w(u,v)`, **`count[v] = count[u]`**, and `Decrease-Key`.
     - Else if `dist[u] + w(u,v) == dist[v]`: set **`count[v] = count[v] + count[u]`**.
   - Since $w_e > 0$, all predecessors $u$ on shortest paths to $v$ have strictly smaller distance $d[u] < d[v]$ and are settled before $v$. Runtime is identical to Dijkstra: $O((n+m)\log n)$.

</details>

---

### Exam Problem 8: Max-Flow, Residual Network & Min-Cut Certificate (Lecture 8)
Consider the directed network with vertices $\{s, a, b, t\}$ and capacities:
$c(s, a) = 10$, $c(s, b) = 5$, $c(a, b) = 8$, $c(a, t) = 4$, $c(b, t) = 12$.
1. **(a)** Execute Ford-Fulkerson starting by pushing flow along $s \to a \to b \to t$, then $s \to a \to t$, then $s \to b \to t$.
2. **(b)** State the final flow value $|f^*|$, list all residual edges in $G_{f^*}$ reachable from $s$, and exhibit a minimum $s$-$t$ cut $(X, V \setminus X)$ certifying optimality.

<details><summary>Full Rubric Solution</summary>

1. **Part (a) — Augmentation Trace:**
   - **Step 1 ($P_1 = s \to a \to b \to t$):** Bottleneck $\Delta_1 = \min\{10, 8, 12\} = 8$. Flow $= 8$.
   - **Step 2 ($P_2 = s \to a \to t$):** Remaining capacities on $(s,a)$ is $10-8=2$, on $(a,t)$ is $4$. Bottleneck $\Delta_2 = \min\{2, 4\} = 2$. Flow $= 8 + 2 = 10$.
   - **Step 3 ($P_3 = s \to b \to t$):** Remaining capacity on $(s,b)$ is $5$, on $(b,t)$ is $12-8=4$. Bottleneck $\Delta_3 = \min\{5, 4\} = 4$. Flow $= 10 + 4 = 14$.
   - **Step 4 ($P_4 = s \to b \to a \to t$ using backward edge $(b,a)$!):** Wait—can we reach $t$ from $s$ in $G_f$?
     - From $s$, $(s,a)$ is saturated ($f_{sa}=10$), while $(s,b)$ has residual capacity $c_f(s,b) = 5 - 4 = 1$, so $b$ is reachable!
     - Since $f_{ab} = 8 > 0$, the **backward edge $(b, a)$** is in $G_f$ with residual capacity $8$, so $a$ is reachable from $b$!
     - From $a$, edge $(a, t)$ has residual capacity $4 - 2 = 2 > 0$, so $t$ is reachable along $P_4 = s \to b \to a \to t$ with bottleneck $\Delta_4 = \min\{1, 8, 2\} = 1$!
     - Augmenting along $P_4$ sets $f_{sb} = 5$, $f_{ab} = 8 - 1 = 7$, $f_{at} = 2 + 1 = 3$, increasing total flow to **$|f^*| = 15$**.
2. **Part (b) — Min-Cut Certificate:**
   - Now both $(s, a)$ ($10/10$) and $(s, b)$ ($5/5$) are saturated! Thus the reachable set from $s$ in $G_{f^*}$ is $X = \{s\}$.
   - Cut capacity $c(\{s\}, \{a, b, t\}) = c(s, a) + c(s, b) = 10 + 5 = 15 = |f^*|$, certifying optimality!

</details>

---
### Exam Problem 9: LP Formulation, Duality & Optimality Certificates (Lectures 9–10)
Consider the Primal LP:

$$
\max \; 4x_1 + 5x_2 \quad \text{s.t.} \quad x_1 + 2x_2 \le 6 \;\;(y_1), \quad 2x_1 + x_2 \le 6 \;\;(y_2), \quad x_1, x_2 \ge 0
$$

1. **(a)** Write the Dual LP.
2. **(b)** Determine the primal optimal vertex $x^*$ and dual optimal vertex $y^*$, and verify optimality using Weak Duality and Complementary Slackness.

<details><summary>Full Rubric Solution</summary>

1. **Part (a) — Dual LP:**

   $\displaystyle \min \; 6y_1 + 6y_2 \quad \text{s.t.} \quad y_1 + 2y_2 \ge 4, \quad 2y_1 + y_2 \ge 5, \quad y_1, y_2 \ge 0$

2. **Part (b) — Optimal Solutions & Certificates:**
   - **Primal intersection of the two constraints:** Solving $x_1 + 2x_2 = 6$ and $2x_1 + x_2 = 6$ gives **$x^* = (2, 2)$**, which is feasible ($x^* \ge 0$) with objective value $c^\top x^* = 4(2) + 5(2) = 18$.
   - **Dual intersection of the two dual constraints:** Since $x_1^* > 0$ and $x_2^* > 0$, both dual constraints must be tight by complementary slackness: solving $y_1 + 2y_2 = 4$ and $2y_1 + y_2 = 5$ gives **$y^* = (2, 1)$**, which is dual feasible ($y^* \ge 0$) with objective value $b^\top y^* = 6(2) + 6(1) = 18$.
   - Since $c^\top x^* = 18 = b^\top y^*$, Weak Duality certifies that both $x^* = (2, 2)$ and $y^* = (2, 1)$ are optimal!

</details>

---

### Exam Problem 10: Farkas' Lemma & Active-Constraint Certificate (Lecture 11)
Let $a_1 = (1, 0)^\top$, $a_2 = (1, 1)^\top$, and $p = (0, 1)^\top$ in $\mathbb{R}^2$.
1. **(a)** Prove that $p \notin C = \text{cone}(a_1, a_2) = \{\lambda_1 a_1 + \lambda_2 a_2 : \lambda_1, \lambda_2 \ge 0\}$.
2. **(b)** Using the geometric projection proof of Farkas' Lemma from Lecture 11, find the closest point $q \in C$ to $p$, construct the separating vector $w = q - p$, and verify that $a_1^\top w \ge 0$, $a_2^\top w \ge 0$, and $p^\top w < 0$.

<details><summary>Full Rubric Solution</summary>

1. **Part (a):** Any point in $C$ has coordinates $\lambda_1(1, 0) + \lambda_2(1, 1) = (\lambda_1 + \lambda_2, \lambda_2)$. Setting this equal to $p = (0, 1)$ requires $\lambda_2 = 1$ and $\lambda_1 + \lambda_2 = 0 \implies \lambda_1 = -1 < 0$, which violates $\lambda_1 \ge 0$. Thus $p \notin C$.
2. **Part (b):**
   - Minimize $\|(\lambda_1 + \lambda_2, \lambda_2) - (0, 1)\|_2^2 = (\lambda_1 + \lambda_2)^2 + (\lambda_2 - 1)^2$ over $\lambda_1, \lambda_2 \ge 0$. Since $\lambda_1 \ge 0$ only increases $(\lambda_1 + \lambda_2)^2$, set $\lambda_1 = 0$; minimizing $\lambda_2^2 + (\lambda_2 - 1)^2$ gives $\lambda_2 = 1/2$.
   - Thus the closest point in $C$ to $p$ is **$q = (1/2, 1/2)^\top$**, and $v = p - q = (-1/2, 1/2)^\top$, so **$w = q - p = (1/2, -1/2)^\top$** (or scaled by $2$: $w = (1, -1)^\top$).
   - **Verification:** $a_1^\top w = 1 \ge 0$, $a_2^\top w = 1 - 1 = 0 \ge 0$, and $p^\top w = -1 < 0$.

</details>

---
### Exam Problem 11: Convex Optimization & Smooth Projected Gradient Descent (Lectures 12–13)
Consider the constrained regularized least-squares problem on the box $K = [-1, 1]^d$:

$$
\min_{x \in K} \; f(x) = \frac{1}{2}\|Ax - b\|_2^2 + \frac{\mu}{2}\|x\|_2^2 \qquad (\mu > 0)
$$

1. **(a)** Compute $\nabla f(x)$ and $\nabla^2 f(x)$, prove that $f$ is convex and $\beta$-smooth, and express $\beta$ in terms of $\lambda_{\max}(A^\top A)$ and $\mu$.
2. **(b)** State the Projected Gradient Descent update for $x_{t+1}$, specify the smooth step size $\eta$, and state the number of iterations $T$ needed to guarantee $f(x_T) - f(x^*) \le \varepsilon$.

<details><summary>Full Rubric Solution</summary>

1. **Part (a) — Gradient, Hessian, Convexity & Smoothness:**
   - $\nabla f(x) = A^\top(Ax - b) + \mu x$, and $\nabla^2 f(x) = A^\top A + \mu I$.
   - For any $v \in \mathbb{R}^d$, $v^\top \nabla^2 f(x) v = \|Av\|_2^2 + \mu \|v\|_2^2 \ge \mu \|v\|_2^2 > 0$, so $\nabla^2 f(x) \succeq \mu I \succeq 0$ ($f$ is convex).
   - Moreover, $v^\top \nabla^2 f(x) v \le (\lambda_{\max}(A^\top A) + \mu)\|v\|_2^2$, so $f$ is **$\beta$-smooth** with **$\beta = \lambda_{\max}(A^\top A) + \mu$**.
2. **Part (b) — Update, Step Size & Iteration Complexity:**
   - Unconstrained step: $y_{t+1} = x_t - \eta\left(A^\top(Ax_t - b) + \mu x_t\right)$ with $\eta = \frac{1}{\beta} = \frac{1}{\lambda_{\max}(A^\top A) + \mu}$.
   - Box projection $x_{t+1} = \Pi_K(y_{t+1})$ clips each coordinate: $(x_{t+1})_i = \min\{1, \max\{-1, (y_{t+1})_i\}\}$.
   - Starting from $x_0 = 0 \in K$, $\|x_0 - x^*\|_2 \le \sqrt{d} = D$. Thus $f(x_T) - f(x^*) \le \frac{\beta d}{2T} \implies T = \left\lceil \frac{(\lambda_{\max}(A^\top A) + \mu) d}{2\varepsilon} \right\rceil = O(\beta d / \varepsilon)$ iterations suffice.

</details>

---

### Exam Problem 12: Approximation Algorithms — $d$-Uniform Hypergraph Vertex Cover & $k$-Path Packing (Lectures 14–15)
1. **(a)** In the **$d$-Uniform Hypergraph Vertex Cover (Hitting Set)** problem, each hyperedge $e \in E$ is a subset of **exactly $d$ vertices** ($|e| = d$), and each vertex $v \in V$ has a nonnegative weight $w_v \ge 0$. Formulate the LP relaxation and design a deterministic threshold-rounding **$d$-approximation algorithm**, proving both feasibility and the $d$-approximation guarantee.
2. **(b)** Give two completely distinct polynomial-time $d$-approximation algorithms when weights are unit ($w_v = 1$): one via **Maximal Disjoint Hyperedge Matching** (Lecture 14 style) and one via **LP Threshold Rounding** (Lecture 15 style).

<details><summary>Full Rubric Solution</summary>

1. **Part (a) — LP Relaxation & Threshold Rounding ($d$-Approximation):**
   - **LP Relaxation:**

     $\displaystyle \min \sum_{v \in V} w_v x_v \quad \text{s.t.} \quad \sum_{v \in e} x_v \ge 1 \;\;\forall e \in E, \qquad x_v \ge 0 \;\;\forall v \in V$

   - **Rounding Rule:** Solve the LP to obtain $x^*$ and output $C = \{v \in V : x_v^* \ge 1/d\}$.
   - **Feasibility Proof:** For every hyperedge $e \in E$ with $|e| = d$, $\sum_{v \in e} x_v^* \ge 1$. By the Pigeonhole Principle (averaging over the $d$ vertices of $e$), $\max_{v \in e} x_v^* \ge \frac{1}{d}$, so at least one vertex of $e$ is placed in $C$.
   - **Approximation Ratio Proof:** For every $v \in C$, $1 \le d \cdot x_v^*$. Hence:

     $\displaystyle \sum_{v \in C} w_v \le \sum_{v \in C} w_v (d \cdot x_v^*) \le d \sum_{v \in V} w_v x_v^* = d \cdot \text{OPT}_{\text{LP}} \le d \cdot \text{OPT}$

2. **Part (b) — Combinatorial Maximal Matching $d$-Approximation (Unit Weights):**
   - Greedily pick a maximal collection $M \subseteq E$ of **pairwise vertex-disjoint hyperedges**, and let $C = \bigcup_{e \in M} e$ include **all $d$ vertices** of each chosen hyperedge $e \in M$.
   - Since $M$ is maximal, every hyperedge $e' \in E$ intersects $C$, so $C$ is a valid cover.
   - Since hyperedges in $M$ are vertex-disjoint, any optimal cover $C^*$ must pick at least $1$ distinct vertex from each $e \in M$, so $\text{OPT} \ge |M|$, while $|C| = d|M| \le d \cdot \text{OPT}$.

</details>

---
## 9. Textbook References & Curated Video Lectures

### 9.1 Primary Textbooks

| Abbrev. | Textbook | Best For |
| :--- | :--- | :--- |
| **DPV** | S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani, *Algorithms*, McGraw-Hill, 2008. | Official CS 6515 bridge text (Divide & Conquer, DP, Graphs, Flows, LP). |
| **KT** | J. Kleinberg and É. Tardos, *Algorithm Design*, Pearson, 2005. | Exchange arguments, Cut Property, Max-Flow/Min-Cut, Knapsack FPTAS, and Approximation. |
| **CLRS** | T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, *Introduction to Algorithms* (4th ed.), MIT Press, 2022. | Strong-induction recurrence proofs, Median-of-Medians, Dijkstra/Prim heaps, and LP Duality. |
| **WS** | D. P. Williamson and D. B. Shmoys, *The Design of Approximation Algorithms*, Cambridge Univ. Press, 2011 ([Free PDF](https://www.designofapproxalgs.com/)). | Lectures 10, 14 & 15: LP rounding, Vertex Cover, Edge-Disjoint Paths, and Metric Facility Location. |
| **Bubeck** | S. Bubeck, *Convex Optimization: Algorithms and Complexity*, FnTML, 2015 ([arXiv:1405.4980](https://arxiv.org/abs/1405.4980)). | Lectures 12 & 13: Bounded-gradient GD ($O(1/\sqrt{T})$), Projected GD, and $\beta$-smooth GD ($O(1/T)$). |
| **MG** | J. Matoušek and B. Gärtner, *Understanding and Using Linear Programming*, Springer, 2007. | Lectures 9–11: Polyhedral geometry, vertices, Cramer's rule, Farkas' Lemma, and Strong Duality. |

---

### 9.2 Lecture-by-Lecture Textbook Chapter Mapping (Lectures 1–15)

| Lecture | Topics Covered | DPV | KT | CLRS (4e) | Specialized Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Lec 1** | Asymptotics ($O,\Omega,\Theta,o,\omega$), $\log(n!)$, Merge Sort | Ch. 0, §2.3 | Ch. 2, §5.1 | Ch. 2–3 | — |
| **Lec 2** | Strong Induction for Recurrences, Master Theorem, Max Difference | §2.2 | §5.2 | §4.3–4.6 | — |
| **Lec 2–3** | Deterministic Selection (Median-of-Medians / BFPRT) | §2.4 | §13.5 | §9.3 | Blum et al. (1973) |
| **Lec 3** | DP Recipe, Largest Contiguous Subarray Sum (Kadane), LCS | §6.1–6.3 | §6.1, §6.6 | §14.4 | — |
| **Lec 4** | Tree DP (Max Independent Set), 0-1 Knapsack (Capacity & Value DPs), Pseudo-Poly | §6.4, §6.7 | §6.2, §6.4 | §14.2 | — |
| **Lec 4–5** | PTAS vs. FPTAS, Knapsack FPTAS via Value Scaling ($O(n^3/\varepsilon)$) | §9.2.4 | §11.8 | §35.5 | WS §3.1 |
| **Lec 5** | Finite-Horizon Markov Decision Processes (MDPs), Bellman Equation | — | — | — | Puterman Ch. 4; Sutton & Barto Ch. 3–4 |
| **Lec 6** | Graph Representations, BFS, Nonnegative Shortest Paths (Dijkstra), MST Cut Property | Ch. 3–4, §5.1 | Ch. 3, §4.4–4.5 | Ch. 20, §21.2, §22.3 | — |
| **Lec 7** | Prim's MST Algorithm ($T \subseteq T^*$), Matchings, Alternating/Augmenting Paths, Berge's Theorem | §5.1.3, §7.3 | §4.5, §7.5 | §21.2, §24.3 | Berge (1957); Lovász & Plummer Ch. 1 |
| **Lec 8** | Maximum Flow, Residual Network $G_f$, Ford-Fulkerson, Edmonds-Karp, Max-Flow Min-Cut | §7.1–7.2 | §7.1–7.3 | §24.1–24.2 | — |
| **Lec 9** | LP Formulations, Canonical Conversions, Convex Polyhedra, Vertices, Cramer's Rule | §7.1, §7.4 | — | §29.1 | MG Ch. 2–4 |
| **Lec 10** | LP Duality, Shadow Prices, Weak/Strong Duality, Path Max-Flow Dual & Cut Rounding | §7.4 | — | §29.2 | MG Ch. 6; WS §4.3 |
| **Lec 11** | Farkas' Lemma (Closest-Point Separation Proof) & Active-Constraint Proof of Strong Duality | — | — | — | MG §6.4–6.5; Boyd & Vandenberghe §5.8 |
| **Lec 12** | Convex Sets & Functions, First/Second-Order Conditions, Bounded-Gradient GD ($O(DG/\sqrt{T})$) | — | — | — | Bubeck §1.2, §3.1 |
| **Lec 13** | Projected Gradient Descent (Contraction Lemma) & $\beta$-Smooth GD ($O(\beta D^2/T)$) | — | — | — | Bubeck §3.1–3.2 |
| **Lec 14** | Greedy Approximation: Vertex Cover ($O(\log n)$ vs. $2$-approx), Directed EDP ($O(\sqrt{m})$) | §9.2.1 | §11.1, §11.3 | §35.1, §35.3 | WS §1.1–1.2; Kleinberg (1996) |
| **Lec 15** | LP Rounding: Weighted Vertex Cover ($2$-approx) & Metric Facility Location ($6$-approx) | §9.2.2 | §11.6 | §35.4 | WS §1.3, §4.5 |

---

### 9.3 Curated Video Lectures by Module

1. **Module 1 (Asymptotics, Recurrences & Median-of-Medians Selection):**
   - **MIT 6.046J / 6.006 (Erik Demaine, Srini Devadas, Charles Leiserson):** *Divide & Conquer, Recurrences, and Deterministic Order Statistics (Median-of-Medians)* — [MIT OpenCourseWare 6.046J](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)
   - **Tim Roughgarden (Stanford / Columbia):** *Algorithms Illuminated, Part 1: Master Method & Linear-Time Selection* — [timroughgarden.org/videos.html](https://timroughgarden.org/videos.html)
2. **Module 2 (Dynamic Programming, Knapsack FPTAS & MDPs):**
   - **MIT 6.006 / 6.046J (Erik Demaine):** *Dynamic Programming I–IV (Subproblems, LCS, Knapsack, Pseudo-Polynomial Time)*
   - **Tim Roughgarden (CS261 / Algorithms Illuminated Part 3 & 4):** *Dynamic Programming & Knapsack FPTAS via Value Scaling*
   - **Pieter Abbeel (UC Berkeley CS188) / David Silver (UCL):** *Markov Decision Processes, Value Iteration, and Bellman Equations*
3. **Module 3 (BFS, Dijkstra, MST Cut Property, Prim, Matchings & Max-Flow Min-Cut):**
   - **MIT 6.046J / 6.006:** *BFS, Dijkstra's Algorithm, Minimum Spanning Trees, and Max-Flow Min-Cut (Ford-Fulkerson & Edmonds-Karp)*
   - **Tim Roughgarden (Stanford CS261 — A Second Course in Algorithms):** *Maximum Flow, Minimum Cuts, and Bipartite Matching (Berge's Theorem)*
4. **Module 4 (Linear Programming, Polyhedral Geometry, LP Duality & Farkas' Lemma):**
   - **Ryan O'Donnell & Anupam Gupta (CMU 15-451 / 15-859):** *Linear Programming, Polyhedra, LP Duality, and Farkas' Lemma (Separation of Convex Cones)*
   - **Tim Roughgarden (Stanford CS261 Lectures 8–11):** *Linear Programming Duality, Complementary Slackness, Max-Flow/Min-Cut as Dual LPs*
5. **Module 5 (Convex Optimization, Projected GD & Smooth GD):**
   - **Stephen Boyd (Stanford EE364a):** *Convex Sets, Convex Functions, Duality, and Gradient Methods* — [Stanford SEE EE364a](https://see.stanford.edu/Course/EE364A)
   - **Sébastien Bubeck & Elad Hazan (Princeton / MSR):** *Oracle Complexity of Convex Optimization: Lipschitz GD, Projected GD, and $\beta$-Smooth GD*
6. **Module 6 (Approximation Algorithms: Greedy, EDP & LP Rounding for Facility Location):**
   - **Anupam Gupta & Ryan O'Donnell (CMU 15-854 Approximation Algorithms):** *Greedy Set/Vertex Cover, Edge-Disjoint Paths, LP Rounding, and Metric Uncapacitated Facility Location*
   - **David Williamson & David Shmoys (Cornell CS 6820):** *LP Relaxations, Threshold Rounding, and Clustering Balls for Facility Location*
