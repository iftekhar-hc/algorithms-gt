# LP for Regression: Step-by-Step Explanation

The key idea is that absolute values and maximums are not directly linear, but we can represent them using extra variables and linear constraints. Once we do that, both regression problems become linear programs (LPs).

We'll derive the two primal LPs, explain how to construct their duals, and work through an example.

## 1. Background: What are we optimizing?

We are given $n$ data points:

$$
(x_1,y_1),\ldots,(x_n,y_n).
$$

We want to find a line

$$
\hat y=ax+b,
$$

where $a$ is the slope and $b$ is the intercept.

For each data point, define its residual as the difference between the observed and predicted values:

$$
r_i=y_i-(ax_i+b).
$$

- If $r_i>0$, the line predicts too low.
- If $r_i<0$, the line predicts too high.
- If $r_i=0$, the line passes exactly through that point.

The question is how to measure the total error.

## Visual intuition: fitting a line

13.2. Simple Linear Regression — STAT 350

Each vertical gap between a point and the line represents the absolute residual $|r_i|$. The two objectives below measure these gaps differently.

### $\ell_1$ regression

$$
\min\sum_{i=1}^n |r_i|
$$

Minimizes the sum of all absolute errors.

### $\ell_\infty$ regression

$$
\min\max_i |r_i|
$$

Minimizes the largest absolute error.

### What makes a problem a linear program?

A linear program has:

- A linear objective function.
- Linear equality or inequality constraints.
- Variables that are allowed to be real numbers unless explicitly restricted.

Absolute values and maximums appear nonlinear at first glance. The trick is to introduce auxiliary variables that allow us to express the same optimization problem using linear constraints.

## 2. Part 1: $\ell_1$ regression

We want to solve

$$
\min_{a,b\in\mathbb R}
\sum_{i=1}^n |y_i-ax_i-b|.
$$

### Step 1: Introduce one variable per residual

Introduce a variable $t_i$ for each data point, intended to represent the magnitude of its residual:

$$
t_i\approx |y_i-ax_i-b|.
$$

How do we enforce this relationship using linear constraints?

Recall the identity

$$
|z|=\max\{z,-z\}.
$$

Therefore, requiring $t_i\ge |r_i|$ is equivalent to requiring both

$$
t_i\ge r_i
\qquad\text{and}\qquad
t_i\ge-r_i.
$$

Substitute $r_i=y_i-ax_i-b$:

$$
t_i\ge y_i-ax_i-b,
$$

$$
t_i\ge -y_i+ax_i+b.
$$

Both constraints are linear in $a,b,t_i$.

### Step 2: Minimize the sum of the auxiliary variables

Our objective becomes

$$
\min \sum_{i=1}^n t_i.
$$

Because every $t_i$ is constrained to be at least $|r_i|$, minimizing the sum forces each $t_i$ down to the smallest permissible value, namely $|r_i|$.

We can therefore write the LP as follows.

### Final answer: $\ell_1$ primal LP

$$
\boxed{
\begin{aligned}
\min\quad & \sum_{i=1}^n t_i\\
\text{subject to}\quad
& ax_i+b+t_i\ge y_i,
&& i=1,\ldots,n,\\
& -ax_i-b+t_i\ge -y_i,
&& i=1,\ldots,n,\\
& t_i\ge 0,
&& i=1,\ldots,n,\\
& a,b\in\mathbb R.
\end{aligned}
}
$$

The constraints $t_i\ge0$ are actually implied by the first two inequalities, but explicitly including them makes the interpretation clear.

There are $n+2$ variables and $O(n)$ constraints, so this is a polynomial-sized LP.

## 3. Part 2: $\ell_\infty$ regression

Now the objective is

$$
\min_{a,b\in\mathbb R}
\max_{1\le i\le n}|y_i-ax_i-b|.
$$

Instead of minimizing the sum of errors, we minimize the worst error.

### Step 1: Introduce one variable for the maximum error

Let $t$ represent the maximum absolute residual:

$$
t=\max_i |y_i-ax_i-b|.
$$

We can avoid the maximum by requiring that every absolute residual be at most $t$:

$$
|y_i-ax_i-b|\le t
\qquad\text{for all }i.
$$

Using the absolute-value identity again, this is equivalent to

$$
-t\le y_i-ax_i-b\le t.
$$

Splitting this into two inequalities gives

$$
ax_i+b+t\ge y_i,
$$

$$
-ax_i-b+t\ge -y_i.
$$

These are all linear constraints.

### Step 2: Minimize the maximum error

Since $t$ bounds every absolute residual from above, minimizing $t$ gives the smallest possible worst-case error.

### Final answer: $\ell_\infty$ primal LP

$$
\boxed{
\begin{aligned}
\min\quad & t\\
\text{subject to}\quad
& ax_i+b+t\ge y_i,
&& i=1,\ldots,n,\\
& -ax_i-b+t\ge -y_i,
&& i=1,\ldots,n,\\
& t\ge0,\\
& a,b\in\mathbb R.
\end{aligned}
}
$$

This LP has only three variables, $a,b,t$, and $2n+1$ inequalities. It is therefore polynomial-sized.

