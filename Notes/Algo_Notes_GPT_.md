# Algorithms Study Guide

This guide combines divide-and-conquer, dynamic programming, approximation algorithms, finite-horizon Markov decision processes, and foundational graph algorithms. The recurring design question is:

> **What information must each subproblem return or remember so that the complete problem can be solved efficiently?**

---

## 1. Asymptotic Analysis

Asymptotic notation describes how an algorithm's resource usage grows as the input size $n$ becomes large. Constant factors and lower-order terms are ignored.

### 1.1 Core notation

- **Big-O:** $f(n) \in O(g(n))$ if there exist constants $c>0$ and $n_0$ such that
  $$
  0 \le f(n) \le c g(n) \qquad \text{for every } n \ge n_0.
  $$
  This is an eventual upper bound.

- **Big-Omega:** $f(n) \in \Omega(g(n))$ if there exist constants $c>0$ and $n_0$ such that
  $$
  0 \le c g(n) \le f(n) \qquad \text{for every } n \ge n_0.
  $$
  This is an eventual lower bound.

- **Big-Theta:** $f(n) \in \Theta(g(n))$ when
  $$
  f(n) \in O(g(n)) \quad \text{and} \quad f(n) \in \Omega(g(n)).
  $$
  This is a tight asymptotic bound.

- **Little-o:** $f(n) \in o(g(n))$ if $f$ grows strictly more slowly than $g$, equivalently,
  $$
  \lim_{n\to\infty}\frac{f(n)}{g(n)}=0.
  $$

### 1.2 Useful growth comparisons

$$
1=o(\log n),
$$
$$
\log n=o(n^{0.1}),
$$
$$
n^{0.1}=o(n),
$$
$$
n=o(2^n),
$$
$$
2^n=o(2^{n^2}),
$$
$$
n!=o(n^n).
$$

To show $n!=o(n^n)$, observe that every factor in $n!$ is at most $n$, while a constant fraction of the factors is strictly smaller by a constant factor.

---

## 2. Divide and Conquer

A divide-and-conquer algorithm has three stages:

1. **Divide:** Break the input into smaller subproblems.
2. **Conquer:** Solve the subproblems recursively.
3. **Combine:** Assemble their results.

The running-time recurrence records the number and sizes of recursive calls and the cost of the combine operation.

### 2.1 Merge sort

Merge sort splits an array into two halves, recursively sorts each half, and merges the sorted results.

Its recurrence is

$$
T(n)=2T\left(\frac{n}{2}\right)+cn.
$$

The two recursive calls cost $2T(n/2)$, and merging costs $\Theta(n)$. Therefore,

$$
T(n)=\Theta(n\log n).
$$

**Correctness idea:** Use induction on the input length. The recursive calls correctly sort both halves, and the merge operation outputs every input element exactly once in nondecreasing order.

### 2.2 Proving recurrences with strong induction

A useful proof workflow is:

1. Use a recursion tree or experimentation to guess a bound.
2. State the induction hypothesis for all smaller input sizes.
3. Prove the base cases.
4. Substitute the induction hypothesis into the recurrence.
5. Choose constants large enough to absorb lower-order terms.

Strong induction is especially useful when recursive calls have unequal sizes, such as $\lfloor n/2\rfloor$ and $\lceil n/2\rceil$.

### 2.3 Master theorem

For a recurrence of the form

$$
T(n)=aT\left(\frac{n}{b}\right)+\Theta(n^d),
$$

compare $n^d$ with $n^{\log_b a}$.

| Condition | Solution |
|---|---|
| $d>\log_b a$ | $\Theta(n^d)$ |
| $d=\log_b a$ | $\Theta(n^d\log n)$ |
| $d<\log_b a$ | $\Theta(n^{\log_b a})$ |

For merge sort, $a=2$, $b=2$, and $d=1=\log_2 2$, so

$$
T(n)=\Theta(n\log n).
$$

---

## 3. Better Divide-and-Conquer Summaries

### 3.1 Maximum difference

**Problem:** Find indices $i<j$ that maximize

$$
A[i]-A[j].
$$

This is the largest drop from an earlier element to a later element.

An optimal pair lies entirely in the left half, entirely in the right half, or crosses from the left half to the right half.

#### Basic design

If a recursive call returns only the best difference, finding the crossing answer requires scanning both halves:

$$
T(n)=2T\left(\frac{n}{2}\right)+\Theta(n)=\Theta(n\log n).
$$

#### Enriched-summary design

Have each recursive call return:

- $D$: best difference inside the subarray,
- $M$: maximum element in the subarray,
- $m$: minimum element in the subarray.

Given left and right summaries,

