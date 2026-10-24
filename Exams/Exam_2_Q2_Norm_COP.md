# Why \(L_1\), \(L_2\), and \(L_\infty\) Norms Are Not Linear, and How to Linearize Them for Linear Programming

## Why norms are not linear

A function \(f\) is **linear** if for all vectors \(x,y\) and scalars \(\alpha,\beta\),

$$
f(\alpha x + \beta y)
=
\alpha f(x)+\beta f(y).
$$

Equivalently, a linear function must satisfy:

1. **Additivity**

$$
f(x+y)=f(x)+f(y)
$$

2. **Homogeneity**

$$
f(\alpha x)=\alpha f(x)
$$

for all real \(\alpha\).

---

## \(L_1\) norm

$$
\|x\|_1=\sum_i |x_i|.
$$

Take

$$
x=(1), \qquad y=(-1).
$$

Then

$$
\|x+y\|_1 = \|0\|_1 =0,
$$

but

$$
\|x\|_1+\|y\|_1 =1+1=2.
$$

Therefore

$$
\|x+y\|_1 \neq \|x\|_1+\|y\|_1.
$$

So \(L_1\) is not linear.

The culprit is the absolute value.

---

## \(L_2\) norm

$$
\|x\|_2=\sqrt{\sum_i x_i^2}.
$$

Take

$$
x=(1,0),\qquad y=(0,1).
$$

Then

$$
\|x+y\|_2
=
\sqrt{2},
$$

while

$$
\|x\|_2+\|y\|_2
=
1+1=2.
$$

Not equal.

Hence \(L_2\) is not linear.

The square root and squares make it nonlinear.

---

## \(L_\infty\) norm

$$
\|x\|_\infty=\max_i |x_i|.
$$

Take

$$
x=(1,0), \qquad y=(0,1).
$$

Then

$$
\|x+y\|_\infty
=
1,
$$

but

$$
\|x\|_\infty+\|y\|_\infty
=
2.
$$

Again not linear.

The max operation is nonlinear.

---

# Why LP can still handle \(L_1\) and \(L_\infty\)

Although the norm functions themselves are nonlinear, they are **piecewise-linear convex functions**.

A standard LP trick is to introduce auxiliary variables.

---

# Linearizing \(L_1\)

Suppose we want

$$
\min \|x\|_1.
$$

Introduce variables

$$
t_i \ge 0
$$

and impose

$$
t_i \ge x_i,
$$

$$
t_i \ge -x_i.
$$

Then

$$
t_i \ge |x_i|.
$$

Now minimize

$$
\sum_i t_i.
$$

At optimum,

$$
t_i = |x_i|,
$$

because making \(t_i\) larger only worsens the objective.

Therefore

$$
\min \|x\|_1
$$

is equivalent to

$$
\begin{aligned}
\min \quad & \sum_i t_i \\
\text{s.t.}\quad
& t_i \ge x_i,\\
& t_i \ge -x_i,\\
& t_i \ge 0.
\end{aligned}
$$

This is a pure LP.

## Example

Minimize

$$
|x_1|+|x_2|
$$

subject to

$$
x_1+x_2=1.
$$

LP form:

$$
\begin{aligned}
\min\quad & t_1+t_2\\
\text{s.t.}\quad
& x_1+x_2=1,\\
& t_1\ge x_1,\\
& t_1\ge -x_1,\\
& t_2\ge x_2,\\
& t_2\ge -x_2.
\end{aligned}
$$

---

# Linearizing \(L_\infty\)

Suppose we want

$$
\min \|x\|_\infty.
$$

Introduce a single variable \(t\).

Require

$$
t \ge |x_i|
\qquad \forall i.
$$

Replace absolute values by

$$
t \ge x_i,
$$

$$
t \ge -x_i.
$$

Then

$$
t \ge \max_i |x_i|
=
\|x\|_\infty.
$$

Minimize \(t\):

$$
\begin{aligned}
\min\quad & t\\
\text{s.t.}\quad
& t \ge x_i,\quad \forall i,\\
& t \ge -x_i,\quad \forall i.
\end{aligned}
$$

At optimality,

$$
t=\|x\|_\infty.
$$

Thus \(L_\infty\) minimization is also an LP.

## Example

Minimize

$$
\max(|x_1|,|x_2|)
$$

subject to

$$
x_1+x_2=1.
$$

LP form:

$$
\begin{aligned}
\min\quad & t\\
\text{s.t.}\quad
& x_1+x_2=1,\\
& t\ge x_1,\\
& t\ge -x_1,\\
& t\ge x_2,\\
& t\ge -x_2.
\end{aligned}
$$

---

# What about \(L_2\)?

$$
\|x\|_2 = \sqrt{\sum_i x_i^2}
$$

cannot be represented exactly with linear constraints.

The quadratic terms \(x_i^2\) are fundamentally nonlinear.

## Exact formulation

Use a **Second-Order Cone Program (SOCP)**:

$$
\min t
$$

subject to

$$
\sqrt{\sum_i x_i^2}\le t.
$$

Equivalently,

$$
\|x\|_2 \le t.
$$

This is convex but not linear.

## Approximation by LP

Approximate the Euclidean ball with a polygon/polytope.

For example in 2D:

$$
x\cos\theta_k + y\sin\theta_k \le t,
\qquad
k=1,\dots,m.
$$

As \(m\) increases, the polygon approaches the circle.

This converts the problem into an LP approximation.

---

# Summary

| Norm | Linear? | LP Formulation? | Method |
|------|------|------|------|
| $\|x\|_1=\sum |x_i|$ | No | Yes | Introduce $t_i\ge \pm x_i$ |
| $\|x\|_\infty=\max |x_i|$ | No | Yes | Introduce $t\ge \pm x_i$ |
| $\|x\|_2=\sqrt{\sum x_i^2}$ | No | No (exactly) | Use SOCP |
| $\|x\|_2$ approximation | No | Yes (approximately) | Polyhedral approximation |

## Rule of Thumb

- **Absolute values** and **max/min** can usually be linearized exactly using auxiliary variables.
- **Squares, products, and square roots** generally cannot be represented exactly in LPs and require quadratic, conic, or nonlinear optimization methods.
