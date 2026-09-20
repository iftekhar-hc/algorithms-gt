# CS 6515 Graduate Algorithms — Exam 1 Study Guide

**Coverage:** Lectures 1–8 (asymptotics, divide-and-conquer, DP, graphs, matching, max-flow)  
**Instructors:** Sahil Singla and Gerandy Brito, Fall 2026  
**Exam date (from notes):** September 22

Use this guide as a closed-book rehearsal: for each algorithm, be able to (1) state the problem, (2) write the algorithm or recurrence, (3) prove correctness with an invariant, and (4) give the running time with justification.

---

## How to study

- Recite definitions and theorem statements from memory before looking at proofs.
- For every recurrence, be ready to prove the bound by **strong induction**, not only by naming the Master Theorem.
- For graph algorithms, always name the invariant, the progress step, and the optimality certificate.
- Work the lecture examples by hand (max-difference, LCS, knapsack, Prim, matching, flow).

---

## 1. Asymptotic notation

For input size \(n\), \(T(n)\) (or \(f(n)\)) counts elementary operations. We care about growth as \(n \to \infty\).

### Definitions

Let \(f, g : \mathbb{N} \to \mathbb{R}_{\ge 0}\).

| Notation | Meaning | Formal condition |
|---|---|---|
| \(f(n) = O(g(n))\) | eventual upper bound, up to a constant | \(\exists\, c > 0,\, n_0\) such that \(f(n) \le c\, g(n)\) for all \(n \ge n_0\) |
| \(f(n) = \Omega(g(n))\) | eventual lower bound | \(g(n) = O(f(n))\); equivalently \(f(n) \ge c\, g(n)\) for large \(n\) |
| \(f(n) = \Theta(g(n))\) | tight bound | both \(O\) and \(\Omega\) |
| \(f(n) = o(g(n))\) | strictly slower | for **every** \(c > 0\), eventually \(f(n) < c\, g(n)\); if \(g > 0\), equivalent to \(\lim f/g = 0\) |
| \(f(n) = \omega(g(n))\) | strictly faster | \(g(n) = o(f(n))\) |

**Limit test for Big-O.** If \(\lim_{n\to\infty} f(n)/g(n) < \infty\), then \(f = O(g)\).

**Important:** Big-O is an upper bound, not necessarily tight. \(n^2 + 2n = O(n^2)\) and also \(O(n^3)\).

### Standard growth chain

\[
1 = o(\log\log n) = o(\log n) = o(n^{0.1}) = o(n) = o(2^n) = o(2^{n^2}).
\]

Also \(n! = o(n^n)\), because
\[
\frac{n^n}{n!} = \prod_{i=1}^{n} \frac{n}{i} \to \infty.
\]

### Exercise you should be able to prove

**Claim.** \(\log(n!) = \Theta(n \log n)\).

- Upper bound: \(n! \le n^n\), so \(\log(n!) \le n\log n\).
- Lower bound: keep only the largest \(n/2\) factors: \(n! \ge (n/2)^{n/2}\), so \(\log(n!) \ge (n/2)\log(n/2) = \Omega(n\log n)\).

---

## 2. Divide and conquer

Three steps:

1. **Divide** the problem into smaller subproblems.
2. **Conquer** by solving them recursively.
3. **Combine** the answers into a solution for the original instance.

Efficiency depends on (a) number and size of subproblems and (b) combine cost.

### 2.1 Merge sort

**Input.** Array \(A[0..n-1]\) of numbers (constant-bit comparisons).  
**Goal.** Sort into nondecreasing order.

**Algorithm.**

1. If \(n \le 1\), return \(A\).
2. Split into left and right halves.
3. Recursively sort each half.
4. Merge the two sorted halves.

**Merge.** Repeatedly take the smaller of the two unmerged heads; append the unused suffix at the end. Two sorted arrays of length \(n\) merge in \(O(n)\) time.

**Correctness (induction on \(n\)).** Base \(n\le 1\) is immediate. Inductive step: recursive calls sort the halves; merge outputs every element exactly once in nondecreasing order.

**Recurrence.**
\[
T(n) = 2T(n/2) + cn,\qquad T(1)=\Theta(1).
\]
More carefully,
\[
T(n) = T(\lfloor n/2\rfloor) + T(\lceil n/2\rceil) + cn.
\]

**Recursion tree.** Level \(i\) has \(2^i\) subproblems of size \(n/2^i\); total merge work per level is \(cn\). There are \(\log_2 n\) non-leaf levels plus \(\Theta(n)\) leaf work, so
\[
T(n) = cn\log_2 n + \Theta(n) = \Theta(n\log n).
\]

### 2.2 Maximum difference

**Input.** Numbers \(A[0..n-1]\).  
**Goal.** Indices \(i\le j\) maximizing \(A[i]-A[j]\) (largest drop from an earlier element to a later one).

**Example.** \(A = [2,5,1,7,3,2,4,6]\). Optimum \(7-2=5\) at \(i=3\), \(j=5\).

An optimal pair is one of three types: both in the left half, both in the right half, or \(i\) left and \(j\) right.

**Approach 1 (return only the best difference).** Crossing candidate needs a scan for \(\max(A_{\text{left}}) - \min(A_{\text{right}})\):
\[
T(n) = 2T(n/2) + O(n) = \Theta(n\log n).
\]

**Approach 2 (richer summary).** Return \((D, M, m)\): best difference, max element, min element.

- Single element \(x\): \((0,x,x)\).
- Combine:
  \[
  D = \max\{D_L, D_R, M_L - m_R\},\quad
  M = \max\{M_L,M_R\},\quad
  m = \min\{m_L,m_R\}.
  \]

Combine is \(O(1)\), so
\[
T(n) = 2T(n/2) + O(1) = \Theta(n).
\]

**Why it works.** The three candidates in \(D\) are exactly the three pair types. Returning extra information makes the combine cheap.

**Recursion-tree check for \(\Theta(n)\).** At level \(r\) there are \(2^r\) nodes, each doing \(O(1)\) work, for \(O(2^r)\) work. Geometric series over \(\log n\) levels sums to \(\Theta(n)\).

**Takeaway.** Divide-and-conquer gets faster when recursive calls return exactly the extra information needed for a cheap combine, or when a good pivot discards a constant fraction of the input.

---

## 3. Recurrences, strong induction, Master Theorem

**Recipe.** Guess a bound (recursion tree or experiment), then prove it by **strong induction** on integer \(n\). The IH applies to every smaller integer, so floors/ceilings and unequal subproblem sizes are fine.

### 3.1 Merge-sort recurrence is \(O(n\log n)\)