### The difference between the two formulations

Notice how little the constraints change:

- In $\ell_1$ regression, each point gets its own error variable $t_i$, and we minimize $\sum_i t_i$.
- In $\ell_\infty$ regression, all points share one error bound $t$, and we minimize $t$.

That distinction is the main modeling insight.

## 4. A small numerical example

Consider the three points

$$
(0,1),\quad (1,2),\quad (2,2).
$$

Here are two candidate lines and their residuals.

## Compare two possible fitted lines

Line A: $y=0.5x+1$

Predictions: $1,\ 1.5,\ 2$

Absolute residuals: $0,\ 0.5,\ 0$

Total error = 0.5; maximum error = 0.5

Line B: $y=0.5x+1.25$

Predictions: $1.25,\ 1.75,\ 2.25$

Absolute residuals: $0.25,\ 0.25,\ 0.25$

Total error = 0.75; maximum error = 0.25

Line A has a smaller sum of absolute errors than Line B, so it is better for the $\ell_1$ objective among these two candidates. Line B has a smaller maximum error, so it is better for the $\ell_\infty$ objective.

In fact, for these three points, both lines are optimal for their respective objectives: Line A achieves the minimum $\ell_1$ error of $0.5$, while Line B achieves the minimum $\ell_\infty$ error of $0.25$.

The example shows why the two objectives can produce different answers.

## 5. Part 3: Deriving the dual LPs

The dual is another LP associated with a primal LP. To derive it, we use a standard set of rules.

For a primal minimization LP written as

$$
\begin{aligned}
\min\quad & c^\top z\\
\text{subject to}\quad & Az\ge d,
\end{aligned}
$$

with $z\ge0$, the dual is

$$
\begin{aligned}
\max\quad & d^\top u\\
\text{subject to}\quad & A^\top u\le c,\\
&u\ge0.
\end{aligned}
$$

There is one important modification in our regression problems: $a$ and $b$ are free variables, meaning they may be positive, negative, or zero. In the dual, the constraints corresponding to free primal variables become equalities.

Here is a quick reference:

| Primal feature | Dual consequence |
| --- | --- |
| Minimization objective | Dual is a maximization |
| Constraint $Az\ge d$ | Dual variables are nonnegative |
| Primal variable $z_j\ge0$ | Corresponding dual constraint is $\le c_j$ |
| Free primal variable | Corresponding dual constraint is an equality |

For both regression problems, we will use two nonnegative dual variables per data point:

- $u_i\ge0$ for the constraint $ax_i+b+t_i\ge y_i$ (or its $\ell_\infty$ counterpart).
- $v_i\ge0$ for the constraint $-ax_i-b+t_i\ge-y_i$.

This makes the derivation systematic.

## 6. Dual of the $\ell_1$ regression LP

Recall the primal:

$$
\begin{aligned}
\min\quad &\sum_{i=1}^n t_i\\
\text{s.t.}\quad
&ax_i+b+t_i\ge y_i,\\
&-ax_i-b+t_i\ge-y_i,\\
&t_i\ge0,\quad a,b\text{ free}.
\end{aligned}
$$

### Step 1: Introduce dual variables

Assign $u_i\ge0$ to the first constraint and $v_i\ge0$ to the second constraint, for every $i$.

The dual objective is the sum of each primal constraint's right-hand side multiplied by its dual variable:

$$
\max\sum_{i=1}^n(y_i u_i-y_i v_i).
$$

Equivalently,

$$
\max\sum_{i=1}^n y_i(u_i-v_i).
$$

### Step 2: Derive the dual constraints

We derive one dual constraint for each primal variable.

From the free variable $a$:

The coefficient of $a$ is $x_i$ in the first constraint and $-x_i$ in the second. Since $a$ is free, the dual constraint is an equality:

$$
\sum_{i=1}^n x_i u_i-\sum_{i=1}^n x_i v_i=0.
$$

Equivalently,

$$
\sum_{i=1}^n x_i(u_i-v_i)=0.
$$

From the free variable $b$:

Its coefficients are $1$ and $-1$, respectively. Thus,

$$
\sum_{i=1}^n(u_i-v_i)=0.
$$

From each nonnegative variable $t_i$:

Its coefficient is $1$ in both primal constraints, and its objective coefficient is also $1$. The dual constraint is therefore

$$
u_i+v_i\le1.
$$

Finally, all dual variables must be nonnegative:

$$
u_i,v_i\ge0.
$$

### Final answer: $\ell_1$ dual LP

$$
\boxed{
\begin{aligned}
\max\quad &\sum_{i=1}^n y_i(u_i-v_i)\\
\text{subject to}\quad
&\sum_{i=1}^n x_i(u_i-v_i)=0,\\
&\sum_{i=1}^n(u_i-v_i)=0,\\
&u_i+v_i\le1,
&&i=1,\ldots,n,\\
&u_i,v_i\ge0,
&&i=1,\ldots,n.
\end{aligned}
}
$$

### An equivalent, more compact form

Define $z_i=u_i-v_i$. Since $u_i,v_i\ge0$ and $u_i+v_i\le1$, we have $-1\le z_i\le1$. Conversely, any $z_i\in[-1,1]$ can be represented by such $u_i,v_i$.

