# 14. Convex Sets and Convex Functions

The key to all four parts is to work directly from the definitions. Differentiation is unnecessary, so the proofs apply even to convex functions with corners, such as $f(x)=|x|$.

---

## 1. Background and definitions

### Convex sets

A set $K\subseteq \mathbb{R}^n$ is **convex** if, for every $x,y\in K$ and every $\lambda\in[0,1]$,

$$
\lambda x+(1-\lambda)y\in K.
$$

The point

$$
z=\lambda x+(1-\lambda)y
$$

lies on the line segment connecting $x$ and $y$.

### Geometric interpretation

A set is convex if the complete line segment between any two points in the set remains inside the set:

```text
x •================• y
      all inside K
```

A nonconvex set has at least one pair of points for which part of the connecting segment leaves the set:

```text
x •======      ======• y
        outside
```

---

### Convex functions

A function $f:\mathbb{R}\to\mathbb{R}$ is **convex** if, for every $x,y\in\mathbb{R}$ and every $\lambda\in[0,1]$,

$$
f\bigl(\lambda x+(1-\lambda)y\bigr)
\leq
\lambda f(x)+(1-\lambda)f(y).
$$

This is often called the **convexity inequality**.

### Geometric interpretation

Let

$$
z=\lambda x+(1-\lambda)y.
$$

Then:

- $f(z)$ is the height of the function at the intermediate point $z$;
- $\lambda f(x)+(1-\lambda)f(y)$ is the height of the chord connecting $(x,f(x))$ and $(y,f(y))$.

Thus, a function is convex when its graph lies below every chord connecting two points on the graph.

```text
height
  ^
  |   •----------------•  chord
  |     \            /
  |      \__________/     convex graph
  +------------------------> x
```

Notice that the definition uses only function values and inequalities. It does not require derivatives.

---

# Part 1: Intersection and union of convex sets

## Question 1(a)

If $K,L\subseteq\mathbb{R}^n$ are convex, must $K\cap L$ be convex?

## Answer

$$
\boxed{\text{Yes, }K\cap L\text{ must be convex.}}
$$

## Proof

To prove that $K\cap L$ is convex, choose arbitrary points

$$
x,y\in K\cap L
$$

and an arbitrary $\lambda\in[0,1]$.

Because $x,y\in K\cap L$, both points belong to both sets:

$$
x,y\in K
\qquad\text{and}\qquad
x,y\in L.
$$

Since $K$ is convex,

$$
\lambda x+(1-\lambda)y\in K.
$$

Since $L$ is convex,

$$
\lambda x+(1-\lambda)y\in L.
$$

Therefore, the point belongs to both $K$ and $L$:

$$
\lambda x+(1-\lambda)y\in K\cap L.
$$

This proves that $K\cap L$ is convex.

$$
\boxed{K\cap L\text{ is convex.}}
$$

---

## Visualization

Suppose $K$ and $L$ are overlapping disks:

```text
            K                 L
       ___________       ___________
      /           \_____/           \
     /             #####             \
    |              #####              |
     \             #####             /
      \___________/     \___________/

                    #####
                  intersection
```

If two points are in the intersection, they are in both sets. Each set contains the whole line segment, so their intersection does as well.

---

## Important generalization

The same proof works for the intersection of any collection of convex sets.

If $\{K_i\}_{i\in I}$ is a family of convex sets, then

$$
\bigcap_{i\in I} K_i
$$

is convex, provided the intersection is interpreted in the usual set-theoretic sense. The intersection may be empty, and under the standard convention, the empty set is convex because there are no points violating the definition.

---

## Question 1(b)

If $K,L\subseteq\mathbb{R}^n$ are convex, must $K\cup L$ be convex?

## Answer

$$
\boxed{\text{No, }K\cup L\text{ need not be convex.}}
$$

To disprove a universal statement, it is enough to provide one counterexample.

---

## Counterexample in $\mathbb{R}$

Let

$$
K=[-2,-1],
\qquad
L=[1,2].
$$

Both $K$ and $L$ are intervals, so both are convex.

Their union is

$$
K\cup L=[-2,-1]\cup[1,2].
$$

Choose

$$
x=-1\in K,
\qquad
y=1\in L,
\qquad
\lambda=\frac12.
$$

Their midpoint is

$$
\lambda x+(1-\lambda)y
=
\frac12(-1)+\frac12(1)
=
0.
$$

But

$$
0\notin [-2,-1]\cup[1,2].
$$

Therefore, the union does not contain the entire segment between $x$ and $y$, so it is not convex.

$$
\boxed{K\cup L\text{ is not necessarily convex.}}
$$

---

## Visualization

```text
K                         L
●==========●             ●==========●
-2        -1             1          2
             \           /
              \         /
               midpoint
                  0
```

