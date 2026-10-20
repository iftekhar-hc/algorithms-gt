# 18. Hitting Set via Deterministic Rounding

This problem illustrates a fundamental approximation-algorithm pattern:

1. Express the combinatorial problem as an integer program.
2. Relax the integrality requirement to obtain a linear program.
3. Solve the LP efficiently.
4. Round the fractional solution.
5. Prove both **feasibility** and an **approximation guarantee**.

The key structural parameter is

$$
b=\max_{1\le j\le m}|B_j|,
$$

the maximum number of elements in any set that must be hit.

---

## 0. Background and intuition

We have:

- A universe of elements

  $$
  [n]=\{1,2,\ldots,n\}.
  $$

- A positive cost or weight $w_i>0$ for selecting element $i$.
- A collection of subsets

  $$
  B_1,B_2,\ldots,B_m\subseteq[n].
  $$

We want to choose a set $H\subseteq[n]$ such that every $B_j$ contains at least one chosen element:

$$
H\cap B_j\neq\varnothing
\qquad \text{for every }j.
$$

Among all such hitting sets, we want one with minimum total weight:

$$
w(H)=\sum_{i\in H}w_i.
$$

### Visual interpretation

Think of columns as selectable elements and rows as sets that must be covered:

```text
                   Elements
              1    2    3    4    5
            +----+----+----+----+----+
B1          | X  |    | X  |    |    |
B2          |    | X  | X  | X  |    |
B3          |    |    |    | X  | X  |
            +----+----+----+----+----+
```

Selecting element $3$, for example, hits both $B_1$ and $B_2$. Selecting element $5$ hits $B_3$.

A hitting set for this instance could be

$$
H=\{3,5\}.
$$

---

# 1. LP formulation

## Step 1: Introduce decision variables

For each element $i\in[n]$, define

$$
x_i=
\begin{cases}
1, & \text{if element }i\text{ is selected},\\
0, & \text{otherwise}.
\end{cases}
$$

Thus, the selected hitting set is

$$
H=\{i:x_i=1\}.
$$

## Step 2: Express the objective

If $x_i=1$, we pay $w_i$. Therefore, the total weight is

$$
\sum_{i=1}^n w_i x_i.
$$

We want to minimize it.

## Step 3: Express the hitting constraints

For a particular set $B_j$, at least one of its elements must be selected. Therefore,

$$
\sum_{i\in B_j}x_i\ge 1.
$$

We need one such constraint for every $j=1,\ldots,m$.

## Integer programming formulation

The exact Minimum Hitting Set problem can therefore be written as

$$
\begin{aligned}
\text{minimize}\quad
    & \sum_{i=1}^n w_i x_i\\[2mm]
\text{subject to}\quad
    & \sum_{i\in B_j}x_i\ge 1,
      && j=1,2,\ldots,m,\\
    & x_i\in\{0,1\},
      && i=1,2,\ldots,n.
\end{aligned}
\tag{IP}
$$

The binary restriction makes this an integer program and, in general, computationally difficult to solve exactly.

## LP relaxation

We relax the binary requirement

$$
x_i\in\{0,1\}
$$

to the interval constraint

$$
0\le x_i\le 1.
$$

The relaxed LP is

$$
\boxed{
\begin{aligned}
\text{minimize}\quad
    & \sum_{i=1}^n w_i x_i\\[2mm]
\text{subject to}\quad
    & \sum_{i\in B_j}x_i\ge 1,
      && j=1,2,\ldots,m,\\
    & 0\le x_i\le 1,
      && i=1,2,\ldots,n.
\end{aligned}}
\tag{LP}
$$

Let $x^*=(x_1^*,\ldots,x_n^*)$ be an optimal solution to this LP.

Its objective value is

$$
\operatorname{LP}^*
=
\sum_{i=1}^n w_i x_i^*.
$$

## Why the LP value is a lower bound

Every feasible integral solution is also a feasible fractional solution. In particular,

