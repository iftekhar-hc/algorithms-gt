# 15. Gradient Descent for Strongly Convex Functions

## Statement

Let \(f:\mathbb{R}^n\to\mathbb{R}\) be differentiable and \(\alpha\)-strongly convex for some \(\alpha>0\), and assume \(\lVert\nabla f(x)\rVert_2\le G\) at every iterate below. Let \(x^\star\) be a minimizer of \(f\). Run gradient descent from an arbitrary \(x_0\in\mathbb{R}^n\),

\[
x_{t+1}=x_t-\eta_t\nabla f(x_t),\qquad \eta_t=\frac{1}{\alpha(t+1)},\qquad t=0,1,\ldots,T-1.
\]

Then the average of these \(T\) iterates satisfies

\[
f\!\left(\frac{1}{T}\sum_{t=0}^{T-1}x_t\right)-f(x^\star)\le\frac{G^2(1+\log T)}{2\alpha T},
\]

where \(\log\) is the natural logarithm.

### Indexing

The step size \(\eta_t=1/(\alpha(t+1))\) and the hinted potential

\[
\Phi(t)=\frac{t\alpha}{2}\lVert x_t-x^\star\rVert_2^2
\]

fit together only if the index is allowed to start at \(t=0\). Then \(\Phi(0)=0\), and the initial distance drops out of the telescope. The average written in the problem as \(\frac1T\sum_{t=1}^T x_t\) is the same set of points after the relabeling \(x'_s=x_{s-1}\). Under that relabeling the step taken at \(x'_s\) has size \(1/(\alpha s)\), not \(1/(\alpha(s+1))\). The literal schedule \(\eta_t=1/(\alpha(t+1))\) on iterates \(x_1,\ldots,x_T\) leaves a nonzero initial potential; that variant is recorded in the remark, and it does not yield the constant above.

## Proof

Write \(g_t=\nabla f(x_t)\) and \(R_t=\lVert x_t-x^\star\rVert_2^2\).

### Strong convexity

Substitute \(x=x_t\) and \(y=x^\star\) into the definition of \(\alpha\)-strong convexity:

\[
f(x^\star)\ge f(x_t)+\langle g_t,x^\star-x_t\rangle+\frac\alpha2 R_t.
\]

Rearranging gives the basic gap inequality

\begin{equation}
f(x_t)-f(x^\star)\le\langle g_t,x_t-x^\star\rangle-\frac\alpha2 R_t.
\tag{1}
\end{equation}

For comparison, ordinary convexity would omit the last term. The negative quadratic term is what produces the \(1/T\) rate.

### Distance recursion

The update \(x_{t+1}=x_t-\eta_t g_t\) expands as

\begin{align*}
R_{t+1}
&=\lVert x_t-\eta_t g_t-x^\star\rVert_2^2\\
&=R_t-2\eta_t\langle g_t,x_t-x^\star\rangle+\eta_t^2\lVert g_t\rVert_2^2.
\end{align*}

Solving for the inner product and using \(\lVert g_t\rVert_2\le G\),

\begin{equation}
\langle g_t,x_t-x^\star\rangle
=\frac{R_t-R_{t+1}}{2\eta_t}+\frac{\eta_t}{2}\lVert g_t\rVert_2^2
\le\frac{R_t-R_{t+1}}{2\eta_t}+\frac{\eta_t G^2}{2}.
\tag{2}
\end{equation}

Substitute (2) into (1):

\begin{equation}
f(x_t)-f(x^\star)
\le\frac{R_t-R_{t+1}}{2\eta_t}-\frac\alpha2 R_t+\frac{\eta_t G^2}{2}.
\tag{3}
\end{equation}

### Step size and potential

The given step size is \(\eta_t=1/(\alpha(t+1))\), so

\[
\frac{1}{2\eta_t}=\frac{\alpha(t+1)}{2},\qquad
\frac{\eta_t G^2}{2}=\frac{G^2}{2\alpha(t+1)}.
\]

Equation (3) becomes

\begin{align*}
f(x_t)-f(x^\star)
&\le\frac{\alpha(t+1)}{2}(R_t-R_{t+1})-\frac\alpha2 R_t+\frac{G^2}{2\alpha(t+1)}\\
&=\Bigl(\frac{\alpha(t+1)}{2}-\frac\alpha2\Bigr)R_t-\frac{\alpha(t+1)}{2}R_{t+1}+\frac{G^2}{2\alpha(t+1)}\\
&=\frac{\alpha t}{2}R_t-\frac{\alpha(t+1)}{2}R_{t+1}+\frac{G^2}{2\alpha(t+1)}.
\end{align*}

Define

\[
\Phi(t)=\frac{\alpha t}{2}R_t=\frac{\alpha t}{2}\lVert x_t-x^\star\rVert_2^2.
\]

