# Dynamic Programming Solution: Split Array Largest Sum

## Problem Statement

Given an array $A$ of $n$ non-negative integers and an integer $k$, partition $A$ into $k$ contiguous, non-empty subarrays such that the maximum sum among all subarrays is minimized. Let this minimum achievable largest sum be $S$.

---

## 1. Dynamic Programming Table Definition

Let $A$ be a 1-indexed array of $n$ elements: $A[1 \dots n]$.

We define a 2D dynamic programming table $T$ with dimensions $(n + 1) \times (k + 1)$:

- **$T(i, j)$** represents the **minimum achievable largest subarray sum** obtained by partitioning the prefix $A[1 \dots i]$ into exactly $j$ contiguous, non-empty subarrays.

The target solution to the overall problem is given by:
$$S = T(n, k)$$

---

## 2. Recurrence Relation and Correctness

### Prefix Sums
To compute range sums in $O(1)$ time, define the prefix sum array $P$:
- $P[0] = 0$
- $P[i] = \sum_{m=1}^{i} A[m] = P[i-1] + A[i]$ for $1 \le i \le n$

The sum of any contiguous subarray spanning from index $p + 1$ to $i$ is:
$$\text{Sum}(A[p+1 \dots i]) = P[i] - P[p]$$

### Base Cases
1. **Single partition ($j = 1$):**
   $$T(i, 1) = P[i] \quad \text{for all } 1 \le i \le n$$
2. **Impossible partitions ($i < j$):**
   $$T(i, j) = \infty \quad \text{whenever } i < j$$
   (An array of length $i$ cannot be partitioned into more than $i$ non-empty subarrays.)

### Recurrence
For $2 \le j \le k$ and $j \le i \le n$:
$$T(i, j) = \min_{j-1 \le p < i} \max\Big(T(p, j-1),\, P[i] - P[p]\Big)$$

### Correctness Explanation
- **Partition Structure:** Any valid partition of $A[1 \dots i]$ into $j$ contiguous subarrays has a last subarray starting at index $p + 1$ and ending at index $i$, where $p$ is the boundary split point ($j - 1 \le p \le i - 1$).
- **Subproblem Independence:** The first $j - 1$ subarrays must partition the prefix $A[1 \dots p]$. For a fixed split point $p$, the largest subarray sum across all $j$ subarrays is:
  $$\max\Big(\text{largest sum in } A[1 \dots p] \text{ with } j-1 \text{ parts},\; P[i] - P[p]\Big)$$
- **Optimal Substructure:** To minimize this maximum for a given $p$, we must minimize the largest sum in the first $j - 1$ subarrays. By definition, this minimum is $T(p, j-1)$.
- **Global Optimality:** Testing all feasible partition points $p \in \{j-1, j, \dots, i-1\}$ and taking the minimum ensures that no valid partition is missed, guaranteeing the global optimum.

---

## 3. Complexity Analysis: $O(k n^2)$ Time

### Preprocessing
- Computing the prefix sums $P[0 \dots n]$ takes $O(n)$ time and $O(n)$ space.

### DP State Transitions
- **Total states:** There are $(k) \times (n)$ reachable states in the table.
- **Cost per state:** To compute $T(i, j)$, the split index $p$ iterates from $j - 1$ to $i - 1$, examining at most $i - j + 1 \le n$ candidates.
- Each evaluation requires an $O(1)$ lookup: $\max(T(p, j-1), P[i] - P[p])$.
- **Total Time Complexity:**
  $$O(n) + \sum_{j=2}^{k} \sum_{i=j}^{n} O(i) = O(k n^2)$$

### Space Complexity
- **Table storage:** $O(k n)$ to store all entries of $T$.
- **Space optimization:** Since row $j$ only depends on row $j - 1$, storage can be reduced to $O(n)$ auxiliary space by maintaining only the previous column/row.

---

## 4. Improving to $O(k n \log n)$ Time via Binary Search

