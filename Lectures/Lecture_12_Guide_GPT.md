# Lecture 12 Study Guide: Convexity and Gradient Descent

Your lecture explains why **convexity** makes nonlinear optimization manageable and how to prove a basic convergence guarantee for gradient descent. Its central result is:

$$
\boxed{
f(\bar x_T)-f(x^*)\le \frac{DG}{\sqrt T}
}
$$

Here, $D$ bounds the initial distance to an optimum, $G$ bounds gradient norms at the queried points, and $\bar x_T$ is the average of those points. The guarantee requires specific assumptions and a particular step size—not just convexity alone. [Lecture notes](#source-notes)

Below, I follow the lecture’s progression, explain the proof step by step, and add worked examples, text-based visualizations, pseudocode, a quiz, and a 100-point practice exam with solutions.

---

## 1. The big picture: from linear to nonlinear optimization

### 1.1 The optimization problem

We want to solve

$$
\min_{x\in K} f(x),
$$

where:

- $x\in\mathbb R^d$ is the decision vector.
- $K\subseteq\mathbb R^d$ is a nonempty convex feasible set.
- $f$ is the objective function.
- $x^*$ denotes a minimizer, assumed to exist.

An $\varepsilon$-optimal answer is a feasible point $x$ satisfying

$$
f(x)-f(x^*)\le \varepsilon.
$$

This measures objective-value error, not necessarily distance from the optimizer. [Lecture notes](#source-notes)

For example, if

$$
f(x)=(x-3)^2,
$$

then $x^*=3$. Returning $x=3.1$ gives

$$
f(3.1)-f(3)=0.01.
$$

Thus, $3.1$ is a $0.01$-optimal solution.

### 1.2 How this extends linear programming

A linear program has a linear objective and a convex feasible region. Convex optimization allows the objective to be nonlinear while retaining convexity. For example:

| Problem | Objective | Feasible set |
|---|---|---|
| Linear programming | $c^\top x$ | Linear constraints |
| Least squares | $\frac12\lVert Ax-b\rVert _2^2$ | Often $\mathbb R^d$ |
| Constrained least squares | $\frac12\lVert Ax-b\rVert _2^2$ | A convex set $K$ |

A maximization LP can be written as a convex minimization problem because

$$
\max_{x\in K}c^\top x
\quad\Longleftrightarrow\quad
\min_{x\in K}-c^\top x.
$$

Linear functions are both convex and concave. [Lecture notes](#source-notes) [Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

### 1.3 The oracle viewpoint

The algorithm can query:

$$
f(x)
\qquad\text{and}\qquad
\nabla f(x).
$$

A convergence theorem counts how many queries are sufficient. Actual runtime also depends on the cost of each query and the vector operations used to update $x$. [Lecture notes](#source-notes)

---

## 2. Convex sets and convex functions

### 2.1 A convex set contains every segment between its points

A set $K$ is convex if

$$
x,y\in K,\quad \lambda\in[0,1]
\quad\Longrightarrow\quad
\lambda x+(1-\lambda)y\in K.
$$

Geometrically:

```text
Convex set                     Nonconvex set

   __________                    ____      ____
  /          \                  /    \    /    \
 |  x------y  |                |  x---outside---y |
  \__________/                  \____/    \____/

The entire segment             Some of the segment
remains feasible.              leaves the set.
```

Intervals, balls, and regions defined by linear inequalities are convex. Convexity of the feasible set matters because it ensures that averages of feasible points remain feasible. [Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

### 2.2 A convex function lies below its chords

A function $f$ is convex on a convex set $K$ if

$$
f(\lambda x+(1-\lambda)y)
\le
\lambda f(x)+(1-\lambda)f(y)
$$

for every $x,y\in K$ and $\lambda\in[0,1]$. [Lecture notes](#source-notes)

The two sides represent different operations:

| Expression | Meaning |
|---|---|
| $f(\lambda x+(1-\lambda)y)$ | Average the inputs, then evaluate |
| $\lambda f(x)+(1-\lambda)f(y)$ | Evaluate first, then average the values |

For a convex function, averaging inputs is no worse than averaging their objective values.

### Worked example: the chord inequality

Let $f(x)=x^2$, with endpoints $x=0$ and $y=4$. At the midpoint,

$$
f\left(\frac{0+4}{2}\right)=f(2)=4,
$$

whereas

$$
\frac{f(0)+f(4)}{2}=\frac{0+16}{2}=8.
$$

Therefore,

$$
4\le 8.
$$

```text
Height above input x = 2:

Chord between (0,0) and (4,16):       8
                                      |
                                      | gap = 4
                                      |
Curve f(x) = x²:                      4
```

The chord lies above the curve.

### 2.3 Convexity does not mean differentiability or uniqueness

Two distinctions are important:

- $f(x)=|x|$ is convex but is not differentiable at $0$.
- $f(x_1,x_2)=x_1^2$ is convex but has infinitely many minimizers:

$$
\{(0,a):a\in\mathbb R\}.
$$

Thus, convexity alone guarantees neither a gradient everywhere nor a unique solution. [Lecture notes](#source-notes) [Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

---

## 3. The first-order viewpoint: tangent planes are lower bounds

For a differentiable convex function,

$$
\boxed{
f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle.
}
$$

The expression on the right is the tangent line in one dimension, or tangent hyperplane in several dimensions. Convexity makes this local linear approximation a global lower bound. [Lecture notes](#source-notes)

### 3.1 Do not confuse chords and tangents

```text
For a differentiable convex function:

       chord between two graph points
                    ↓
            lies above the curve

                actual curve

            lies above every tangent
                    ↑
          tangent at a chosen point
```

These are complementary views:

$$
\text{tangent lower bound}
\le
\text{function}
\le
\text{chord between endpoints}.
$$

### Worked example: a tangent to a quadratic

Let

$$
f(x)=\frac{x^2}{2}.
$$

At $x=2$,

$$
f(2)=2,
\qquad
f'(2)=2.
$$

The tangent line is

$$
\ell(y)=2+2(y-2)=2y-2.
$$

It is a global lower bound because

$$
f(y)-\ell(y)
=
\frac{y^2}{2}-2y+2
=
\frac{(y-2)^2}{2}
\ge 0.
$$

The nonnegative squared term explains exactly why the tangent never crosses above the function.

### 3.2 The inequality used in the convergence proof

Substitute $y=x^*$:

$$
f(x^*)\ge f(x)+\langle\nabla f(x),x^*-x\rangle.
$$

Rearrange:

$$
\boxed{
f(x)-f(x^*)
\le
\langle\nabla f(x),x-x^*\rangle.
}
$$

This converts objective error into an inner product. That inner product also appears when we expand the squared distance after a gradient step, which is the key connection behind the proof. [Lecture notes](#source-notes)

### 3.3 Why the first-order inequality follows from convexity

For $0<\theta\le1$, convexity gives

$$
f(x+\theta(y-x))
\le
(1-\theta)f(x)+\theta f(y).
$$

Rearranging,

$$
f(y)-f(x)
\ge
\frac{f(x+\theta(y-x))-f(x)}{\theta}.
$$

As $\theta\downarrow0$, the right-hand side becomes the directional derivative:

$$
\langle\nabla f(x),y-x\rangle.
$$

That proves the tangent lower-bound inequality. [Lecture notes](#source-notes)

---

## 4. Testing convexity and understanding optimality

### 4.1 Second derivatives in one dimension

For a twice continuously differentiable function on $\mathbb R$,

$$
f\text{ is convex}
\quad\Longleftrightarrow\quad
f''(x)\ge0\text{ for every }x.
$$

For example:

$$
f(x)=x^2
\quad\Rightarrow\quad
f''(x)=2\ge0.
$$

But

$$
f(x)=x^3
\quad\Rightarrow\quad
f''(x)=6x,
$$

which is negative when $x<0$. Therefore, $x^3$ is not convex on all of $\mathbb R$, although it is convex on $[0,\infty)$. The domain matters. [Lecture notes](#source-notes) [Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

### 4.2 Hessians in several dimensions

The multivariable equivalent is

$$
f\text{ is convex}
\quad\Longleftrightarrow\quad
\nabla^2 f(x)\succeq0
$$

at every point, under the lecture’s twice-continuously-differentiable assumptions.

Positive semidefinite means

$$
v^\top\nabla^2 f(x)v\ge0
\qquad\text{for every vector }v.
$$

In words: there is no direction of negative curvature. [Lecture notes](#source-notes)

### 4.3 Least squares: the main application example

Let

$$
f(x)=\frac12\|Ax-b\|_2^2,
\qquad A\in\mathbb R^{m\times d}.
$$

Then

$$
\nabla f(x)=A^\top(Ax-b),
$$

and

$$
\nabla^2f(x)=A^\top A.
$$

For every $v$,

$$
v^\top A^\top Av=\|Av\|_2^2\ge0.
$$

Therefore, least squares is convex. [Lecture notes](#source-notes)

The dimensions explain why the transpose is essential:

```text
x:                  d × 1
A:                  m × d
Ax − b:             m × 1
Aᵀ(Ax − b):         d × 1
```

The residual lives in measurement space, with $m$ coordinates. Multiplication by $A^\top$ maps it back to parameter space, where the update must have $d$ coordinates.

### 4.4 Why every local minimum is global

Suppose $x$ is a local minimum, but some feasible $y$ has

$$
f(y)<f(x).
$$

Consider

$$
z_\theta=(1-\theta)x+\theta y.
$$

Convexity of $K$ makes $z_\theta$ feasible. Convexity of $f$ gives

$$
f(z_\theta)
\le
(1-\theta)f(x)+\theta f(y)
<
f(x).
$$

As $\theta\downarrow0$, these better feasible points approach $x$, contradicting local optimality. [Lecture notes](#source-notes)

### 4.5 Stationary points versus constrained optima

For differentiable, unconstrained convex minimization,

$$
\nabla f(x)=0
$$

certifies a global minimum. The first-order inequality becomes

$$
f(y)\ge f(x)
$$

for every $y$. [Lecture notes](#source-notes)

At a constrained boundary optimum, the gradient need not vanish. For example,

$$
\min_{x\in[0,1]}x
$$

has optimum $x^*=0$, even though $f'(0)=1$.

The more general constrained condition is

$$
\langle\nabla f(x^*),y-x^*\rangle\ge0
\qquad\text{for every }y\in K.
$$

It says that no feasible direction offers a negative first-order change. [Bubeck](http://sbubeck.com/Bubeck15.pdf)

---

## 5. Gradient descent: direction and step size

For unconstrained optimization, gradient descent uses

$$
\boxed{
x_{t+1}=x_t-\eta\nabla f(x_t),
}
$$

where $\eta>0$ is the step size. [Lecture notes](#source-notes)

### 5.1 Why move opposite the gradient?

For a small displacement $h$,

$$
f(x+h)
=
f(x)+\langle\nabla f(x),h\rangle
+o(\|h\|_2).
$$

If $\|h\|_2\le\rho$, Cauchy–Schwarz gives

$$
\langle\nabla f(x),h\rangle
\ge
-\rho\|\nabla f(x)\|_2.
$$

For a nonzero gradient, equality is achieved by

$$
h=-\rho\frac{\nabla f(x)}{\|\nabla f(x)\|_2}.
$$

Thus, the negative gradient gives the steepest first-order decrease for a fixed Euclidean movement budget. This does not mean that an arbitrarily long step in that direction will improve the objective. [Lecture notes](#source-notes)

### 5.2 A complete step-size example

Let

$$
f(x)=\frac{x^2}{2},
\qquad f'(x)=x.
$$

The update is

$$
x_{t+1}=(1-\eta)x_t,
$$

so

$$
x_t=(1-\eta)^t x_0.
$$

Starting at $x_0=2$:

| Step size | Iterates | Behavior |
|---|---|---|
| $\eta=\frac12$ | $2,1,\frac12,\frac14,\ldots$ | Converges without crossing zero |
| $\eta=1$ | $2,0,0,\ldots$ | Reaches the optimum immediately |
| $\eta=\frac32$ | $2,-1,\frac12,-\frac14,\ldots$ | Converges while alternating |
| $\eta=2$ | $2,-2,2,-2,\ldots$ | Oscillates without improvement |
| $\eta=\frac52$ | $2,-3,\frac92,-\frac{27}{4},\ldots$ | Diverges |

For this quadratic, convergence from a nonzero starting point occurs exactly when

$$
|1-\eta|<1
\quad\Longleftrightarrow\quad
0<\eta<2.
$$

This condition is specific to this objective’s curvature; it is not a universal step-size rule. [Lecture notes](#source-notes)

### Visualization

For $\eta=\frac12$:

```text
Optimum                                      Start
  0      0.25     0.5          1                 2
  |--------●-------●-----------●-----------------●
           x3      x2          x1                x0

Movement: 2 → 1 → 0.5 → 0.25 → ...
```

For $\eta=2$:

```text
       −2                  0                  2
        ●------------------|------------------●
        x1                                   x0
        x3                                   x2

The sign changes, but f(x) stays equal to 2.
```

---

## 6. The convergence theorem: what is actually guaranteed?

The lecture assumes:

1. $f:\mathbb R^d\to\mathbb R$ is differentiable and convex.
2. A minimizer $x^*$ exists.
3. The initial point satisfies

$$
\|x_0-x^*\|_2\le D.
$$

4. At every queried iterate,

$$
\|\nabla f(x_t)\|_2\le G.
$$

5. A constant step size $\eta>0$ is used for $T$ updates.

Return the average of the queried points:

$$
\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t.
$$

Then

$$
\boxed{
f(\bar x_T)-f(x^*)
\le
\frac{D^2}{2\eta T}
+
\frac{\eta G^2}{2}.
}
$$

Choosing

$$
\boxed{
\eta=\frac{D}{G\sqrt T}
}
$$

gives

$$
\boxed{
f(\bar x_T)-f(x^*)\le\frac{DG}{\sqrt T}.
}
$$

These statements apply under the assumptions above. In particular, convexity does not automatically provide $D$ or $G$. [Lecture notes](#source-notes)

### What do the two error terms mean?

| Term | Effect of increasing $\eta$ |
|---|---|
| $\frac{D^2}{2\eta T}$ | Decreases |
| $\frac{\eta G^2}{2}$ | Increases |

The step size balances these competing terms.

A very small step reduces the second term but makes the first large. A very large step does the reverse.

### What does $1/\sqrt T$ imply?

For this guarantee:

- Four times as many iterations halves the error bound.
- One hundred times as many iterations reduces the bound by a factor of ten.
- To guarantee error at most $\varepsilon$, it suffices to use

$$
T\ge\left(\frac{DG}{\varepsilon}\right)^2.
$$

This is an upper bound, not a prediction that every problem needs that many iterations. [Lecture notes](#source-notes)

---

## 7. The proof, step by step

The proof’s central device is a potential function:

$$
R_t=\|x_t-x^*\|_2^2.
$$

Although the algorithm does not know $x^*$, the analysis may compare its iterates with $x^*$. [Lecture notes](#source-notes)

### Step 1: expand one update

Write

$$
g_t=\nabla f(x_t).
$$

Then

$$
\begin{aligned}
R_{t+1}
&=\|x_t-\eta g_t-x^*\|_2^2\\
&=\|(x_t-x^*)-\eta g_t\|_2^2\\
&=R_t
-2\eta\langle g_t,x_t-x^*\rangle
+\eta^2\|g_t\|_2^2.
\end{aligned}
$$

This is the vector version of

$$
(a-b)^2=a^2-2ab+b^2.
$$

### Step 2: use convexity

The first-order inequality gives

$$
f(x_t)-f(x^*)
\le
\langle g_t,x_t-x^*\rangle.
$$

Since $-2\eta<0$, multiplying reverses the inequality:

$$
-2\eta\langle g_t,x_t-x^*\rangle
\le
-2\eta\bigl(f(x_t)-f(x^*)\bigr).
$$

Using $\|g_t\|_2^2\le G^2$,

$$
R_{t+1}
\le
R_t
-2\eta\bigl(f(x_t)-f(x^*)\bigr)
+\eta^2G^2.
$$

Rearrange:

$$
\boxed{
f(x_t)-f(x^*)
\le
\frac{R_t-R_{t+1}}{2\eta}
+\frac{\eta G^2}{2}.
}
$$

This is the one-step inequality from which everything else follows. [Lecture notes](#source-notes)

### Step 3: sum and telescope

Summing for $t=0,\ldots,T-1$,

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac1{2\eta}
\sum_{t=0}^{T-1}(R_t-R_{t+1})
+\frac{\eta G^2T}{2}.
$$

The distance terms cancel:

```text
(R0 − R1)
    + (R1 − R2)
          + (R2 − R3)
                + ...
                    + (R(T−1) − RT)
-----------------------------------
= R0 − RT
```

Therefore,

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{R_0-R_T}{2\eta}
+\frac{\eta G^2T}{2}.
$$

Because $R_0\le D^2$ and $R_T\ge0$,

$$
\sum_{t=0}^{T-1}
\bigl(f(x_t)-f(x^*)\bigr)
\le
\frac{D^2}{2\eta}
+\frac{\eta G^2T}{2}.
$$

Dividing by $T$,

$$
\frac1T\sum_{t=0}^{T-1}f(x_t)-f(x^*)
\le
\frac{D^2}{2\eta T}
+\frac{\eta G^2}{2}.
$$

### Step 4: move from average values to the average point

Convexity gives the finite Jensen inequality:

$$
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

Hence,

$$
f(\bar x_T)-f(x^*)
\le
\frac{D^2}{2\eta T}
+\frac{\eta G^2}{2}.
$$

Notice that we use an inequality, not an equality:

$$
f(\text{average point})
\neq
\text{average function value}
$$

in general. [Lecture notes](#source-notes)

### Step 5: balance the terms

Set

$$
\frac{D^2}{2\eta T}
=
\frac{\eta G^2}{2}.
$$

Then

$$
D^2=\eta^2G^2T,
$$

so

$$
\eta=\frac{D}{G\sqrt T}.
$$

Each term becomes

$$
\frac{DG}{2\sqrt T},
$$

and their sum is

$$
\frac{DG}{\sqrt T}.
$$

### Proof map to memorize

```text
Gradient update
      ↓
Expand squared distance
      ↓
Use first-order convexity
      ↓
Obtain one-step objective-error bound
      ↓
Sum and telescope
      ↓
Apply initial-distance and gradient bounds
      ↓
Use convexity at the average point
      ↓
Balance the step-size terms
```

---

## 8. Worked examples and pseudocode

### 8.1 The lecture’s numerical exercise

Given

$$
D=2,\qquad G=3,\qquad T=900,
$$

we have $\sqrt T=30$, so

$$
\eta=\frac{2}{3\cdot30}=\frac1{45}.
$$

The guarantee is

$$
f(\bar x_T)-f(x^*)
\le
\frac{2\cdot3}{30}
=
0.2.
$$

Each term in the general bound equals $0.1$. This guarantees objective error at most $0.2$; it does not guarantee that $\bar x_T$ is within distance $0.2$ of $x^*$. [Lecture notes](#source-notes)

### 8.2 A least-squares calibration example

Consider a constructed example with measurements approximately following

$$
b_i\approx a_iw.
$$

Take

$$
A=
\begin{bmatrix}
1\\
2
\end{bmatrix},
\qquad
b=
\begin{bmatrix}
1\\
2
\end{bmatrix}.
$$

Then

$$
\begin{aligned}
f(w)
&=\frac12\|Aw-b\|_2^2\\
&=\frac12\bigl((w-1)^2+(2w-2)^2\bigr)\\
&=\frac52(w-1)^2.
\end{aligned}
$$

Its gradient is

$$
f'(w)=5(w-1),
$$

consistent with the lecture’s formula $A^\top(Aw-b)$. [Lecture notes](#source-notes)

With $w_0=0$ and $\eta=0.1$,

$$
w_{t+1}
=
w_t-0.5(w_t-1)
=
0.5w_t+0.5.
$$

| $t$ | $w_t$ | $f(w_t)$ |
|---|---:|---:|
| 0 | $0$ | $2.5$ |
| 1 | $0.5$ | $0.625$ |
| 2 | $0.75$ | $0.15625$ |
| 3 | $0.875$ | $0.0390625$ |

The parameter error satisfies

$$
w_{t+1}-1=\frac12(w_t-1).
$$

Thus, in this particular example, the parameter error halves each iteration and the objective error shrinks by a factor of four. The general $1/\sqrt T$ theorem is valid under much weaker assumptions and need not describe this quadratic’s faster behavior.

### 8.3 Pseudocode matching the lecture theorem

```text
AVERAGED-GRADIENT-DESCENT(Gradient, x0, D, G, T):
    require D > 0, G > 0, T ≥ 1

    eta ← D / (G * sqrt(T))
    x ← copy(x0)
    sum_points ← zero vector with the same dimension as x0

    for t ← 0 to T − 1:
        sum_points ← sum_points + x
        g ← Gradient(x)
        x ← x − eta * g

    return sum_points / T
```

The summation happens before the update, so the output is

$$
\frac{x_0+x_1+\cdots+x_{T-1}}{T}.
$$

The algorithm computes $x_T$, but $x_T$ is not included in this average. That matches the lecture’s indexing exactly. [Lecture notes](#source-notes)

### 8.4 An alternative: return the best queried iterate

If function values are available, return

$$
\hat x\in
\arg\min_{x\in\{x_0,\ldots,x_{T-1}\}}f(x).
$$

Because a minimum is no greater than an average,

$$
f(\hat x)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

The same error bound follows. This proof does not establish the same bound for the final iterate $x_T$. [Lecture notes](#source-notes)

```text
BEST-ITERATE-GRADIENT-DESCENT(Value, Gradient, x0, eta, T):
    x ← copy(x0)
    best_value ← +infinity
    best_point ← copy(x0)

    for t ← 0 to T − 1:
        value ← Value(x)

        if value < best_value:
            best_value ← value
            best_point ← copy(x)

        x ← x − eta * Gradient(x)

    return best_point
```

### 8.5 Runtime and storage

If one gradient evaluation costs $C_{\nabla}$, the averaged algorithm takes

$$
O\bigl(T(C_{\nabla}+d)\bigr)
$$

time and $O(d)$ auxiliary storage, excluding storage used internally by the oracle.

For dense least squares,

$$
\nabla f(x)=A^\top(Ax-b)
$$

takes $O(md)$ time, so $T$ iterations take $O(Tmd)$ time. There is no need to form $A^\top A$ explicitly. [Lecture notes](#source-notes)

---

## 9. Caveats, nonsmooth functions, and the next lecture

### 9.1 A bounded gradient is not the same as a slowly changing gradient

These are different assumptions:

$$
\|\nabla f(x)\|_2\le G
$$

bounds gradient magnitude, whereas

$$
\|\nabla f(x)-\nabla f(y)\|_2
\le
L\|x-y\|_2
$$

bounds how quickly gradients change. The second property is called $L$-smoothness. [Shalev-Shwartz and Ben-David](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf)

For example,

$$
f(x)=\frac{x^2}{2}
$$

has gradient $x$, which is unbounded over $\mathbb R$, but

$$
|f'(x)-f'(y)|=|x-y|,
$$

so it is $1$-smooth.

The lecture only needs the $G$ bound at the queried iterates. For this quadratic with $x_0=2$ and $\eta=\frac12$, all iterates lie in $[0,2]$, so $G=2$ is valid along that trajectory. [Lecture notes](#source-notes)

### 9.2 Convex does not automatically mean “the minimum exists”

For example,

$$
f(x)=e^x
$$

is convex on $\mathbb R$, but its infimum $0$ is never attained. There is no finite $x^*$. This illustrates why the lecture explicitly assumes a minimizer exists. [Lecture notes](#source-notes) [Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

### 9.3 Subgradients handle corners

A subgradient $g$ at $x$ satisfies

$$
f(y)\ge f(x)+\langle g,y-x\rangle
$$

for every $y$.

For $f(x)=|x|$,

$$
\partial f(x)=
\begin{cases}
\{1\},&x>0,\\
[-1,1],&x=0,\\
\{-1\},&x<0.
\end{cases}
$$

Replacing $\nabla f(x_t)$ with a bounded subgradient preserves the proof, because the proof only needs the supporting-linear-function inequality. [Lecture notes](#source-notes)

```text
SUBGRADIENT-ABS(x):
    if x > 0:
        return 1
    if x < 0:
        return −1
    return 0
```

A constant-step subgradient method can bounce around a corner. For instance, starting at $x_0=0.2$ with $\eta=0.3$,

$$
0.2\to-0.1\to0.2\to-0.1\to\cdots.
$$

So the word “descent” does not ensure monotone objective decrease for general subgradient steps. [Bubeck](http://sbubeck.com/Bubeck15.pdf)

### 9.4 Constraints require additional machinery

A gradient step can leave $K$. For example, minimizing $f(x)=x$ over $[0,1]$, an unconstrained step from $0.1$ with $\eta=0.2$ produces $-0.1$, which is infeasible.

The projected method uses

$$
x_{t+1}
=
\Pi_K\bigl(x_t-\eta\nabla f(x_t)\bigr).
$$

For an interval,

$$
\Pi_{[a,b]}(z)=\min\{b,\max\{a,z\}\}.
$$

Projection is a preview of the next topic, rather than part of the lecture’s main unconstrained theorem. [Lecture notes](#source-notes) [Bubeck](http://sbubeck.com/Bubeck15.pdf)

---

## 10. Quick quiz

Try these before reading the answer key. The questions below are original practice questions based on the lecture.

### Questions

1. State the definition of a convex function.

2. For a differentiable convex function, is a tangent plane an upper bound or a lower bound?

3. True or false: Every convex function has a unique minimizer.

4. Why does $\nabla f(x)=0$ certify an unconstrained global minimum?

5. For $f(x)=x^2/2$, derive a formula for $x_t$ in terms of $x_0,\eta,t$.

6. If the bound is $DG/\sqrt T$, how much must $T$ increase to halve the error bound?

7. Which output has the lecture’s guarantee?
   - A. The final iterate, automatically.
   - B. The average of the queried iterates.
   - C. Every queried iterate individually.

8. Identify the error:

$$
f\left(\frac{x_0+x_1}{2}\right)
=
\frac{f(x_0)+f(x_1)}{2}.
$$

9. Does convexity imply globally bounded gradients?

10. For $A\in\mathbb R^{m\times d}$, what is the dimension of $A^\top(Ax-b)$?

### Answer key

1. For all $x,y$ in the convex domain and $\lambda\in[0,1]$,

$$
f(\lambda x+(1-\lambda)y)
\le
\lambda f(x)+(1-\lambda)f(y).
$$

2. A lower bound.

3. False. A constant function has every point as a minimizer.

4. The first-order inequality becomes

$$
f(y)\ge f(x)+0=f(x).
$$

5. Since $x_{t+1}=(1-\eta)x_t$,

$$
x_t=(1-\eta)^t x_0.
$$

6. Multiply $T$ by $4$.

7. B. The best queried iterate also has the bound when function values are available.

8. Convexity gives $\le$, not equality in general.

9. No. For $f(x)=x^2/2$, the gradient is $x$, unbounded over $\mathbb R$.

10. $d\times1$. [Lecture notes](#source-notes)

---

## 11. Practice exam: 100 points

These are original exam-style questions, not past course exam questions.

### Problem 1: Convexity and optimality — 15 points

Consider

$$
f(u,v)=(u+v-2)^2.
$$

1. Compute its gradient and Hessian.
2. Prove it is convex.
3. Describe all global minimizers.
4. Explain why the minimizer is not unique.

### Problem 2: Step sizes and exact iterates — 15 points

For

$$
f(x)=\frac{x^2}{2},
\qquad x_0=4:
$$

1. Derive $x_t$ for a constant step size $\eta$.
2. Determine exactly which positive step sizes converge.
3. For $\eta=\frac12$, compute $x_1,x_2,x_3$.
4. Compute

$$
\bar x_4=\frac{x_0+x_1+x_2+x_3}{4}
$$

   and its objective value.

5. Give one step size that oscillates without converging and one that diverges.

### Problem 3: Reconstruct the convergence proof — 25 points

Assume the lecture’s convexity, minimizer-existence, distance-bound, and gradient-bound assumptions.

Starting from

$$
x_{t+1}=x_t-\eta\nabla f(x_t),
$$

prove

$$
f(\bar x_T)-f(x^*)
\le
\frac{D^2}{2\eta T}
+\frac{\eta G^2}{2}.
$$

Your proof must explicitly identify:

1. The potential function.
2. The squared-distance expansion.
3. Where convexity is used.
4. Where the gradient bound is used.
5. The telescoping sum.
6. The final averaging argument.

Then choose the optimal constant $\eta$ for this bound.

### Problem 4: Design an $\varepsilon$-approximation algorithm — 15 points

Suppose

$$
D=3,\qquad G=2,\qquad \varepsilon=0.1.
$$

1. Find a sufficient iteration count $T$.
2. Find the prescribed step size.
3. Write pseudocode returning an $\varepsilon$-optimal point under the theorem’s assumptions.
4. If a gradient evaluation costs $O(md)$, state the total runtime.

### Problem 5: Feasible averages and Jensen’s inequality — 15 points

Let $x_0,\ldots,x_{T-1}\in K$, where $K$ is convex.

Prove by induction that:

1. Their average lies in $K$.
2. For convex $f$,

$$
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

### Problem 6: Diagnose a flawed argument — 15 points

A student writes:

> “Least squares is convex, so its gradients are globally bounded. Therefore, any positive constant step size makes gradient descent converge. The $DG/\sqrt T$ theorem applies to the final iterate, and the error guarantee means the output is within Euclidean distance $\varepsilon$ of the optimizer.”

Identify and correct four distinct errors.

---

## 12. Practice exam solutions

### Solution 1: Convexity and optimality

The gradient is

$$
\nabla f(u,v)
=
2(u+v-2)
\begin{bmatrix}
1\\
1
\end{bmatrix}.
$$

The Hessian is

$$
\nabla^2f
=
\begin{bmatrix}
2&2\\
2&2
\end{bmatrix}.
$$

For $z=(a,b)$,

$$
z^\top\nabla^2f\,z
=
2(a+b)^2
\ge0.
$$

Thus, the Hessian is positive semidefinite and $f$ is convex.

Since a square is nonnegative, its minimum value is $0$, attained exactly when

$$
u+v=2.
$$

Therefore, the minimizers form a line:

$$
\{(u,v):u+v=2\}.
$$

The function is flat along the direction $(1,-1)$, so its minimizer is not unique.

```text
v
↑
2 ●
  | \
  |  \    Every point on this line is optimal.
  |   \
0 +----●----------------→ u
       2
```

This uses the lecture’s Hessian criterion and illustrates why convexity does not imply uniqueness. [Lecture notes](#source-notes)

### Solution 2: Step sizes and exact iterates

The recurrence is

$$
x_{t+1}=(1-\eta)x_t,
$$

hence

$$
x_t=4(1-\eta)^t.
$$

Convergence occurs exactly when

$$
0<\eta<2.
$$

For $\eta=\frac12$,

$$
x_1=2,\qquad x_2=1,\qquad x_3=\frac12.
$$

Therefore,

$$
\bar x_4
=
\frac{4+2+1+\frac12}{4}
=
\frac{15}{8},
$$

and

$$
f(\bar x_4)
=
\frac12\left(\frac{15}{8}\right)^2
=
\frac{225}{128}.
$$

At $\eta=2$, the iterates alternate between $4$ and $-4$. At $\eta=3$, their magnitudes double each step. [Lecture notes](#source-notes)

### Solution 3: Convergence proof

Let

$$
R_t=\|x_t-x^*\|_2^2,
\qquad
g_t=\nabla f(x_t).
$$

Expanding the update,

$$
R_{t+1}
=
R_t
-2\eta\langle g_t,x_t-x^*\rangle
+\eta^2\|g_t\|_2^2.
$$

Convexity gives

$$
\langle g_t,x_t-x^*\rangle
\ge
f(x_t)-f(x^*),
$$

and the gradient assumption gives

$$
\|g_t\|_2^2\le G^2.
$$

Thus,

$$
f(x_t)-f(x^*)
\le
\frac{R_t-R_{t+1}}{2\eta}
+\frac{\eta G^2}{2}.
$$

Summing,

$$
\sum_{t=0}^{T-1}(f(x_t)-f(x^*))
\le
\frac{R_0-R_T}{2\eta}
+\frac{\eta G^2T}{2}.
$$

Since $R_0\le D^2$ and $R_T\ge0$,

$$
\frac1T\sum_{t=0}^{T-1}(f(x_t)-f(x^*))
\le
\frac{D^2}{2\eta T}
+\frac{\eta G^2}{2}.
$$

Apply convexity to the average point:

$$
f(\bar x_T)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

Finally, choose

$$
\eta=\frac{D}{G\sqrt T}
$$

to obtain

$$
f(\bar x_T)-f(x^*)\le\frac{DG}{\sqrt T}.
$$

This is the lecture’s central proof. [Lecture notes](#source-notes)

### Solution 4: An $\varepsilon$-approximation algorithm

We need

$$
\frac{DG}{\sqrt T}\le\varepsilon.
$$

Therefore,

$$
T\ge
\left(\frac{3\cdot2}{0.1}\right)^2
=
60^2
=
3600.
$$

Choose $T=3600$. Then

$$
\eta
=
\frac{3}{2\cdot60}
=
\frac1{40}.
$$

```text
EPSILON-OPTIMIZER(Gradient, x0):
    T ← 3600
    eta ← 1/40
    x ← copy(x0)
    total ← zero vector

    repeat T times:
        total ← total + x
        x ← x − eta * Gradient(x)

    return total / T
```

With $O(md)$ gradient cost, the runtime is $O(Tmd)$. More generally, substituting the sufficient iteration count gives

$$
O\left(
md\left\lceil\frac{D^2G^2}{\varepsilon^2}\right\rceil
\right).
$$

The guarantee still depends on the stated bounds being valid for this run. [Lecture notes](#source-notes)

### Solution 5: Feasible averages and Jensen’s inequality

For $T=1$, both statements are immediate.

Assume both hold for $T-1$ points. Define

$$
a=\frac1{T-1}\sum_{t=0}^{T-2}x_t.
$$

By induction, $a\in K$. The full average can be written as

$$
\bar x_T
=
\frac{T-1}{T}a+\frac1T x_{T-1}.
$$

This is a convex combination of two points in $K$, so $\bar x_T\in K$.

For the function inequality,

$$
f(\bar x_T)
\le
\frac{T-1}{T}f(a)+\frac1T f(x_{T-1}).
$$

By the induction hypothesis,

$$
f(a)
\le
\frac1{T-1}\sum_{t=0}^{T-2}f(x_t).
$$

Substituting,

$$
f(\bar x_T)
\le
\frac1T\sum_{t=0}^{T-1}f(x_t).
$$

These are the feasibility and objective-value facts needed for averaging. [Lecture notes](#source-notes)

### Solution 6: Four errors

1. Convexity does not imply globally bounded gradients.

   For $f(x)=x^2/2$, the gradient is $x$, which is unbounded on $\mathbb R$. A bound along the iterates must be justified separately.

2. Not every positive step size converges.

   For the same quadratic, $\eta=2$ causes persistent oscillation and $\eta>2$ causes divergence from a nonzero start.

3. The theorem’s output rule is being changed.

   The proof guarantees the average queried point, or the best queried iterate if function values are available. It does not establish the same bound for the final iterate.

4. Objective error is not Euclidean distance error.

   The theorem bounds $f(x)-f(x^*)$, not $\|x-x^*\|_2$. Convexity alone does not provide a general conversion between them. [Lecture notes](#source-notes)

---

## 13. Textbook reading map

### 13.1 Closest match to this lecture’s proof

Shai Shalev-Shwartz and Shai Ben-David, *Understanding Machine Learning: From Theory to Algorithms*, Cambridge University Press, 2014.

Read:

- Section 12.1.1: Convexity.
- Section 12.1.2: Lipschitzness.
- Section 14.1: Gradient Descent.
- Section 14.1.1: Analysis of GD for Convex-Lipschitz Functions.
- Section 14.2: Subgradients.
- Section 14.4.1: Adding a Projection Step.

This is a close match to the lecture’s averaged-iterate, bounded-gradient analysis. Although Chapter 14 is titled “Stochastic Gradient Descent,” it begins with ordinary deterministic gradient descent. The author-hosted PDF notes that its page numbers differ from the printed book, so use section numbers. [Shalev-Shwartz and Ben-David](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf)

### 13.2 Best for geometry and convexity foundations

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004.

Read:

- Section 2.1: Affine and convex sets.
- Section 3.1: Basic properties and examples of convex functions.
- Section 4.2: Convex optimization.
- Section 9.3: Gradient descent method.

Use this text to strengthen your understanding of chords, tangent lower bounds, Hessians, and optimality. Its gradient-descent treatment develops additional assumptions and techniques, so distinguish those results from the lecture’s basic $1/\sqrt T$ guarantee. [Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

### 13.3 Best for convergence rates and the next topics

Sébastien Bubeck, *Convex Optimization: Algorithms and Complexity*, *Foundations and Trends in Machine Learning*, 8(3–4), 231–357, 2015.

Read:

- Sections 1.2–1.4: Convexity, its consequences, and the oracle model.
- Section 3.1: Projected subgradient descent for Lipschitz functions.
- Section 3.2: Gradient descent for smooth functions.
- Section 3.4: Strong convexity.

Section 3.1 is the closest theoretical companion to this lecture. Sections 3.2 and 3.4 explain how additional curvature assumptions lead to stronger guarantees. This is a research monograph rather than a conventional introductory textbook, but it provides a particularly useful map of the convergence results. [Bubeck](http://sbubeck.com/Bubeck15.pdf)

### Suggested reading order

1. Read the lecture and reconstruct its potential-function proof without looking.
2. Read Shalev-Shwartz and Ben-David, Sections 14.1–14.2, for a parallel derivation.
3. Use Boyd and Vandenberghe, Sections 2.1 and 3.1, to reinforce the geometry.
4. Read Bubeck, Sections 3.1–3.2, to connect bounded gradients, projection, and smoothness.

For exam preparation, prioritize explaining every transition in

$$
\boxed{
\text{update}
\;\longrightarrow\;
\text{squared distance}
\;\longrightarrow\;
\text{objective error}
\;\longrightarrow\;
\text{telescoping}
\;\longrightarrow\;
\text{average-point guarantee}.
}
$$

---

## Source notes

The lecture source is the user-provided `Lec_12_Unmarked.pdf`: *CS 6515: Graduate Algorithms — Lecture 12: Convexity and Gradient Descent*, instructors Sahil Singla and Gerandy Brito, Fall 2026, 7 pages. Keep your original PDF separately; it is not embedded in this Markdown document. Links labeled “Lecture notes” refer to this source note.

The textbook citations above link directly to the publicly available PDFs. The worked examples, quiz, and exam-style questions added to the lecture explanation are study aids, not official past exam questions.
