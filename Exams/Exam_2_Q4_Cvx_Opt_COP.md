# Question 4: Convex Optimization and Gradient Descent

Question 4 considers an unconstrained differentiable function

$$
f:\mathbb{R}^d\to\mathbb{R}
$$

that is:

- $\alpha$-strongly convex,
- $\beta$-smooth,
- minimized globally at $x^\ast$,

and applies gradient descent with step size

$$
\eta=\frac{1}{\beta},
\qquad
x_{k+1}=x_k-\frac{1}{\beta}\nabla f(x_k).
$$

The problem asks you to prove that gradient descent decreases the objective gap geometrically:

$$
f(x_k)-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)^k
\bigl(f(x_0)-f(x^\ast)\bigr).
$$

This is often called **linear convergence** or **geometric convergence**, even though the algorithm itself is iterative rather than “linear.”

---

## 1. The big picture

The proof has three stages:

1. **Smoothness gives sufficient decrease:**

   $$
   f(x_k)-f(x_{k+1})
   \ge
   \frac{1}{2\beta}\|\nabla f(x_k)\|^2.
   $$

2. **Strong convexity connects gradient size to suboptimality:**

   $$
   \|\nabla f(x_k)\|^2
   \ge
   2\alpha\bigl(f(x_k)-f(x^\ast)\bigr).
   $$

3. Combining them shows that each iteration removes at least an $\alpha/\beta$ fraction of the current objective gap:

   $$
   f(x_{k+1})-f(x^\ast)
   \le
   \left(1-\frac{\alpha}{\beta}\right)
   \bigl(f(x_k)-f(x^\ast)\bigr).
   $$

Repeatedly applying this one-step contraction produces the desired exponential bound.

A useful mental model is:

$$
\boxed{\text{Smoothness}\Longrightarrow\text{one step makes progress}}
$$

and

$$
\boxed{\text{Strong convexity}\Longrightarrow\text{the gradient detects how far we are from optimal}}
$$

Together:

$$
\boxed{\text{progress is a constant fraction of the remaining error}}
$$

---

## 2. Preliminary concepts

### 2.1 Gradient and gradient descent

For a differentiable function $f$, the gradient is

$$
\nabla f(x)=
\begin{bmatrix}
\frac{\partial f}{\partial x_1}(x)\\
\vdots\\
\frac{\partial f}{\partial x_d}(x)
\end{bmatrix}.
$$

The gradient points in the direction of greatest local increase. Therefore, the negative gradient points in the direction of greatest local decrease.

Gradient descent uses

$$
x_{k+1}=x_k-\eta\nabla f(x_k),
$$

where $\eta>0$ is the **step size** or **learning rate**.

#### Why does step size matter?

- If $\eta$ is too small, progress is safe but slow.
- If $\eta$ is appropriately chosen, progress is fast and stable.
- If $\eta$ is too large, the iterates can overshoot, oscillate, or diverge.

For this problem,

$$
\eta=\frac{1}{\beta}.
$$

The significance of this choice will become clear when we substitute the update into the smoothness inequality.

### 2.2 Convexity

A differentiable function $f$ is convex if

$$
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle
$$

for every $x,y$.

Geometrically, the tangent hyperplane at $x$ lies below the function everywhere.

For a convex differentiable function, a point satisfying

$$
\nabla f(x^\ast)=0
$$

is a global minimizer.

Ordinary convexity does not require the function to have noticeable curvature. For example,

$$
f(x)=x^4
$$

is convex, but it becomes very flat near $x=0$. That flatness can prevent a uniform geometric convergence guarantee.

---

## 3. Strong convexity

### 3.1 Definition

The function $f$ is $\alpha$-strongly convex if

$$
f(y)
\ge
f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\alpha}{2}\|y-x\|^2
$$

for all $x,y\in\mathbb{R}^d$, where $\alpha>0$.

Compare this with ordinary convexity:

$$
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle.
$$

Strong convexity adds a positive quadratic term:

$$
\frac{\alpha}{2}\|y-x\|^2.
$$

This means the function must curve upward at least as rapidly as a quadratic with curvature $\alpha$.

### 3.2 Geometric interpretation

Strong convexity says that the function lies above the quadratic model

$$
f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\alpha}{2}\|y-x\|^2.
$$

The parameter $\alpha$ is a **lower bound on curvature**:

- large $\alpha$: the function is sharply curved;
- small $\alpha$: the function can be relatively flat;
- $\alpha=0$: the condition reduces to ordinary convexity.

Strong convexity also implies that the global minimizer is unique.

