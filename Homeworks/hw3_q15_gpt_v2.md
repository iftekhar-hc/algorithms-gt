# Gradient Descent for Strongly Convex Functions: Step-by-Step Proof

The key idea is to use **strong convexity to control how far each iterate is from the minimizer**, then combine those bounds to prove that the average of the iterates converges at a rate of $1/T$.

We will build the proof from the basics, explain why the step size is chosen as it is, derive each inequality, and finish with an intuitive example.

## 1\. Background: What are we trying to prove?

We are given a differentiable function $f:\mathbb R^n\to\mathbb R$ that is $\alpha$-strongly convex, meaning

$$
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\alpha}{2}\|y-x\|_2^2,
$$

where $\alpha>0$.

We also know that the gradient is bounded:

$$
\|\nabla f(x)\|_2\le G
\qquad\text{for all }x.
$$

Let $x^*$ be the minimizer of $f$. We want to show that gradient descent, using the step size

$$
\boxed{\eta_t=\frac{1}{\alpha(t+1)}},
$$

satisfies

$$
\boxed{
f\left(\frac{1}{T}\sum_{t=1}^T x_t\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
}
$$

Here, gradient descent updates its current point according to

$$
\boxed{x_{t+1}=x_t-\eta_t\nabla f(x_t).}
$$

Let's understand what each assumption contributes to the proof.

### A. What is strong convexity?

Ordinary convexity says that the graph of a function lies above its tangent lines. Strong convexity strengthens this condition by adding a positive quadratic term.

Specifically,

$$
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\alpha}{2}\|y-x\|_2^2.
$$

The extra term

$$
\frac{\alpha}{2}\|y-x\|_2^2
$$

ensures that the function curves upward at least as strongly as a quadratic with curvature $\alpha$.

A larger $\alpha$ means stronger curvature. This gives us more control over how far a point can be from the minimizer when its function value is close to optimal.

### B. What does the gradient bound mean?

The condition

$$
\|\nabla f(x)\|_2\le G
$$

says that the gradient never has a norm greater than $G$.

Since the gradient determines the direction and magnitude of each update, this condition lets us bound the size of the changes made by gradient descent.

### C. Why average the iterates?

Define the average iterate as

$$
\bar x_T=\frac{1}{T}\sum_{t=1}^T x_t.
$$

We will first derive a bound on the sum of the function-value differences,

$$
\sum_{t=1}^T \bigl(f(x_t)-f(x^*)\bigr),
$$

and then divide by $T$.

Because $f$ is convex, averaging the iterates cannot produce a worse function-value bound than their average:

$$
f(\bar x_T)\le \frac{1}{T}\sum_{t=1}^T f(x_t).
$$

Consequently,

$$
f(\bar x_T)-f(x^*)
\le
\frac{1}{T}\sum_{t=1}^T
\bigl(f(x_t)-f(x^*)\bigr).
$$

**This is our strategy:** bound the cumulative error of the iterates, then use convexity to transfer that bound to their average.

---

## 2\. The key inequality: Use strong convexity at the minimizer

The most important step is to apply strong convexity with

$$
x=x_t,\qquad y=x^*.
$$

Substituting these into the definition gives

$$
f(x^*)\ge f(x_t)
+\langle\nabla f(x_t),x^*-x_t\rangle
+\frac{\alpha}{2}\|x^*-x_t\|_2^2.
$$

Rearranging,

$$
f(x_t)-f(x^*)
\le
\langle\nabla f(x_t),x_t-x^*\rangle
-\frac{\alpha}{2}\|x_t-x^*\|_2^2.
$$

This inequality is crucial because it connects the function-value error to the gradient and the distance from the minimizer.

Let

$$
g_t=\nabla f(x_t).
$$

Then we can write

$$
\boxed{
f(x_t)-f(x^*)
\le
\langle g_t,x_t-x^*\rangle
-\frac{\alpha}{2}\|x_t-x^*\|_2^2.
}
\tag{1}
$$

Notice the **negative quadratic term**. This term is precisely what strong convexity gives us, and it will cancel an inconvenient term later in the proof.

## 3\. Connect the gradient to the distance between iterates

Gradient descent updates according to

$$
x_{t+1}=x_t-\eta_t g_t.
$$

Subtract $x^*$ from both sides:

$$
x_{t+1}-x^*=x_t-x^*-\eta_tg_t.
$$

Now square the Euclidean norm. Using the identity

