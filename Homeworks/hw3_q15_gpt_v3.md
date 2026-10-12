# Gradient Descent for Strongly Convex Functions — Step-by-Step Solution

The key idea is that strong convexity gives us an extra negative term in the gradient descent analysis. By choosing a step size that decreases like $1/t$, we can use that term to make the error shrink fast enough to obtain a $1/T$ convergence bound.

We'll build the proof from the background, derive the key inequality, and then use the hint to finish the result.

## 1. Background: What are we trying to prove?

We want to minimize a differentiable function $f:\mathbb{R}^n\to\mathbb{R}$. Its minimizer is $x^*$, meaning

$$
x^*=\arg\min_x f(x).
$$

Gradient descent updates its current point by moving in the opposite direction of the gradient:

$$
\boxed{x_{t+1}=x_t-\eta_t\nabla f(x_t)}
$$

Here, the step size is

$$
\eta_t=\frac{1}{\alpha(t+1)}.
$$

The assumptions are:

- Strong convexity: $f$ curves upward at least as strongly as a quadratic with curvature $\alpha>0$.
- Bounded gradient: $\|\nabla f(x)\|_2\le G$ for every $x$.
- Goal: Bound the suboptimality of the average of the iterates,

$$
\bar x_T=\frac1T\sum_{t=1}^T x_t.
$$

Specifically, we need to prove

$$
f(\bar x_T)-f(x^*)
\le \frac{G^2(1+\log T)}{2\alpha T}.
$$

Notice that the bound decreases approximately like $\log(T)/T$, which is faster than the usual $1/\sqrt T$ rate for general convex optimization.

## 2. What does strong convexity give us?

The definition says that for any $x,y$,

$$
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\alpha}{2}\|y-x\|_2^2.
$$

Think of this as the usual first-order convexity inequality, with an additional positive quadratic term.

Convex Optimization - Engineering Design Optimization

Ordinary convexity

The graph lies above its tangent lines. The function may be very flat, so the minimizer can be difficult to approach quickly.

The world of optimization

Strong convexity

The graph has a guaranteed minimum curvature. This gives us an extra term proportional to the squared distance from the minimizer.

To see the most useful consequence, set $x=x_t$ and $y=x^*$ in the strong convexity inequality:

$$
\begin{aligned}
f(x^*)\ge {}& f(x_t)
+\langle\nabla f(x_t),x^*-x_t\rangle\\
&+\frac{\alpha}{2}\|x_t-x^*\|_2^2.
\end{aligned}
$$

Rearrange it:

$$
\begin{aligned}
f(x_t)-f(x^*)\le {}&
\langle\nabla f(x_t),x_t-x^*\rangle\\
&-\frac{\alpha}{2}\|x_t-x^*\|_2^2.
\end{aligned}
$$

This is the crucial inequality. The negative squared-distance term is what lets us improve the convergence rate.

## 3. The main trick: Track the squared distance to the minimizer

Define the squared distance at iteration $t$ as

$$
D_t=\|x_t-x^*\|_2^2.
$$

Gradient descent updates according to

$$
x_{t+1}=x_t-\eta_t\nabla f(x_t).
$$

Subtract $x^*$ from both sides, then square the norm:

$$
\begin{aligned}
D_{t+1}
&=\|x_t-x^*-\eta_t\nabla f(x_t)\|_2^2\\
&=D_t-2\eta_t
\langle\nabla f(x_t),x_t-x^*\rangle\\
&\qquad+\eta_t^2\|\nabla f(x_t)\|_2^2.
\end{aligned}
$$

Rearranging gives

$$
\begin{aligned}
\langle\nabla f(x_t),x_t-x^*\rangle
={}&\frac{D_t-D_{t+1}}{2\eta_t}\\
&+\frac{\eta_t}{2}\|\nabla f(x_t)\|_2^2.
\end{aligned}
$$

Since the gradient norm is bounded by $G$,

$$
\boxed{
\langle\nabla f(x_t),x_t-x^*\rangle
\le
\frac{D_t-D_{t+1}}{2\eta_t}
+\frac{\eta_tG^2}{2}
}
$$

This identity is the bridge between gradient descent and the distance to the optimum.