### 3.3 Quadratic example

Consider

$$
f(x)=\frac{a}{2}x^2.
$$

Then

$$
f'(x)=ax,
\qquad
f''(x)=a.
$$

The function is $a$-strongly convex because its curvature is exactly $a$.

In higher dimensions, consider

$$
f(x)=\frac12x^\top Qx+b^\top x+c,
$$

where $Q$ is symmetric positive definite. Then

$$
\nabla f(x)=Qx+b,
\qquad
\nabla^2 f(x)=Q.
$$

The strong-convexity parameter can be taken as

$$
\alpha=\lambda_{\min}(Q),
$$

the smallest eigenvalue of $Q$.

Thus, strong convexity constrains the function from being too flat in any direction.

### 3.4 Strong convexity gives quadratic growth

Set $x=x^\ast$ in the definition. Because $x^\ast$ is an unconstrained differentiable minimizer,

$$
\nabla f(x^\ast)=0.
$$

Therefore,

$$
f(y)\ge f(x^\ast)+\frac{\alpha}{2}\|y-x^\ast\|^2.
$$

Renaming $y$ as $x$,

$$
\boxed{f(x)-f(x^\ast)\ge\frac{\alpha}{2}\|x-x^\ast\|^2.}
$$

This says that objective suboptimality grows at least quadratically with distance from the optimizer.

Equivalently,

$$
\|x-x^\ast\|^2
\le
\frac{2}{\alpha}\bigl(f(x)-f(x^\ast)\bigr).
$$

Be careful about the inequality direction: small objective error guarantees small distance, but the displayed lower bound alone does not produce an upper bound on objective error.

---

## 4. Smoothness

### 4.1 Gradient-Lipschitz definition

A differentiable function is $\beta$-smooth if

$$
\|\nabla f(x)-\nabla f(y)\|
\le
\beta\|x-y\|
$$

for all $x,y$.

This means the gradient cannot change arbitrarily rapidly. The parameter $\beta$ is an **upper bound on curvature**.

- Strong convexity gives a lower curvature bound $\alpha$.
- Smoothness gives an upper curvature bound $\beta$.

For a twice-differentiable function, the two conditions correspond informally to

$$
\alpha I\preceq\nabla^2 f(x)\preceq\beta I.
$$

Consequently,

$$
0<\alpha\le\beta.
$$

### 4.2 Smoothness or descent lemma

The form needed for this question is

$$
\boxed{
f(y)
\le
f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\beta}{2}\|y-x\|^2.
}
$$

This is sometimes called the **descent lemma** or the quadratic upper bound.

It says that a $\beta$-smooth function lies below a quadratic model based at $x$.

Compare the two central inequalities:

#### Strong convexity: lower bound

$$
f(y)
\ge
f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\alpha}{2}\|y-x\|^2.
$$

#### Smoothness: upper bound

$$
f(y)
\le
f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\beta}{2}\|y-x\|^2.
$$

The function is therefore “sandwiched” between quadratic models.

### 4.3 Quadratic example

For

$$
f(x)=\frac12x^\top Qx+b^\top x+c,
$$

the smoothness parameter can be taken as

$$
\beta=\lambda_{\max}(Q).
$$

Thus,

$$
\lambda_{\min}(Q)=\alpha,
\qquad
\lambda_{\max}(Q)=\beta.
$$

---

## 5. Gradient norms and optimality

The Euclidean gradient norm is

$$
\|\nabla f(x)\|
=
\sqrt{\sum_{i=1}^d\left(\frac{\partial f}{\partial x_i}(x)\right)^2}.
$$

Its square is

$$
\|\nabla f(x)\|^2
=
\langle\nabla f(x),\nabla f(x)\rangle.
$$

The gradient norm measures first-order stationarity:

$$
\|\nabla f(x)\|=0
$$

means that $x$ is a stationary point.

For a convex differentiable function, stationary implies globally optimal. For a strongly convex function, the global optimizer is unique.

But a small gradient does not have the same meaning for every function. Strong convexity provides the quantitative relationship needed in this problem.

### 5.1 Strong convexity implies a gradient-gap inequality

The practice problem allows you to assume

$$
\boxed{\|\nabla f(x)\|^2\ge2\alpha\bigl(f(x)-f(x^\ast)\bigr).}
$$

This is often written as

$$
f(x)-f(x^\ast)
\le
\frac{1}{2\alpha}\|\nabla f(x)\|^2.
$$

Let us derive it.

From strong convexity, with $y=x^\ast$,

