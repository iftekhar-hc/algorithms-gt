# CS 6515: Graduate Algorithms — Study Guide
### Lectures 1–6 | Fall 2026 | Instructors: Sahil Singla & Gerandy Brito

---

## Table of Contents
1. [Asymptotic Notation](#1-asymptotic-notation)
2. [Divide and Conquer](#2-divide-and-conquer)
3. [Recurrence Relations & Master Theorem](#3-recurrence-relations--master-theorem)
4. [Maximum Difference Problem](#4-maximum-difference-problem)
5. [Selection & Median Finding](#5-selection--median-finding)
6. [Dynamic Programming (DP)](#6-dynamic-programming)
7. [Largest Contiguous Sum](#7-largest-contiguous-sum)
8. [Longest Common Subsequence (LCS)](#8-longest-common-subsequence-lcs)
9. [Maximum Independent Set in a Tree](#9-maximum-independent-set-in-a-tree)
10. [Knapsack Problem](#10-knapsack-problem)
11. [FPTAS for Knapsack](#11-fptas-for-knapsack)
12. [Markov Decision Processes (MDPs)](#12-markov-decision-processes-mdps)
13. [Graph Representations](#13-graph-representations)
14. [Breadth-First Search (BFS)](#14-breadth-first-search-bfs)
15. [Dijkstra's Algorithm](#15-dijkstras-algorithm)
16. [Minimum Spanning Trees (MST)](#16-minimum-spanning-trees-mst)
17. [Key Exam Dates & Course Info](#17-key-exam-dates--course-info)

---

## 1. Asymptotic Notation

Asymptotic notation describes how the resource usage of an algorithm (time, space) grows as input size *n* becomes large. We count **elementary operations** (addition, subtraction, multiplication, bit operations).

### Big-O (Upper Bound)

> **Definition:** $f(n) = O(g(n))$ if there exist constants $c > 0$ and $n_{0} \in \mathbb{N}$ such that $f(n) \le c\cdot g(n)$ for every $n \ge n_{0}$.

- g is an *eventual upper bound* on f, up to a constant factor.
- Useful limit test: if $\lim_{n\to\infty} f(n)/g(n) < \infty$, then $f(n) = O(g(n))$.
- **Example:** $n^{2} + 2n = O(n^{2})$ because for $n \ge 1$, $n^{2} + 2n \le 3n^{2}$.
- Note: Big-O is an upper bound, **not necessarily tight**. $n^{2} + 2n = O(n^{3})$ is also valid.

### Big-Ω (Lower Bound)

> **Definition:** $f(n) = \Omega(g(n))$ if $g(n) = O(f(n))$. Equivalently, there exist constants $c > 0$ and $n_{0}$ such that $f(n) \ge c\cdot g(n)$ for every $n \ge n_{0}$.

### Little-o and Little-\omega (Strict Bounds)

> **Definition:** $f(n) = o(g(n))$ if, for *every* constant $c > 0$, there exists $n_{0}$ such that $f(n) < c\cdot g(n)$ for every $n \ge n_{0}$.

Equivalently: $\lim_{n\to\infty} f(n)/g(n) = 0$ (f grows *strictly more slowly* than g).

- $f(n) = \omega(g(n))$ means $g(n) = o(f(n))$.

### Big-Θ (Tight Bound)

> **Definition:** $f(n) = \Theta(g(n))$ if both $f(n) = O(g(n))$ AND $f(n) = \Omega(g(n))$.

### Useful Hierarchy (all are o of the next)

$$
1 = o(\log \log n) = o(\log n) = o(n^0.1) = o(n) = o(2^n) = o(2^{n^2})
$$

Also: $n! = o(n^n)$, and $\log(n!) = \Theta(n \log n)$

**Proof sketch for log(n!) = Θ(n log n):**
- Upper bound: $\log(n!) = \log(n^n) = n \log n$ → $O(n \log n)$
- Lower bound: Use only the largest n/2 factors: $n/2 \cdot \log(n/2) = \Theta(n \log n)$

---

## 2. Divide and Conquer

The **divide-and-conquer** paradigm has three steps:
1. **Divide:** Break the problem into smaller subproblems.
2. **Conquer:** Solve each subproblem recursively.
3. **Combine:** Assemble the subproblem solutions into a solution to the original problem.

### Case Study: Merge Sort

**Input:** An array $A[0], A[1], \ldots, A[n-1]$ of n numbers.
**Goal:** Rearrange in nondecreasing order.

**Algorithm:**
1. If $n \le 1$, return A.
2. Divide A into left half $A[0, \ldots, n/2-1]$ and right half $A[n/2, \ldots, n-1]$.
3. Recursively sort each half.
4. Merge the two sorted halves.

**Merge step:** Repeatedly compare the first unmerged element of each half, move the smaller one to the output, and append the unused suffix of the nonempty half. Two sorted arrays each of length n can be merged in $O(n)$ time.

**Correctness:** By induction on n.
- *Base case:* n ≤ 1 is immediate.
- *Inductive step:* The recursive calls correctly sort both halves; the merge step outputs all elements in nondecreasing order exactly once.

**Running time — Recurrence:**

$$
T(n) = 2T(n/2) + cn, T(1) = \Theta(1)
$$

**Solving with Recursion Tree:**

| Level | # Subproblems | Work per subproblem | Total work |
|-------|---------------|---------------------|------------|
| $0$ | $1$ | $cn$ | $cn$ |
| $1$ | $2$ | $cn/2$ | $cn$ |
| $2$ | $4$ | $cn/4$ | $cn$ |
| $i$ | $2^i$ | $cn/2^i$ | $cn$ |

- There are $\log_2 n$ levels; each does $cn$ work.
- The n leaves contribute $\Theta(n)$ total work.
- **Result:** $T(n) = cn\cdot \log_2 n + \Theta(n) = \Theta(n \log n)$

**Takeaway:** Divide and conquer turns a problem into many simpler copies. Its efficiency depends on the size and number of subproblems and the cost of the combine step.

---

## 3. Recurrence Relations & Master Theorem

### Proving Recurrence Bounds by Induction

The general recipe:
1. Use a recursion tree, experimentation, or heuristic to *guess* a bound.
2. Prove that bound by **strong induction**.

**Strong induction:** When proving a bound for T(n), the induction hypothesis is available for every smaller integer. This handles unequal recursive subproblem sizes naturally.

**Example — Merge Sort Recurrence:**

*Theorem:* If c > 0, T(1) > 0 is constant, and for every integer n ≥ 2: $T(n) = T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + cn$, then $T(n) = O(n \log n)$.

*Proof sketch:*
- Induction hypothesis: $T(m) \le Km\cdot \log_2 m$ for every integer m ≥ 2.
- Choose K large enough for base cases m = 2, 3, and so that $K\cdot \log_2(3/2) \ge c$.
- For n ≥ 4, set a = ⌊n/2⌋, b = ⌈n/2⌉. Then a, b ≤ 2n/3.
- By induction: $T(n) \le K(a \log a + b \log b) + cn \le K(a+b)\cdot \log(2n/3) + cn = Kn\cdot \log n + Kn\cdot \log(2/3) + cn \le Kn\cdot \log n$

**Selection-type recurrence:** If $T(n) \le T(\lceil n/5 \rceil) + T(\lceil 7n/10 \rceil) + cn$, then $T(n) = O(n)$.

Key insight: $1/5 + 7/10 = 9/10 < 1$, so the total subproblem size shrinks by a constant fraction.

### Master Theorem

For constants $a \ge 1$, $b > 1$, $d \ge 0$, and the recurrence:

$$
T(n) = aT(n/b) + \Theta(nᵈ), T(1) = \Theta(1)
$$

The solution is:

| Condition | Solution |
|-----------|----------|
| $d > log_b(a)$ | $T(n) = \Theta(nᵈ)$ — root work dominates |
| $d = log_b(a)$ | $T(n) = \Theta(nᵈ \log n)$ — balanced |
| $d < log_b(a)$ | $T(n) = \Theta(n^(log_b a))$ — leaves dominate |

This compares the work $nᵈ$ performed at the root with the total leaf growth $n^(log_b a)$.

**Examples:**
- Merge sort: a=2, b=2, d=1 → $\log_2 2 = 1 = d$ → $\Theta(n \log n)$ ✓
- Binary search: a=1, b=2, d=0 → $\log_2 1 = 0 = d$ → $\Theta(\log n)$ ✓

---

## 4. Maximum Difference Problem

**Input:** Numbers $A[0], A[1], \ldots, A[n-1]$.
**Goal:** Find indices $i \le j$ that maximize $A[i] - A[j]$ (largest drop from earlier to later element).

**Example:** $A = [2, 5, 1, 7, 3, 2, 4, 6]$ → optimal value is $7 - 2 = 5$, at $i = 3, j = 5$.

### Approach 1: Return Only Best Difference — O(n log n)

Split into left and right halves. An optimal pair either:
1. Both indices in left half
2. Both indices in right half
3. i in left half, j in right half → need $\max(A_{left}) - \min(A_{right})$

Requires scanning to find max/min → T(n) = 2T(n/2) + O(n) = $\Theta(n\log n)$

### Approach 2: Return a Richer Summary — O(n)

Each recursive call returns three quantities:
- **D:** maximum difference
- **M:** maximum element
- **m:** minimum element

For a single element x, return (0, x, x).

Given summaries (D_L, M_L, m_L) and (D_R, M_R, m_R):

$$
\begin{aligned}
D = \max{D_{L}, D_{R}, M_{L} - m_{R}} \\
M = \max{M_{L}, M_{R}} \\
m = \min{m_{L}, m_{R}}
\end{aligned}
$$

All three quantities combine in **O(1)** time → T(n) = 2T(n/2) + O(1) = $\Theta(n)$

**Key insight:** By returning *exactly the information the parent needs*, we avoid rescanning and achieve linear time.

---

## 5. Selection & Median Finding

**Input:** Distinct numbers $A[0], \ldots, A[n-1]$ and rank $k \in \{1, 2, \ldots, n}$.
**Goal:** Find the k-th smallest element (k = ⌈n/2⌉ gives the median).

Sorting first takes Θ(n log n). The **Blum-Floyd-Pratt-Rivest-Tarjan** algorithm achieves **deterministic O(n)** time.

**Theorem (Deterministic Selection):** The k-th order statistic of n numbers can be found in O(n) time.

### What Makes a Pivot Good?

Choose pivot p and partition into:
- $L = \{x : x < p}$, $\{p}$, $G = \{x : x > p}$

Once we know |L|, we recurse only on the relevant side (one recursive call).

**Bad case:** If p is the smallest or largest element, the recursive problem has size n-1, giving T(n) ≤ T(n-1) + cn → **quadratic** time.

**Definition (Good Pivot):** p is a *good pivot* if both L and G have size at most $7n/10 + O(1)$. Equivalently, at least 3n/10 elements lie on each side.

### Finding a Good Pivot: Median of Medians

For n divisible by 5 (ignore rounding):
1. **Partition** input into n/5 groups of five.
2. **Sort** each group and record its median. Takes O(n) total (constant-size groups).
3. **Recursively find** the median p of the n/5 group medians. Costs T(n/5).

**Claim:** The median-of-medians pivot p has at least 3n/10 elements ≤ p and at least 3n/10 elements ≥ p.

*Proof:* At least half the group medians are ≥ p. For each such group, the median and two larger elements are all ≥ p. Hence at least $3 \cdot (1/2) \cdot (n/5) = 3n/10$ elements are ≥ p. Symmetric for ≤ p. □

### Discarding One Side

After finding good pivot p, partition in O(n):
- If $k \le |L|$: recurse on L with rank k
- If $k = |L| + 1$: return p
- If $k > |L| + 1$: recurse on G with rank $k - |L| - 1$

Because p is a good pivot, the recursive side has at most 7n/10 + O(1) elements.

### Running Time

$$
T(n) \le T(n/5) + T(7n/10) + cn
$$

This matches the selection-type recurrence, giving **T(n) = O(n)**.

**Takeaway:** A good pivot lets us discard a constant fraction at every step, achieving linear time.

---

## 6. Dynamic Programming

**Dynamic Programming (DP)** is useful when a problem has many smaller *overlapping* subproblems. Instead of resolving the same subproblem repeatedly, we store its answer and reuse it (memoization / bottom-up table filling).

### Four Design Steps

1. **Define** a collection of subproblems, indexed by integers i, j, ...
2. **Write a recurrence** relating each subproblem to smaller ones (i.e., fill array M[i, j, ...]).
3. **Identify base cases** and an evaluation order (usually smallest to largest).
4. **Recover** the desired solution (not just its value), tracing back decisions if needed.

**DP takeaway:** The hardest part is not filling the table — it's choosing a *state* that contains exactly the information needed by the recurrence.

---

## 7. Largest Contiguous Sum

**Input:** Array $A[0], \ldots, A[n-1]$ of numbers (possibly negative).
**Goal:** Find interval [x, y] maximizing $\sum A[i]$ for i from x to y. (Empty interval has value 0.)

**Example:** $A = [5, 15, -30, 10, -5, 40, 10]$ → optimal interval is [10, -5, 40, 10] with value 55.

### Subproblem Definition

$M[i]$ = largest sum of a contiguous subarray **ending exactly at position i**.

Any nonempty interval ending at i either starts at i or extends the best interval ending at i-1:

$$
\begin{aligned}
M[0] = A[0] \\
M[i] = \max{A[i], A[i] + M[i-1]} for i \ge 1
\end{aligned}
$$

The answer is: $\max{0, \max over 0\le i<n of M[i]}$

- **n states**, each takes O(1) time → **O(n) total**
- Only the preceding value M[i-1] is needed → **O(1) auxiliary space** (if only the value is needed)

**Correctness invariant:** After computing M[i], it equals the best sum among all intervals ending at i. Proved by induction: removing A[i] from an interval starting before i leaves one ending at i-1; the recurrence picks the better of extending that interval or starting fresh.

---

## 8. Longest Common Subsequence (LCS)

**Input:** Sequences $A = a_{1}a_{2}\cdot \cdot \cdot aₙ$ and $B = b_{1}b_{2}\cdot \cdot \cdot bₘ$.
- A *subsequence* is obtained by deleting zero or more elements without changing order.
**Goal:** Find the maximum length of a sequence that is a subsequence of both A and B.

**Example:** A = ABCDEFG, B = BCDGKAB → BCDG is a common subsequence of length 4.

### Subproblem Definition (Prefix Subproblem)

$D[i, j]$ = length of a longest common subsequence of $a_{1}\cdot \cdot \cdot aᵢ$ and $b_{1}\cdot \cdot \cdot bⱼ$, for $0 \le i \le n$, $0 \le j \le m$.

### Base Cases and Recurrence

$$
\begin{aligned}
D[0, j] = D[i, 0] = 0 (empty prefix) \\
For i, j \ge 1: \\
D[i, j] = D[i-1, j-1] + 1 if aᵢ = bⱼ \\
D[i, j] = \max{D[i-1, j], D[i, j-1]} if aᵢ \ne bⱼ
\end{aligned}
$$

**Why it works:**
- If $aᵢ = bⱼ$: some LCS ends with this common symbol; what precedes is an LCS of the two shorter prefixes.
- If $aᵢ \ne bⱼ$: a common subsequence cannot use *both* final symbols, so at least one must be discarded.

**Complexity:** Table has (n+1)(m+1) entries, each filled in O(1) → **O(nm) time and space**.

### Recovering an Actual LCS

Start at (n, m) and trace backward:
- If $aᵢ = bⱼ$: output that symbol, move to (i-1, j-1)
- Otherwise: move to the neighboring state with equal value to D[i, j]

Symbols discovered in reverse order. Traceback takes $O(n+m)$ once the table is available.

---

## 9. Maximum Independent Set in a Tree

**Input:** Undirected tree T = (V, E).
**Goal:** Find an *independent set* (no two adjacent vertices) of maximum cardinality.

Root the tree at an arbitrary vertex r. For vertex v, let T_v denote the subtree rooted at v.

### One-State Formulation

$M[v]$ = size of a largest independent set in T_v.

Two possibilities at v:
- **Include v:** none of v's children may be included, but each grandchild roots an independent subproblem.
- **Exclude v:** each child roots an independent subproblem.

$$
\begin{aligned}
M[v] = \max{ 1 + \sum M[u] over grandchildren(v), \\
\sum M[u] over children(v) }
\end{aligned}
$$

For a leaf v: M[v] = 1.

### Two-State Formulation (Cleaner)

$$
\begin{aligned}
I[v] = best size in T_{v} subject to including v \\
X[v] = best size in T_{v} subject to excluding v \\
I[v] = 1 + \sum X[u] over children(v) \\
X[v] = \sum \max{I[u], X[u]} over children(v) \\
Answer = \max{I[r], X[r]}
\end{aligned}
$$

**Why it's useful:** The state says exactly what constraint the parent imposes on the child. This pattern generalizes to many tree DP problems.

**Evaluation order:** Postorder traversal (children before parents). Each vertex appears in the computation of only its parent and grandparent → **O(|V|) total time**.

---

## 10. Knapsack Problem

**Input:** n items; item i has positive integer size $sᵢ$ and positive integer value $vᵢ$. Knapsack capacity B.
**Goal:** Choose $S \subseteq \{1, \ldots, n}$ maximizing $\sum vᵢ$ subject to $\sum sᵢ \le B$.

**Example:** Sizes (6,3,4,2), values (30,14,16,9), B=10 → Items 1 and 3 fit exactly, total value 46.

Knapsack is **NP-hard**, so we don't expect a polynomial-time algorithm in the usual bit-length sense. However, there is a DP polynomial in the *numeric values* of the input.

### Value-Indexed DP

Let $V_{sum} = \sum vᵢ$ (sum of all values).

**Subproblem:** $D[i, v]$ = minimum total size of a subset of the first i items having total value *exactly* v. Set D[i, v] = +\infty if no such subset exists.

**Base cases:**

$$
\begin{aligned}
D[0, 0] = 0 \\
D[0, v] = +\infty for v > 0
\end{aligned}
$$

**Recurrence for i > 1:**

$$
\begin{aligned}
D[i, v] = \min{D[i-1, v], sᵢ + D[i-1, v - vᵢ]} if v \ge vᵢ \\
D[i, v] = D[i-1, v] if v < vᵢ
\end{aligned}
$$

The answer is the largest v for which $D[n, v] \le B$.

**Complexity:** Table has O(n·V_sum) entries → $O(nV_sum) = O(n^{2} \max vᵢ)$ time.

### Why This Is Pseudo-Polynomial

Writing integer x in binary takes Θ(log x) bits. The DP time depends on the *values* themselves, not their bit lengths. For example, $vᵢ = 2^k$ needs only k+1 bits, but iterating over every value up to $vᵢ$ takes exponential time in k.

An algorithm polynomial in numeric magnitudes of integer inputs but not necessarily in their encoding length is called **pseudo-polynomial**.

---

## 11. FPTAS for Knapsack

The pseudo-polynomial DP is slow only because the value axis can be enormous. The idea: **round values** so the table becomes small, while losing only a small fraction of the objective.

### Approximation Terminology

- A **(1 - ε)-approximation** returns a feasible solution of value ≥ (1 - ε)·OPT, where 0 < ε < 1.
- **PTAS** (polynomial-time approximation scheme): poly time for every fixed ε.
- **FPTAS** (fully polynomial-time approximation scheme): poly time in both input length *and* 1/ε.

### The Algorithm

1. Discard items with $sᵢ > B$ (they can never be selected).
2. Let $V_{max} = \max vᵢ$. (An item attaining V_max is feasible alone, so V_max ≤ OPT.)
3. Choose scaling unit: $K = \varepsilonV_max / n$.
4. Round each value: $v̂ᵢ = \lfloor vᵢ / K \rfloor$.
5. Run the value-indexed DP on scaled values v̂ᵢ. Let Ŝ be the feasible subset with maximum total scaled value.

**Theorem (Knapsack FPTAS):** For every 0 < ε < 1, the scaling algorithm returns a feasible set Ŝ with $v(Ŝ) \ge (1 - \varepsilon)\cdot OPT$. Running time: $O(n^3/\varepsilon)$.

### Running Time Analysis

Each scaled value satisfies: $v̂ᵢ \le vᵢ/K \le V_{max}/K = n/\varepsilon$.

Therefore: $\sum v̂ᵢ \le n^{2}/\varepsilon$, and the DP takes $O(n \cdot n^{2}/\varepsilon) = O(n^{3}/\varepsilon)$ — polynomial in n and 1/ε.

### Approximation Guarantee

Rounding down loses less than K on each item: $vᵢ - K < K\cdot v̂ᵢ \le vᵢ$.

Let S* be an optimal solution:

$$
\begin{aligned}
v(Ŝ) \ge K\cdot \sum v̂ᵢ (for i in Ŝ) \\
\ge K\cdot \sum v̂ᵢ (for i in S*, since Ŝ maximizes scaled value) \\
> \sum (vᵢ - K) (for i in S*) \\
\ge OPT - nK \\
= OPT - \varepsilonV_max \\
\ge (1 - \varepsilon)\cdot OPT
\end{aligned}
$$

**What to notice:** The algorithm is the same DP — we only changed the numbers used to index its states, trading a controlled amount of objective value for a polynomial number of states.

---

## 12. Markov Decision Processes (MDPs)

### Motivation

In knapsack, each decision determined the next subproblem. Now we consider decisions with *uncertain* outcomes: an action leads to a **distribution** over possible next states.

### Formal Definition

A finite-horizon MDP consists of:
- A finite **state space** S
- A finite **action space** A
- A **starting state** s₁ \in S
- **Transition probabilities** $p_{a}(s, s') \ge 0$ with $\sumₛ' p_{a}(s, s') = 1$ for every a, s
- An **immediate reward** $r_{a}(s) \in ℝ$ for taking action a in state s
- A **time horizon** T

When action aₜ is taken in state Sₜ, reward $r_{a_{t}}(S_{t})$ is received, and next state Sₜ₊₁ is drawn from $p_{a_{t}}(S_{t}, \cdot )$.

**Objective:** Maximize $E[\sum_{t}₌_{1}ᵀ r_{a_{t}}(S_{t})]$

Storage: transition table has Θ(|A|·|S|²) entries.

### Bellman Recurrence (Optimal Value)

$V^*(s,t)$ = maximum expected total reward when current state is s and exactly t actions remain.

**Base case:** $V*(s, 0) = 0$ for every s \in S.

**Bellman optimality equation (t ≥ 1):**

$$
V^*(s,t) = max_{a \in A} \{ r_{a}(s) + \sum_{s' \in S} p_{a}(s, s') \cdot V^*(s',t-1) }
$$

**Key observations:**
1. There is an optimal policy whose action depends only on the **current state** and **number of steps remaining** (not the earlier history).
2. There is an optimal **deterministic** policy — randomizing among actions cannot improve on the best action's expected value.

### Bottom-Up Algorithm

1. Set $V[s, 0] = 0$ for every state s.
2. For t = 1, 2, ..., T and every s, evaluate the Bellman expression for each action a.
3. Store both $V[s, t]$ and $act[s, t]$ (the action attaining the maximum).
4. Execute: starting in s₁ with T steps, use $act[s, t]$ and decrement t after each transition.

**Theorem:** An optimal finite-horizon policy can be computed in **O(T·|A|·|S|²)** time and **O(T·|S|)** space.

---

## 13. Graph Representations

A **graph** is G = (V, E), where V is a set of vertices and E is a set of edges. Write n = |V| and m = |E|. Graphs may be directed or undirected, weighted or unweighted.

For an undirected graph, the degree deg(v) is the number of edges incident to v, and:

$$
\sum_{v \in V} deg(v) = 2m
$$

| Representation | Space | Typical Operation |
|----------------|-------|-------------------|
| Adjacency matrix | Θ(n²) | Test (u,v) \in E in O(1) |
| Adjacency lists | Θ(n + m) | Scan all neighbors in Θ(deg(u)) |

**Adjacency lists** are the default for sparse-graph algorithms because scanning all lists costs Θ(n + m).

---

## 14. Breadth-First Search (BFS)

In an **unweighted** graph, path length = number of edges. BFS explores vertices in nondecreasing order of their shortest-path distance from a source s.

### Algorithm

1. Initialize $\operatorname{dist}[s] = 0$; set all other distances to +\infty.
2. Place s in a first-in, first-out **queue**.
3. Repeatedly remove a vertex u from the queue. For every neighbor v not yet discovered:
   - Set $\operatorname{dist}[v] = \operatorname{dist}[u] + 1$, $parent[v] = u$
   - Append v to the queue.

BFS processes distance layers L₀, L₁, L₂, ... in order.

**Theorem (BFS Correctness):** When BFS finishes, $\operatorname{dist}[v]$ is the minimum number of edges on an s-v path for every reachable v. Parent pointers form a shortest-path tree.

**Proof idea:** When v is first discovered from u, BFS has found a path of length $\operatorname{dist}[u] + 1$. If a shorter path to v existed, its preceding vertex would have belonged to an earlier layer and would have discovered v first.

**Running time:** Each vertex enters the queue once and each adjacency-list entry is scanned once → $O(n+m)$.

---

## 15. Dijkstra's Algorithm

For **weighted** graphs with nonnegative edge weights, Dijkstra's algorithm maintains a tentative distance d[v] and repeatedly settles the unsettled vertex of minimum tentative distance.

### Algorithm

1. Set $d[s] = 0$, $d[v] = +\infty$ for v ≠ s. Store unsettled vertices in a **min-priority queue** keyed by d[v].
2. Extract vertex u of minimum key; mark it settled.
3. For every outgoing edge (u, v) with v unsettled, **relax** it: if $d[u] + w(u,v) < d[v]$, update $d[v]$ and set $parent[v] = u$.
4. Repeat until priority queue is empty.

**Theorem (Dijkstra Correctness):** If all edge weights are nonnegative, then whenever a vertex u is extracted, $d[u]$ equals the true shortest-path distance from s to u.

**Proof idea:** Suppose u is the first incorrectly settled vertex. Let (x, y) be the first edge on a shortest path leaving the settled set. Since x was settled correctly and weights are nonneg, $d[y] \le \operatorname{dist}(s, u)$, but then u wouldn't have minimum key — contradiction.

**Running time with binary heap:** n extract-min + at most m decrease-key operations → $O((n+m)\log n)$.

**Fibonacci heap improvement (optional):** Decrease-key in O(1) amortized → $O(m+n\log n)$.

> ⚠️ **Dijkstra fails with negative edge weights** — the proof uses nonnegativity to conclude that a subpath is no longer than the full path.

### Pseudo-Polynomial Reduction (for context)

For positive integer weights: replace each edge of weight w with a path of w unit edges, reducing to unweighted BFS. Size depends on numeric weights → pseudo-polynomial.

---

## 16. Minimum Spanning Trees (MST)

**Input:** Connected, undirected graph G = (V, E) with nonneg edge weights w: E → ℝ≥0.
**Goal:** Find T \subseteq E that connects all vertices and minimizes $w(T) = \sum_{e \in T} w(e)$.

**Observation:** An optimal solution is a tree. If a connected solution contains a cycle, remove a max-weight edge on that cycle — connectivity is preserved and cost doesn't increase.

### Cut Property

For ∅ ≠ S \subseteq V, the **cut (S, V\S)** consists of all edges with one endpoint in S and the other outside S.

**Theorem (Cut Property):** Let e be a minimum-weight edge crossing any cut (S, V\S). There is a minimum spanning tree containing e. If e is the *unique* lightest crossing edge, every MST contains e.

**Proof:** Let T be an MST. If e \in T, done. Otherwise, adding e to T creates a cycle. The cycle crosses from S to V\S using e, so it must cross back on some edge f \in T. By choice of e, $w(e) \le w(f)$. Then $T' = (T \cup \{e\}) \setminus \{f\}$ is a spanning tree with $w(T') \le w(T)$, so T' is also an MST containing e. □

**Prim's Algorithm** (teased for next lecture): The cut property immediately yields Prim's MST algorithm — grow the MST one edge at a time by always choosing the lightest crossing edge for the current settled set.

---

## 17. Key Exam Dates & Course Info

### Exams
| Exam | Date | Topics |
|------|------|--------|
| Exam 1 | September 22 | Part 1 (Divide & Conquer, DP, Graph Algorithms) |
| Exam 2 | October 27 | Part 2 (LP, Convex Optimization, Approx Algorithms) |
| Exam 3 | November 19 | Part 3 (Randomized Algorithms, Complexity Theory) |
| Final | December 10/11 | Cumulative |

- The worst exam grade is dropped. If happy with first 3 exam grades, the final is optional.
- Practice exam available on Piazza.

### Grading
- Exams: **75%**, Homework: **25%**
- Grade thresholds: A ≥ 90%, B ≥ 80%, C ≥ 70%, D ≥ 60% (thresholds may only lower)

### Homework
- 6 problem sets, ~25 problems total (~4 per set)
- Best 15 problems used for grade; lowest-scoring are dropped
- Must be typed PDF (LaTeX strongly recommended); handwritten not accepted
- Submitted via Gradescope

### Platforms
- **Piazza:** announcements, lecture notes, discussions
- **Canvas:** grades, links
- **Gradescope:** homework submission and grading

### Recommended References
- *Algorithms* by Dasgupta, Papadimitriou, and Vazirani (free PDF available)
- *Algorithms* by Erickson (free at jeffe.cs.illinois.edu/teaching/algorithms)
- *Algorithm Design* by Kleinberg and Tardos
- *Introduction to Algorithms* (CLRS) by Cormen, Leiserson, Rivest, and Stein
- *Algorithms Illuminated* by Roughgarden (videos at algorithmsilluminated.org)

---

## Quick Reference: Algorithm Complexities

| Algorithm / Problem | Time Complexity | Notes |
|---------------------|----------------|-------|
| Merge Sort | Θ(n log n) | Optimal for comparison sort |
| Maximum Difference | Θ(n) | Return richer summary |
| Deterministic Selection (Median of Medians) | O(n) | Groups of 5; good pivot |
| Largest Contiguous Sum | O(n) | DP; M[i] = best ending at i |
| LCS | O(nm) | Prefix subproblem D[i,j] |
| Max Independent Set in Tree | O(\|V\|) | Postorder DP |
| Knapsack (exact) | O(nV_sum) | Pseudo-polynomial |
| Knapsack FPTAS | O(n³/ε) | (1-ε)-approx; true poly |
| Finite-Horizon MDP | O(T·\|A\|·\|S\|²) | Bellman recurrence |
| BFS | O(n + m) | Unweighted shortest paths |
| Dijkstra (binary heap) | O((n+m) log n) | Nonneg weights only |
| Dijkstra (Fibonacci heap) | O(m + n log n) | Optional; theoretical |
| MST (Prim's) | O((n+m) log n) | Cut property → greedy |

---

*Study tip: For each algorithm, practice (1) stating the subproblem/recurrence precisely, (2) proving correctness, and (3) analyzing the running time. These three steps reflect how the course evaluates solutions.*
