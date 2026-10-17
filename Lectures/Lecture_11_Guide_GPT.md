# Lecture 11 Study Guide: Why Strong Duality Holds

The central idea of this lecture is that an optimal solution comes with a matching **certificate**: a nonnegative weighted combination of the constraints that proves no feasible solution can have a better objective value. Strong duality guarantees that such a certificate exists whenever the primal linear program is feasible and has a finite optimum. The lecture proves this through geometry, Farkas' lemma, and the constraints that are tight at an optimum.

This guide follows the lecture's proof, adds worked examples and text-based visualizations, and finishes with pseudocode, quizzes, exam-style problems, solutions, and textbook reading recommendations.

> Lecture source: *CS 6515: Graduate Algorithms, Lecture 11: Why Strong Duality Holds*, Sahil Singla and Gerandy Brito, Fall 2026. Based on the uploaded lecture note, `Lec_11_Unmarked.pdf`. Additional textbook sources are linked in Section 14.
>
> Math formatting: this file uses GitHub-supported inline math (`$...$`) and display math (`$$...$$`). Diagrams and pseudocode appear in fenced code blocks.

## 1. The big picture

Consider the primal–dual pair used throughout the lecture:

$$
\begin{aligned}
(P)\qquad
\max_x\quad &c^\top x\\
\text{subject to}\quad &Ax\le b,\\
&x\ge0,
\end{aligned}
$$

$$
\begin{aligned}
(D)\qquad
\min_y\quad &b^\top y\\
\text{subject to}\quad &A^\top y\ge c,\\
&y\ge0.
\end{aligned}
$$

Here:

- $x\in\mathbb R^n$ contains the primal decision variables.
- $A\in\mathbb R^{m\times n}$ describes the constraints.
- $b\in\mathbb R^m$ contains the resource limits.
- $c\in\mathbb R^n$ contains the objective coefficients.
- $y\in\mathbb R^m$ assigns a nonnegative weight to each primal constraint.

### Weak duality: every feasible dual solution gives an upper bound

If $x$ and $y$ are primal- and dual-feasible, then

$$
c^\top x
\le
(A^\top y)^\top x
=
y^\top Ax
\le
y^\top b.
$$

The first inequality uses $A^\top y\ge c$ and $x\ge0$. The second uses $Ax\le b$ and $y\ge0$.

Therefore,

$$
\boxed{c^\top x\le b^\top y.}
$$

Every primal-feasible objective value is at most every dual-feasible objective value.

### Strong duality: the best upper bound is exact

If the primal is feasible and has a finite optimum, there are optimal solutions $x^*$ and $y^*$ satisfying

$$
\boxed{c^\top x^*=b^\top y^*.}
$$

Weak duality tells us that dual upper bounds are valid. Strong duality tells us that an exact one exists.

```text
Primal feasible values                 Dual feasible values
        increase →                         ← decrease

----------------------------●----------------------------
                         common optimum

           max cᵀx = min bᵀy
```

The lecture's question is not just “What does strong duality say?” It is “Why must the matching dual solution exist?”

---

## 2. A worked example to carry through the lecture

Consider the following example:

$$
\begin{aligned}
\max\quad &3x_1+2x_2\\
\text{subject to}\quad
&x_1+x_2\le4,\\
&x_1\le2,\\
&x_2\le3,\\
&x_1,x_2\ge0.
\end{aligned}
$$

### 2.1 Visualizing the feasible region

The feasible vertices are

$$
(0,0),\ (2,0),\ (2,2),\ (1,3),\ (0,3).
$$

A schematic picture is:

```text
x₂
↑
3   ●────● (1,3)
    │     \
    │      \  x₁ + x₂ = 4
2   │       ★ (2,2)
    │       │
1   │       │  x₁ = 2
    │       │
0   ●───────●────────→ x₁
    0       2
```

Evaluating the objective at these vertices gives:

| Point | $3x_1+2x_2$ |
|---|---:|
| $(0,0)$ | $0$ |
| $(2,0)$ | $6$ |
| $(2,2)$ | $10$ |
| $(1,3)$ | $9$ |
| $(0,3)$ | $6$ |

The candidate optimum is

$$
x^*=(2,2),\qquad c^\top x^*=10.
$$

We can prove optimality without relying on vertex enumeration.

### 2.2 Build an upper-bound certificate

Take:

- Twice the constraint $x_1+x_2\le4$.
- Once the constraint $x_1\le2$.
- Zero times the constraint $x_2\le3$.

Adding gives

