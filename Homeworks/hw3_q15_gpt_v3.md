# Gradient Descent for Strongly Convex Functions

The key is to reuse the lecture’s squared-distance calculation, but use strong convexity’s extra quadratic term to create an exact **cancellation**. With the decreasing step size, that cancellation makes the weighted potential telescope, leaving a harmonic sum.

There is one indexing detail to handle carefully: the given step size $\eta_t=1/[\alpha(t+1)]$ naturally starts at $t=0$, as does the hinted potential. I will first prove the result for the queried points $x_0,\ldots,x_{T-1}$, then write the equivalent one-based version matching your displayed average. The standard strongly convex gradient-descent analysis uses precisely this logarithmic-regret argument. [Logarithmic Regret Algorithms for Online Convex Optimization](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2006-Logarithmic_Regret_Algorithms_for_Online_Convex_Optimization.pdf)

## 1. Start with the lecture’s proof template

In the lecture, ordinary convexity gave

$$
f(x_t)-f(x^*)
\le
\langle \nabla f(x_t),x_t-x^*\rangle.
$$

Strong convexity improves this to

$$
\boxed{
f(x_t)-f(x^*)
\le
\langle \nabla f(x_t),x_t-x^*\rangle
-
\frac{\alpha}{2}\|x_t-x^*\|_2^2.
}
\tag{1}
$$

To obtain this, substitute $x=x_t$ and $y=x^*$ into the definition:

$$
f(x^*)
\ge
f(x_t)
+\langle\nabla f(x_t),x^*-x_t\rangle
+\frac{\alpha}{2}\|x_t-x^*\|_2^2,
$$

and rearrange.

The new negative squared-distance term is what makes the faster bound possible.

## 2. Expand one gradient-descent update

Write

$$
g_t=\nabla f(x_t),
\qquad
R_t=\|x_t-x^*\|_2^2.
$$

The update is

$$
x_{t+1}=x_t-\eta_tg_t.
$$

Therefore,

$$
\begin{aligned}
R_{t+1}
&=\|x_t-\eta_tg_t-x^*\|_2^2\\
&=R_t
-2\eta_t\langle g_t,x_t-x^*\rangle
+\eta_t^2\|g_t\|_2^2.
\end{aligned}
$$

Rearrange to isolate the inner product:

$$
\langle g_t,x_t-x^*\rangle
=
\frac{R_t-R_{t+1}}{2\eta_t}
+\frac{\eta_t}{2}\|g_t\|_2^2.
$$

Using $\|g_t\|_2\le G$,

$$
\boxed{
\langle g_t,x_t-x^*\rangle
\le
\frac{R_t-R_{t+1}}{2\eta_t}
+\frac{\eta_tG^2}{2}.
}
\tag{2}
$$

This is the same squared-distance identity used in the lecture. The improvement comes from combining it with strong convexity rather than ordinary convexity.

## 3. Combine the two inequalities

Substitute (2) into (1):

$$
f(x_t)-f(x^*)
\le
\frac{R_t-R_{t+1}}{2\eta_t}
-\frac{\alpha}{2}R_t
+\frac{\eta_tG^2}{2}.
\tag{3}
$$

Now use the prescribed step size,

$$
\eta_t=\frac{1}{\alpha(t+1)}.
$$

Then

$$
\frac{1}{2\eta_t}=\frac{\alpha(t+1)}{2},
$$

so (3) becomes

$$
\begin{aligned}
f(x_t)-f(x^*)
&\le
\frac{\alpha(t+1)}{2}(R_t-R_{t+1})
-\frac{\alpha}{2}R_t
+\frac{G^2}{2\alpha(t+1)}\\[2mm]
&=
\left(\frac{\alpha(t+1)}{2}-\frac{\alpha}{2}\right)R_t
-\frac{\alpha(t+1)}{2}R_{t+1}
+\frac{G^2}{2\alpha(t+1)}\\[2mm]
&=
\frac{\alpha t}{2}R_t
-\frac{\alpha(t+1)}{2}R_{t+1}
+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
\tag{4}
$$

### The crucial algebra

