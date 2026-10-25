# Convex Optimization — Understanding Question 4

Question 4 on page 9 of the practice exam proves why **gradient descent converges exponentially fast when a function is both strongly convex and smooth**. The three parts build on one another: first prove that each step decreases the objective, then prove that the error shrinks by a constant factor, and finally repeat that bound for $k$ iterations.

The central idea is:

$$
\boxed{\text{Smoothness} + \text{Strong convexity} \Longrightarrow \text{Fast convergence}}
$$

This guide follows the exam's assumptions and notation.

## 1. The setup: what are we trying to prove?

Assume $f:\mathbb{R}^d\to\mathbb{R}$ is:

- **$\alpha$-strongly convex**, with $\alpha>0$.
- **$\beta$-smooth**, with $\beta>0$.
- Has a global minimizer $x^*$, so $f(x^*)$ is the smallest objective value.
- Optimized by unconstrained gradient descent from any $x_0$ using the fixed step size $\eta=1/\beta$.

The update rule is

$$
x_{k+1}=x_k-\frac{1}{\beta}\nabla f(x_k).
$$

The proof roadmap is:

1. **Descent (Part 1):** show that the objective decrease is at least $\|\nabla f(x_k)\|^2/(2\beta)$.
2. **Contraction (Part 2):** use strong convexity to show that the next iteration's optimality gap is at most $1-\alpha/\beta$ times the current gap.
3. **Repeated contraction (Part 3):** apply the Part 2 bound repeatedly to obtain a geometric convergence rate.

## 2. What is $\alpha$-strong convexity?

The exam defines strong convexity by

$$
f(y)\geq f(x)+\langle\nabla f(x),y-x\rangle+\frac{\alpha}{2}\|y-x\|^2.
$$

The first two terms, $f(x)+\langle\nabla f(x),y-x\rangle$, form the linear approximation to $f$ at $x$. Strong convexity says the function stays above this approximation by at least a quadratic amount.

In plain English, **strong convexity prevents the objective from being too flat**. The parameter $\alpha$ quantifies a minimum amount of curvature.

For a twice-differentiable function, a useful interpretation is

$$
\alpha I\preceq\nabla^2 f(x),
$$

where $\nabla^2 f(x)$ is the Hessian matrix. It means that curvature in every direction is at least $\alpha$.

### Visual intuition: a bowl-shaped objective

![A bowl-shaped objective and iterates moving toward the minimum](convex_optimization_bowl.png)

Imagine a ball rolling down a bowl. The minimum is at the bottom. A strongly convex function has a bowl-like shape with enough curvature to rule out long, perfectly flat directions.

**Example:** Consider $f(x)=x^2$.

$$
f'(x)=2x,\qquad f''(x)=2.
$$

Its curvature is exactly $2$, so it is $\alpha$-strongly convex for any $0<\alpha\leq 2$.

### Why strong convexity matters

It gives us a powerful relationship between the gradient and the distance from optimality. For this exam, the most important version is

$$
\boxed{\|\nabla f(x)\|^2\geq 2\alpha\bigl(f(x)-f(x^*)\bigr)}
$$

If we're still far above the optimal objective value, the gradient cannot be arbitrarily small. This is the inequality used in Part 2.

## 3. What is $\beta$-smoothness?

A differentiable function is $\beta$-smooth if its gradient does not change too rapidly:

$$
\|\nabla f(y)-\nabla f(x)\|\leq\beta\|y-x\|.
$$

The parameter $\beta$ is an **upper bound on curvature**. For a twice-differentiable function, the corresponding Hessian condition is

$$
\nabla^2 f(x)\preceq\beta I.
$$

Smoothness gives us an inequality called the *descent lemma*:

$$
\boxed{f(y)\leq f(x)+\langle\nabla f(x),y-x\rangle+\frac{\beta}{2}\|y-x\|^2}
$$

Notice the difference between the two definitions:

| Property | Inequality direction | Intuition |
|---|---|---|
| $\alpha$-strong convexity | Lower bound on $f(y)$ | The bowl cannot be too flat |
| $\beta$-smoothness | Upper bound on $f(y)$ | The bowl cannot be too sharply curved |

When both conditions hold,

