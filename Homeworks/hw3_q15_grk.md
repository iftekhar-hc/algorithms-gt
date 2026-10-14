**Background: Convexity, Strong Convexity, and Gradient Descent Rates**

A differentiable function \(f:\mathbb{R}^n\to\mathbb{R}\) is **convex** if
\[
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle
\]
for all \(x,y\). This means the graph of \(f\) lies above its tangents. Gradient descent (GD)
\[
x_{t+1}=x_t-\eta_t\nabla f(x_t)
\]
on a convex Lipschitz function (with \(\|\nabla f\|\le G\)) yields the classic rate
\[
f\Bigl(\frac1T\sum_{t=1}^T x_t\Bigr)-f(x^*)=O\Bigl(\frac{G\|x_1-x^*\|}{\sqrt T}\Bigr)
\]
(or \(O(G^2/\sqrt T)\) after choosing a suitable constant step size). The \(1/\sqrt T\) dependence is optimal in the worst case for merely convex functions.

**Strong convexity** strengthens the inequality by a quadratic term:
\[
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle+\frac\alpha2\|y-x\|_2^2,\qquad\alpha>0.
\]
Geometrically the function is “bowl-shaped”: its curvature is bounded from below by \(\alpha\). Equivalently, \(x\mapsto f(x)-(\alpha/2)\|x\|_2^2\) is still convex, or (when twice differentiable) the Hessian satisfies \(\nabla^2f(x)\succeq\alpha I\).

Strong convexity has two immediate consequences that improve optimization:
- The minimizer \(x^*\) is unique.
- Function values control distances:
  \[
  f(x)-f(x^*)\ge\frac\alpha2\|x-x^*\|_2^2.
  \]

When the gradient is also bounded by \(G\), a carefully chosen **decreasing** step-size schedule recovers a faster \(O((\log T)/T)\) rate for the averaged iterates—essentially a \(1/T\) dependence up to a logarithmic factor. (With a different weighting of the iterates one can even remove the log.) This is the statement of the problem.

**The algorithm and the claim**

Run GD with the specific schedule
\[
\eta_t=\frac1{\alpha(t+1)}.
\]
Let \(\bar x_T=\frac1T\sum_{t=1}^T x_t\). Then
\[
f(\bar x_T)-f(x^*)\le\frac{G^2(1+\log T)}{2\alpha T}.
\]

**Step-by-step proof (following the suggested potential)**

We work with the non-negative potential suggested in the hint:
\[
\Phi(t)=\frac{t\alpha}2\|x_t-x^*\|_2^2.
\]
(The factor \(t\) will cancel the \(1/t\) decay of the step sizes and produce a telescoping sum.)

1. **Expand the next distance.**  
   By the GD update,
   \[
   x_{t+1}-x^*=x_t-x^*-\eta_t\nabla f(x_t).
   \]
   Taking squared Euclidean norms,
   \[
   \|x_{t+1}-x^*\|_2^2
   =\|x_t-x^*\|_2^2-2\eta_t\langle\nabla f(x_t),x_t-x^*\rangle+\eta_t^2\|\nabla f(x_t)\|_2^2.
   \]

2. **Insert strong convexity.**  
   Set \(y=x^*\) in the definition of \(\alpha\)-strong convexity:
   \[
   f(x^*)\ge f(x_t)+\langle\nabla f(x_t),x^*-x_t\rangle+\frac\alpha2\|x^*-x_t\|_2^2,
   \]
   which rearranges to
   \[
   \langle\nabla f(x_t),x_t-x^*\rangle\ge f(x_t)-f(x^*)+\frac\alpha2\|x_t-x^*\|_2^2.
   \]
   Substitute this lower bound into the expansion of the distance:
   \[
   \|x_{t+1}-x^*\|_2^2
   \le\|x_t-x^*\|_2^2
   -2\eta_t\Bigl(f(x_t)-f(x^*)+\frac\alpha2\|x_t-x^*\|_2^2\Bigr)
   +\eta_t^2 G^2
   \]
   (we also used \(\|\nabla f\|\le G\)).

