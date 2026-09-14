# Asymptotic Analysis and the Master Theorem

Below is an intuitive, exam-focused explanation of **asymptotic analysis** and the **Master Theorem**, with worked examples and common pitfalls.

## 1. Asymptotic Analysis

Asymptotic analysis describes how an algorithm's resource use, usually **running time** or **memory**, grows as the input size $n$ becomes large.

It focuses on the **growth rate**, rather than exact execution time.

For example, suppose an algorithm takes

$$
T(n)=3n^2+10n+50
$$

operations. For large $n$, the $n^2$ term dominates:

$$
T(n)=\Theta(n^2)
$$

We ignore:

- Constant factors, such as $3$
- Lower-order terms, such as $10n$ and $50$
- Hardware and implementation-specific timing

This allows us to compare algorithms independently of the machine running them.

### 1.1 Why Constants and Lower-Order Terms Are Ignored

Consider:

$$
f(n)=100n
$$

and

$$
g(n)=n^2
$$

For small inputs, $100n$ may be larger. For example:

$$
f(10)=1000,\qquad g(10)=100
$$

But eventually $n^2$ grows faster:

$$
f(1000)=100{,}000,\qquad g(1000)=1{,}000{,}000
$$

Asymptotic analysis is interested in this **long-term behavior**.

That does not mean constants are irrelevant in practice. An $O(n)$ algorithm with a huge constant may be slower than an $O(n^2)$ algorithm for small inputs. Asymptotic analysis describes scalability, not necessarily performance for every input size.

## 2. Big-O, Big-Omega, and Big-Theta

### 2.1 Big-O: Asymptotic Upper Bound

We write

$$
f(n)\in O(g(n))
$$

if there are positive constants $c$ and $n_0$ such that

$$
0\le f(n)\le c\,g(n)
$$

for every $n\ge n_0$.

Intuitively, $f(n)$ eventually grows **no faster than** $g(n)$, up to a constant multiplier.

#### Example

Show that

$$
3n^2+10n+50\in O(n^2)
$$

For $n\ge 1$:

$$
10n\le 10n^2
$$

and

$$
50\le 50n^2
$$

Therefore,

$$
\begin{aligned}
3n^2+10n+50
&\le 3n^2+10n^2+50n^2 \\
&=63n^2
\end{aligned}
$$

Choose:

$$
c=63,\qquad n_0=1
$$

Thus,

$$
3n^2+10n+50\in O(n^2)
$$

#### Important Subtlety

Big-O is **not necessarily a tight bound**.

For example:

$$
n\in O(n^2)
$$

is true, even though $O(n)$ is a more informative upper bound.

### 2.2 Big-Omega: Asymptotic Lower Bound

We write

$$
f(n)\in\Omega(g(n))
$$

if there are positive constants $c$ and $n_0$ such that

$$
0\le c\,g(n)\le f(n)
$$

for every $n\ge n_0$.

Intuitively, $f(n)$ eventually grows **at least as fast as** $g(n)$.

#### Example

For

$$
f(n)=3n^2+10n+50
$$

we have

$$
f(n)\ge 3n^2
$$

for all $n\ge 1$. Therefore,

$$
f(n)\in\Omega(n^2)
$$

using $c=3$ and $n_0=1$.

### 2.3 Big-Theta: Tight Asymptotic Bound

We write

$$
f(n)\in\Theta(g(n))
$$

when both conditions hold:

$$
f(n)\in O(g(n))
$$

and

$$
f(n)\in\Omega(g(n))
$$

This means that $f(n)$ and $g(n)$ grow at the same asymptotic rate, up to constant factors.

Since

$$
3n^2+10n+50\in O(n^2)
$$

and

$$
3n^2+10n+50\in\Omega(n^2)
$$

we conclude:

$$
3n^2+10n+50\in\Theta(n^2)
$$

#### Practical Interpretation

- $O(g(n))$: grows no faster than $g(n)$
- $\Omega(g(n))$: grows no slower than $g(n)$
- $\Theta(g(n))$: grows at the same rate as $g(n)$

