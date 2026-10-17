# Lecture 13 Study Guide: Projected and Smooth Gradient Descent

Based on the attached lecture, *CS 6515: Graduate Algorithms — Lecture 13: Projected and Smooth Gradient Descent*, Sahil Singla and Gerandy Brito, Fall 2026.

Your lecture develops two upgrades to basic gradient descent:

1. Projection keeps iterates inside a feasible set without breaking the distance-based convergence proof.
2. Smoothness controls curvature, allowing a constant step size and improving the objective-error guarantee from $O(1/\sqrt{T})$ for an average iterate to $O(1/T)$ for the last iterate.

The central proof idea is **cancellation**: smoothness supplies a negative gradient-squared term that cancels the positive gradient-squared term in the squared-distance expansion.

Below is a study guide with worked examples, text visualizations, pseudocode, quizzes, and exam-style problems with solutions.

## 1. Roadmap and notation

We want to solve

$$
\min_{x\in K} f(x),
$$

where $f$ is the objective and $K$ is the feasible set. In unconstrained optimization, $K=\mathbb{R}^d$.

| Symbol | Meaning |
|---|---|
| $x_t$ | Iterate after $t$ updates |
| $x^*$ | An attained minimizer over the relevant domain |
| $g_t$ | Gradient $\nabla f(x_t)$, or a chosen subgradient |
| $\eta$ | Step size |
| $D$ | Upper bound on $\lVert x_0-x^*\rVert_2$ |
| $G$ | Upper bound on gradient/subgradient norms at queried iterates |
| $\beta>0$ | Upper bound on how quickly the gradient changes |
| $\Pi_K(u)$ | Euclidean projection of $u$ onto $K$ |

The lecture compares these two guarantees:

| Assumptions | Output | Error bound after $T$ steps | Step size |
|---|---|---|---|
| Convex; $\lVert g_t\rVert_2\le G$; projection when constrained | $\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t$ | $\frac{DG}{\sqrt T}$ | $\frac{D}{G\sqrt T}$ |
| Convex and $\beta$-smooth; unconstrained | $x_T$ | $\frac{\beta D^2}{2T}$ | $\frac1\beta$ |

The indexing matters: $T$ updates query $x_0,\ldots,x_{T-1}$ and produce $x_T$.

## 2. Projection: take a gradient step, then restore feasibility

### 2.1 Why ordinary gradient descent can fail with constraints

Ordinary gradient descent computes

$$
u_{t+1}=x_t-\eta\nabla f(x_t).
$$

Even if $x_t\in K$, the new point $u_{t+1}$ might lie outside $K$. Projected gradient descent corrects this:

$$
\boxed{x_{t+1}=\Pi_K\bigl(x_t-\eta\nabla f(x_t)\bigr)}
$$

with

$$
\Pi_K(u)=\arg\min_{z\in K}\lVert z-u\rVert_2^2.
$$

For a nonempty, closed, convex set $K$, the projection exists and is unique.

### 2.2 Worked example: an interval constraint

Consider

$$
\min_{0\le x\le 2} f(x),\qquad f(x)=(x-3)^2.
$$

The unconstrained minimizer is $3$, but the constrained minimizer is $x^*=2$.

Start with $x_0=1$ and $\eta=\frac12$. Since

$$
f'(x)=2(x-3),
$$

the raw step is

$$
u_1=1-\frac12(-4)=3.
$$

Project onto $[0,2]$:

$$
x_1=\Pi_{[0,2]}(3)=2.
$$

```text
Feasible set K
[---------------------]
0          1          2          3
           x₀         x₁         u₁
           └──── raw step ──────►
                      ◄─ project ┘
```

At $x=2$, the gradient is $-2$, not zero. Nevertheless, another raw step moves to $3$, and projection returns to $2$.

This illustrates an important distinction: a constrained optimum can have a nonzero gradient because the improving direction may be infeasible. The appropriate constrained first-order condition is

$$
\langle\nabla f(x^*),z-x^*\rangle\ge 0
\qquad\text{for every }z\in K.
$$

