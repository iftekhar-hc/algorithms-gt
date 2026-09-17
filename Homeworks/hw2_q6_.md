# Dynamic Programming and Approximation Schemes for the 0/1 Knapsack Problem

## 1. Problem Formulation and Preliminaries

In the 0/1 Knapsack problem, we are given:
- A set of $n$ items labeled $i \in \{1, \dots, n\}$.
- Item sizes (weights) $s_i \le B$, where $B$ is the knapsack budget/capacity.
- Item values $v_i \in \mathbb{Z}^+$.

The goal is to find an index set $I \subseteq \{1, \dots, n\}$ maximizing:
$$\sum_{i \in I} v_i \quad \text{subject to} \quad \sum_{i \in I} s_i \le B$$

Let $V' = \sum_{i \in I^*} v_i$ denote the optimal value achieved by an optimal subset $I^*$.

---

## 2. Question 1: Approximation Ratio for Value Truncation

### Claim
Let $K > 0$ be a scaling parameter. If we truncate each value $v_i$ to its nearest smaller multiple of $K$, setting:
$$v'_i = \left\lfloor \frac{v_i}{K} \right\rfloor \cdot K$$
and run the exact dynamic programming algorithm maximizing $\sum_{i \in I} v'_i$ subject to $\sum_{i \in I} s_i \le B$, the returned subset $I$ has original value $V = \sum_{i \in I} v_i$ satisfying:
$$1 - \frac{nK}{\max_i v_i} \le \frac{V}{V'} \le 1$$

### Proof

#### 1. Feasibility and the Upper Bound
The dynamic programming algorithm enforces the exact weight capacity constraint $\sum_{i \in I} s_i \le B$. Hence, the subset $I$ is feasible. Because $V'$ is the global optimum for the original instance:
$$V = \sum_{i \in I} v_i \le V' \implies \frac{V}{V'} \le 1$$

#### 2. Truncation Invariants
By definition of the floor function:
$$\frac{v_i}{K} - 1 < \left\lfloor \frac{v_i}{K} \right\rfloor \le \frac{v_i}{K}$$
Multiplying by $K$:
$$v_i - K < v'_i \le v_i$$
This implies two properties for every item $i$:
1. $v'_i \le v_i$ (truncated value does not exceed original value).
2. $v_i - v'_i \le K$ (truncation error per item is at most $K$).

#### 3. Optimality under Truncated Values
Because the dynamic programming algorithm finds an optimal subset $I$ with respect to the truncated values $v'_i$, and $I^*$ is also a feasible subset:
$$\sum_{i \in I} v'_i \ge \sum_{i \in I^*} v'_i$$

#### 4. Lower Bound Derivation
Using the truncation properties:
$$V = \sum_{i \in I} v_i \ge \sum_{i \in I} v'_i \ge \sum_{i \in I^*} v'_i \ge \sum_{i \in I^*} (v_i - K) = \sum_{i \in I^*} v_i - |I^*| K = V' - |I^*| K$$

Since $|I^*| \le n$:
$$V \ge V' - nK$$

Dividing both sides by $V'$:
$$\frac{V}{V'} \ge 1 - \frac{nK}{V'}$$

Because each single item $i$ satisfies $s_i \le B$, the single item with maximum value $v_{\max} = \max_i v_i$ is feasible on its own. Therefore, the optimal value must be at least as large as this item:
$$V' \ge \max_{i} v_i$$

Substituting $V' \ge \max_i v_i$ yields:
$$\frac{nK}{V'} \le \frac{nK}{\max_i v_i} \implies 1 - \frac{nK}{V'} \ge 1 - \frac{nK}{\max_i v_i}$$

