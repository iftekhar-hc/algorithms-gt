# Lecture 12 Study Guide: Convexity and Gradient Descent

The main intellectual move in the lecture is the transition from linear programming to nonlinear optimization while preserving **convexity**, the geometric property that keeps global optimization tractable. The lecture then develops gradient descent and proves an $O(1/\sqrt{T})$ convergence guarantee under bounded-distance and bounded-gradient assumptions.

---

## 1. Learning Objectives

After studying this lecture, you should be able to:

1. Define convex sets and convex functions.
2. Interpret convexity geometrically using chords and tangent planes.
3. Use the first-order characterization of differentiable convex functions.
4. Determine convexity using the Hessian when second derivatives exist.
5. Explain why every local minimum of a convex optimization problem is global.
6. Derive the gradient descent update.
7. Explain how the step size affects convergence.
8. Prove the bounded-gradient convergence theorem using:
   - a squared-distance potential,
   - the first-order convexity inequality,
   - telescoping sums,
   - convexity of the objective.
9. Distinguish guarantees for the average iterate, best iterate, and last iterate.
10. Extend the analysis from gradients to subgradients.

---

## 2. From Linear to Convex Optimization

A linear program optimizes a linear function over a convex feasible region. Convex optimization allows the objective to be nonlinear, but retains enough geometric structure to prevent misleading local minima. We consider

$$
\min_{x\in K} f(x),
$$

where:

- $K\subseteq \mathbb{R}^d$ is nonempty and convex,
- $f:K\to\mathbb{R}$ is convex,
- $x^\star$ denotes an optimal solution.

A feasible point $x$ is called $\varepsilon$-optimal when

$$
f(x)-f(x^\star)\leq \varepsilon.
$$

This is an **additive approximation guarantee**.

### 2.1 Convex Sets

A set $K$ is convex if the line segment joining any two points in $K$ remains entirely inside $K$:

$$
x,y\in K,\quad \lambda\in[0,1]
\quad\Longrightarrow\quad
\lambda x+(1-\lambda)y\in K.
$$

#### Visualization

```text
Convex set                         Nonconvex set

       * y                              * y
      /                                  \
     / entire segment                     \ segment leaves set
    / stays inside                         \
   * x                                      * x
```

Examples of convex sets include:

- intervals,
- Euclidean balls,
- half-spaces,
- affine subspaces,
- polyhedra and linear-programming feasible regions.

A union of two separated balls is generally not convex because the segment joining points in different balls can leave the union.

### 2.2 Convex Functions

A function $f$ is convex on $K$ if, for every $x,y\in K$ and $\lambda\in[0,1]$,

$$
f\bigl(\lambda x+(1-\lambda)y\bigr)
\leq
\lambda f(x)+(1-\lambda)f(y).
$$

Geometrically, the graph of a convex function lies **below every chord** joining two points on its graph.

```text
f(x)
 ^
 |        *
 |      /   chord
 |    /   /
 |  _/___/_
 | / convex curve
 +-----------------> x
```

At the midpoint, $\lambda=\frac12$, so

$$
f\left(\frac{x+y}{2}\right)
\leq
\frac{f(x)+f(y)}{2}.
$$

#### Example 1: A Quadratic

Let

$$
f(x)=x^2.
$$

For $\lambda\in[0,1]$,

$$
\begin{aligned}
&\lambda f(x)+(1-\lambda)f(y)
-f\bigl(\lambda x+(1-\lambda)y\bigr)\\
&=\lambda x^2+(1-\lambda)y^2
-\bigl(\lambda x+(1-\lambda)y\bigr)^2\\
&=\lambda(1-\lambda)(x-y)^2\geq 0.
\end{aligned}
$$

Therefore, $x^2$ is convex.

#### Example 2: Linear Functions

If $f(x)=c^\top x+b$, then

$$
f(\lambda x+(1-\lambda)y)
=
\lambda f(x)+(1-\lambda)f(y).
$$

Thus an affine function is both convex and concave. Consequently, maximizing $c^\top x$ is equivalent to minimizing the convex function $-c^\top x$.

---

## 3. The First-Order Characterization

For a differentiable function $f:\mathbb{R}^d\to\mathbb{R}$, convexity is equivalent to

$$
\boxed{
f(y)\geq f(x)+\left\langle\nabla f(x),y-x\right\rangle
}
$$

for every $x,y\in\mathbb{R}^d$.

The right-hand side is the first-order Taylor approximation of $f$ at $x$. Therefore:

> Every tangent plane of a differentiable convex function is a global lower bound.

### 3.1 Visualization

```text
f(z)
 ^
 |                         convex function
 |                       /
 |                    __/
 |                 __* y
 |              __/
 |           __* x
 |         /  /
 |_______/__/________________> z
        tangent line

The tangent line touches at x and remains below f everywhere.
```

### 3.2 Why the Inequality Follows from Convexity

For $0<\theta<1$, define

$$
z_\theta=x+\theta(y-x).
$$

Convexity gives

$$
f(z_\theta)
\leq
(1-\theta)f(x)+\theta f(y).
$$

Rearranging,

$$
f(y)-f(x)
\geq
\frac{f(x+\theta(y-x))-f(x)}{\theta}.
$$

Letting $\theta\downarrow 0$,

$$
f(y)-f(x)
\geq
\left\langle\nabla f(x),y-x\right\rangle.
$$