Here, $-2(z-2)\ge0$ for every $z\in[0,2]$.

### 2.3 Box projection is coordinatewise clipping

For

$$
K=\prod_{i=1}^d[a_i,b_i],
$$

projection is

$$
\boxed{(\Pi_K(u))_i=\min\{b_i,\max\{a_i,u_i\}\}.}
$$

Each coordinate is independently moved to its nearest allowed value.

For example, if

$$
K=[0,1]\times[0,2],\qquad u=(-0.4,2.7),
$$

then

$$
\Pi_K(u)=(0,2).
$$

```text
Second coordinate
       ^
  2.7  | u •
       |    \
  2.0  |     • p=(0,2) ┌────────────┐
       |               │     K      │
       |               │            │
  0.0  +---------------└────────────┘---->
                      0             1
                              First coordinate
```

The diagram is schematic; the formula gives the exact projection.

## 3. Why projection preserves the convergence argument

### 3.1 The geometric inequality

Let $p=\Pi_K(u)$. For any feasible point $z\in K$,

$$
\boxed{
\lVert p-z\rVert_2^2
\le\lVert u-z\rVert_2^2-\lVert u-p\rVert_2^2
\le\lVert u-z\rVert_2^2.
}
$$

Thus projection cannot increase distance to any feasible comparison point—including the optimum $x^*$.

The claim is about feasible $z$, not arbitrary points outside $K$.

### 3.2 Proof, step by step

Because $K$ is convex,

$$
p+\theta(z-p)\in K,\qquad 0\le\theta\le1.
$$

Since $p$ minimizes squared distance to $u$, moving from $p$ toward $z$ cannot initially decrease that distance. Define

$$
h(\theta)=\lVert u-p-\theta(z-p)\rVert_2^2.
$$

Then

$$
h'(0)=-2\langle u-p,z-p\rangle\ge0,
$$

so

$$
\langle u-p,z-p\rangle\le0.
$$

Now expand:

$$
\begin{aligned}
\lVert u-z\rVert_2^2
&=\lVert(u-p)+(p-z)\rVert_2^2\\
&=\lVert u-p\rVert_2^2+\lVert p-z\rVert_2^2
+2\langle u-p,p-z\rangle.
\end{aligned}
$$

The final inner product is nonnegative, giving the result. This is the lecture's geometric foundation for projected gradient descent.

### 3.3 Plugging projection into the potential argument

Define the squared-distance potential

$$
R_t=\lVert x_t-x^*\rVert_2^2.
$$

Projection gives

$$
\begin{aligned}
R_{t+1}
&\le\lVert x_t-\eta g_t-x^*\rVert_2^2\\
&=R_t-2\eta\langle g_t,x_t-x^*\rangle
+\eta^2\lVert g_t\rVert_2^2.
\end{aligned}
$$

Rearranging,

$$
\langle g_t,x_t-x^*\rangle
\le\frac{R_t-R_{t+1}}{2\eta}
+\frac{\eta}{2}\lVert g_t\rVert_2^2.
$$

Convexity—or the subgradient inequality—implies

$$
f(x_t)-f(x^*)\le\langle g_t,x_t-x^*\rangle.
$$

Therefore,

$$
f(x_t)-f(x^*)
\le\frac{R_t-R_{t+1}}{2\eta}+\frac{\eta G^2}{2}.
$$

Sum over $t=0,\ldots,T-1$:

$$
\sum_{t=0}^{T-1}[f(x_t)-f(x^*)]
\le\frac{R_0-R_T}{2\eta}+\frac{T\eta G^2}{2}.
$$

Using $R_0\le D^2$, $R_T\ge0$, and convexity at the average,

$$
\boxed{
f(\bar x_T)-f(x^*)
\le\frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
}
$$

Choosing $\eta=D/(G\sqrt T)$, for positive $D,G$, gives $DG/\sqrt T$. Also, $\bar x_T\in K$ because an average of feasible points remains in a convex set.

### 3.4 Pseudocode with matching indexing