$$
\alpha I\preceq\nabla^2 f(x)\preceq\beta I.
$$

In particular, $0<\alpha\leq\beta$. Strong convexity implies a unique minimizer; smoothness helps us choose a step size that makes predictable progress.

## 4. What is the gradient norm, and why does it matter?

The gradient at $x_k$ is $g_k=\nabla f(x_k)$. It points in the direction of steepest local increase. Gradient descent moves in the opposite direction:

$$
x_{k+1}=x_k-\eta g_k.
$$

The **gradient norm**, $\|g_k\|$, measures the magnitude of the slope. A large norm generally means the function changes rapidly near the current point; for an unconstrained differentiable minimizer, the gradient is zero.

The square $\|g_k\|^2$ appears in the proof because the guaranteed improvement is proportional to the square of the gradient magnitude.

Two useful inequalities connect gradient norm to the optimality gap $f(x)-f(x^*)$:

$$
\underbrace{2\alpha\bigl(f(x)-f(x^*)\bigr)}_{\text{strong convexity}}
\leq \|\nabla f(x)\|^2
\leq \underbrace{2\beta\bigl(f(x)-f(x^*)\bigr)}_{\text{smoothness}}.
$$

The left inequality is the one explicitly used in Part 2. The right inequality follows from the descent lemma and the fact that $f(x^*)$ is the global minimum. Together, they explain why the gradient norm is a useful measure of progress: for this class of functions, a small gradient norm implies a small objective gap.

## 5. Gradient descent step size: why use $\eta=1/\beta$?

The step size controls how far we move in the negative-gradient direction.

- **Too small:** progress may be unnecessarily slow.
- **Appropriately sized:** the objective decreases predictably.
- **Too large:** we may overshoot the minimum and even diverge.

Your exam chooses

$$
\boxed{\eta=\frac{1}{\beta}}.
$$

This value is particularly useful because the descent lemma gives a clean guarantee: each step decreases the objective by at least $\|\nabla f(x_k)\|^2/(2\beta)$.

For example, with $f(x)=x^2/2$, we have $\beta=1$ and $f'(x)=x$. Gradient descent becomes

$$
x_{k+1}=(1-\eta)x_k.
$$

Starting at $x_0=2$:

| Step size | Update behavior |
|---|---|
| $\eta=1$ | Reaches $x^*=0$ in one step |
| $\eta=0.2$ | Converges more slowly |
| $\eta=3$ | Diverges because the magnitude doubles each step |

Thus, convergence does **not** hold for an arbitrary step size. We use $1/\beta$ in Question 4 because it supports the proof we need.

## 6. Solve Question 4, Part 1: prove sufficient decrease

The exam asks us to show

$$
\frac{1}{2\beta}\|\nabla f(x_k)\|^2\leq f(x_k)-f(x_{k+1}).
$$

The key is to start with the **descent lemma**, then substitute the gradient descent update.

### Step 1: Start with smoothness

Apply the descent lemma at $x=x_k$ and $y=x_{k+1}$:

$$
\begin{aligned}
f(x_{k+1})\leq {}& f(x_k)
+\langle\nabla f(x_k),x_{k+1}-x_k\rangle\\
&+\frac{\beta}{2}\|x_{k+1}-x_k\|^2.
\end{aligned}
$$

### Step 2: Substitute the update rule

We know

$$
x_{k+1}-x_k=-\frac{1}{\beta}\nabla f(x_k).
$$

The inner-product term becomes

$$
\begin{aligned}
\langle\nabla f(x_k),x_{k+1}-x_k\rangle
&=-\frac{1}{\beta}\|\nabla f(x_k)\|^2.
\end{aligned}
$$

The squared-norm term becomes

$$
\frac{\beta}{2}\|x_{k+1}-x_k\|^2
=\frac{1}{2\beta}\|\nabla f(x_k)\|^2.
$$

### Step 3: Simplify

Substituting both expressions gives

$$
\begin{aligned}
f(x_{k+1})
&\leq f(x_k)-\frac{1}{\beta}\|\nabla f(x_k)\|^2\\
&\quad+\frac{1}{2\beta}\|\nabla f(x_k)\|^2\\
&=f(x_k)-\frac{1}{2\beta}\|\nabla f(x_k)\|^2.
\end{aligned}
$$