Thus, the dual can equivalently be written as

$$
\boxed{
\begin{aligned}
\max\quad &\sum_{i=1}^n y_i z_i\\
\text{subject to}\quad
&\sum_{i=1}^n x_i z_i=0,\\
&\sum_{i=1}^n z_i=0,\\
&-1\le z_i\le1,
&&i=1,\ldots,n.
\end{aligned}
}
$$

This compact version is also a linear program.

## 7. Dual of the $\ell_\infty$ regression LP

Recall the primal:

$$
\begin{aligned}
\min\quad &t\\
\text{s.t.}\quad
&ax_i+b+t\ge y_i,\\
&-ax_i-b+t\ge-y_i,\\
&t\ge0,\quad a,b\text{ free}.
\end{aligned}
$$

The structure is almost identical to the $\ell_1$ primal. The key difference is that there is now one shared nonnegative variable $t$ rather than $n$ separate variables $t_i$.

### Step 1: Introduce dual variables

As before, assign $u_i\ge0$ and $v_i\ge0$ to the two constraints for point $i$.

The dual objective is

$$
\max\sum_{i=1}^n y_i(u_i-v_i).
$$

### Step 2: Derive the constraints

The constraints corresponding to the free variables $a$ and $b$ are unchanged:

$$
\sum_{i=1}^n x_i(u_i-v_i)=0,
$$

$$
\sum_{i=1}^n(u_i-v_i)=0.
$$

But now there is only one variable $t$. Its coefficient is $1$ in every constraint, and its objective coefficient is $1$. Therefore, its dual constraint is

$$
\sum_{i=1}^n(u_i+v_i)\le1.
$$

Notice the difference:

- $\ell_1$: $u_i+v_i\le1$ for every individual $i$.
- $\ell_\infty$: $\sum_i(u_i+v_i)\le1$, a single constraint across all points.

### Final answer: $\ell_\infty$ dual LP

$$
\boxed{
\begin{aligned}
\max\quad &\sum_{i=1}^n y_i(u_i-v_i)\\
\text{subject to}\quad
&\sum_{i=1}^n x_i(u_i-v_i)=0,\\
&\sum_{i=1}^n(u_i-v_i)=0,\\
&\sum_{i=1}^n(u_i+v_i)\le1,\\
&u_i,v_i\ge0,
&&i=1,\ldots,n.
\end{aligned}
}
$$

This is a polynomial-sized LP with $2n$ variables, two equality constraints, one additional inequality, and nonnegativity constraints.

We can also use $z_i=u_i-v_i$ to express the dual more compactly as

$$
\boxed{
\begin{aligned}
\max\quad &\sum_{i=1}^n y_i z_i\\
\text{subject to}\quad
&\sum_{i=1}^n x_i z_i=0,\\
&\sum_{i=1}^n z_i=0,\\
&\sum_{i=1}^n |z_i|\le1.
\end{aligned}
}
$$

This last form is mathematically equivalent to the dual LP, although its absolute-value constraint is not written in standard linear form. The $u_i,v_i$ formulation above is the explicit LP.

## 8. Visual summary of the derivation

### Original regression objective

Residuals: $r_i=y_i-ax_i-b$

### $\ell_1$

One variable per point

$$
t_i\ge |r_i|
$$

Minimize

$$
\sum_i t_i
$$

### $\ell_\infty$

One shared variable

$$
t\ge |r_i|
$$

Minimize

$$
t
$$

### Linear constraints

Replace each absolute value with two inequalities.

### Primal LPs and their duals

Use the coefficients of $a,b$ to form equality constraints in the dual, then use the error-variable coefficients to obtain the remaining dual constraints.

## 9. Final answers at a glance

| Formulation | Objective | Key dual constraint |
| --- | --- | --- |
| $\ell_1$ primal | $\min\sum_i t_i$ | One error variable per point |
| $\ell_\infty$ primal | $\min t$ | One shared error bound |
| $\ell_1$ dual | $\max\sum_i y_i(u_i-v_i)$ | $u_i+v_i\le1$ for every $i$ |
| $\ell_\infty$ dual | $\max\sum_i y_i(u_i-v_i)$ | $\sum_i(u_i+v_i)\le1$ |

Both duals also have the two common equality constraints

$$
\sum_i x_i(u_i-v_i)=0,
\qquad
\sum_i(u_i-v_i)=0,
$$

and nonnegative dual variables $u_i,v_i$.

### What to remember for an exam

1. Linearize the absolute value: $t_i\ge r_i$ and $t_i\ge-r_i$.
2. Linearize the maximum: use one variable $t$ that bounds every $|r_i|$.
3. Form the dual systematically: each primal constraint gives a dual variable; each primal variable gives a dual constraint.
4. Watch for free variables: because $a$ and $b$ are unrestricted, their dual constraints are equalities.
5. Watch the error-variable structure: individual error variables give individual dual inequalities; one shared error variable gives one summed dual inequality.

The central insight is that changing the error measure changes the structure of the primal variables, and that change is reflected directly in the dual LP.