$$
D=\max(D_L,D_R,M_L-m_R),
$$
$$
M=\max(M_L,M_R),
$$
$$
m=\min(m_L,m_R).
$$

The combine operation takes constant time, so

$$
T(n)=2T\left(\frac{n}{2}\right)+\Theta(1)=\Theta(n).
$$

> **Design lesson:** Returning the right extra information can make the combine step dramatically cheaper.

### 3.2 Deterministic selection: median of medians

**Problem:** Find the $k$-th smallest element of an array of distinct values.

Sorting first costs $\Theta(n\log n)$. Median of medians guarantees $\Theta(n)$ worst-case time by selecting a pivot that is not too close to either extreme.

#### Algorithm

1. Partition the elements into groups of five.
2. Sort each group and record its median.
3. Recursively find the median of the group medians.
4. Use that value as the pivot.
5. Partition the original input around the pivot.
6. Recurse only into the side containing the desired rank.

At least roughly $3n/10$ elements are at most the pivot and at least roughly $3n/10$ are at least the pivot. Thus, the larger recursive partition has size at most roughly $7n/10$.

The recurrence is

$$
T(n)\le T\left(\frac{n}{5}\right)+T\left(\frac{7n}{10}\right)+\Theta(n).
$$

Because

$$
\frac{1}{5}+\frac{7}{10}=\frac{9}{10}<1,
$$

the total running time is

$$
T(n)=\Theta(n).
$$

> **Design lesson:** A provably good pivot lets an algorithm discard a constant fraction of the input in every round.

---

## 4. Dynamic Programming

Dynamic programming is useful when a problem has **overlapping subproblems** and an optimal solution can be constructed from optimal solutions to smaller states.

### 4.1 DP design checklist

1. Define each state in plain language.
2. Write a recurrence using smaller states.
3. Identify base cases.
4. Choose a valid evaluation order.
5. Store decisions or parent information if reconstruction is required.

The hardest step is usually selecting a state that remembers exactly what future decisions require.

### 4.2 Largest contiguous sum

**Problem:** Find a contiguous interval with maximum sum. Array entries may be negative, and the empty interval is allowed with value $0$.

Define

$$
M[i]=\text{maximum sum of a nonempty contiguous subarray ending exactly at }i.
$$

Base case:

$$
M[0]=A[0].
$$

Recurrence:

$$
M[i]=\max\bigl(A[i],A[i]+M[i-1]\bigr).
$$

At each position, either start a new interval or extend the best interval ending at the previous position. The final answer is

$$
\max\left(0,\max_{0\le i<n}M[i]\right).
$$

- **Time:** $\Theta(n)$
- **Auxiliary space for the value only:** $O(1)$

To recover endpoints, track when a new interval starts and remember the best interval seen so far.

### 4.3 Longest common subsequence

A **subsequence** preserves order but need not be contiguous. A **substring** must be contiguous.

For sequences $A=a_1a_2\cdots a_n$ and $B=b_1b_2\cdots b_m$, define

$$
D[i,j]=\text{length of an LCS of }A[1..i]\text{ and }B[1..j].
$$

Base cases:

$$
D[0,j]=0,\qquad D[i,0]=0.
$$

Recurrence:

$$
D[i,j]=
\begin{cases}
D[i-1,j-1]+1, & \text{if }a_i=b_j,\\
\max(D[i-1,j],D[i,j-1]), & \text{if }a_i\ne b_j.
\end{cases}
$$

- **Time:** $\Theta(nm)$
- **Space:** $\Theta(nm)$

To recover an LCS, trace backward from $D[n,m]$. Move diagonally and record the symbol on a match; otherwise move to a neighboring cell with the same optimal value. Reverse the recorded symbols at the end.

---

## 5. Tree Dynamic Programming

Root an undirected tree at any vertex. A postorder traversal evaluates children before their parent and is therefore a natural order for tree DP.

### 5.1 Maximum independent set in a tree

An independent set contains no pair of adjacent selected vertices. Let $T_v$ be the subtree rooted at vertex $v$.

Define two states:

$$
I[v]=\text{best independent-set size in }T_v\text{ when }v\text{ is included},
$$

$$
X[v]=\text{best independent-set size in }T_v\text{ when }v\text{ is excluded}.
$$

For each child $u$ of $v$,

$$
I[v]=1+\sum_{u\in \operatorname{children}(v)}X[u],
$$

$$
X[v]=\sum_{u\in \operatorname{children}(v)}\max(I[u],X[u]).
$$

At the root $r$, the answer is

$$
\max(I[r],X[r]).
$$

- **Time:** $\Theta(|V|)$

