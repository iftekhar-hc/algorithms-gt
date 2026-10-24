# Linear Programming Formulation for Minimum \(L_\infty\) Distance to a Convex Polygon

## Problem Statement

Let \(P\) be a convex polygon given by

$$
a_i x + b_i y \le c_i, \qquad i=1,\ldots,m.
$$

Given a fixed point

$$
q=(x_0,y_0),
$$

find a point

$$
p=(x_1,y_1)\in P
$$

that minimizes

$$
\|p-q\|_\infty
=
\max\{|x_1-x_0|,|y_1-y_0|\}.
$$

The goal is to formulate this as a **Linear Program (LP)**.

---

# Step 1: What is a Convex Polygon?

A polygon \(P\) is **convex** if, whenever two points \(u,v\in P\) are chosen, the entire line segment joining them also lies in \(P\).

Formally:

$$
u,v\in P
\implies
\lambda u +(1-\lambda)v \in P
\quad\forall \lambda\in[0,1].
$$

### Example

A square is convex.

A star-shaped polygon is not convex because a line segment connecting two interior points may leave the region.

## Why is

$$
a_i x+b_i y\le c_i
$$

a convex set?

Each inequality defines a **half-plane**.

For example,

$$
x+y\le 5
$$

contains all points on one side of the line

$$
x+y=5.
$$

A convex polygon is the intersection of finitely many half-planes:

$$
P
=
\bigcap_{i=1}^m
\{(x,y): a_i x+b_i y\le c_i\}.
$$

Since intersections of convex sets remain convex, \(P\) is convex.

---

# Step 2: Understanding Norms

The problem involves the \(L_\infty\)-norm.

## \(L_2\) Norm (Euclidean Distance)

$$
\|(x,y)\|_2
=
\sqrt{x^2+y^2}.
$$

The unit ball is

$$
x^2+y^2\le1,
$$

which is a circle.

---

## \(L_1\) Norm (Manhattan Distance)

$$
\|(x,y)\|_1
=
|x|+|y|.
$$

The unit ball is

$$
|x|+|y|\le1,
$$

which forms a diamond.

---

## \(L_\infty\) Norm (Maximum Coordinate Distance)

$$
\|(x,y)\|_\infty
=
\max\{|x|,|y|\}.
$$

The unit ball is

$$
\max(|x|,|y|)\le1.
$$

Equivalently,

$$
|x|\le1,
\qquad
|y|\le1.
$$

The unit ball is a square.

---

## Geometric Meaning Here

We want the smallest axis-aligned square centered at \(q=(x_0,y_0)\) that touches the polygon \(P\).

The radius of that square is the optimal value.

---

# Step 3: Why the Objective Is Not Yet Linear

The quantity

$$
\max\{|x_1-x_0|,\;|y_1-y_0|\}
$$

contains:

- Absolute values
- A maximum operator

Neither appears directly in standard LP form.

We therefore introduce an auxiliary variable.

---

# Step 4: Introduce a Distance Variable

Let

$$
t
=
\max\{|x_1-x_0|,\;|y_1-y_0|\}.
$$

We want to minimize \(t\).

To ensure \(t\) is at least each absolute value:

$$
t \ge |x_1-x_0|,
$$

$$
t \ge |y_1-y_0|.
$$

---

# Step 5: Remove Absolute Values

Recall:

$$
|z|\le t
$$

is equivalent to

$$
-t\le z\le t.
$$

Thus

$$
|x_1-x_0|\le t
$$

becomes

$$
x_1-x_0\le t,
$$

$$
x_0-x_1\le t.
$$

Likewise,

$$
|y_1-y_0|\le t
$$

becomes

$$
y_1-y_0\le t,
$$

$$
y_0-y_1\le t.
$$

All are linear constraints.

---

# Step 6: Keep the Point Inside the Polygon

Since \(p=(x_1,y_1)\) must belong to \(P\),

