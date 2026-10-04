# 11.1 Converting LP2 to LP1

The main obstacle is that LP1 has a very restricted form:

1. Every variable must be nonnegative.
2. Every constraint must be an equality.

LP2 has neither restriction: its variables are unrestricted in sign, and its constraints are inequalities. The hint gives exactly the two transformations needed.

---

## 1. Background: What Does “Efficiently Represent” Mean?

We need a **polynomial-time reduction** from LP2 to LP1.

Given an instance of LP2, we must:

1. Construct an equivalent instance of LP1 in polynomial time.
2. Solve the resulting LP1 using the assumed LP1 algorithm.
3. Convert the LP1 solution back into an LP2 solution in polynomial time.

“Equivalent” means that the transformation preserves:

- feasibility,
- infeasibility,
- boundedness or unboundedness,
- and the optimal objective value.

---

## 2. Difficulty 1: LP2 Variables Are Unrestricted

In LP2, each variable $x_i$ may be positive, zero, or negative:

$$
x_i \in \mathbb{R}.
$$

But LP1 requires all variables to satisfy $x_i \ge 0$.

### Splitting an unrestricted variable

For every original variable $x_i$, introduce two new variables:

$$
x_i^+ \ge 0,
\qquad
x_i^- \ge 0,
$$

and define

$$
x_i = x_i^+ - x_i^-.
$$

This can represent every real number:

- If $x_i=5$, choose $x_i^+=5$ and $x_i^-=0$.
- If $x_i=-3$, choose $x_i^+=0$ and $x_i^-=3$.
- If $x_i=0$, choose $x_i^+=x_i^-=0$.

More generally, several pairs may represent the same value. For example,

$$
5=5-0=7-2=100-95.
$$

This nonuniqueness does not cause a problem because the objective and constraints depend only on the difference $x_i^+-x_i^-$.

### Vector form

Introduce

$$
x^+,x^- \in \mathbb{R}_{\ge 0}^n.
$$

Then

$$
x=x^+-x^-.
$$

### Visualization

```text
Unrestricted real variable x_i
               |
               v
      x_i = x_i^+ - x_i^-
             |         |
             v         v
          x_i^+ >= 0  x_i^- >= 0
```

The two nonnegative variables encode movement in opposite directions along the real line:

```text
negative direction <------ 0 ------> positive direction
       represented by x_i^-         represented by x_i^+
```

---

## 3. Difficulty 2: LP2 Has Inequality Constraints

LP2 contains

$$
Ax \le b.
$$

For each constraint $j$, introduce a nonnegative **slack variable** $z_j \ge 0$:

$$
\sum_{i=1}^n A_{ji}x_i+z_j=b_j.
$$

Equivalently,

$$
z_j=b_j-\sum_{i=1}^n A_{ji}x_i.
$$

The condition $z_j\ge 0$ is equivalent to

$$
\sum_{i=1}^n A_{ji}x_i\le b_j.
$$

Thus,

$$
Ax\le b
\quad\Longleftrightarrow\quad
Ax+z=b,
\qquad z\ge 0.
$$

### Interpretation of the slack

The slack measures the unused portion of the constraint:

```text
left-hand side + unused capacity = right-hand side
      Ax       +       z          =        b
```

For instance,

$$
x_1+x_2\le 10
$$

becomes

$$
x_1+x_2+z=10,
\qquad z\ge 0.
$$

If $x_1+x_2=7$, then $z=3$. If $x_1+x_2=10$, then $z=0$.

---

## 4. Apply Both Transformations

The original LP2 is

$$
\begin{aligned}
\text{maximize}\quad & c^Tx\\
\text{subject to}\quad & Ax\le b,
\end{aligned}
$$

where $x$ is unrestricted.

Substitute

$$
x=x^+-x^-.
$$

The objective becomes

$$
c^Tx
=
c^T(x^+-x^-)
=
c^Tx^+-c^Tx^-.
$$

The constraints become

$$
A(x^+-x^-)\le b,
$$

or

$$
Ax^+-Ax^-\le b.
$$

