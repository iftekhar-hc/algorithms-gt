# Non-Convex Gradient Descent: Step-by-Step Solution

The proof follows one chain:

$$
\boxed{
\text{smoothness}
\;\Longrightarrow\;
\text{decrease proportional to }\|\nabla f(x_t)\|^2
\;\Longrightarrow\;
\text{bounded sum of squared gradients}
\;\Longrightarrow\;
\text{at least one small gradient}.
}
$$

The key idea is that every iteration with a large gradient must substantially decrease $f$. Because $f$ cannot decrease below its global minimum, large gradients cannot persist indefinitely. This argument does not require convexity.

There is also an indexing detail: $T$ updates naturally give a sum over $k=0,\ldots,T-1$. The problem sums through $T$; we prove that version too and explain the distinction.

## 1. Background: Assumptions and Guarantees

### Gradient descent

We use the update

$$
x_{t+1}=x_t-\eta\nabla f(x_t),
$$

with a fixed step size

$$
0<\eta\le \frac1\beta.
$$

Assume $f:\mathbb R^n\to\mathbb R$ is differentiable and has a global minimizer $x^*$. Define the initial objective gap

$$
\Delta_0:=f(x_0)-f(x^*)\ge 0.
$$

The algorithm does not need to know $x^*$ or $f(x^*)$; they appear only in the analysis.

### What does beta-smooth mean?

A differentiable function is $\beta$-smooth if its gradient is Lipschitz:

$$
\|\nabla f(y)-\nabla f(x)\|
\le \beta\|y-x\|.
$$

This implies the quadratic upper bound

$$
\boxed{
f(y)\le
f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\beta}{2}\|y-x\|^2.
}
$$

This is the smoothness inequality, also called the descent lemma. It remains valid for nonconvex functions: smoothness limits how rapidly the gradient changes, rather than requiring the function to curve upward everywhere.

### What changes without convexity?

Our target is stationarity: finding a point with a small gradient norm, rather than necessarily a small objective gap.

A necessary correction to the problem's parenthetical note: a small gradient does not, by itself, guarantee that the point is geometrically close to a local minimum or saddle point. Even a local maximum can have gradient zero. The conclusion is an approximately first-order stationary point—not necessarily an approximate minimum.

## 2. Part 1: Prove the One-Step Decrease

We want to show

$$
f(x_{t+1})
\le f(x_t)-\frac{\eta}{2}\|\nabla f(x_t)\|^2.
$$

### Step 1: Apply smoothness to consecutive iterates

Set $x=x_t$ and $y=x_{t+1}$:

$$
f(x_{t+1})
\le
f(x_t)
+
\langle\nabla f(x_t),x_{t+1}-x_t\rangle
+
\frac{\beta}{2}\|x_{t+1}-x_t\|^2.
$$

### Step 2: Substitute the gradient-descent update

Since

$$
x_{t+1}-x_t=-\eta\nabla f(x_t),
$$

the inner-product term is

$$
\langle\nabla f(x_t),-\eta\nabla f(x_t)\rangle
=
-\eta\|\nabla f(x_t)\|^2,
$$

and the squared-step term is

$$
\|-\eta\nabla f(x_t)\|^2
=
\eta^2\|\nabla f(x_t)\|^2.
$$

Therefore,

$$
\begin{aligned}
f(x_{t+1})
&\le
f(x_t)
-\eta\|\nabla f(x_t)\|^2
+\frac{\beta\eta^2}{2}\|\nabla f(x_t)\|^2\\
&=
f(x_t)
-\eta\left(1-\frac{\beta\eta}{2}\right)
\|\nabla f(x_t)\|^2.
\end{aligned}
$$

### Step 3: Use the step-size restriction

Because $\beta\eta\le 1$,

$$
1-\frac{\beta\eta}{2}\ge \frac12.
$$

Consequently,

$$
\boxed{
f(x_{t+1})
\le
f(x_t)-\frac{\eta}{2}\|\nabla f(x_t)\|^2.
}
$$

### Visual interpretation

Think of each update as spending part of the remaining objective gap:

```text
f(x₀)   ●
        │  decrease ≥ (η/2)‖∇f(x₀)‖²
f(x₁)   ●
        │  decrease ≥ (η/2)‖∇f(x₁)‖²
f(x₂)   ●
        │
        ⋮
f(x*)   ───────────────────────── lower bound
```

A large gradient forces a large downward step in function value. The total available decrease is at most $\Delta_0$.

## 3. Part 2: Sum the Decreases and Telescope

Rearranging Part 1 gives

$$
\frac{\eta}{2}\|\nabla f(x_k)\|^2
\le f(x_k)-f(x_{k+1}).
$$

