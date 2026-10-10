# Gradient Descent for Strongly Convex Functions

The central idea is to combine **strong convexity** with the squared-distance progress made by one gradient-descent step. A carefully weighted potential function then makes all distance terms telescope, leaving only a harmonic sum, which contributes the factor $1+\log T$.

---

## 1. Setup and notation

Let

$$
g_t=\nabla f(x_t),
\qquad
D_t=\lVert x_t-x^*\rVert_2^2.
$$

Gradient descent performs

$$
x_{t+1}=x_t-\eta_t g_t,
\qquad
\eta_t=\frac{1}{\alpha(t+1)}.
$$

We assume that along the iterates,

$$
\lVert g_t\rVert_2\le G.
$$

Our goal is to prove

$$
f\left(\frac1T\sum_{t=1}^T x_t\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
$$

The proof has three main steps:

1. Use strong convexity to bound $f(x_t)-f(x^*)$.
2. Rewrite the inner product using the gradient-descent update.
3. Sum the resulting inequalities and use convexity on the averaged iterate.

---

## 2. Background: what strong convexity gives us

Ordinary convexity says

$$
f(y)\ge f(x)+\langle \nabla f(x),y-x\rangle.
$$

Strong convexity strengthens this by adding a positive quadratic term:

$$
f(y)
\ge
f(x)+\langle \nabla f(x),y-x\rangle
+\frac{\alpha}{2}\lVert y-x\rVert_2^2.
$$

Geometrically, the tangent-plane approximation must lie below the function by at least a quadratic bowl.

```text
Function value
   ^
   |                         f(x)
   |                    _.-'
   |                _.-'
   |            _.-'
   |        _.-'      quadratic separation
   |    _.-'         /
   |_.-'------------/---------- tangent line
   +----------------------------------------> x
```

A larger $\alpha$ means greater curvature and, consequently, more information about how far a point is from the minimizer.

---

## 3. The key strong-convexity inequality

Apply strong convexity with

$$
x=x_t,
\qquad
y=x^*.
$$

Then

$$
f(x^*)
\ge
f(x_t)
+\langle g_t,x^*-x_t\rangle
+\frac{\alpha}{2}\lVert x^*-x_t\rVert_2^2.
$$

Rearranging gives

$$
\boxed{
f(x_t)-f(x^*)
\le
\langle g_t,x_t-x^*\rangle
-\frac{\alpha}{2}D_t
}
\tag{1}
$$

The first term is the usual convexity term. The second term,

$$
-\frac{\alpha}{2}D_t,
$$

is the improvement from strong convexity. It is precisely what eventually improves the convergence rate from order $1/\sqrt T$ to order $1/T$, up to a logarithmic factor.

---

## 4. Analyze one gradient-descent step

From the update

$$
x_{t+1}=x_t-\eta_tg_t,
$$

we have

$$
x_{t+1}-x^*
=
x_t-x^*-\eta_tg_t.
$$

Taking squared norms,

$$
\begin{aligned}
D_{t+1}
&=
\lVert x_t-x^*-\eta_tg_t\rVert_2^2\\
&=
D_t
-2\eta_t\langle g_t,x_t-x^*\rangle
+\eta_t^2\lVert g_t\rVert_2^2.
\end{aligned}
$$

Solve this expression for the inner product:

$$
2\eta_t\langle g_t,x_t-x^*\rangle
=
D_t-D_{t+1}
+\eta_t^2\lVert g_t\rVert_2^2.
$$

Therefore,

$$
\boxed{
\langle g_t,x_t-x^*\rangle
=
\frac{D_t-D_{t+1}}{2\eta_t}
+\frac{\eta_t}{2}\lVert g_t\rVert_2^2
}
\tag{2}
$$

Using $\lVert g_t\rVert_2\le G$,

$$
\langle g_t,x_t-x^*\rangle
\le
\frac{D_t-D_{t+1}}{2\eta_t}
+\frac{\eta_tG^2}{2}.
\tag{3}
$$

---

## 5. Combine the two inequalities

Insert (3) into the strong-convexity bound (1):

$$
f(x_t)-f(x^*)
\le
\frac{D_t-D_{t+1}}{2\eta_t}
+\frac{\eta_tG^2}{2}
-\frac{\alpha}{2}D_t.
$$

Now substitute

$$
\eta_t=\frac{1}{\alpha(t+1)},
\qquad
\frac{1}{\eta_t}=\alpha(t+1).
$$

This gives

$$
\begin{aligned}
f(x_t)-f(x^*)
&\le
\frac{\alpha(t+1)}{2}(D_t-D_{t+1})
-\frac{\alpha}{2}D_t
+\frac{G^2}{2\alpha(t+1)}\\[2mm]
&=
\left(
\frac{\alpha(t+1)}{2}
-\frac{\alpha}{2}
\right)D_t
-\frac{\alpha(t+1)}{2}D_{t+1}
+\frac{G^2}{2\alpha(t+1)}\\[2mm]
&=
\frac{\alpha t}{2}D_t
-\frac{\alpha(t+1)}{2}D_{t+1}
+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
$$

Thus,

$$
\boxed{
f(x_t)-f(x^*)
\le
\frac{\alpha t}{2}D_t
-\frac{\alpha(t+1)}{2}D_{t+1}
+\frac{G^2}{2\alpha(t+1)}
}
\tag{4}
$$

---

## 6. Introduce the potential function

The suggested potential is

$$
\Phi(t)
=
\frac{\alpha t}{2}\lVert x_t-x^*\rVert_2^2
=
\frac{\alpha t}{2}D_t.
$$

Notice that

$$
\Phi(t+1)
=
\frac{\alpha(t+1)}{2}D_{t+1}.
$$

Therefore, inequality (4) becomes

$$
\boxed{
f(x_t)-f(x^*)
\le
\Phi(t)-\Phi(t+1)
+\frac{G^2}{2\alpha(t+1)}
}
\tag{5}
$$

This is the key inequality.

### Why this potential works

The coefficient $t$ is not arbitrary. It was chosen so that

$$
\frac{1}{\eta_t}-\alpha
=
\alpha(t+1)-\alpha
=
\alpha t.
$$

In other words, the strong-convexity correction transforms the coefficient $\alpha(t+1)$ into $\alpha t$, exactly matching the potential at the preceding iteration.

```text
Strong-convexity subtraction:

 alpha(t+1)D_t/2  -  alpha D_t/2
                 |
                 v
             alpha t D_t/2
                 |
                 v
               Phi(t)
```

---

## 7. Sum over the iterations

There is a small indexing convention hidden in the problem. With

$$
\eta_t=\frac{1}{\alpha(t+1)},
$$

the clean telescoping argument starts at $t=0$. Summing (5) for

$$
t=0,1,\ldots,T-1
$$

gives

$$
\begin{aligned}
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^*)\bigr)
&\le
\sum_{t=0}^{T-1}
\bigl(\Phi(t)-\Phi(t+1)\bigr)
+
\frac{G^2}{2\alpha}
\sum_{t=0}^{T-1}\frac{1}{t+1}.
\end{aligned}
$$