### 3.3 The Inequality Used in Gradient Descent

Put $y=x^\star$:

$$
f(x^\star)
\geq
f(x)+\left\langle\nabla f(x),x^\star-x\right\rangle.
$$

Rearranging,

$$
\boxed{
f(x)-f(x^\star)
\leq
\left\langle\nabla f(x),x-x^\star\right\rangle.
}
$$

This is the bridge between the quantity we want to control, $f(x)-f(x^\star)$, and the algebra generated by the gradient descent update.

#### Numerical Example

Let

$$
f(x)=\frac12x^2,\qquad x=2,\qquad y=1.
$$

Since $f'(x)=x$,

$$
f(y)=\frac12,
$$

while the tangent lower bound at $x=2$ is

$$
f(2)+f'(2)(1-2)=2+2(-1)=0.
$$

Indeed,

$$
\frac12\geq 0.
$$

---

## 4. Second-Order Characterization

If $f$ is twice continuously differentiable, then

$$
f\text{ is convex}
\quad\Longleftrightarrow\quad
\nabla^2 f(x)\succeq 0
$$

for every $x$, where $\nabla^2 f(x)$ is the Hessian.

Positive semidefiniteness means

$$
v^\top\nabla^2f(x)v\geq 0
$$

for every vector $v$. In one dimension, the condition becomes $f''(x)\geq0$.

### 4.1 Example: Least Squares

Consider

$$
f(x)=\frac12\|Ax-b\|_2^2.
$$

Then

$$
\nabla f(x)=A^\top(Ax-b)
$$

and

$$
\nabla^2f(x)=A^\top A.
$$

For every $v$,

$$
v^\top A^\top Av
=(Av)^\top(Av)
=\|Av\|_2^2
\geq0.
$$

Therefore $A^\top A$ is positive semidefinite and least squares is convex. Notice that $A^\top$, not $A$, appears in the gradient.

#### Small Numerical Example

Let

$$
A=\begin{bmatrix}1\\2\end{bmatrix},
\qquad
b=\begin{bmatrix}1\\0\end{bmatrix}.
$$

Then

$$
f(x)=\frac12\left[(x-1)^2+(2x)^2\right]
=\frac12(5x^2-2x+1).
$$

Therefore,

$$
f'(x)=5x-1,
\qquad
f''(x)=5>0.
$$

The unique minimizer satisfies

$$
5x^\star-1=0
\quad\Longrightarrow\quad
x^\star=\frac15.
$$

### 4.2 Convex but Nondifferentiable Functions

Differentiability is not part of the definition of convexity. Important nondifferentiable convex functions include

$$
f(x)=|x|
$$

and

$$
f(x)=\max_i(a_i^\top x+b_i).
$$

The absolute-value function is nondifferentiable at $x=0$, but it is still convex.

---

## 5. Why Local Minima Are Global

If $f$ is convex and $K$ is convex, every local minimum of $f$ over $K$ is a global minimum.

### Proof Idea

Suppose $x$ is a local minimum, but there is some $y\in K$ with

$$
f(y)<f(x).
$$

For $0<\theta\leq1$, let

$$
z_\theta=(1-\theta)x+\theta y.
$$

Because $K$ is convex, $z_\theta\in K$. By convexity of $f$,

$$
f(z_\theta)
\leq
(1-\theta)f(x)+\theta f(y)
<
f(x).
$$

As $\theta\to0$, $z_\theta\to x$. Thus there are better feasible points arbitrarily close to $x$, contradicting local optimality.

### Important Distinction

For an **unconstrained**, differentiable convex problem,

$$
\nabla f(x)=0
$$

certifies that $x$ is a global minimizer.

For a constrained problem, an optimum can lie on the boundary even when its gradient is nonzero. For example,

$$
\min_{x\in[0,1]}x
$$

has optimum $x^\star=0$, but $f'(0)=1$.

---

## 6. Gradient Descent

For unconstrained minimization, gradient descent starts from $x_0$ and repeats

$$
\boxed{
x_{t+1}=x_t-\eta\nabla f(x_t),
}
$$

where $\eta>0$ is the step size.

### 6.1 Why the Negative Gradient?

For a small displacement $h$,

$$
f(x+h)
=
f(x)+\left\langle\nabla f(x),h\right\rangle
+o(\|h\|_2).
$$

Suppose $\|h\|_2\leq\rho$. By Cauchy-Schwarz,

$$
\left\langle\nabla f(x),h\right\rangle
\geq
-\rho\|\nabla f(x)\|_2.
$$

Equality occurs when

$$
h=-\rho\frac{\nabla f(x)}{\|\nabla f(x)\|_2}.
$$

Thus $-\nabla f(x)$ is the direction of greatest first-order decrease per unit Euclidean distance. The direction tells us **where** to move. The step size tells us **how far** to move.

### 6.2 Step-Size Example

Let

$$
f(x)=\frac12x^2.
$$

Then $\nabla f(x)=x$, so gradient descent becomes

$$
x_{t+1}=x_t-\eta x_t=(1-\eta)x_t.
$$

Therefore,

$$
x_t=(1-\eta)^t x_0.
$$

- If $0<\eta<1$, the sequence converges without changing signs.
- If $\eta=1$, the sequence reaches $0$ after one update.
- If $1<\eta<2$, the sequence oscillates while converging.
- If $\eta=2$, it oscillates with constant magnitude.
- If $\eta>2$, it diverges.