### 2.4 Little-$o$: Strictly Slower Growth

We write

$$
f(n)\in o(g(n))
$$

when $f(n)$ grows strictly more slowly than $g(n)$.

A common test is:

$$
\lim_{n\to\infty}\frac{f(n)}{g(n)}=0
$$

#### Example

$$
n\in o(n^2)
$$

because

$$
\lim_{n\to\infty}\frac{n}{n^2}
=
\lim_{n\to\infty}\frac{1}{n}
=0
$$

However,

$$
3n^2\notin o(n^2)
$$

because

$$
\lim_{n\to\infty}\frac{3n^2}{n^2}=3
$$

The functions have the same growth rate, rather than one growing strictly slower.

## 3. Common Growth Rates

From slower to faster:

$$
1
<
\log n
<
\sqrt n
<
n
<
n\log n
<
n^2
<
n^3
<
2^n
<
n!
<
n^n
$$

More precisely:

$$
1=o(\log n)
$$

$$
\log n=o(n^c)
\quad\text{for every fixed }c>0
$$

$$
n^k=o(c^n)
\quad\text{for fixed }k>0,\ c>1
$$

### Typical Examples

| Complexity | Typical algorithm |
|---|---|
| $\Theta(1)$ | Accessing an array element |
| $\Theta(\log n)$ | Binary search |
| $\Theta(n)$ | Scanning an array |
| $\Theta(n\log n)$ | Merge sort |
| $\Theta(n^2)$ | Simple nested loops |
| $\Theta(2^n)$ | Enumerating all subsets |
| $\Theta(n!)$ | Enumerating all permutations |

## 4. Analyzing Simple Code

### Example 1: One Loop

```python
for i in range(n):
    process(i)
```

The body runs $n$ times:

$$
T(n)=\Theta(n)
$$

### Example 2: Nested Loops

```python
for i in range(n):
    for j in range(n):
        process(i, j)
```

The inner operation runs

$$
n\cdot n=n^2
$$

times. Therefore:

$$
T(n)=\Theta(n^2)
$$

### Example 3: Dependent Nested Loop

```python
for i in range(n):
    for j in range(i):
        process(i, j)
```

The total number of iterations is:

$$
0+1+2+\cdots +(n-1)
$$

Using the arithmetic-series formula:

$$
\frac{n(n-1)}{2}
=
\frac{n^2-n}{2}
$$

Therefore:

$$
T(n)=\Theta(n^2)
$$

The inner loop does not always run $n$ times, but the total is still quadratic.

### Example 4: Logarithmic Loop

```python
i = 1
while i < n:
    i *= 2
```

After $k$ iterations:

$$
i=2^k
$$

The loop stops when:

$$
2^k\ge n
$$

Taking logarithms:

$$
k\ge\log_2 n
$$

Therefore:

$$
T(n)=\Theta(\log n)
$$

The base of the logarithm is usually omitted in asymptotic notation because logarithms with different constant bases differ only by a constant factor:

$$
\log_a n=\frac{\log_b n}{\log_b a}
$$

## 5. Recurrences in Divide-and-Conquer Algorithms

A divide-and-conquer algorithm normally performs three steps:

1. **Divide** the input into smaller subproblems.
2. **Conquer** each subproblem recursively.
3. **Combine** the recursive results.

Its running time is often represented as:

$$
T(n)=aT\left(\frac{n}{b}\right)+f(n)
$$

where:

- $a$ is the number of recursive subproblems
- $n/b$ is the size of each subproblem
- $f(n)$ is the nonrecursive divide-and-combine work

For example, merge sort has:

$$
T(n)=2T\left(\frac n2\right)+\Theta(n)
$$

because it:

- Creates $2$ recursive calls
- Gives each call approximately $n/2$ elements
- Spends $\Theta(n)$ time merging

## 6. Intuition Behind the Master Theorem

For

$$
T(n)=aT\left(\frac nb\right)+f(n)
$$

