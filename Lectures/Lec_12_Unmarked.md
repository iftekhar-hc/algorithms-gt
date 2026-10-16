# CS 6515: Graduate Algorithms

## Lecture 12: Convexity and Gradient Descent

**Instructors:** Sahil Singla and Gerandy Brito  
**Term:** Fall 2026

---

## From linear to nonlinear optimization

An LP optimizes a linear function over a convex feasible region. We now allow a nonlinear objective, while retaining the geometric property that will make the problem tractable: convexity.

## 1. The offline optimization problem

We are given one fixed function $f:\mathbb{R}^d \to \mathbb{R}$ and a nonempty convex set $K \subseteq \mathbb{R}^d$. Our goal is

$$
\min_{x \in K} f(x).
$$

Whenever we write $x^*$, we assume a minimizer exists. An $\varepsilon$-optimal feasible answer satisfies

$$
f(x)-f(x^*) \leq \varepsilon.
$$

The input and objective are fixed throughout the computation. A value/gradient oracle lets us evaluate $f(x)$ and $\nabla f(x)$ at points we choose.

> **Definition (convex function).** A function $f$ is convex on a convex set $K$ if, for all $x,y \in K$ and $\lambda \in [0,1]$,
>
> $$
> f\bigl(\lambda x+(1-\lambda)y\bigr)
> \leq \lambda f(x)+(1-\lambda)f(y).
> $$

The graph lies below its chords. In particular, at the midpoint,

$$
f\left(\frac{x+y}{2}\right) \leq \frac{f(x)+f(y)}{2}.
$$

A linear function is both convex and concave. Thus maximizing $c^\top x$ over an LP region is equivalent to minimizing the convex function $-c^\top x$.

## 2. The first-order view: tangent planes are lower bounds

For vectors, write

$$
\langle u,v\rangle=u^\top v=\sum_i u_i v_i,
\qquad
\lVert u\rVert_2=\sqrt{\sum_i u_i^2},
\qquad
\nabla f(x)=\left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_d}\right).
$$

We use the Euclidean norm throughout these two lectures.

> **Theorem (first-order characterization).** A differentiable function $f:\mathbb{R}^d\to\mathbb{R}$ is convex if and only if, for all $x,y\in\mathbb{R}^d$,
>
> $$
> f(y) \geq f(x)+\langle \nabla f(x),y-x\rangle.
> $$

### Proof of the direction we will use

For $0<\theta\leq 1$, convexity gives

$$
f\bigl(x+\theta(y-x)\bigr)
\leq (1-\theta)f(x)+\theta f(y).
$$

Rearrange and let $\theta\downarrow 0$:

$$
f(y)-f(x)
\geq
\lim_{\theta\downarrow 0}
\frac{f\bigl(x+\theta(y-x)\bigr)-f(x)}{\theta}
=
\langle \nabla f(x),y-x\rangle.
$$

For the converse, apply the first-order inequality at

$$
z=\lambda x+(1-\lambda)y,
$$

once to $x$ and once to $y$. Multiply by $\lambda$ and $1-\lambda$ and add; the gradient terms cancel.

### The inequality to remember

Putting $y=x^*$ and rearranging,

$$
\boxed{f(x)-f(x^*) \leq \langle \nabla f(x),x-x^*\rangle.}
$$

This converts objective error into an inner product that we can analyze using the algorithm's update.

## 3. Examples and why local minima suffice

### 3.1 A calculus test, when second derivatives exist

For a twice continuously differentiable $f:\mathbb{R}^d\to\mathbb{R}$, convexity is equivalent to

$$
\nabla^2 f(x) \succeq 0
\qquad \text{for every }x.
$$

Here $\nabla^2 f$ is the Hessian matrix, and positive semidefinite means

$$
v^\top \nabla^2 f(x)v \geq 0
$$

for every vector $v$. In one dimension this is simply $f''(x)\geq 0$. Restricting $f$ to each line gives the multivariable version of this test.

> **Example (least squares).** For
>
> $$
> f(x)=\frac{1}{2}\lVert Ax-b\rVert_2^2,
> $$
>
> we have
>
> $$
> \nabla f(x)=A^\top(Ax-b),
> \qquad
> \nabla^2 f(x)=A^\top A.
> $$
>
> Since
>
> $$
> v^\top A^\top A v=\lVert Av\rVert_2^2\geq 0,
> $$
>
> least squares is convex. The transpose $A^\top$ in the gradient is essential.