$$
2(x_1+x_2)+x_1\le2(4)+2,
$$

so

$$
3x_1+2x_2\le10.
$$

Because $(2,2)$ attains $10$, it is optimal.

The multipliers are

$$
y=(2,1,0).
$$

They are dual variables: their role is to combine primal constraints into an objective upper bound. This is the certificate interpretation of LP duality.

### 2.3 Write the dual explicitly

The dual is

$$
\begin{aligned}
\min\quad &4y_1+2y_2+3y_3\\
\text{subject to}\quad
&y_1+y_2\ge3,\\
&y_1+y_3\ge2,\\
&y_1,y_2,y_3\ge0.
\end{aligned}
$$

For $y^*=(2,1,0)$,

$$
y_1+y_2=3,\qquad y_1+y_3=2,
$$

and

$$
4y_1+2y_2+3y_3=8+2=10.
$$

Thus

$$
c^\top x^*=b^\top y^*=10.
$$

The primal solution proves that a value of $10$ is achievable. The dual solution proves that no value above $10$ is achievable.

---

## 3. Active constraints and outward normals

The lecture's geometric proof focuses on constraints that are tight at a candidate optimum.

### 3.1 Active versus inactive constraints

A constraint

$$
a_r^\top x\le d_r
$$

is active, or tight, at $x^*$ when

$$
a_r^\top x^*=d_r.
$$

It is inactive when

$$
a_r^\top x^*<d_r.
$$

For the worked example at $x^*=(2,2)$:

| Constraint | Value at $x^*$ | Status |
|---|---:|---|
| $x_1+x_2\le4$ | $4=4$ | Active |
| $x_1\le2$ | $2=2$ | Active |
| $x_2\le3$ | $2<3$ | Inactive |
| $-x_1\le0$ | $-2<0$ | Inactive |
| $-x_2\le0$ | $-2<0$ | Inactive |

### 3.2 What an outward normal means

For

$$
a^\top x\le d,
$$

the vector $a$ points toward increasing $a^\top x$: the direction that eventually violates the constraint.

If the constraint is active, a direction $v$ is locally permissible only if

$$
a^\top v\le0.
$$

Indeed,

$$
a^\top(x^*+\varepsilon v)
=
d+\varepsilon a^\top v.
$$

If $a^\top v>0$, every positive step violates the active constraint. If $a^\top v\le0$, the constraint remains satisfied.

### 3.3 The geometric condition for optimality

At an optimum,

$$
\boxed{
c=\sum_{r\in S}\lambda_r a_r,
\qquad \lambda_r\ge0,
}
$$

where $S$ is the active set, including active nonnegativity constraints. The objective direction lies in the cone generated by the active outward normals.

In the example,

$$
a_1=(1,1),\qquad a_2=(1,0),
$$

and

$$
c=(3,2)=2(1,1)+(1,0).
$$

```text
Direction space

second coordinate
↑
│        a₁ = (1,1)
│       ↗
│      /   c = (3,2)
│     /   ↗
│    /  /
└──────────────────→ first coordinate
       a₂ = (1,0) →

c lies between the two active normal rays.
```

Why does this block improvement? Any direction satisfying

$$
a_r^\top v\le0
\quad\text{for all active }r
$$

must also satisfy

$$
c^\top v
=
\sum_{r\in S}\lambda_r a_r^\top v
\le0.
$$

So every locally feasible direction fails to increase the objective. The hard part is proving the converse: if no improving direction exists, why must these nonnegative multipliers exist? Farkas' lemma supplies that implication.

---

## 4. Farkas' lemma: either a representation or a separating witness

Let

$$
M=[a_1\ \cdots\ a_k].
$$

The equation

$$
M\lambda=p,\qquad\lambda\ge0
$$

asks whether $p$ can be expressed as a nonnegative combination of the columns of $M$.

Farkas' lemma says exactly one of the following systems is feasible:

$$
\begin{aligned}
\text{I:}\qquad &M\lambda=p,\\
&\lambda\ge0;
\end{aligned}
$$

or

$$
\begin{aligned}
\text{II:}\qquad &M^\top w\ge0,\\
&p^\top w<0.
\end{aligned}
$$

The vector $w$ is unrestricted in sign.

### 4.1 What the two alternatives mean

- System I gives a construction: coefficients that build $p$.
- System II gives an impossibility certificate: a linear measurement that is nonnegative on every generator but negative on $p$.

### 4.2 Why both cannot hold

Suppose both systems had solutions. Then

$$
p^\top w
=
(M\lambda)^\top w
=
\lambda^\top M^\top w
\ge0,
$$