$$
f(x^\ast)
\ge
f(x)+\langle\nabla f(x),x^\ast-x\rangle
+\frac{\alpha}{2}\|x^\ast-x\|^2.
$$

Rearrange:

$$
f(x)-f(x^\ast)
\le
\langle\nabla f(x),x-x^\ast\rangle
-\frac{\alpha}{2}\|x-x^\ast\|^2.
$$

Let

$$
g=\nabla f(x),
\qquad
z=x-x^\ast.
$$

Then

$$
f(x)-f(x^\ast)
\le
\langle g,z\rangle-\frac{\alpha}{2}\|z\|^2.
$$

Complete the square:

$$
\langle g,z\rangle-\frac{\alpha}{2}\|z\|^2
=
-\frac{\alpha}{2}\left\|z-\frac{g}{\alpha}\right\|^2
+\frac{1}{2\alpha}\|g\|^2.
$$

Because the squared norm is nonnegative,

$$
-\frac{\alpha}{2}\left\|z-\frac{g}{\alpha}\right\|^2\le0.
$$

Therefore,

$$
f(x)-f(x^\ast)
\le
\frac{1}{2\alpha}\|\nabla f(x)\|^2.
$$

Multiplying by $2\alpha$,

$$
\boxed{\|\nabla f(x)\|^2\ge2\alpha\bigl(f(x)-f(x^\ast)\bigr).}
$$

#### Interpretation

If the objective gap is large, the gradient cannot be arbitrarily small:

$$
f(x)-f(x^\ast)\text{ large}
\quad\Longrightarrow\quad
\|\nabla f(x)\|\text{ sufficiently large}.
$$

That prevents gradient descent from becoming stuck far from the optimum.

---

## 6. Question 4.1: Prove sufficient decrease

We want to show

$$
\frac{1}{2\beta}\|\nabla f(x_k)\|^2
\le
f(x_k)-f(x_{k+1}).
$$

The smoothness inequality is

$$
f(y)
\le
f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\beta}{2}\|y-x\|^2.
$$

Apply it with

$$
x=x_k,
\qquad
y=x_{k+1}.
$$

Then

$$
f(x_{k+1})
\le
f(x_k)
+\langle\nabla f(x_k),x_{k+1}-x_k\rangle
+\frac{\beta}{2}\|x_{k+1}-x_k\|^2.
$$

The gradient-descent update gives

$$
x_{k+1}-x_k=-\frac{1}{\beta}\nabla f(x_k).
$$

Substitute this into the inner-product term:

$$
\begin{aligned}
\langle\nabla f(x_k),x_{k+1}-x_k\rangle
&=\left\langle\nabla f(x_k),-\frac1\beta\nabla f(x_k)\right\rangle\\
&=-\frac1\beta\|\nabla f(x_k)\|^2.
\end{aligned}
$$

For the squared-distance term,

$$
\begin{aligned}
\|x_{k+1}-x_k\|^2
&=\left\|-\frac1\beta\nabla f(x_k)\right\|^2\\
&=\frac{1}{\beta^2}\|\nabla f(x_k)\|^2.
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
f(x_{k+1})
&\le f(x_k)-\frac1\beta\|\nabla f(x_k)\|^2
+\frac{\beta}{2}\frac{1}{\beta^2}\|\nabla f(x_k)\|^2\\
&=f(x_k)-\frac1\beta\|\nabla f(x_k)\|^2
+\frac{1}{2\beta}\|\nabla f(x_k)\|^2\\
&=f(x_k)-\frac{1}{2\beta}\|\nabla f(x_k)\|^2.
\end{aligned}
$$

Rearrange:

$$
\boxed{f(x_k)-f(x_{k+1})\ge\frac{1}{2\beta}\|\nabla f(x_k)\|^2.}
$$

### What this inequality means

The quantity

$$
f(x_k)-f(x_{k+1})
$$

is the objective improvement during iteration $k$.

The result says

$$
\text{one-step improvement}
\ge
\frac{1}{2\beta}\|\nabla f(x_k)\|^2.
$$

Thus:

- a large gradient forces substantial progress;
- if little progress is made, the gradient must be small;
- the objective never increases under this step-size choice.

In particular,

$$
f(x_{k+1})\le f(x_k).
$$

---

## 7. Why choose $\eta=1/\beta$?

For a general step size

$$
x_{k+1}=x_k-\eta\nabla f(x_k),
$$

smoothness gives