> **Example (nondifferentiable convex functions).** The function $f(x)=|x|$ is convex but not differentiable at $0$. A maximum of affine functions,
>
> $$
> f(x)=\max_j\left(a_j^\top x+b_j\right),
> $$
>
> is also convex. Thus differentiability is an additional assumption, not part of the definition of convexity.

> **Theorem (local minimum implies global minimum).** If $f$ and $K$ are convex, every local minimum of $f$ on $K$ is a global minimum.

**Proof.** Suppose $x\in K$ is a local minimum but some $y\in K$ has $f(y)<f(x)$. For every $0<\theta\leq 1$, the feasible point

$$
z_\theta=(1-\theta)x+\theta y
$$

satisfies

$$
f(z_\theta)
\leq (1-\theta)f(x)+\theta f(y)
<f(x).
$$

As $\theta\downarrow 0$, these better feasible points approach $x$, contradicting local optimality. $\square$

### Stationary points and constraints

For differentiable unconstrained convex minimization, $\nabla f(x)=0$ certifies a global minimum by the first-order inequality. The converse also holds for an unconstrained minimum.

At a constrained boundary optimum the gradient need not vanish: $\min_{x\in[0,1]}x$ is optimized at $0$, with derivative $1$.

## 4. Gradient descent

First take $K=\mathbb{R}^d$. Starting at $x_0$, repeat

$$
x_{t+1}=x_t-\eta\nabla f(x_t),
\qquad t=0,1,\ldots.
$$

The parameter $\eta>0$ is the step size.

### 4.1 Why move in the negative-gradient direction?

For a small step $h$,

$$
f(x+h)=f(x)+\langle \nabla f(x),h\rangle+o(\lVert h\rVert_2).
$$

Among vectors with $\lVert h\rVert_2\leq \rho$, Cauchy-Schwarz gives

$$
\langle \nabla f(x),h\rangle
\geq -\rho\lVert \nabla f(x)\rVert_2.
$$

If the gradient is nonzero, equality is attained in direction $-\nabla f(x)$. This is the steepest first-order decrease in Euclidean distance. The direction is useful, but the step length still matters.

> **Example.** For $f(x)=x^2/2$, the update is
>
> $$
> x_{t+1}=(1-\eta)x_t.
> $$
>
> | Step size | Behavior from $x_0\neq 0$ | Lesson |
> |---:|:---|:---|
> | $\eta=1/2$ | $x_t=2^{-t}x_0$ | Converges |
> | $\eta=1$ | $x_1=0$ | Reaches the optimum immediately |
> | $\eta=2$ | $x_t=(-1)^t x_0$ | Oscillates without improving |
> | $\eta>2$ | $|x_t|$ grows | Can diverge |

A convergence theorem must specify assumptions, step sizes, and which iterate or average is returned.

## 5. The basic convergence guarantee

Assume $f:\mathbb{R}^d\to\mathbb{R}$ is differentiable and convex, and has a minimizer $x^*$. Suppose

$$
\lVert x_0-x^*\rVert_2\leq D,
\qquad
\lVert \nabla f(x_t)\rVert_2\leq G
\quad \text{at every iterate used}.
$$

Here $D,G>0$ are known bounds used to choose the step size. Fix an iteration count $T$, use the same $\eta$ for all steps, and return the average of the points at which gradients were queried:

$$
\bar{x}_T=\frac{1}{T}\sum_{t=0}^{T-1}x_t.
$$

> **Theorem (gradient descent with bounded gradients).** For every constant step size $\eta>0$ satisfying the assumptions above,
>
> $$
> f(\bar{x}_T)-f(x^*)
> \leq
> \frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
> $$
>
> Choosing
>
> $$
> \eta=\frac{D}{G\sqrt{T}}
> $$
>
> gives
>
> $$
> f(\bar{x}_T)-f(x^*)\leq \frac{DG}{\sqrt{T}}.
> $$
>
> Thus
>
> $$
> T\geq \left(\frac{DG}{\varepsilon}\right)^2
> $$
>
> suffices for additive error $\varepsilon$.

### 5.1 Proof plan before the algebra

We cannot evaluate $x^*$, but we can use it in the analysis. Track the squared distance

$$
R_t=\lVert x_t-x^*\rVert_2^2.
$$

The update expands $R_{t+1}$ into $R_t$, a gradient-squared term, and an inner product. Convexity turns that inner product into $f(x_t)-f(x^*)$.

Our target one-step inequality is

$$
f(x_t)-f(x^*)
\leq
\frac{R_t-R_{t+1}}{2\eta}
+
\frac{\eta G^2}{2}.
$$

