# 11.1 and 11.2: Step-by-step solutions

The key idea behind both problems is that we can transform one mathematical formulation into another without changing the essential problem.

For 11.1, we want to convert a general linear program (LP2) into the more restricted form (LP1).

For 11.2, we use a similar conversion to show that one version of Farkas' Lemma implies another.

Let's build the intuition first, then work through both proofs.

# Part 1. Background you need

## 1. What is a linear program?

A linear program (LP) consists of:

- Variables: the unknowns we want to choose.
- Objective function: a linear expression we want to maximize or minimize.
- Constraints: linear equations or inequalities the variables must satisfy.

For example,

$$
\begin{aligned}
\text{maximize}\quad & 3x+2y\\
\text{subject to}\quad & x+y\le 5\\
& 2x+y\le 8\\
& x,y\ge 0
\end{aligned}
$$

asks us to find nonnegative $x,y$ that maximize $3x+2y$ while satisfying both inequalities.

The important point is that different-looking LP formulations can represent the same optimization problem.

## 2. Understanding LP1 versus LP2

The two formulations differ in two ways.

| Feature | LP1 | LP2 |
| --- | --- | --- |
| Constraints | Equalities $Ax=b$ | Inequalities $Ax\le b$ |
| Variables | Must satisfy $x_i\ge 0$ | Unrestricted in sign |
| Objective | Maximize $c^Tx$ | Maximize $c^Tx$ |

Here, $A$ is the constraint matrix, $b$ is the vector of bounds, and $c$ contains the objective coefficients.

LP1 looks more restrictive. It requires equality constraints and nonnegative variables. The challenge is to show that we can encode the more general LP2 using only those restricted ingredients.

## 3. The two essential tricks

### Trick A: Turn an unrestricted variable into nonnegative variables

Suppose $x$ can be positive, negative, or zero.

Write

$$
\boxed{x=x^+-x^-}
$$

where

$$
x^+\ge 0,\qquad x^-\ge 0.
$$

Why does this work?

## $x^+$

Positive part

If $x=5$, choose $x^+=5$, $x^-=0$.

$$
5=5-0
$$

## $x^-$

Negative part

If $x=-3$, choose $x^+=0$, $x^-=3$.

$$
-3=0-3
$$

## Both

Zero

If $x=0$, choose $x^+=x^-=0$.

$$
0=0-0
$$

Every real number can be expressed as the difference of two nonnegative numbers. Thus, we no longer need variables that can be negative.

For an original variable $x_i$, we introduce two new variables:

$$
x_i=x_i^+-x_i^-,
\qquad x_i^+,x_i^-\ge 0.
$$

### Trick B: Turn an inequality into an equality

Suppose we have

$$
ax\le b.
$$

The difference between the right and left sides is nonnegative, so we can introduce a slack variable $z\ge 0$:

$$
\boxed{ax+z=b,\qquad z\ge 0.}
$$

Equivalently,

$$
z=b-ax.
$$

Visual intuition: filling the gap

$ax$

Slack $z$

Together, the two parts equal $b$: $ax+z=b$.

If $ax=7$ and $b=10$, then $z=3$. If $ax=b$, then $z=0$. If $ax>b$, the required slack would be negative, which is forbidden.

So the inequality holds exactly when there exists a nonnegative slack variable making the equality true.

These two tricks are all we need for 11.1.

# Part 2. Problem 11.1 — Converting LP2 to LP1

## Step 1: Write down the original problem

LP2 is

$$
\begin{aligned}
\max\quad &\sum_{i=1}^n c_i x_i\\
\text{s.t.}\quad
&\sum_{i=1}^n A_{ji}x_i\le b_j,
&&j=1,\ldots,m.
\end{aligned}
$$

Notice that the variables $x_i$ are unrestricted in sign. They may be positive, negative, or zero.

We must transform this into LP1, which requires:

1. All variables to be nonnegative.
2. All constraints to be equalities.

