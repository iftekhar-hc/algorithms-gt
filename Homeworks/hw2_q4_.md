# Partition Array into \(K\) Parts: Minimizing the Maximum Subarray Sum

## Understanding the Problem

Before considering an algorithm, let us build some intuition.

**Example:**

\[
A = [1,2,3,4,5], \qquad k=3
\]

Some possible partitions are:

- \([1] \mid [2] \mid [3,4,5]\), with maximum sum \(12\)
- \([1,2,3] \mid [4] \mid [5]\), with maximum sum \(6\)
- \([1,2] \mid [3,4] \mid [5]\), with maximum sum \(7\)
- \([1,2] \mid [3] \mid [4,5]\), with maximum sum \(9\)

Therefore, the minimum possible maximum subarray sum is

\[
\boxed{S=6}.
\]

---

## Key Observations

### Observation 1: Prefix Sums

Define the prefix-sum array \(P\) as

\[
P[i] = \sum_{t=0}^{i-1} A[t],
\]

with

\[
P[0]=0.
\]

Equivalently,

\[
P[i]=A[0]+A[1]+\cdots+A[i-1].
\]

The sum of the subarray \(A[i\ldots j-1]\) is

\[
\sum_{t=i}^{j-1} A[t] = P[j]-P[i].
\]

Because all elements are nonnegative, the prefix sums are monotonically nondecreasing:

\[
P[i] \le P[i+1].
\]

This property is useful for both dynamic programming and binary search.

### Observation 2: Optimal Substructure

Suppose we optimally partition

\[
A[0\ldots n-1]
\]

into \(k\) contiguous, nonempty parts.

If the final part begins at index \(m\), then the first \(k-1\) parts must form an optimal partition of

\[
A[0\ldots m-1]
\]

into \(k-1\) parts. Otherwise, we could improve the first \(k-1\) parts and obtain a better complete partition.

This optimal-substructure property justifies a dynamic programming solution.

---

## Method 1: Brute Force

### Idea

There are \(n-1\) gaps between adjacent array elements. To create \(k\) contiguous, nonempty parts, we must place \(k-1\) dividers among these gaps.

The number of possible partitions is

\[
\binom{n-1}{k-1}.
\]

For each partition, compute the sum of every part and take the maximum.

### Complexity

If each partition is evaluated using prefix sums, its \(k\) part sums can be computed in \(O(k)\) time.

Therefore,

\[
\boxed{
T(n,k)=O\left(k\binom{n-1}{k-1}\right)
}
\]

This is exponential in general.

The additional space required to store the divider positions is

\[
O(k).
\]

---

## Method 2: Dynamic Programming

### DP Definition

Define

\[
dp[i][j]
\]

as the minimum possible largest part sum when partitioning the prefix

\[
A[0\ldots i-1]
\]

into exactly \(j\) contiguous, nonempty parts.

Formally,

\[
\boxed{
dp[i][j]
=
\text{minimum possible maximum part sum when partitioning }
A[0\ldots i-1]
\text{ into }j\text{ parts}
}
\]

The final answer is

\[
\boxed{dp[n][k]}.
\]

A state \(dp[i][j]\) is valid only when

\[
0 \le j \le i \le n,
\]

because each part must contain at least one element.

### Base Cases

Partitioning zero elements into zero parts has cost zero:

\[
dp[0][0]=0.
\]

Partitioning a nonempty prefix into zero parts is impossible:

\[
dp[i][0]=\infty
\qquad \text{for } i>0.
\]

Partitioning zero elements into a positive number of parts is also impossible:

\[
dp[0][j]=\infty
\qquad \text{for } j>0.
\]

If the first \(i\) elements are placed into one part, the cost is their total sum:

\[
dp[i][1]=P[i].
\]

If \(i\) elements are partitioned into \(i\) parts, each element forms its own part:

\[
dp[i][i]
=
\max_{0\le t<i} A[t].
\]

---

## Recurrence

Suppose the final part begins at index \(m\). Then:

- The first \(j-1\) parts cover \(A[0\ldots m-1]\).
- The final part covers \(A[m\ldots i-1]\).

Because the first \(j-1\) parts must be nonempty, the split point must satisfy

\[
m \ge j-1.
\]

Because the final part must be nonempty, it must also satisfy

\[
m \le i-1.
\]

Therefore,

\[
m\in\{j-1,j,\ldots,i-1\}.
\]

The optimal cost of partitioning the first \(m\) elements into \(j-1\) parts is

\[
dp[m][j-1].
\]

The sum of the final part is

