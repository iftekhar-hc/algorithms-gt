# Lecture 11: Why Strong Duality Holds

The central question in `Lec_11_Unmarked.pdf` is not merely what linear-programming duality says, but **why an exact dual certificate must exist whenever the primal has a finite optimum**. The lecture builds the answer from three geometric ideas: separating hyperplanes, Farkas' lemma, and the normals of the constraints active at an optimal solution.

> **Notation warning:** The extracted PDF contains several OCR sign errors. In particular, the nonnegativity condition $x_i\ge 0$ should be written as $-x_i\le 0$, whose outward normal is $-e_i$. The explanation below uses the mathematically consistent signs.

---

## 1. Primal and dual linear programs

The lecture considers the primal LP

$$
\begin{aligned}
\text{(P)}\qquad
\max_x \quad & c^\top x\\
\text{subject to}\quad & Ax\le b,\\
&x\ge 0,
\end{aligned}
$$

and its dual

$$
\begin{aligned}
\text{(D)}\qquad
\min_y \quad & b^\top y\\
\text{subject to}\quad & A^\top y\ge c,\\
&y\ge 0.
\end{aligned}
$$

Here:

- $x\in\mathbb R^n$ contains primal decision variables;
- $y\in\mathbb R^m$ contains dual multipliers;
- each $y_j$ corresponds to one primal constraint;
- the primal seeks a value to maximize;
- the dual seeks an upper bound to minimize.

---

## 2. Weak duality: every dual solution is an upper-bound certificate

Suppose $x$ is primal-feasible and $y$ is dual-feasible. Then

$$
Ax\le b,\qquad A^\top y\ge c,\qquad x,y\ge 0.
$$

Since $y\ge0$, multiplying $Ax\le b$ by $y^\top$ preserves the inequality:

$$
y^\top Ax\le y^\top b.
$$

Since $x\ge0$ and $A^\top y\ge c$,

$$
c^\top x\le (A^\top y)^\top x=y^\top Ax.
$$

Combining them gives

$$
\boxed{c^\top x\le b^\top y.}
$$

Consequently,

$$
\boxed{\operatorname{OPT}_{P}\le \operatorname{OPT}_{D}.}
$$

This is **weak duality**. It says that every dual-feasible $y$ provides a verifiable upper bound on every primal-feasible value.

### Why this is a certificate

If someone gives us feasible $x$ and $y$ satisfying

$$
c^\top x=b^\top y,
$$

then weak duality proves immediately that both are optimal:

$$
c^\top x
\le \operatorname{OPT}_{P}
\le \operatorname{OPT}_{D}
\le b^\top y
= c^\top x.
$$

Therefore, all inequalities must be equalities.

The difficult part is proving that such a matching dual certificate **always exists** when the primal has a finite optimum.

---

## 3. The geometric picture at an optimum

Consider constraints written uniformly as

$$
a_r^\top x\le d_r.
$$

At a feasible point $x^*$:

- constraint $r$ is **active** or **tight** if $a_r^\top x^*=d_r$;
- it is **inactive** if $a_r^\top x^*<d_r$.

The vector $a_r$ is the normal to the constraint boundary.

### 3.1 Active constraints block movement

Suppose $a_r^\top x^*=d_r$. Moving from $x^*$ in direction $v$ gives

$$
a_r^\top(x^*+\varepsilon v)=d_r+\varepsilon a_r^\top v.
$$

For small $\varepsilon>0$:

- if $a_r^\top v>0$, the constraint is violated;
- if $a_r^\top v\le0$, the active constraint remains feasible.

Thus, a direction $v$ is locally allowed by all active constraints only if

$$
a_r^\top v\le0
\qquad\text{for every active }r.
$$

### 3.2 Inactive constraints do not matter locally

If constraint $r$ is inactive, it has positive slack

$$
\delta_r=d_r-a_r^\top x^*>0.
$$

For the perturbed point,

$$
a_r^\top(x^*+\varepsilon v)=a_r^\top x^*+\varepsilon a_r^\top v.
$$