Assume \(T(n) = T(\lfloor n/2\rfloor)+T(\lceil n/2\rceil)+cn\) for \(n\ge 2\).

**IH.** \(T(m) \le K m\log_2 m\) for every \(2\le m < n\).

**Base.** Choose \(K\) large enough for \(m=2,3\) and so that \(K\log_2(3/2)\ge c\).

**Step (\(n\ge 4\)).** Let \(a=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\). Then \(a+b=n\) and \(a,b\le 2n/3\).
\[
\begin{align*}
T(n)
&\le K(a\log_2 a + b\log_2 b)+cn \\
&\le K(a+b)\log_2(2n/3)+cn \\
&= Kn\log_2 n + Kn\log_2(2/3)+cn \\
&\le Kn\log_2 n,
\end{align*}
\]
because \(\log_2(2/3)<0\) and \(K\) was chosen so the negative term absorbs \(cn\).

**Matching lower bound.** Use \(\lfloor n/2\rfloor,\lceil n/2\rceil\ge n/3\) for \(n\ge 2\). Then \(T(n)=\Theta(n\log n)\).

### 3.2 Selection-type recurrence is \(O(n)\)

\[
T(n)\le T(\lceil n/5\rceil)+T(\lceil 7n/10\rceil)+cn.
\]

**IH.** \(T(m)\le Am\) for all \(m<n\). Choose \(A\ge 20c\) large enough for finite base cases.
\[
T(n)\le A\lceil n/5\rceil + A\lceil 7n/10\rceil + cn
\le \tfrac{9}{10}An + 2A + cn
\le \tfrac{19}{20}An + 2A
\le An
\]
for large \(n\). The key is that \(\frac15+\frac{7}{10}=\frac{9}{10}<1\): recursive work is a **strictly smaller constant fraction** of \(n\).

### 3.3 Master Theorem (useful form)

For constants \(a\ge 1\), \(b>1\), \(d\ge 0\),
\[
T(n)=aT(n/b)+\Theta(n^d),\qquad T(1)=\Theta(1):
\]

| Case | Condition | Solution | Intuition |
|---|---|---|---|
| 1 | \(d > \log_b a\) | \(\Theta(n^d)\) | root work dominates |
| 2 | \(d = \log_b a\) | \(\Theta(n^d\log n)\) | every level costs about the same |
| 3 | \(d < \log_b a\) | \(\Theta(n^{\log_b a})\) | leaves dominate |

Compare root work \(n^d\) with leaf growth \(n^{\log_b a}\).

**Common applications.**

- Merge sort: \(a=2\), \(b=2\), \(d=1\), \(\log_2 2=1=d\) \(\Rightarrow \Theta(n\log n)\).
- Max-diff approach 2: \(a=2\), \(b=2\), \(d=0\) \(\Rightarrow \Theta(n)\).
- The selection recurrence is **not** in Master form (unequal subproblem sizes).

---

## 4. Deterministic linear-time selection

**Input.** Distinct numbers \(A[0..n-1]\) and rank \(k\in\{1,\ldots,n\}\).  
**Goal.** The \(k\)-th smallest element (exactly \(k-1\) smaller elements).

Sorting first is \(\Theta(n\log n)\). Blum–Floyd–Pratt–Rivest–Tarjan (median of medians) achieves **deterministic \(O(n)\)**.

### Why a random/arbitrary pivot is not enough

Partition around pivot \(p\) into \(L=\{x:x<p\}\), \(\{p\}\), \(G=\{x:x>p\}\). Recurse on the relevant side.

If \(p\) is always an extreme, \(T(n)\le T(n-1)+cn\) permits **quadratic** time. Need a pivot bounded away from both extremes.

**Good pivot.** Both \(L\) and \(G\) have size at most \(7n/10+O(1)\). Equivalently, at least \(3n/10\) elements lie on each side of \(p\).

### Algorithm (median of medians)

1. Partition into groups of 5 (\(n/5\) groups). Sort each group in \(O(1)\) per group, total \(O(n)\). Record each group median.
2. Recursively select the median \(p\) of the \(n/5\) group medians. Cost \(T(\lceil n/5\rceil)\).
3. Partition around \(p\) in \(O(n)\).
4. If \(k\le |L|\), recurse on \(L\) with rank \(k\).  
   If \(k=|L|+1\), return \(p\).  
   If \(k>|L|+1\), recurse on \(G\) with rank \(k-|L|-1\).

### Why \(p\) is a good pivot

At least half of the group medians are \(\ge p\). In each such group, the median and the two larger elements are \(\ge p\). Hence at least
\[
3\cdot \tfrac12\cdot \tfrac n5 = \tfrac{3n}{10}
\]
elements are \(\ge p\). The symmetric argument gives \(\ge 3n/10\) elements \(\le p\). So the recursive side has size at most \(7n/10+O(1)\).

### Recurrence and time

\[
T(n)\le T(n/5)+T(7n/10)+cn = O(n).
\]

**Exam warning.** You must justify both (i) the \(3n/10\) counting argument and (ii) why \(\frac15+\frac{7}{10}<1\) implies linear time.

---

## 5. Dynamic programming

DP is for **overlapping** subproblems. Store each answer once and reuse it.

### Four design steps

1. Define a collection of subproblems, typically indexed by integers \(i,j,\ldots\).
2. Give a recurrence relating each subproblem to smaller ones.
3. Identify base cases and a valid evaluation order.
4. Recover the actual solution (not only the value), if required.

**Central design question.** What information must a subproblem remember so that it can be extended?

### 5.1 Largest contiguous sum (Kadane)

**Input.** Array \(A[0..n-1]\), possibly negative. Empty interval has value \(0\).  
**Goal.** Interval \([x,y]\) maximizing \(\sum_{i=x}^{y} A[i]\).

**Example.** \(A=[5,15,-30,10,-5,40,10]\). Optimal interval \([10,-5,40,10]\) has value \(55\).

**State.** \(M[i]\) = largest sum of a contiguous subarray **ending exactly at \(i\)**.

\[
M[0]=A[0],\qquad
M[i]=\max\{A[i],\, A[i]+M[i-1]\}\quad (i\ge 1).
\]

Answer:
\[
\max\bigl\{0,\; \max_{0\le i<n} M[i]\bigr\}.
\]

**Time / space.** \(n\) states, \(O(1)\) work each \(\Rightarrow O(n)\) time. Value-only needs \(O(1)\) extra space.

**Invariant.** After computing \(M[i]\), it equals the best sum among intervals ending at \(i\). Removing \(A[i]\) from an interval that starts earlier leaves an interval ending at \(i-1\); the recurrence chooses the better of extending vs. starting anew.

