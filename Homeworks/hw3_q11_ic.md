## LP Equivalent Formulation
### 11.1 — Converting LP2 to LP1

LP2 is

$$
\begin{aligned}
\max\quad &\sum_{i=1}^n c_i x_i\\
\text{s.t.}\quad
&\sum_{i=1}^n A_{ji}x_i\le b_j,
&&j=1,\ldots,m.
\end{aligned}
$$

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
\sum_{i=1}^n A_{ji}x_i^+
-\sum_{i=1}^n A_{ji}x_i^-
+z_j=b_j.
$$

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

### 11.2 — Farkas' Lemma A implies Lemma B

Farkas' Lemma A says the following system is infeasible:

$$
Ax=b,\qquad x\ge0.
$$

if and only if there exists a vector $\lambda$ such that

$$
\lambda^Tb<0,\qquad \lambda^TA\ge0.
$$

Farkas' Lemma B says the following system is infeasible:

$$
Ax\le b.
$$

if and only if there exists $\lambda$ satisfying:

$$
\lambda\ge0,\qquad
\lambda^Tb<0,\qquad
\lambda^TA=0.
$$

We introduce a slack vector $z\ge0$ to the system in Lemma B:

$$
Ax+z=b.
$$

Let $x=x^+-x^-$ with $x^+,x^-\ge0$. Then, we have:

$$
Ax^+-Ax^-+z=b, \qquad x^+\ge0,x^-\ge0,z\ge0.
$$

Now, we can apply Lemma A to the above transformed system.

Re-writing the transformed system in matrix form:

$$
\begin{bmatrix}A&-A&I\end{bmatrix}
\begin{bmatrix}x^+\\x^-\\z\end{bmatrix}
=b,
$$

Let $\widetilde A = \begin{bmatrix}A&-A&I\end{bmatrix}$ and $\widetilde x = \begin{bmatrix}x^+\\x^-\\z\end{bmatrix}$. Then, $\widetilde x\ge0$.

By Lemma A, there exists a vector $\lambda$ such that:
$$
\lambda^Tb<0,\qquad \lambda^T\widetilde A\ge0.
$$

Substituting $\widetilde A$, we get:

$$
\lambda^T[A\ -A\ I]\ge0.
$$

Each term in the above equation satisfies the following:

$$
\lambda^TA\ge0,\qquad
-\lambda^TA\ge0,\qquad
\lambda^TI\ge0.
$$

Since $\lambda^TA\ge0$ and $-\lambda^TA\ge0$ or $\lambda^TA\le0$, we have:

$$
\lambda^TA=0.
$$

Next, $\lambda^Tb<0$ from Lemma A and $\lambda^TI=\lambda^T\ge0$.

Consolidating all the terms of interest:

$$
\lambda\ge0,\qquad
\lambda^Tb<0,\qquad
\lambda^TA=0.
$$

The above are the conditions in Lemma B proving the forward direction.

For backward direction, suppose there exists $\lambda\ge0$ with $\lambda^Tb<0$ and $\lambda^TA=0$.

Suppose there exists a feasible $x$ with $Ax\le b$.

Multiplying both sides by $\lambda^T$:

$$
\lambda^TAx\le\lambda^Tb.
$$

Since $\lambda^TA=0$, we get:

$$
0\le\lambda^Tb<0,
$$

which is not plausible.

Hence, the system must be infeasible.








