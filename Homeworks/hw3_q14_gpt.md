# Convex Sets and Convex Functions — A Step-by-Step Guide

The key to solving all four parts is to understand the definition of convexity and know when to use a proof versus a counterexample. You do not need derivatives for any of these problems.

We'll build the background first, then solve each part with detailed reasoning, examples, and visual intuition.

## 1. Background: What does convex mean?

### A. Convex sets

A set $K\subseteq\mathbb R^n$ is convex if, whenever you choose any two points $x,y\in K$, the entire line segment joining them also lies in $K$.

Mathematically,

$$
\boxed{tx+(1-t)y\in K}
$$

for every $x,y\in K$ and every $t\in[0,1]$.

Here:

- $t=0$ gives you $y$.
- $t=1$ gives you $x$.
- Values between 0 and 1 give you the points between them.

geometry - Strong convexity on sets? - Mathematics Stack Exchange

Convex set

Every segment between two points stays inside the set.

File:Convex polygon illustration2.svg - Wikimedia Commons

Nonconvex set

At least one segment between two points leaves the set.

Examples of convex sets include intervals such as $[0,1]$, disks, squares, and the whole space $\mathbb R^n$.

An important detail: a convex set does not have to be closed or bounded. For example, $(0,1)$ is convex.

### B. Convex functions

A function $f:\mathbb R\to\mathbb R$ is convex if, for every $x,y\in\mathbb R$ and every $t\in[0,1]$,

$$
\boxed{
f(tx+(1-t)y)
\leq tf(x)+(1-t)f(y)
}
$$

This inequality is the most important tool in the entire exercise.

The left-hand side is the function value at a point between $x$ and $y$. The right-hand side is the corresponding weighted average of the endpoint function values.

In plain language:

A convex function lies below or on the straight line connecting any two points on its graph.

아래로 볼록과 위로 볼록::::수학과 사는 이야기

For a convex parabola, the chord joining two points on its graph stays above the graph between those points.

Examples:

- $f(x)=x^2$ is convex.
- $f(x)=|x|$ is convex, even though it is not differentiable at $x=0$.
- $f(x)=3x+2$ is convex because every affine function is convex.

A function does not need to be differentiable to be convex. That's why we'll rely on the defining inequality rather than derivative tests.

## 2. A strategy for the four questions

Before solving anything, identify what kind of object you have.

| Problem | Object | Best strategy |
| --- | --- | --- |
| 1 | Intersection and union of sets | Use the line-segment definition |
| 2 | Sum of functions | Add the two convexity inequalities |
| 3 | Product of functions | Test a simple counterexample |
| 4 | Maximum of functions | Compare the maximum with each function |

A useful rule for all four questions:

- To prove a statement is always true, start with arbitrary points or arbitrary convex functions and use the definition.
- To disprove a statement, find just one valid counterexample. One counterexample is enough to show that a universal claim is false.

## 3. Part 1 — Are intersections and unions of convex sets convex?

The question has two separate claims, so we must analyze them independently.

### Part 1(a): Must $K\cap L$ be convex?

Answer: Yes.

### Step-by-step proof

Step 1: Start with two arbitrary points.

Suppose $K,L\subseteq\mathbb R^n$ are convex. Choose any two points

$$
x,y\in K\cap L.
$$

What does membership in the intersection mean? It means both points belong to both sets:

$$
x,y\in K \quad\text{and}\quad x,y\in L.
$$

Step 2: Use convexity of $K$.

Since $K$ is convex, for every $t\in[0,1]$,

$$
tx+(1-t)y\in K.
$$

Step 3: Use convexity of $L$.

Since $L$ is also convex,

$$
tx+(1-t)y\in L.
$$

Step 4: Combine the conclusions.

The point $tx+(1-t)y$ belongs to both $K$ and $L$. Therefore,

$$
tx+(1-t)y\in K\cap L.
$$

This is precisely the definition of a convex set. Hence

$$
\boxed{K\cap L\text{ is convex}.}
$$

### Visual intuition

Imagine two overlapping disks. Their intersection is the region shared by both disks.

If you choose two points in that shared region, the line segment joining them stays inside the first disk and inside the second disk. Therefore, it stays inside their intersection.

Question 18: In the figure above, A and b are the centers of : Multiple-choice Questions — Select One Answer Choice

The shared lens-shaped region is convex: every segment between two points in it stays in the shared region.

The central idea is that a segment that lies in both sets must lie in their intersection.

### Part 1(b): Must $K\cup L$ be convex?

Answer: No.

To disprove this claim, we need just one counterexample.

### Step-by-step counterexample

Step 1: Choose two convex sets.

Let

$$
K=[0,1],\qquad L=[2,3].
$$

Both are intervals in $\mathbb R$, so both are convex.

Step 2: Take their union.

Their union is

$$
K\cup L=[0,1]\cup[2,3].
$$

Notice the gap between $1$ and $2$.

Step 3: Find two points in the union.

Choose

$$
x=0,\qquad y=3.
$$

Both belong to $K\cup L$.

Step 4: Find a point between them that is missing.