because both $\lambda$ and $M^\top w$ are componentwise nonnegative.

But System II requires $p^\top w<0$, a contradiction. The nontrivial part of the lemma is proving that one alternative always exists.

### 4.3 Worked example

Use the lecture's vectors

$$
a_1=(1,0),\qquad a_2=(1,1),\qquad p=(0,1).
$$

A nonnegative combination is

$$
\lambda_1a_1+\lambda_2a_2
=
(\lambda_1+\lambda_2,\lambda_2).
$$

To equal $(0,1)$, we would need

$$
\lambda_2=1,\qquad\lambda_1=-1,
$$

which violates nonnegativity.

A separating certificate is

$$
w=(1,-1).
$$

Check:

$$
a_1^\top w=1,\qquad
a_2^\top w=0,\qquad
p^\top w=-1.
$$

Thus $p$ cannot be a nonnegative combination of $a_1$ and $a_2$.

```text
second coordinate
↑
│ p = (0,1)
│ ●
│          /  a₂ ray: x₂ = x₁
│         /░
│        /░░  cone C
│       /░░░  x₁ ≥ x₂ ≥ 0
└────────────────────────→ first coordinate
            a₁ ray

wᵀz = z₁ − z₂ ≥ 0 throughout C,
but wᵀp = −1.
```

---

## 5. Why separation works: use the nearest point

The lecture proves the relevant separating-hyperplane theorem using a nearest-point argument.

Let $C$ be a nonempty, closed, convex set, and let $p\notin C$. Choose a point $q\in C$ closest to $p$, and define

$$
v=p-q.
$$

Then

$$
v^\top z\le v^\top q<v^\top p
\quad\text{for every }z\in C.
$$

### 5.1 The geometric intuition

```text
       closed convex set C
       __________
      /          \
     /            ● q ─────────→ ● p
     \____________/    v = p − q

A supporting hyperplane through q is
perpendicular to v.
```

If another feasible point $z$ lay in a direction that had a positive component toward $p$, a short move from $q$ toward $z$ would get closer to $p$. That would contradict the choice of $q$.

### 5.2 The calculation

Convexity implies

$$
q+\theta(z-q)\in C
\qquad\text{for }0\le\theta\le1.
$$

Its squared distance to $p$ is

$$
\begin{aligned}
\|p-(q+\theta(z-q))\|^2
&=\|v-\theta(z-q)\|^2\\
&=\|v\|^2
-2\theta v^\top(z-q)
+\theta^2\|z-q\|^2.
\end{aligned}
$$

If $v^\top(z-q)>0$, the negative term dominates for sufficiently small positive $\theta$. The new point would be closer to $p$.

Therefore,

$$
v^\top(z-q)\le0.
$$

Also,

$$
v^\top p-v^\top q
=
v^\top(p-q)
=
\|p-q\|^2>0.
$$

These facts give the separating inequalities.

### 5.3 Specializing to a finitely generated cone

For

$$
C=\left\{\sum_j\lambda_ja_j:\lambda_j\ge0\right\},
$$

the lecture uses the standard fact that a finitely generated cone is closed and convex.

If $v^\top a_j>0$ for some generator, scaling that generator would make $v^\top z$ arbitrarily large. This contradicts the finite separating upper bound.

Hence

$$
v^\top a_j\le0
\quad\text{for all }j.
$$

Since $0\in C$, the maximum of $v^\top z$ over the cone is $0$, while

$$
v^\top p>0.
$$

Setting $w=-v$ gives

$$
M^\top w\ge0,\qquad p^\top w<0,
$$

which is the Farkas certificate.

---

## 6. The strong-duality proof, step by step

This is the main proof to be able to reconstruct on an exam.

### Step 1: Include every inequality

Rewrite all constraints as

$$
a_r^\top x\le d_r.
$$

This includes the original $m$ rows of $Ax\le b$ and the $n$ nonnegativity rows

$$
-e_i^\top x\le0.
$$

Let $S$ contain the rows tight at an optimal solution $x^*$.

### Step 2: Claim that the objective belongs to the active-normal cone

We want to prove

$$
c=\sum_{r\in S}\lambda_ra_r,
\qquad\lambda_r\ge0.
$$

Suppose no such coefficients exist.

Apply Farkas' lemma to the matrix whose columns are the active normals, using $c$ as the target. It gives a vector $w$ with

$$
a_r^\top w\ge0
\quad(r\in S),
\qquad
c^\top w<0.
$$

Set

