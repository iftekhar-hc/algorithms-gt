# Problem 1: Essential Concepts Behind Gradient Descent

The goal of Problem 1 is to understand why **gradient descent can make progress even when the objective function is non-convex**, and how to prove that at least one iterate has a small gradient.

The proof rests on four main ideas:

1. **Smoothness:** the gradient cannot change too quickly.
2. **The descent lemma:** smoothness gives an upper bound on how much the function can increase.
3. **Telescoping sums:** adding the per-iteration improvements bounds the total amount of progress.
4. **Averaging:** if the sum of squared gradient norms is small, at least one gradient norm must be small.

---

## 1. What problem are we solving?

We want to minimize a differentiable function

$$
\min_{x\in\mathbb{R}^d} f(x).
$$

Gradient descent iteratively updates the parameters:

$$
\boxed{x^{t+1}=x^t-\eta\nabla f(x^t)}
$$

where $x^t$ is the current point, $\nabla f(x^t)$ is the gradient, and $\eta>0$ is the step size.

The gradient points in the direction of steepest local increase. Therefore, its negative is the direction of steepest local decrease.

---

# 2. Smoothness

A function is **$\beta$-smooth** if its gradient is $\beta$-Lipschitz:

$$
\boxed{
\|\nabla f(x)-\nabla f(y)\|
\leq \beta\|x-y\|
}
$$

for every pair of points $x,y$.

Intuitively:

- $\|x-y\|$ measures how far apart the points are.
- $\|\nabla f(x)-\nabla f(y)\|$ measures how much the slope changes.
- $\beta$ controls how rapidly the slope can change.

A small $\beta$ means the gradient changes slowly. A large $\beta$ allows the gradient to change more rapidly.

### One-dimensional interpretation

For a twice-differentiable function, a sufficient condition is

$$
|f''(x)|\leq\beta.
$$

The second derivative measures how quickly the gradient changes.

For a twice-differentiable multivariate function, the analogous condition is

$$
\|\nabla^2f(x)\|_{\mathrm{op}}\leq\beta.
$$

**Important:** smoothness does not imply convexity. A function can be smooth and non-convex.

---

# 3. The Descent Lemma

If $f$ is $\beta$-smooth, then for any $x,y$,

$$
\boxed{
f(y)\leq f(x)+\nabla f(x)^\top(y-x)
+\frac{\beta}{2}\|y-x\|^2
}
$$

This is the central inequality in Problem 1.

The terms have the following interpretation:

| Term | Meaning |
|---|---|
| $f(x)$ | Current function value |
| $\nabla f(x)^\top(y-x)$ | Linear/tangent approximation |
| $\frac{\beta}{2}\|y-x\|^2$ | Allowance for curvature |
| $f(y)$ | Actual function value |

The quadratic term is what makes the bound valid even when the function curves away from its tangent plane.

---

# 4. Deriving the Descent Lemma

We derive it from smoothness.

## Step 1: Connect $x$ and $y$

Let

$$
d=y-x
$$

and define

$$
z(s)=x+sd,\qquad 0\leq s\leq1.
$$

At $s=0$, $z(0)=x$. At $s=1$, $z(1)=y$.

Define

$$
\phi(s)=f(x+sd).
$$

By the chain rule,

$$
\phi'(s)=\nabla f(x+sd)^\top d.
$$

## Step 2: Apply the fundamental theorem of calculus

Since

$$
f(y)-f(x)=\phi(1)-\phi(0),
$$

we have

$$
f(y)-f(x)
=
\int_0^1
\nabla f(x+sd)^\top d\,ds.
$$

Add and subtract $\nabla f(x)$:

$$
\begin{aligned}
f(y)-f(x)
&=
\nabla f(x)^\top d\\
&\quad+
\int_0^1
[\nabla f(x+sd)-\nabla f(x)]^\top d\,ds.
\end{aligned}
$$

The first term is exactly the linear approximation.

## Step 3: Bound the changing-gradient term

By Cauchy-Schwarz,

$$
a^\top b\leq\|a\|\|b\|.
$$

Therefore,

$$
\begin{aligned}
&[\nabla f(x+sd)-\nabla f(x)]^\top d\\
&\qquad\leq
\|\nabla f(x+sd)-\nabla f(x)\|\|d\|.
\end{aligned}
$$

Because $f$ is $\beta$-smooth,

$$
\begin{aligned}
\|\nabla f(x+sd)-\nabla f(x)\|
&\leq\beta\|sd\|\\
&=\beta s\|d\|.
\end{aligned}
$$

