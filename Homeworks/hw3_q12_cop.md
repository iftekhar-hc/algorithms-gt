Here is the text with consistent inline and display math formatting, including corrected absolute-value notation in the tables.

# LP Formulations for \(\ell_1\) and \(\ell_\infty\) Regression

The central difficulty is that absolute values and maximums are not linear functions. The standard LP technique is to introduce auxiliary variables that represent the errors, then constrain those variables using linear inequalities.

For a proposed line

\[
\hat y=ax+b,
\]

the prediction at \(x_i\) is

\[
\hat y_i=ax_i+b.
\]

Define the signed residual

\[
r_i=y_i-\hat y_i=y_i-ax_i-b.
\]

Geometrically, \(r_i\) is the vertical difference between the observed point and the fitted line:

```text
        observed point (xi, yi)
                  ●
                  │
                  │ residual ri = yi - (axi+b)
                  │
fitted line  -----×----------------
              (xi, axi+b)
```

- \(r_i>0\): the point lies above the line.
- \(r_i<0\): the point lies below the line.
- \(\lvert r_i\rvert\): the magnitude of the vertical error.

The variables \(a\) and \(b\) are unrestricted because the slope and intercept may be positive, negative, or zero.

---

## 1. \(\ell_1\) regression

We want to solve

\[
\min_{a,b}\sum_{i=1}^{n}\lvert y_i-ax_i-b\rvert.
\]

**Step 1:** Introduce one error variable per point.

Introduce variables

\[
t_1,t_2,\ldots,t_n,
\]

where \(t_i\) is intended to represent

\[
t_i=\lvert y_i-ax_i-b\rvert.
\]

Because absolute values are nonlinear, we enforce this relationship with two inequalities.

For any real number \(r_i\),

\[
t_i\ge \lvert r_i\rvert
\]

is equivalent to

\[
t_i\ge r_i
\]

and

\[
t_i\ge -r_i.
\]

Substituting \(r_i=y_i-ax_i-b\), we obtain

\[
t_i\ge y_i-ax_i-b
\]

and

\[
t_i\ge -y_i+ax_i+b.
\]

Equivalently,

\[
y_i-ax_i-b\le t_i,
\]

\[
-y_i+ax_i+b\le t_i.
\]

**Step 2:** Minimize the sum of the error variables.

The LP is

\[
\boxed{
\begin{aligned}
\min_{a,b,t_1,\ldots,t_n}\quad
    &\sum_{i=1}^{n}t_i\\[2mm]
\text{subject to}\quad
    &y_i-ax_i-b\le t_i,
        &&i=1,\ldots,n,\\
    &-y_i+ax_i+b\le t_i,
        &&i=1,\ldots,n,\\
    &t_i\ge 0,
        &&i=1,\ldots,n,\\
    &a,b\in\mathbb R.
\end{aligned}
}
\]

The explicit constraints \(t_i\ge0\) are redundant because the first two inequalities already imply \(t_i\ge \lvert r_i\rvert\ge0\), but including them makes the meaning of the variables clearer.

Why does minimizing \(t_i\) produce equality?

For fixed \(a\) and \(b\), the constraints say

\[
t_i\ge \lvert y_i-ax_i-b\rvert.
\]

Because the objective minimizes \(\sum_i t_i\), the optimizer has no reason to make any \(t_i\) larger than necessary. Therefore, at an optimum,

\[
t_i=\lvert y_i-ax_i-b\rvert.
\]

The objective consequently becomes exactly the desired \(\ell_1\) loss.

The formulation has:

- \(n+2\) main variables: \(a,b,t_1,\ldots,t_n\)
- \(2n\) residual inequalities
- \(n\) nonnegativity constraints

Thus its size is \(O(n)\), and therefore polynomial in the input size.

---

## 2. \(\ell_\infty\) regression

Now we want to solve

\[
\min_{a,b}\max_{1\le i\le n}\lvert y_i-ax_i-b\rvert.
\]

Instead of giving every point its own objective variable, introduce one common variable \(t\) representing the largest absolute residual:

\[
t=\max_i \lvert y_i-ax_i-b\rvert.
\]

**Step 1:** Bound every residual by the same variable.

The condition

\[
\lvert y_i-ax_i-b\rvert\le t
\]

is equivalent to

\[
y_i-ax_i-b\le t
\]

and

\[
-y_i+ax_i+b\le t.
\]

These constraints must hold for every \(i\).

**Step 2:** Minimize the common upper bound.