$$
v=-w.
$$

Then

$$
a_r^\top v\le0
\quad(r\in S),
\qquad
c^\top v>0.
$$

Thus $v$ respects every active constraint and improves the objective.

### Step 3: Show that a small step respects inactive constraints

Consider

$$
x'=x^*+\varepsilon v.
$$

For an active row,

$$
a_r^\top x'
=
d_r+\varepsilon a_r^\top v
\le d_r.
$$

For an inactive row, define its positive slack

$$
\delta_r=d_r-a_r^\top x^*>0.
$$

If $a_r^\top v\le0$, the row cannot become violated as we move in that direction.

If $a_r^\top v>0$, feasibility requires

$$
\varepsilon
\le
\frac{\delta_r}{a_r^\top v}.
$$

There are only finitely many rows, so a sufficiently small positive $\varepsilon$ satisfies all of them.

### Step 4: Contradict optimality

The new objective is

$$
c^\top x'
=
c^\top x^*+\varepsilon c^\top v
>
c^\top x^*.
$$

This contradicts optimality. Therefore the claimed nonnegative representation exists.

### Step 5: Extract the dual variables

Give inactive rows multiplier zero.

Split the multipliers into:

- $y\ge0$, for the original rows $Ax\le b$.
- $z\ge0$, for the rows $-x_i\le0$.

The representation becomes

$$
c=A^\top y-z.
$$

Thus

$$
A^\top y=c+z\ge c,
$$

so $y$ is dual-feasible.

### Step 6: Show that the values match

Every row with a positive multiplier is tight. The nonnegativity rows have right-hand side zero. Consequently,

$$
\begin{aligned}
c^\top x^*
&=\sum_r\lambda_ra_r^\top x^*\\
&=\sum_r\lambda_rd_r\\
&=b^\top y.
\end{aligned}
$$

Weak duality now proves that $y$ is dual-optimal.

### Proof roadmap

```text
No nonnegative combination of active normals equals c
                         │
                         ▼
                   Farkas' lemma
                         │
                         ▼
       Direction v respects active constraints
                  and satisfies cᵀv > 0
                         │
                         ▼
       A small step also respects inactive rows
                         │
                         ▼
             Better feasible solution
                         │
                         ▼
             Contradiction to optimality
                         │
                         ▼
          Active-normal multipliers exist
                         │
                         ▼
       Dual-feasible solution with matching value
```

---

## 7. Three subtleties that often cause mistakes

### 7.1 Nonnegativity constraints have normals too

Consider the lecture's example

$$
\max -x
\quad\text{subject to}\quad
x\le1,\quad x\ge0.
$$

The optimum is $x^*=0$.

At this point:

- $x\le1$ is inactive.
- $-x\le0$ is active.
- The objective coefficient is $c=-1$.

The active nonnegativity normal supplies the objective direction:

$$
-1=1\cdot(-1).
$$

Ignoring nonnegativity would leave no active normal capable of representing $c$.

The dual is

$$
\min y
\quad\text{subject to}\quad
y\ge-1,\quad y\ge0.
$$

The optimal pair is

$$
x^*=0,\qquad y^*=0,
$$

with common value $0$.

### 7.2 Tight does not imply a positive multiplier

Consider

$$
\begin{aligned}
\max\quad &x_1\\
\text{subject to}\quad
&x_1\le1,\\
&x_2\le0,\\
&x_1,x_2\ge0.
\end{aligned}
$$

The unique feasible maximizer is $(1,0)$.

The dual multiplier choice

$$
y=(1,0)
$$

is optimal, even though the second original constraint is tight.

The correct implications are

$$
y_j>0
\implies
a_j^\top x=b_j,
$$

and

$$
a_j^\top x<b_j
\implies
y_j=0.
$$

The reverse implication “tight implies positive” is not required. This addresses one of the lecture's checks for understanding.

### 7.3 The optimal solution need not be a vertex

For the constructed example

$$
\max x_1
\quad\text{subject to}\quad
0\le x_1\le1,\quad 0\le x_2\le1,
$$

every point on the edge

$$
\{(1,t):0\le t\le1\}
$$

is optimal.

The point $(1,\tfrac12)$ is not a vertex, but its active normal $(1,0)$ already equals the objective direction.

The lecture's proof works at any optimal solution; it does not require selecting a vertex.

---

## 8. Complementary slackness and approximate certificates

These are useful consequences of the lecture's multiplier construction.

### 8.1 Decomposing the duality gap

For any feasible $x,y$,