Combining with the upper bound:
$$1 - \frac{nK}{\max_i v_i} \le \frac{V}{V'} \le 1$$
$\blacksquare$

---

## 3. Question 2: Designing an FPTAS

### Target
We require:
$$\frac{V}{V'} \ge 1 - \epsilon$$
with running time polynomial in $n$ and $1/\epsilon$.

### Choice of $K$
From Question 1, it suffices to set:
$$\frac{nK}{\max_i v_i} = \epsilon \implies K = \frac{\epsilon \max_i v_i}{n}$$

### Algorithmic Implementation and Scaling
Define the scaled integral values:
$$\bar{v}_i = \left\lfloor \frac{v_i}{K} \right\rfloor = \left\lfloor \frac{n \cdot v_i}{\epsilon \max_i v_i} \right\rfloor$$
Because $v'_i = K \cdot \bar{v}_i$, maximizing $\sum_{i \in I} v'_i$ is equivalent to maximizing $\sum_{i \in I} \bar{v}_i$.

### Running Time Complexity
1. The maximum scaled value is:
   $$\bar{v}_{\max} = \max_i \bar{v}_i = \left\lfloor \frac{n \max_i v_i}{\epsilon \max_i v_i} \right\rfloor = \left\lfloor \frac{n}{\epsilon} \right\rfloor \le \frac{n}{\epsilon}$$
2. The maximum possible total scaled value is at most:
   $$V_{\text{scaled, max}} \le n \cdot \bar{v}_{\max} \le \frac{n^2}{\epsilon}$$
3. The dynamic programming table $DP(i, v)$ stores the minimum weight subset of items $\{1, \dots, i\}$ that achieves scaled value exactly $v$.
   - Number of states: $n \times V_{\text{scaled, max}} = O\left(\frac{n^3}{\epsilon}\right)$.
   - Transition time per entry: $O(1)$.

Thus, the overall time complexity is $O\left(\frac{n^3}{\epsilon}\right)$, which is $\operatorname{poly}(n, 1/\epsilon)$, completing the Fully Polynomial-Time Approximation Scheme (FPTAS).

---

## 4. Question 3: $P = NP$ Implication

### Theorem
If an algorithm achieves a $(1 - \epsilon)$-approximation in polynomial time (i.e., polynomial in $n$ and the bit-length of the inputs) for:
$$\epsilon < \frac{1}{n \max_i v_i}$$
then $P = NP$.

### Proof

1. **Upper Bound on the Optimal Value:**
   Any feasible solution contains at most $n$ items, and each item has value at most $\max_i v_i$:
   $$V' \le n \max_i v_i$$

2. **Absolute Approximation Error:**
   The algorithm produces a feasible subset with value $V$ satisfying $V \ge (1 - \epsilon) V'$. The error is:
   $$V' - V \le \epsilon V'$$
   Using $\epsilon < \frac{1}{n \max_i v_i}$ and $V' \le n \max_i v_i$:
   $$V' - V < \left(\frac{1}{n \max_i v_i}\right) (n \max_i v_i) = 1$$

3. **Integrality of Item Values:**
   All values $v_i$ are positive integers, which means $V'$ and $V$ are integers.
   Since $V' - V$ is an integer and $0 \le V' - V < 1$, it strictly follows that:
   $$V' - V = 0 \implies V = V'$$

4. **Complexity Conclusion:**
   An approximation algorithm with $\epsilon < \frac{1}{n \max_i v_i}$ returns the exact optimum value $V'$. If this algorithm runs in time polynomial in the binary encoding of the instance ($n$, $\log B$, $\log(\max_i v_i)$), it solves the NP-hard 0/1 Knapsack problem in polynomial time. Therefore:
   $$P = NP$$
   $\blacksquare$

---

## 5. Concrete Numerical Example

Consider a knapsack instance with $B = 10$ and $n = 3$ items:
- Item 1: $s_1 = 4, v_1 = 70$
- Item 2: $s_2 = 5, v_2 = 80$
- Item 3: $s_3 = 6, v_3 = 90$

Here, $\max_i v_i = 90$.

### Exact Solution
Feasible pairs:
- Items $\{1, 2\}$: weight $4 + 5 = 9 \le 10$, value $70 + 80 = 150$.
- Items $\{1, 3\}$: weight $4 + 6 = 10 \le 10$, value $70 + 90 = 160$.
- Items $\{2, 3\}$: weight $5 + 6 = 11 > 10$ (infeasible).

Optimal subset is $I^* = \{1, 3\}$ with $V' = 160$.

### Approximation Scheme with $\epsilon = 0.25$
1. Compute $K$:
   $$K = \frac{\epsilon \max_i v_i}{n} = \frac{0.25 \times 90}{3} = 7.5$$
2. Compute scaled values $\bar{v}_i = \lfloor v_i / K \rfloor$:
   - $\bar{v}_1 = \lfloor 70 / 7.5 \rfloor = \lfloor 9.333 \rfloor = 9$
   - $\bar{v}_2 = \lfloor 80 / 7.5 \rfloor = \lfloor 10.667 \rfloor = 10$
   - $\bar{v}_3 = \lfloor 90 / 7.5 \rfloor = \lfloor 12.0 \rfloor = 12$
3. Evaluate feasible subsets under scaled values:
   - Items $\{1, 2\}$: scaled value $9 + 10 = 19$.
   - Items $\{1, 3\}$: scaled value $9 + 12 = 21$.
4. The DP selects $\{1, 3\}$, giving original value $V = 160$.
5. Approximation ratio:
   $$\frac{V}{V'} = \frac{160}{160} = 1.0 \ge 1 - \epsilon = 0.75$$