For example, with $x_0=2$ and $\eta=\frac12$,

$$
2,\;1,\;\frac12,\;\frac14,\;\frac18,\ldots
$$

```text
x*=0      x3      x2          x1                  x0
 |---------*-------*-----------*-------------------*
 0        0.25    0.5          1                   2
```

---

## 7. Gradient Descent Pseudocode

```text
Algorithm: Gradient Descent with Averaged Output

Input:
    differentiable convex function f
    gradient oracle grad_f
    initial point x_0
    step size eta > 0
    iteration count T

x <- x_0
sum <- zero vector

for t = 0, 1, ..., T - 1:
    sum <- sum + x
    g <- grad_f(x)
    x <- x - eta * g

x_bar <- sum / T
return x_bar
```

The average is formed from the points where gradients were queried:

$$
\bar{x}_T=\frac1T\sum_{t=0}^{T-1}x_t.
$$

Do not accidentally include $x_T$ while still dividing by $T$.

---

## 8. Basic Convergence Theorem

Assume:

1. $f:\mathbb{R}^d\to\mathbb{R}$ is differentiable and convex.
2. A minimizer $x^\star$ exists.
3. The initial distance is bounded:

   $$
   \|x_0-x^\star\|_2\leq D.
   $$

4. Every gradient queried by the algorithm is bounded:

   $$
   \|\nabla f(x_t)\|_2\leq G.
   $$

5. A constant step size $\eta$ is used for $T$ iterations.

Then the averaged iterate satisfies

$$
\boxed{
f(\bar{x}_T)-f(x^\star)
\leq
\frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
}
$$

Choosing

$$
\boxed{
\eta=\frac{D}{G\sqrt{T}}
}
$$

gives

$$
\boxed{
f(\bar{x}_T)-f(x^\star)
\leq
\frac{DG}{\sqrt{T}}.
}
$$

Therefore, to guarantee additive error at most $\varepsilon$, it is sufficient to use

$$
\boxed{
T\geq\left(\frac{DG}{\varepsilon}\right)^2.
}
$$

This is an $O(1/\sqrt{T})$ convergence rate, or equivalently an $O(1/\varepsilon^2)$ iteration complexity.

---

## 9. Proof of the Convergence Theorem

### Step 1: Select a Potential Function

Define

$$
R_t=\|x_t-x^\star\|_2^2.
$$

This measures squared distance to an optimum. We need not know or compute $x^\star$; it is used only in the analysis.

Let

$$
g_t=\nabla f(x_t).
$$

The update is

$$
x_{t+1}=x_t-\eta g_t.
$$

### Step 2: Expand One Update

$$
\begin{aligned}
R_{t+1}
&=\|x_{t+1}-x^\star\|_2^2\\
&=\|x_t-\eta g_t-x^\star\|_2^2\\
&=\|x_t-x^\star\|_2^2
 -2\eta\langle g_t,x_t-x^\star\rangle
 +\eta^2\|g_t\|_2^2\\
&=R_t
 -2\eta\langle g_t,x_t-x^\star\rangle
 +\eta^2\|g_t\|_2^2.
\end{aligned}
$$

By convexity,

$$
f(x_t)-f(x^\star)
\leq
\langle g_t,x_t-x^\star\rangle.
$$

Using $\|g_t\|_2\leq G$,

$$
R_{t+1}
\leq
R_t-2\eta\bigl(f(x_t)-f(x^\star)\bigr)+\eta^2G^2.
$$

Rearranging,

$$
\boxed{
f(x_t)-f(x^\star)
\leq
\frac{R_t-R_{t+1}}{2\eta}
+\frac{\eta G^2}{2}.
}
$$

This is the crucial one-step inequality.

### Step 3: Sum and Telescope

Sum from $t=0$ to $T-1$:

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^\star)\bigr)
\leq
\frac{1}{2\eta}
\sum_{t=0}^{T-1}(R_t-R_{t+1})
+\frac{\eta G^2T}{2}.
$$

The potential terms telescope:

$$
(R_0-R_1)+(R_1-R_2)+\cdots+(R_{T-1}-R_T)
=R_0-R_T.
$$

Because $R_T\geq0$ and $R_0\leq D^2$,

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^\star)\bigr)
\leq
\frac{D^2}{2\eta}+\frac{\eta G^2T}{2}.
$$

Divide by $T$:

$$
\frac1T\sum_{t=0}^{T-1}f(x_t)-f(x^\star)
\leq
\frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
$$

### Step 4: Use Convexity on the Average Iterate

Because $f$ is convex,

$$
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)
\leq
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

Hence,

$$
f(\bar{x}_T)-f(x^\star)
\leq
\frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
$$

### Step 5: Choose the Step Size

The bound contains two competing terms:

$$
\underbrace{\frac{D^2}{2\eta T}}_{\text{large if }\eta\text{ is too small}}
+
\underbrace{\frac{\eta G^2}{2}}_{\text{large if }\eta\text{ is too large}}.
$$

Balance them:

$$
\frac{D^2}{2\eta T}
=
\frac{\eta G^2}{2}.
$$

This gives

$$
D^2=\eta^2G^2T
\quad\Longrightarrow\quad
\eta=\frac{D}{G\sqrt{T}}.
$$

Substituting this value gives