```text
PROJECTED-SUBGRADIENT-DESCENT(x0, T, eta, Subgradient, Project):
    require x0 belongs to K
    require T >= 1

    x = x0
    total = zero vector

    for t = 0, ..., T-1:
        total = total + x
        g = Subgradient(x)
        u = x - eta * g
        x = Project(u)

    return total / T
```

The returned average contains $x_0,\ldots,x_{T-1}$, exactly as in the proof.

```text
BOX-PROJECTION(u, lower, upper):
    for i = 1, ..., d:
        p[i] = min(upper[i], max(lower[i], u[i]))

    return p
```

Box projection costs $O(d)$. More complicated projections can require substantial optimization work; iteration count alone is not the full running time.

## 4. Smoothness: controlling changes in the gradient

### 4.1 Definition and intuition

A differentiable function is $\beta$-smooth if

$$
\boxed{
\lVert\nabla f(y)-\nabla f(x)\rVert_2
\le\beta\lVert y-x\rVert_2
\quad\text{for all }x,y.
}
$$

Interpretation: moving the input a little cannot change the gradient arbitrarily much.

```text
Bounded gradients:                   Smoothness:

How large can the slope be?          How quickly can the slope change?

        ||∇f(x)|| ≤ G                ||∇f(y)-∇f(x)|| ≤ β||y-x||
```

These are different assumptions.

For example,

$$
f(x)=\frac{x^2}{2},\qquad f'(x)=x
$$

is $1$-smooth because $|f'(y)-f'(x)|=|y-x|$, but its gradient is unbounded on $\mathbb R$.

Conversely, $f(x)=|x|$ has bounded subgradients but is not smooth because it is not differentiable at zero; projected subgradient methods handle this type of nonsmooth convex objective.

### 4.2 Curvature interpretation

For a twice continuously differentiable convex function,

$$
0\preceq\nabla^2f(x)\preceq\beta I.
$$

In one dimension this becomes

$$
0\le f''(x)\le\beta.
$$

Convexity supplies the lower curvature bound; smoothness supplies the upper bound. Smoothness alone does not imply convexity.

### 4.3 The descent lemma: a quadratic ceiling

For a $\beta$-smooth function,

$$
\boxed{
f(y)\le f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\beta}{2}\lVert y-x\rVert_2^2.
}
$$

For a function that is also convex, the objective lies between a tangent lower bound and a quadratic upper bound:

$$
\underbrace{f(x)+\langle\nabla f(x),y-x\rangle}_{\text{linear lower model}}
\;\le\;f(y)\;\le\;
\underbrace{f(x)+\langle\nabla f(x),y-x\rangle
+\frac{\beta}{2}\lVert y-x\rVert_2^2}_{\text{quadratic upper model}}.
$$

This “sandwich” explains the roles of the assumptions:

- Convexity connects local gradient information to global optimality.
- Smoothness bounds the error made by the local linear approximation.

### 4.4 Where the descent lemma comes from

Let $h=y-x$. Along the line segment from $x$ to $y$,

$$
f(y)-f(x)=\int_0^1\langle\nabla f(x+sh),h\rangle\,ds.
$$

Subtract the linear approximation:

$$
\begin{aligned}
f(y)-f(x)-\langle\nabla f(x),h\rangle
&=\int_0^1\langle\nabla f(x+sh)-\nabla f(x),h\rangle\,ds\\
&\le\int_0^1\beta s\lVert h\rVert_2^2\,ds\\
&=\frac{\beta}{2}\lVert h\rVert_2^2.
\end{aligned}
$$

The inequality uses Cauchy–Schwarz and gradient Lipschitz continuity. Notice that this derivation does not require convexity.

## 5. Why $1/\beta$ is a safe step size

Substitute $y=x-\eta\nabla f(x)$ into the descent lemma:

$$
\begin{aligned}
f(x-\eta\nabla f(x))
&\le f(x)-\eta\lVert\nabla f(x)\rVert_2^2
+\frac{\beta\eta^2}{2}\lVert\nabla f(x)\rVert_2^2\\
&=f(x)-\eta\left(1-\frac{\beta\eta}{2}\right)
\lVert\nabla f(x)\rVert_2^2.
\end{aligned}
$$