The coefficient of $R_t$ changes as follows:

$$
\boxed{
\frac{\alpha(t+1)}{2}
-
\frac{\alpha}{2}
=
\frac{\alpha t}{2}.
}
$$

The strong-convexity term subtracts exactly one unit of $\alpha R_t/2$. That is why the coefficient matches the hinted potential.

Without that term, the coefficient would remain $\alpha(t+1)/2$, and this particular telescoping argument would not work.

## 4. Introduce the hinted potential

Define

$$
\Phi(t)=\frac{\alpha t}{2}R_t
=
\frac{\alpha t}{2}\|x_t-x^*\|_2^2.
$$

Then (4) is exactly

$$
\boxed{
f(x_t)-f(x^*)
\le
\Phi(t)-\Phi(t+1)
+
\frac{G^2}{2\alpha(t+1)}.
}
\tag{5}
$$

This is the main one-step inequality.

Its interpretation is:

```text
Objective error at time t
           ≤
Decrease in weighted distance potential
           +
A remaining cost proportional to 1/(t+1)
```

The potential need not decrease every step. What matters is that its differences cancel when summed.

## 5. Sum and telescope

Sum (5) over $t=0,\ldots,T-1$:

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\sum_{t=0}^{T-1}
\bigl(\Phi(t)-\Phi(t+1)\bigr)
+
\frac{G^2}{2\alpha}
\sum_{t=0}^{T-1}\frac1{t+1}.
$$

The potential terms telescope:

$$
\begin{aligned}
&(\Phi(0)-\Phi(1))
+(\Phi(1)-\Phi(2))
+\cdots
+(\Phi(T-1)-\Phi(T))\\
&\qquad=\Phi(0)-\Phi(T).
\end{aligned}
$$

Now observe that

$$
\Phi(0)=0,
\qquad
\Phi(T)\ge0.
$$

Therefore,

$$
\Phi(0)-\Phi(T)\le0.
$$

Dropping this nonpositive term gives

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2}{2\alpha}
\sum_{t=0}^{T-1}\frac1{t+1}.
$$

Reindex the harmonic sum using $s=t+1$:

$$
\sum_{t=0}^{T-1}\frac1{t+1}
=
\sum_{s=1}^{T}\frac1s
\le1+\log T.
$$

Hence,

$$
\boxed{
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2(1+\log T)}{2\alpha}.
}
\tag{6}
$$

Here and below, $\log$ denotes the natural logarithm.

Notice that there is no initial-distance term: multiplying the initial squared distance by $t=0$ makes the initial potential zero.

## 6. Convert the sum into a guarantee for the average point

Define

$$
\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t.
$$

Strong convexity implies ordinary convexity, so Jensen’s inequality gives

$$
f(\bar x_T)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

Subtract $f(x^*)$ and apply (6):

$$
\begin{aligned}
f(\bar x_T)-f(x^*)
&\le
\frac1T\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)\\
&\le
\frac{G^2(1+\log T)}{2\alpha T}.
\end{aligned}
$$

Thus,

$$
\boxed{
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
}
\tag{7}
$$

## 7. Match the one-based indexing in your question

To label the queried points $x_1,\ldots,x_T$, rather than $x_0,\ldots,x_{T-1}$, shift every iteration index by one.

Under that convention, the update is

$$
x_{t+1}
=
x_t-\frac{1}{\alpha t}\nabla f(x_t),
\qquad t=1,\ldots,T.
$$

This uses the same step-size sequence:

$$
\frac1\alpha,\quad
\frac1{2\alpha},\quad
\frac1{3\alpha},\quad\ldots.
$$

The correspondingly shifted potential is

$$
\Psi(t)
=
\frac{\alpha(t-1)}{2}\|x_t-x^*\|_2^2,
$$

so $\Psi(1)=0$. The same calculation gives

$$
f(x_t)-f(x^*)
\le
\Psi(t)-\Psi(t+1)
+\frac{G^2}{2\alpha t}.
$$

Summing from $t=1$ to $T$ and applying Jensen yields exactly