Thus,

$$
[\nabla f(x+sd)-\nabla f(x)]^\top d
\leq
\beta s\|d\|^2.
$$

## Step 4: Integrate

Therefore,

$$
\begin{aligned}
f(y)-f(x)
&\leq
\nabla f(x)^\top d
+
\int_0^1
\beta s\|d\|^2\,ds\\
&=
\nabla f(x)^\top d
+
\frac{\beta}{2}\|d\|^2.
\end{aligned}
$$

Substituting $d=y-x$ gives

$$
\boxed{
f(y)\leq f(x)+\nabla f(x)^\top(y-x)
+\frac{\beta}{2}\|y-x\|^2
}
$$

which is the descent lemma.

### Key observation

**Convexity was never used.**

The result follows from the fact that the gradient is Lipschitz.

---

# 5. Geometric intuition

The descent lemma says that $f(y)$ lies below the quadratic model

$$
q_x(y)
=
f(x)+\nabla f(x)^\top(y-x)
+\frac{\beta}{2}\|y-x\|^2.
$$

The first two terms are the tangent-plane approximation. The quadratic term accounts for curvature.

For example, let

$$
f(y)=\sin y.
$$

Then

$$
f'(y)=\cos y
$$

and

$$
|f''(y)|=|\!-\sin y|\leq1,
$$

so $\beta=1$ is valid.

At $x=0$,

$$
f(0)=0,\qquad f'(0)=1.
$$

The descent lemma gives

$$
\boxed{
\sin y\leq y+\frac12y^2.
}
$$

At $y=0.5$,

$$
\sin(0.5)\approx0.479
$$

while

$$
0.5+\frac12(0.5)^2=0.625.
$$

So the quadratic expression is indeed an upper bound.

---

# 6. Applying the Descent Lemma to Gradient Descent

Gradient descent is

$$
x^{t+1}=x^t-\eta\nabla f(x^t).
$$

Let

$$
g_t=\nabla f(x^t).
$$

Then

$$
x^{t+1}-x^t=-\eta g_t.
$$

Apply the descent lemma with $x=x^t$ and $y=x^{t+1}$:

$$
\begin{aligned}
f(x^{t+1})
&\leq
f(x^t)
+
g_t^\top(-\eta g_t)
+
\frac{\beta}{2}\|-\eta g_t\|^2\\
&=
f(x^t)
-\eta\|g_t\|^2
+
\frac{\beta\eta^2}{2}\|g_t\|^2.
\end{aligned}
$$

Therefore,

$$
\boxed{
f(x^{t+1})
\leq
f(x^t)
-
\eta\left(1-\frac{\beta\eta}{2}\right)
\|\nabla f(x^t)\|^2
}
$$

This is the general one-step descent inequality.

---

# 7. Why choose $\eta\leq1/\beta$?

If

$$
0<\eta\leq\frac1\beta,
$$

then

$$
\frac{\beta\eta}{2}\leq\frac12,
$$

so

$$
1-\frac{\beta\eta}{2}\geq\frac12.
$$

Thus,

$$
\boxed{
f(x^{t+1})
\leq
f(x^t)
-
\frac{\eta}{2}
\|\nabla f(x^t)\|^2
}
$$

This is the key inequality used by Problem 1.

It says:

> The amount by which the function decreases at iteration $t$ is at least proportional to the squared gradient norm.

The general inequality actually gives strict descent for

$$
0<\eta<\frac{2}{\beta}
$$

when $\nabla f(x^t)\neq0$. The homework uses the more conservative $\eta\leq1/\beta$ because it gives the clean factor $1/2$.

---

# 8. Why step size matters

Consider the simple quadratic

$$
f(x)=\frac{\beta}{2}x^2.
$$

Its gradient is

$$
\nabla f(x)=\beta x.
$$

Gradient descent becomes

$$
x^{t+1}
=
(1-\eta\beta)x^t.
$$

Consider three cases:

### Case 1: $\eta=1/\beta$

$$
x^{t+1}=0.
$$

The algorithm reaches the minimum in one step.

### Case 2: $\eta=2/\beta$

$$
x^{t+1}=-x^t.
$$

The sign flips but the magnitude stays the same, so the function value does not decrease.

### Case 3: $\eta>2/\beta$

The magnitude of $x^t$ grows, so the function value grows.

This illustrates why a sufficiently small step size is necessary for a general descent guarantee.

---

# 9. Telescoping Sums

From

$$
f(x^{t+1})
\leq
f(x^t)
-
\frac{\eta}{2}
\|\nabla f(x^t)\|^2,
$$