$$
f(\bar{x}_T)-f(x^\star)
\leq
\frac{DG}{2\sqrt{T}}+\frac{DG}{2\sqrt{T}}
=
\frac{DG}{\sqrt{T}}.
$$

---

## 10. Worked Example from the Lecture

Given

$$
D=2,\qquad G=3,\qquad T=900,
$$

the prescribed step size is

$$
\eta=\frac{D}{G\sqrt{T}}
=\frac{2}{3\sqrt{900}}
=\frac{2}{3\cdot30}
=\frac1{45}.
$$

The guaranteed additive error is

$$
\frac{DG}{\sqrt{T}}
=
\frac{2\cdot3}{30}
=
\frac15
=
0.2.
$$

Therefore,

$$
\boxed{
\eta=\frac1{45},\qquad
f(\bar{x}_{900})-f(x^\star)\leq0.2.
}
$$

---

## 11. Average, Best, and Last Iterates

The proof directly establishes a guarantee for

$$
\bar{x}_T=\frac1T\sum_{t=0}^{T-1}x_t.
$$

If function values are available, we can instead return the best queried point

$$
\hat{x}\in
\operatorname*{arg\,min}_{0\leq t<T}f(x_t).
$$

Because a minimum is no greater than an average,

$$
f(\hat{x})
\leq
\frac1T\sum_{t=0}^{T-1}f(x_t),
$$

so $\hat{x}$ satisfies the same bound.

However, this proof does **not** establish that the last iterate $x_T$ satisfies the same bound. A theorem about an optimization method must identify exactly what output is being analyzed.

---

## 12. Nonsmooth Extension

A vector $g$ is a subgradient of $f$ at $x$ if

$$
f(y)\geq f(x)+\langle g,y-x\rangle
$$

for every $y$.

If $g_t$ is a subgradient at $x_t$, then we may use

$$
x_{t+1}=x_t-\eta g_t.
$$

Provided $\|g_t\|_2\leq G$, the same potential-function proof applies.

### Example: $f(x)=|x|$

A valid subgradient is

$$
g(x)=
\begin{cases}
1, & x>0,\\
-1, & x<0,\\
\text{any value in }[-1,1], & x=0.
\end{cases}
$$

Thus subgradient descent can optimize convex functions even where no ordinary gradient exists.

---

## 13. Scope and Caveats

### 13.1 Additive, Not Multiplicative, Approximation

The theorem guarantees

$$
f(x)-f(x^\star)\leq\varepsilon,
$$

not a ratio such as $f(x)/f(x^\star)$. Multiplicative approximation is problematic when $f(x^\star)=0$ or $f(x^\star)<0$.

### 13.2 Oracle Complexity Is Not Total Runtime

The theorem counts gradient evaluations. Actual running time also includes:

- computing the gradient,
- vector additions,
- scalar-vector multiplication,
- storage and averaging.

For dense least squares with $A\in\mathbb{R}^{m\times d}$, computing

$$
A^\top(Ax-b)
$$

takes $O(md)$ time. Thus $T$ iterations require approximately $O(Tmd)$ arithmetic time.

### 13.3 Convexity Does Not Imply Bounded Gradients

For

$$
f(x)=\frac12x^2,
$$

the gradient is $f'(x)=x$, which is unbounded over $\mathbb{R}$.

The theorem only requires the gradients at the iterates to be bounded, but that bound must be separately established.

### 13.4 Constraints Require Projection

For a constrained problem, a gradient update can leave $K$. The standard correction is projected gradient descent:

$$
x_{t+1}
=
\Pi_K\left(x_t-\eta\nabla f(x_t)\right),
$$

where $\Pi_K$ returns the closest point in $K$.

### 13.5 Stronger Assumptions Produce Faster Rates

```text
bounded subgradients
        |
        v
  O(1/sqrt(T))

smooth gradients
        |
        v
     O(1/T)

smooth + strongly convex
        |
        v
 geometric convergence
```

The present lecture proves only the first of these guarantees.

---

## 14. Concept Map

```text
Convex feasible set K
        +
Convex objective f
        |
        v
Local minimum = global minimum
        |
        v
First-order inequality
f(x)-f(x*) <= <grad f(x), x-x*>
        |
        v
Gradient descent update
x_(t+1) = x_t - eta grad f(x_t)
        |
        v
Squared-distance potential
R_t = ||x_t-x*||^2
        |
        v
One-step progress inequality
        |
        v
Telescoping sum
        |
        v
Average-iterate guarantee
f(x_bar_T)-f(x*) <= D^2/(2 eta T) + eta G^2/2
        |
        v
Choose eta = D/(G sqrt(T))
        |
        v
Error <= DG/sqrt(T)
```

---

## 15. Common Mistakes

1. **Reversing the chord inequality**

   For convex $f$,

   $$
   f(\lambda x+(1-\lambda)y)
   \leq
   \lambda f(x)+(1-\lambda)f(y).
   $$

2. **Reversing the tangent inequality**

   A tangent plane is a lower bound:

   $$
   f(y)\geq f(x)+\langle\nabla f(x),y-x\rangle.
   $$

3. **Assuming every convex function is differentiable**

   The function $|x|$ is convex but nondifferentiable at $0$.

4. **Assuming a constrained optimum has zero gradient**

   Boundary optima can have nonzero gradients.

5. **Forgetting the transpose in least squares**

   $$
   \nabla\left(\frac12\|Ax-b\|^2\right)
   =A^\top(Ax-b).
   $$