$$
\boxed{
f\left(\frac{\sum_{t=1}^{T}x_t}{T}\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
}
$$

This is the standard one-based formulation of the logarithmic-regret bound. [Logarithmic Regret Algorithms for Online Convex Optimization](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2006-Logarithmic_Regret_Algorithms_for_Online_Convex_Optimization.pdf)

### Why the indexing matters

If you instead insist on simultaneously using

$$
x_{t+1}
=
x_t-\frac{1}{\alpha(t+1)}\nabla f(x_t),
\qquad t=1,\ldots,T,
$$

and the unshifted potential $\Phi(t)=\alpha tR_t/2$, the telescoping sum starts with $\Phi(1)$, not zero:

$$
\sum_{t=1}^{T}\bigl(f(x_t)-f(x^*)\bigr)
\le
\Phi(1)-\Phi(T+1)
+
\frac{G^2}{2\alpha}\sum_{t=1}^{T}\frac1{t+1}.
$$

You cannot simply discard the positive initial term. The clean intended proof uses either zero-based indexing throughout or the equivalent one-based indexing above.

## 8. Compare this with the ordinary-convexity result

| Feature | General convexity | Strong convexity |
|---|---|---|
| Objective-error inequality | $\langle g_t,x_t-x^*\rangle$ | $\langle g_t,x_t-x^*\rangle-\frac{\alpha}{2}R_t$ |
| Step size in this analysis | $D/(G\sqrt T)$ | $1/[\alpha(t+1)]$, zero-based |
| Potential | A constant multiple of $R_t$ | $\alpha tR_t/2$ |
| Sum of objective gaps | At most $DG\sqrt T$ | At most $\frac{G^2}{2\alpha}(1+\log T)$ |
| Average-point error | At most $DG/\sqrt T$ | At most $\frac{G^2}{2\alpha T}(1+\log T)$ |

The terminology in the question needs a small refinement:

- Cumulative regret, meaning the sum of the gaps, is $O(\log T)$.
- Average regret and the average-point optimization error are $O(\log T/T)$.

Thus, this proof gives a $1/T$-type improvement with a logarithmic factor, not a pure $O(1/T)$ bound. The standard strongly convex online gradient-descent theorem makes the same distinction. [Logarithmic Regret Algorithms for Online Convex Optimization](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2006-Logarithmic_Regret_Algorithms_for_Online_Convex_Optimization.pdf)

## 9. A technical caveat about the assumptions

Taken literally, an $\alpha$-strongly convex differentiable function on all of $\mathbb R^n$ cannot have a globally bounded gradient.

To see why, apply strong convexity in both directions and add:

$$
\langle\nabla f(x)-\nabla f(x^*),x-x^*\rangle
\ge
\alpha\|x-x^*\|_2^2.
$$

Since $x^*$ is an unconstrained minimizer, $\nabla f(x^*)=0$. Cauchy–Schwarz then implies, for $x\ne x^*$,

$$
\|\nabla f(x)\|_2
\ge
\alpha\|x-x^*\|_2.
$$

The right-hand side grows without bound as $x$ moves away from $x^*$.

For this exercise, the meaningful assumption is that

$$
\|\nabla f(x_t)\|_2\le G
$$

at all queried iterates. That is all the proof actually uses. Another standard formulation works over a bounded convex feasible set and uses projected gradient descent. [Logarithmic Regret Algorithms for Online Convex Optimization](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2006-Logarithmic_Regret_Algorithms_for_Online_Convex_Optimization.pdf)

## 10. What to remember for an exam

The entire argument is organized around this chain:

$$
\boxed{
\begin{aligned}
f(x_t)-f(x^*)
&\le
\frac{R_t-R_{t+1}}{2\eta_t}
-\frac{\alpha}{2}R_t
+\frac{\eta_tG^2}{2}\\
&=
\Phi(t)-\Phi(t+1)
+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
}
$$

Then:

1. Sum over the correctly indexed $T$ queried points.
2. Telescope the potential differences.
3. Use the zero initial potential and nonnegative final potential.
4. Bound the harmonic sum by $1+\log T$.
5. Divide by $T$ and apply convexity at the average point.