The midpoint $0$ lies in the gap and therefore lies outside the union.

---

## Important nuance

The union of two convex sets **can** be convex in some cases. It simply need not be convex.

For example,

$$
K=[0,2],
\qquad
L=[1,3]
$$

are convex, and

$$
K\cup L=[0,3]
$$

is also convex.

Thus, the correct statement is:

$$
\boxed{\text{A union of convex sets may or may not be convex.}}
$$

---

# Part 2: Sum of convex functions

## Question

If $f,g:\mathbb{R}\to\mathbb{R}$ are convex, must $f+g$ be convex?

## Answer

$$
\boxed{\text{Yes, }f+g\text{ must be convex.}}
$$

---

## Step-by-step proof

Define

$$
h(x)=f(x)+g(x).
$$

We need to prove that, for all $x,y\in\mathbb{R}$ and $\lambda\in[0,1]$,

$$
h\bigl(\lambda x+(1-\lambda)y\bigr)
\leq
\lambda h(x)+(1-\lambda)h(y).
$$

Let

$$
z=\lambda x+(1-\lambda)y.
$$

Then

$$
h(z)=f(z)+g(z).
$$

Since $f$ is convex,

$$
f(z)\leq \lambda f(x)+(1-\lambda)f(y).
$$

Since $g$ is convex,

$$
g(z)\leq \lambda g(x)+(1-\lambda)g(y).
$$

Add these two inequalities:

$$
f(z)+g(z)
\leq
\lambda f(x)+(1-\lambda)f(y)
+
\lambda g(x)+(1-\lambda)g(y).
$$

Group the terms with the same coefficients:

$$
f(z)+g(z)
\leq
\lambda\bigl(f(x)+g(x)\bigr)
+
(1-\lambda)\bigl(f(y)+g(y)\bigr).
$$

Since $h=f+g$,

$$
h(z)\leq \lambda h(x)+(1-\lambda)h(y).
$$

Substituting back $z=\lambda x+(1-\lambda)y$,

$$
h\bigl(\lambda x+(1-\lambda)y\bigr)
\leq
\lambda h(x)+(1-\lambda)h(y).
$$

Therefore,

$$
\boxed{f+g\text{ is convex.}}
$$

---

## Example

Consider

$$
f(x)=x^2,
\qquad
g(x)=|x|.
$$

Both functions are convex. Their sum is

$$
h(x)=x^2+|x|.
$$

The absolute-value function is nondifferentiable at $x=0$, but the preceding proof still applies.

```text
y
^
|                     /
|                  __/
|               __/
|             _/
|           _/
|__________/ \__________
+------------------------> x
           0
```

The graph has a corner at $0$, but it is still convex.

---

## Useful generalization

If $f_1,\ldots,f_m$ are convex and $a_1,\ldots,a_m\geq 0$, then

$$
h(x)=\sum_{i=1}^m a_i f_i(x)
$$

is convex.

The condition $a_i\geq0$ matters. Multiplication by a negative number reverses the convexity inequality and generally produces a concave function.

For example, $x^2$ is convex, but $-x^2$ is not convex.

---

# Part 3: Product of convex functions

## Question

If $f,g:\mathbb{R}\to\mathbb{R}$ are convex, must

$$
h(x)=f(x)g(x)
$$

be convex?

## Answer

$$
\boxed{\text{No, the product need not be convex.}}
$$

---

## Strategy for finding a counterexample

We need two functions satisfying:

1. $f$ is convex;
2. $g$ is convex;
3. $fg$ is not convex.

A simple observation is that every affine function

$$
\ell(x)=ax+b
$$

is convex. Indeed,

$$
\ell\bigl(\lambda x+(1-\lambda)y\bigr)
=
\lambda\ell(x)+(1-\lambda)\ell(y),
$$

so the convexity inequality holds with equality.

This suggests choosing two affine functions whose product is concave.

---

## Counterexample

Let

$$
f(x)=x,
\qquad
g(x)=-x.
$$

Both are affine and hence convex.

Their product is

$$
h(x)=f(x)g(x)=x(-x)=-x^2.
$$

We now show directly from the definition that $h$ is not convex.

Choose

$$
x=-1,\qquad y=1,\qquad \lambda=\frac12.
$$

The midpoint is

$$
\lambda x+(1-\lambda)y
=
\frac12(-1)+\frac12(1)
=
0.
$$

Evaluate $h$:

$$
h(0)=0,
$$

while

$$
\frac12h(-1)+\frac12h(1)
=
\frac12(-1)+\frac12(-1)
=
-1.
$$

For convexity, we would need

$$
h(0)\leq \frac12h(-1)+\frac12h(1).
$$

That would mean

$$
0\leq -1,
$$

