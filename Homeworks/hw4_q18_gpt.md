# Hitting Set via Deterministic Rounding

The key idea is **thresholding**: solve a fractional version of hitting set, then select every element whose LP value is at least $1/b$. Every set must contain such an element, and rounding increases each element's contribution to the objective by at most a factor of $b$.

We prove two properties separately:

1. Feasibility: the rounded solution hits every set.
2. Cost: its weight is at most $b$ times the optimal hitting-set weight.

## 1. Background: what are we choosing?

The available elements are the indices $1,\ldots,n$. Selecting element $i$ costs $w_i>0$.

Each subset $B_j$ imposes a requirement:

> Select at least one element belonging to $B_j$.

An element can satisfy several requirements at once.

For example, consider

$$
B_1=\{1,2\},\qquad B_2=\{2,3\},\qquad B_3=\{1,3\}.
$$

An incidence table makes the requirements visible:

| Requirement | Element 1 | Element 2 | Element 3 |
|---|:---:|:---:|:---:|
| $B_1$ | ✓ | ✓ | |
| $B_2$ | | ✓ | ✓ |
| $B_3$ | ✓ | | ✓ |

We must choose columns so that every row contains at least one chosen column. For example, $H=\{1,2\}$ works; $H=\{1\}$ does not, because it misses $B_2$.

We assume all $B_j$ are nonempty. An empty $B_j$ makes the problem infeasible. If there are no requirements, the empty hitting set is optimal and no rounding is needed.

## 2. Part 1: formulate the optimization problem

### Step 1: introduce a selection variable

For every element $i$, define

$$
x_i=
\begin{cases}
1,&\text{if element }i\text{ is selected},\\
0,&\text{otherwise}.
\end{cases}
$$

### Step 2: express the total weight

The objective is

$$
\min \sum_{i=1}^{n}w_i x_i.
$$

When $x_i=1$, we pay $w_i$; when $x_i=0$, we pay nothing.

### Step 3: require every set to be hit

For each $B_j$, write

$$
\sum_{i\in B_j}x_i\ge 1.
$$

With binary variables, this says that at least one member of $B_j$ must be selected.

Thus the exact integer linear program is

$$
\boxed{
\begin{aligned}
\min\quad &\sum_{i=1}^{n}w_i x_i\\
\text{subject to}\quad
&\sum_{i\in B_j}x_i\ge 1,
&&j=1,\ldots,m,\\
&x_i\in\{0,1\},
&&i=1,\ldots,n.
\end{aligned}}
$$

### Step 4: relax the binary restriction

Replace $x_i\in\{0,1\}$ with $0\le x_i\le 1$:

$$
\boxed{
\begin{aligned}
\min\quad &\sum_{i=1}^{n}w_i x_i\\
\text{subject to}\quad
&\sum_{i\in B_j}x_i\ge 1,
&&j=1,\ldots,m,\\
&0\le x_i\le 1,
&&i=1,\ldots,n.
\end{aligned}}
$$

This is the LP relaxation. Fractional values are allowed, so several elements can jointly supply the required total of $1$. Formulating an integer program, relaxing it, and then rounding is the approximation framework used here.

Let

$$
\mathrm{OPT}_{LP}=\text{optimal LP objective},
\qquad
\mathrm{OPT}=\text{optimal hitting-set weight}.
$$

Every integer solution is also LP-feasible. Because this is a minimization problem,

$$
\boxed{\mathrm{OPT}_{LP}\le \mathrm{OPT}.}
$$

This lower bound is what lets us compare our algorithm with the unknown optimal hitting set.

## 3. Part 2: prove that rounding produces a hitting set

Recall

$$
b=\max_j|B_j|.
$$

Round using

$$
\hat{x}_i=
\begin{cases}
1,&x_i^*\ge 1/b,\\
0,&x_i^*<1/b,
\end{cases}
\qquad
H'=\{i:\hat{x}_i=1\}.
$$