If $a_r^\top v\le0$, the constraint remains feasible for every $\varepsilon\ge0$.

If $a_r^\top v>0$, it remains feasible whenever

$$
\varepsilon\le\frac{\delta_r}{a_r^\top v}.
$$

Because there are only finitely many constraints, we can choose one sufficiently small positive $\varepsilon$ that preserves every inactive constraint. This is why the local geometry around $x^*$ is determined by the active constraints.

### 3.3 Objective improvement

The objective at $x^*+\varepsilon v$ is

$$
c^\top(x^*+\varepsilon v)=c^\top x^*+\varepsilon c^\top v.
$$

Therefore, $v$ is an improving direction if

$$
c^\top v>0.
$$

At an optimum, there cannot be a direction satisfying both

$$
a_r^\top v\le0
\quad\text{for every active }r,
$$

and

$$
c^\top v>0.
$$

That observation is the bridge to Farkas' lemma.

---

## 4. Cones and nonnegative combinations

Given vectors $a_1,\ldots,a_k\in\mathbb R^d$, their nonnegative combinations form the cone

$$
C=\left\{\sum_{j=1}^{k}\lambda_j a_j:\lambda_j\ge0\right\}.
$$

If

$$
M=\begin{bmatrix}a_1&a_2&\cdots&a_k\end{bmatrix},
$$

then asking whether $p\in C$ is equivalent to asking whether the system

$$
M\lambda=p,\qquad \lambda\ge0
$$

has a solution.

### Conceptual visualization

```text
                    a2
                   /
                  /      p inside cone:
                 /       p = lambda1*a1 + lambda2*a2
                /
origin --------/--------------------> a1
              cone C
```

A cone is closed under:

1. addition;
2. multiplication by nonnegative scalars.

Unlike a subspace, it does not generally include negative multiples.

---

## 5. Farkas' lemma

One form of Farkas' lemma says that exactly one of the following systems is feasible:

$$
\text{(I)}\qquad M\lambda=p,\qquad \lambda\ge0,
$$

or

$$
\text{(II)}\qquad M^\top w\ge0,\qquad p^\top w<0.
$$

This is a **theorem of alternatives**:

- either $p$ belongs to the cone generated by the columns of $M$;
- or a vector $w$ separates $p$ from that cone.

### 5.1 Why both alternatives cannot hold

Suppose both held. Then $p=M\lambda$, where $\lambda\ge0$, and $M^\top w\ge0$. Thus,

$$
p^\top w=(M\lambda)^\top w=\lambda^\top M^\top w\ge0.
$$

But alternative (II) requires $p^\top w<0$, a contradiction.

Therefore, the two alternatives are mutually exclusive.

### 5.2 Numerical example

Let

$$
a_1=\begin{bmatrix}1\\0\end{bmatrix},\qquad
a_2=\begin{bmatrix}1\\1\end{bmatrix},\qquad
p=\begin{bmatrix}0\\1\end{bmatrix}.
$$

A nonnegative combination of $a_1$ and $a_2$ is

$$
\lambda_1a_1+\lambda_2a_2=
\begin{bmatrix}\lambda_1+\lambda_2\\\lambda_2\end{bmatrix}.
$$

To equal $p$, we would need

$$
\lambda_2=1,\qquad \lambda_1+\lambda_2=0.
$$

This implies $\lambda_1=-1$, which violates $\lambda_1\ge0$. Hence $p$ is outside the cone.

Choose

$$
w=\begin{bmatrix}1\\-1\end{bmatrix}.
$$

Then

$$
a_1^\top w=1,\qquad a_2^\top w=0,
$$

so $M^\top w\ge0$. But

$$
p^\top w=-1<0.
$$

Therefore, $w$ is a short certificate proving that $p$ cannot be a nonnegative combination of $a_1$ and $a_2$.

### Visualization

```text
       p = (0,1)
       *
       |       cone generated by a1 and a2
       |      /
       |     /
-------+----/------------------>
            a1 = (1,0)

Separating line: w^T z = 0
where w = (1,-1)
```