The LP is

\[
\boxed{
\begin{aligned}
\min_{a,b,t}\quad
    &t\\[2mm]
\text{subject to}\quad
    &y_i-ax_i-b\le t,
        &&i=1,\ldots,n,\\
    &-y_i+ax_i+b\le t,
        &&i=1,\ldots,n,\\
    &t\ge0,\\
    &a,b\in\mathbb R.
\end{aligned}
}
\]

At an optimum,

\[
t=\max_i\lvert y_i-ax_i-b\rvert.
\]

If \(t\) were larger than the maximum residual, it could be decreased, improving the objective while maintaining feasibility.

For the geometric interpretation, the inequalities

\[
-t\le y_i-ax_i-b\le t
\]

can be rearranged as

\[
ax_i+b-t\le y_i\le ax_i+b+t.
\]

Thus all points must lie inside a vertical strip of total width \(2t\) around the fitted line:

```text
Upper boundary:  y = ax + b + t
                  /----------------
                 /      ●
Fitted line:    /----------------    y = ax + b
               /   ●
Lower boundary:/----------------     y = ax + b - t

Every point must lie between the two boundaries.
```

The goal is to make this strip as narrow as possible.

This formulation has:

- 3 variables: \(a,b,t\)
- \(2n\) residual inequalities
- One nonnegativity constraint

Its size is also \(O(n)\).

---

## 3. \(\ell_1\) regression dual

Start with

\[
\begin{aligned}
\min\quad &\sum_{i=1}^{n}t_i\\
\text{s.t.}\quad
&y_i-ax_i-b-t_i\le0,\\
&-y_i+ax_i+b-t_i\le0,\\
&t_i\ge0.
\end{aligned}
\]

Associate nonnegative dual variables:

- \(u_i\ge0\) with \(y_i-ax_i-b-t_i\le0\)
- \(v_i\ge0\) with \(-y_i+ax_i+b-t_i\le0\)

**Step 1:** Write the Lagrangian.

\[
\begin{aligned}
L(a,b,t,u,v)
={}&\sum_{i=1}^{n}t_i\\
&+\sum_{i=1}^{n}u_i(y_i-ax_i-b-t_i)\\
&+\sum_{i=1}^{n}v_i(-y_i+ax_i+b-t_i).
\end{aligned}
\]

Collect terms:

\[
\begin{aligned}
L
={}&\sum_{i=1}^{n}(u_i-v_i)y_i\\
&+a\sum_{i=1}^{n}(v_i-u_i)x_i\\
&+b\sum_{i=1}^{n}(v_i-u_i)\\
&+\sum_{i=1}^{n}(1-u_i-v_i)t_i.
\end{aligned}
\]

**Step 2:** Obtain conditions from the free variables \(a\) and \(b\).

Because \(a\) is unrestricted, the coefficient of \(a\) must be zero:

\[
\sum_{i=1}^{n}(u_i-v_i)x_i=0.
\]

Similarly, because \(b\) is unrestricted,

\[
\sum_{i=1}^{n}(u_i-v_i)=0.
\]

**Step 3:** Obtain the condition from \(t_i\ge0\).

To ensure that minimizing over \(t_i\ge0\) does not produce \(-\infty\), we need

\[
1-u_i-v_i\ge0.
\]

Therefore,

\[
u_i+v_i\le1.
\]

The dual in terms of \(u_i,v_i\) is

\[
\begin{aligned}
\max_{u,v}\quad
    &\sum_{i=1}^{n}(u_i-v_i)y_i\\
\text{subject to}\quad
    &\sum_{i=1}^{n}(u_i-v_i)x_i=0,\\
    &\sum_{i=1}^{n}(u_i-v_i)=0,\\
    &u_i+v_i\le1,
        &&i=1,\ldots,n,\\
    &u_i,v_i\ge0,
        &&i=1,\ldots,n.
\end{aligned}
\]

**Step 4:** Simplify using one signed variable.

Define

\[
z_i=u_i-v_i.
\]

Since \(u_i,v_i\ge0\) and \(u_i+v_i\le1\),

\[
\lvert z_i\rvert\le1.
\]

The simplified dual is therefore

\[
\boxed{
\begin{aligned}
\max_{z\in\mathbb R^n}\quad
    &\sum_{i=1}^{n}y_i z_i\\
\text{subject to}\quad
    &\sum_{i=1}^{n}x_i z_i=0,\\
    &\sum_{i=1}^{n}z_i=0,\\
    &\lvert z_i\rvert\le1,
        &&i=1,\ldots,n.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
\max y^\top z
\quad\text{subject to}\quad
X^\top z=0,\qquad
\lVert z\rVert_\infty\le1,
}
\]