### Step 1: Sum from k = 0 through T

$$
\frac{\eta}{2}
\sum_{k=0}^{T}\|\nabla f(x_k)\|^2
\le
\sum_{k=0}^{T}\bigl(f(x_k)-f(x_{k+1})\bigr).
$$

### Step 2: Telescope

The right side expands as

$$
\begin{aligned}
&[f(x_0)-f(x_1)]\\
&\quad+[f(x_1)-f(x_2)]\\
&\quad+\cdots\\
&\quad+[f(x_T)-f(x_{T+1})].
\end{aligned}
$$

Every intermediate term cancels, leaving

$$
\frac{\eta}{2}
\sum_{k=0}^{T}\|\nabla f(x_k)\|^2
\le
f(x_0)-f(x_{T+1}).
$$

### Step 3: Use the global lower bound

Since $x^*$ is a global minimizer,

$$
f(x_{T+1})\ge f(x^*).
$$

Thus,

$$
f(x_0)-f(x_{T+1})
\le f(x_0)-f(x^*)=\Delta_0.
$$

Multiplying by $2/\eta$ gives

$$
\boxed{
\sum_{k=0}^{T}\|\nabla f(x_k)\|^2
\le
\frac{2}{\eta}
\bigl(f(x_0)-f(x^*)\bigr).
}
$$

### The indexing detail

The displayed proof uses $x_{T+1}$. If only $T$ updates have actually been performed, this can be a hypothetical next point:

$$
x_{T+1}:=x_T-\eta\nabla f(x_T).
$$

There is no need to execute that update; its existence and Part 1 justify the bound.

Alternatively, summing only the $T$ updates actually performed gives

$$
\boxed{
\sum_{k=0}^{T-1}\|\nabla f(x_k)\|^2
\le
\frac{2\Delta_0}{\eta}.
}
$$

This latter form is the cleanest starting point for an “after $T$ iterations” statement.

## 4. Part 3: The Minimum Is at Most the Average

Let

$$
m_T:=\min_{0\le k\le T}\|\nabla f(x_k)\|.
$$

Every term in the sum satisfies

$$
\|\nabla f(x_k)\|^2\ge m_T^2.
$$

Because there are $T+1$ terms,

$$
(T+1)m_T^2
\le
\sum_{k=0}^{T}\|\nabla f(x_k)\|^2.
$$

Using Part 2,

$$
(T+1)m_T^2\le \frac{2\Delta_0}{\eta}.
$$

Therefore,

$$
\boxed{
m_T\le
\sqrt{\frac{2\Delta_0}{\eta(T+1)}}.
}
$$

For $T\ge1$, this is slightly stronger than the requested result, since $T+1\ge T$:

$$
\boxed{
\min_{k=0,\ldots,T}\|\nabla f(x_k)\|
\le
\sqrt{
\frac{2}{\eta T}
\left(f(x_0)-f(x^*)\right)
}.
}
$$

Alternatively, using the $T$-term bound directly yields

$$
\min_{0\le k<T}\|\nabla f(x_k)\|
\le
\sqrt{\frac{2\Delta_0}{\eta T}},
$$

which also proves the requested statement because including $x_T$ cannot increase the minimum.

### Which point should we return?

Choose

$$
x'=x_{k^*},
\qquad
k^*\in
\operatorname*{arg\,min}_{0\le k\le T}
\|\nabla f(x_k)\|.
$$

The theorem controls the best gradient norm among the iterates. It does not establish the same finite-time bound specifically for the last iterate.

## 5. Worked Example: A Smooth, Nonconvex Function

Consider

$$
f(x)=1-\cos x.
$$

Its derivatives are

$$
f'(x)=\sin x,
\qquad
f''(x)=\cos x.
$$

Because $|f''(x)|\le1$, we can take $\beta=1$. The function is nonconvex because its second derivative is negative on some intervals. Its global minimum value is $0$, attained at $x=2m\pi$, where $m$ is any integer.

Take

$$
\eta=1,
\qquad
x_0=\frac{\pi}{2}.
$$

Then

$$
x_{k+1}=x_k-\sin x_k,
\qquad
\Delta_0=1.
$$

### Computed trajectory

The first few iterates are:

| $k$ | $x_k$ | $f(x_k)$ | Gradient norm |
|---:|---:|---:|---:|
| 0 | 1.570796 | 1.000000 | 1.000000 |
| 1 | 0.570796 | 0.158529 | 0.540302 |
| 2 | 0.030494 | 0.000465 | 0.030489 |
| 3 | 0.00000473 | approximately $1.12\times10^{-11}$ | approximately $4.73\times10^{-6}$ |