\[
P[i]-P[m].
\]

For a fixed split point \(m\), the largest part sum is therefore

\[
\max\left(dp[m][j-1],\,P[i]-P[m]\right).
\]

We minimize this value over all valid split points:

\[
\boxed{
dp[i][j]
=
\min_{m=j-1}^{i-1}
\max\left(
dp[m][j-1],
P[i]-P[m]
\right)
}
\]

### Meaning of Each Term

- \(dp[m][j-1]\): optimal cost of the first \(j-1\) parts
- \(P[i]-P[m]\): sum of the final part
- \(\max(\cdot)\): largest part sum for the current split
- \(\min(\cdot)\): best result over all valid split points

---

## Visualization of the Recurrence

```text
A: [ 0 ........ m-1 | m ........ i-1 ]
    \______________/  \______________/
        j-1 parts          last part

       dp[m][j-1]         P[i] - P[m]
```

For this split point, the partition cost is

\[
\max\left(dp[m][j-1],\,P[i]-P[m]\right).
\]

---

## Pseudocode

```text
Algorithm DP-Partition(A, k):
    n = length(A)

    if k < 1 or k > n:
        return invalid

    P[0] = 0

    for i = 1 to n:
        P[i] = P[i - 1] + A[i - 1]

    dp[0..n][0..k] = infinity
    dp[0][0] = 0

    for j = 1 to k:
        for i = j to n:
            for m = j - 1 to i - 1:
                last_sum = P[i] - P[m]

                dp[i][j] = min(
                    dp[i][j],
                    max(dp[m][j - 1], last_sum)
                )

    return dp[n][k]
```

---

## Worked Example

Let

\[
A=[1,2,3,4,5],
\qquad
k=3.
\]

The prefix sums are

\[
P=[0,1,3,6,10,15].
\]

### DP Table

| \(dp[i][j]\) | \(j=1\) | \(j=2\) | \(j=3\) |
|:---:|:---:|:---:|:---:|
| \(i=1\) | \(1\) | \(\infty\) | \(\infty\) |
| \(i=2\) | \(3\) | \(2\) | \(\infty\) |
| \(i=3\) | \(6\) | \(3\) | \(3\) |
| \(i=4\) | \(10\) | \(6\) | \(4\) |
| \(i=5\) | \(15\) | \(9\) | \(\mathbf{6}\) |

Therefore,

\[
\boxed{dp[5][3]=6}.
\]

### Computing \(dp[4][2]\)

The valid split points are

\[
m\in\{1,2,3\}.
\]

#### Split at \(m=1\)

The partition is

\[
[1] \mid [2,3,4].
\]

Its cost is

\[
\begin{aligned}
\max\left(dp[1][1],P[4]-P[1]\right)
&=
\max(1,10-1) \\
&=
\max(1,9) \\
&=9.
\end{aligned}
\]

#### Split at \(m=2\)

The partition is

\[
[1,2] \mid [3,4].
\]

Its cost is

\[
\begin{aligned}
\max\left(dp[2][1],P[4]-P[2]\right)
&=
\max(3,10-3) \\
&=
\max(3,7) \\
&=7.
\end{aligned}
\]

#### Split at \(m=3\)

The partition is

\[
[1,2,3] \mid [4].
\]

Its cost is

\[
\begin{aligned}
\max\left(dp[3][1],P[4]-P[3]\right)
&=
\max(6,10-6) \\
&=
\max(6,4) \\
&=6.
\end{aligned}
\]

Thus,

\[
dp[4][2]=\min(9,7,6)=6.
\]

The previously stated value \(dp[4][2]=4\) was incorrect because it treated

\[
dp[3][1]
\]

as \(3\). However,

\[
dp[3][1]=1+2+3=6.
\]

### Computing \(dp[5][3]\)

The valid split points are

\[
m\in\{2,3,4\}.
\]

#### Split at \(m=2\)

\[
\begin{aligned}
\max\left(dp[2][2],P[5]-P[2]\right)
&=
\max(2,15-3) \\
&=
\max(2,12) \\
&=12.
\end{aligned}
\]

This corresponds to

\[
[1] \mid [2] \mid [3,4,5].
\]

#### Split at \(m=3\)

\[
\begin{aligned}
\max\left(dp[3][2],P[5]-P[3]\right)
&=
\max(3,15-6) \\
&=
\max(3,9) \\
&=9.
\end{aligned}
\]

This corresponds to

\[
[1,2] \mid [3] \mid [4,5].
\]

#### Split at \(m=4\)