## Step 2: Split every unrestricted variable

For each original variable $x_i$, introduce two new variables $x_i^+$ and $x_i^-$:

$$
x_i=x_i^+-x_i^-,
\qquad x_i^+,x_i^-\ge 0.
$$

Substitute this expression into the objective:

$$
\begin{aligned}
\sum_{i=1}^n c_i x_i
&=\sum_{i=1}^n c_i(x_i^+-x_i^-)\\
&=\sum_{i=1}^n c_i x_i^+
-\sum_{i=1}^n c_i x_i^-.
\end{aligned}
$$

The new objective is still linear, and every new variable is nonnegative.

## Step 3: Introduce slack variables

Each constraint in LP2 has the form

$$
\sum_{i=1}^n A_{ji}x_i\le b_j.
$$

Introduce a nonnegative slack variable $z_j\ge 0$ for each constraint:

$$
\sum_{i=1}^n A_{ji}x_i+z_j=b_j.
$$

Now substitute $x_i=x_i^+-x_i^-$:

$$
\boxed{
\sum_{i=1}^n A_{ji}x_i^+
-\sum_{i=1}^n A_{ji}x_i^-
+z_j=b_j.
}
$$

This is an equality, and all its variables are nonnegative.

## Step 4: Write the complete transformed LP

The resulting LP1 instance is

$$
\boxed{
\begin{aligned}
\max\quad &
\sum_{i=1}^n c_i x_i^+
-\sum_{i=1}^n c_i x_i^-\\[2pt]
\text{s.t.}\quad &
\sum_{i=1}^n A_{ji}x_i^+
-\sum_{i=1}^n A_{ji}x_i^-
+z_j=b_j,\\
&\hspace{6cm} j=1,\ldots,m,\\
&x_i^+,x_i^-\ge0,
&&i=1,\ldots,n,\\
&z_j\ge0,
&&j=1,\ldots,m.
\end{aligned}
}
$$

This matches the LP1 format exactly.

In matrix form, define the new variable vector

$$
y=(x^+,x^-,z).
$$

Then the transformed problem has the form

$$
\max d^Ty
\qquad\text{subject to}\qquad
My=b,\quad y\ge0,
$$

which is precisely LP1.

## Step 5: Why does this transformation preserve the solution?

We must establish that the transformed problem really represents the original one.

- Every feasible LP2 solution gives a feasible LP1 solution. Given any feasible $x$, choose $x_i^+=\max(x_i,0)$ and $x_i^-=\max(-x_i,0)$. Set $z_j=b_j-\sum_i A_{ji}x_i$. Because the original constraints hold, every $z_j\ge0$.
- Every feasible LP1 solution gives a feasible LP2 solution. Given $x_i^+,x_i^-,z_j$, set $x_i=x_i^+-x_i^-$. The equality constraints imply $\sum_i A_{ji}x_i=b_j-z_j\le b_j$.
- The objective value is unchanged. The transformed objective is exactly $\sum_i c_i(x_i^+-x_i^-)=\sum_i c_i x_i$.

Therefore, the two problems have the same feasible objective values and the same optimal value whenever an optimum exists.

## Step 6: Why is the transformation efficient?

The original problem has $n$ variables and $m$ constraints.

After transformation:

- Each original variable becomes two variables: $2n$.
- Each original constraint gets one slack variable: $m$.
- The total number of variables becomes $2n+m$.
- The number of constraints remains $m$.

The transformed LP is only polynomially larger than the original. Its coefficients can also be constructed in polynomial time.

Therefore, if we have a polynomial-time algorithm for LP1, we can transform any LP2 instance into LP1, solve it, and translate the answer back in polynomial time.

Conclusion for 11.1: LP1 can efficiently represent any LP2.

# Part 3. Problem 11.2 — Farkas' Lemma A implies Farkas' Lemma B

The same two transformations will establish this result. The key difference is that we now track the coefficients of the infeasibility certificate.

## Step 1: Understand what each lemma says