we get

$$
\frac{\eta}{2}
\|\nabla f(x^t)\|^2
\leq
f(x^t)-f(x^{t+1}).
$$

Sum from $t=0$ to $T-1$:

$$
\frac{\eta}{2}
\sum_{t=0}^{T-1}
\|\nabla f(x^t)\|^2
\leq
\sum_{t=0}^{T-1}
[f(x^t)-f(x^{t+1})].
$$

The right-hand side is

$$
\begin{aligned}
&[f(x^0)-f(x^1)]\\
&+[f(x^1)-f(x^2)]\\
&+\cdots\\
&+[f(x^{T-1})-f(x^T)].
\end{aligned}
$$

All intermediate terms cancel:

$$
\boxed{
\sum_{t=0}^{T-1}
[f(x^t)-f(x^{t+1})]
=
f(x^0)-f(x^T)
}
$$

This is called a **telescoping sum**.

If $x^*$ is a global minimizer, then

$$
f(x^T)\geq f(x^*).
$$

Therefore,

$$
\begin{aligned}
\frac{\eta}{2}
\sum_{t=0}^{T-1}
\|\nabla f(x^t)\|^2
&\leq
f(x^0)-f(x^T)\\
&\leq
f(x^0)-f(x^*).
\end{aligned}
$$

Define

$$
\Delta=f(x^0)-f(x^*).
$$

Then

$$
\boxed{
\sum_{t=0}^{T-1}
\|\nabla f(x^t)\|^2
\leq
\frac{2\Delta}{\eta}
}
$$

---

# 10. Averaging: finding one small gradient

There are $T$ nonnegative numbers

$$
\|\nabla f(x^0)\|^2,\ldots,
\|\nabla f(x^{T-1})\|^2.
$$

The minimum of a collection of numbers is no greater than their average:

$$
\min_{0\leq t<T}
\|\nabla f(x^t)\|^2
\leq
\frac1T
\sum_{t=0}^{T-1}
\|\nabla f(x^t)\|^2.
$$

Using the previous bound,

$$
\begin{aligned}
\min_{0\leq t<T}
\|\nabla f(x^t)\|^2
&\leq
\frac{2\Delta}{\eta T}.
\end{aligned}
$$

Taking square roots:

$$
\boxed{
\min_{0\leq t<T}
\|\nabla f(x^t)\|
\leq
\sqrt{\frac{2\Delta}{\eta T}}
}
$$

where

$$
\Delta=f(x^0)-f(x^*).
$$

The bound decreases as

$$
O\left(\frac1{\sqrt{T}}\right).
$$

---

# 11. What does a small gradient mean?

A point satisfying

$$
\|\nabla f(x)\|\leq\varepsilon
$$

is called an **$\varepsilon$-stationary point**.

A small gradient means the function has a small first-order slope at that point.

However, in a non-convex problem, a stationary point does not necessarily mean a global minimum.

For example,

$$
f(x)=-x^2
$$

has

$$
f'(0)=0,
$$

but $x=0$ is a maximum.

Thus, Problem 1 proves the existence of an approximately stationary point, not necessarily an approximately globally optimal point.

---

# 12. How many iterations are needed?

Suppose we want

$$
\|\nabla f(x^t)\|\leq\varepsilon
$$

for at least one iterate.

It is sufficient that

$$
\sqrt{\frac{2\Delta}{\eta T}}\leq\varepsilon.
$$

Squaring:

$$
\frac{2\Delta}{\eta T}\leq\varepsilon^2.
$$

Therefore,

$$
\boxed{
T\geq
\frac{2\Delta}{\eta\varepsilon^2}
}
$$

For $\eta=1/\beta$,

$$
\boxed{
T\geq
\frac{2\beta\Delta}{\varepsilon^2}
}
$$

Thus, the proof gives an iteration complexity of

$$
O\left(\frac{\beta\Delta}{\varepsilon^2}\right).
$$

---

# 13. The Complete Logical Chain

The entire proof can be remembered as:

$$
\boxed{
\text{Smoothness}
\Longrightarrow
\text{Descent Lemma}
\Longrightarrow
\text{Per-step decrease}
\Longrightarrow
\text{Telescoping}
\Longrightarrow
\text{Small gradient}
}
$$

Each step answers a different question:

| Question | Tool |
|---|---|
| How quickly can the gradient change? | Smoothness |
| How much can $f$ change between two points? | Descent lemma |
| Does gradient descent decrease $f$? | Substitute the update |
| What happens after many iterations? | Telescoping sum |
| Must one iterate have a small gradient? | Minimum $\leq$ average |