Move the terms to the other side:

$$
\boxed{f(x_k)-f(x_{k+1})\geq\frac{1}{2\beta}\|\nabla f(x_k)\|^2}
$$

**Part 1 is proved.**

### The intuition

The objective doesn't just decrease; we have a quantitative lower bound on the decrease. A larger gradient norm guarantees more progress under this step-size choice.

Remember the pattern: **descent lemma $\to$ substitute update $\to$ simplify**.

## 7. Solve Question 4, Part 2: prove one-step contraction

The exam provides the strong-convexity inequality

$$
\|\nabla f(x_k)\|^2\geq 2\alpha\bigl(f(x_k)-f(x^*)\bigr)
$$

and asks us to prove

$$
\boxed{
f(x_{k+1})-f(x^*)\leq
\left(1-\frac{\alpha}{\beta}\right)\bigl(f(x_k)-f(x^*)\bigr)
}
$$

This part is an exercise in **combining inequalities**. We already proved one inequality in Part 1, and the question gives us the second one.

### Step 1: Start with Part 1

$$
f(x_k)-f(x_{k+1})\geq\frac{1}{2\beta}\|\nabla f(x_k)\|^2.
$$

### Step 2: Apply the strong-convexity bound

Because

$$
\|\nabla f(x_k)\|^2\geq2\alpha\bigl(f(x_k)-f(x^*)\bigr),
$$

we can substitute the lower bound for the gradient norm:

$$
\begin{aligned}
f(x_k)-f(x_{k+1})
&\geq\frac{1}{2\beta}\|\nabla f(x_k)\|^2\\
&\geq\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^*)\bigr).
\end{aligned}
$$

This is the critical step: **each iteration removes at least an $\alpha/\beta$ fraction of the current optimality gap**.

### Step 3: Rearrange the inequality

Write the current gap as the sum of the decrease and the next gap:

$$
\begin{aligned}
f(x_{k+1})-f(x^*)
={}&f(x_k)-f(x^*)\\
&-\bigl(f(x_k)-f(x_{k+1})\bigr).
\end{aligned}
$$

Since the decrease is at least $\frac{\alpha}{\beta}(f(x_k)-f(x^*))$, we get

$$
\begin{aligned}
f(x_{k+1})-f(x^*)
&\leq (f(x_k)-f(x^*))\\
&\quad-\frac{\alpha}{\beta}(f(x_k)-f(x^*))\\
&=\left(1-\frac{\alpha}{\beta}\right)(f(x_k)-f(x^*)).
\end{aligned}
$$

**Part 2 is proved.**

### Why is this result so important?

Define the optimality gap as

$$
\Delta_k=f(x_k)-f(x^*).
$$

Then Part 2 simply says

$$
\Delta_{k+1}\leq q\Delta_k,\qquad q=1-\frac{\alpha}{\beta}.
$$

Because $0<\alpha\leq\beta$, the factor $q$ lies between $0$ and $1$. Each iteration shrinks the gap by a fixed factor, rather than subtracting just a fixed amount.

## 8. Solve Question 4, Part 3: prove exponential convergence

Now use Part 2 repeatedly:

$$
\begin{aligned}
\Delta_1&\leq q\Delta_0,\\
\Delta_2&\leq q\Delta_1\leq q^2\Delta_0,\\
\Delta_3&\leq q\Delta_2\leq q^3\Delta_0.
\end{aligned}
$$

Continuing this pattern gives

$$
\boxed{
f(x_k)-f(x^*)\leq
\left(1-\frac{\alpha}{\beta}\right)^k
\bigl(f(x_0)-f(x^*)\bigr)
}
$$

**Part 3 is proved.** This is the exponential (geometric) convergence guarantee.

### Visualizing the rate

Suppose $\alpha=1$ and $\beta=4$. The contraction factor is $q=1-1/4=0.75$. The chart shows the theoretical upper bound on the gap, relative to the initial gap.

![Geometric convergence bound when alpha is 1 and beta is 4](convex_optimization_convergence.png)

For $\alpha/\beta=1/4$, each iteration guarantees a remaining gap no larger than 75% of the previous gap.

