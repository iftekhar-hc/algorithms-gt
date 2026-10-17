# Gradient Descent for Strongly Convex Functions

## Indexing clarification

The stated step size
\[
\eta_t=\frac{1}{\alpha(t+1)}
\]
and the suggested potential
\[
\Phi(t)=\frac{\alpha t}{2}\|x_t-x^*\|_2^2
\]
naturally give the proof below when the updates start at \(t=0\) and the output averages \(x_0,\ldots,x_{T-1}\).

The original problem instead averages \(x_1,\ldots,x_T\). To express the same algorithm with one-based labels, both the iterates and the step sizes must be reindexed: the step size becomes \(1/(\alpha t)\). We explicitly give that equivalent formulation at the end. We do not claim that changing only the averaging indices proves the original statement verbatim.

## Assumptions and algorithm

Let \(f\) be differentiable and \(\alpha\)-strongly convex, and let \(x^*\) be a minimizer. Assume that the gradients used by the algorithm satisfy
\[
\|\nabla f(x_t)\|_2\le G.
\]
Starting from \(x_0\), perform the updates
\[
x_{t+1}=x_t-\eta_t\nabla f(x_t),
\qquad
\eta_t=\frac{1}{\alpha(t+1)},
\qquad t=0,\ldots,T-1.
\]
Define
\[
\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t.
\]
We will show that
\[
\boxed{
f(\bar x_T)-f(x^*)
\le\frac{G^2(1+\log T)}{2\alpha T}.
}
\]
Here \(\log\) denotes the natural logarithm.

## 1. Apply strong convexity

Set
\[
g_t=\nabla f(x_t),
\qquad
R_t=\|x_t-x^*\|_2^2.
\]
Applying strong convexity with \(x=x_t\) and \(y=x^*\) gives
\[
f(x^*)\ge f(x_t)+\langle g_t,x^*-x_t\rangle
+\frac{\alpha}{2}R_t.
\]
Rearranging,
\[
f(x_t)-f(x^*)
\le\langle g_t,x_t-x^*\rangle-\frac{\alpha}{2}R_t.
\tag{1}
\]

## 2. Expand the gradient descent update

The update rule implies
\[
\begin{aligned}
R_{t+1}
&=\|x_t-\eta_tg_t-x^*\|_2^2\\
&=R_t-2\eta_t\langle g_t,x_t-x^*\rangle
+\eta_t^2\|g_t\|_2^2.
\end{aligned}
\]
Consequently,
\[
\langle g_t,x_t-x^*\rangle
=\frac{R_t-R_{t+1}}{2\eta_t}
+\frac{\eta_t}{2}\|g_t\|_2^2
\le\frac{R_t-R_{t+1}}{2\eta_t}
+\frac{\eta_tG^2}{2}.
\tag{2}
\]
Combining (1) and (2),
\[
f(x_t)-f(x^*)
\le\frac{R_t-R_{t+1}}{2\eta_t}
-\frac{\alpha}{2}R_t
+\frac{\eta_tG^2}{2}.
\tag{3}
\]

## 3. Introduce the potential

Substituting \(\eta_t=1/[\alpha(t+1)]\) into (3) yields
\[
\begin{aligned}
f(x_t)-f(x^*)
&\le\frac{\alpha(t+1)}{2}(R_t-R_{t+1})
-\frac{\alpha}{2}R_t
+\frac{G^2}{2\alpha(t+1)}\\
&=\frac{\alpha t}{2}R_t
-\frac{\alpha(t+1)}{2}R_{t+1}
+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
\]
Define
\[
\Phi(t)=\frac{\alpha t}{2}R_t.
\]
Then
\[
f(x_t)-f(x^*)
\le\Phi(t)-\Phi(t+1)
+\frac{G^2}{2\alpha(t+1)}.
\tag{4}
\]
The negative quadratic term supplied by strong convexity is what makes these time-weighted potential terms telescope.

## 4. Sum and telescope

Summing (4) over \(t=0,\ldots,T-1\),
\[
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^*)\bigr)
\le\Phi(0)-\Phi(T)
+\frac{G^2}{2\alpha}\sum_{t=0}^{T-1}\frac1{t+1}.
\]
Since \(\Phi(0)=0\) and \(\Phi(T)\ge0\),
\[
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^*)\bigr)
\le\frac{G^2}{2\alpha}\sum_{s=1}^{T}\frac1s
\le\frac{G^2(1+\log T)}{2\alpha}.
\tag{5}
\]

## 5. Bound the function value at the average

Strong convexity implies convexity, so Jensen's inequality gives
\[
f(\bar x_T)
\le\frac1T\sum_{t=0}^{T-1}f(x_t).
\]
Subtracting \(f(x^*)\) and applying (5),
\[
\boxed{
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)-f(x^*)
\le\frac{G^2(1+\log T)}{2\alpha T}.
}
\]
Thus the average suboptimality is \(O((\log T)/T)\), while the cumulative suboptimality is \(O(\log T)\). The displayed bound includes a logarithmic factor; it is not literally an \(O(1/T)\) bound.

## Equivalent formulation averaging from 1 to T

To label the same sequence starting at 1, define
\[
y_t=x_{t-1},\qquad t=1,\ldots,T+1.
\]
Then
\[
y_{t+1}=y_t-\frac1{\alpha t}\nabla f(y_t),
\]
and
\[
\frac1T\sum_{t=1}^{T}y_t
=\frac1T\sum_{t=0}^{T-1}x_t.
\]
Therefore,
\[
\boxed{
f\left(\frac1T\sum_{t=1}^{T}y_t\right)-f(x^*)
\le\frac{G^2(1+\log T)}{2\alpha T}.
}
\]
Equivalently, renaming \(y_t\) as \(x_t\), a fully consistent one-indexed statement uses the average \(T^{-1}\sum_{t=1}^{T}x_t\), step size \(\eta_t=1/(\alpha t)\), and potential
\[
\Psi(t)=\frac{\alpha(t-1)}2\|x_t-x^*\|_2^2.
\]

### Why the original indexing cannot simply be retained in this proof

If the original step size \(\eta_t=1/[\alpha(t+1)]\) is retained and (4) is summed from \(t=1\) to \(T\), the result is instead
\[
\sum_{t=1}^{T}\bigl(f(x_t)-f(x^*)\bigr)
\le\frac{\alpha}{2}\|x_1-x^*\|_2^2
-\frac{\alpha(T+1)}2\|x_{T+1}-x^*\|_2^2
+\frac{G^2}{2\alpha}\sum_{t=1}^{T}\frac1{t+1}.
\]
The initial potential is generally nonzero. An additional argument would be needed to obtain the exact original conclusion from that expression; it cannot be discarded merely by shifting the indices.