**Recovering endpoints.** Track a start index with each \(M[i]\): if you start anew, set start to \(i\); if you extend, keep the previous start. Then take the pair for the best \(M[i]\) (or empty if all are negative).

**Worked \(M[i]\) for the example.**

| \(i\) | \(A[i]\) | \(M[i]\) |
|---|---|---|
| 0 | 5 | 5 |
| 1 | 15 | 20 |
| 2 | \(-30\) | \(-10\) |
| 3 | 10 | 10 |
| 4 | \(-5\) | 5 |
| 5 | 40 | 45 |
| 6 | 10 | 55 |

### 5.2 Longest common subsequence

**Input.** Sequences \(A=a_1\cdots a_n\), \(B=b_1\cdots b_m\).  
A **subsequence** deletes zero or more elements without reordering. Unlike a substring, positions need not be consecutive.

**Goal.** Maximum length of a common subsequence.

**Example.** \(A=\texttt{ABCDEFG}\), \(B=\texttt{BCDGKAB}\). One LCS is \(\texttt{BCDG}\) of length 4.

**State.** \(D[i,j]\) = LCS length of prefixes \(a_1\cdots a_i\) and \(b_1\cdots b_j\).

**Base.** \(D[0,j]=D[i,0]=0\).

**Recurrence.** For \(i,j\ge 1\):
\[
D[i,j]=
\begin{cases}
D[i-1,j-1]+1 & \text{if } a_i=b_j,\\
\max\{D[i-1,j],\, D[i,j-1]\} & \text{if } a_i\neq b_j.
\end{cases}
\]

**Why.** If last symbols match, some LCS can end with that symbol. If they differ, a common subsequence cannot use both finals, so discard at least one.

**Complexity.** Table size \((n+1)(m+1)\), \(O(1)\) per cell \(\Rightarrow O(nm)\) time and \(O(nm)\) space.

**Traceback (actual LCS).** Start at \((n,m)\):

- if \(a_i=b_j\), output that symbol and go to \((i-1,j-1)\);
- else move to a neighbor whose value equals \(D[i,j]\).

Symbols appear in reverse. Traceback is \(O(n+m)\) after the table is filled. Ties mean multiple LCSs.

### 5.3 Maximum independent set in a tree

**Independent set:** \(S\subseteq V\) with no edge internal to \(S\).  
**Goal.** Maximum cardinality independent set in an undirected tree.

Root the tree at arbitrary \(r\). Let \(T_v\) be the subtree rooted at \(v\).

**One-state formulation.** \(M[v]\) = size of a largest independent set in \(T_v\).
\[
M[v]=\max\left\{
1+\sum_{u\in\text{grandchildren}(v)} M[u],\;
\sum_{u\in\text{children}(v)} M[u]
\right\}.
\]
Leaf: \(M[v]=1\).

- Include \(v\): cannot include children; remaining problems sit at grandchildren.
- Exclude \(v\): each child is an independent subproblem.

**Evaluation order.** Postorder (bottom-up) so children and grandchildren are ready. Total time \(O(|V|)\): each vertex appears in its parent’s and grandparent’s computation.

**Two-state formulation (often cleaner for recovery).**
\[
\begin{align*}
I[v] &= \text{best in }T_v\text{ subject to including }v,\\
X[v] &= \text{best in }T_v\text{ subject to excluding }v.
\end{align*}
\]
\[
I[v]=1+\sum_{u\in\text{children}(v)} X[u],\qquad
X[v]=\sum_{u\in\text{children}(v)}\max\{I[u],X[u]\}.
\]
Answer: \(\max\{I[r],X[r]\}\).

**Pattern.** Create one state for each possible interaction across the edge to the parent.

**Recovery.** At each vertex record whether the optimum included it. If the root includes \(v\), all children must be excluded; if excluded, each child independently takes \(\arg\max\{I[u],X[u]\}\).

### 5.4 0-1 knapsack (exact, value-indexed)

**Input.** Item \(i\) has size \(s_i\) and value \(v_i\) (positive integers); capacity \(B\).  
**Goal.** Subset \(S\) maximizing \(\sum_{i\in S} v_i\) subject to \(\sum_{i\in S}s_i\le B\).

**Example.** Sizes \((6,3,4,2)\), values \((30,14,16,9)\), \(B=10\). Items 1 and 3 fit exactly, value \(46\).

Knapsack is NP-hard. The DP is polynomial in the **numeric values**, not necessarily in bit length.

Let \(V_{\mathrm{sum}}=\sum_i v_i\).

**State.** \(D[i,v]\) = minimum total size of a subset of the first \(i\) items with value **exactly** \(v\), or \(+\infty\) if impossible.

**Base.** \(D[0,0]=0\), \(D[0,v]=+\infty\) for \(v>0\).

**Recurrence.**
\[
D[i,v]=
\begin{cases}
\min\{D[i-1,v],\; s_i+D[i-1,v-v_i]\} & v\ge v_i,\\
D[i-1,v] & v<v_i.
\end{cases}
\]

**Answer.** Largest \(v\) with \(D[n,v]\le B\).

**Correctness.** Subsets of the first \(i\) items either exclude item \(i\) or include it and realize remaining value \(v-v_i\) with items \(1..i-1\). Take the smaller feasible size.

**Time.** \(O(n V_{\mathrm{sum}})=O(n^2\max_i v_i)\).

**Pseudo-polynomial.** Writing integer \(x\) takes \(\Theta(\log x)\) bits. Time depends on the **values** themselves. Example: \(v_i=2^k\) uses \(k+1\) bits, but looping over values up to \(v_i\) is exponential in \(k\).

An algorithm polynomial in numeric magnitudes of integer inputs, but not necessarily in encoding length, is **pseudo-polynomial**.

**Capacity-indexed alternative (know it).** Let \(K[i,b]\) be the maximum value using the first \(i\) items with capacity \(b\). Time \(O(nB)\), also pseudo-polynomial.

**Recovery.** From the maximizing \(v\), if \(D[i,v]=s_i+D[i-1,v-v_i]\) then item \(i\) was taken.

---

## 6. Approximation: knapsack FPTAS

### Language

For a maximization problem, a \((1-\varepsilon)\)-approximation returns a feasible solution of value at least \((1-\varepsilon)\mathrm{OPT}\), where \(0<\varepsilon<1\).

| Term | Meaning |
|---|---|
| PTAS | polynomial time for every **fixed** \(\varepsilon\) |
| FPTAS | time polynomial in **both** input length and \(1/\varepsilon\) |

### Algorithm