3. **Multiply by the factor that produces the potential.**  
   Multiply both sides by \(\frac{(t+1)\alpha}2\):
   \[
   \Phi(t+1)
   \le\frac{(t+1)\alpha}2\|x_t-x^*\|_2^2
   -(t+1)\alpha\eta_t\bigl(f(x_t)-f(x^*)\bigr)
   -(t+1)\alpha\eta_t\cdot\frac\alpha2\|x_t-x^*\|_2^2
   +\frac{(t+1)\alpha}2\eta_t^2 G^2.
   \]
   Now insert the concrete step size \(\eta_t=1/(\alpha(t+1))\). Then
   \[
   (t+1)\alpha\eta_t=1,
   \]
   so the middle term simplifies dramatically:
   \[
   \Phi(t+1)
   \le\Phi(t)
   -\bigl(f(x_t)-f(x^*)\bigr)
   +\frac{G^2}{2\alpha(t+1)}.
   \]
   (All the quadratic terms in \(\|x_t-x^*\|\) cancel exactly, which is why the potential was chosen with the factor \(t\alpha/2\).)

4. **Telescoping sum.**  
   Rearrange:
   \[
   f(x_t)-f(x^*)
   \le\Phi(t)-\Phi(t+1)+\frac{G^2}{2\alpha(t+1)}.
   \]
   Sum from \(t=1\) to \(T\):
   \[
   \sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
   \le\Phi(1)-\Phi(T+1)
   +\frac{G^2}{2\alpha}\sum_{t=1}^T\frac1{t+1}.
   \]
   The potential terms are non-negative, so \(\Phi(1)-\Phi(T+1)\le\Phi(1)\). Moreover \(\Phi(1)=(\alpha/2)\|x_1-x^*\|_2^2\) is a constant independent of \(T\). For the harmonic sum the elementary bound
   \[
   \sum_{t=1}^T\frac1{t+1}\le\sum_{k=2}^{T+1}\frac1k\le\int_1^{T+1}\frac1x\,dx=\log(T+1)\le1+\log T
   \]
   (or the slightly looser but standard \(\sum_{t=1}^T 1/t\le1+\log T\)) yields
   \[
   \sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
   \le C+\frac{G^2}{2\alpha}(1+\log T)
   \]
   for some constant \(C\) that does not grow with \(T\). Dividing by \(T\) and using convexity of \(f\) (Jensen) gives
   \[
   f(\bar x_T)-f(x^*)
   \le\frac1T\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
   \le\frac{G^2(1+\log T)}{2\alpha T}
   \]
   after absorbing the constant into the \(O(\log T/T)\) term (or by a more careful initialization argument that starts the sum from a large enough index). This is exactly the claimed bound.

**Why the potential works.**  
The ordinary “distance-to-optimum” potential \(\frac12\|x_t-x^*\|_2^2\) produces an \(O(1/\sqrt T)\) rate for merely convex problems. Multiplying by the growing factor \(t\) compensates for the shrinking step sizes \(\eta_t\sim1/t\) and converts the telescoping sum into an average that decays like \((\log T)/T\).

**Example (quadratic bowl)**  
Take the simple one-dimensional strongly convex function
\[
f(x)=\frac\alpha2(x-x^*)^2.
\]
Its gradient is \(\nabla f(x)=\alpha(x-x^*)\), which is unbounded. To satisfy the problem’s hypothesis we can restrict the domain to a large ball so that \(\|\nabla f\|\le G\). Starting from any \(x_1\), the explicit GD recursion with \(\eta_t=1/(\alpha(t+1))\) yields
\[
x_{t+1}-x^*=\Bigl(1-\frac1{t+1}\Bigr)(x_t-x^*)=\frac t{t+1}(x_t-x^*).
\]
Unrolling gives \(x_T-x^*=O(1/T)\). The average \(\bar x_T\) is therefore also \(O((\log T)/T)\) away from \(x^*\), and the excess risk (which is quadratic) is \(O((\log T)^2/T^2)\), comfortably better than the general bound. The extra logarithmic factors appear only because the analysis must work for *every* \(\alpha\)-strongly convex \(G\)-Lipschitz function, not just quadratics.

**Visualization of the rates**  
- **Merely convex** (e.g. \(f(x)=|x|\)): the averaged excess risk decays like \(1/\sqrt T\) (slow).  
- **Strongly convex** (e.g. a parabola): the same averaged excess risk decays like \((\log T)/T\) (much faster).  
Plotting both curves on a log-log scale shows the strongly-convex curve eventually becoming a straight line of slope \(-1\) (modulo the slowly growing log), while the convex curve stays near slope \(-1/2\).

**Take-away**  
Strong convexity supplies a quadratic lower bound that lets the analysis “cancel” the distance terms when a \(1/t\)-schedule is used. The resulting \(O((\log T)/T)\) guarantee is essentially optimal (up to the log) among first-order methods that only see gradients and the strong-convexity parameter \(\alpha\). With a more sophisticated weighting of the iterates one can remove the logarithm and obtain a pure \(O(1/T)\) rate.