$$
\|a-b\|_2^2
=\|a\|_2^2-2\langle a,b\rangle+\|b\|_2^2,
$$

we obtain

$$
\begin{aligned}
\|x_{t+1}-x^*\|_2^2
={}&\|x_t-x^*\|_2^2\\
&-2\eta_t\langle g_t,x_t-x^*\rangle\\
&+\eta_t^2\|g_t\|_2^2.
\end{aligned}
$$

Rearrange to isolate the inner product:

$$
\boxed{
\langle g_t,x_t-x^*\rangle
=
\frac{\|x_t-x^*\|_2^2-\|x_{t+1}-x^*\|_2^2}
{2\eta_t}
+\frac{\eta_t}{2}\|g_t\|_2^2.
}
\tag{2}
$$

This identity is the bridge between the gradient and the distance to the minimizer.

Since $\|g_t\|_2\le G$, we also have

$$
\boxed{
\langle g_t,x_t-x^*\rangle
\le
\frac{\|x_t-x^*\|_2^2-\|x_{t+1}-x^*\|_2^2}
{2\eta_t}
+\frac{\eta_t G^2}{2}.
}
\tag{3}
$$

### Why is this useful?

Equation (1) tells us that the function-value error is bounded by an inner product minus a quadratic distance term.

Equation (3) gives us a way to replace that inner product with a difference of squared distances.

Combining the two will produce terms that cancel when summed over iterations.

---

## 4\. Introduce the potential function

The hint suggests using

$$
\boxed{
\Phi(t)=\frac{t\alpha}{2}\|x_t-x^*\|_2^2.
}
$$

A potential function is a quantity that measures progress toward a goal. Here, it measures the squared distance to the minimizer, scaled by the iteration number.

Why multiply by $t$?

Because our step size decreases with $t$. The factor $t$ lets the distance terms from consecutive iterations line up and cancel when we sum the inequalities.

### Substitute the step size

Recall that

$$
\eta_t=\frac{1}{\alpha(t+1)}.
$$

Therefore,

$$
\frac{1}{2\eta_t}=\frac{\alpha(t+1)}{2}.
$$

Substituting this into equation (3) gives

$$
\begin{aligned}
\langle g_t,x_t-x^*\rangle
\le{}&
\frac{\alpha(t+1)}{2}\|x_t-x^*\|_2^2\\
&-\frac{\alpha(t+1)}{2}\|x_{t+1}-x^*\|_2^2\\
&+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
$$

Now substitute this bound into the strong-convexity inequality (1):

$$
\begin{aligned}
f(x_t)-f(x^*)
\le{}&
\frac{\alpha(t+1)}{2}\|x_t-x^*\|_2^2\\
&-\frac{\alpha(t+1)}{2}\|x_{t+1}-x^*\|_2^2\\
&+\frac{G^2}{2\alpha(t+1)}
-\frac{\alpha}{2}\|x_t-x^*\|_2^2.
\end{aligned}
$$

Combine the two terms involving $\|x_t-x^*\|_2^2$:

$$
\frac{\alpha(t+1)}{2}-\frac{\alpha}{2}
=\frac{\alpha t}{2}.
$$

Thus,

$$
\begin{aligned}
f(x_t)-f(x^*)
\le{}&
\frac{\alpha t}{2}\|x_t-x^*\|_2^2\\
&-\frac{\alpha(t+1)}{2}\|x_{t+1}-x^*\|_2^2\\
&+\frac{G^2}{2\alpha(t+1)}.
\end{aligned}
$$

Using the potential function, we obtain our main intermediate inequality:

$$
\boxed{
f(x_t)-f(x^*)
\le
\Phi(t)-\Phi(t+1)
+\frac{G^2}{2\alpha(t+1)}.
}
\tag{4}
$$

This is the central result of the potential-function analysis.

---

## 5\. Sum the inequalities: Watch the cancellation

Sum equation (4) over $t=1,\ldots,T$:

$$
\begin{aligned}
\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
\le{}&
\sum_{t=1}^T\bigl(\Phi(t)-\Phi(t+1)\bigr)\\
&+\frac{G^2}{2\alpha}
\sum_{t=1}^T\frac{1}{t+1}.
\end{aligned}
$$

The potential terms telescope:

$$
\begin{aligned}
\sum_{t=1}^T\bigl(\Phi(t)-\Phi(t+1)\bigr)
={}&\bigl(\Phi(1)-\Phi(2)\bigr)\\
&+\bigl(\Phi(2)-\Phi(3)\bigr)\\
&+\cdots\\
&+\bigl(\Phi(T)-\Phi(T+1)\bigr)\\
={}&\Phi(1)-\Phi(T+1).
\end{aligned}
$$