$$
\begin{aligned}
f(x_{k+1})
&\le f(x_k)+\left\langle\nabla f(x_k),-\eta\nabla f(x_k)\right\rangle
+\frac{\beta}{2}\left\|-\eta\nabla f(x_k)\right\|^2\\
&=f(x_k)-\eta\|\nabla f(x_k)\|^2
+\frac{\beta\eta^2}{2}\|\nabla f(x_k)\|^2\\
&=f(x_k)-\eta\left(1-\frac{\beta\eta}{2}\right)\|\nabla f(x_k)\|^2.
\end{aligned}
$$

Therefore,

$$
\boxed{
f(x_k)-f(x_{k+1})
\ge
\eta\left(1-\frac{\beta\eta}{2}\right)\|\nabla f(x_k)\|^2.
}
$$

A guaranteed decrease requires

$$
1-\frac{\beta\eta}{2}>0,
$$

which means

$$
0<\eta<\frac{2}{\beta}.
$$

The guaranteed-decrease coefficient is

$$
h(\eta)=\eta-\frac{\beta}{2}\eta^2.
$$

This concave quadratic is maximized when

$$
h'(\eta)=1-\beta\eta=0,
$$

so

$$
\eta=\frac{1}{\beta}.
$$

At this value,

$$
h\left(\frac1\beta\right)=\frac{1}{2\beta}.
$$

Therefore, $\eta=1/\beta$ is the step size that maximizes this particular smoothness-based lower bound on one-step progress.

---

## 8. Question 4.2: Prove the one-step contraction

Part 1 gave

$$
f(x_k)-f(x_{k+1})
\ge
\frac{1}{2\beta}\|\nabla f(x_k)\|^2.
$$

Strong convexity gives

$$
\|\nabla f(x_k)\|^2
\ge
2\alpha\bigl(f(x_k)-f(x^\ast)\bigr).
$$

Substitute the second inequality into the first:

$$
\begin{aligned}
f(x_k)-f(x_{k+1})
&\ge\frac{1}{2\beta}\|\nabla f(x_k)\|^2\\
&\ge\frac{1}{2\beta}\cdot2\alpha\bigl(f(x_k)-f(x^\ast)\bigr)\\
&=\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr).
\end{aligned}
$$

Thus,

$$
f(x_k)-f(x_{k+1})
\ge
\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr).
$$

Now rearrange carefully:

$$
f(x_{k+1})
\le
f(x_k)-\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr).
$$

Subtract $f(x^\ast)$ from both sides:

$$
f(x_{k+1})-f(x^\ast)
\le
f(x_k)-f(x^\ast)
-\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr).
$$

Factor:

$$
\boxed{
f(x_{k+1})-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)
\bigl(f(x_k)-f(x^\ast)\bigr).
}
$$

### Error-sequence notation

Introduce the objective error

$$
\Delta_k=f(x_k)-f(x^\ast).
$$

Then the result becomes

$$
\boxed{\Delta_{k+1}\le\left(1-\frac{\alpha}{\beta}\right)\Delta_k.}
$$

### Interpretation as fractional progress

Rearrange the inequality from another perspective:

$$
f(x_k)-f(x_{k+1})
\ge
\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr).
$$

It says that each iteration eliminates at least the fraction

$$
\frac{\alpha}{\beta}
$$

of the current objective error. Accordingly, the fraction that remains is at most

$$
1-\frac{\alpha}{\beta}.
$$

---

## 9. Question 4.3: Prove convergence after $k$ iterations

We have

$$
\Delta_{k+1}\le\rho\Delta_k,
\qquad
\rho=1-\frac{\alpha}{\beta}.
$$

Apply the inequality repeatedly:

$$
\Delta_1\le\rho\Delta_0,
$$

$$
\Delta_2\le\rho\Delta_1\le\rho^2\Delta_0,
$$

$$
\Delta_3\le\rho\Delta_2\le\rho^3\Delta_0.
$$

Continuing,

$$
\Delta_k\le\rho^k\Delta_0.
$$

Substituting the definitions of $\rho$ and $\Delta_k$,

$$
\boxed{
f(x_k)-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)^k
\bigl(f(x_0)-f(x^\ast)\bigr).
}
$$

### Formal induction proof

#### Base case: $k=0$

$$
f(x_0)-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)^0
\bigl(f(x_0)-f(x^\ast)\bigr).
$$

Since the exponent is zero, the right-hand side equals the left-hand side.

#### Inductive hypothesis

Suppose

$$
f(x_k)-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)^k
\bigl(f(x_0)-f(x^\ast)\bigr).
$$

#### Inductive step

Using part 2,