6. **Claiming the theorem applies to the last iterate**

   The proof applies to the average iterate and, with function values, the best queried iterate.

7. **Assuming convexity implies bounded gradients**

   It does not.

8. **Using the optimized step size without knowing $T$**

   The choice

   $$
   \eta=\frac{D}{G\sqrt{T}}
   $$

   depends on the intended iteration count.

---

## 16. Quiz Questions

### Multiple Choice

#### Q1

Which inequality characterizes differentiable convex functions?

A. $f(y)\leq f(x)+\langle\nabla f(x),y-x\rangle$

B. $f(y)\geq f(x)+\langle\nabla f(x),y-x\rangle$

C. $f(y)=f(x)+\langle\nabla f(x),y-x\rangle$

D. $f(y)\geq f(x)+\|\nabla f(x)\|^2$

**Answer:** B.

#### Q2

Which statement is always true for a convex optimization problem?

A. Every stationary point is a strict minimum.

B. Every local minimum is a global minimum.

C. Every convex function has a unique minimizer.

D. The gradient is bounded.

**Answer:** B.

#### Q3

Suppose $f(x)=x^2/2$. For which step size does gradient descent oscillate without decreasing the magnitude?

A. $\eta=1/2$

B. $\eta=1$

C. $\eta=2$

D. $\eta=3$

**Answer:** C, because $x_{t+1}=-x_t$.

#### Q4

Under the lecture's assumptions, the optimized convergence guarantee is:

A. $O(1/T^2)$

B. $O(1/T)$

C. $O(1/\sqrt{T})$

D. $O(\log T)$

**Answer:** C.

#### Q5

Which point is directly guaranteed by the proof?

A. Only $x_T$

B. The average of $x_0,\ldots,x_{T-1}$

C. A randomly selected infeasible point

D. Only $x_0$

**Answer:** B.

### Short-Answer Quiz

#### Q6

Why is the first-order inequality essential in the convergence proof?

**Answer:** It converts the inner product

$$
\langle\nabla f(x_t),x_t-x^\star\rangle
$$

arising from the squared-distance expansion into an upper bound on the objective error

$$
f(x_t)-f(x^\star).
$$

#### Q7

Why does the sum $\sum_t(R_t-R_{t+1})$ telescope?

**Answer:** Every intermediate term appears once positively and once negatively, leaving only $R_0-R_T$.

#### Q8

Why do we return an average iterate?

**Answer:** The proof controls the average of the function values. Convexity allows us to convert that into a bound on the function value at the average point:

$$
f(\bar{x}_T)
\leq
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

#### Q9

Is $\nabla f(x)=0$ necessary at a constrained optimum?

**Answer:** No. An optimum on the boundary can have a nonzero gradient.

#### Q10

If $D=4$, $G=5$, and $T=400$, find the prescribed step size and error guarantee.

**Answer:**

$$
\eta=\frac{4}{5\sqrt{400}}
=\frac{4}{100}
=0.04,
$$

and

$$
f(\bar{x}_T)-f(x^\star)
\leq
\frac{4\cdot5}{20}
=1.
$$

---

## 17. Exam-Style Questions

### Problem 1: Proving Convexity

Let

$$
f(x)=\|Ax-b\|_2^2.
$$

1. Compute $\nabla f(x)$.
2. Compute $\nabla^2 f(x)$.
3. Prove that $f$ is convex.
4. State when $f$ is strictly convex.

#### Solution Outline

$$
\nabla f(x)=2A^\top(Ax-b),
$$

and

$$
\nabla^2f(x)=2A^\top A.
$$

For every $v$,

$$
v^\top\nabla^2f(x)v
=2\|Av\|_2^2\geq0.
$$

Thus $f$ is convex. It is strictly convex when $A^\top A$ is positive definite, equivalently when $A$ has full column rank.

### Problem 2: First-Order Optimality

Suppose $f:\mathbb{R}^d\to\mathbb{R}$ is differentiable and convex. Prove that if

$$
\nabla f(\hat{x})=0,
$$

then $\hat{x}$ is a global minimizer.

#### Solution Outline

For every $y$,

$$
f(y)
\geq
f(\hat{x})+
\left\langle\nabla f(\hat{x}),y-\hat{x}\right\rangle
=
f(\hat{x}).
$$

Therefore no point has a lower objective value.

### Problem 3: Full Convergence Proof

Assume

$$
\|x_0-x^\star\|\leq D,
\qquad
\|\nabla f(x_t)\|\leq G.
$$

Starting from

$$
x_{t+1}=x_t-\eta\nabla f(x_t),
$$

prove

$$
f(\bar{x}_T)-f(x^\star)
\leq
\frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
$$

Your proof must explicitly identify:

1. the potential function,
2. the use of convexity,
3. the telescoping sum,
4. the use of convexity at the average point.

#### Grading Focus

- Correct expansion of squared distance.
- Correct direction of the first-order inequality.
- Correct telescope from $R_0$ to $R_T$.
- Correct definition of $\bar{x}_T$.

### Problem 4: Complexity Calculation

Suppose $D=10$, $G=4$, and the desired additive error is $\varepsilon=0.1$.

1. Find a sufficient number of iterations.
2. Find the corresponding constant step size.

#### Solution