Every intermediate potential appears once with a positive sign and once with a negative sign, so those terms cancel.

Consequently,

$$
\boxed{
\begin{aligned}
\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
\le{}&
\Phi(1)-\Phi(T+1)\\
&+\frac{G^2}{2\alpha}
\sum_{t=1}^T\frac{1}{t+1}.
\end{aligned}
}
\tag{5}
$$

Since $\Phi(T+1)\ge 0$, we can drop the negative term $-\Phi(T+1)$. This gives

$$
\boxed{
\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
\le
\Phi(1)+\frac{G^2}{2\alpha}
\sum_{t=1}^T\frac{1}{t+1}.
}
\tag{6}
$$

**An important detail:** with the step-size indexing in the question, the initial term $\Phi(1)$ remains. We cannot simply discard it. We will return to this indexing issue below because it matters for the exact claimed bound.

## 6\. Use the harmonic-series bound

The hint gives us

$$
\sum_{t=1}^T\frac1t\le 1+\log T.
$$

The same bound, after shifting the index, gives

$$
\sum_{t=1}^T\frac1{t+1}
=\sum_{k=2}^{T+1}\frac1k
\le \log(T+1).
$$

Using this in equation (6), we obtain

$$
\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
\le
\Phi(1)+\frac{G^2}{2\alpha}\log(T+1).
$$

By convexity,

$$
f\left(\frac1T\sum_{t=1}^T x_t\right)
\le \frac1T\sum_{t=1}^T f(x_t).
$$

Therefore,

$$
\boxed{
f\left(\frac1T\sum_{t=1}^T x_t\right)-f(x^*)
\le
\frac{\Phi(1)}{T}
+\frac{G^2\log(T+1)}{2\alpha T}.
}
\tag{7}
$$

This is what the preceding calculation establishes for the step size as stated.

However, notice that equation (7) contains an initial-potential term, and its logarithmic term differs slightly from the desired bound. We need to address the indexing carefully to obtain the usual result.

---

## 7\. The indexing issue: How to obtain the claimed bound

There is a small but important indexing mismatch in the problem as written.

The standard proof of the claimed bound uses the step size

$$
\boxed{\eta_t=\frac{1}{\alpha t},\qquad t=1,\ldots,T.}
$$

With this indexing, we can prove the desired result directly.

Starting from the same inequalities as before, substitute $\eta_t=1/(\alpha t)$. We get

$$
\begin{aligned}
f(x_t)-f(x^*)
&\le
\frac{\alpha t}{2}\|x_t-x^*\|_2^2
-\frac{\alpha t}{2}\|x_{t+1}-x^*\|_2^2\\
&\qquad-\frac{\alpha}{2}\|x_t-x^*\|_2^2
+\frac{G^2}{2\alpha t}\\[4pt]
&=
\frac{\alpha(t-1)}{2}\|x_t-x^*\|_2^2
-\frac{\alpha t}{2}\|x_{t+1}-x^*\|_2^2
+\frac{G^2}{2\alpha t}.
\end{aligned}
$$

Define the shifted potential

$$
\Psi(t)=\frac{\alpha(t-1)}{2}\|x_t-x^*\|_2^2.
$$

Then

$$
\boxed{
f(x_t)-f(x^*)
\le
\Psi(t)-\Psi(t+1)+\frac{G^2}{2\alpha t}.
}
$$

Sum over $t=1,\ldots,T$:

$$
\begin{aligned}
\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
&\le \Psi(1)-\Psi(T+1)
+\frac{G^2}{2\alpha}\sum_{t=1}^T\frac1t.
\end{aligned}
$$

Now the crucial observation is that

$$
\Psi(1)=\frac{\alpha(1-1)}2\|x_1-x^*\|_2^2=0.
$$

Also, $\Psi(T+1)\ge0$. Hence,

$$
\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2}{2\alpha}\sum_{t=1}^T\frac1t.
$$

Apply the harmonic-series bound:

$$
\sum_{t=1}^T\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{G^2}{2\alpha}(1+\log T).
$$

Finally, convexity gives

$$
f\left(\frac1T\sum_{t=1}^T x_t\right)
\le \frac1T\sum_{t=1}^T f(x_t).
$$

Subtract $f(x^*)$ and divide by $T$:

$$
\boxed{
f\left(\frac{\sum_{t=1}^T x_t}{T}\right)-f(x^*)
\le
\frac{G^2(1+\log T)}{2\alpha T}.
}
$$

This is the claimed result, using the standard indexing $\eta_t=1/(\alpha t)$.

**Important qualification:** the proof above establishes the requested bound for $\eta_t=1/(\alpha t)$, not exactly for the stated $\eta_t=1/(\alpha(t+1))$ when the iterates are indexed from $1$. The latter convention requires an additional initial-potential term in this proof. The exercise likely has an off-by-one indexing error.

---

## 8\. Visual intuition: Why does the potential telescope?

Think of the potential as a measure of how far we are from the minimizer.

At each iteration, we have an inequality of the form

$$
\text{function error}
\le
\text{current potential}
-\text{next potential}
+\text{small error}.
$$

For the corrected indexing, the first few inequalities look like this:

| Iteration | Potential difference | Error term |
| --- | --- | --- |
| $t=1$ | $\Psi(1)-\Psi(2)$ | $\frac{G^2}{2\alpha}$ |
| $t=2$ | $\Psi(2)-\Psi(3)$ | $\frac{G^2}{4\alpha}$ |
| $t=3$ | $\Psi(3)-\Psi(4)$ | $\frac{G^2}{6\alpha}$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $t=T$ | $\Psi(T)-\Psi(T+1)$ | $\frac{G^2}{2\alpha T}$ |

When we add the rows, all intermediate potential terms cancel:

$$
\begin{aligned}
&\cancel{\Psi(1)}
-\cancel{\Psi(2)}
+\cancel{\Psi(2)}
-\cancel{\Psi(3)}\\
&\qquad+\cdots
+\cancel{\Psi(T)}
-\Psi(T+1).
\end{aligned}
$$

Only the initial and final potentials survive. Because the initial potential is zero and the final potential is nonnegative, the entire sum is nonpositive.

That is why the final bound depends only on the sum of the error terms.

---

## 9\. A simple example: A quadratic function

Consider the one-dimensional function

$$
f(x)=\frac{\alpha}{2}x^2.
$$

Its minimizer is $x^*=0$, and its gradient is

$$
f'(x)=\alpha x.
$$

Gradient descent with the step size $\eta_t=1/(\alpha t)$ gives

$$
\begin{aligned}
x_{t+1}
&=x_t-\frac{1}{\alpha t}\alpha x_t\\
&=x_t-\frac{x_t}{t}\\
&=\left(1-\frac1t\right)x_t.
\end{aligned}
$$

At $t=1$,

$$
x_2=(1-1)x_1=0.
$$

The algorithm reaches the minimizer in one update for this particular quadratic.

This is a special case, not a general property of gradient descent. For other strongly convex functions, the iterates need not reach the minimizer immediately. The potential-function proof instead controls their cumulative error.

---

## 10\. Why is the convergence rate $1/T$ instead of $1/\sqrt T$?

For general convex optimization, a common gradient-descent analysis with a suitable step size yields a bound of order

$$
O\left(\frac1{\sqrt T}\right).
$$

For strongly convex functions, the stronger curvature condition provides the additional negative term

$$
-\frac{\alpha}{2}\|x_t-x^*\|_2^2.
$$

That term is what makes the potential telescope with the right coefficients. The cumulative error grows at most logarithmically:

$$
\sum_{t=1}^T \bigl(f(x_t)-f(x^*)\bigr)
=O(\log T).
$$

Averaging the iterates and dividing by $T$ gives

$$
\boxed{
f(\bar x_T)-f(x^*)
=O\left(\frac{\log T}{T}\right).
}
$$

This is the improvement delivered by the standard strongly convex analysis.

One final mathematical caveat: a differentiable, strongly convex function on all of $\mathbb R^n$ cannot have a globally bounded gradient. In standard optimization settings, the gradient bound is understood to hold on a bounded feasible domain or on the iterates under consideration.

### Summary of the proof

The entire argument rests on four steps:

1. **Strong convexity:** Bound the function-value error using the gradient and squared distance to the minimizer.
2. **Gradient descent identity:** Express the gradient inner product as a difference of squared distances.
3. **Potential function:** Choose the scaling so the distance terms telescope when summed.
4. **Averaging:** Apply convexity and the harmonic-series bound to obtain an $O(\log T/T)$ error bound.

The most important technique to remember is the potential-function method: **choose a weighted distance to the optimum so that summing the one-step inequalities cancels all intermediate terms.**