$$
\begin{aligned}
f(x_{k+1})-f(x^\ast)
&\le\left(1-\frac{\alpha}{\beta}\right)\bigl(f(x_k)-f(x^\ast)\bigr)\\
&\le\left(1-\frac{\alpha}{\beta}\right)
\left(1-\frac{\alpha}{\beta}\right)^k
\bigl(f(x_0)-f(x^\ast)\bigr)\\
&=\left(1-\frac{\alpha}{\beta}\right)^{k+1}
\bigl(f(x_0)-f(x^\ast)\bigr).
\end{aligned}
$$

Therefore, the claim holds for every $k\ge0$.

---

## 10. Condition number

Define the condition number

$$
\boxed{\kappa=\frac{\beta}{\alpha}.}
$$

Since $\alpha\le\beta$,

$$
\kappa\ge1.
$$

The convergence factor becomes

$$
1-\frac{\alpha}{\beta}=1-\frac{1}{\kappa}.
$$

Therefore,

$$
f(x_k)-f(x^\ast)
\le
\left(1-\frac1\kappa\right)^k
\bigl(f(x_0)-f(x^\ast)\bigr).
$$

### Well-conditioned case

If $\alpha$ and $\beta$ are close, then $\kappa$ is close to $1$. The convergence factor is small, so convergence is fast.

### Ill-conditioned case

If $\beta\gg\alpha$, then $\kappa$ is large. The factor

$$
1-\frac1\kappa
$$

is close to $1$, so convergence is slow.

Geometrically, an ill-conditioned quadratic has elongated elliptical level sets. Gradient descent can zigzag across the narrow direction while making relatively slow progress along the flat direction.

---

## 11. Iteration complexity

Suppose we want

$$
f(x_k)-f(x^\ast)\le\varepsilon.
$$

Let

$$
\Delta_0=f(x_0)-f(x^\ast).
$$

The convergence result gives

$$
\Delta_k\le\left(1-\frac{\alpha}{\beta}\right)^k\Delta_0.
$$

Using

$$
1-t\le e^{-t}
$$

for $t\ge0$,

$$
\left(1-\frac{\alpha}{\beta}\right)^k
\le
e^{-k\alpha/\beta}.
$$

Thus,

$$
\Delta_k\le e^{-k\alpha/\beta}\Delta_0.
$$

It is sufficient to require

$$
e^{-k\alpha/\beta}\Delta_0\le\varepsilon.
$$

Solving for $k$,

$$
k\ge\frac{\beta}{\alpha}\ln\left(\frac{\Delta_0}{\varepsilon}\right).
$$

Using $\kappa=\beta/\alpha$,

$$
\boxed{k=O\left(\kappa\log\frac{\Delta_0}{\varepsilon}\right).}
$$

The logarithmic dependence on $1/\varepsilon$ is why the convergence is called exponential or geometric.

---

## 12. Worked one-dimensional example

Consider

$$
f(x)=\frac{a}{2}x^2,
\qquad a>0.
$$

Then

$$
\nabla f(x)=ax,
\qquad
x^\ast=0.
$$

This function is both $a$-strongly convex and $a$-smooth, so

$$
\alpha=\beta=a.
$$

With $\eta=1/\beta=1/a$,

$$
\begin{aligned}
x_{k+1}
&=x_k-\frac1a(ax_k)\\
&=x_k-x_k\\
&=0.
\end{aligned}
$$

Thus gradient descent reaches the optimizer in one step.

The general bound gives

$$
1-\frac{\alpha}{\beta}=1-\frac aa=0,
$$

which correctly predicts

$$
f(x_1)-f(x^\ast)=0.
$$

---

## 13. Worked two-dimensional quadratic

Consider

$$
f(x_1,x_2)=\frac12x_1^2+5x_2^2.
$$

Write it as

$$
f(x)=\frac12x^\top
\begin{bmatrix}
1&0\\
0&10
\end{bmatrix}x.
$$

Therefore,

$$
\alpha=1,
\qquad
\beta=10,
\qquad
\kappa=10.
$$

The gradient is

$$
\nabla f(x)=
\begin{bmatrix}
x_1\\
10x_2
\end{bmatrix}.
$$

With step size $\eta=1/10$,

$$
\begin{aligned}
x_{k+1}
&=x_k-\frac1{10}\nabla f(x_k)\\
&=
\begin{bmatrix}
x_{1,k}\\
x_{2,k}
\end{bmatrix}
-\frac1{10}
\begin{bmatrix}
x_{1,k}\\
10x_{2,k}
\end{bmatrix}\\
&=
\begin{bmatrix}
0.9x_{1,k}\\
0
\end{bmatrix}.
\end{aligned}
$$