Choosing $\eta=1/\beta$ yields the lecture's descent guarantee:

$$
\boxed{f(x_{t+1})\le f(x_t)-\frac{1}{2\beta}\lVert g_t\rVert_2^2.}
$$

Thus objective values never increase.

There is also a useful model-based interpretation. The quadratic upper model

$$
q_x(y)=f(x)+\langle g,y-x\rangle+\frac{\beta}{2}\lVert y-x\rVert_2^2
$$

is minimized when

$$
\nabla_yq_x(y)=g+\beta(y-x)=0,
$$

which gives $y=x-g/\beta$. Gradient descent with this step minimizes a tractable upper model of the objective.

### Worked example: safe steps versus overshooting

Let

$$
f(x)=2x^2,\qquad f'(x)=4x,\qquad\beta=4.
$$

The update is

$$
x_{t+1}=(1-4\eta)x_t.
$$

Starting from $x_0=1$:

| Step size | Update multiplier | Behavior |
|---|---:|---|
| $\eta=1/8$ | $1/2$ | $1,\frac12,\frac14,\ldots$ |
| $\eta=1/4=1/\beta$ | $0$ | Reaches the optimum in one step |
| $\eta=1/2=2/\beta$ | $-1$ | Oscillates: $1,-1,1,-1,\ldots$ |
| $\eta=3/4$ | $-2$ | Diverges: $1,-2,4,-8,\ldots$ |

This directly computed example illustrates why step size must respect curvature.

## 6. The main theorem: $O(1/T)$ error for the last iterate

Assume:

1. $f:\mathbb R^d\to\mathbb R$ is convex.
2. $f$ is $\beta$-smooth.
3. A minimizer $x^*$ exists.
4. $\lVert x_0-x^*\rVert_2\le D$.
5. $x_{t+1}=x_t-\nabla f(x_t)/\beta$.

Then, for $T\ge1$,

$$
\boxed{f(x_T)-f(x^*)\le\frac{\beta D^2}{2T}.}
$$

The lecture proves this for unconstrained minimization.

### Step 1: Expand squared distance

Let

$$
R_t=\lVert x_t-x^*\rVert_2^2,\qquad g_t=\nabla f(x_t).
$$

Then

$$
R_{t+1}=R_t-\frac{2}{\beta}\langle g_t,x_t-x^*\rangle
+\frac{1}{\beta^2}\lVert g_t\rVert_2^2.
$$

Rearrange:

$$
\boxed{
\frac{\beta}{2}(R_t-R_{t+1})
=\langle g_t,x_t-x^*\rangle-\frac{1}{2\beta}\lVert g_t\rVert_2^2.
}
\tag{A}
$$

### Step 2: Combine descent with convexity

Descent gives

$$
f(x_{t+1})-f(x^*)
\le f(x_t)-f(x^*)-\frac{1}{2\beta}\lVert g_t\rVert_2^2.
$$

Convexity gives

$$
f(x_t)-f(x^*)\le\langle g_t,x_t-x^*\rangle.
$$

Consequently,

$$
\begin{aligned}
f(x_{t+1})-f(x^*)
&\le\langle g_t,x_t-x^*\rangle-\frac{1}{2\beta}\lVert g_t\rVert_2^2\\
&=\frac{\beta}{2}(R_t-R_{t+1}),
\end{aligned}
$$

where the last equality uses (A).

### Step 3: See the cancellation explicitly

Equivalently, the distance identity says

$$
\langle g_t,x_t-x^*\rangle
=\frac{\beta}{2}(R_t-R_{t+1})+\frac{1}{2\beta}\lVert g_t\rVert_2^2.
$$

Substitute into the preceding objective bound:

$$
\begin{aligned}
f(x_{t+1})-f(x^*)
&\le\frac{\beta}{2}(R_t-R_{t+1})
+\underbrace{\frac{1}{2\beta}\lVert g_t\rVert_2^2}_{\text{distance expansion}}
-\underbrace{\frac{1}{2\beta}\lVert g_t\rVert_2^2}_{\text{smooth descent}}\\
&=\frac{\beta}{2}(R_t-R_{t+1}).
\end{aligned}
$$

Unlike the bounded-gradient proof, no gradient-norm penalty remains.

### Step 4: Telescope

Summing,

$$
\sum_{t=0}^{T-1}[f(x_{t+1})-f(x^*)]
\le\frac{\beta}{2}(R_0-R_T)\le\frac{\beta D^2}{2}.
$$

```text
(R₀ - R₁)
    + (R₁ - R₂)
          + (R₂ - R₃)
                + ...
                    + (Rₜ₋₁ - Rₜ)
---------------------------------
 R₀                          - Rₜ
```

### Step 5: Use monotonicity to obtain the last iterate

Because function values decrease,

$$
f(x_1)\ge f(x_2)\ge\cdots\ge f(x_T).
$$

Every one of the $T$ terms in the sum is therefore at least $f(x_T)-f(x^*)$. Hence

$$
T[f(x_T)-f(x^*)]\le\frac{\beta D^2}{2}.
$$

Dividing by $T$ proves the theorem. This is why averaging is unnecessary in this analysis.

### Pseudocode

```text
SMOOTH-GRADIENT-DESCENT(x0, beta, T, Gradient):
    require beta > 0
    require T >= 1

    x = x0

    for t = 0, ..., T-1:
        g = Gradient(x)
        x = x - g / beta

    return x
```

If a valid bound $D$ is known, choosing

$$
T\ge\max\left\{1,\left\lceil\frac{\beta D^2}{2\varepsilon}\right\rceil\right\}
$$

guarantees objective error at most $\varepsilon>0$.

## 7. Worked smooth example and convergence visualization

Consider

$$
f(a,b)=\frac12a^2+2b^2,\qquad\nabla f(a,b)=(a,4b).
$$

Its Hessian is

$$
\nabla^2f=\begin{pmatrix}1&0\\0&4\end{pmatrix},
$$

so $\beta=4$ is valid. Start at $x_0=(2,1)$, and use $\eta=1/4$. The coordinate updates are

$$
a_{t+1}=\frac34a_t,\qquad b_{t+1}=0.
$$

| $t$ | $x_t$ | $f(x_t)$ |
|---:|---|---:|
| 0 | $(2,1)$ | $4$ |
| 1 | $(1.5,0)$ | $1.125$ |
| 2 | $(1.125,0)$ | $0.6328125$ |
| 3 | $(0.84375,0)$ | Approximately $0.356$ |
| 4 | $(0.6328125,0)$ | Approximately $0.200$ |

```text
b
^
|                           • x₀=(2,1)
|                          /
|                         /
+--★------•------•------•------•------> a
  x*      x₄     x₃     x₂     x₁

After the first step, motion is along the a-axis toward the origin.
Not to scale.
```

Here $x^*=(0,0)$ and $D^2=5$, so the lecture guarantees

$$
f(x_T)-f(x^*)\le\frac{4\cdot5}{2T}=\frac{10}{T}.
$$

The actual errors are much smaller. A worst-case upper bound need not accurately predict the behavior of a particular objective.

### Comparing the rate shapes

To compare only the dependence on $T$, normalize away the problem-dependent constants:

| $T$ | $1/\sqrt T$ | $1/T$ |
|---:|---:|---:|
| 1 | 1 | 1 |
| 4 | 0.5 | 0.25 |
| 16 | 0.25 | 0.0625 |
| 100 | 0.1 | 0.01 |

Thus:

- Halving a $1/\sqrt T$ bound requires four times as many iterations.
- Halving a $1/T$ bound requires twice as many iterations.

The lecture's corresponding sufficient iteration counts are

$$
T\ge\frac{D^2G^2}{\varepsilon^2}
\quad\text{versus}\quad
T\ge\frac{\beta D^2}{2\varepsilon},
$$