Summing makes the distance terms telescope. Convexity then turns a bound on the average function value into a bound at the average point:

$$
f\left(\frac{1}{T}\sum_{t=0}^{T-1}x_t\right)
\leq
\frac{1}{T}\sum_{t=0}^{T-1}f(x_t).
$$

This is the many-point version of the chord inequality.

### 5.2 Step 1: expand one update

Write $g_t=\nabla f(x_t)$. Then

$$
\begin{aligned}
R_{t+1}
&=\lVert x_t-\eta g_t-x^*\rVert_2^2\\
&=R_t-2\eta\langle g_t,x_t-x^*\rangle+\eta^2\lVert g_t\rVert_2^2\\
&\leq R_t-2\eta\bigl(f(x_t)-f(x^*)\bigr)+\eta^2G^2.
\end{aligned}
$$

The last line uses precisely the first-order convexity inequality and the gradient bound. Rearranging proves the target one-step inequality.

### 5.3 Step 2: telescope

Sum over $t=0,\ldots,T-1$:

$$
\begin{aligned}
\sum_{t=0}^{T-1}\bigl(f(x_t)-f(x^*)\bigr)
&\leq
\frac{1}{2\eta}\sum_{t=0}^{T-1}(R_t-R_{t+1})
+\frac{\eta G^2T}{2}\\
&=
\frac{R_0-R_T}{2\eta}
+\frac{\eta G^2T}{2}\\
&\leq
\frac{D^2}{2\eta}
+\frac{\eta G^2T}{2},
\end{aligned}
$$

because $R_0\leq D^2$ and $R_T\geq 0$. Dividing by $T$ and applying convexity to $\bar{x}_T$ proves the theorem.

### 5.4 Step 3: balance the two terms

For $\eta=D/(G\sqrt{T})$,

$$
\frac{D^2}{2\eta T}=\frac{DG}{2\sqrt{T}},
\qquad
\frac{\eta G^2}{2}=\frac{DG}{2\sqrt{T}}.
$$

A tiny step keeps the discretization term small but makes progress slow. A large step does the opposite. The chosen step size balances the two.

### A second valid output rule

If function values are available, choose

$$
\hat{t}\in\operatorname*{arg\,min}_{0\leq t<T} f(x_t)
$$

and return $\hat{x}=x_{\hat{t}}$. This best queried iterate satisfies the same bound, since its value is at most the average value. This argument does not establish the same bound for the last iterate.

## 6. Scope, caveats, and what comes next

### This is an additive approximation

The guarantee is

$$
f(x)-f(x^*)\leq \varepsilon,
$$

not a multiplicative approximation ratio. The latter can be inappropriate when $f(x^*)=0$ or is negative.

### Count the work per iteration

The theorem bounds gradient-oracle calls. Total time also includes the cost of a gradient evaluation and vector arithmetic. For dense least squares with $A\in\mathbb{R}^{m\times d}$, computing $A^\top(Ax-b)$ takes $O(md)$ time.

### The bounds are real assumptions

Convexity alone does not bound $D$ or $G$. For example, the gradient of $x^2/2$ is not bounded on all of $\mathbb{R}$. It is enough to bound gradients at the iterates, but the bound must be justified for the problem and step-size choice.

### A short extension to nonsmooth functions

A subgradient $g$ at $x$ satisfies

$$
f(y)\geq f(x)+\langle g,y-x\rangle
\qquad \text{for every }y.
$$

Replacing gradients by subgradients with $\lVert g_t\rVert_2\leq G$ leaves the proof unchanged. For $f(x)=|x|$, use

$$
g=
\begin{cases}
1, & x>0,\\
-1, & x<0,\\
\text{any }g\in[-1,1], & x=0.
\end{cases}
$$

This is a brief extension, not a new convergence proof.

### Why projection and smoothness are next

- A gradient step may leave a constrained feasible set $K$. We will project it back and preserve the distance analysis.
- A bounded gradient gives a $1/\sqrt{T}$ error bound. An upper bound on how rapidly the gradient changes will yield a faster $1/T$ guarantee.
- Lower as well as upper curvature bounds will give geometric convergence.

## Exercises

1. With $D=2$, $G=3$, and $T=900$, find the prescribed step size and the guaranteed additive error.
2. Show that the average of $T$ points in a convex set lies in that set. Then prove the many-point convexity inequality used in the analysis.
3. For $f(x)=x^2/2$, check the potential calculation directly when $\eta=1/2$. Which inequality in the general proof loses information specific to this quadratic?