$$
\begin{aligned}
b^\top y-c^\top x
&=y^\top(b-Ax)+x^\top(A^\top y-c).
\end{aligned}
$$

Both terms are nonnegative.

Therefore the gap is zero exactly when every componentwise product vanishes:

$$
\boxed{
y_j(b_j-a_j^\top x)=0
\quad\text{for every }j,
}
$$

and

$$
\boxed{
x_i((A^\top y)_i-c_i)=0
\quad\text{for every }i.
}
$$

These are the complementary-slackness conditions. They make precise the relationship between tight constraints and nonzero multipliers.

In words:

- A positive constraint multiplier requires zero primal slack.
- A positive primal variable requires a tight corresponding dual constraint.
- A zero multiplier does not force positive slack.
- A zero primal variable does not force strict dual slack.

### 8.2 Approximate optimality

Suppose $x,y$ are feasible and

$$
b^\top y-c^\top x\le\varepsilon.
$$

Weak duality gives

$$
c^\top x\le\operatorname{OPT}\le b^\top y.
$$

Subtracting $c^\top x$,

$$
\boxed{
0\le\operatorname{OPT}-c^\top x\le\varepsilon.
}
$$

So the feasible pair certifies that $x$ is within $\varepsilon$ of optimal in objective value. This is one of the lecture's exercises.

For example, a primal value of $9.97$ and a dual value of $10.02$ certify an objective error of at most $0.05$, provided both solutions are feasible.

---

## 9. Pseudocode

The following routines translate the proof into computational tasks. The lecture establishes the underlying alternatives; the pseudocode below is an instructional implementation of those ideas.

### 9.1 Verify a primal–dual certificate

```text
VERIFY_CERTIFICATE(A, b, c, x, y):
    if any component of x < 0:
        return "Primal infeasible"

    if any component of A*x > b:
        return "Primal infeasible"

    if any component of y < 0:
        return "Dual infeasible"

    if any component of transpose(A)*y < c:
        return "Dual infeasible"

    primal_value = dot(c, x)
    dual_value   = dot(b, y)
    gap          = dual_value - primal_value

    if gap == 0:
        return "Both optimal", primal_value
    else:
        return "Certified primal error at most", gap
```

Once candidate solutions are supplied, verification requires matrix–vector products and comparisons, rather than solving another optimization problem.

The pseudocode uses exact comparisons. For floating-point implementations, feasibility residuals and numerical tolerances must be handled explicitly; a nearly feasible pair should not automatically be treated as an exact mathematical certificate.

### 9.2 Find a certificate or an improving direction

Let

$$
B=
\begin{bmatrix}
A\\
-I
\end{bmatrix},
\qquad
d=
\begin{bmatrix}
b\\
0
\end{bmatrix}.
$$

Then all primal inequalities are $Bx\le d$.

```text
CERTIFICATE_OR_DIRECTION(A, b, c, x):
    require x is feasible

    B = vertically_stack(A, -IdentityMatrix(n))
    d = concatenate(b, ZeroVector(n))

    S = {r : dot(B[r], x) == d[r]}

    solve the feasibility problem:
        transpose(B[S]) * lambda = c
        lambda >= 0

    if feasible:
        full_lambda = ZeroVector(m + n)
        full_lambda[S] = lambda

        y = first m entries of full_lambda

        return "Optimality certificate", y

    otherwise:
        solve the feasibility problem:
            B[S] * v <= 0
            dot(c, v) >= 1

        return "Improving direction", v
```

The normalization

$$
c^\top v\ge1
$$

is valid because any direction with $c^\top v>0$ can be scaled.

This routine uses LP-feasibility subroutines. It illustrates the theorem; it is not a new standalone LP-solving algorithm or a claim that repeated local steps have a particular convergence rate.

### 9.3 Take a safe step

```text
SAFE_STEP(B, d, c, x, v):
    require x is feasible
    require dot(c, v) > 0
    require dot(B[r], v) <= 0 for every active row r

    step_limit = infinity

    for each row r:
        rate = dot(B[r], v)

        if rate > 0:
            slack = d[r] - dot(B[r], x)
            step_limit = min(step_limit, slack / rate)

    if step_limit == infinity:
        return "Objective is unbounded along this ray"

    epsilon = min(1, step_limit / 2)

    return x + epsilon*v
```

When the step limit is finite, this chooses a positive step strictly below the first blocking constraint. If no constraint blocks the improving ray, the objective is unbounded along it.

### Example of the step calculation

In the running example, take

$$
x=(2,1),\qquad v=(0,1).
$$

The objective rate is