the recursive portion produces approximately

$$
n^{\log_b a}
$$

units of work across the recursion tree.

The Master Theorem compares:

$$
f(n)
$$

with

$$
n^{\log_b a}
$$

Think of these as two competing sources of work:

- $n^{\log_b a}$: work created by recursive branching
- $f(n)$: local divide-and-combine work

The larger source generally determines the final complexity. When they are equal, an extra logarithmic factor appears because comparable work occurs at every recursion level.

## 7. Simplified Master Theorem

Consider:

$$
T(n)=aT\left(\frac nb\right)+\Theta(n^d)
$$

where $a\ge 1$, $b>1$, and $d\ge 0$.

Compute:

$$
p=\log_b a
$$

Then compare $d$ with $p$.

### Case 1: Recursive Work Dominates

If

$$
d<\log_b a
$$

then:

$$
T(n)=\Theta\left(n^{\log_b a}\right)
$$

### Case 2: Equal Work at Every Level

If

$$
d=\log_b a
$$

then:

$$
T(n)=\Theta\left(n^d\log n\right)
$$

### Case 3: Divide-and-Combine Work Dominates

If

$$
d>\log_b a
$$

then:

$$
T(n)=\Theta(n^d)
$$

A compact memory aid is:

- **Recursion larger**: keep $n^{\log_b a}$
- **Equal**: multiply by $\log n$
- **Nonrecursive work larger**: keep $f(n)$

## 8. Master Theorem Examples

### Example 1: Merge Sort

$$
T(n)=2T\left(\frac n2\right)+\Theta(n)
$$

Identify:

$$
a=2,\qquad b=2,\qquad d=1
$$

Compute:

$$
\log_b a=\log_2 2=1
$$

Therefore:

$$
d=\log_b a
$$

This is Case 2:

$$
\boxed{T(n)=\Theta(n\log n)}
$$

#### Recursion-Tree Intuition

At each level, the total merge work is $\Theta(n)$:

$$
n,\ n,\ n,\ldots
$$

There are $\log_2 n$ levels, so:

$$
\Theta(n)\cdot\Theta(\log n)
=
\Theta(n\log n)
$$

### Example 2: Binary Search

Binary search makes one recursive call on half of the input and performs constant additional work:

$$
T(n)=T\left(\frac n2\right)+\Theta(1)
$$

Here:

$$
a=1,\qquad b=2,\qquad d=0
$$

and

$$
\log_2 1=0
$$

Thus:

$$
d=\log_b a
$$

Using Case 2:

$$
\boxed{T(n)=\Theta(\log n)}
$$

Although the formula appears as

$$
\Theta(n^0\log n)
$$

we have $n^0=1$, giving $\Theta(\log n)$.

### Example 3: Recursive Work Dominates

Consider:

$$
T(n)=4T\left(\frac n2\right)+\Theta(n)
$$

Identify:

$$
a=4,\qquad b=2,\qquad d=1
$$

Compute:

$$
\log_2 4=2
$$

Since

$$
d=1<2
$$

this is Case 1:

$$
\boxed{T(n)=\Theta(n^2)}
$$

The algorithm creates so many recursive subproblems that their total cost dominates the linear combine work.

### Example 4: Combine Work Dominates

Consider:

$$
T(n)=2T\left(\frac n2\right)+\Theta(n^2)
$$

Identify:

$$
a=2,\qquad b=2,\qquad d=2
$$

Compute:

$$
\log_2 2=1
$$

Since

$$
d=2>1
$$

this is Case 3:

$$
\boxed{T(n)=\Theta(n^2)}
$$

The quadratic combine operation is more expensive than the total recursive branching.

### Example 5: Unusual Values of $a$ and $b$

Consider:

$$
T(n)=9T\left(\frac n3\right)+\Theta(n)
$$

Here:

$$
a=9,\qquad b=3,\qquad d=1
$$

Compute:

$$
\log_3 9=2
$$

Since

$$
1<2
$$

Case 1 applies:

$$
\boxed{T(n)=\Theta(n^2)}
$$

### Example 6: Another Balanced Case

Consider:

$$
T(n)=8T\left(\frac n2\right)+\Theta(n^3)
$$

Here:

$$
a=8,\qquad b=2,\qquad d=3
$$

Compute:

$$
\log_2 8=3
$$

The exponents are equal, so Case 2 applies:

$$
\boxed{T(n)=\Theta(n^3\log n)}
$$

## 9. General Master Theorem

The more general version analyzes:

$$
T(n)=aT\left(\frac nb\right)+f(n)
$$

by comparing $f(n)$ with

$$
n^{\log_b a}
$$

### Case 1: $f(n)$ Is Polynomially Smaller

If, for some constant $\varepsilon>0$,

$$
f(n)=O\left(n^{\log_b a-\varepsilon}\right)
$$

then:

$$
T(n)=\Theta\left(n^{\log_b a}\right)
$$

#### Example

$$
T(n)=8T(n/2)+n^2
$$

Since:

$$
n^{\log_2 8}=n^3
$$

and $n^2$ is polynomially smaller than $n^3$:

$$
T(n)=\Theta(n^3)
$$

### Case 2: $f(n)$ Matches the Recursive Work

If

$$
f(n)=\Theta\left(n^{\log_b a}\log^k n\right)
$$

for $k\ge 0$, then:

$$
T(n)=\Theta\left(n^{\log_b a}\log^{k+1}n\right)
$$

#### Example

$$
T(n)=2T(n/2)+n\log n
$$

Here:

$$
n^{\log_2 2}=n
$$

and:

$$
f(n)=\Theta(n\log n)
$$

Therefore:

$$
\boxed{T(n)=\Theta(n\log^2 n)}
$$

### Case 3: $f(n)$ Is Polynomially Larger

If, for some constant $\varepsilon>0$,

$$
f(n)=\Omega\left(n^{\log_b a+\varepsilon}\right)
$$

and the regularity condition holds:

$$
a f(n/b)\le c f(n)
$$

for some $c<1$ and sufficiently large $n$, then:

$$
T(n)=\Theta(f(n))
$$

#### Example

$$
T(n)=2T(n/2)+n^2
$$

Here:

$$
n^{\log_2 2}=n
$$

and $n^2$ is polynomially larger than $n$.

Check the regularity condition:

$$
\begin{aligned}
2f(n/2)
&=2\left(\frac n2\right)^2 \\
&=\frac{n^2}{2}
\end{aligned}
$$

Thus:

$$
2f(n/2)\le\frac12 f(n)
$$

Using $c=1/2<1$, Case 3 applies:

$$
T(n)=\Theta(n^2)
$$

## 10. When the Master Theorem Does Not Apply

The theorem is powerful, but it does not solve every recurrence.

### Unequal Subproblem Sizes

$$
T(n)=T(n/3)+T(2n/3)+\Theta(n)
$$

The recursive calls do not all have size $n/b$, so the standard Master Theorem does not directly apply.

A recursion tree or another theorem is needed. In this case:

$$
T(n)=\Theta(n\log n)
$$

### Subtracting Instead of Dividing

$$
T(n)=T(n-1)+\Theta(n)
$$

This is not of the required form $T(n/b)$.

Expanding it gives:

$$
T(n)
=
n+(n-1)+(n-2)+\cdots+1
$$

Therefore:

$$
T(n)=\Theta(n^2)
$$

### Nonconstant Number of Recursive Calls

$$
T(n)=nT(n/2)+\Theta(n)
$$

Here $a=n$, but the theorem assumes that $a$ is a constant.

### Irregular Nonrecursive Work

Some functions do not fit neatly into one of the standard polynomial comparison cases. Other methods, such as recursion trees, substitution, or Akra-Bazzi analysis, may be required.

## 11. Fast Exam Procedure

Given:

$$
T(n)=aT(n/b)+f(n)
$$

use the following steps.

### Step 1: Identify $a$, $b$, and $f(n)$