The potential terms telescope:

$$
\sum_{t=0}^{T-1}
\bigl(\Phi(t)-\Phi(t+1)\bigr)
=
\Phi(0)-\Phi(T).
$$

But

$$
\Phi(0)
=
\frac{0\cdot\alpha}{2}D_0
=
0,
$$

and $\Phi(T)\ge0$. Hence

$$
\Phi(0)-\Phi(T)\le0.
$$

It follows that

$$
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2}{2\alpha}
\sum_{t=0}^{T-1}\frac{1}{t+1}.
$$

Changing the index $s=t+1$,

$$
\sum_{t=0}^{T-1}\frac1{t+1}
=
\sum_{s=1}^T\frac1s.
$$

Using the harmonic-sum bound

$$
\sum_{s=1}^T\frac1s\le1+\log T,
$$

we obtain

$$
\boxed{
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2(1+\log T)}{2\alpha}
}
\tag{6}
$$

Dividing by $T$,

$$
\boxed{
\frac1T
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2(1+\log T)}{2\alpha T}
}
\tag{7}
$$

---

## 8. Convert average function value to function value at the average point

Define the averaged iterate

$$
\bar x_T
=
\frac1T\sum_{t=0}^{T-1}x_t.
$$

Because strong convexity implies ordinary convexity, Jensen's inequality gives