Take their midpoint:

$$
\frac{x+y}{2}=\frac{0+3}{2}=1.5.
$$

But

$$
1.5\notin [0,1]\cup[2,3].
$$

Thus, the segment between two points in the union does not stay entirely in the union.

Therefore,

$$
\boxed{K\cup L\text{ need not be convex}.}
$$

### Visual intuition

The number line for the counterexample

Green: points in the union

Red: midpoint not in the union

Important distinction: A union of convex sets can be convex in some cases—for example, if one set contains the other. The statement is that the union is not necessarily convex.

## 4. Part 2 — Is the sum of two convex functions convex?

Suppose $f,g:\mathbb R\to\mathbb R$ are convex, and define

$$
h(x)=f(x)+g(x).
$$

Answer: Yes. The sum of convex functions is convex.

### Step-by-step proof

Step 1: Recall what we must prove.

We need to establish that, for all $x,y\in\mathbb R$ and $t\in[0,1]$,

$$
h(tx+(1-t)y)
\leq th(x)+(1-t)h(y).
$$

Step 2: Expand the definition of $h$.

The left-hand side is

$$
\begin{aligned}
h(tx+(1-t)y)
={}&f(tx+(1-t)y)\\
&+g(tx+(1-t)y).
\end{aligned}
$$

Step 3: Apply convexity separately to $f$ and $g$.

Because $f$ is convex,

$$
f(tx+(1-t)y)
\leq tf(x)+(1-t)f(y).
$$

Because $g$ is convex,

$$
g(tx+(1-t)y)
\leq tg(x)+(1-t)g(y).
$$

Step 4: Add the inequalities.

Adding the left and right sides gives

$$
\begin{aligned}
h(tx+(1-t)y)
&\leq tf(x)+(1-t)f(y)\\
&\quad+tg(x)+(1-t)g(y).
\end{aligned}
$$

Group the terms:

$$
\begin{aligned}
h(tx+(1-t)y)
&\leq t[f(x)+g(x)]\\
&\quad+(1-t)[f(y)+g(y)].
\end{aligned}
$$

Since $h=f+g$, this becomes

$$
\boxed{
h(tx+(1-t)y)\leq th(x)+(1-t)h(y).
}
$$

That is the definition of convexity. Therefore,

$$
\boxed{f+g\text{ is convex}.}
$$

### Example

Let

$$
f(x)=x^2,\qquad g(x)=|x|.
$$

Both functions are convex, so their sum

$$
h(x)=x^2+|x|
$$

is convex.

Fonctions - forum mathématiques - 644207

Adding two convex functions preserves convexity. The graph may have a corner, so differentiability is not required.

### Why this proof is useful

Notice that we never needed a formula for the derivatives of $f$ or $g$. We used only their defining inequalities.

This proof also generalizes: any finite sum of convex functions is convex.

## 5. Part 3 — Is the product of two convex functions convex?

Suppose $f,g:\mathbb R\to\mathbb R$ are convex, and define

$$
h(x)=f(x)g(x).
$$

Answer: No. The product of two convex functions need not be convex.

This is a perfect opportunity to use a counterexample.

### Step-by-step counterexample

Step 1: Choose two simple functions.

Let

$$
f(x)=x,\qquad g(x)=-x.
$$

Why choose these? Because linear functions are convex, and their product is easy to calculate.

Step 2: Verify that both functions are convex.

Every affine function $ax+b$, where $a,b$ are constants, is convex.

In particular, both $f(x)=x$ and $g(x)=-x$ are convex.

To see this directly, for $f(x)=x$,

$$
\begin{aligned}
f(tx+(1-t)y)
&=tx+(1-t)y\\
&=tf(x)+(1-t)f(y).
\end{aligned}
$$

We have equality in the convexity inequality. The same reasoning works for $g(x)=-x$.

Step 3: Calculate the product.

We obtain

$$
h(x)=f(x)g(x)=x(-x)=-x^2.
$$

Step 4: Show that $h$ is not convex.

Choose $x=-1$, $y=1$, and $t=\frac12$.

The midpoint is $0$, and

$$
h(0)=0.
$$

But the average of the endpoint values is

$$
\frac{h(-1)+h(1)}{2}
=\frac{-1-1}{2}=-1.
$$

For convexity, we would need

$$
h(0)\leq\frac{h(-1)+h(1)}2.
$$

That would require

$$
0\leq-1,
$$

which is false.

Therefore,

$$
\boxed{fg\text{ need not be convex}.}
$$

### Visual intuition

1.1 Functions and Function Notation - Precalculus 2e | OpenStax

The original functions

Both are straight lines, hence convex.

Графика На Функцията y = ax^2, a ≠ 0. Упражнение

Their product

The graph bends downward, violating convexity.

The essential observation is that the product is a downward-opening parabola. At the midpoint $x=0$, its value is higher than the average of its values at $x=-1$ and $x=1$. Convexity requires the opposite inequality.

### Why doesn't the sum proof work for products?

For sums, we could add two inequalities and preserve their direction.