More generally, since $1-t\leq e^{-t}$,

$$
\left(1-\frac{\alpha}{\beta}\right)^k\leq e^{-\alpha k/\beta}.
$$

This also gives the approximate iteration count needed for an error tolerance $\varepsilon$:

$$
k\geq\frac{\beta}{\alpha}\ln\left(\frac{f(x_0)-f(x^*)}{\varepsilon}\right).
$$

The number of iterations depends logarithmically on the desired accuracy and is governed by the ratio $\beta/\alpha$.

## 9. The condition number: why $\beta/\alpha$ matters

The ratio

$$
\kappa=\frac{\beta}{\alpha}
$$

is commonly called the condition number for this optimization setting.

- If $\alpha$ is close to $\beta$, then $1-\alpha/\beta$ is small, and the gap shrinks quickly.
- If $\beta$ is much larger than $\alpha$, then $1-\alpha/\beta$ is close to $1$, and the guaranteed progress per iteration is slower.

Strong convexity provides a lower curvature bound; smoothness provides an upper one. A wide gap between those bounds can make gradient descent less efficient.

For the exam, you don't need to derive the condition-number interpretation. It is useful for understanding the result.

## 10. A subtle point: the other Question 4 on page 2

The practice exam also has a separate short-answer question claiming that gradient descent on a $\beta$-smooth convex function converges regardless of the step size or initial point. The correct True/False answer is **False**.

The initial point can be arbitrary under the assumptions of the main question, provided it is a valid point in $\mathbb{R}^d$. But the step size cannot be arbitrary.

For $f(x)=x^2/2$, whose smoothness parameter is $\beta=1$,

$$
x_{k+1}=(1-\eta)x_k.
$$

With $\eta=3$, this becomes $x_{k+1}=-2x_k$; the magnitude of each iterate doubles, so gradient descent diverges unless the starting point is already at zero.

That is why Question 4 fixes $\eta=1/\beta$: it makes Part 1 work cleanly, enabling the later convergence proof.

## 11. Test your understanding

Try answering these four questions before checking the answer key.

### Question 1

What does $\alpha$-strong convexity tell us?

A. The gradient is always small.  
B. There is a positive lower bound on the function's curvature.  
C. Any gradient descent step size will work.

### Question 2

What key inequality comes from $\beta$-smoothness?

A. $f(y)\leq f(x)+\langle\nabla f(x),y-x\rangle+\frac{\beta}{2}\|y-x\|^2$.  
B. The function has exactly one global minimizer.  
C. The function's gradient is always zero.

### Question 3

Given $\eta=1/\beta$, what does Part 1 guarantee?

A. $f(x_k)-f(x_{k+1})\geq\frac{1}{2\beta}\|\nabla f(x_k)\|^2$.  
B. The objective decrease equals the squared gradient norm exactly.  
C. Every step reaches the global minimum.

### Question 4

If $\alpha=1$ and $\beta=4$, what is the contraction factor? What upper bound follows after three steps?

A. Factor $0.25$; gap at most $0.25^3$ times its initial value.  
B. Factor $0.75$; gap at most $0.75^3\approx0.422$ times its initial value.  
C. Factor $1$; no guaranteed decrease.

<details>
<summary><strong>Answer key and explanations</strong></summary>

1. **B.** Strong convexity rules out excessively flat directions.
2. **A.** This upper bound, the descent lemma, drives Part 1.
3. **A.** It is a lower bound on the decrease, not generally an equality.
4. **B.** Compute $q=1-\alpha/\beta=1-1/4=0.75$, then take $q^3$.

</details>

## Final proof pattern to remember

The most important chain of reasoning is:

1. **Descent lemma:** the chosen step gives a guaranteed objective decrease.
2. **Strong-convexity gradient bound:** the gradient norm is large enough relative to the current objective gap.
3. **One-step contraction:** combine the two bounds to get $\Delta_{k+1}\leq(1-\alpha/\beta)\Delta_k$.
4. **Geometric convergence:** repeat the contraction $k$ times.

In one sentence: **Part 1 tells you how much the objective decreases; strong convexity tells you why that decrease is proportional to the current gap.**