\[
\begin{aligned}
\max\left(dp[4][2],P[5]-P[4]\right)
&=
\max(6,15-10) \\
&=
\max(6,5) \\
&=6.
\end{aligned}
\]

This corresponds to

\[
[1,2,3] \mid [4] \mid [5].
\]

Therefore,

\[
\begin{aligned}
dp[5][3]
&=
\min(12,9,6) \\
&=
\boxed{6}.
\end{aligned}
\]

---

## Dynamic Programming Complexity

The algorithm evaluates:

- \(k\) possible numbers of parts
- Up to \(n\) prefix lengths
- Up to \(n\) split points for each state

Therefore, its time complexity is

\[
\boxed{O(kn^2)}.
\]

The full DP table requires

\[
\boxed{O(nk)}
\]

space.

Because column \(j\) depends only on column \(j-1\), the space can be reduced to

\[
\boxed{O(n)}
\]

by storing only the previous and current columns.

---

## Method 3: Binary Search on the Answer

The \(O(kn^2)\) dynamic programming solution can be improved when all array elements are nonnegative.

### Search Range

The answer \(S\) must be at least the largest element because every element must belong to some part:

\[
S \ge \max(A).
\]

The answer cannot exceed the sum of the entire array because placing everything in one part gives this upper bound:

\[
S \le \sum_{i=0}^{n-1} A[i].
\]

Therefore, the search range is

\[
\boxed{
\max(A)
\le S \le
\sum_{i=0}^{n-1} A[i]
}.
\]

### Greedy Feasibility Check

For a candidate value \(S\), greedily add elements to the current part while its sum remains at most \(S\).

If adding the next element would make the sum exceed \(S\), begin a new part.

```text
Greedy-Check(A, k, S):
    parts = 1
    current_sum = 0

    for each element x in A:
        if x > S:
            return false

        if current_sum + x > S:
            parts = parts + 1
            current_sum = x

            if parts > k:
                return false
        else:
            current_sum = current_sum + x

    return true
```

The greedy algorithm produces the minimum number of parts needed when no part may have sum greater than \(S\).

Thus, \(S\) is feasible if the greedy algorithm uses at most \(k\) parts:

\[
\operatorname{parts}(S)\le k.
\]

If exactly \(k\) parts are required and \(k\le n\), any part containing multiple elements can be split further without increasing the maximum part sum. Therefore, using at most \(k\) parts is sufficient.

### Binary Search Pseudocode

```text
Algorithm Binary-Search-Partition(A, k):
    n = length(A)

    if k < 1 or k > n:
        return invalid

    low = maximum element in A
    high = sum of all elements in A

    while low < high:
        mid = low + floor((high - low) / 2)

        if Greedy-Check(A, k, mid):
            high = mid
        else:
            low = mid + 1

    return low
```

### Complexity

Let

\[
R=
\sum_{i=0}^{n-1} A[i]-\max(A)+1
\]

be the size of the integer search range.

Binary search performs

\[
O(\log R)
\]

feasibility checks, and each check takes

\[
O(n)
\]

time.

Therefore,

\[
\boxed{
T(n)=O(n\log R)
}
\]

or, more loosely,

\[
\boxed{
T(n)=O\left(n\log\left(\sum A\right)\right)
}.
\]

The greedy feasibility check uses constant additional space:

\[
\boxed{O(1)}.
\]

---

## Summary

| Method | Time Complexity | Space Complexity | Key Idea |
|---|---:|---:|---|
| Brute force | \(\displaystyle O\left(k\binom{n-1}{k-1}\right)\) | \(O(k)\) | Try every divider placement |
| Dynamic programming | \(O(kn^2)\) | \(O(nk)\), reducible to \(O(n)\) | Optimize over all split points |
| Binary search on the answer | \(\displaystyle O\left(n\log R\right)\) | \(O(1)\) | Binary search the maximum allowed sum |

where

\[
R=
\sum_{i=0}^{n-1}A[i]-\max(A)+1.
\]

## Main Corrections

- Removed the `<br>` tags because Markdown already handles paragraph and section spacing.
- Replaced inline array intervals with consistent mathematical notation.
- Corrected \(dp[4][2]\) from \(4\) to \(6\).
- Corrected the final answer from the mistaken recalculation of \(5\) back to \(\boxed{6}\).
- Corrected the brute-force expression to \(\displaystyle O\left(k\binom{n-1}{k-1}\right)\).
- Clarified that binary search performs \(O(\log R)\) checks, not \(O(n\sum A)\) checks.
- Corrected the binary-search space complexity to \(O(1)\).