The high-curvature $x_2$ component vanishes immediately, while the low-curvature $x_1$ component contracts by $0.9$.

The theoretical objective-gap factor is

$$
1-\frac{\alpha}{\beta}=1-\frac1{10}=0.9.
$$

This bound is valid, although it may not always be tight for a particular starting point or quadratic.

---

## 14. General step size and contraction

With a general step size $\eta$, smoothness gave

$$
f(x_k)-f(x_{k+1})
\ge
\eta\left(1-\frac{\beta\eta}{2}\right)\|\nabla f(x_k)\|^2.
$$

Using

$$
\|\nabla f(x_k)\|^2
\ge
2\alpha\bigl(f(x_k)-f(x^\ast)\bigr),
$$

we obtain

$$
f(x_k)-f(x_{k+1})
\ge
2\alpha\eta\left(1-\frac{\beta\eta}{2}\right)
\bigl(f(x_k)-f(x^\ast)\bigr).
$$

Therefore,

$$
\boxed{
f(x_{k+1})-f(x^\ast)
\le
\left(1-2\alpha\eta+\alpha\beta\eta^2\right)
\bigl(f(x_k)-f(x^\ast)\bigr).
}
$$

Setting $\eta=1/\beta$,

$$
\begin{aligned}
1-2\alpha\eta+\alpha\beta\eta^2
&=1-\frac{2\alpha}{\beta}+\frac{\alpha}{\beta}\\
&=1-\frac{\alpha}{\beta}.
\end{aligned}
$$

This recovers the bound required in the exam.

---

## 15. The short-answer question about step size

Consider the claim:

> When running gradient descent on a $\beta$-smooth convex function, we converge to the optimum regardless of step size or initial point.

The answer is:

$$
\boxed{\text{False}}
$$

Smoothness does not make every positive step size safe.

### Counterexample

Take

$$
f(x)=\frac{\beta}{2}x^2.
$$

Then

$$
\nabla f(x)=\beta x.
$$

Gradient descent produces

$$
x_{k+1}=x_k-\eta\beta x_k=(1-\eta\beta)x_k.
$$

The iterates converge to zero precisely when

$$
|1-\eta\beta|<1,
$$

which is equivalent to

$$
0<\eta<\frac{2}{\beta}.
$$

If

$$
\eta=\frac{2}{\beta},
$$

then

$$
x_{k+1}=-x_k,
$$

so the iterates oscillate without converging unless $x_0=0$.

If

$$
\eta>\frac{2}{\beta},
$$

then

$$
|1-\eta\beta|>1,
$$

and the iterates diverge in magnitude.

Therefore, convergence is not independent of step size.

---

## 16. Common proof mistakes

### Mistake 1: Using the wrong direction for smoothness

Smoothness gives an upper bound:

$$
f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\frac{\beta}{2}\|y-x\|^2.
$$

Strong convexity gives a lower bound:

$$
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle+\frac{\alpha}{2}\|y-x\|^2.
$$

A useful memory device:

- strong convexity: function is **above** a quadratic;
- smoothness: function is **below** a quadratic.

### Mistake 2: Forgetting to square the step-size factor

From

$$
x_{k+1}-x_k=-\frac1\beta\nabla f(x_k),
$$

we obtain

$$
\|x_{k+1}-x_k\|^2
=\frac1{\beta^2}\|\nabla f(x_k)\|^2,
$$

not $1/\beta$ times the squared gradient norm.

### Mistake 3: Combining inequalities in an invalid direction

You have

$$
A\ge\frac{1}{2\beta}\|\nabla f(x_k)\|^2
$$

and

$$
\|\nabla f(x_k)\|^2\ge2\alpha\Delta_k.
$$

Therefore,

$$
A
\ge
\frac{1}{2\beta}\|\nabla f(x_k)\|^2
\ge
\frac{\alpha}{\beta}\Delta_k.
$$

Both inequalities point in the same direction, so substitution is valid.

### Mistake 4: Losing the optimum term while rearranging

From

$$
f(x_k)-f(x_{k+1})
\ge
\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr),
$$

do not jump directly to the conclusion.

First isolate $f(x_{k+1})$, then subtract $f(x^\ast)$, and finally factor the gap.

### Mistake 5: Claiming a small gradient always proves near-optimality

Without additional structure, a small gradient need not imply a small objective gap. The quantitative implication used here,

$$
f(x)-f(x^\ast)\le\frac{1}{2\alpha}\|\nabla f(x)\|^2,
$$

depends on strong convexity.

### Mistake 6: Confusing exponential convergence with an exponential-time algorithm