## 4. Combine the two inequalities

Recall our strong convexity result:

$$
f(x_t)-f(x^*)
\le
\langle\nabla f(x_t),x_t-x^*\rangle
-\frac{\alpha}{2}D_t.
$$

Substitute the bound from Step 3:

$$
\begin{aligned}
f(x_t)-f(x^*)
\le {}&
\frac{D_t-D_{t+1}}{2\eta_t}\\
&+\frac{\eta_tG^2}{2}
-\frac{\alpha}{2}D_t.
\end{aligned}
$$

Now insert the specified step size,

$$
\eta_t=\frac{1}{\alpha(t+1)},
\qquad
\frac{1}{2\eta_t}=\frac{\alpha(t+1)}2.
$$

This gives

$$
\begin{aligned}
f(x_t)-f(x^*)
\le {}&
\frac{\alpha(t+1)}2(D_t-D_{t+1})\\
&+\frac{G^2}{2\alpha(t+1)}
-\frac{\alpha}{2}D_t.
\end{aligned}
$$

Collect the coefficients of $D_t$:

$$
\frac{\alpha(t+1)}2-\frac{\alpha}{2}
=\frac{\alpha t}{2}.
$$

Therefore,

$$
\boxed{
\begin{aligned}
f(x_t)-f(x^*)\le {}&
\frac{t\alpha}{2}D_t
-\frac{(t+1)\alpha}{2}D_{t+1}\\
&+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
}
$$

This is the central inequality of the proof.

## 5. Use the potential function from the hint

The hint suggests defining

$$
\Phi(t)=\frac{t\alpha}{2}\|x_t-x^*\|_2^2
=\frac{t\alpha}{2}D_t.
$$

The inequality from Step 4 becomes especially simple:

$$
\boxed{
f(x_t)-f(x^*)
\le
\Phi(t)-\Phi(t+1)
+\frac{G^2}{2\alpha(t+1)}
}
$$

Why is this useful? The potential difference telescopes when we sum over iterations.

### Visualizing the telescoping sum

Each positive potential cancels the matching negative potential from the previous term.

$$
\Phi(1)-\Phi(2)
$$

$$
+\ \Phi(2)-\Phi(3)
$$

$$
+\ \Phi(3)-\Phi(4)
$$

$$
=\ \Phi(1)-\Phi(4)
$$

The intermediate terms disappear. In general, only the initial and final potentials remain.

Summing the inequality from $t=1$ through $T$ yields

$$
\begin{aligned}
\sum_{t=1}^T[f(x_t)-f(x^*)]
\le {}&\Phi(1)-\Phi(T+1)\\
&+\frac{G^2}{2\alpha}
\sum_{t=1}^T\frac1{t+1}.
\end{aligned}
$$

Since $\Phi(T+1)\ge0$, we may discard the negative final potential:

$$
\boxed{
\sum_{t=1}^T[f(x_t)-f(x^*)]
\le
\Phi(1)+\frac{G^2}{2\alpha}
\sum_{t=1}^T\frac1{t+1}
}
$$

Notice that one initial-potential term remains. This matters when checking the exact constants in the question.

## 6. Bound the harmonic sum

The hint gives us

$$
\sum_{t=1}^T\frac1t\le 1+\log T.
$$

But our sum currently starts at $t+1$:

$$
\sum_{t=1}^T\frac1{t+1}
=\sum_{k=2}^{T+1}\frac1k.
$$

This is where an indexing detail in the problem matters. With the update and indices exactly as stated, the bound obtained so far is

$$
\sum_{t=1}^T[f(x_t)-f(x^*)]
\le \Phi(1)+\frac{G^2}{2\alpha}
\sum_{k=2}^{T+1}\frac1k.
$$

We cannot simply drop $\Phi(1)$ or replace this shifted sum by the requested harmonic sum. The usual proof of the advertised result starts the iteration at $t=0$, averaging $x_0,\ldots,x_{T-1}$, or equivalently uses the step size $1/(\alpha t)$ when indexing from $t=1$.

Let's complete the standard proof, which explains the intended result.

## 7. Complete the intended proof with consistent indexing

Use the following equivalent indexing convention:

$$
x_{t+1}=x_t-\frac{1}{\alpha(t+1)}
\nabla f(x_t),\qquad t=0,\ldots,T-1.
$$

Define the potential

$$
\Phi(t)=\frac{t\alpha}{2}\|x_t-x^*\|_2^2.
$$

The same derivation as before gives, for every $t\ge0$,

$$
f(x_t)-f(x^*)
\le \Phi(t)-\Phi(t+1)
+\frac{G^2}{2\alpha(t+1)}.
$$

Sum over $t=0,\ldots,T-1$:

$$
\begin{aligned}
\sum_{t=0}^{T-1}[f(x_t)-f(x^*)]
&\le \Phi(0)-\Phi(T)\\
&\quad+\frac{G^2}{2\alpha}
\sum_{t=0}^{T-1}\frac1{t+1}.
\end{aligned}
$$

Because $\Phi(0)=0$ and $\Phi(T)\ge0$,

$$
\sum_{t=0}^{T-1}[f(x_t)-f(x^*)]
\le \frac{G^2}{2\alpha}
\sum_{k=1}^{T}\frac1k.
$$

Applying the harmonic-sum bound,

$$
\boxed{
\sum_{t=0}^{T-1}[f(x_t)-f(x^*)]
\le \frac{G^2(1+\log T)}{2\alpha}
}
$$

Now divide by $T$:

$$
\frac1T\sum_{t=0}^{T-1}f(x_t)-f(x^*)
\le \frac{G^2(1+\log T)}{2\alpha T}.
$$

Finally, use Jensen's inequality. Because $f$ is convex,

$$
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)
\le \frac1T\sum_{t=0}^{T-1}f(x_t).
$$

Combining the last two inequalities gives

$$
\boxed{
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)-f(x^*)
\le \frac{G^2(1+\log T)}{2\alpha T}
}
$$

This is the advertised bound, with the iteration indices aligned to the specified step size.

## 8. A numerical example

Suppose $\alpha=2$, $G=4$, and $T=100$. The bound is

$$
\begin{aligned}
f(\bar x_T)-f(x^*)
&\le \frac{16(1+\log 100)}{2(2)(100)}\\
&\approx 0.4484.
\end{aligned}
$$

### Explore the convergence bound

Adjust the number of iterations to see how the theoretical upper bound changes. Here, $\alpha=2$ and $G=4$.

Iterations $T$

## 100

1

250

500

750

1000

Upper bound on suboptimality

# 0.2242

The bound decreases approximately as $\log(T)/T$. It is a guarantee, not necessarily the actual error.

## 9. Why is this faster than the general convex case?

| General convex functions | Strongly convex functions |
| --- | --- |
| No guaranteed minimum curvature | Curvature is at least $\alpha$ |
| Typical regret bound $O(\sqrt T)$ | Regret bound $O(\log T)$ |
| Average suboptimality $O(1/\sqrt T)$ | Average suboptimality $O(\log T/T)$ |

The essential improvement is the negative term

$$
-\frac{\alpha}{2}\|x_t-x^*\|_2^2.
$$

It combines with the distance change in the gradient descent update to produce the telescoping potential. The diminishing step size then leaves a harmonic sum, which grows only logarithmically.

One technical caveat: a differentiable, strongly convex function on all of $\mathbb R^n$ cannot have a globally bounded gradient. The bounded-gradient assumption is typically intended for a bounded feasible domain. Also, as shown above, the problem's stated indexing has a one-step shift; the standard proof yields the requested bound when the iterates and step sizes are indexed consistently.

## Final proof strategy to remember

1. Apply strong convexity with $y=x^*$.
2. Expand $\|x_{t+1}-x^*\|_2^2$ using the gradient descent update.
3. Substitute the resulting inner-product bound into the strong convexity inequality.
4. Choose a weighted squared-distance potential so that the distance terms telescope.
5. Bound the remaining harmonic sum by $1+\log T$.
6. Apply Jensen's inequality to transfer the average function-value bound to the function evaluated at the average iterate.

The most important insight is Step 4: strong convexity and the right step size turn the per-iteration error into a telescoping potential difference plus a small summable term.