### Monotonicity of the Objective Function
For a fixed state $(i, j)$, consider the two terms inside the $\max$ operation as a function of the split point $p \in [j-1, i-1]$:
1. **$f(p) = T(p, j-1)$:** Monotonically non-decreasing with respect to $p$. Partitioning a longer prefix into the same number of pieces $(j - 1)$ cannot decrease the maximum subarray sum.
2. **$g(p) = P[i] - P[p]$:** Monotonically non-increasing with respect to $p$. Because all elements in $A$ are non-negative, increasing $p$ removes elements from the range $[p+1 \dots i]$.

The objective function:
$$h(p) = \max\big(f(p), g(p)\big)$$
is the pointwise maximum of a non-decreasing function and a non-increasing function. Hence, $h(p)$ is unimodal (V-shaped), and its minimum occurs at the intersection point where $f(p) \approx g(p)$.

### Binary Search Procedure
Instead of scanning all $p$ from $j - 1$ to $i - 1$ linearly in $O(n)$, we binary search for the optimal split point $p^*$ in $O(\log n)$ time:

1. Initialize search boundaries:
   $$\text{low} = j - 1, \quad \text{high} = i - 1, \quad \text{best} = \infty$$
2. While $\text{low} \le \text{high}$:
   - Compute $\text{mid} = \lfloor (\text{low} + \text{high}) / 2 \rfloor$.
   - Evaluate $v_1 = T(\text{mid}, j-1)$ and $v_2 = P[i] - P[\text{mid}]$.
   - Update $\text{best} = \min(\text{best}, \max(v_1, v_2))$.
   - If $v_1 \le v_2$:
     - The left component is smaller or equal; moving right may balance or decrease the maximum. Set $\text{low} = \text{mid} + 1$.
   - Else ($v_1 > v_2$):
     - The left component is larger; moving left will decrease $v_1$. Set $\text{high} = \text{mid} - 1$.
3. Assign $T(i, j) = \text{best}$.

### Improved Time Complexity
- Evaluating each of the $k \times n$ entries takes $O(\log n)$ time.
- **Total Time Complexity:**
  $$O(k n \log n)$$

---

## 5. Concrete Walkthrough Example

### Input
- Array: $A = [7, 2, 5, 10, 8]$
- Size: $n = 5$
- Subarrays: $k = 2$

### Prefix Sums
- $P[0] = 0$
- $P[1] = 7$
- $P[2] = 7 + 2 = 9$
- $P[3] = 9 + 5 = 14$
- $P[4] = 14 + 10 = 24$
- $P[5] = 24 + 8 = 32$

### Base Case ($j = 1$)
For 1 subarray, the partition covers the entire prefix:
- $T(1, 1) = P[1] = 7$
- $T(2, 1) = P[2] = 9$
- $T(3, 1) = P[3] = 14$
- $T(4, 1) = P[4] = 24$
- $T(5, 1) = P[5] = 32$

### Computing $T(5, 2)$ ($i = 5, j = 2$)
Candidate split points $p \in \{1, 2, 3, 4\}$:

| $p$ | Left Prefix $A[1 \dots p]$ | Right Subarray $A[p+1 \dots 5]$ | $T(p, 1)$ | $P[5] - P[p]$ | $\max(T(p, 1), P[5] - P[p])$ |
|:---:|:--------------------------:|:--------------------------------:|:---------:|:-------------:|:----------------------------:|
| $1$ | $[7]$                      | $[2, 5, 10, 8]$                  | $7$       | $32 - 7 = 25$ | $\max(7, 25) = 25$           |
| $2$ | $[7, 2]$                   | $[5, 10, 8]$                     | $9$       | $32 - 9 = 23$ | $\max(9, 23) = 23$           |
| $3$ | $[7, 2, 5]$                | $[10, 8]$                        | $14$      | $32 - 14 = 18$| $\max(14, 18) = \mathbf{18}$ |
| $4$ | $[7, 2, 5, 10]$            | $[8]$                            | $24$      | $32 - 24 = 8$ | $\max(24, 8) = 24$           |

The minimum value among all candidates is achieved at $p = 3$:
$$T(5, 2) = \min(25, 23, 18, 24) = 18$$

### Conclusion
The optimal partition divides the array into $[7, 2, 5]$ (sum = $14$) and $[10, 8]$ (sum = $18$), giving the minimum largest subarray sum:
$$S = 18$$