$$
c^\top v=(3,2)^\top(0,1)=2>0.
$$

The potentially blocking constraints give:

$$
x_1+x_2\le4:
\qquad
\varepsilon\le\frac{4-3}{1}=1,
$$

$$
x_2\le3:
\qquad
\varepsilon\le\frac{3-1}{1}=2.
$$

Thus the largest feasible step along this direction is $1$, reaching $(2,2)$. The conservative routine would take a smaller improving step.

---

## 10. Bridge to convex optimization

The lecture ends by replacing the fixed linear objective direction with a gradient. For a differentiable function,

$$
f(x+h)\approx f(x)+\nabla f(x)^\top h.
$$

An LP maximization can be rewritten as minimizing the convex linear function

$$
f(x)=-c^\top x.
$$

This connects the lecture's geometric argument to first-order optimality in convex optimization.

For a differentiable convex objective over a polyhedron

$$
Bx\le d,
$$

the corresponding multiplier condition is

$$
\nabla f(x^*)+B^\top\lambda=0,
\qquad
\lambda\ge0,
$$

together with feasibility and complementary slackness.

For the LP objective $f(x)=-c^\top x$, this becomes

$$
-c+B^\top\lambda=0,
$$

or

$$
c=B^\top\lambda.
$$

That is exactly the active-normal representation from the lecture. These feasibility, stationarity, and complementary-slackness conditions are the LP version of the Karush–Kuhn–Tucker framework.

---

## 11. Quick quiz

Try these before reading the answer key.

### Questions

1. For a feasible primal–dual pair in the lecture's maximization convention, which inequality holds?
   - A. $b^\top y\le c^\top x$
   - B. $c^\top x\le b^\top y$
   - C. The values must always be equal.

2. If $a^\top x^*=d$, what condition must a feasible direction $v$ satisfy for a small positive step?

3. What does $M\lambda=p,\ \lambda\ge0$ mean geometrically?

4. What two inequalities must a Farkas certificate $w$ satisfy?

5. True or false: every tight primal constraint must have a strictly positive multiplier in every optimal dual solution.

6. For

   $$
   \max -x,\qquad 0\le x\le1,
   $$

   which active normal represents the objective direction at the optimum?

7. A feasible primal solution has value $18.4$, and a feasible dual solution has value $18.7$. What objective-error guarantee follows?

8. True or false: the active-constraint proof requires $x^*$ to be a vertex.

### Answer key

1. B:

   $$
   c^\top x\le b^\top y.
   $$

2. It must satisfy

   $$
   a^\top v\le0.
   $$

3. The vector $p$ belongs to the cone generated by the columns of $M$.

4.

   $$
   M^\top w\ge0,\qquad p^\top w<0.
   $$

5. False. Tightness permits a positive multiplier but does not require one.

6. The normal $-1$ from the constraint $-x\le0$.

7.

   $$
   0\le\operatorname{OPT}-18.4\le0.3.
   $$

8. False. The proof applies to any optimal solution.

These answers follow from weak duality, Farkas' lemma, and the active-constraint argument in the lecture.

---

## 12. Exam-style practice

The following six problems form a suggested 100-point practice exam.

### Problem 1: Derive and verify a dual certificate — 20 points

Consider

$$
\begin{aligned}
\max\quad &4x_1+3x_2\\
\text{subject to}\quad
&x_1+x_2\le5,\\
&x_1\le2,\\
&x_2\le4,\\
&x_1,x_2\ge0.
\end{aligned}
$$

1. Write the dual.
2. Find optimal primal and dual solutions.
3. Prove optimality using a weighted combination of constraints.
4. Identify the active constraints and express $c$ using their normals.

### Problem 2: Farkas certificate — 15 points

Let

$$
M=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix},
\qquad
p=
\begin{bmatrix}
1\\
2
\end{bmatrix}.
$$

1. Show that $M\lambda=p,\ \lambda\ge0$ is infeasible.
2. Find a Farkas certificate $w$.
3. Explain geometrically which region contains the cone.

### Problem 3: Reconstruct the strong-duality proof — 20 points

Let $x^*$ be optimal for the lecture's primal LP.

1. Explain why the active set must include nonnegativity rows.
2. Suppose $c$ is not in the cone of active normals. State exactly what Farkas' lemma gives.
3. Construct an improving direction.
4. Explain how to choose a positive step that preserves every constraint.
5. Extract a dual solution and prove equality of objective values.

### Problem 4: Nonnegativity and complementary slackness — 20 points

Consider