which is false.

Hence $h(x)=-x^2$ is not convex.

Therefore,

$$
\boxed{\text{The pointwise product of convex functions need not be convex.}}
$$

---

## Visualization

The function

$$
h(x)=-x^2
$$

opens downward:

```text
y
^
|               • (0,0)
|             /   \
|           /       \
|   •-------------------•  chord at height -1
| (-1,-1)           (1,-1)
+----------------------------> x
```

The graph at the midpoint lies **above** the chord:

$$
h(0)=0>-1.
$$

That is the opposite of the convexity requirement.

---

## Why the direct proof used for sums does not work

For the sum, we can add inequalities:

$$
f(z)\leq \lambda f(x)+(1-\lambda)f(y),
$$

$$
g(z)\leq \lambda g(x)+(1-\lambda)g(y).
$$

Adding inequalities always preserves the inequality:

$$
f(z)+g(z)
\leq
\lambda[f(x)+g(x)]
+
(1-\lambda)[f(y)+g(y)].
$$

For products, multiplying the inequalities would produce

$$
f(z)g(z)
\leq
\bigl(\lambda f(x)+(1-\lambda)f(y)\bigr)
\bigl(\lambda g(x)+(1-\lambda)g(y)\bigr)
$$

only under appropriate sign conditions. Even then, the right-hand side contains cross terms:

$$
\begin{aligned}
&\bigl(\lambda f(x)+(1-\lambda)f(y)\bigr)
 \bigl(\lambda g(x)+(1-\lambda)g(y)\bigr) \\
&=
\lambda^2 f(x)g(x)
+
\lambda(1-\lambda)f(x)g(y) \\
&\quad+
\lambda(1-\lambda)f(y)g(x)
+
(1-\lambda)^2 f(y)g(y).
\end{aligned}
$$

This is not the desired convex combination

$$
\lambda f(x)g(x)+(1-\lambda)f(y)g(y).
$$

So convexity is not generally preserved by multiplication.

---

## A case where the product is convex

The claim is not that products are never convex.

For example,

$$
f(x)=x^2,\qquad g(x)=x^2
$$

are convex, and their product is

$$
h(x)=x^4,
$$

which is also convex.

The conclusion is only:

$$
\boxed{\text{Convexity of }f\text{ and }g\text{ alone does not guarantee convexity of }fg.}
$$

---

# Part 4: Maximum of convex functions

## Question

If $f,g:\mathbb{R}\to\mathbb{R}$ are convex, must

$$
h(x)=\max\{f(x),g(x)\}
$$

be convex?

## Answer

$$
\boxed{\text{Yes, the pointwise maximum is convex.}}
$$

---

## Step-by-step proof

Define

$$
h(x)=\max\{f(x),g(x)\}.
$$

Choose arbitrary $x,y\in\mathbb{R}$ and $\lambda\in[0,1]$. Let

$$
z=\lambda x+(1-\lambda)y.
$$

We need to prove

$$
h(z)\leq \lambda h(x)+(1-\lambda)h(y).
$$

Since

$$
h(z)=\max\{f(z),g(z)\},
$$

we handle $f(z)$ and $g(z)$ separately.

---

### Step 1: Bound $f(z)$

By convexity of $f$,

$$
f(z)\leq \lambda f(x)+(1-\lambda)f(y).
$$

By the definition of $h$,

$$
f(x)\leq h(x),
\qquad
f(y)\leq h(y).
$$

Because $\lambda\geq0$ and $1-\lambda\geq0$,

$$
\lambda f(x)+(1-\lambda)f(y)
\leq
\lambda h(x)+(1-\lambda)h(y).
$$

Therefore,

$$
f(z)\leq \lambda h(x)+(1-\lambda)h(y).
$$

---

### Step 2: Bound $g(z)$

Similarly, convexity of $g$ gives

$$
g(z)\leq \lambda g(x)+(1-\lambda)g(y).
$$

Since

$$
g(x)\leq h(x),
\qquad
g(y)\leq h(y),
$$

we get

$$
g(z)\leq \lambda h(x)+(1-\lambda)h(y).
$$

---

### Step 3: Take the maximum

Both $f(z)$ and $g(z)$ are bounded above by the same quantity:

$$
f(z)\leq \lambda h(x)+(1-\lambda)h(y),
$$

$$
g(z)\leq \lambda h(x)+(1-\lambda)h(y).
$$

Therefore, their maximum is also bounded above by that quantity:

$$
\max\{f(z),g(z)\}
\leq
\lambda h(x)+(1-\lambda)h(y).
$$

Since $h(z)=\max\{f(z),g(z)\}$,

$$
h(z)\leq \lambda h(x)+(1-\lambda)h(y).
$$

Thus,

