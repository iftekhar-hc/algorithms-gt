## Q15. Gradient Descent for Strongly Convex Functions

For ordinary convexity, we have:

$$
f(x_t)-f(x^*)
\le
\langle \nabla f(x_t),x_t-x^*\rangle.
$$

For strong convexity, we substitute $x = x_t$ and $y = x^*$ into the definition:

$$
f(x^*)
\ge
f(x_t)
+\langle\nabla f(x_t),x^*-x_t\rangle
+\frac{\alpha}{2}\|x_t-x^*\|_2^2,
$$

Re-arranging the above, we get:

$$
f(x_t)-f(x^*)
\le
\langle \nabla f(x_t),x_t-x^*\rangle
-
\frac{\alpha}{2}\|x_t-x^*\|_2^2.
\tag{1}
$$

Let

$$
g_t=\nabla f(x_t),
\qquad
R_t=\|x_t-x^*\|_2^2.
$$

Applying the gradient descent update rule, $x_{t+1}=x_t-\eta_tg_t$:

$$
\begin{aligned}
R_{t+1}
&=\|x_t-\eta_tg_t-x^*\|_2^2\\
&=R_t
-2\eta_t\langle g_t,x_t-x^*\rangle
+\eta_t^2\|g_t\|_2^2.
\end{aligned}
$$

Re-arranging the inner product:

$$
\langle g_t,x_t-x^*\rangle
=
\frac{R_t-R_{t+1}}{2\eta_t}
+\frac{\eta_t}{2}\|g_t\|_2^2.
$$

Since $\|g_t\|_2\le G$, we have:

$$
\langle g_t,x_t-x^*\rangle
\le
\frac{R_t-R_{t+1}}{2\eta_t}
+\frac{\eta_tG^2}{2}.
\tag{2}
$$

Now, substituting (2) into (1):

$$
f(x_t)-f(x^*)
\le
\frac{R_t-R_{t+1}}{2\eta_t}
-\frac{\alpha}{2}R_t
+\frac{\eta_tG^2}{2}.
\tag{3}
$$

The given step-size can written as:

$$
\frac{1}{2\eta_t}=\frac{\alpha(t+1)}{2},
$$

This allows us to re-write (3) as follows:

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

We define the potential:

$$
\Phi(t)=\frac{\alpha t}{2}R_t
=
\frac{\alpha t}{2}\|x_t-x^*\|_2^2.
$$

Then, (4) can be written as:

$$
f(x_t)-f(x^*)
\le
\Phi(t)-\Phi(t+1)
+
\frac{G^2}{2\alpha(t+1)}.
\tag{5}
$$

Summing (5) over $t$ steps:

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

The potential terms telescope above and we note that $\Phi(0)=0, \Phi(T)\ge0.$ Hence,

$$
\Phi(0)-\Phi(T)\le0.
$$

This allows us to write:

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2}{2\alpha}
\sum_{t=0}^{T-1}\frac1{t+1}.
$$

Using the harmonic sum bound and letting $s = t + 1$:

$$
\sum_{t=0}^{T-1}\frac1{t+1}
=
\sum_{s=1}^{T}\frac1s
\le1+\log T.
$$

Consequently,

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2(1+\log T)}{2\alpha}.
\tag{6}
$$

We define:

$$
\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t.
$$

Strong convexity implies ordinary convexity. This allows us to apply Jensen’s inequality:

$$
f(\bar x_T)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

Subtract $f(x^*)$:

$$
f(\bar x_T)-f(x^*)
\le
\frac1T\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr).
$$

Applying (6), we get:

$$
f(\bar x_T)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
$$

Hence,

$$
f\left(\frac1T\sum_{t}x_t\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
$$

