Farkas' Lemma A concerns a system of equations with nonnegative variables:

$$
Ax=b,\qquad x\ge0.
$$

It says this system is infeasible if and only if there exists a vector $\lambda$ such that

$$
\lambda^Tb<0,\qquad \lambda^TA\ge0.
$$

Here, $\lambda^TA\ge0$ means every component of that row vector is nonnegative.

Farkas' Lemma B concerns inequalities with unrestricted variables:

$$
Ax\le b.
$$

It says this system is infeasible if and only if there exists $\lambda$ satisfying

$$
\lambda\ge0,\qquad
\lambda^Tb<0,\qquad
\lambda^TA=0.
$$

The important difference is that Lemma B requires nonnegative multipliers and an exact zero, rather than merely nonnegative coefficients.

How do these stronger conditions appear? They come from applying Lemma A to a carefully transformed system.

## Step 2: Turn the inequalities into equalities

Start with the system from Lemma B:

$$
Ax\le b.
$$

Introduce a nonnegative slack vector $z\ge0$:

$$
Ax+z=b.
$$

But $x$ is unrestricted in sign, so we also split it:

$$
x=x^+-x^-,
\qquad x^+,x^-\ge0.
$$

The transformed system is

$$
\boxed{Ax^+-Ax^-+z=b}
$$

with

$$
x^+\ge0,\qquad x^-\ge0,\qquad z\ge0.
$$

This is a system of exactly the kind addressed by Lemma A.

## Step 3: Verify that infeasibility is preserved

The original system $Ax\le b$ is feasible if and only if the transformed system is feasible.

- If $Ax\le b$, choose $x^+=\max(x,0)$, $x^-=\max(-x,0)$, and $z=b-Ax\ge0$.
- If $Ax^+-Ax^-+z=b$ with all variables nonnegative, set $x=x^+-x^-$. Then $Ax=b-z\le b$.

Consequently, if the original inequality system is infeasible, the transformed equality system is also infeasible.

## Step 4: Apply Farkas' Lemma A

Write the transformed system as one matrix equation:

$$
\underbrace{\begin{bmatrix}A&-A&I\end{bmatrix}}_{\widetilde A}
\underbrace{\begin{bmatrix}x^+\\x^-\\z\end{bmatrix}}_{\widetilde x}
=b,
\qquad \widetilde x\ge0.
$$

Because this system is infeasible, Lemma A guarantees that there exists a vector $\lambda$ such that

$$
\lambda^Tb<0
$$

and

$$
\lambda^T\widetilde A\ge0.
$$

Substitute the block matrix $\widetilde A=[A\ -A\ I]$:

$$
\boxed{\lambda^T[A\ -A\ I]\ge0.}
$$

The crucial step is to examine each block separately.

## Step 5: Analyze the three blocks

Expanding the inequality gives

$$
\boxed{
\lambda^TA\ge0,\qquad
-\lambda^TA\ge0,\qquad
\lambda^TI\ge0.
}
$$

Let's see what each condition tells us.

First block: $A$

$$
\lambda^TA\ge0
$$

Every component of $\lambda^TA$ is nonnegative.

Second block: $-A$

$$
-\lambda^TA\ge0
$$

Equivalently, $\lambda^TA\le0$.

Combine the first two blocks

A vector that is both componentwise nonnegative and componentwise nonpositive must be zero:

$$
\boxed{\lambda^TA=0.}
$$

Third block: $I$

$$
\lambda^TI=\lambda^T\ge0
$$

Therefore,

$$
\boxed{\lambda\ge0.}
$$

We already obtained $\lambda^Tb<0$ from Lemma A. Putting everything together gives

$$
\boxed{
\lambda\ge0,\qquad
\lambda^Tb<0,\qquad
\lambda^TA=0.
}
$$

These are exactly the certificate conditions in Farkas' Lemma B.

This proves the forward implication: if $Ax\le b$ is infeasible, then a certificate of the type required by Lemma B exists.