---

## 6. Why a separating certificate exists

Let $C\subseteq\mathbb R^d$ be a nonempty closed convex set, and suppose $p\notin C$. Choose a closest point $q\in C$ to $p$, and define

$$
v=p-q.
$$

The vector $v$ points from $q$ toward $p$.

The separating-hyperplane theorem gives

$$
v^\top p>v^\top q\ge v^\top z
\qquad\text{for every }z\in C.
$$

Thus the hyperplane perpendicular to $v$ separates $p$ from $C$.

```text
                       p
                       *
                       | v = p - q
                       |
                -------q-------  supporting hyperplane
              /        *
             /      convex set C
            /________________
```

### 6.1 Closest-point argument

For any $z\in C$, convexity implies

$$
q+\theta(z-q)\in C
\qquad\text{for }0\le\theta\le1.
$$

If $v^\top(z-q)>0$, then for sufficiently small $\theta>0$,

$$
\begin{aligned}
\left\|p-\left(q+\theta(z-q)\right)\right\|^2
&=\|p-q\|^2-2\theta v^\top(z-q)+\theta^2\|z-q\|^2\\
&<\|p-q\|^2.
\end{aligned}
$$

That would produce a point in $C$ closer to $p$ than $q$, contradicting the definition of $q$. Hence

$$
v^\top(z-q)\le0,
$$

or

$$
v^\top z\le v^\top q.
$$

Also,

$$
v^\top p-v^\top q=v^\top(p-q)=\|p-q\|^2>0.
$$

This proves separation.

### 6.2 Specialization to a cone

Suppose $C$ is the cone generated by $a_1,\ldots,a_k$.

Because $0\in C$, and every $\alpha a_j\in C$ for $\alpha\ge0$, a linear functional bounded above over $C$ must satisfy

$$
v^\top a_j\le0
\qquad\text{for all }j.
$$

Otherwise, if $v^\top a_j>0$, then

$$
v^\top(\alpha a_j)=\alpha v^\top a_j\to\infty
$$

as $\alpha\to\infty$.

After reversing the sign by setting $w=-v$, we obtain

$$
a_j^\top w\ge0
\qquad\text{for all }j,
$$

and

$$
p^\top w<0.
$$

This is precisely the infeasibility certificate in Farkas' lemma.

---

## 7. Strong duality through active constraints

Let $x^*$ be an optimal primal solution.

Write all primal constraints uniformly as

$$
a_r^\top x\le d_r.
$$

This includes:

- the original rows $A_jx\le b_j$;
- nonnegativity constraints $-x_i\le0$.

Let $S$ be the set of constraints active at $x^*$.

The key claim is

$$
\boxed{c=\sum_{r\in S}\lambda_r a_r,\qquad \lambda_r\ge0.}
$$

In words:

> At an optimum, the objective direction belongs to the cone generated by the outward normals of the active constraints.

### 7.1 Why the claim must hold

Suppose the claim were false. Then $c$ would not be a nonnegative combination of the active normals.

Apply Farkas' lemma to the matrix whose columns are the active normals, with target $c$. There would be a vector $w$ such that

$$
a_r^\top w\ge0\quad(r\in S),
$$

and

$$
c^\top w<0.
$$

Set $v=-w$. Then

$$
a_r^\top v\le0\quad(r\in S),
$$

and

$$
c^\top v>0.
$$

Therefore:

- every active constraint remains feasible along $v$;
- every inactive constraint remains feasible for a sufficiently small step;
- the objective strictly improves.

So for sufficiently small $\varepsilon>0$, $x^*+\varepsilon v$ is feasible and

$$
c^\top(x^*+\varepsilon v)>c^\top x^*.
$$

This contradicts the optimality of $x^*$. Hence $c$ must be a nonnegative combination of the active normals.

### 7.2 Pseudocode for constructing the local contradiction