where

\[
X=
\begin{bmatrix}
x_1&1\\
x_2&1\\
\vdots&\vdots\\
x_n&1
\end{bmatrix}.
\]

---

## 4. \(\ell_\infty\) regression dual

The primal is

\[
\begin{aligned}
\min\quad&t\\
\text{s.t.}\quad
&y_i-ax_i-b-t\le0,\\
&-y_i+ax_i+b-t\le0,\\
&t\ge0.
\end{aligned}
\]

As before, introduce \(u_i,v_i\ge0\).

**Step 1:** Form the Lagrangian.

\[
\begin{aligned}
L
={}&t
+\sum_{i=1}^{n}u_i(y_i-ax_i-b-t)\\
&+\sum_{i=1}^{n}v_i(-y_i+ax_i+b-t).
\end{aligned}
\]

Collecting terms gives

\[
\begin{aligned}
L
={}&\sum_{i=1}^{n}(u_i-v_i)y_i\\
&+a\sum_{i=1}^{n}(v_i-u_i)x_i\\
&+b\sum_{i=1}^{n}(v_i-u_i)\\
&+\left(1-\sum_{i=1}^{n}(u_i+v_i)\right)t.
\end{aligned}
\]

**Step 2:** Obtain conditions from \(a\) and \(b\).

Since \(a,b\) are unrestricted,

\[
\sum_{i=1}^{n}(u_i-v_i)x_i=0
\]

and

\[
\sum_{i=1}^{n}(u_i-v_i)=0.
\]

**Step 3:** Obtain the condition from \(t\ge0\).

We need

\[
1-\sum_{i=1}^{n}(u_i+v_i)\ge0,
\]

so

\[
\sum_{i=1}^{n}(u_i+v_i)\le1.
\]

The dual is

\[
\begin{aligned}
\max_{u,v}\quad
    &\sum_{i=1}^{n}(u_i-v_i)y_i\\
\text{subject to}\quad
    &\sum_{i=1}^{n}(u_i-v_i)x_i=0,\\
    &\sum_{i=1}^{n}(u_i-v_i)=0,\\
    &\sum_{i=1}^{n}(u_i+v_i)\le1,\\
    &u_i,v_i\ge0.
\end{aligned}
\]

Define again

\[
z_i=u_i-v_i.
\]

The smallest possible value of \(u_i+v_i\) for a given \(z_i\) is \(\lvert z_i\rvert\). Consequently, the budget constraint becomes

\[
\sum_{i=1}^{n}\lvert z_i\rvert\le1.
\]

The simplified dual is

\[
\boxed{
\begin{aligned}
\max_{z\in\mathbb R^n}\quad
    &\sum_{i=1}^{n}y_i z_i\\
\text{subject to}\quad
    &\sum_{i=1}^{n}x_i z_i=0,\\
    &\sum_{i=1}^{n}z_i=0,\\
    &\sum_{i=1}^{n}\lvert z_i\rvert\le1.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
\max y^\top z
\quad\text{subject to}\quad
X^\top z=0,\qquad
\lVert z\rVert_1\le1.
}
\]

Although this compact form contains absolute values, it can itself be written as an LP by introducing nonnegative variables \(w_i\):

\[
-w_i\le z_i\le w_i,
\qquad
\sum_i w_i\le1.
\]

---

## 5. Worked example and interpretation

Consider the three points

\[
(0,0),\qquad (1,2),\qquad (2,2).
\]

```text
y
3 |
2 |       ●-------●
1 |
0 | ●
  +------------------- x
    0       1       2
```

For \(\ell_1\) regression, consider the line

\[
y=x.
\]

Its predictions and residuals are:

| \(i\) | Point | Prediction \(ax_i+b\) | Residual \(r_i\) | \(\lvert r_i\rvert\) |
|---:|---:|---:|---:|---:|
| 1 | \((0,0)\) | \(0\) | \(0\) | \(0\) |
| 2 | \((1,2)\) | \(1\) | \(1\) | \(1\) |
| 3 | \((2,2)\) | \(2\) | \(0\) | \(0\) |

Therefore,

\[
\sum_i\lvert r_i\rvert=1.
\]

A dual feasible solution is