$$
f(\bar x_T)
=
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

Subtracting $f(x^*)$,

$$
\begin{aligned}
f(\bar x_T)-f(x^*)
&\le
\frac1T
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)\\
&\le
\frac{G^2(1+\log T)}{2\alpha T}.
\end{aligned}
$$

Therefore,

$$
\boxed{
f(\bar x_T)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}
}
$$

Relabeling the $T$ iterates $x_0,\ldots,x_{T-1}$ as $x_1,\ldots,x_T$, this is exactly

$$
\boxed{
f\left(\frac{\sum_{t=1}^{T}x_t}{T}\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
}
$$

---

## Indexing note

The stated step size and potential are naturally compatible with zero-based indexing:

$$
t=0,\ldots,T-1,
\qquad
\eta_t=\frac1{\alpha(t+1)}.
$$

If one insists on starting the update index at $t=1$, the equivalent step-size notation is usually written as

$$
\eta_t=\frac1{\alpha t}.
$$

This is only a relabeling issue. The mathematical argument and final bound are unchanged.

---

## 9. Proof as a compact chain

The entire proof can be summarized as follows:

$$
\begin{aligned}
f(x_t)-f(x^*)
&\le
\langle g_t,x_t-x^*\rangle
-\frac{\alpha}{2}D_t\\
&=
\frac{D_t-D_{t+1}}{2\eta_t}
+\frac{\eta_t}{2}\lVert g_t\rVert^2
-\frac{\alpha}{2}D_t\\
&\le
\frac{\alpha t}{2}D_t
-\frac{\alpha(t+1)}{2}D_{t+1}
+\frac{G^2}{2\alpha(t+1)}\\
&=
\Phi(t)-\Phi(t+1)
+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
$$

Summing for $t=0,\ldots,T-1$,

$$
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2}{2\alpha}
\sum_{t=0}^{T-1}\frac1{t+1}
\le
\frac{G^2(1+\log T)}{2\alpha}.
$$

Finally, Jensen's inequality yields the result for the averaged iterate.

---

## 10. Numerical example of the bound

Suppose

$$
\alpha=2,
\qquad
G=4,
\qquad
T=100.
$$

Then

$$
\frac{G^2(1+\log T)}{2\alpha T}
=
\frac{16(1+\log 100)}{2\cdot2\cdot100}.
$$

Since

$$
\log 100\approx4.605,
$$

the guarantee is

$$
f(\bar x_{100})-f(x^*)
\le
\frac{16(5.605)}{400}
\approx0.2242.
$$

For several values of $T$:

| $T$ | Upper bound |
|---:|---:|
| $10$ | $1.3210$ |
| $100$ | $0.2242$ |
| $1{,}000$ | $0.0316$ |
| $10{,}000$ | $0.0041$ |

The bound behaves like

$$
\frac{\log T}{T},
$$

so multiplying $T$ by $10$ reduces the bound by approximately a factor close to $10$, apart from the slowly increasing logarithmic term.

---

## 11. Visualization of the rate

Ignoring constants, compare

$$
\text{general convex: }\frac1{\sqrt T},
\qquad
\text{strongly convex: }\frac{1+\log T}{T}.
$$

| $T$ | $1/\sqrt T$ | $(1+\log T)/T$ |
|---:|---:|---:|
| $10$ | $0.3162$ | $0.3303$ |
| $100$ | $0.1000$ | $0.0561$ |
| $1{,}000$ | $0.0316$ | $0.0079$ |
| $10{,}000$ | $0.0100$ | $0.0010$ |