```text
PROCEDURE FindImprovingStep(x_star, v, constraints):
    # Constraints are a_r^T x <= d_r
    epsilon_max = +infinity

    FOR each constraint r:
        slack = d_r - a_r^T x_star

        IF slack == 0:
            # Active constraint
            IF a_r^T v > 0:
                RETURN "v is not a feasible local direction"

        ELSE IF a_r^T v > 0:
            epsilon_r = slack / (a_r^T v)
            epsilon_max = min(epsilon_max, epsilon_r)

    IF c^T v <= 0:
        RETURN "v is not an improving direction"

    IF epsilon_max == +infinity:
        epsilon = 1
    ELSE:
        epsilon = epsilon_max / 2

    RETURN x_star + epsilon * v
```

This is mostly a proof device, not a practical LP algorithm. It formalizes the statement that inactive constraints can be protected by taking a sufficiently small step.

---

## 8. Turning active-constraint multipliers into a dual solution

Separate the active-normal representation into two kinds of constraints:

1. original constraints $A_jx\le b_j$, with multipliers $y_j\ge0$;
2. nonnegativity constraints $-x_i\le0$, with multipliers $z_i\ge0$.

The representation of $c$ becomes

$$
c=A^\top y-z.
$$

Since $z\ge0$,

$$
A^\top y=c+z\ge c.
$$

Thus $y$ is dual-feasible.

Now multiply the representation by $x^*$:

$$
c^\top x^*=\sum_r\lambda_r a_r^\top x^*.
$$

A positive multiplier is assigned only to an active constraint, so $a_r^\top x^*=d_r$ whenever $\lambda_r>0$. Therefore,

$$
c^\top x^*=\sum_r\lambda_r d_r.
$$

The right-hand sides of the nonnegativity constraints $-x_i\le0$ are zero, so they contribute nothing. The remaining terms give

$$
c^\top x^*=b^\top y.
$$

Because $x^*$ is primal-feasible and $y$ is dual-feasible, weak duality says

$$
c^\top x^*\le\operatorname{OPT}_D\le b^\top y.
$$

But the endpoints are equal. Hence

$$
\boxed{\operatorname{OPT}_P=c^\top x^*=b^\top y=\operatorname{OPT}_D.}
$$

This is **strong duality**.

---

## 9. Complete proof structure

```text
Optimal primal solution x*
          |
          v
Find constraints active at x*
          |
          v
Is c in the cone of active normals?
       /                    \
     Yes                    No
      |                      |
      v                      v
Obtain nonnegative       Farkas gives a
multipliers              separating vector
      |                      |
      v                      v
Construct dual y         Negate it to obtain
with A^T y >= c          feasible improving direction
      |                      |
      v                      v
Show b^T y = c^T x*      Contradicts optimality
      |
      v
Weak duality proves both solutions optimal
```

---

## 10. Worked example

Consider

$$
\begin{aligned}
\max\quad & 3x_1+2x_2\\
\text{subject to}\quad
&x_1+x_2\le4,\\
&2x_1+x_2\le5,\\
&x_1,x_2\ge0.
\end{aligned}
$$

### 10.1 Find the primal optimum

The two resource constraints intersect where

$$
x_1+x_2=4,
$$

$$
2x_1+x_2=5.
$$

Subtracting gives $x_1=1$ and $x_2=3$. The objective value is

$$
3(1)+2(3)=9.
$$

At $x^*=(1,3)$, both original constraints are active. The nonnegativity constraints are inactive because both coordinates are positive.

The active normals are

$$
a_1=\begin{bmatrix}1\\1\end{bmatrix},\qquad
a_2=\begin{bmatrix}2\\1\end{bmatrix}.
$$

The objective direction is

$$
c=\begin{bmatrix}3\\2\end{bmatrix}.
$$

Find nonnegative multipliers satisfying

$$
c=y_1a_1+y_2a_2.
$$

This gives

$$
\begin{aligned}
y_1+2y_2&=3,\\
y_1+y_2&=2.
\end{aligned}
$$

Therefore,

$$
y_2=1,\qquad y_1=1.
$$

So $c=a_1+a_2$.

### 10.2 Dual problem

The dual is