\[
z=
\begin{bmatrix}
-\frac12\\
1\\
-\frac12
\end{bmatrix}.
\]

Check the dual constraints:

\[
\sum_i z_i=-\frac12+1-\frac12=0,
\]

\[
\sum_i x_i z_i
=0\left(-\frac12\right)+1(1)+2\left(-\frac12\right)=0,
\]

and

\[
\lvert z_i\rvert\le1.
\]

Its dual objective value is

\[
\sum_i y_i z_i
=0\left(-\frac12\right)+2(1)+2\left(-\frac12\right)
=1.
\]

The primal solution \(y=x\) has value \(1\), and the dual solution has value \(1\). By strong duality, both are optimal.

Thus an optimal \(\ell_1\) regression line is

\[
\boxed{y=x}
\]

with optimal objective value

\[
\boxed{1}.
\]

For \(\ell_\infty\) regression, consider the line

\[
y=x+\frac12.
\]

The residuals are

\[
\begin{aligned}
r_1&=0-\frac12=-\frac12,\\
r_2&=2-\frac32=\frac12,\\
r_3&=2-\frac52=-\frac12.
\end{aligned}
\]

Therefore,

\[
\max_i\lvert r_i\rvert=\frac12.
\]

Visually:

```text
Point residuals alternate between the strip boundaries:

upper boundary          ●
                       /
fitted line       -----/-----
                     /
lower boundary  ●---/-------●
```

For the dual, choose

\[
z=
\begin{bmatrix}
-\frac14\\
\frac12\\
-\frac14
\end{bmatrix}.
\]

Then

\[
\sum_i z_i=0,
\]

\[
\sum_i x_i z_i
=0\left(-\frac14\right)+1\left(\frac12\right)
 +2\left(-\frac14\right)=0,
\]

and

\[
\lVert z\rVert_1
=\frac14+\frac12+\frac14
=1.
\]

Its objective value is

\[
\sum_i y_i z_i
=0\left(-\frac14\right)
 +2\left(\frac12\right)
 +2\left(-\frac14\right)
=\frac12.
\]

The primal and dual values are equal, so the fitted line is optimal:

\[
\boxed{y=x+\frac12}
\]

with maximum absolute error

\[
\boxed{\frac12}.
\]

---

The primal norm and dual constraint norm are paired:

| Regression objective | Primal residual norm | Dual norm constraint |
|---|---:|---:|
| \(\ell_1\) regression | \(\lVert r\rVert_1\) | \(\lVert z\rVert_\infty\le1\) |
| \(\ell_\infty\) regression | \(\lVert r\rVert_\infty\) | \(\lVert z\rVert_1\le1\) |

This reflects the dual-norm relationships

\[
(\ell_1)^*=\ell_\infty,
\qquad
(\ell_\infty)^*=\ell_1.
\]

In both duals, the equations

\[
\sum_i z_i=0
\]

and

\[
\sum_i x_i z_i=0
\]

mean that the dual weights are orthogonal to both columns of the regression design matrix: the constant column and the \(x\)-coordinate column.

---

For the compact formulations below, let

\[
r_i=y_i-ax_i-b.
\]

The \(\ell_1\) primal is

\[
\boxed{
\begin{aligned}
\min\quad&\sum_i t_i\\
\text{s.t.}\quad&r_i\le t_i,\\
&-r_i\le t_i,\\
&t_i\ge0.
\end{aligned}
}
\]

The \(\ell_1\) dual is

\[
\boxed{
\begin{aligned}
\max\quad&\sum_i y_i z_i\\
\text{s.t.}\quad&\sum_i x_i z_i=0,\\
&\sum_i z_i=0,\\
&\lVert z\rVert_\infty\le1.
\end{aligned}
}
\]

The \(\ell_\infty\) primal is

\[
\boxed{
\begin{aligned}
\min\quad&t\\
\text{s.t.}\quad&r_i\le t,\\
&-r_i\le t,\\
&t\ge0.
\end{aligned}
}
\]

The \(\ell_\infty\) dual is

\[
\boxed{
\begin{aligned}
\max\quad&\sum_i y_i z_i\\
\text{s.t.}\quad&\sum_i x_i z_i=0,\\
&\sum_i z_i=0,\\
&\lVert z\rVert_1\le1.
\end{aligned}
}
\]

The key distinction is simple: \(\ell_1\) uses one auxiliary error variable per observation, while \(\ell_\infty\) uses one common variable that bounds every error.