## Step 6: Verify the converse

Lemma B is an “if and only if” statement, so we should also verify that a certificate satisfying its conditions guarantees infeasibility.

Suppose there exists $\lambda\ge0$ with

$$
\lambda^Tb<0,\qquad \lambda^TA=0.
$$

Assume, for contradiction, that a feasible $x$ exists with $Ax\le b$.

Multiplying each inequality by the corresponding nonnegative $\lambda_j$ and summing preserves the inequality:

$$
\lambda^TAx\le\lambda^Tb.
$$

But $\lambda^TA=0$, so the left side equals zero. Hence,

$$
0\le\lambda^Tb<0,
$$

which is impossible.

Therefore, the system must be infeasible.

This completes the proof of both directions of Lemma B, using Lemma A for the main implication and a direct contradiction for the converse.

# Part 4. A numerical example to make the proof concrete

Consider the following system of inequalities in the unrestricted variable $x$:

$$
\begin{aligned}
x&\le0,\\
-x&\le-1.
\end{aligned}
$$

The first inequality says $x\le0$, while the second says $x\ge1$. No real number can satisfy both, so the system is infeasible.

Here,

$$
A=\begin{bmatrix}1\\-1\end{bmatrix},
\qquad
b=\begin{bmatrix}0\\-1\end{bmatrix}.
$$

We can choose

$$
\lambda=\begin{bmatrix}1\\1\end{bmatrix}.
$$

Check the certificate conditions:

1. Nonnegativity:

$$
\lambda=\begin{bmatrix}1\\1\end{bmatrix}\ge0.
$$

2. The weighted right-hand side is negative:

$$
\lambda^Tb=1(0)+1(-1)=-1<0.
$$

3. The weighted constraint coefficients cancel:

$$
\lambda^TA=1(1)+1(-1)=0.
$$

The certificate combines the two inequalities into

$$
x+(-x)\le0+(-1),
$$

which simplifies to

$$
0\le-1.
$$

That contradiction proves infeasibility.

Visual summary of the contradiction

$x\le0$

$-x\le-1$, or $x\ge1$

## Contradiction

$$
0\le-1
$$

Impossible for any real $x$

# Part 5. The big picture

The same transformations underlie both exercises.

### LP2 / Farkas' Lemma B

Inequalities, unrestricted variables

Split unrestricted variables

$$
x=x^+-x^-
$$

All variables become nonnegative.

Add slack variables

$$
Ax^+-Ax^-+z=b
$$

Inequalities become equalities.

### LP1 / Farkas' Lemma A

Equalities, nonnegative variables

### Extract the result

In the Farkas proof, the $A$ and $-A$ blocks force $\lambda^TA=0$, while the identity block forces $\lambda\ge0$.

The most important insight is that the extra structure of the transformed system gives us exactly the conditions we need. The pair of blocks $A$ and $-A$ forces equality, and the slack-variable block $I$ forces nonnegative multipliers.

## Quick self-check

1. Why do we need two variables to represent an unrestricted variable?

Because the variable must be strictly positive.

Because the difference of two nonnegative variables can be any real number.

Because each constraint needs two slack variables.

2. In the Farkas proof, why does $\lambda^TA=0$ follow?

Because the original inequalities are equalities.

Because $\lambda^TA\ge0$ and $-\lambda^TA\ge0$ both hold.

Because the objective function is zero.

 Check answers

What to remember for an exam:

- To convert unrestricted variables into nonnegative variables, use $x=x^+-x^-$.
- To convert $Ax\le b$ into equalities, introduce $z\ge0$ and write $Ax+z=b$.
- In the Farkas proof, apply Lemma A to the augmented matrix $[A\ -A\ I]$.
- The $A$ and $-A$ blocks imply $\lambda^TA=0$, and the $I$ block implies $\lambda\ge0$.
- Finally, $\lambda^Tb<0$ supplies the contradiction needed to certify infeasibility.