The previous display is then

\begin{equation}
f(x_t)-f(x^\star)\le\Phi(t)-\Phi(t+1)+\frac{G^2}{2\alpha(t+1)}.
\tag{4}
\end{equation}

This identity is valid at \(t=0\) as well: \(\eta_0=1/\alpha\) is finite, and \(\Phi(0)=0\).

### Telescoping

Sum (4) from \(t=0\) to \(t=T-1\):

\[
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^\star)\bigr)
\le\sum_{t=0}^{T-1}\bigl(\Phi(t)-\Phi(t+1)\bigr)
+\frac{G^2}{2\alpha}\sum_{t=0}^{T-1}\frac{1}{t+1}.
\]

The potential sum is \(\Phi(0)-\Phi(T)\). The first term is zero, and \(\Phi(T)=\frac{\alpha T}{2}R_T\ge 0\), so discarding \(-\Phi(T)\) only weakens the upper bound:

\[
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^\star)\bigr)
\le\frac{G^2}{2\alpha}\sum_{t=0}^{T-1}\frac{1}{t+1}.
\]

The change of index \(s=t+1\) turns the sum into a harmonic number,

\[
\sum_{t=0}^{T-1}\frac{1}{t+1}=\sum_{s=1}^{T}\frac1s.
\]

The hint, or the integral comparison \(1+\sum_{s=2}^{T}1/s\le 1+\int_1^T(1/u)\,du\), gives

\[
\sum_{s=1}^{T}\frac1s\le 1+\log T.
\]

Therefore

\begin{equation}
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^\star)\bigr)
\le\frac{G^2(1+\log T)}{2\alpha}.
\tag{5}
\end{equation}

### Averaging

Let

\[
\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t.
\]

Strong convexity implies convexity, so Jensen's inequality yields

\[
f(\bar x_T)\le\frac1T\sum_{t=0}^{T-1}f(x_t).
\]

Subtract \(f(x^\star)\) and apply (5):

\[
f(\bar x_T)-f(x^\star)
\le\frac1T\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^\star)\bigr)
\le\frac{G^2(1+\log T)}{2\alpha T}.
\]

This is the claimed bound. The \(1/T\) rate, up to the logarithmic factor from the decreasing step size, replaces the \(1/\sqrt{T}\) rate that the same argument gives for a merely convex Lipschitz function.

The bound is for the uniform average, not for the last iterate \(x_T\). The negative term \(-\Phi(T)\) was discarded, so the same estimate does not by itself control \(f(x_T)-f(x^\star)\).

## Remark on the 1-based reading

Suppose instead that the algorithm starts at a given \(x_1\) and uses \(\eta_t=1/(\alpha(t+1))\) for \(t=1,\ldots,T\), and that one averages \(x_1,\ldots,x_T\). Summing (4) from \(t=1\) to \(T\) produces

\[
\sum_{t=1}^{T}\bigl(f(x_t)-f(x^\star)\bigr)
\le\Phi(1)+\frac{G^2}{2\alpha}\sum_{t=1}^{T}\frac{1}{t+1},
\]

since \(\Phi(T+1)\ge 0\). The initial term is \(\Phi(1)=\frac\alpha2\lVert x_1-x^\star\rVert_2^2\). Strong monotonicity of the gradient, together with \(\nabla f(x^\star)=0\) and \(\lVert g_1\rVert_2\le G\), gives \(\lVert x_1-x^\star\rVert_2\le G/\alpha\), hence \(\Phi(1)\le G^2/(2\alpha)\). The remaining sum is \(H_{T+1}-1\le\log(T+1)\). One therefore obtains only

\[
f\!\left(\frac1T\sum_{t=1}^{T}x_t\right)-f(x^\star)
\le\frac{G^2\bigl(1+\log(T+1)\bigr)}{2\alpha T},
\]

which is slightly weaker than the stated constant.

The stated constant is recovered for the average of \(x_1,\ldots,x_T\) by the shifted schedule \(\eta_t=1/(\alpha t)\). The matching potential is then \(\Psi(t)=\frac{\alpha(t-1)}{2}R_t\), so that \(\Psi(1)=0\), and the same calculation yields

\[
f(x_t)-f(x^\star)\le\Psi(t)-\Psi(t+1)+\frac{G^2}{2\alpha t}.
\]

Summing from \(t=1\) to \(T\) and applying Jensen gives exactly

\[
f\!\left(\frac1T\sum_{t=1}^{T}x_t\right)-f(x^\star)\le\frac{G^2(1+\log T)}{2\alpha T}.
\]

This is the same algorithm as the proof above, after the relabeling \(x'_s=x_{s-1}\) and \(\eta'_s=\eta_{s-1}\).