$$
\begin{aligned}
\max\quad &-x_1+2x_2\\
\text{subject to}\quad
&x_1+x_2\le3,\\
&x_2\le2,\\
&x_1,x_2\ge0.
\end{aligned}
$$

1. Find the unique primal optimum.
2. Write the dual and find an optimal dual solution.
3. Identify the active normals.
4. Express $c=(-1,2)$ as a nonnegative combination of those normals.
5. Verify both sets of complementary-slackness conditions.

### Problem 5: Explicit feasible step — 15 points

For the running example,

$$
\max 3x_1+2x_2
$$

subject to

$$
x_1+x_2\le4,\quad x_1\le2,\quad x_2\le3,\quad x\ge0,
$$

take

$$
x=(2,1),\qquad v=(0,1).
$$

1. List the active constraints.
2. Check that $v$ respects them.
3. Calculate the largest feasible $\varepsilon\ge0$.
4. Calculate the objective improvement at that step.

### Problem 6: Gap decomposition and error bounds — 10 points

For a feasible pair $x,y$:

1. Derive

   $$
   b^\top y-c^\top x
   =
   y^\top(b-Ax)+x^\top(A^\top y-c).
   $$

2. Explain why both terms are nonnegative.
3. Prove that a gap of at most $\varepsilon$ certifies objective error at most $\varepsilon$.

---

## 13. Exam solutions

### Solution 1

The dual is

$$
\begin{aligned}
\min\quad &5y_1+2y_2+4y_3\\
\text{subject to}\quad
&y_1+y_2\ge4,\\
&y_1+y_3\ge3,\\
&y_1,y_2,y_3\ge0.
\end{aligned}
$$

Choose

$$
x^*=(2,3),
\qquad
y^*=(3,1,0).
$$

Both are feasible, and

$$
4(2)+3(3)=17,
$$

$$
5(3)+2(1)+4(0)=17.
$$

The upper-bound certificate is

$$
3(x_1+x_2)+x_1\le3(5)+2,
$$

hence

$$
4x_1+3x_2\le17.
$$

The active original constraints are $x_1+x_2=5$ and $x_1=2$. Their normals satisfy

$$
(4,3)=3(1,1)+(1,0).
$$

Matching feasible values prove optimality by weak duality.

### Solution 2

The equations are

$$
\lambda_1+\lambda_2=1,
\qquad
\lambda_2=2.
$$

Therefore $\lambda_1=-1$, so no nonnegative solution exists.

Choose

$$
w=(1,-1).
$$

Then

$$
M^\top w=
\begin{bmatrix}
1\\
0
\end{bmatrix}
\ge0,
$$

and

$$
p^\top w=1-2=-1<0.
$$

The cone is

$$
C=\{(u,v):u\ge v\ge0\}.
$$

The target $(1,2)$ lies above the line $v=u$, outside that cone. The inequalities above verify the Farkas certificate directly.

### Solution 3

A complete proof should contain this chain:

1. Include the rows $-e_i^\top x\le0$, since zero coordinates can block improving directions.

2. If $c$ is not a nonnegative combination of active normals, Farkas gives

   $$
   a_r^\top w\ge0,\qquad c^\top w<0.
   $$

3. Set $v=-w$, giving

   $$
   a_r^\top v\le0,\qquad c^\top v>0.
   $$

4. Active rows remain feasible. For every inactive row with $a_r^\top v>0$, require

   $$
   0<\varepsilon\le
   \frac{d_r-a_r^\top x^*}{a_r^\top v}.
   $$

   Finiteness of the constraint set ensures a common positive choice.

5. The resulting step improves the objective, contradicting optimality.

6. Thus active multipliers exist. Split them into $y,z\ge0$:

   $$
   c=A^\top y-z.
   $$

7. This makes $y$ dual-feasible. Tightness of positively weighted rows gives

   $$
   c^\top x^*=b^\top y.
   $$

These are the essential steps of the lecture's proof.

### Solution 4

Because $x_1\ge0$ and $x_2\le2$,

$$
-x_1+2x_2\le4.
$$

Equality requires $x_1=0$ and $x_2=2$, so the unique optimum is

$$
x^*=(0,2),
\qquad \operatorname{OPT}=4.
$$

The dual is

$$
\begin{aligned}
\min\quad &3y_1+2y_2\\
\text{subject to}\quad
&y_1\ge-1,\\
&y_1+y_2\ge2,\\
&y_1,y_2\ge0.
\end{aligned}
$$

An optimal solution is

$$
y^*=(0,2),
$$