Example:

$$
T(n)=3T(n/2)+n
$$

gives:

$$
a=3,\qquad b=2,\qquad f(n)=n
$$

### Step 2: Compute the Critical Function

$$
n^{\log_b a}
$$

For the example:

$$
n^{\log_2 3}\approx n^{1.585}
$$

### Step 3: Compare $f(n)$ with the Critical Function

$$
n
\quad\text{versus}\quad
n^{1.585}
$$

The recursive work is polynomially larger.

### Step 4: Select the Case

This is Case 1:

$$
\boxed{T(n)=\Theta\left(n^{\log_2 3}\right)}
$$

## 12. Common Mistakes

### Mistake 1: Comparing $a$ Directly with $f(n)$

For:

$$
T(n)=4T(n/2)+n
$$

do not compare $4$ with $n$. Compare:

$$
n^{\log_2 4}=n^2
$$

with:

$$
f(n)=n
$$

### Mistake 2: Forgetting the Logarithm in the Equal Case

For:

$$
T(n)=2T(n/2)+n
$$

the answer is not $\Theta(n)$. Since the two sources of work match, comparable work occurs at every level:

$$
\boxed{\Theta(n\log n)}
$$

### Mistake 3: Treating Big-O as an Exact Bound

Saying merge sort is $O(n^2)$ is technically true, but weak.

The tight bound is:

$$
\Theta(n\log n)
$$

Use $\Theta$ when you know both the upper and lower asymptotic bounds.

### Mistake 4: Applying the Theorem to Unequal Recursive Calls

The recurrence

$$
T(n)=T(n/5)+T(7n/10)+\Theta(n)
$$

does not have $a$ equal-sized recursive calls, so the standard Master Theorem does not apply. This is the type of recurrence produced by deterministic selection using median of medians.

## 13. Practice Problems

Try these before checking the answers.

1. $T(n)=2T(n/2)+1$
2. $T(n)=3T(n/3)+n$
3. $T(n)=4T(n/2)+n^3$
4. $T(n)=16T(n/4)+n^2$
5. $T(n)=2T(n/2)+n\log n$
6. $T(n)=T(n/2)+n$

### Answers

#### 1.

$$
n^{\log_2 2}=n
$$

and $1$ is smaller than $n$, so:

$$
\boxed{\Theta(n)}
$$

#### 2.

$$
n^{\log_3 3}=n
$$

This is the equal case:

$$
\boxed{\Theta(n\log n)}
$$

#### 3.

$$
n^{\log_2 4}=n^2
$$

Since $n^3$ is larger:

$$
\boxed{\Theta(n^3)}
$$

#### 4.

$$
n^{\log_4 16}=n^2
$$

This is the equal case:

$$
\boxed{\Theta(n^2\log n)}
$$

#### 5.

The critical function is:

$$
n^{\log_2 2}=n
$$

Since $f(n)=n\log n$, the generalized equal case gives:

$$
\boxed{\Theta(n\log^2 n)}
$$

#### 6.

$$
n^{\log_2 1}=1
$$

Since $f(n)=n$ dominates:

$$
\boxed{\Theta(n)}
$$

## Final Summary

### Asymptotic Notation

$$
O(g(n)):\ \text{upper bound}
$$

$$
\Omega(g(n)):\ \text{lower bound}
$$

$$
\Theta(g(n)):\ \text{tight bound}
$$

$$
o(g(n)):\ \text{strictly slower growth}
$$

### Simplified Master Theorem

For

$$
T(n)=aT(n/b)+\Theta(n^d)
$$

compute:

$$
p=\log_b a
$$

Then:

$$
\boxed{
T(n)=
\begin{cases}
\Theta(n^p), & d<p, \\[4pt]
\Theta(n^p\log n), & d=p, \\[4pt]
\Theta(n^d), & d>p.
\end{cases}}
$$

The central idea is to compare the work caused by **recursive branching**, $n^{\log_b a}$, with the algorithm's **local work**, $f(n)$.