For the first step, Part 1 predicts

$$
f(x_1)
\le
1-\frac12(1)^2
=
0.5.
$$

The computed value is approximately $0.158529$, so the actual decrease is larger than the guaranteed decrease.

For $T=5$, the theorem guarantees

$$
\min_{0\le k\le5}|f'(x_k)|
\le
\sqrt{\frac25}
\approx0.63246.
$$

The example reaches a much smaller gradient by iteration $3$. The theorem is a worst-case upper bound, not a prediction of the exact trajectory.

### Schematic visualization

```text
f(x) = 1 − cos(x)

2                       ●  local maximum
                      /   \
                    /       \
1             x₀ ●             \
                /                \
              /                   \
0   minimum ●                       ● minimum
            0          π            2π

Starting at x₀ = π/2, gradient descent moves left:

0  ←  x₃  ←  x₂  ←  x₁  ←  x₀
```

The sketch is schematic, not to scale.

## 6. What the Guarantee Means—and Does Not Mean

### Iterations needed for a target gradient norm

Suppose we want

$$
\|\nabla f(x')\|\le\varepsilon.
$$

It is sufficient to ensure

$$
\sqrt{\frac{2\Delta_0}{\eta T}}\le\varepsilon.
$$

Squaring and rearranging gives

$$
\boxed{
T\ge\frac{2\Delta_0}{\eta\varepsilon^2}.
}
$$

With the largest permitted step size, $\eta=1/\beta$,

$$
\boxed{
T\ge\frac{2\beta\Delta_0}{\varepsilon^2}.
}
$$

Thus the best gradient norm has an $O(T^{-1/2})$ guarantee, corresponding to $O(\varepsilon^{-2})$ iterations to reach an $\varepsilon$-stationary point.

### A zero gradient can still be a bad solution

Return to

$$
f(x)=1-\cos x.
$$

If we initialize at $x_0=\pi$, then

$$
f'(\pi)=0.
$$

Gradient descent stays there forever, even though

$$
f(\pi)=2,
\qquad
f(x^*)=0.
$$

The stationarity guarantee is satisfied perfectly, but the point is a local maximum. This illustrates why first-order stationarity alone cannot certify a local or global minimum.

### Why we return an iterate rather than average the points

In convex optimization, convexity can turn a bound on average objective values into a guarantee for the average point.

Here, the proof instead bounds

$$
\frac1T\sum_{k=0}^{T-1}\|\nabla f(x_k)\|^2.
$$

That directly identifies at least one iterate with a small gradient. It does not provide a corresponding guarantee for the average location

$$
\bar x_T=\frac1T\sum_{k=0}^{T-1}x_k.
$$

The proof therefore selects an actual iterate rather than averaging their coordinates.

## 7. Compact Proof to Remember

After $T$ updates, smoothness and $0<\eta\le1/\beta$ imply

$$
f(x_{k+1})
\le
f(x_k)
-\frac{\eta}{2}\|\nabla f(x_k)\|^2.
$$

Summing for $k=0,\ldots,T-1$,

$$
\frac{\eta}{2}
\sum_{k=0}^{T-1}\|\nabla f(x_k)\|^2
\le
f(x_0)-f(x_T)
\le
f(x_0)-f(x^*).
$$

Hence,

$$
\begin{aligned}
\min_{0\le k\le T}\|\nabla f(x_k)\|^2
&\le
\min_{0\le k<T}\|\nabla f(x_k)\|^2\\
&\le
\frac1T
\sum_{k=0}^{T-1}\|\nabla f(x_k)\|^2\\
&\le
\frac{2}{\eta T}
\bigl(f(x_0)-f(x^*)\bigr).
\end{aligned}
$$

Taking square roots proves the result.

## Supporting Reading

- [On Nonconvex Optimization for Machine Learning: Gradients, Stochasticity, and Saddle Points](https://arxiv.org/html/1902.04811v2): first-order stationarity and nonconvex gradient-descent convergence.
- [Princeton Lecture 6: Gradient Descent](https://www.cs.princeton.edu/courses/archive/fall18/cos597G/lecnotes/lecture6.pdf): gradient descent and stationary points.
- [Carnegie Mellon Lecture 9: Gradient Descent Convergence / Subgradients](https://www.cs.cmu.edu/~mgormley/courses/10425//slides/lecture9-subgrad.pdf): small-gradient guarantees in nonconvex optimization.
- [MMiDS: Gradient Descent and Its Convergence Analysis](https://mmids-textbook.github.io/chap03_opt/05_gd/roch-mmids-opt-gd.html): smoothness and descent analysis.