$$
\begin{aligned}
\min\quad &4y_1+5y_2\\
\text{subject to}\quad
&y_1+2y_2\ge3,\\
&y_1+y_2\ge2,\\
&y_1,y_2\ge0.
\end{aligned}
$$

Using $y^*=(1,1)$,

$$
b^\top y^*=4(1)+5(1)=9.
$$

Thus

$$
c^\top x^*=b^\top y^*=9.
$$

Weak duality now certifies that both solutions are optimal.

---

## 11. Why nonnegativity constraints must be included

Consider

$$
\begin{aligned}
\max\quad &-x\\
\text{subject to}\quad &x\le1,\\
&x\ge0.
\end{aligned}
$$

The optimum is $x^*=0$ with value $0$.

At $x^*=0$:

- $x\le1$ is inactive;
- $-x\le0$ is active.

The objective normal is $c=-1$, which is exactly the normal of the active nonnegativity constraint:

$$
c=1(-1).
$$

If we ignored $x\ge0$, there would be no active constraint explaining why motion toward negative $x$ is forbidden. The strong-duality geometry would therefore be incomplete.

---

## 12. Complementary slackness connection

The proof naturally reveals complementary slackness.

For primal constraint $j$,

$$
y_j(b_j-A_jx^*)=0.
$$

Thus:

- if $y_j>0$, then primal constraint $j$ must be tight;
- if primal constraint $j$ has positive slack, then $y_j=0$.

For primal variable $i$,

$$
x_i^*\left((A^\top y)_i-c_i\right)=0.
$$

Thus:

- if $x_i^*>0$, the corresponding dual constraint is tight;
- if the dual constraint has positive slack, then $x_i^*=0$.

One subtle point is important:

$$
\text{positive multiplier}\implies\text{tight constraint},
$$

but the converse is not always true:

$$
\text{tight constraint}\centernot\implies\text{positive multiplier}.
$$

A tight constraint may be redundant and receive multiplier zero.

---

## 13. Example of a tight constraint with zero multiplier

Consider

$$
\begin{aligned}
\max\quad &x_1+x_2\\
\text{subject to}\quad
&x_1+x_2\le1,\\
&x_1\le1,\\
&x_2\le1,\\
&x_1,x_2\ge0.
\end{aligned}
$$

Choose the optimal solution $x^*=(1,0)$.

At this point:

- $x_1+x_2\le1$ is tight;
- $x_1\le1$ is tight;
- $-x_2\le0$ is tight.

Nevertheless, the objective direction can be represented using only the first normal:

$$
\begin{bmatrix}1\\1\end{bmatrix}
=1\begin{bmatrix}1\\1\end{bmatrix}.
$$

The tight constraint $x_1\le1$ can therefore receive multiplier zero.

---

## 14. Approximate optimality certificates

Suppose $x$ is primal-feasible, $y$ is dual-feasible, and

$$
b^\top y-c^\top x\le\varepsilon.
$$

Weak duality gives

$$
c^\top x\le\operatorname{OPT}_P\le b^\top y.
$$

Subtracting $c^\top x$,

$$
0\le\operatorname{OPT}_P-c^\top x\le b^\top y-c^\top x\le\varepsilon.
$$

Therefore,

$$
\boxed{\operatorname{OPT}_P-c^\top x\le\varepsilon.}
$$

So the primal solution is at most $\varepsilon$ below optimal. This provides a practical stopping condition for approximate optimization algorithms.

---

## 15. Pseudocode for checking an optimality certificate

```text
PROCEDURE VerifyLPCertificate(A, b, c, x, y, tolerance):
    primal_constraint_violation =
        max_component(A*x - b)

    primal_nonnegativity_violation =
        max_component(-x)

    dual_constraint_violation =
        max_component(c - transpose(A)*y)

    dual_nonnegativity_violation =
        max_component(-y)

    primal_value = transpose(c)*x
    dual_value = transpose(b)*y
    duality_gap = dual_value - primal_value

    primal_feasible =
        primal_constraint_violation <= tolerance AND
        primal_nonnegativity_violation <= tolerance

    dual_feasible =
        dual_constraint_violation <= tolerance AND
        dual_nonnegativity_violation <= tolerance

    certificate_valid =
        primal_feasible AND
        dual_feasible AND
        absolute_value(duality_gap) <= tolerance

    RETURN {
        primal_feasible,
        dual_feasible,
        primal_value,
        dual_value,
        duality_gap,
        certificate_valid
    }
```