---

# 14. Common Mistakes

## Mistake 1: Confusing smoothness with convexity

Smoothness says

$$
\|\nabla f(x)-\nabla f(y)\|
\leq
\beta\|x-y\|.
$$

Convexity says

$$
f(y)\geq
f(x)+\nabla f(x)^\top(y-x).
$$

They are different properties.

A function can be smooth but non-convex.

## Mistake 2: Forgetting the step-size condition

The clean bound

$$
f(x^{t+1})
\leq
f(x^t)
-\frac{\eta}{2}
\|\nabla f(x^t)\|^2
$$

uses

$$
\eta\leq\frac1\beta.
$$

## Mistake 3: Forgetting the quadratic term

The descent lemma is **not**

$$
f(y)\leq
f(x)+\nabla f(x)^\top(y-x).
$$

The correct smoothness-based upper bound is

$$
f(y)\leq
f(x)+\nabla f(x)^\top(y-x)
+\frac{\beta}{2}\|y-x\|^2.
$$

## Mistake 4: Claiming the final iterate has the small gradient

The proof establishes

$$
\min_{0\leq t<T}
\|\nabla f(x^t)\|
\leq
\sqrt{\frac{2\Delta}{\eta T}},
$$

not necessarily

$$
\|\nabla f(x^T)\|
\leq
\sqrt{\frac{2\Delta}{\eta T}}.
$$

The guarantee is that **at least one** of the first $T$ iterates has a small gradient.

---

# 15. Exam-Ready Derivation

If you need to reproduce the proof quickly, remember this sequence.

Start with the descent lemma:

$$
f(y)\leq
f(x)+\nabla f(x)^\top(y-x)
+\frac{\beta}{2}\|y-x\|^2.
$$

Plug in

$$
y=x^{t+1}
=
x^t-\eta\nabla f(x^t).
$$

Then

$$
\begin{aligned}
f(x^{t+1})
&\leq
f(x^t)
-\eta\|\nabla f(x^t)\|^2
+\frac{\beta\eta^2}{2}
\|\nabla f(x^t)\|^2\\
&\leq
f(x^t)
-\frac{\eta}{2}
\|\nabla f(x^t)\|^2.
\end{aligned}
$$

Rearrange:

$$
\frac{\eta}{2}
\|\nabla f(x^t)\|^2
\leq
f(x^t)-f(x^{t+1}).
$$

Sum:

$$
\frac{\eta}{2}
\sum_{t=0}^{T-1}
\|\nabla f(x^t)\|^2
\leq
f(x^0)-f(x^T)
\leq
f(x^0)-f(x^*).
$$

Therefore,

$$
\sum_{t=0}^{T-1}
\|\nabla f(x^t)\|^2
\leq
\frac{2[f(x^0)-f(x^*)]}{\eta}.
$$

Average:

$$
\boxed{
\min_{0\leq t<T}
\|\nabla f(x^t)\|
\leq
\sqrt{
\frac{2[f(x^0)-f(x^*)]}
{\eta T}
}
}
$$

That is the entire proof in compact form.

---

# 16. Self-Test

### Question 1

Does the descent lemma require convexity?

**Answer:** No. It follows from the Lipschitz-gradient/smoothness assumption.

### Question 2

Why does the quadratic term contain $\beta/2$?

**Answer:** Smoothness produces a term proportional to $\beta s\|d\|^2$, and

$$
\int_0^1s\,ds=\frac12.
$$

### Question 3

Why does the proof use the squared gradient norm?

**Answer:** The gradient-descent displacement is

$$
-\eta\nabla f(x^t),
$$

so the linear term becomes

$$
\nabla f(x^t)^\top
(-\eta\nabla f(x^t))
=
-\eta\|\nabla f(x^t)\|^2.
$$

### Question 4

Why can we telescope the function values?

**Answer:** Each iteration gives a difference

$$
f(x^t)-f(x^{t+1}),
$$

so adjacent terms cancel when summed.

### Question 5

What does the final result guarantee?

**Answer:** At least one iterate among $x^0,\ldots,x^{T-1}$ has gradient norm no larger than

$$
\sqrt{
\frac{2[f(x^0)-f(x^*)]}
{\eta T}
}.
$$

It does not guarantee that the final iterate is globally optimal.

---

# 17. One-Sentence Summary

> **Smoothness gives the descent lemma; the descent lemma gives per-step decrease; summing those decreases telescopes; and averaging converts the total bound into the existence of an iterate with a small gradient.**