For feasibility, $x^*$ only needs to be LP-feasible; it does not yet need to be optimal.

### Step 1: examine one arbitrary requirement

Fix any $B_j$. LP feasibility gives

$$
\sum_{i\in B_j}x_i^*\ge 1.
$$

There are at most $b$ terms in this sum.

### Step 2: at least one term must reach the threshold

The largest term is at least the average:

$$
\max_{i\in B_j}x_i^*
\ge
\frac{1}{|B_j|}\sum_{i\in B_j}x_i^*
\ge
\frac{1}{|B_j|}
\ge
\frac{1}{b}.
$$

Therefore, some $i\in B_j$ satisfies $x_i^*\ge 1/b$.

### Step 3: that element is selected

The rounding rule sets $\hat{x}_i=1$. Hence

$$
H'\cap B_j\ne\varnothing.
$$

Because $B_j$ was arbitrary, $H'$ hits every set.

### Visualization: why the threshold works

Suppose $b=3$. Every requirement contains at most three variables whose sum must reach $1$.

```text
If every value were below 1/3:

       x₁ < 1/3     x₂ < 1/3     x₃ < 1/3
              \        |        /
               total would be < 1

But LP feasibility requires total ≥ 1.

Therefore at least one value must be ≥ 1/3.
```

The equality in “$\ge 1/b$” matters. If three values are exactly $1/3$, their sum is $1$, and they must not all be rounded down.

## 4. Part 3: prove the approximation guarantee

Now assume $x^*$ is an optimal LP solution.

The crucial coordinate-by-coordinate inequality is

$$
\boxed{\hat{x}_i\le b x_i^*.}
$$

Check both cases:

| Case | Rounded value | Why the inequality holds |
|---|---:|---|
| $x_i^*<1/b$ | $\hat{x}_i=0$ | $0\le b x_i^*$ |
| $x_i^*\ge1/b$ | $\hat{x}_i=1$ | $1\le b x_i^*$ |

Multiply by $w_i>0$ and sum:

$$
\begin{aligned}
w(H')
&=\sum_{i=1}^{n}w_i\hat{x}_i\\
&\le\sum_{i=1}^{n}w_i(bx_i^*)\\
&=b\sum_{i=1}^{n}w_i x_i^*\\
&=b\,\mathrm{OPT}_{LP}\\
&\le b\,\mathrm{OPT}.
\end{aligned}
$$

Thus

$$
\boxed{w(H')\le b\,\mathrm{OPT}.}
$$

Together with feasibility, this proves a $b$-approximation.

### The proof structure to remember

```text
Rounded cost  ≤  b × optimal LP cost  ≤  b × optimal integer cost
                 rounding bound          relaxation bound
```

A subtle distinction: if $x^*$ is merely feasible rather than optimal, feasibility still holds, but we can only conclude

$$
w(H')\le b\sum_i w_i x_i^*.
$$

An arbitrary feasible LP solution does not necessarily give a $b$-approximation relative to $\mathrm{OPT}$.

## 5. Worked weighted example

Consider the following constructed instance:

$$
(w_1,w_2,w_3)=(2,3,4)
$$

and

$$
B_1=\{1,2\},\qquad
B_2=\{2,3\},\qquad
B_3=\{1,3\}.
$$

Here $b=2$, so the threshold is $1/2$.

### Step 1: write the LP

$$
\begin{aligned}
\min\quad &2x_1+3x_2+4x_3\\
\text{subject to}\quad
&x_1+x_2\ge1,\\
&x_2+x_3\ge1,\\
&x_1+x_3\ge1,\\
&0\le x_i\le1.
\end{aligned}
$$

### Step 2: find and certify an optimal fractional solution

Take

$$
x^*=\left(\frac12,\frac12,\frac12\right).
$$

Every constraint has left-hand side $1$, and the cost is

$$
2\left(\frac12\right)
+3\left(\frac12\right)
+4\left(\frac12\right)
=\frac92.
$$

To verify optimality, observe that every feasible solution satisfies

$$
\begin{aligned}
2x_1+3x_2+4x_3
&=\frac12(x_1+x_2)
+\frac32(x_1+x_3)
+\frac52(x_2+x_3)\\
&\ge\frac12+\frac32+\frac52\\
&=\frac92.
\end{aligned}
$$

Our solution achieves this lower bound, so

$$
\mathrm{OPT}_{LP}=\frac92.
$$

### Step 3: round

All three values meet the threshold:

| Element $i$ | Weight $w_i$ | LP value $x_i^*$ | Rounded $\hat{x}_i$ |
|---|---:|---:|---:|
| 1 | 2 | $1/2$ | 1 |
| 2 | 3 | $1/2$ | 1 |
| 3 | 4 | $1/2$ | 1 |

Therefore,

$$
H'=\{1,2,3\},
\qquad
w(H')=9.
$$

The instance can also be visualized as a triangle, with each edge representing a set that must be hit:

```text
                   1: weight 2
                     /     \
                B₁  /       \  B₃
                   /         \
          2: weight 3 ------- 3: weight 4
                        B₂
```

Selecting a vertex hits its incident edges. Rounding selects all three vertices.

### Step 4: compare with the integer optimum

No singleton hits every set. The possible two-element solutions cost:

| Hitting set | Weight |
|---|---:|
| $\{1,2\}$ | 5 |
| $\{1,3\}$ | 6 |
| $\{2,3\}$ | 7 |

Thus $\mathrm{OPT}=5$. The actual approximation ratio is

$$
\frac{9}{5}=1.8\le2=b.
$$

Notice both inequalities in the analysis:

$$
9=2\left(\frac92\right)\le2(5)=10.
$$

## 6. Can the rounding lose the full factor b?

Yes—for an allowed optimal LP solution.

Consider a single requirement

$$
B_1=\{1,\ldots,b\},
$$

with every weight equal to $1$.

The LP is

$$
\min\sum_{i=1}^{b}x_i
\quad\text{subject to}\quad
\sum_{i=1}^{b}x_i\ge1,\quad 0\le x_i\le1.
$$

The solution

$$
x_i^*=\frac1b\quad\text{for every }i
$$

is optimal, with LP cost $1$.

But threshold rounding selects every element:

```text
Fractional:   [1/b] [1/b] [1/b] ... [1/b]    total cost 1
Rounded:      [ 1 ] [ 1 ] [ 1 ] ... [ 1 ]    total cost b
Optimal set:  [ 1 ] [ 0 ] [ 0 ] ... [ 0 ]    total cost 1
```

The ratio is exactly $b$.

This shows that the bound is tight for the stated rule applied to arbitrary optimal LP solutions. It does not say that every LP solver returns this fractional optimum: the same LP also has integral optimal solutions.

## 7. Algorithm and practical proof checklist

```text
DeterministicHittingSetRounding(w, B₁, ..., Bₘ):
    If there are no sets:
        return ∅

    If any Bⱼ is empty:
        report infeasible

    b ← maxⱼ |Bⱼ|

    Solve the LP relaxation optimally, obtaining x*

    H ← ∅
    For i = 1, ..., n:
        If x*[i] ≥ 1/b:
            add i to H

    return H
```

The LP has $n$ variables and $m$ covering constraints, plus variable bounds. With rationally encoded inputs, the LP-based framework is polynomial-time; the rounding scan itself takes $O(n)$ time after solving the LP.

For an exam proof, keep these four steps distinct:

1. Model selection with binary variables, then relax them.
2. Use “maximum ≥ average” to prove every set contains a variable at least $1/b$.
3. Prove the pointwise cost bound $\hat{x}_i\le b x_i^*$.
4. Use LP optimality and $\mathrm{OPT}_{LP}\le\mathrm{OPT}$ to complete the approximation argument.