Now introduce the slack vector $z\ge 0$:

$$
Ax^+-Ax^-+z=b.
$$

Therefore, the LP1 instance is

$$
\boxed{
\begin{aligned}
\text{maximize}\quad
& c^Tx^+-c^Tx^-\\
\text{subject to}\quad
& Ax^+-Ax^-+z=b,\\
& x^+\ge 0,\quad x^-\ge 0,\quad z\ge 0.
\end{aligned}}
$$

This has exactly the LP1 form: equality constraints and nonnegative variables.

### Matrix form

Define

$$
y=
\begin{bmatrix}
x^+\\
x^-\\
z
\end{bmatrix},
\qquad
\widetilde A=
\begin{bmatrix}
A&-A&I_m
\end{bmatrix},
\qquad
\widetilde c=
\begin{bmatrix}
c\\
-c\\
0
\end{bmatrix}.
$$

Then the converted problem is

$$
\begin{aligned}
\text{maximize}\quad & \widetilde c^T y\\
\text{subject to}\quad & \widetilde A y=b,\\
& y\ge 0.
\end{aligned}
$$

This is an instance of LP1.

---

## 5. Why the Transformation Is Correct

We prove equivalence in both directions.

### Direction 1: LP2 feasible implies the constructed LP1 is feasible

Suppose $x$ satisfies

$$
Ax\le b.
$$

Define

$$
x_i^+=\max\{x_i,0\},
\qquad
x_i^-=\max\{-x_i,0\}.
$$

Then

$$
x=x^+-x^-.
$$

Also define

$$
z=b-Ax.
$$

Since $Ax\le b$, we have $z\ge 0$. Therefore,

$$
\begin{aligned}
Ax^+-Ax^-+z
&=A(x^+-x^-)+(b-Ax)\\
&=Ax+b-Ax\\
&=b.
\end{aligned}
$$

So $(x^+,x^-,z)$ is feasible for the LP1 instance.

The objective is preserved:

$$
c^Tx^+-c^Tx^-
=
c^T(x^+-x^-)
=
c^Tx.
$$

### Direction 2: constructed LP1 feasible implies LP2 is feasible

Suppose $(x^+,x^-,z)$ satisfies

$$
Ax^+-Ax^-+z=b
$$

with

$$
x^+,x^-,z\ge 0.
$$

Recover the original variable by setting

$$
x=x^+-x^-.
$$

Then

$$
Ax+z=b,
$$

so

$$
Ax=b-z.
$$

Because $z\ge 0$,

$$
b-z\le b.
$$

Therefore,

$$
Ax\le b.
$$

Thus, $x$ is feasible for LP2, and again,

$$
c^Tx=c^Tx^+-c^Tx^-.
$$

Therefore, feasibility and objective values are preserved in both directions.

---

## 6. Why the Reduction Takes Polynomial Time

The original LP2 has:

- $n$ variables,
- $m$ constraints.

The transformed LP1 has:

- $2n+m$ variables:
  - $n$ variables in $x^+$,
  - $n$ variables in $x^-$,
  - $m$ slack variables in $z$;
- $m$ equality constraints.

The new matrix is

$$
[A\; -A\; I_m].
$$

Constructing it only requires:

- copying $A$,
- negating $A$,
- adding an identity matrix.

The number of variables and coefficients grows only polynomially. Therefore, if LP1 can be solved in polynomial time, then LP2 can also be solved in polynomial time.

---

## 7. Numerical Example

Consider

$$
\begin{aligned}
\text{maximize}\quad & 3x_1-x_2\\
\text{subject to}\quad
& x_1+x_2\le 4,\\
& -x_1+2x_2\le 2,
\end{aligned}
$$

where $x_1,x_2$ are unrestricted.

Split the variables:

$$
x_1=x_1^+-x_1^-,
\qquad
x_2=x_2^+-x_2^-.
$$

The objective becomes

$$
3x_1^+-3x_1^- -x_2^+ +x_2^-.
$$

Introduce slack variables $z_1,z_2\ge 0$:

$$
x_1^+-x_1^-+x_2^+-x_2^-+z_1=4,
$$

$$
-x_1^++x_1^-+2x_2^+-2x_2^-+z_2=2.
$$

Thus, the LP1 instance is

$$
\begin{aligned}
\text{maximize}\quad
&3x_1^+-3x_1^- -x_2^+ +x_2^-\\
\text{subject to}\quad
&x_1^+-x_1^-+x_2^+-x_2^-+z_1=4,\\
&-x_1^++x_1^-+2x_2^+-2x_2^-+z_2=2,\\
&x_1^+,x_1^-,x_2^+,x_2^-,z_1,z_2\ge0.
\end{aligned}
$$

For example, $x_1=2,x_2=1$ is feasible in the original problem. It corresponds to

$$
x_1^+=2,\quad x_1^-=0,\quad
x_2^+=1,\quad x_2^-=0.
$$

The slacks are

$$
z_1=4-(2+1)=1,
$$

$$
z_2=2-(-2+2)=2.
$$

Therefore,

$$
(x_1^+,x_1^-,x_2^+,x_2^-,z_1,z_2)
=
(2,0,1,0,1,2)
$$

is feasible in the transformed LP.

---

# 11.2 Deriving Farkas’ Lemma B from Lemma A

The same transformation converts the inequality system in Lemma B into the equality system covered by Lemma A.

---

## 1. Start with the System in Lemma B

We are given

$$
Ax\le b,
$$

where $x$ is unrestricted.

Introduce

$$
x=x^+-x^-,
\qquad x^+,x^-\ge0,
$$

and slack variables

$$
z\ge0.
$$

Then

$$
Ax\le b
$$

is equivalent to

$$
Ax^+-Ax^-+z=b,
$$

with

$$
x^+,x^-,z\ge0.
$$

In block matrix form,

$$
\begin{bmatrix}
A&-A&I_m
\end{bmatrix}
\begin{bmatrix}
x^+\\
x^-\\
z
\end{bmatrix}
=b.
$$

Define

$$
M=
\begin{bmatrix}
A&-A&I_m
\end{bmatrix}.
$$

We can now apply Farkas’ Lemma A to

$$
My=b,
\qquad y\ge0.
$$

---

## 2. Apply Farkas’ Lemma A

Lemma A says the transformed system is infeasible if and only if there exists a vector $\lambda\in\mathbb R^m$ such that

$$
\lambda^Tb<0
$$

and

$$
\lambda^TM\ge0.
$$

Since

$$
M=[A\; -A\; I_m],
$$

the condition $\lambda^TM\ge0$ means

$$
\begin{bmatrix}
\lambda^TA&
-\lambda^TA&
\lambda^T
\end{bmatrix}
\ge0.
$$

This gives three sets of conditions.

### Columns corresponding to $x^+$

$$
\lambda^TA\ge0.
$$

### Columns corresponding to $x^-$

$$
-\lambda^TA\ge0.
$$

Equivalently,

$$
\lambda^TA\le0.
$$

Combining the two,

$$
\lambda^TA\ge0
\quad\text{and}\quad
\lambda^TA\le0,
$$

so

$$
\boxed{\lambda^TA=0.}
$$

Componentwise,

$$
\sum_{j=1}^m\lambda_jA_{ji}=0,
\qquad i=1,\ldots,n.
$$

### Columns corresponding to $z$

Because the slack-variable coefficient matrix is $I_m$,

$$
\lambda^TI_m\ge0.
$$

Therefore,

$$
\boxed{\lambda\ge0.}
$$

Together with the remaining Lemma A condition,

$$
\boxed{\lambda^Tb<0,}
$$

we obtain exactly Farkas’ Lemma B:

$$
\lambda_j\ge0,
$$

$$
\sum_{j=1}^m\lambda_jb_j<0,
$$

and

$$
\sum_{j=1}^m\lambda_jA_{ji}=0
\qquad\text{for every }i.
$$

Therefore, Lemma A implies Lemma B.

---

## 3. Visualizing Where the Conditions Come From