$$
T\geq
\left(\frac{DG}{\varepsilon}\right)^2
=
\left(\frac{10\cdot4}{0.1}\right)^2
=
400^2
=
160{,}000.
$$

Using $T=160{,}000$,

$$
\eta
=
\frac{10}{4\sqrt{160{,}000}}
=
\frac{10}{4\cdot400}
=
\frac1{160}.
$$

### Problem 5: Constrained Stationarity Counterexample

Give an example of a differentiable convex function and convex feasible set for which the constrained minimizer has nonzero gradient.

#### Solution

Take

$$
f(x)=x,\qquad K=[0,1].
$$

The minimizer is $x^\star=0$, but

$$
f'(0)=1\neq0.
$$

This does not contradict unconstrained first-order optimality because movement in the negative-gradient direction is infeasible at $x=0$.

### Problem 6: Many-Point Convexity

Let $x_1,\ldots,x_n\in K$, where $K$ is convex, and let

$$
\lambda_i\geq0,
\qquad
\sum_{i=1}^n\lambda_i=1.
$$

Prove:

1. $\sum_i\lambda_i x_i\in K$.
2. If $f$ is convex, then

   $$
   f\left(\sum_i\lambda_i x_i\right)
   \leq
   \sum_i\lambda_i f(x_i).
   $$

#### Hint

Use induction on $n$. This result is often called the finite form of Jensen's inequality.

### Problem 7: Identify Where the General Proof Is Loose

For

$$
f(x)=\frac12x^2,\qquad \eta=\frac12,
$$

compute $x_t$ exactly and compare the actual objective error with the theorem's $O(1/\sqrt T)$ guarantee.

#### Solution Outline

The exact recurrence is

$$
x_{t+1}=\frac12x_t,
$$

so

$$
x_t=2^{-t}x_0
$$

and

$$
f(x_t)=\frac12\,4^{-t}x_0^2.
$$

Thus the individual iterates converge geometrically, much faster than $1/\sqrt T$.

The general proof loses problem-specific information when it replaces

$$
\|\nabla f(x_t)\|^2
$$

by the uniform upper bound $G^2$. It also does not exploit smoothness or strong convexity.

---

## 18. Further Textbook References

1. **Stephen Boyd and Lieven Vandenberghe, _Convex Optimization_.**  
   Recommended topics include convex sets, convex functions, first-order conditions, least squares, duality, and numerical algorithms.

2. **Sébastien Bubeck, _Convex Optimization: Algorithms and Complexity_.**  
   Particularly relevant for the black-box oracle model, projected subgradient descent, smooth gradient descent, strong convexity, and accelerated methods.

3. **Yurii Nesterov, _Lectures on Convex Optimization_, 2nd ed.**  
   Recommended for a rigorous treatment of first-order methods, smooth convex optimization, strong convexity, acceleration, and complexity bounds.

### Suggested Reading Order

1. Boyd and Vandenberghe for geometric intuition and foundational definitions.
2. Bubeck for an algorithmic and complexity-oriented presentation.
3. Nesterov for deeper theory, smoothness, strong convexity, and accelerated optimization.

---

## Final Takeaway

The complete proof can be remembered as one chain:

$$
\boxed{
\text{convexity}
\Rightarrow
\text{tangent lower bound}
\Rightarrow
\text{objective error as an inner product}
\Rightarrow
\text{squared-distance potential}
\Rightarrow
\text{telescoping}
\Rightarrow
O(1/\sqrt{T}).
}
$$

The most important proof skill is not memorizing the final rate. It is recognizing how the update suggests a potential function and how convexity converts the resulting algebra into progress in objective value.


## Video Lectures
Based on the lecture note, you need resources that cover **convex sets and functions, first-order optimality, gradient descent, convergence proofs, subgradients, and constrained optimization**. I’d use one complete course as the backbone, then add a few shorter videos for intuition.

## Best overall course

### Stanford EE364A: Convex Optimization I

**Instructor:** Stephen Boyd  
**Level:** Intermediate to advanced  
**Best for:** A rigorous, comprehensive treatment with strong geometric intuition and applications.

The updated course consists of 18 lectures of roughly 75–80 minutes each. It covers convex sets, convex functions, convex optimization problems, duality, optimality conditions, numerical methods, and applications in machine learning, statistics, engineering, control, and finance. [[youtube.com]](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h)