with integer rounding as needed. Their constants differ, so the rate comparison is not a universal numerical comparison between arbitrary problems.

## 8. Important distinctions and common exam mistakes

1. Smoothness is not a gradient-magnitude bound. The quadratic $x^2/2$ is smooth despite having unbounded gradient.
2. Smoothness is not strong convexity. Smoothness bounds curvature from above; strong convexity bounds it away from zero from below. The lecture's $O(1/T)$ theorem does not require strong convexity.
3. Descent is not the same as convergence to a global optimum. The descent lemma works without convexity, but the global-error proof uses convexity essentially. A nonconvex stationary point need not be a local minimum.
4. Do not confuse objective error with distance error. The theorem bounds $f(x_T)-f(x^*)$, not directly $\lVert x_T-x^*\rVert_2$. Its assumptions and conclusion should be stated separately.
5. Keep the two proof indexings distinct. The bounded-gradient proof averages $x_0,\ldots,x_{T-1}$. The smooth proof sums errors at $x_1,\ldots,x_T$ and then bounds $x_T$.
6. Include projection and gradient-evaluation costs. A useful implementation-level accounting is

   $$
   O\!\left(T(C_{\mathrm{grad}}+C_{\mathrm{proj}}+d)\right),
   $$

   when these are uniform per-iteration cost bounds. Convexity alone does not make the required oracle or projection cheap.

## 9. Quick quiz

Try these before reading the answers.

### Questions

1. Compute the projection of $(-2,0.3,4)$ onto $[0,1]^3$.
2. True or false: if $f$ is $\beta$-smooth, then $\lVert\nabla f(x)\rVert_2\le\beta$ everywhere.
3. What assumption ensures that the average of feasible iterates remains feasible?
4. For a $\beta$-smooth objective, what step size does the lecture use, and what one-step descent inequality does it prove?
5. Which assumption gives

   $$
   f(x_t)-f(x^*)\le\langle\nabla f(x_t),x_t-x^*\rangle?
   $$

6. Why does the smooth proof give a last-iterate guarantee rather than only an average guarantee?
7. If $\beta=8$, $D=3$, and $\varepsilon=0.01$, how many iterations suffice under the smooth theorem?
8. A projected method stops changing at $x^*$, but $\nabla f(x^*)\ne0$. Must there be an error?

### Answer key

1. $(0,0.3,1)$.
2. False. Smoothness bounds changes in the gradient. For $f(x)=x^2/2$, $\beta=1$, but $f'(x)=x$ is unbounded.
3. Convexity of $K$.
4. $\eta=1/\beta$, giving

   $$
   f(x_{t+1})\le f(x_t)-\frac{1}{2\beta}\lVert\nabla f(x_t)\rVert_2^2.
   $$

5. Convexity of $f$.
6. Function values are nonincreasing, so the final error is no larger than the average of the errors at $x_1,\ldots,x_T$.
7.

   $$
   T\ge\frac{8\cdot9}{2(0.01)}=3600.
   $$

8. No. At a constrained optimum, a gradient step can point outside the feasible set and projection can return to the same point. The interval example in Section 2 demonstrates this.

## 10. Exam-style questions

These are original practice questions based on the lecture.

### Problem 1 — Projection geometry and necessity of assumptions: 15 points

Let $K\subseteq\mathbb R^d$ be nonempty, closed, and convex, and let $p=\Pi_K(u)$.

1. Prove $\langle u-p,z-p\rangle\le0$ for all $z\in K$.
2. Deduce

   $$
   \lVert p-z\rVert_2^2\le\lVert u-z\rVert_2^2-\lVert u-p\rVert_2^2.
   $$

3. Give a nonconvex set for which projection is not unique.

### Problem 2 — Projected subgradient convergence: 25 points

Suppose $f$ is convex, $x^*\in K$ minimizes $f$ over $K$, and

$$
\lVert x_0-x^*\rVert_2\le D,\qquad\lVert g_t\rVert_2\le G.
$$

For