For products, we would need to multiply inequalities involving function values. But multiplying inequalities is delicate: the result depends on the signs of the quantities involved. Convex functions are not necessarily nonnegative.

For example, $f(x)=x$ is convex even though it takes negative values. This is one reason there is no general rule that the product of two convex functions is convex.

A useful nuance: The product can be convex under additional assumptions, but convexity of the two factors alone is insufficient.

## 6. Part 4 — Is the maximum of two convex functions convex?

Suppose $f,g:\mathbb R\to\mathbb R$ are convex, and define

$$
h(x)=\max\{f(x),g(x)\}.
$$

Here, the maximum is taken pointwise. At each input $x$, we choose whichever function has the larger value.

Answer: Yes. The pointwise maximum of two convex functions is convex.

### Step-by-step proof

The key is to show that both $f$ and $g$ are bounded above by the same expression.

Step 1: Choose arbitrary $x,y\in\mathbb R$ and $t\in[0,1]$.

Set

$$
z=tx+(1-t)y.
$$

We need to prove

$$
h(z)\leq th(x)+(1-t)h(y).
$$

Step 2: Apply convexity to $f$.

Since $f$ is convex,

$$
f(z)\leq tf(x)+(1-t)f(y).
$$

By definition of the maximum,

$$
f(x)\leq h(x),\qquad f(y)\leq h(y).
$$

Because $t$ and $1-t$ are nonnegative, we can substitute these bounds to obtain

$$
f(z)\leq th(x)+(1-t)h(y).
$$

Step 3: Apply the same reasoning to $g$.

Convexity of $g$ gives

$$
g(z)\leq tg(x)+(1-t)g(y).
$$

Using $g(x)\leq h(x)$ and $g(y)\leq h(y)$,

$$
g(z)\leq th(x)+(1-t)h(y).
$$

Step 4: Take the maximum.

We have shown that both $f(z)$ and $g(z)$ are at most $th(x)+(1-t)h(y)$.

Consequently, their maximum is also at most that quantity:

$$
\begin{aligned}
h(z)&=\max\{f(z),g(z)\}\\
&\leq th(x)+(1-t)h(y).
\end{aligned}
$$

Substitute $z=tx+(1-t)y$:

$$
\boxed{
h(tx+(1-t)y)
\leq th(x)+(1-t)h(y).
}
$$

This is exactly the definition of convexity. Therefore,

$$
\boxed{\max\{f,g\}\text{ is convex}.}
$$

### Visual intuition: The upper envelope

Imagine drawing two convex curves. At each point on the horizontal axis, keep the point on whichever curve is higher. The resulting graph is called the upper envelope of the two functions.

Machine Learning cơ bản

The maximum follows the higher graph at each input. The resulting upper envelope remains convex, although it may have a corner where the active function changes.

### A concrete example

Let

$$
f(x)=x,\qquad g(x)=-x.
$$

Both are convex, and their pointwise maximum is

$$
h(x)=\max\{x,-x\}=|x|.
$$

The absolute value function is convex, even though it has a sharp corner at $x=0$.

This example is particularly helpful because it illustrates that the maximum operation can create a nondifferentiable function without destroying convexity.

## 7. Summary of all four answers

| Part | Statement | Answer | Main reason |
| --- | --- | --- | --- |
| 1(a) | $K\cap L$ is convex | Yes | A segment in both sets is in their intersection. |
| 1(b) | $K\cup L$ is convex | No, not always | Two disjoint intervals can have a gap. |
| 2 | $f+g$ is convex | Yes | Add the two convexity inequalities. |
| 3 | $fg$ is convex | No, not always | $f(x)=x,\ g(x)=-x$ give $h(x)=-x^2$. |
| 4 | $\max\{f,g\}$ is convex | Yes | Both functions are bounded above by the same convexity expression. |

## 8. Test your understanding

Try these three short questions to check whether the main ideas have clicked.

Question 1

If $K$ and $L$ are convex, which fact guarantees that $K\cap L$ is convex?

The intersection always contains every point in $\mathbb R^n$.

A segment between points in the intersection lies in both sets.

The intersection of any two sets is convex.

Question 2

If $f$ and $g$ are convex, which operation is guaranteed to preserve convexity?

Their pointwise product $fg$.

Their sum $f+g$.

Both operations, without any additional assumptions.

Question 3

Why is $h(x)=\max\{f(x),g(x)\}$ convex?

Because the maximum of any two functions is convex.

Because the maximum is always differentiable.

Because both function values satisfy the same upper bound from convexity.

 Check answers

## 9\. Final advice for writing your proof on an exam

You can solve this whole exercise without derivatives by remembering three proof patterns:

1. For sets: Start with arbitrary $x,y$ in the set and prove that $tx+(1-t)y$ remains in it.
2. For functions: Write the convexity inequality and use it to establish the required inequality for the new function.
3. For false statements: Give a simple counterexample and explicitly show which convexity condition fails.

The most important distinction is that addition and pointwise maximum preserve convexity, but pointwise multiplication does not necessarily do so. And for sets, intersection preserves convexity, while union does not necessarily preserve it.