$$
a_i x_1+b_i y_1 \le c_i,
\qquad
i=1,\ldots,m.
$$

These are already linear.

---

# Final LP Formulation

### Variables

$$
x_1,\; y_1,\; t.
$$

### Objective

$$
\min t.
$$

### Subject to

#### Polygon Constraints

$$
a_i x_1+b_i y_1 \le c_i,
\qquad i=1,\ldots,m.
$$

#### \(L_\infty\) Distance Constraints

$$
x_1-x_0\le t,
$$

$$
x_0-x_1\le t,
$$

$$
y_1-y_0\le t,
$$

$$
y_0-y_1\le t.
$$

Optionally,

$$
t\ge0.
$$

---

# Why This Works

The four inequalities imply

$$
|x_1-x_0|\le t,
$$

and

$$
|y_1-y_0|\le t.
$$

Therefore,

$$
\max\{|x_1-x_0|,|y_1-y_0|\}
\le t.
$$

Since the LP minimizes \(t\), at optimality:

$$
t
=
\max\{|x_1-x_0|,|y_1-y_0|\}.
$$

Thus \(t\) equals the minimum \(L_\infty\) distance.

---

# Geometric Interpretation

Suppose

$$
q=(5,7).
$$

For a given value of \(t\), the constraints

$$
|x-5|\le t,
\qquad
|y-7|\le t
$$

define the square

$$
[5-t,5+t]\times[7-t,7+t].
$$

The LP is finding the **smallest such square that intersects the polygon**.

At optimality:

- If \(q\in P\), then \(t=0\).
- Otherwise, the square expands until it first touches \(P\).

---

# Alternative Norms and Their LP Formulations

## \(L_1\) Distance

$$
|x_1-x_0|+|y_1-y_0|.
$$

Introduce variables \(u,v\):

$$
u \ge x_1-x_0,
\qquad
u \ge x_0-x_1,
$$

$$
v \ge y_1-y_0,
\qquad
v \ge y_0-y_1.
$$

Minimize

$$
u+v.
$$

This is still an LP.

---

## \(L_2\) Distance

$$
\sqrt{(x_1-x_0)^2+(y_1-y_0)^2}.
$$

This involves squares and is **not** a linear program.

It becomes a quadratic or second-order cone optimization problem.

---

# A Useful General Pattern

Whenever you see

$$
\min \max\{f_1(x),\ldots,f_k(x)\},
$$

introduce

$$
t
$$

and replace it by

$$
\min t
$$

subject to

$$
f_i(x)\le t
\quad \forall i.
$$

This is known as the **epigraph trick**.

---

# Check Your Understanding

## Conceptual Questions

1. Why is the intersection of half-planes convex?
2. Why does \(|z|\le t\) become two linear inequalities?
3. What shape is the \(L_\infty\) unit ball in \(\mathbb{R}^2\)?
4. What shape is the \(L_1\) unit ball?
5. Why does minimizing

   $$
   \max\{|x_1-x_0|,|y_1-y_0|\}
   $$

   suggest introducing a new variable \(t\)?

## True/False

1. Every convex polygon can be represented as finitely many linear inequalities.
2. The \(L_2\) distance objective produces a linear program.
3. If \(q\in P\), the optimal \(L_\infty\) distance is zero.
4. The feasible region of an LP is always convex.

## Derivation Exercise

Suppose the distance were

$$
\max\Bigl(|x_1-x_0|,\;2|y_1-y_0|\Bigr).
$$

Formulate the corresponding LP.

Hint: enforce

$$
t\ge |x_1-x_0|
$$

and

$$
t\ge 2|y_1-y_0|.
$$

## Challenge Question

Suppose

$$
P=\{(x,y): x+y\le 5,\; x\ge0,\; y\ge0\},
$$

and

$$
q=(4,4).
$$

Without using an LP solver, determine the closest point in \(P\) under the \(L_\infty\) norm and compute the optimal distance.