> **General pattern:** Create one state for every constraint that can pass across the edge between a node and its parent.

---

## 6. Knapsack and Pseudo-Polynomial Time

Each item $i$ has an integer size $s_i$ and positive integer value $v_i$. Given capacity $B$, choose items of total size at most $B$ while maximizing total value.

### 6.1 Value-indexed dynamic programming

Let

$$
V_{\mathrm{sum}}=\sum_{i=1}^{n}v_i.
$$

Define

$$
D[i,v]=\text{minimum total size of a subset of the first }i\text{ items having value exactly }v.
$$

Use $\infty$ when no such subset exists.

Base cases:

$$
D[0,0]=0,
$$

$$
D[0,v]=\infty \qquad \text{for }v>0.
$$

Recurrence:

$$
D[i,v]=
\begin{cases}
D[i-1,v], & v<v_i,\\
\min\bigl(D[i-1,v],s_i+D[i-1,v-v_i]\bigr), & v\ge v_i.
\end{cases}
$$

The answer is

$$
\max\{v:D[n,v]\le B\}.
$$

- **Time:** $O(nV_{\mathrm{sum}})$
- **Space:** $O(nV_{\mathrm{sum}})$, reducible to $O(V_{\mathrm{sum}})$ for the value only

### 6.2 Why the algorithm is pseudo-polynomial

The running time is polynomial in the **numeric magnitudes** of the values, not necessarily in their binary encoding length. A number such as $2^k$ needs only $k+1$ bits to encode, but indexing every value through $2^k$ takes exponentially many steps as a function of $k$.

---

## 7. Knapsack FPTAS

For a maximization problem, a $(1-\varepsilon)$-approximation returns a feasible solution with value at least

$$
(1-\varepsilon)\operatorname{OPT}.
$$

A fully polynomial-time approximation scheme, or **FPTAS**, runs in time polynomial in both the input length and $1/\varepsilon$.

### 7.1 Scaling algorithm

1. Discard every item with $s_i>B$.
2. Let $V=\max_i v_i$ among the remaining items.
3. Set
   $$
   K=\frac{\varepsilon V}{n}.
   $$
4. Scale each value:
   $$
   v_i'=\left\lfloor\frac{v_i}{K}\right\rfloor.
   $$
5. Run the value-indexed knapsack DP using the scaled values.

Each selected item loses less than $K$ through rounding. Since at most $n$ items are selected, total loss is less than

$$
nK=\varepsilon V.
$$

The best feasible single item has value $V$, so $V\le \operatorname{OPT}$. Hence the loss is at most $\varepsilon\operatorname{OPT}$, and the solution value is at least

$$
(1-\varepsilon)\operatorname{OPT}.
$$

Under the unit-cost arithmetic convention, the running time is

$$
O\left(\frac{n^3}{\varepsilon}\right).
$$

> **Design lesson:** Scale objective values to shrink the state space, then bound the total rounding error.

---

## 8. Finite-Horizon Markov Decision Processes

A finite-horizon Markov decision process extends dynamic programming to sequential decisions under uncertainty.

### 8.1 Components

A finite-horizon MDP includes:

- a finite state space $S$,
- a finite action space $A$,
- a starting state $s_1$,
- transition probabilities $p_a(s,s')$,
- immediate rewards $r_a(s)$,
- a time horizon $T$.

The objective is to maximize expected total reward:

$$
\mathbb{E}\left[\sum_{t=1}^{T}r_{a_t}(S_t)\right].
$$

An optimal finite-horizon policy needs to depend only on the current state and the number of actions remaining.

### 8.2 Bellman optimality equation

Define

$$
V(s,t)=\text{maximum expected reward from state }s\text{ with }t\text{ actions remaining}.
$$

Base case:

$$
V(s,0)=0.
$$

For $t\ge1$,

$$
V(s,t)=\max_{a\in A}\left(r_a(s)+\sum_{s'\in S}p_a(s,s')V(s',t-1)\right).
$$

The sum is the **expected** optimal continuation value. The most favorable possible next state is not sufficient; transition probabilities must be considered.

### 8.3 Bottom-up algorithm and complexity

Compute $V(s,t)$ in increasing order of $t$:

1. Set $V(s,0)=0$ for every state $s$.
2. For $t=1,2,\ldots,T$, compute $V(s,t)$ for every state.
3. Store an action attaining the maximum for each state-time pair if policy reconstruction is needed.

With explicit transitions:

- **Time:**
  $$
  O\left(T|A||S|^2\right)
  $$
- **Space for all value layers:**
  $$
  O(T|S|)
  $$
- **Space for the optimal value only:** $O(|S|)$, using two consecutive layers

> **Key insight:** The best action may change with the remaining horizon, so the state must include both the physical state and time remaining.

---

## 9. Graph Representations

A graph is written as

$$
G=(V,E),
$$

where $V$ is the vertex set and $E$ is the edge set. Let

$$
n=|V|,\qquad m=|E|.
$$

Graphs may be directed or undirected, weighted or unweighted.

For an undirected graph, the degree-sum identity is

$$
\sum_{v\in V}\deg(v)=2m.
$$

### 9.1 Common representations

| Representation | Space | Main advantage |
|---|---:|---|
| Adjacency matrix | $O(n^2)$ | Tests whether $(u,v)\in E$ in $O(1)$ time |
| Adjacency lists | $O(n+m)$ | Efficiently scans neighbors; preferred for sparse graphs |

Scanning all adjacency lists takes $O(n+m)$ time.

---

## 10. Breadth-First Search

Breadth-first search finds single-source shortest paths in an **unweighted** graph, where path length is the number of edges.

For a source $s$:

1. Set
   $$
   d(s)=0
   $$
   and set $d(v)=\infty$ for every $v\ne s$.
2. Insert $s$ into a FIFO queue.
3. Repeatedly remove a vertex $u$.
4. For every undiscovered neighbor $v$, set
   $$
   d(v)=d(u)+1,
   $$
   set the parent
   $$
   \pi(v)=u,
   $$
   and enqueue $v$.

BFS explores vertices in nondecreasing order of distance from $s$. Its parent pointers form a shortest-path tree over the reachable vertices.

- **Time with adjacency lists:**
  $$
  O(n+m)
  $$

**Correctness intuition:** If a shorter path to a newly discovered vertex existed, the preceding vertex on that path would lie in an earlier BFS layer and would have discovered it sooner.

---

## 11. Nonnegative Weighted Shortest Paths

For a weighted graph, each edge $e$ has weight $w_e$, and a path's length is the sum of its edge weights. Ordinary BFS is insufficient because edges may have different costs.

### 11.1 Why edge subdivision is insufficient

If every weight is a positive integer, an edge of weight $w$ can be replaced with a path of $w$ unit-weight edges. BFS then works on the expanded graph. However, this creates $w-1$ extra vertices per edge, making the running time depend on the numeric magnitudes of weights rather than their encoding lengths. The method is pseudo-polynomial.

### 11.2 Dijkstra's algorithm

Dijkstra's algorithm computes shortest paths from a source when all edge weights are nonnegative.

Initialization:

$$
d(s)=0,
$$

$$
d(v)=\infty \qquad \text{for }v\ne s.
$$

Store unsettled vertices in a min-priority queue keyed by $d(v)$. Repeatedly extract the unsettled vertex $u$ of minimum tentative distance. For every outgoing edge $(u,v)$, relax it:

$$
\text{if }d(u)+w(u,v)<d(v),
$$

then set

$$
d(v)=d(u)+w(u,v)
$$

and

$$
\pi(v)=u.
$$

### 11.3 Correctness and complexity

When Dijkstra extracts $u$, its tentative distance equals its true shortest-path distance. Nonnegative weights ensure that no later path through an unsettled vertex can produce a cheaper route to an already settled vertex.

With a binary heap:

$$
O((n+m)\log n).
$$

Dijkstra's algorithm does not work in general with negative-weight edges because a vertex may be settled before a later route reduces its true distance.

---

## 12. Minimum Spanning Trees

For a connected, undirected, weighted graph, a minimum spanning tree is a set $T\subseteq E$ that connects all vertices and minimizes

$$
w(T)=\sum_{e\in T}w_e.
$$

An optimal connected solution can always be taken to be a tree. If a connected subgraph contains a cycle, removing a maximum-weight edge from that cycle preserves connectivity and does not increase cost.

### 12.1 Cuts and the cut property

For $S\subset V$, the cut $(S,V\setminus S)$ consists of edges with one endpoint in $S$ and the other in $V\setminus S$.

**Cut property:** If $e$ is a minimum-weight edge crossing a cut, then at least one MST contains $e$. If $e$ is the unique lightest edge crossing the cut, every MST contains $e$.

**Exchange proof pattern:**

1. Start with an MST $T$.
2. If $e\in T$, the claim already holds.
3. Otherwise, add $e$ to $T$, creating a cycle.
4. That cycle contains another edge $f$ crossing the cut.
5. Since $w(e)\le w(f)$, replace $f$ with $e$.
6. The result is a spanning tree no more expensive than $T$, so it is also an MST.

### 12.2 MST versus shortest-path tree

- A **shortest-path tree** minimizes the route from one designated source to each reachable vertex.
- An **MST** minimizes the total cost of a shared network connecting all vertices.

An MST does not necessarily preserve shortest paths from any source.

---

## 13. Algorithm Selection Cheat Sheet

| Problem characteristic | Likely technique | Key state or invariant |
|---|---|---|
| Split into independent subproblems | Divide and conquer | Summary needed by the combine step |
| Repeated overlapping subproblems | Dynamic programming | Minimal information needed for future choices |
| Sequential decisions under uncertainty | Finite-horizon MDP | Current state and remaining horizon |
| Unweighted shortest paths | BFS | Distance layers and parent pointers |
| Nonnegative weighted shortest paths | Dijkstra | Minimum unsettled tentative distance |
| Cheapest network connecting all vertices | MST algorithms | Safe light edge across a cut |
| NP-hard optimization with numeric DP | Pseudo-polynomial DP or FPTAS | Scaled values and bounded rounding loss |

---

## 14. Exam-Focused Checklist

Be able to:

- Define and distinguish $O$, $\Omega$, $\Theta$, and $o$.
- Compare standard growth rates.
- Translate recursive algorithms into recurrences.
- Use recursion trees, the Master theorem, and strong induction.
- Explain why merge sort runs in $\Theta(n\log n)$.
- Improve divide-and-conquer algorithms using enriched summaries.
- Prove the median-of-medians pivot guarantee and linear running time.
- Define DP states, recurrences, base cases, and evaluation orders.
- Trace and reconstruct largest-contiguous-sum and LCS solutions.
- Design include/exclude states for tree DP.
- Explain why value-indexed knapsack is pseudo-polynomial.
- Explain how scaling produces a knapsack FPTAS.
- Derive the finite-horizon MDP Bellman recurrence.
- Compare adjacency matrices and adjacency lists.
- Analyze BFS as $O(n+m)$ and justify its layer invariant.
- Perform Dijkstra relaxations and explain the nonnegative-weight requirement.
- State and apply the MST cut property.
- Distinguish an MST from a shortest-path tree.

---

## 15. Self-Check Questions

1. Why does merge sort do $\Theta(n)$ work per recursion level, and why are there $\Theta(\log n)$ levels?
2. Which extra values make the maximum-difference combine step constant time?
3. Why do groups of five yield the approximate $3n/10$ median-of-medians guarantee?
4. For every DP problem, can you explain one state in plain language?
5. Why does the LCS recurrence discard at least one final symbol when the final symbols differ?
6. Why does including a tree vertex force all its children to be excluded?
7. Why can value-indexed knapsack be exponential in the bit length of the input?
8. How does the FPTAS convert additive rounding loss into a multiplicative guarantee?
9. Why does an MDP use expected continuation value instead of the best possible next state?
10. Why does BFS find shortest paths in unweighted graphs?
11. Which exact edge-weight property makes Dijkstra's settling step valid?
12. How does the MST exchange argument prove that a light cut edge is safe?
13. Why can an MST fail to be a shortest-path tree?

---

## 16. Compact Formula Reference

### Divide and conquer

$$
T_{\text{merge}}(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)
$$

$$
T_{\text{max-difference}}(n)=2T(n/2)+\Theta(1)=\Theta(n)
$$

$$
T_{\text{selection}}(n)\le T(n/5)+T(7n/10)+\Theta(n)=\Theta(n)
$$

### Dynamic programming

$$
M[i]=\max(A[i],A[i]+M[i-1])
$$

$$
D_{\mathrm{LCS}}[i,j]=
\begin{cases}
D[i-1,j-1]+1, & a_i=b_j,\\
\max(D[i-1,j],D[i,j-1]), & a_i\ne b_j
\end{cases}
$$

$$
I[v]=1+\sum_u X[u],\qquad X[v]=\sum_u\max(I[u],X[u])
$$

### Approximation

$$
K=\frac{\varepsilon V}{n},\qquad v_i'=\left\lfloor\frac{v_i}{K}\right\rfloor
$$

$$
\text{Approximate value}\ge(1-\varepsilon)\operatorname{OPT}
$$

### MDP

$$
V(s,t)=\max_{a\in A}\left(r_a(s)+\sum_{s'\in S}p_a(s,s')V(s',t-1)\right)
$$

### Graphs

$$
\sum_{v\in V}\deg(v)=2|E|
$$

$$
T_{\mathrm{BFS}}=O(|V|+|E|)
$$

$$
T_{\mathrm{Dijkstra}}=O((|V|+|E|)\log|V|)
$$

$$
w(T)=\sum_{e\in T}w_e
$$