```text
Original inequality system
        Ax <= b
           |
           | split x = x+ - x-
           | add slack z >= 0
           v
[A | -A | I] [x+; x-; z] = b
           |
           | apply Farkas A
           v
lambda^T [A | -A | I] >= 0
           |
           +--------------------------+
           |            |             |
           v            v             v
 lambda^T A >= 0  -lambda^T A >= 0  lambda >= 0
           |            |
           +-----+------+
                 v
          lambda^T A = 0
```

The equality $\lambda^TA=0$ appears because every unrestricted variable creates both an $A$ column and a $-A$ column.

The condition $\lambda\ge0$ appears because every inequality introduces a slack-variable column from the identity matrix.

---

## 4. Why $\lambda$ Is a Certificate of Infeasibility

Suppose a vector $\lambda$ satisfies

$$
\lambda\ge0,
\qquad
\lambda^TA=0,
\qquad
\lambda^Tb<0.
$$

Assume, for contradiction, that some $x$ satisfies

$$
Ax\le b.
$$

Because $\lambda\ge0$, multiplying each inequality by $\lambda_j$ and adding preserves the inequality:

$$
\lambda^TAx\le\lambda^Tb.
$$

But

$$
\lambda^TA=0,
$$

so

$$
\lambda^TAx=0.
$$

Consequently,

$$
0\le\lambda^Tb.
$$

This contradicts

$$
\lambda^Tb<0.
$$

Therefore, no feasible $x$ can exist.

The vector $\lambda$ is called a **certificate of infeasibility** because anyone can verify the three conditions and conclude immediately that the original system is infeasible.

---

## 5. Concrete Farkas Certificate Example

Consider

$$
x\le0
$$

and

$$
-x\le-1.
$$

The second inequality means $x\ge1$. Thus, the system requires

$$
x\le0
\quad\text{and}\quad
x\ge1,
$$

which is impossible.

Write it as

$$
Ax\le b,
$$

where

$$
A=
\begin{bmatrix}
1\\
-1
\end{bmatrix},
\qquad
b=
\begin{bmatrix}
0\\
-1
\end{bmatrix}.
$$

Choose

$$
\lambda=
\begin{bmatrix}
1\\
1
\end{bmatrix}.
$$

Check the conditions.

### Nonnegativity

$$
\lambda\ge0.
$$

### Cancellation of variables

$$
\lambda^TA
=
1(1)+1(-1)
=
0.
$$

### Negative combination of right-hand sides

$$
\lambda^Tb
=
1(0)+1(-1)
=
-1<0.
$$

Therefore, $\lambda=(1,1)^T$ certifies infeasibility.

The weighted sum of the original inequalities is

$$
x+(-x)\le0+(-1),
$$

which simplifies to

$$
0\le-1.
$$

This impossible inequality proves that the original system has no solution.

---

# Key Patterns to Remember

## LP2 to LP1

$$
\boxed{x=x^+-x^-,\qquad x^+,x^-\ge0}
$$

handles unrestricted variables.

$$
\boxed{Ax+z=b,\qquad z\ge0}
$$

handles $\le$ constraints.

Together,

$$
\boxed{
Ax\le b
\iff
Ax^+-Ax^-+z=b,
\quad x^+,x^-,z\ge0.
}
$$

## Farkas A to Farkas B

Apply Lemma A to

$$
[A\; -A\; I]
\begin{bmatrix}
x^+\\x^-\\z
\end{bmatrix}
=b.
$$

Then

$$
\lambda^T[A\; -A\; I]\ge0
$$

produces

$$
\lambda^TA\ge0,
\qquad
-\lambda^TA\ge0,
\qquad
\lambda\ge0.
$$

The first two imply

$$
\lambda^TA=0.
$$

Thus,

$$
\boxed{
Ax\le b\text{ is infeasible}
\iff
\exists\lambda\ge0:
\lambda^TA=0,\;
\lambda^Tb<0.
}
$$

> **Common sign error:** Do not use $Ax-z=b$ for a $\le$ constraint. The correct conversion is $Ax+z=b$, because $z=b-Ax\ge0$.