For floating-point solvers, one normally permits small feasibility and duality-gap tolerances instead of exact equality.

---

## 16. Bridge to convex optimization

For a differentiable nonlinear function $f$,

$$
f(x+h)\approx f(x)+\nabla f(x)^\top h.
$$

The gradient $\nabla f(x)$ plays the role that $c$ plays in an LP: it gives the local direction of change.

At a constrained optimum, the gradient is balanced by active constraint normals. In a more general differentiable constrained problem, this becomes a stationarity condition of the form

$$
\nabla f(x^*)+\sum_j\lambda_j\nabla g_j(x^*)=0.
$$

This is the conceptual route from LP duality to:

- Lagrange multipliers;
- the Karush-Kuhn-Tucker conditions;
- convex duality;
- constrained nonlinear optimization.

---

## 17. Common misconceptions

### Misconception 1: Every tight constraint must have a positive multiplier

False. A tight constraint can be redundant or unnecessary in the representation of the objective normal.

### Misconception 2: The optimum must be a vertex

False. The active-normal argument works at any optimal point, including points in the interior of an optimal edge or face.

### Misconception 3: Inactive constraints can be discarded globally

Not necessarily. They can be ignored only when reasoning about sufficiently small local movements around the current point.

### Misconception 4: Weak duality proves equality

Weak duality proves only

$$
\operatorname{OPT}_P\le\operatorname{OPT}_D.
$$

Strong duality proves equality under the appropriate feasibility and boundedness assumptions.

### Misconception 5: Farkas' vector is an approximate indication

No. It is an exact algebraic certificate. Checking

$$
M^\top w\ge0,\qquad p^\top w<0
$$

proves that $p$ is outside the cone.

---

## 18. Quiz questions

### Conceptual questions

1. What is the difference between weak and strong duality?
2. Why does a dual-feasible solution provide an upper bound on a primal maximization problem?
3. Define an active constraint.
4. Why can inactive constraints be ignored for sufficiently small local movements?
5. What geometric object is formed by the nonnegative combinations of a finite set of vectors?
6. State the version of Farkas' lemma used in this lecture.
7. Why can the two alternatives in Farkas' lemma not both hold?
8. What does the separating vector $w$ certify?
9. Why must the nonnegativity constraints $x_i\ge0$ be included among the primal constraints?
10. At an optimum, why must the objective direction lie in the cone generated by active normals?
11. Does a tight constraint necessarily have a positive dual multiplier?
12. Does the active-normal proof require the optimal solution to be a vertex?

### Short computational questions

13. Determine whether

    $$
    p=\begin{bmatrix}2\\3\end{bmatrix}
    $$

    belongs to the cone generated by

    $$
    a_1=\begin{bmatrix}1\\0\end{bmatrix},\qquad
    a_2=\begin{bmatrix}1\\1\end{bmatrix}.
    $$

14. For

    $$
    \max\{2x:x\le3,\ x\ge0\},
    $$

    write the dual and find matching primal and dual optima.

15. If a primal-feasible solution has value $17$ and a dual-feasible solution has value $17.04$, what can you conclude about the primal solution's suboptimality?

16. At a feasible point, a constraint has slack $0.6$ and $a_r^\top v=3$. What upper bound on $\varepsilon$ ensures this constraint remains feasible along $x+\varepsilon v$?

---

## 19. Quiz answers