“Exponential convergence” means the error decreases geometrically:

$$
\Delta_k\le\rho^k\Delta_0,
\qquad 0\le\rho<1.
$$

It does not mean the running time grows exponentially. In fact, reaching accuracy $\varepsilon$ takes only logarithmically many iterations in $1/\varepsilon$, up to the condition-number factor.

---

## 17. Exam-ready solution

Here is a concise version suitable for an exam answer.

### Part 1

By $\beta$-smoothness,

$$
f(x_{k+1})
\le
f(x_k)+\langle\nabla f(x_k),x_{k+1}-x_k\rangle
+\frac{\beta}{2}\|x_{k+1}-x_k\|^2.
$$

Since

$$
x_{k+1}-x_k=-\frac1\beta\nabla f(x_k),
$$

we obtain

$$
\begin{aligned}
f(x_{k+1})
&\le f(x_k)-\frac1\beta\|\nabla f(x_k)\|^2
+\frac{\beta}{2\beta^2}\|\nabla f(x_k)\|^2\\
&=f(x_k)-\frac1{2\beta}\|\nabla f(x_k)\|^2.
\end{aligned}
$$

Hence,

$$
\boxed{\frac1{2\beta}\|\nabla f(x_k)\|^2\le f(x_k)-f(x_{k+1}).}
$$

### Part 2

Using part 1 and the supplied strong-convexity inequality,

$$
\begin{aligned}
f(x_k)-f(x_{k+1})
&\ge\frac1{2\beta}\|\nabla f(x_k)\|^2\\
&\ge\frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr).
\end{aligned}
$$

Rearranging gives

$$
\boxed{
f(x_{k+1})-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)
\bigl(f(x_k)-f(x^\ast)\bigr).
}
$$

### Part 3

Repeatedly applying part 2 gives

$$
\begin{aligned}
f(x_k)-f(x^\ast)
&\le\left(1-\frac{\alpha}{\beta}\right)\bigl(f(x_{k-1})-f(x^\ast)\bigr)\\
&\le\cdots\\
&\le\left(1-\frac{\alpha}{\beta}\right)^k\bigl(f(x_0)-f(x^\ast)\bigr).
\end{aligned}
$$

Therefore,

$$
\boxed{
f(x_k)-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)^k
\bigl(f(x_0)-f(x^\ast)\bigr).
}
$$

---

## 18. Concept map

```text
alpha-strong convexity
        |
        |  gradient cannot be too small far from optimum
        v
||grad f(x_k)||^2 >= 2 alpha [f(x_k) - f(x*)]
        |
        |
        +----------------------------------+
                                           |
beta-smoothness                            |
        |                                  |
        |  safe descent step               |
        v                                  |
f(x_k) - f(x_{k+1})                        |
    >= ||grad f(x_k)||^2 / (2 beta)         |
        |                                  |
        +----------------------------------+
                         |
                         v
f(x_{k+1}) - f(x*)
    <= (1 - alpha/beta)[f(x_k) - f(x*)]
                         |
                         v
f(x_k) - f(x*)
    <= (1 - alpha/beta)^k [f(x_0) - f(x*)]
```

---

## 19. Questions to evaluate your understanding

### Level 1: Core definitions

1. State the first-order definition of convexity.
2. What additional term appears in the definition of $\alpha$-strong convexity?
3. Conceptually, what does $\alpha$ measure?
4. State the gradient-Lipschitz definition of $\beta$-smoothness.
5. State the smoothness inequality used in the proof.
6. Conceptually, what does $\beta$ measure?
7. Why must $\alpha\le\beta$ when both conditions hold?
8. Why is an unconstrained minimizer $x^\ast$ expected to satisfy $\nabla f(x^\ast)=0$?
9. What is the difference between the update norm $\|x_{k+1}-x_k\|$ and the gradient norm $\|\nabla f(x_k)\|$?
10. What does the condition number $\kappa=\beta/\alpha$ tell us?

### Level 2: Proof mechanics

11. Starting with smoothness, derive

    $$
    f(x_{k+1})
    \le
    f(x_k)-\eta\left(1-\frac{\beta\eta}{2}\right)\|\nabla f(x_k)\|^2.
    $$

12. Why does setting $\eta=1/\beta$ produce the coefficient $1/(2\beta)$?
13. Show that the smoothness-based descent coefficient is positive when $0<\eta<2/\beta$.
14. Explain in words why part 1 alone does not yet prove geometric convergence.
15. What extra relationship supplied by strong convexity makes the geometric proof possible?
16. Starting from

    $$
    \|\nabla f(x)\|^2\ge2\alpha(f(x)-f(x^\ast)),
    $$

    rearrange it to upper-bound $f(x)-f(x^\ast)$.