$$
\boxed{h(x)=\max\{f(x),g(x)\}\text{ is convex.}}
$$

---

## Example: absolute value as a maximum

Let

$$
f(x)=x,
\qquad
g(x)=-x.
$$

Both functions are affine and hence convex. Their maximum is

$$
h(x)=\max\{x,-x\}=|x|.
$$

Therefore, this result immediately shows that $|x|$ is convex.

```text
y
^
| \             /
|  \           /
|   \         /
|    \       /
|     \     /
|      \   /
|       \ /
|        •
+----------------------> x
         0
```

The maximum follows:

- $g(x)=-x$ when $x\leq0$;
- $f(x)=x$ when $x\geq0$.

The resulting function can have a corner where the active function changes, but it remains convex.

---

## Epigraph visualization

There is another useful way to understand the maximum result.

The **epigraph** of a function $f$ is

$$
\operatorname{epi}(f)
=
\{(x,t)\in\mathbb{R}^2:t\geq f(x)\}.
$$

A function is convex exactly when its epigraph is a convex set.

For

$$
h(x)=\max\{f(x),g(x)\},
$$

we have

$$
\begin{aligned}
t\geq h(x)
&\iff t\geq\max\{f(x),g(x)\}\\
&\iff t\geq f(x)\text{ and }t\geq g(x).
\end{aligned}
$$

Therefore,

$$
\operatorname{epi}(h)
=
\operatorname{epi}(f)\cap\operatorname{epi}(g).
$$

Because $f$ and $g$ are convex, their epigraphs are convex. From Part 1, the intersection of convex sets is convex. Hence $\operatorname{epi}(h)$ is convex, which means $h$ is convex.

This reveals a close connection between Parts 1 and 4:

$$
\boxed{
\text{Maximum of convex functions}
\quad\longleftrightarrow\quad
\text{intersection of convex epigraphs}.
}
$$

---

# Final answers

| Part | Operation | Always convex? | Main reason |
|---|---|---:|---|
| 1(a) | $K\cap L$ | Yes | A segment in both sets remains in both sets |
| 1(b) | $K\cup L$ | No | A segment may pass through a gap between the sets |
| 2 | $f+g$ | Yes | Add the two convexity inequalities |
| 3 | $fg$ | No | Example: $x(-x)=-x^2$ |
| 4 | $\max\{f,g\}$ | Yes | Each function is bounded by the same convex combination |

In compact form:

$$
\boxed{
\begin{aligned}
K\cap L&:\text{ convex},\\
K\cup L&:\text{ not necessarily convex},\\
f+g&:\text{ convex},\\
fg&:\text{ not necessarily convex},\\
\max\{f,g\}&:\text{ convex}.
\end{aligned}
}
$$

---

# A reusable problem-solving method

For questions asking whether an operation preserves convexity, use the following workflow.

## Step 1: Write the definition

For sets:

$$
x,y\in K,\quad \lambda\in[0,1]
\quad\Longrightarrow\quad
\lambda x+(1-\lambda)y\in K.
$$

For functions:

$$
f\bigl(\lambda x+(1-\lambda)y\bigr)
\leq
\lambda f(x)+(1-\lambda)f(y).
$$

## Step 2: Try a direct proof

Start with the left-hand side of the desired inequality and apply convexity to the original functions.

This succeeds naturally for:

- nonnegative weighted sums;
- pointwise maxima;
- intersections of convex sets.

## Step 3: If the proof stalls, search for a counterexample

Use simple convex objects:

- intervals for convex sets;
- affine functions;
- constant functions;
- $x^2$;
- $|x|$.

Affine functions are especially useful because they are both convex and concave.

## Step 4: Test the midpoint first

To disprove convexity, it is enough to find $x,y$ for which the midpoint inequality fails:

$$
f\left(\frac{x+y}{2}\right)
>
\frac{f(x)+f(y)}{2}.
$$

This is not a complete test for proving convexity, but it is often the fastest way to disprove it.

For the product counterexample:

$$
h(x)=-x^2,
$$

$$
h(0)=0
>
-1
=
\frac{h(-1)+h(1)}{2}.
$$

That single violation establishes nonconvexity.

---

## Common misconception: maximum versus minimum

The pointwise maximum of convex functions is convex, but the pointwise minimum need not be.

For example, let

$$
f(x)=x,
\qquad
g(x)=-x.
$$

Then

$$
\min\{f(x),g(x)\}=-|x|,
$$

which is not convex.

Indeed,

$$
-|0|=0
>
-1
=
\frac{-|-1|+-|1|}{2}.
$$

Thus,

$$
\boxed{
\max\{\text{convex functions}\}\text{ preserves convexity, but }
\min\{\text{convex functions}\}\text{ generally does not.}
}
$$