with value $4$.

The active normals are

$$
(0,1)
\quad\text{from }x_2\le2,
$$

and

$$
(-1,0)
\quad\text{from }-x_1\le0.
$$

They represent the objective:

$$
(-1,2)=2(0,1)+1(-1,0).
$$

For complementary slackness, the primal slacks are

$$
b-Ax^*=(1,0),
$$

so

$$
y^*\odot(b-Ax^*)=(0,0).
$$

The dual slacks are

$$
A^\top y^*-c
=
(0,2)-(-1,2)
=
(1,0),
$$

so

$$
x^*\odot(A^\top y^*-c)=(0,0).
$$

Here $\odot$ denotes componentwise multiplication.

This example illustrates why the active nonnegativity normal cannot be omitted.

### Solution 5

Only $x_1\le2$ is active at $(2,1)$. Its normal is $(1,0)$, and

$$
(1,0)^\top v=0.
$$

Along the direction,

$$
x+\varepsilon v=(2,1+\varepsilon).
$$

The constraints require

$$
3+\varepsilon\le4,
$$

and

$$
1+\varepsilon\le3.
$$

Thus

$$
\varepsilon_{\max}=1.
$$

The objective improvement is

$$
\varepsilon_{\max}c^\top v
=
1\cdot2
=
2.
$$

The objective increases from $8$ to $10$, reaching $(2,2)$.

### Solution 6

Add and subtract $y^\top Ax$:

$$
\begin{aligned}
b^\top y-c^\top x
&=b^\top y-y^\top Ax+y^\top Ax-c^\top x\\
&=y^\top(b-Ax)+x^\top(A^\top y-c).
\end{aligned}
$$

All vectors in the componentwise products are nonnegative by primal and dual feasibility.

Finally,

$$
c^\top x\le\operatorname{OPT}\le b^\top y
$$

implies

$$
0\le\operatorname{OPT}-c^\top x
\le b^\top y-c^\top x
\le\varepsilon.
$$

This is the lecture's approximate-certificate argument.

---

## 14. Textbook reading guide

### 14.1 Closest match to this lecture

Dimitris Bertsimas and John N. Tsitsiklis, *Introduction to Linear Optimization*.

Read Chapter 4, especially:

- §4.2: The dual problem.
- §4.3: The duality theorem.
- §4.6: Farkas' lemma and linear inequalities.
- §4.7: From separating hyperplanes to duality.
- §4.8: Cones and extreme rays.

Sections 4.6–4.7 most closely match the lecture's geometric proof route.

[Table of contents](https://www.gbv.de/dms/ilmenau/toc/226515281.PDF)

### 14.2 Best algorithms-oriented companion

Sanjoy Dasgupta, Christos H. Papadimitriou, and Umesh V. Vazirani, *Algorithms*.

Read Chapter 7, particularly §7.4 on duality. Its emphasis on weighted combinations of constraints, matching primal–dual values, and max-flow/min-cut connects well to the surrounding algorithms lectures. An author-hosted chapter is publicly available.

[Author-hosted Chapter 7](https://people.eecs.berkeley.edu/~vazirani/algorithms/chap7.pdf)

### 14.3 Best bridge to the next convex-optimization material

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*.

Read:

- §2.5.1: Separating hyperplane theorem.
- §5.2: The Lagrange dual problem.
- §5.2.3: Strong duality and Slater's constraint qualification.
- §5.5: Optimality conditions, including complementary slackness and KKT conditions.

This text places LP duality within a broader theory of convex optimization. Be careful to track the sign convention: its general framework uses primal minimization, so dual values are lower bounds rather than the upper bounds used in this lecture's primal maximization formulation.

[Author-hosted textbook](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

## 15. What to prioritize when studying

You should be able to do the following without looking at the notes:

1. Derive weak duality and identify where nonnegativity is used.
2. State Farkas' lemma with the correct signs and strict inequality.
3. Explain why active rows govern sufficiently small feasible moves.
4. Compute an explicit step bound from inactive-row slacks.
5. Include nonnegativity normals in the active set.
6. Turn

   $$
   c=A^\top y-z,\qquad y,z\ge0
   $$

   into dual feasibility.

7. Use tightness to prove

   $$
   c^\top x^*=b^\top y.
   $$

8. Distinguish “positive multiplier implies tight” from the false converse.
9. Use a primal–dual gap to certify approximate optimality.

These skills capture the lecture's main relationship: geometry rules out improvement, Farkas converts that geometric obstruction into multipliers, and those multipliers become an exact dual certificate.