1. Weak duality gives $\operatorname{OPT}_P\le\operatorname{OPT}_D$; strong duality gives equality when finite optima exist under the standard LP conditions.
2. Because feasibility implies $c^\top x\le y^\top Ax\le b^\top y$.
3. A constraint satisfying equality at the point.
4. They have positive slack, which absorbs sufficiently small changes.
5. A convex cone.
6. Exactly one of $M\lambda=p,\ \lambda\ge0$ and $M^\top w\ge0,\ p^\top w<0$ is feasible.
7. If both held, then $p^\top w=\lambda^\top M^\top w\ge0$, contradicting $p^\top w<0$.
8. It proves that $p$ is not a nonnegative combination of the columns of $M$.
9. They may be the constraints that block an improving direction, especially when some $x_i=0$.
10. Otherwise Farkas' lemma would produce a feasible improving direction.
11. No.
12. No.
13. We need $\lambda_1+\lambda_2=2$ and $\lambda_2=3$. This gives $\lambda_1=-1$, so $p$ is not in the cone.
14. The dual is $\min 3y$ subject to $y\ge2$ and $y\ge0$. The solutions are $x^*=3$ and $y^*=2$, both with value $6$.
15. If the two points are feasible, then $0\le\operatorname{OPT}-17\le0.04$.
16. Require $\varepsilon\le0.6/3=0.2$.

---

## 20. Exam-style questions

### Question 1: Weak duality and certification

Consider

$$
\begin{aligned}
\max\quad & c^\top x\\
\text{subject to}\quad &Ax\le b,\quad x\ge0,
\end{aligned}
$$

and its dual.

1. Prove weak duality.
2. Show that feasible $x$ and $y$ satisfying $c^\top x=b^\top y$ are both optimal.
3. Show that a duality gap at most $\varepsilon$ certifies $\varepsilon$-optimality.

#### Solution outline

Use

$$
c^\top x\le(A^\top y)^\top x=y^\top Ax\le y^\top b.
$$

Equality of the endpoints forces optimality. A gap bounded by $\varepsilon$ bounds the difference between the primal value and the optimum.

### Question 2: Farkas certificate

Let

$$
M=\begin{bmatrix}1&1\\0&1\end{bmatrix},\qquad
p=\begin{bmatrix}0\\1\end{bmatrix}.
$$

1. Prove that $M\lambda=p,\ \lambda\ge0$ is infeasible.
2. Find $w$ satisfying $M^\top w\ge0$ and $p^\top w<0$.
3. Explain the geometry.

#### Solution outline

The equations give

$$
\lambda_1+\lambda_2=0,\qquad \lambda_2=1,
$$

so $\lambda_1=-1$. A certificate is

$$
w=(1,-1)^\top.
$$

Then

$$
M^\top w=\begin{bmatrix}1\\0\end{bmatrix}\ge0,
\qquad p^\top w=-1<0.
$$

The line $w^\top z=0$ separates $p$ from the generated cone.

### Question 3: Strong duality proof

Let $x^*$ be an optimal solution of a primal maximization LP.

1. Define the active set $S$.
2. Prove that $c\in\operatorname{cone}\{a_r:r\in S\}$.
3. Convert the cone coefficients into a dual-feasible solution.
4. Prove equality of the primal and dual objective values.

#### Solution outline

Assume $c$ is not in the cone. Farkas gives a separating direction; reverse its sign to obtain $v$ satisfying

$$
a_r^\top v\le0\quad(r\in S),\qquad c^\top v>0.
$$

For sufficiently small $\varepsilon$, $x^*+\varepsilon v$ remains feasible and improves the objective, contradiction. The cone coefficients give $c=A^\top y-z$, hence $A^\top y\ge c$, and tightness gives $c^\top x^*=b^\top y$.

### Question 4: Full primal-dual calculation

Solve

$$
\begin{aligned}
\max\quad &4x_1+3x_2\\
\text{subject to}\quad
&2x_1+x_2\le8,\\
&x_1+2x_2\le8,\\
&x_1,x_2\ge0.
\end{aligned}
$$

Then:

1. derive the dual;
2. find an optimal dual solution;
3. identify the active constraints;
4. represent $c$ as a nonnegative combination of active normals;
5. verify complementary slackness.

