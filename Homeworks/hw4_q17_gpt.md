# Greedy Approximation Algorithm: A 1.5-Approximation

The algorithm is called Longest Processing Time first (LPT). The key is to examine the item that finishes filling a maximum-load bin: before that item is added, the bin's load is at most the optimal maximum load; unless the bin contains only one item, that final item weighs at most half the optimum. Adding these bounds proves the **1.5-approximation** guarantee.

## 1. Background: what are we trying to prove?

Assume the weights are nonnegative. Zero-weight items do not affect any bin's load, so we can ignore them.

Define:

- $W=\sum_{i=1}^n w_i$: the total weight.
- $\mathrm{OPT}$: the smallest achievable maximum bin load.
- $C_G$: the maximum bin load produced by the greedy algorithm.

We want to show that, for every input,

$$
\boxed{C_G\le \frac32\,\mathrm{OPT}.}
$$

This does not mean the algorithm always finds the optimal placement. It means its maximum load is never more than 50% above the best possible maximum load. This problem is also known as load balancing on identical machines, where item weights represent job durations and the maximum load is called the *makespan*.

### Two basic lower bounds on the optimum

Although we do not know the optimal placement, we know:

$$
\mathrm{OPT}\ge \max_i w_i.
$$

Every item must go somewhere, so no solution can have a maximum load smaller than its largest item.

Also,

$$
\mathrm{OPT}\ge \frac{W}{m}.
$$

The maximum bin load cannot be below the average load. These are standard lower bounds used to analyze load-balancing algorithms.

The proof will compare the greedy solution against these bounds, rather than trying to construct the optimal solution.

## 2. Example: greedy is good, but not always optimal

Consider two bins and the already-sorted weights

$$
3,\ 3,\ 2,\ 2,\ 2.
$$

The greedy algorithm puts each item into a currently least-loaded bin. Breaking ties in favor of bin A gives:

| Step | Item added | Selected bin | Load of A | Load of B |
|---|---:|---|---:|---:|
| Start | — | — | 0 | 0 |
| 1 | 3 | A | 3 | 0 |
| 2 | 3 | B | 3 | 3 |
| 3 | 2 | A | 5 | 3 |
| 4 | 2 | B | 5 | 5 |
| 5 | 2 | A | 7 | 5 |

Here is a visualization, with each digit representing one unit of weight:

```text
Greedy placement

Bin A: [333][22][22]    load 7
Bin B: [333][22]        load 5
```

But a better placement is:

```text
Optimal placement

Bin A: [333][333]       load 6
Bin B: [22][22][22]     load 6
```

The total weight is $12$, so the average-load lower bound is $12/2=6$. Since the second placement achieves that bound, $\mathrm{OPT}=6$.

Thus, on this example,

$$
\frac{C_G}{\mathrm{OPT}}=\frac76<\frac32.
$$

This illustrates the difference between finding an optimal solution and guaranteeing an approximation ratio.

## 3. Step-by-step proof

Write the sorted weights as

$$
w_1\ge w_2\ge \cdots\ge w_n.
$$

### Step 1: Focus on one maximum-load bin

After the algorithm finishes, choose a bin whose load is $C_G$.

Let:

- $j$ be the index of the last item placed into that bin;
- $s$ be that bin's load immediately before item $j$ was added.

Then

$$
C_G=s+w_j.
$$

```text
Chosen maximum-load bin

Before item j:   [------- existing load s -------]
Added item:                                      [-- w_j --]

Final load:     [---------------- C_G ---------------------]
```

The useful move is to analyze the moment item $j$ was assigned—not necessarily the end of the whole algorithm. This is the standard “last job on a maximum-load machine” approach.

### Step 2: Bound the existing load s

The algorithm placed item $j$ into a least-loaded bin.

Therefore, at that moment, every bin had load at least $s$:

```text
Chosen bin:     [------ s ------]
Other bin:      [------ s ------][possibly more]
Other bin:      [------ s ------][possibly more]
    ...
```

So the total weight already assigned was at least $ms$. Since this cannot exceed the total input weight $W$,