$$
x_{t+1}=\Pi_K(x_t-\eta g_t),
$$

prove

$$
f\left(\frac1T\sum_{t=0}^{T-1}x_t\right)-f(x^*)
\le\frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
$$

Then choose the best constant $\eta>0$ for this upper bound, assuming $D,G>0$.

### Problem 3 — Smooth last-iterate convergence: 30 points

Suppose $f$ is convex and $\beta$-smooth on $\mathbb R^d$, with an attained minimizer $x^*$. Analyze

$$
x_{t+1}=x_t-\frac1\beta\nabla f(x_t).
$$

1. Derive the one-step descent inequality.
2. Prove

   $$
   f(x_{t+1})-f(x^*)
   \le\frac{\beta}{2}\left(\lVert x_t-x^*\rVert_2^2-\lVert x_{t+1}-x^*\rVert_2^2\right).
   $$

3. Derive the last-iterate bound.
4. Identify precisely where convexity and monotonicity enter.

### Problem 4 — Computation and interpretation: 15 points

Consider

$$
f(a,b)=a^2+3b^2,\qquad x_0=(3,2).
$$

1. Find the smallest valid global smoothness constant $\beta$.
2. Compute $x_1$ and $x_2$ using $\eta=1/\beta$.
3. Compute $f(x_2)$.
4. Compare this with the lecture's upper bound for $T=2$.

### Problem 5 — What survives without convexity? 15 points

Suppose $f$ is $\beta$-smooth and bounded below by $f_{\inf}$, but need not be convex.

For step size $1/\beta$, prove

$$
\min_{0\le t<T}\lVert\nabla f(x_t)\rVert_2^2
\le\frac{2\beta[f(x_0)-f_{\inf}]}{T}.
$$

Explain why this is not a global-optimality guarantee.

## 11. Exam solutions and grading checkpoints

### Solution 1

For parts 1–2, use the feasible segment $p+\theta(z-p)$, differentiate squared distance at $\theta=0$, and expand $\lVert u-z\rVert_2^2$, as in Section 3.

For part 3, choose

$$
K=\{-1,1\},\qquad u=0.
$$

Both points are equally close to $u$, so projection is not unique.

Grading checkpoints: feasible segment, correct inner-product sign, correct expansion, valid counterexample.

### Solution 2

Projection and the subgradient inequality give

$$
f(x_t)-f(x^*)\le\frac{R_t-R_{t+1}}{2\eta}+\frac{\eta G^2}{2}.
$$

Summing and discarding $-R_T/(2\eta)$,

$$
\frac1T\sum_{t=0}^{T-1}[f(x_t)-f(x^*)]
\le\frac{D^2}{2\eta T}+\frac{\eta G^2}{2}.
$$

Convexity at the average gives the desired statement.

To minimize the bound, differentiate with respect to $\eta$:

$$
-\frac{D^2}{2T\eta^2}+\frac{G^2}{2}=0.
$$

Thus

$$
\eta=\frac{D}{G\sqrt T},\qquad
f(\bar x_T)-f(x^*)\le\frac{DG}{\sqrt T}.
$$

Grading checkpoints: projection inequality, subgradient inequality, telescoping, averaging, optimized step size. This matches the lecture's analysis.

### Solution 3

The descent lemma gives

$$
f(x_{t+1})\le f(x_t)-\frac{\lVert g_t\rVert_2^2}{2\beta}.
$$

The distance identity gives

$$
\langle g_t,x_t-x^*\rangle
=\frac{\beta}{2}(R_t-R_{t+1})+\frac{\lVert g_t\rVert_2^2}{2\beta}.
$$

Convexity bounds $f(x_t)-f(x^*)$ by the inner product. Substitution cancels the gradient-squared terms:

$$
f(x_{t+1})-f(x^*)\le\frac{\beta}{2}(R_t-R_{t+1}).
$$

Summing and using monotonicity,

$$
T[f(x_T)-f(x^*)]\le\frac{\beta}{2}(R_0-R_T)\le\frac{\beta D^2}{2}.
$$