- [2023 course playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h)
- [Lecture 1](https://www.youtube.com/watch?v=kV1ru-Inzl4)
- [Older complete 37-video collection](https://www.youtube.com/playlist?list=PL4DA205E607D8DBCB)

### Why I recommend it

It pairs naturally with:

> Stephen Boyd and Lieven Vandenberghe, _Convex Optimization_

It is especially strong for:

- recognizing convex problems;
- developing geometric intuition;
- convex sets and functions;
- least-squares and quadratic optimization;
- optimality conditions;
- Lagrange duality;
- Newton and interior-point methods;
- applications of convex optimization.

### Limitation

The course treats much more than gradient descent. If your immediate goal is specifically to understand the O(1/T)O(1/\sqrt{T})O(1/T​) proof from the lecture note, combine it with a first-order methods lecture below.

---

## Best focused material for gradient descent

### MIT: Gradient Descent, Lecture 7

**Instructor:** Gabriele Farina  
**Course:** MIT 6.7220/15.084, Nonlinear Optimization  
**Level:** Intermediate  
**Best for:** A precise mathematical treatment of gradient descent and smoothness.

The lecture begins with the update

xt+1=xt−η∇f(xt)x_{t+1}=x_t-\eta\nabla f(x_t)xt+1​=xt​−η∇f(xt​)

and develops the analysis using LLL-smoothness, including why the negative gradient is useful and how the step size determines convergence. [[mit.edu]](https://www.mit.edu/~gfarina/2024/67220s24_L07_gradient_descent/L07.pdf)

The accompanying notes are particularly useful when reviewing:

- first-order models;
    
- steepest descent;
    
- LLL-Lipschitz gradients;
    
- the descent lemma;
    
- step-size restrictions;
    
- convergence on convex and strongly convex objectives.
    
- [MIT Gradient Descent lecture notes](https://www.mit.edu/~gfarina/2024/67220s24_L07_gradient_descent/L07.pdf)
    

This is the best follow-up after understanding the bounded-gradient proof in your lecture note, because it introduces the stronger **smooth-function analysis** commonly used for gradient descent.

---

## Best course structure with freely available notes

### MIT OpenCourseWare: Introduction to Convex Optimization

**Course:** MIT 6.079  
**Level:** Advanced undergraduate or beginning graduate  
**Best for:** Systematic study with lecture notes, exercises, and exams.

The course progresses from convex sets and functions through duality, applications, unconstrained minimization, constrained minimization, and interior-point methods. Lecture 16 specifically covers gradient methods, steepest descent, Newton’s method, and convergence analysis. [[ocw.mit.edu]](https://ocw.mit.edu/courses/6-079-introduction-to-convex-optimization-fall-2009/pages/lecture-notes/)

- [MIT course lecture notes](https://ocw.mit.edu/courses/6-079-introduction-to-convex-optimization-fall-2009/pages/lecture-notes/)

### Relevant sequence

1. Lecture 1: Introduction to optimization
2. Lecture 2: Convex sets
3. Lecture 3: Convex functions
4. Lecture 4: Convex optimization problems
5. Lecture 5: Duality
6. Lecture 16: Gradient and steepest-descent methods
7. Lecture 17: Equality-constrained minimization
8. Lecture 18: Interior-point methods

Although this resource is primarily notes rather than a polished video playlist, it is an excellent companion to video lectures because the sequence aligns closely with a standard graduate optimization course. [[ocw.mit.edu]](https://ocw.mit.edu/courses/6-079-introduction-to-convex-optimization-fall-2009/pages/lecture-notes/)

---

## Best for subgradients and advanced first-order methods

### Stanford EE364B: Convex Optimization II

**Instructor:** Stephen Boyd and course collaborators  
**Level:** Advanced  
**Best for:** Subgradient methods, proximal methods, ADMM, mirror descent, and distributed optimization.

This is the natural continuation after EE364A. The course materials include subgradient methods, stochastic subgradient descent, mirror descent, proximal algorithms, operator splitting, ADMM, cutting-plane methods, and Newton-type methods. [[web.stanford.edu]](https://web.stanford.edu/class/ee364b/videos.html), [[web.stanford.edu]](https://web.stanford.edu/class/ee364b/lectures.html)

- [Stanford EE364B lecture videos](https://web.stanford.edu/class/ee364b/videos.html)
- [Stanford EE364B notes and slides](https://web.stanford.edu/class/ee364b/lectures.html)

This course is particularly relevant to the nondifferentiable extension in your note:

xt+1=xt−ηgt,gt∈∂f(xt).x_{t+1}=x_t-\eta g_t, \qquad g_t\in\partial f(x_t).xt+1​=xt​−ηgt​,gt​∈∂f(xt​).

Start with these topics:

1. Subgradients
2. Subgradient methods
3. Constrained subgradient methods
4. Stochastic subgradient methods
5. Mirror descent
6. Proximal algorithms

---

## Best alternative full course

### NPTEL: Convex Optimization

**Instructor:** Joydeep Dutta, IIT Kanpur  
**Level:** Intermediate to advanced  
**Best for:** A slower, mathematically detailed presentation.

The NPTEL course has 42 lectures, generally around 35–60 minutes each. It provides a sustained mathematical treatment and is useful if the pace of Stanford EE364A feels too fast. [[youtube.com]](https://www.youtube.com/playlist?list=PLbMVogVj5nJQHFqfiSdgaLCCWvDcm1W4l)

- [NPTEL Convex Optimization playlist](https://www.youtube.com/playlist?list=PLbMVogVj5nJQHFqfiSdgaLCCWvDcm1W4l)

A shorter 17-video NPTEL playlist is also available, though the 42-lecture course is the more complete option. [[youtube.com]](https://www.youtube.com/playlist?list=PL6KtZi1OAytXlHqAlsq6eNqMl7ITONS1k)

---

## Shorter supplementary videos

### Convex optimization and gradient descent overview

This seven-minute video provides a quick review of the connection between convexity and gradient descent. It is useful as a preview, but not as a replacement for a full lecture. [[youtube.com]](https://www.youtube.com/watch?v=38U0eLSyXGA)

[](https://www.youtube.com/watch?v=38U0eLSyXGA)

[![](https://ts4.mm.bing.net/th?id=OVP.wrjiPwRw2n1xTQICojza1gEsDh&pid=15.1&w=313&h=176&c=7&dpr=2)07:23](https://www.youtube.com/watch?v=38U0eLSyXGA)

[[W2-1] Convex Optimization and Gradient Descent](https://www.youtube.com/watch?v=38U0eLSyXGA)

[Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.](https://www.youtube.com/watch?v=38U0eLSyXGA)

### Convex functions and gradient-descent analysis

This longer lecture covers convex-function properties, subgradients, smoothness, strong convexity, and convergence analysis for gradient descent. The gradient-descent discussion begins after the initial convexity review. [[youtube.com]](https://www.youtube.com/watch?v=WFzRb-Nd--c)

[](https://www.youtube.com/watch?v=WFzRb-Nd--c)

[![](https://ts2.mm.bing.net/th?id=OVP.Sl04_YdpUzJa4iyvC_QsAAHgFo&pid=15.1&w=313&h=176&c=7&dpr=2)02:54:50](https://www.youtube.com/watch?v=WFzRb-Nd--c)

[Optimization in Machine Learning: Lecture 2 (Convex Functions Cont, Analysis of Gradient Descent)](https://www.youtube.com/watch?v=WFzRb-Nd--c)

[Optimization in Machine Learning: Lecture 2 - Continuation of Convex Functions: Properties, Examples, Global Miniman and Local Minima - Analysis of Gradient Descent for Convex Functions: Lipschitz Continuous, Smooth, and Strongly Convex cases](https://www.youtube.com/watch?v=WFzRb-Nd--c)

---

# Recommended learning path

## Fast path: approximately 8–10 hours

Use this if your goal is to understand the attached lecture note and solve related exam problems.

### Stage 1: Convexity foundations

Watch the early Stanford EE364A lectures covering:

- convex sets;
- convex functions;
- first-order characterization;
- convex optimization problems. [[youtube.com]](https://www.youtube.com/watch?v=2H4_7izio9Y), [[youtube.com]](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h)

While watching, make sure you can prove:

f(y)≥f(x)+∇f(x)⊤(y−x)f(y)\ge f(x)+\nabla f(x)^\top(y-x)f(y)≥f(x)+∇f(x)⊤(y−x)

and derive:

f(x)−f(x⋆)≤∇f(x)⊤(x−x⋆).f(x)-f(x^\star) \le \nabla f(x)^\top(x-x^\star).f(x)−f(x⋆)≤∇f(x)⊤(x−x⋆).

### Stage 2: Gradient descent

Study the MIT gradient-descent lecture alongside the provided notes. Focus on the role of smoothness and why a step size such as η≤1/L\eta\le 1/Lη≤1/L arises in the smooth setting. [[mit.edu]](https://www.mit.edu/~gfarina/2024/67220s24_L07_gradient_descent/L07.pdf)

### Stage 3: Reconstruct the convergence proof

Without looking at the solution, derive:

∥xt+1−x⋆∥2=∥xt−x⋆∥2−2η⟨∇f(xt),xt−x⋆⟩+η2∥∇f(xt)∥2.\|x_{t+1}-x^\star\|^2 = \|x_t-x^\star\|^2 -2\eta\langle\nabla f(x_t),x_t-x^\star\rangle +\eta^2\|\nabla f(x_t)\|^2.∥xt+1​−x⋆∥2=∥xt​−x⋆∥2−2η⟨∇f(xt​),xt​−x⋆⟩+η2∥∇f(xt​)∥2.

Then combine it with convexity, telescope over ttt, and use Jensen’s inequality to prove:

f(xˉT)−f(x⋆)≤D22ηT+ηG22.f(\bar x_T)-f(x^\star) \le \frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.f(xˉT​)−f(x⋆)≤2ηTD2​+2ηG2​.

### Stage 4: Nonsmooth extension

Use the EE364B subgradient materials to understand why the same proof works with

gt∈∂f(xt)g_t\in\partial f(x_t)gt​∈∂f(xt​)

when ∥gt∥≤G\|g_t\|\le G∥gt​∥≤G. [[web.stanford.edu]](https://web.stanford.edu/class/ee364b/lectures.html)

---

## Complete path: approximately 30–40 hours

1. Watch all of Stanford EE364A.
2. Solve exercises from the Boyd–Vandenberghe textbook.
3. Study MIT’s gradient and Newton method notes.
4. Continue with Stanford EE364B:
    - subgradient methods;
    - projected methods;
    - proximal methods;
    - mirror descent;
    - ADMM. [[ocw.mit.edu]](https://ocw.mit.edu/courses/6-079-introduction-to-convex-optimization-fall-2009/pages/lecture-notes/), [[web.stanford.edu]](https://web.stanford.edu/class/ee364b/lectures.html), [[youtube.com]](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h)

---

# My prioritized recommendation

If you choose only three resources:

1. **Stanford EE364A 2023** for the complete conceptual foundation. [[youtube.com]](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h)
2. **MIT Gradient Descent Lecture 7** for a focused convergence analysis. [[mit.edu]](https://www.mit.edu/~gfarina/2024/67220s24_L07_gradient_descent/L07.pdf)
3. **Stanford EE364B subgradient materials** for the nonsmooth extension and advanced first-order methods. [[web.stanford.edu]](https://web.stanford.edu/class/ee364b/lectures.html)

A particularly effective study pattern is to watch one Stanford lecture, read the corresponding textbook section, and then reproduce one proof entirely from memory. That will reinforce the mathematical structure much more effectively than watching the playlist continuously.