$$
ms\le W.
$$

Consequently,

$$
s\le \frac{W}{m}\le \mathrm{OPT}.
$$

We have proved:

$$
\boxed{s\le \mathrm{OPT}.}
$$

This part comes from choosing a least-loaded bin; it does not depend on sorting.

### Step 3: Handle the single-item case

If the chosen maximum-load bin contains only one item, then

$$
C_G=w_j\le\mathrm{OPT}.
$$

So in this case greedy is actually optimal, and the desired approximation bound follows immediately.

For the rest of the proof, suppose the chosen bin contains at least two items.

### Step 4: Use the decreasing order to bound the final item's weight

Because the weights are positive, the first $m$ items go into distinct empty bins: an empty bin always has less load than an occupied bin.

Since item $j$ was added to a bin that already contained an item,

$$
j\ge m+1.
$$

Now consider the first $m+1$ items in sorted order. Every one has weight at least $w_{m+1}$.

In any placement of those $m+1$ items into $m$ bins, the pigeonhole principle says that some bin must contain at least two of them. That bin's load is therefore at least

$$
2w_{m+1}.
$$

This applies to the optimal placement too, so

$$
\mathrm{OPT}\ge 2w_{m+1}.
$$

Since $j\ge m+1$ and the weights are sorted,

$$
w_j\le w_{m+1}\le \frac{\mathrm{OPT}}2.
$$

Thus,

$$
\boxed{w_j\le \frac{\mathrm{OPT}}2.}
$$

This pigeonhole argument is where sorting becomes essential.

### Step 5: Combine the bounds

Recall:

$$
C_G=s+w_j.
$$

Using Steps 2 and 4,

$$
C_G
\le \mathrm{OPT}+\frac{\mathrm{OPT}}2
=\frac32\,\mathrm{OPT}.
$$

Therefore,

$$
\boxed{C_G\le 1.5\,\mathrm{OPT}.}
$$

This proves the required guarantee.

## 4. Why the proof works

The argument separates the final maximum load into two pieces:

```text
Greedy maximum load

[---------- existing load ----------][--- final item ---]
             <= OPT                       <= OPT / 2
```

Each algorithmic choice controls a different piece:

| Algorithmic choice | What it guarantees |
|---|---|
| Choose a least-loaded bin | The existing load is no greater than the overall average, hence no greater than $\mathrm{OPT}$. |
| Process items in decreasing order | An item added to an occupied bin is small enough to be at most $\mathrm{OPT}/2$. |

Together, these give the $3/2$ bound. The second statement follows because more than $m$ items larger than $\mathrm{OPT}/2$ could not fit into $m$ bins with maximum load $\mathrm{OPT}$.

A common mistake is to analyze the last item processed overall. That item may not belong to a maximum-load bin. Instead, choose a maximum-load bin first, then identify the last item placed into that particular bin.

## 5. Compact proof suitable for a written solution

Let the items be ordered so that $w_1\ge\cdots\ge w_n$, and let $W=\sum_iw_i$. We have $\mathrm{OPT}\ge W/m$ and $\mathrm{OPT}\ge w_i$ for every $i$.

Choose a maximum-load bin in the greedy solution. Let $j$ be its last assigned item and $s$ its load before that assignment, so $C_G=s+w_j$. Since the selected bin was least loaded, all bins had load at least $s$, implying

$$
s\le W/m\le\mathrm{OPT}.
$$

If the bin contains only one item, then $C_G=w_j\le\mathrm{OPT}$. Otherwise, ignoring zero-weight items, $j\ge m+1$. Among the first $m+1$ items, any placement into $m$ bins must put two together. Hence

$$
\mathrm{OPT}\ge2w_{m+1}\ge2w_j.
$$

Therefore,

$$
C_G=s+w_j\le\mathrm{OPT}+\frac{\mathrm{OPT}}2
=\frac32\,\mathrm{OPT}.
$$

Thus the algorithm is a $1.5$-approximation. $\square$

---

Source: [Princeton University, Chapter 11: Approximation Algorithms](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pearson/11ApproximationAlgorithms.pdf).