Convexity enters when replacing the objective gap by an inner product. Monotonicity enters when replacing the sum of errors by $T$ times the final error.

### Solution 4

The gradient and Hessian are

$$
\nabla f(a,b)=(2a,6b),\qquad
\nabla^2f=\begin{pmatrix}2&0\\0&6\end{pmatrix}.
$$

Therefore $\beta=6$, and

$$
a_{t+1}=\frac23a_t,\qquad b_{t+1}=0.
$$

Hence

$$
x_1=(2,0),\qquad x_2=\left(\frac43,0\right),
$$

and

$$
f(x_2)=\frac{16}{9}.
$$

Since $x^*=(0,0)$ and $D^2=3^2+2^2=13$, the theorem gives

$$
f(x_2)-f(x^*)\le\frac{6\cdot13}{2\cdot2}=19.5.
$$

The actual error $16/9$ is below the bound. The theorem is valid but conservative here.

### Solution 5

The smooth descent inequality does not require convexity:

$$
\frac{1}{2\beta}\lVert\nabla f(x_t)\rVert_2^2
\le f(x_t)-f(x_{t+1}).
$$

Sum to obtain

$$
\sum_{t=0}^{T-1}\lVert\nabla f(x_t)\rVert_2^2
\le2\beta[f(x_0)-f(x_T)]
\le2\beta[f(x_0)-f_{\inf}].
$$

The minimum is at most the average, so

$$
\boxed{
\min_{0\le t<T}\lVert\nabla f(x_t)\rVert_2^2
\le\frac{2\beta[f(x_0)-f_{\inf}]}{T}.
}
$$

This proves that some queried iterate has a small gradient. It does not prove that its objective value is close to the global minimum: without convexity, a small or zero gradient need not identify a minimum. This extends the lecture's descent inequality while respecting its warning about nonconvex objectives.

## 12. Textbook reading guide

### Closest match: Sébastien Bubeck

Sébastien Bubeck, *Convex Optimization: Algorithms and Complexity*, Foundations and Trends in Machine Learning, 2015.

Read:

- Section 3.1, “Projected subgradient descent for Lipschitz functions.”
- Section 3.2, “Gradient descent for smooth functions.”
- Section 3.4, “Strong convexity,” as a follow-on topic.
- Section 3.7, “Nesterov's accelerated gradient descent,” after mastering the present proofs.

Sections 3.1–3.2 are the closest match to this lecture's assumptions, algorithms, and convergence analysis. Be aware that indexing and constants can differ across presentations.

[Full monograph (PDF)](http://sbubeck.com/Bubeck15.pdf) · [arXiv record](https://arxiv.org/abs/1405.4980)

### Best for geometric foundations: Boyd and Vandenberghe

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004.

Relevant sections:

- Section 2.1: affine and convex sets.
- Section 3.1: basic properties of convex functions.
- Section 8.1: projection on a set.
- Section 9.2: descent methods.
- Section 9.3: gradient descent.

Use this book to strengthen the geometry, first-order inequalities, quadratic models, and algorithmic context. Its gradient-descent treatment is broader than the specific $O(1/T)$ proof in your notes.

[Full textbook (PDF)](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

### More advanced theory: Yurii Nesterov

Yurii Nesterov, *Introductory Lectures on Convex Optimization: A Basic Course*, Springer, 2004.

Chapter 2, “Smooth Convex Optimization,” provides a deeper treatment of smooth first-order optimization and its complexity. It is a useful next step once you can reproduce the lecture's potential-function argument without looking at the notes.

[Publisher's book page](https://link.springer.com/book/10.1007/978-1-4419-8853-9)

For exam preparation, prioritize reconstructing this chain:

$$
\boxed{
\begin{gathered}
\text{update}\;\longrightarrow\;\text{distance expansion}\\
\longrightarrow\;\text{convexity + smooth descent}\\
\longrightarrow\;\text{cancellation}\;\longrightarrow\;\text{telescoping}\\
\longrightarrow\;\text{last-iterate bound}.
\end{gathered}
}
$$