17. Show every algebraic step needed to transform

    $$
    f(x_k)-f(x_{k+1})
    \ge
    \frac{\alpha}{\beta}\bigl(f(x_k)-f(x^\ast)\bigr)
    $$

    into the one-step contraction.

18. Prove part 3 by induction.

### Level 3: Calculations

19. Let $f(x)=3x^2$. Find $\alpha$, $\beta$, $x^\ast$, and the gradient-descent update with $\eta=1/\beta$.

20. Let

    $$
    f(x_1,x_2)=\frac12(2x_1^2+8x_2^2).
    $$

    Find:

    - $\nabla f(x)$,
    - $\alpha$,
    - $\beta$,
    - $\kappa$,
    - the step size $1/\beta$,
    - the theoretical contraction factor.

21. Suppose $\alpha=2$, $\beta=10$, and $f(x_0)-f(x^\ast)=100$. Use the theorem to upper-bound the error after $5$ iterations.
22. For the same values, find a sufficient number of iterations to make the error at most $0.01$.
23. If $\alpha=1$ and $\beta=100$, what fraction of the error is guaranteed to remain after one iteration?
24. If one iteration reduces the guaranteed remaining error factor from $0.99$ to $0.5$, which problem is better conditioned?

### Level 4: Deeper conceptual questions

25. Give an example of a convex function that is not strongly convex.
26. Why can gradient descent be much slower on merely convex functions than on strongly convex functions?
27. Does having a unique minimizer automatically imply strong convexity? Explain.
28. Why does a large condition number correspond to elongated level sets for a quadratic function?
29. Why can gradient descent zigzag on an ill-conditioned quadratic?
30. Does the theorem claim that the bound is exact at every iteration, or only that the actual error is no larger than the bound?
31. If the actual function is smoother than the known upper bound $\beta$, how might using an overly conservative $\beta$ affect convergence?
32. Why does $\eta=1/\beta$ maximize the guaranteed decrease from the descent-lemma analysis?
33. Can a step size larger than $1/\beta$ ever work? If so, why is $1/\beta$ still convenient?
34. Why is the statement “gradient descent converges for every step size on a smooth convex function” false?

---

## 20. Short self-test with answers

### Question A

For a $\beta$-smooth function, fill in the blank:

$$
f(y)
\le
f(x)+\langle\nabla f(x),y-x\rangle+\boxed{\phantom{\frac{\beta}{2}\|y-x\|^2}}.
$$

**Answer:**

$$
\boxed{\frac{\beta}{2}\|y-x\|^2}
$$

### Question B

If

$$
x_{k+1}=x_k-\frac1\beta\nabla f(x_k),
$$

what is $\|x_{k+1}-x_k\|^2$?

**Answer:**

$$
\boxed{\frac1{\beta^2}\|\nabla f(x_k)\|^2}
$$

### Question C

If $\alpha=3$ and $\beta=12$, what is the contraction factor?

**Answer:**

$$
1-\frac{\alpha}{\beta}=1-\frac3{12}=\boxed{\frac34}.
$$

### Question D

If the initial objective gap is $64$ and the contraction factor is $3/4$, what is the guaranteed upper bound after two steps?

**Answer:**

$$
\left(\frac34\right)^2 64
=\frac9{16}\cdot64
=\boxed{36}.
$$

### Question E

Which assumption is primarily responsible for each fact?

1. A step of size $1/\beta$ decreases the objective by at least a multiple of the squared gradient norm.
2. The squared gradient norm lower-bounds the objective gap.

**Answer:**

1. $\beta$-smoothness.
2. $\alpha$-strong convexity.

---

## 21. Final memory aid

Remember the proof as three lines:

$$
\boxed{
f(x_k)-f(x_{k+1})
\ge
\frac{1}{2\beta}\|\nabla f(x_k)\|^2
}
$$

$$
\boxed{
\|\nabla f(x_k)\|^2
\ge
2\alpha\bigl(f(x_k)-f(x^\ast)\bigr)
}
$$

Therefore,

$$
\boxed{
f(x_{k+1})-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)
\bigl(f(x_k)-f(x^\ast)\bigr)
}
$$

and after $k$ iterations,

$$
\boxed{
f(x_k)-f(x^\ast)
\le
\left(1-\frac{\alpha}{\beta}\right)^k
\bigl(f(x_0)-f(x^\ast)\bigr).
}
$$