1. Discard items with \(s_i>B\). If none remain, return \(\emptyset\).
2. Let \(V_{\max}=\max_i v_i\). A single feasible item gives \(V_{\max}\le\mathrm{OPT}\).
3. Scaling unit \(K=\varepsilon V_{\max}/n\).
4. Scaled values \(\tilde v_i=\lfloor v_i/K\rfloor\).
5. Run the value-indexed DP on \(\tilde v_i\). Let \(\tilde S\) be a feasible subset of maximum total scaled value.

**Theorem.** \(v(\tilde S)\ge (1-\varepsilon)\mathrm{OPT}\) in time \(O(n^3/\varepsilon)\) (unit-cost arithmetic).

### Running time

\(\tilde v_i\le v_i/K\le V_{\max}/K=n/\varepsilon\), so \(\sum_i\tilde v_i\le n^2/\varepsilon\). DP time
\[
O\Bigl(n\sum_i\tilde v_i\Bigr)=O(n^3/\varepsilon),
\]
polynomial in input length and \(1/\varepsilon\).

### Approximation proof (memorize the chain)

Rounding down loses less than \(K\) per selected item: \(v_i-K < K\tilde v_i\le v_i\). Let \(S^*\) be optimal.
\[
\begin{align*}
v(\tilde S)
&\ge K\sum_{i\in\tilde S}\tilde v_i
&&\text{(translate scaled value)}\\
&\ge K\sum_{i\in S^*}\tilde v_i
&&\text{\(\tilde S\) optimal for scaled instance)}\\
&\ge \sum_{i\in S^*}(v_i-K)
&&\text{(rounding loss \(<K\) per item)}\\
&\ge \mathrm{OPT}-nK
= \mathrm{OPT}-\varepsilon V_{\max}
\ge (1-\varepsilon)\mathrm{OPT}.
\end{align*}
\]

Total additive loss \(\le nK=\varepsilon V_{\max}\). Then \(V_{\max}\le\mathrm{OPT}\) converts additive loss into a multiplicative guarantee.

**Design pattern.** Same DP; only the numbers indexing states change. Trade a controlled amount of objective for a polynomial number of states.

**Exercise numbers.** Sizes \((6,3,4,2)\), values \((30,14,16,9)\), \(B=10\), \(\varepsilon=1/2\):
\(V_{\max}=30\), \(K=\varepsilon V_{\max}/n=30/(2\cdot 4)=3.75\).
Scaled values \(\lfloor 30/3.75\rfloor=8\), \(\lfloor 14/3.75\rfloor=3\), \(\lfloor 16/3.75\rfloor=4\), \(\lfloor 9/3.75\rfloor=2\).

---

## 7. Finite-horizon Markov decision processes

Move from deterministic DP to decisions with uncertain outcomes. The principle is unchanged: summarize the future by the value of a smaller state.

### Definition

A finite-horizon MDP consists of:

- finite state space \(S\);
- finite action space \(A\);
- start state \(s_1\);
- transitions \(p_a(s,s')\ge 0\) with \(\sum_{s'}p_a(s,s')=1\);
- immediate reward \(r_a(s)\);
- horizon \(T\).

Taking \(a_t\) in \(S_t\) yields reward \(r_{a_t}(S_t)\); next state is drawn from \(p_{a_t}(S_t,\cdot)\).

**Policy.** Specifies the action at each step; in general it may depend on full history.

**Objective.**
\[
\max_\pi\; \mathbb{E}\Bigl[\sum_{t=1}^{T} r_{a_t}(S_t)\Bigr].
\]

Explicit transition table has \(\Theta(|A||S|^2)\) entries.

### Two lessons from the lecture examples

1. **The optimal first action can depend on remaining horizon.** A long high-reward route may be useless if too few steps remain; with more steps it can dominate a short small reward.
2. **Optimize expected reward, not the best possible outcome.** A risky action with chance of reward \(2\) and chance of \(0\) has continuation value \(1\), which loses to a deterministic \(1.5\).

### Bellman optimality

\(V^*(s,t)\) = maximum expected total reward from state \(s\) with exactly \(t\) actions remaining.

**Base.** \(V^*(s,0)=0\) for every \(s\).

**Recurrence (\(t\ge 1\)).**
\[
V^*(s,t)=\max_{a\in A}\Biggl(
r_a(s)+\sum_{s'\in S} p_a(s,s')\, V^*(s',t-1)
\Biggr).
\]

**Observations (exam-ready).**

- There is an optimal policy depending only on **current state and remaining steps**. History is unnecessary.
- There is an optimal **deterministic** policy: pick an action attaining the max. Randomizing cannot beat the best action’s expected value.

### Bottom-up algorithm

1. Set \(V[s,0]=0\).
2. For \(t=1,\ldots,T\) and every \(s\), evaluate every action.
3. Store \(V[s,t]\) and \(\mathrm{act}[s,t]\).
4. Execute from \(s_1\) with \(T\) steps, decrementing \(t\) after each transition.

**Theorem.** Optimal finite-horizon policy in
\[
O(T|A||S|^2)
\]
time and \(O(T|S|)\) space.

There are \(T|S|\) DP states; each considers \(|A|\) actions and sums over \(|S|\) next states.

**Correctness.** Induction on \(t\). Every policy chooses some first action \(a\); conditional on next state \(s'\), no continuation beats \(V^*(s',t-1)\). Choosing the maximizing first action attains the upper bound.

**Space.** Value-only needs \(O(|S|)\) (keep only layer \(t-1\)). Recovering the full policy needs stored actions or recomputation.

---

## 8. Graph representations, BFS, shortest paths, MSTs

Write \(n=|V|\), \(m=|E|\). For undirected graphs, \(\sum_v \deg(v)=2m\).

### Representations

| Representation | Space | Typical operation |
|---|---|---|
| Adjacency matrix | \(\Theta(n^2)\) | test \((u,v)\in E\) in \(O(1)\) |
| Adjacency lists | \(\Theta(n+m)\) | scan neighbors in \(\Theta(\deg(u))\) |

Default for sparse graphs: adjacency lists. Scanning all lists costs \(\Theta(n+m)\).

### 8.1 Breadth-first search

In an **unweighted** graph, path length is number of edges. BFS from source \(s\) explores vertices in nondecreasing shortest-path distance.

**Algorithm.**

- \(\mathrm{dist}[s]=0\), other distances \(+\infty\); enqueue \(s\).
- Dequeue \(u\). For every undiscovered neighbor \(v\):
  \[
  \mathrm{dist}[v]=\mathrm{dist}[u]+1,\quad \mathrm{parent}[v]=u,
  \]
  then enqueue \(v\).

**Theorem.** When BFS finishes, \(\mathrm{dist}[v]\) is the minimum number of edges on an \(s\)–\(v\) path for every reachable \(v\). Parent pointers form a shortest-path tree.

**Proof idea.** The queue processes one distance layer at a time. When \(v\) is first discovered from \(u\), a path of length \(\mathrm{dist}[u]+1\) is found. A shorter path would have had its predecessor in an earlier layer, which would have discovered \(v\) first. Non-tree edges never skip a layer.

**Time.** Each vertex enqueued once; each adjacency-list entry scanned once: \(O(n+m)\).

### 8.2 Nonnegative weighted shortest paths

Now \(w(e)\ge 0\); path length is the sum of edge lengths.

**Pseudo-polynomial reduction.** Replace an integer-weight-\(w\) edge by \(w\) unit edges and run BFS. Graph size depends on numeric weights, not bit length — only pseudo-polynomial.

### Dijkstra’s algorithm

Maintain tentative distances \(d[v]\); repeatedly settle the unsettled vertex of minimum tentative distance.

1. \(d[s]=0\), \(d[v]=+\infty\) otherwise. Min-priority queue keyed by \(d[v]\).
2. Extract min-key vertex \(u\); mark settled.
3. For every outgoing edge \((u,v)\) with \(v\) unsettled, **relax**: if \(d[u]+w(u,v)<d[v]\), update \(d[v]\) and \(\mathrm{parent}[v]\).
4. Repeat until the queue is empty.

**Theorem.** If all weights are nonnegative, whenever \(u\) is extracted, \(d[u]\) equals the true shortest-path distance \(\mathrm{dist}(s,u)\).

**Proof idea.** Let \(u\) be the first incorrectly settled vertex. On a true shortest \(s\)–\(u\) path, let \((x,y)\) be the first edge leaving the settled set. Vertex \(x\) was settled correctly, so relaxing \((x,y)\) made \(d[y]\) at most the prefix length to \(y\). Nonnegativity implies that prefix is \(\le\) the full path to \(u\). Since \(u\) had minimum key, \(d[u]\le d[y]\le\mathrm{dist}(s,u)\). Every finite tentative distance is the length of some \(s\)–\(u\) path, so \(d[u]\ge\mathrm{dist}(s,u)\). Hence equality.

**Where nonnegativity is used.** The prefix to \(y\) cannot be longer than the path to \(u\) only if remaining edges have nonnegative weight. A negative edge can make Dijkstra settle a wrong distance.

**Running times.**

| Heap | Time |
|---|---|
| Binary heap | \(O((n+m)\log n)\) (\(n\) extract-min, \(\le m\) decrease-key) |
| Fibonacci heap (Fredman–Tarjan 1987) | \(O(m+n\log n)\) (decrease-key \(O(1)\) amortized) |

Binary heaps are often simpler and faster in practice.

**Beyond the notes’ core exam material (context only).** Recent work broke the sorting barrier for directed nonnegative weights (\(O(m\log^{2/3}n)\), 2025) and obtained near-linear randomized algorithms for directed graphs with integral negative weights and no reachable negative cycle. Dijkstra itself still forbids negative edges.

### 8.3 Minimum spanning trees and the cut property

**Goal.** Connected undirected \(G\) with weights \(w:E\to\mathbb{R}_{\ge 0}\). Find \(T\subseteq E\) connecting all vertices and minimizing \(w(T)\).

**Observation.** Some optimum is a tree: if a connected solution has a cycle, delete a maximum-weight cycle edge; connectivity is preserved and cost does not increase. A spanning tree has exactly \(n-1\) edges.

An MST need **not** be a shortest-path tree. Objective is total edge weight, not distances from a root.

**Cut.** For \(\emptyset\neq S\subsetneq V\), cut \((S,V\setminus S)\) is all edges with one end in \(S\) and one outside. A **light edge** is a minimum-weight crossing edge.

**Cut property.** Any light edge \(e\) of any nontrivial cut belongs to **some** MST. If \(e\) is the **unique** light edge, it belongs to **every** MST.

**Exchange proof.** Let \(T^*\) be an MST. If \(e\in T^*\), done. Else \(T^*\cup\{e\}\) has a cycle. That cycle must recross the cut on some \(f\in T^*\). Lightness gives \(w(e)\le w(f)\), so
\[
T'=T^*\cup\{e\}\setminus\{f\}
\]
is a spanning tree with \(w(T')\le w(T^*)\). Thus \(T'\) is an MST containing \(e\). If uniquely light, the inequality is strict, so no MST can omit \(e\).

**Ties.** In an equal-weight triangle, each edge is light for some cut, but no tree contains all three. “Some MST” cannot be replaced by “every MST” when there are ties.

---

## 9. Prim’s algorithm

Grow one tree from a chosen root \(r\). Prim chooses cuts whose light edges are compatible with all earlier choices.

**Algorithm.**

1. \(S=\{r\}\), \(T=\emptyset\).
2. Choose a min-weight edge \((u,v)\) crossing \((S,V\setminus S)\), \(u\in S\), \(v\notin S\).
3. Add \((u,v)\) to \(T\), add \(v\) to \(S\). Repeat until \(S=V\).

**Invariant.** Some MST contains all edges selected so far (not merely that each selected edge belongs to some MST on its own).

**Correctness.** Initially \(T=\emptyset\). Suppose MST \(T^*\) contains current \(T\), and \(e\) is the next min-weight crossing edge. If \(e\notin T^*\), adding \(e\) creates a cycle with another crossing edge \(f\), \(w(f)\ge w(e)\). No edge of \(T\) crosses this cut, so \(f\notin T\). Replace \(f\) by \(e\) to get an MST containing \(T\cup\{e\}\). At the end \(T\) has \(n-1\) edges, so it is that MST.

### Priority-queue implementation

For every unvisited \(v\),
\[
\mathrm{key}[v]=\min\{w(u,v):u\in S,\,(u,v)\in E\}
\]
(\(+\infty\) if none). Store a parent attaining a finite minimum. When \(u\) is added, scan incident edges and decrease keys of unvisited neighbors.

**Time.** Adjacency lists + binary heap: \(O((n+m)\log n)=O(m\log n)\) on a connected graph. Fibonacci heaps: \(O(m+n\log n)\).

### Dijkstra vs Prim (memorize)

| | Dijkstra | Prim |
|---|---|---|
| Key at \(v\) | length of a path from \(s\) | cost of **one edge** from \(S\) |
| Candidate on \((u,v)\) | \(d[u]+w(u,v)\) | \(w(u,v)\) |
| Negative weights | proof fails | exchange proof still works |
| Output | shortest-path tree | MST (need not be an SPT) |

---

## 10. Matchings

**Matching.** \(M\subseteq E\) such that no vertex is incident to more than one edge of \(M\).  
**Goal.** Maximum cardinality.

**Maximal vs maximum.** Maximal: no edge can be added. Maximum: no larger matching exists. A greedy matching can be maximal but not maximum.

### Augmenting paths

Given matching \(M\), an **augmenting path** is a simple path that:

- alternates between \(E\setminus M\) and \(M\);
- has both endpoints unmatched by \(M\).

It starts and ends with unmatched edges, so it has one more unmatched edge than matched edge.

**Observation.** If \(P\) is augmenting,
\[
M\,\triangle\, E(P) = \bigl(M\setminus E(P)\bigr)\cup\bigl(E(P)\setminus M\bigr)
\]
is a matching of size \(|M|+1\). Internal vertices swap matched/unmatched edges; endpoints gain their first matched edge.

### Berge’s theorem

**A matching \(M\) is maximum iff there is no \(M\)-augmenting path.**

- If an augmenting path exists, \(M\) is not maximum (previous observation).
- Converse: if a larger matching \(M^*\) exists, consider \(M\,\triangle\, M^*\). Degrees are at most 2, so components are paths or cycles, alternating between \(M\) and \(M^*\). Cycles and even paths contribute equally many edges from each matching. Since \(|M^*|>|M|\), some component has one extra \(M^*\) edge: a path starting and ending with \(M^*\) edges whose endpoints are unmatched by \(M\). That is an \(M\)-augmenting path. Contradiction.

**Algorithmic plan.** Start from \(M=\emptyset\). Repeatedly find an augmenting path and augment. If none exists, Berge certifies optimality.

**General graphs.** Berge still applies, but odd cycles (“blossoms”) make search subtle. Edmonds’ blossom algorithm is polynomial; this unit focuses on the bipartite case.

### Bipartite matching

Graph is bipartite if \(V=A\cup B\), \(A\cap B=\emptyset\), every edge has one end in \(A\) and one in \(B\).

**Search via orientation.**

- Orient unmatched edges \(A\to B\), matched edges \(B\to A\).
- Add a super-source connected to unmatched vertices of \(A\).
- A directed path to an unmatched vertex of \(B\) is an augmenting path.

BFS/DFS finds one in \(O(n+m)\). Each augmentation increases size by 1; matching size \(\le n/2\), so
\[
O\bigl(n(n+m)\bigr)
\]
time. Faster algorithms augment along several paths at once.

After flipping, reverse orientations of the path’s edges and update unmatched vertices.

**Why bipartite is easier.** The orientation argument is clean because there are no odd cycles to confuse “left/right” alternation.

---

## 11. Maximum flow and minimum cut

Matching augmentation generalizes: residual reverse edges let us revise earlier routing.

### Flow networks

Directed graph \(G=(V,E)\) with nonnegative capacities \(c_e\), source \(s\), sink \(t\neq s\). Capacities bound flow; they are **not** path lengths. Notes assume **integral capacities** for termination analysis; the definition of flow still allows reals.

**Feasible flow.** Nonnegative \(f_e\) satisfying:

1. **Capacity:** \(0\le f_e\le c_e\) for all \(e\).
2. **Conservation:** for every \(v\notin\{s,t\}\),
   \[
   \sum_{(u,v)\in E} f_{uv} = \sum_{(v,w)\in E} f_{vw}.
   \]

**Value.**
\[
|f|=\sum_{(s,v)\in E} f_{sv}-\sum_{(v,s)\in E} f_{vs}.
\]

Maximum-flow problem: feasible flow of maximum value.

### Bipartite matching as max flow

Direct original edges \(A\to B\) with capacity 1. Add \((s,a)\) of capacity 1 for each \(a\in A\) and \((b,t)\) of capacity 1 for each \(b\in B\).

An **integral** max flow corresponds to a maximum matching: each flow-1 middle edge is a matched edge; capacities prevent using a vertex twice. Fractional flow need not encode a matching; integer capacities plus integrality of the algorithm complete the reduction.

### Residual graphs

Given feasible \(f\), residual graph \(G_f\) has vertex set \(V\). For original edge \(e=(u,v)\):

- **forward** residual edge \((u,v)\) with capacity \(c_e-f_e\);
- **reverse** residual edge \((v,u)\) with capacity \(f_e\).

Store only positive residual capacities. Reverse edges do **not** create original edges; they allow cancellation.

An \(s\)–\(t\) path in \(G_f\) is an **augmenting path**. Bottleneck
\[
\Delta=\min\{c_f(e): e\text{ on the path}\}.
\]
Augmenting by \(\Delta\) increases flow on forward original edges and decreases flow on backward original edges. Value increases by \(\Delta\).

**Feasibility preserved.** Bottleneck keeps \(0\le f\le c\). At internal vertices, \(+\Delta\) out and \(-\Delta\) in cancel. Only \(s\) and \(t\) have net change.

**Matching connection.** In the unit-capacity matching network, a used middle edge has only a reverse residual edge; an unused one has only a forward edge. These are the Lecture 7 orientations. Flow augmentation generalizes flipping matched/unmatched edges.

**Running example.** All capacities 1. First send one unit on \(s,a,b,t\). Searching only unused **forward** capacity can get stuck. Reverse residual \(b\to a\) cancels the old unit on \(a\to b\). Augment along \(s,b,a,t\) to get value 2 using routes \(s,a,t\) and \(s,b,t\).

### Ford–Fulkerson

1. Start from the zero flow.
2. Build \(G_f\).
3. Find any \(s\)–\(t\) path \(P\) in \(G_f\); if none, stop.
4. Augment by the bottleneck of \(P\); repeat.

**Integrality.** Integer capacities \(\Rightarrow\) all flows and residuals stay integral. Each augmentation increases \(|f|\) by at least 1.

**Time.** Graph search \(O(m+n)\). Bound
\[
O\bigl((m+n)(1+|f^*|)\bigr),
\]
where \(|f^*|\) is the max-flow value. This is **pseudo-polynomial**: \(|f^*|\) can be exponential in the bit length of capacities (same distinction as value-indexed knapsack). Unlike the FPTAS, the goal here is an **exact** optimum.

**Edmonds–Karp.** Always augment along a **shortest** residual path (fewest edges), found by BFS. Time is polynomial in \(n\) and \(m\), independent of capacity magnitudes. With arbitrary real capacities, unrestricted Ford–Fulkerson need not terminate; the BFS variant avoids this.

**Augmenting-path optimality.** If \(G_f\) has no \(s\)–\(t\) path, then \(f\) is a maximum flow.

### Minimum \(s\)–\(t\) cut

An \(s\)–\(t\) cut is a partition \((X,V\setminus X)\) with \(s\in X\), \(t\notin X\). Capacity counts **only outgoing original edges**:
\[
c(X,V\setminus X)=\sum_{\substack{(u,v)\in E\\ u\in X,\, v\notin X}} c_{uv}.
\]

**Weak duality.** For every feasible flow \(f\) and every \(s\)–\(t\) cut,
\[
|f|\le c(X,V\setminus X).
\]
Reason: summing conservation over \(X\setminus\{s\}\) cancels internal flow, so \(|f|\) equals flow leaving \(X\) minus flow entering \(X\), which is at most outgoing capacity.

**MST cut vs flow cut.** MST: lightest undirected crossing edge justifies one greedy choice. Flow: **sum** of outgoing capacities bounds the whole objective. Shared partition idea, different role.

### Max-flow min-cut theorem

**The maximum \(s\)–\(t\) flow value equals the minimum \(s\)–\(t\) cut capacity.**

**Proof (integer capacities).** Ford–Fulkerson terminates. Let \(f\) be the final flow and \(X\) the vertices reachable from \(s\) in \(G_f\). Then \(s\in X\), \(t\notin X\).

- Original edge \((u,v)\) leaving \(X\): forward residual capacity is 0 (else \(v\) reachable), so \(f_{uv}=c_{uv}\).
- Original edge \((v,u)\) entering \(X\): if \(f_{vu}>0\), reverse residual \((u,v)\) would make \(v\) reachable, so \(f_{vu}=0\).

Thus
\[
|f|=\sum_{\text{out of }X}f_{uv}-\sum_{\text{into }X}f_{vu}=c(X,V\setminus X).
\]
Weak duality says every flow is \(\le\) this cut. Equality \(\Rightarrow\) \(f\) is maximum and the cut is minimum.

**Certificate.** Hand someone the flow \(f\) and the reachable set \(X\). They check feasibility, compute \(|f|\) and \(c(X,V\setminus X)\), and verify equality.

**Integrality for matching.** Starting from zero with integer capacities, every augmentation is integral, so the algorithm produces an integral max flow. In the unit-capacity matching network, flow-1 middle edges are a maximum matching.

---

## 12. Running-time cheat sheet

| Algorithm / problem | Recurrence or method | Time |
|---|---|---|
| Merge sort | \(T(n)=2T(n/2)+O(n)\) | \(\Theta(n\log n)\) |
| Max difference (value only) | \(2T(n/2)+O(n)\) | \(\Theta(n\log n)\) |
| Max difference (rich summary) | \(2T(n/2)+O(1)\) | \(\Theta(n)\) |
| Median of medians | \(T(n/5)+T(7n/10)+O(n)\) | \(O(n)\) |
| Largest contiguous sum | \(n\) states, \(O(1)\) each | \(O(n)\) |
| LCS | table \((n+1)(m+1)\) | \(O(nm)\) |
| Tree MIS | postorder DP | \(O(n)\) |
| Knapsack (value-indexed) | \(O(n V_{\mathrm{sum}})\) | pseudo-polynomial |
| Knapsack FPTAS | scaled value DP | \(O(n^3/\varepsilon)\) |
| Finite-horizon MDP | Bellman backup | \(O(T\|A\|\|S\|^2)\) |
| BFS / scan graph | queue + adj. lists | \(O(n+m)\) |
| Dijkstra (binary heap) | \(n\) extract-min, \(\le m\) decrease-key | \(O((n+m)\log n)\) |
| Dijkstra / Prim (Fib heap) | | \(O(m+n\log n)\) |
| Prim (binary heap, connected) | same ops as Dijkstra | \(O(m\log n)\) |
| Bipartite matching (one path at a time) | \(\le n/2\) BFS/DFS | \(O(n(n+m))\) |
| Ford–Fulkerson | augment by \(\ge 1\) | \(O((m+n)(1+\|f^*\|))\) (pseudo-poly) |
| Edmonds–Karp | shortest residual paths | poly(\(n,m\)) |

---

## 13. Proof templates to memorize

### Strong induction for recurrences

1. State the exact claimed bound (include the constant \(K\) or \(A\)).
2. Choose the constant large enough for **all finite base cases** and to absorb linear terms.
3. Invoke the IH on **every strictly smaller argument** (floors/ceilings allowed).
4. Algebraically absorb the nonrecursive work. For linear bounds you need the coefficients of recursive sizes to sum to a number **strictly less than 1**.

### Exchange / cut arguments (MST, Prim)

1. Start from an optimal object \(T^*\).
2. If the chosen edge \(e\) is missing, add it and delete a conflicting edge \(f\) on the created cycle.
3. Show cost does not increase, so the new object is still optimal and contains \(e\).
4. For Prim, strengthen to: some single MST contains **the whole prefix** of chosen edges.

### Augmenting-path optimality (matching, flow)

1. An augmenting structure proves the current solution is **not** optimal (progress).
2. If none exists, exhibit a **certificate** (Berge: no path; flow: reachable-set cut) whose bound matches the current value.
3. Weak duality / counting shows nothing can be better, so the current solution is optimal.

### DP correctness

1. Define the state so it contains exactly the information needed to extend.
2. Argue every feasible solution of the state falls into one of the recurrence cases.
3. Prove the evaluation order only uses already-computed smaller states.
4. If recovering a solution, record argmax/argmin decisions.

---

## 14. Part I synthesis (from Lecture 8)

Three algorithmic lenses:

1. **Divide and conquer** — split, recurse, combine.
2. **Dynamic programming** — overlapping states, reuse values.
3. **Graph algorithms** — reachability, cuts, paths, local exchange.

Every algorithm pairs a construction with a proof invariant and a running-time analysis.

Two ways graphs justify progress:

| Style | Examples | Earlier choices | Optimality certificate |
|---|---|---|---|
| Irrevocable greedy + exchange | Prim | never undone | cut property / invariant that selected edges sit in some MST |
| Augmenting paths | matching, flow | revised along a path | failed search (no augmenting path / no residual \(s\)–\(t\) path); matching uses Berge, flow uses a min cut |

**Looking ahead (not exam core, but in notes).** Flow constraints are linear; “every flow \(\le\) every cut” is weak duality, previewing LP duality.

### Invariant / progress / certificate drill

| Algorithm | Invariant | Progress | Certificate / optimality |
|---|---|---|---|
| Prim | some MST contains \(T\) so far | add a light edge out of \(S\) | \(T\) has \(n-1\) edges \(\Rightarrow\) it is that MST |
| Bipartite matching | \(M\) is a matching | flip an augmenting path, \(\lvert M\rvert+1\) | no augmenting path \(\Leftrightarrow\) maximum (Berge) |
| Max flow | \(f\) feasible | augment by \(\Delta\ge 1\) (integers) | no residual \(s\)–\(t\) path; reachable set is a min cut of capacity \(\lvert f\rvert\) |

---

## 15. Worked lecture examples (do these closed-book)

### Max difference

\(A=[2,5,1,7,3,2,4,6]\). Best drop \(7-2=5\). Crossing from left half \([2,5,1,7]\) to right \([3,2,4,6]\) uses \(\max_{\text{left}}-\min_{\text{right}}=7-2=5\).

### Largest contiguous sum

Fill \(M[i]\) as in Section 5.1; optimum value \(55\), endpoints of \([10,-5,40,10]\).

### LCS

\(A=\texttt{ABCDEFG}\), \(B=\texttt{BCDGKAB}\). One LCS \(\texttt{BCDG}\) length 4. Practice filling \(D[i,j]\) and tracing back. Ties mean multiple LCSs.

### Knapsack

Items \((s,v)\in\{(6,30),(3,14),(4,16),(2,9)\}\), \(B=10\). OPT \(=46\) from items 1 and 3. Also try the FPTAS with \(\varepsilon=1/2\), \(K=3.75\).

### MDP horizons

For a 3-step high-reward route vs a 1-step reward-1 route, compute optimal first action for \(T=1,2,3\). For the \(1/2\cdot 2 + 1/2\cdot 0\) vs deterministic \(1.5\) example, compute \(T=1\) and \(T=2\).

### Flow

All capacities 1 on the 4-vertex network. After routing \(s,a,b,t\), residual reverse \(b\to a\) enables a second unit. Final min cut \(X=\{s\}\) has capacity \(2\).

---

## 16. High-yield practice questions

### Asymptotics and recurrences

1. Prove \(\log(n!)=\Theta(n\log n)\) from first principles.
2. Prove \(T(n)=T(\lfloor n/2\rfloor)+T(\lceil n/2\rceil)+cn=\Theta(n\log n)\) by strong induction (both \(O\) and \(\Omega\)).
3. Prove \(T(n)\le T(\lceil n/5\rceil)+T(\lceil 7n/10\rceil)+cn=O(n)\). Where does the proof fail if groups of 3 are used instead of 5?
4. Apply the Master Theorem to \(T(n)=3T(n/2)+\Theta(n)\), \(T(n)=4T(n/2)+\Theta(n^2)\), and \(T(n)=2T(n/2)+\Theta(1)\).

### Divide-and-conquer / DP design

5. Why does returning only the best difference yield \(\Theta(n\log n)\), while returning \((D,M,m)\) yields \(\Theta(n)\)?
6. Write Kadane’s recurrence, prove the invariant, and recover endpoints.
7. Write the LCS recurrence and justify both cases. Recover one LCS from the table.
8. Give both one-state and two-state tree-MIS recurrences. Prove they compute the same optimum. Recover the set.
9. Write the value-indexed knapsack DP. Explain why it is pseudo-polynomial. Compare with a capacity-indexed DP.

### Approximation and MDPs

10. State PTAS vs FPTAS. Derive \(K=\varepsilon V_{\max}/n\) and the \(O(n^3/\varepsilon)\) bound.
11. Reproduce the knapsack FPTAS inequality chain from memory.
12. Write the Bellman equation. Prove that an optimal policy may be chosen deterministic and Markovian (depends on \((s,t)\) only). Give the \(O(T|A||S|^2)\) argument.

### Graphs

13. Prove BFS distances are shortest unweighted distances.
14. Prove Dijkstra’s extraction invariant. Exhibit a negative-edge counterexample and mark the failed line.
15. Prove the MST cut property. Run Prim, recording \(S\), keys, and chosen edges. Contrast keys with Dijkstra.
16. Prove Berge’s theorem. Convert a bipartite matching instance into an oriented search graph and into a unit-capacity flow network.
17. Define residual graphs. Prove that a bottleneck augmentation preserves feasibility and increases value by \(\Delta\).
18. Prove max-flow min-cut for integer capacities, including why the reachable set saturates outgoing edges and has zero incoming flow.
19. Explain why Ford–Fulkerson is pseudo-polynomial and how Edmonds–Karp differs.
20. For Prim, bipartite matching, and max flow: invariant, progress operation, certificate. Which algorithms can undo an earlier choice?

---

## 17. Common pitfalls

- Treating Big-O as a tight bound; writing \(O\) when the claim needs \(\Theta\) or \(\Omega\).
- Applying the Master Theorem to unequal-size recurrences (selection).
- Forgetting floors/ceilings in induction, or using ordinary induction when subproblems are not \(n-1\).
- Using a bad pivot and claiming linear-time selection.
- Defining a DP state that cannot be extended (too little memory) or that explodes (too much memory).
- Confusing subsequence with substring; forgetting LCS base cases on empty prefixes.
- Confusing tree MIS “include \(v\) \(\Rightarrow\) skip children” with “skip grandchildren.”
- Calling knapsack polynomial; it is pseudo-polynomial unless values are scaled (FPTAS).
- Optimizing best-case MDP outcomes instead of expectations; ignoring remaining horizon.
- Running Dijkstra with negative edges; claiming an MST is a shortest-path tree.
- Saying a light edge is in **every** MST when ties exist.
- Confusing maximal matching with maximum matching.
- Counting **both** directions in an \(s\)–\(t\) cut capacity; only original edges **out of** \(X\) count.
- Searching only unused forward capacity and missing reverse residual edges.
- Claiming Ford–Fulkerson is polynomial in the bit length of capacities.

---

## 18. 60-minute last-pass checklist

- [ ] \(O,\Omega,\Theta,o,\omega\) definitions and \(\log(n!)=\Theta(n\log n)\)
- [ ] Merge-sort tree and strong-induction proof
- [ ] Master Theorem three cases
- [ ] Median-of-medians: groups of 5, \(3n/10\) count, \(T(n/5)+T(7n/10)+O(n)=O(n)\)
- [ ] Max-difference rich summary \(\Theta(n)\)
- [ ] Kadane, LCS, tree MIS (two states), knapsack value DP
- [ ] FPTAS: \(K\), scaled DP, proof chain, \(O(n^3/\varepsilon)\)
- [ ] Bellman equation, deterministic Markov policy, \(O(T|A||S|^2)\)
- [ ] BFS \(O(n+m)\); Dijkstra invariant and heap times
- [ ] Cut property; Prim invariant; Prim vs Dijkstra keys
- [ ] Berge; bipartite orientation; \(O(n(n+m))\)
- [ ] Residual graph; FF; MFMC proof; matching reduction
- [ ] Pseudo-polynomial vs polynomial vs FPTAS, with examples