Conceptually:

```text
Error
  ^
  |\
  | \
  |  \       1/sqrt(T)
  |   \________________
  |
  |\
  | \__
  |    \____           (1 + log T)/T
  |         \________
  +-----------------------------> T
```

For sufficiently large $T$, the strongly convex guarantee decreases much faster.

Strictly speaking, the derived rate is

$$
O\left(\frac{\log T}{T}\right),
$$

often described informally as $1/T$-type dependence. Other step-size schedules or weighted averaging schemes can remove the logarithmic factor in related strongly convex optimization analyses.

---

## 12. Geometric intuition

For a merely convex function, a small gradient does not necessarily tell us that we are close to the optimum. The function may be almost flat over a large region.

Strong convexity prevents this behavior. In fact, since $\nabla f(x^*)=0$, strong monotonicity of the gradient gives

$$
\langle \nabla f(x)-\nabla f(x^*),x-x^*\rangle
\ge
\alpha\lVert x-x^*\rVert^2.
$$

Thus,

$$
\langle \nabla f(x),x-x^*\rangle
\ge
\alpha\lVert x-x^*\rVert^2.
$$

By Cauchy-Schwarz,

$$
\lVert \nabla f(x)\rVert\lVert x-x^*\rVert
\ge
\alpha\lVert x-x^*\rVert^2.
$$

When $x\ne x^*$,

$$
\lVert x-x^*\rVert
\le
\frac{\lVert\nabla f(x)\rVert}{\alpha}.
$$

Therefore, bounded gradients along the iterates imply that the iterates remain within distance $G/\alpha$ of the minimizer.

---

## 13. Important technical subtlety

A differentiable $\alpha$-strongly convex function on all of $\mathbb R^n$ cannot generally have a globally bounded gradient.

Indeed,

$$
\lVert\nabla f(x)\rVert
\ge
\alpha\lVert x-x^*\rVert,
$$

so the gradient must grow as $\lVert x\rVert\to\infty$.

Consequently, the assumption

$$
\lVert\nabla f(x)\rVert\le G
$$

is normally interpreted in one of these ways:

1. the optimization domain is bounded;
2. projected gradient descent is being used;
3. the gradient bound is required only along the generated iterates;
4. $G$ bounds the relevant subgradients on the feasible region.

The proof above only needs

$$
\lVert\nabla f(x_t)\rVert\le G
$$

at the iterates being analyzed.

---

## 14. Pseudocode

```text
Input:
    strongly convex function f
    strong-convexity parameter alpha
    initial point x_0
    number of iterations T

sum_x = 0

for t = 0, 1, ..., T - 1:
    sum_x = sum_x + x_t

    g_t = gradient of f at x_t
    eta_t = 1 / (alpha * (t + 1))

    x_(t+1) = x_t - eta_t * g_t

return sum_x / T
```

If the feasible set is a closed convex set $K$, use projected gradient descent:

```text
x_(t+1) = projection_K(x_t - eta_t * g_t)
```

---

## 15. What to remember

The proof uses four ingredients:

1. **Strong convexity**

   $$
   f(x_t)-f(x^*)
   \le
   \langle g_t,x_t-x^*\rangle
   -\frac{\alpha}{2}\lVert x_t-x^*\rVert^2.
   $$

2. **Distance expansion**

   $$
   \langle g_t,x_t-x^*\rangle
   =
   \frac{D_t-D_{t+1}}{2\eta_t}
   +\frac{\eta_t}{2}\lVert g_t\rVert^2.
   $$

3. **Weighted potential**

   $$
   \Phi(t)
   =
   \frac{\alpha t}{2}D_t.
   $$

4. **Averaging and convexity**

   $$
   f\left(\frac1T\sum_t x_t\right)
   \le
   \frac1T\sum_t f(x_t).
   $$

The specially chosen step size makes the distance terms telescope:

$$
\boxed{
\frac1{\eta_t}-\alpha
=
\alpha t.
}
$$

That identity is the algebraic heart of the proof.