$$
\{0,1\}^n\subseteq[0,1]^n.
$$

The LP therefore minimizes over a larger feasible region than the integer program. Consequently,

$$
\operatorname{LP}^*\le \operatorname{OPT},
$$

where $\operatorname{OPT}$ denotes the weight of an optimal integral hitting set.

This inequality will be essential in the approximation proof.

### Feasible-region picture

```text
Integral feasible solutions
          ⊆
Fractional LP feasible solutions

Therefore:

       LP* ≤ OPT
```

---

# 2. Deterministic rounding

Given the optimal fractional solution $x^*$, define

$$
\hat{x}_i=
\begin{cases}
1, & x_i^*\ge \dfrac1b,\\[2mm]
0, & x_i^*<\dfrac1b.
\end{cases}
$$

Then output

$$
H'=\{i:\hat{x}_i=1\}
   =\left\{i:x_i^*\ge\frac1b\right\}.
$$

The rounding rule is deterministic because once $x^*$ is known, every variable is rounded according to a fixed threshold. There are no random choices.

## Why is $1/b$ the correct threshold?

Every set $B_j$ has at most $b$ elements. The LP constraint says

$$
\sum_{i\in B_j}x_i^*\ge 1.
$$

If all the variables in $B_j$ were strictly smaller than $1/b$, then their sum would be strictly smaller than

$$
|B_j|\cdot \frac1b\le b\cdot\frac1b=1,
$$

contradicting the LP constraint.

Thus, every $B_j$ must contain at least one variable whose value is at least $1/b$.

That variable is selected by the rounding procedure.

## Formal proof that $H'$ is a hitting set

Fix an arbitrary set $B_j$.

Because $x^*$ is feasible for the LP,

$$
\sum_{i\in B_j}x_i^*\ge 1.
\tag{1}
$$

Suppose, for contradiction, that $H'$ does not hit $B_j$. Then

$$
H'\cap B_j=\varnothing.
$$

By the definition of $H'$, no element $i\in B_j$ was rounded to $1$. Therefore,

$$
x_i^*<\frac1b
\qquad\text{for every }i\in B_j.
$$

It follows that

$$
\begin{aligned}
\sum_{i\in B_j}x_i^*
&< \sum_{i\in B_j}\frac1b\\
&=\frac{|B_j|}{b}\\
&\le 1,
\end{aligned}
$$

because $|B_j|\le b$.

This contradicts equation (1). Therefore,

$$
H'\cap B_j\neq\varnothing.
$$

Since $B_j$ was arbitrary, the conclusion holds for every $j$:

$$
\boxed{H'\text{ is a hitting set}.}
$$

## Alternative proof using averages

For any $B_j$, feasibility gives

$$
\sum_{i\in B_j}x_i^*\ge 1.
$$

Therefore, the average fractional value among elements of $B_j$ is at least

$$
\frac{1}{|B_j|}.
$$

At least one variable must be at least as large as the average, so there exists some $i\in B_j$ satisfying

$$
x_i^*
\ge \frac{1}{|B_j|}
\ge \frac1b.
$$

The rounding rule selects this $i$, so $B_j$ is hit.

This is essentially an application of the pigeonhole principle:

```text
At most b values have total at least 1
                    ↓
At least one value is at least 1/b
                    ↓
That element is selected
                    ↓
The corresponding set is hit
```

---

# 3. Approximation guarantee

We now compare the weight of $H'$ with the optimal integral solution.

The weight produced by rounding is

$$
w(H')
=
\sum_{i\in H'}w_i
=
\sum_{i=1}^n w_i\hat{x}_i.
$$

The critical pointwise inequality is

$$
\boxed{\hat{x}_i\le b x_i^*}
\qquad\text{for every }i.
\tag{2}
$$

Let us verify it carefully.

## Case analysis for the rounding inequality

### Case 1: $x_i^*<1/b$

Then $\hat{x}_i=0$, and hence

$$
\hat{x}_i=0\le b x_i^*.
$$

### Case 2: $x_i^*\ge1/b$

Then $\hat{x}_i=1$. Since $x_i^*\ge1/b$,

$$
b x_i^*\ge1.
$$

Thus,

$$
\hat{x}_i=1\le b x_i^*.
$$

So inequality (2) holds in both cases.

## Bound the weight after rounding

Because $w_i>0$, multiplying inequality (2) by $w_i$ preserves the inequality:

$$
w_i\hat{x}_i\le b w_i x_i^*.
$$

Summing over all $i$ gives

$$
\begin{aligned}
w(H')
&=\sum_{i=1}^n w_i\hat{x}_i\\
&\le \sum_{i=1}^n b w_i x_i^*\\
&=b\sum_{i=1}^n w_i x_i^*\\
&=b\,\operatorname{LP}^*.
\end{aligned}
$$

We already established that

$$
\operatorname{LP}^*\le\operatorname{OPT}.
$$

Therefore,

$$
w(H')
\le b\,\operatorname{LP}^*
\le b\,\operatorname{OPT}.
$$

Hence,

$$
\boxed{w(H')\le b\operatorname{OPT}.}
$$

This proves that deterministic threshold rounding is a

$$
\boxed{b\text{-approximation algorithm}.}
$$

## Complete approximation chain

The proof can be summarized by the following chain:

$$
\boxed{
\underbrace{w(H')}_{\text{rounded solution}}
\le
b\underbrace{\operatorname{LP}^*}_{\text{fractional optimum}}
\le
b\underbrace{\operatorname{OPT}}_{\text{integral optimum}}
}
$$

The two inequalities have different meanings:

1. **Rounding inequality**

   $$
   w(H')\le b\operatorname{LP}^*.
   $$

   Rounding may increase the fractional cost by at most a factor of $b$.

2. **Relaxation inequality**

   $$
   \operatorname{LP}^*\le\operatorname{OPT}.
   $$

   The LP optimum is a lower bound on every integral solution.

---

# 4. Worked example

Consider

$$
[n]=\{1,2,3,4,5\}
$$

with weights

$$
(w_1,w_2,w_3,w_4,w_5)=(4,2,3,1,5).
$$

Suppose

$$
\begin{aligned}
B_1&=\{1,2,3\},\\
B_2&=\{2,3,4\},\\
B_3&=\{3,4,5\}.
\end{aligned}
$$

Every set has size $3$, so

$$
b=3.
$$

The LP is

$$
\begin{aligned}
\text{minimize}\quad
&4x_1+2x_2+3x_3+x_4+5x_5\\
\text{subject to}\quad
&x_1+x_2+x_3\ge1,\\
&x_2+x_3+x_4\ge1,\\
&x_3+x_4+x_5\ge1,\\
&0\le x_i\le1.
\end{aligned}
$$

Suppose an LP solver returns the feasible fractional solution

$$
x^*=
\left(
0,\frac23,\frac13,\frac13,\frac13
\right).
$$

Check the constraints:

$$
0+\frac23+\frac13=1,
$$

$$
\frac23+\frac13+\frac13=\frac43\ge1,
$$

and

$$
\frac13+\frac13+\frac13=1.
$$

The threshold is

$$
\frac1b=\frac13.
$$

Therefore,

$$
\hat{x}=(0,1,1,1,1),
$$

because equality with $1/3$ is rounded upward.

Thus,

$$
H'=\{2,3,4,5\}.
$$

### Check feasibility

- $B_1$ is hit by $2$ and $3$.
- $B_2$ is hit by $2,3,$ and $4$.
- $B_3$ is hit by $3,4,$ and $5$.

So $H'$ is a hitting set.

### Check the cost bound

The rounded cost is

$$
w(H')=2+3+1+5=11.
$$

The fractional cost is

$$
\begin{aligned}
\operatorname{LP}(x^*)
&=
4(0)
+2\left(\frac23\right)
+3\left(\frac13\right)
+1\left(\frac13\right)
+5\left(\frac13\right)\\
&=\frac43+1+\frac13+\frac53\\
&=\frac{13}{3}.
\end{aligned}
$$

The rounding bound gives

$$
w(H')
\le 3\operatorname{LP}(x^*)
=3\left(\frac{13}{3}\right)
=13.
$$

Indeed,

$$
11\le13.
$$

Notice that the guarantee need not be tight on every instance. It only promises that the rounded result is no more than $b$ times optimal.

---

# 5. Visualization of the rounding argument

For $b=4$, the threshold is $1/4$.

Suppose a constraint contains four variables:

$$
x_2+x_5+x_7+x_9\ge1.
$$

A feasible assignment might look like this:

```text
Element       x*i         Threshold 1/4       Rounded value

   2          0.10             below               0
   5          0.20             below               0
   7          0.28             above               1
   9          0.42             above               1
              -----
Total         1.00
```

At least one variable must cross the threshold:

```text
Four numbers sum to at least 1
              |
              v
At least one number is at least 1/4
              |
              v
At least one element is rounded to 1
              |
              v
The set is hit
```

If all four values were below $1/4$, then

$$
x_2+x_5+x_7+x_9
<
4\cdot\frac14
=1,
$$

which would violate the LP constraint.

---

# 6. Algorithm

## Pseudocode

```text
DETERMINISTIC-HITTING-SET(W, B1, ..., Bm)

Input:
    Positive weights w1, ..., wn
    Sets B1, ..., Bm

1. Compute
       b = max_j |Bj|.

2. Solve the LP:
       minimize     sum_i wi xi
       subject to   sum_{i in Bj} xi >= 1   for every j
                    0 <= xi <= 1            for every i

3. Let x* be an optimal LP solution.

4. Initialize H' = empty set.

5. For i = 1, ..., n:
       if x_i* >= 1/b:
           add i to H'

6. Return H'.
```

## Correctness invariant

After rounding, for every set $B_j$, at least one member of $B_j$ has been selected.

This follows directly from

$$
\sum_{i\in B_j}x_i^*\ge1
\quad\text{and}\quad
|B_j|\le b.
$$

## Running time

Computing $b$ and applying the rounding rule are straightforward polynomial-time operations.

If the sets are stored explicitly, computing $b$ and rounding take time proportional to the input size, approximately

$$
O\left(n+\sum_{j=1}^m|B_j|\right).
$$

The LP has:

- $n$ variables,
- $m$ covering constraints,
- $2n$ bound constraints.

A linear program of this size can be solved in polynomial time using standard LP methods. Therefore, the entire approximation algorithm runs in polynomial time.

---

# 7. Why strict versus non-strict inequality matters

The rounding rule uses

$$
x_i^*\ge\frac1b,
$$

not merely

$$
x_i^*>\frac1b.
$$

This is necessary.

For example, suppose

$$
B_j=\{1,2,3\}
$$

and

$$
x_1^*=x_2^*=x_3^*=\frac13.
$$

Then

$$
x_1^*+x_2^*+x_3^*=1,
$$

so the LP constraint is satisfied.

If we selected only values strictly greater than $1/3$, none of the three elements would be selected, and $B_j$ would not be hit. Using the condition

$$
x_i^*\ge\frac13
$$

correctly selects all three.

---

# 8. Common mistakes

## Mistake 1: Using threshold $1/n$

The guarantee depends on the maximum constraint size $b$, not the total number of elements $n$.

The relevant implication is

$$
|B_j|\le b
\quad\Longrightarrow\quad
\max_{i\in B_j}x_i^*\ge\frac1b.
$$

Using $1/n$ would still produce a hitting set because $b\le n$, but its cost analysis would generally give only an $n$-approximation, which can be much weaker.

## Mistake 2: Claiming that every fractional variable is at least $1/b$

This is false. The actual statement is:

> For every set $B_j$, at least one variable $x_i^*$, with $i\in B_j$, is at least $1/b$.

Some variables can be much smaller than $1/b$, or even zero.

## Mistake 3: Forgetting the LP lower-bound argument

Showing

$$
w(H')\le b\operatorname{LP}^*
$$

does not by itself finish the approximation proof. We must also use

$$
\operatorname{LP}^*\le\operatorname{OPT}.
$$

Only then do we get

$$
w(H')\le b\operatorname{OPT}.
$$

## Mistake 4: Reversing the relaxation inequality

Because the LP has more feasible solutions, its optimum can only be lower:

$$
\operatorname{LP}^*\le\operatorname{OPT}.
$$

It is not generally true that $\operatorname{OPT}\le\operatorname{LP}^*$.

## Mistake 5: Proving only feasibility

There are two separate obligations:

1. **Feasibility:** $H'$ hits every $B_j$.
2. **Quality:** $w(H')\le b\operatorname{OPT}$.

A complete approximation proof must establish both.

---

# 9. A compact exam-style proof

The integer program is

$$
\begin{aligned}
\min\quad &\sum_{i=1}^n w_i x_i\\
\text{s.t.}\quad
&\sum_{i\in B_j}x_i\ge1
&&\forall j\in[m],\\
&x_i\in\{0,1\}
&&\forall i\in[n].
\end{aligned}
$$

Its LP relaxation replaces $x_i\in\{0,1\}$ with $0\le x_i\le1$.

Let $x^*$ be an optimal LP solution and define

$$
\hat{x}_i=\mathbf{1}\left[x_i^*\ge\frac1b\right].
$$

For any $B_j$, suppose no element of $B_j$ were selected. Then $x_i^*<1/b$ for every $i\in B_j$, and therefore

$$
\sum_{i\in B_j}x_i^*
<
\frac{|B_j|}{b}
\le1,
$$

contradicting LP feasibility. Hence $H'=\{i:\hat{x}_i=1\}$ is a hitting set.

Furthermore, for every $i$,

$$
\hat{x}_i\le b x_i^*.
$$

Therefore,

$$
\begin{aligned}
w(H')
&=\sum_i w_i\hat{x}_i\\
&\le b\sum_i w_i x_i^*\\
&=b\operatorname{LP}^*\\
&\le b\operatorname{OPT}.
\end{aligned}
$$

Thus, the algorithm is a polynomial-time $b$-approximation for weighted Minimum Hitting Set.

---

# 10. Broader interpretation

This hitting-set formulation is a **covering integer program**:

$$
\min\{w^{\mathsf T}x:Ax\ge\mathbf1,\ x\in\{0,1\}^n\},
$$

where

$$
A_{ji}=
\begin{cases}
1, & i\in B_j,\\
0, & i\notin B_j.
\end{cases}
$$

Each row of $A$ has at most $b$ entries equal to $1$. The approximation factor arises from this row sparsity.

The general principle is:

$$
\boxed{
\text{If each covering constraint contains at most }b
\text{ variables, thresholding at }1/b
\text{ preserves feasibility.}
}
$$

So the proof is not merely specific to hitting set. It is an instance of deterministic rounding for sparse covering problems.

---

## Final takeaway

The entire argument rests on three facts:

$$
\sum_{i\in B_j}x_i^*\ge1
\quad\text{and}\quad
|B_j|\le b
$$

imply

$$
\exists i\in B_j:\ x_i^*\ge\frac1b.
$$

Therefore, rounding at $1/b$ hits every set. Also,

$$
\hat{x}_i\le b x_i^*
$$

ensures that the cost increases by at most a factor of $b$. Combining this with the LP lower bound gives

$$
\boxed{
w(H')\le b\operatorname{LP}^*
\le b\operatorname{OPT}.
}
$$

Hence deterministic rounding produces a valid hitting set whose weight is at most $b$ times optimal.