#### Answer

The resource constraints intersect at

$$
2x_1+x_2=8,\qquad x_1+2x_2=8.
$$

Solving gives

$$
x_1=x_2=\frac83.
$$

The primal value is

$$
4\left(\frac83\right)+3\left(\frac83\right)=\frac{56}{3}.
$$

The dual is

$$
\begin{aligned}
\min\quad &8y_1+8y_2\\
\text{subject to}\quad
&2y_1+y_2\ge4,\\
&y_1+2y_2\ge3,\\
&y_1,y_2\ge0.
\end{aligned}
$$

Because both primal variables are positive, both dual constraints are tight:

$$
2y_1+y_2=4,\qquad y_1+2y_2=3.
$$

Solving gives

$$
y_1=\frac53,\qquad y_2=\frac23.
$$

Then

$$
8y_1+8y_2=8\left(\frac73\right)=\frac{56}{3}.
$$

Also,

$$
\begin{bmatrix}4\\3\end{bmatrix}
=\frac53\begin{bmatrix}2\\1\end{bmatrix}
+\frac23\begin{bmatrix}1\\2\end{bmatrix}.
$$

### Question 5: Proof-analysis question

A student argues:

> "At an LP optimum, every tight constraint must have a positive multiplier because every tight constraint contributes to blocking improvement."

Explain why the argument is false, give a counterexample, and state the correct complementary-slackness implication.

#### Expected answer

Several tight constraints may be redundant, or their normals may be unnecessary for representing the objective direction. The correct implication is

$$
y_j>0\implies b_j-A_jx^*=0,
$$

not the reverse.

---

## 21. Textbook and reference recommendations

### Best for algorithms students

1. **Vazirani, _Approximation Algorithms_**  
   Useful for LP duality, certificates, rounding, and primal-dual algorithm design.

2. **Williamson and Shmoys, _The Design of Approximation Algorithms_**  
   Especially useful for seeing how dual variables guide combinatorial algorithms.

3. **Matousek and Gartner, _Understanding and Using Linear Programming_**  
   A geometric and accessible treatment of LPs, duality, and certificates.

### Best for optimization theory

4. **Bertsimas and Tsitsiklis, _Introduction to Linear Optimization_**  
   A rigorous treatment of LP geometry, duality, complementary slackness, and algorithms.

5. **Vanderbei, _Linear Programming: Foundations and Extensions_**  
   Strong coverage of primal-dual formulations, geometry, simplex methods, and interior-point methods.

6. **Chvatal, _Linear Programming_**  
   A classic text with careful algebraic and geometric development.

7. **Schrijver, _Theory of Linear and Integer Programming_**  
   More advanced and particularly valuable for polyhedral theory, theorems of alternatives, and integer programming.

### Best bridge to convex optimization

8. **Boyd and Vandenberghe, _Convex Optimization_**  
   Recommended for separating hyperplanes, Lagrange duality, KKT conditions, and the convex-optimization generalization of the ideas in this lecture.

9. **Rockafellar, _Convex Analysis_**  
   A more advanced reference for convex sets, separation, cones, and duality.

---

## 22. Final takeaway

The entire lecture can be compressed into one geometric statement:

$$
\boxed{\text{At an optimum, active constraints block every improving direction.}}
$$

Farkas' lemma turns the absence of an improving direction into an algebraic representation:

$$
\boxed{c=\sum_{r\in S}\lambda_r a_r,\qquad \lambda_r\ge0.}
$$

Those coefficients become dual variables, and tightness gives

$$
\boxed{c^\top x^*=b^\top y^*.}
$$

Weak duality then proves strong duality:

$$
\boxed{\operatorname{OPT}_{P}=\operatorname{OPT}_{D}.}
$$

The important conceptual chain is therefore

$$
\boxed{
\text{separation}
\Longrightarrow
\text{Farkas' lemma}
\Longrightarrow
\text{active-normal multipliers}
\Longrightarrow
\text{dual certificate}
\Longrightarrow
\text{strong duality}.
}
$$
