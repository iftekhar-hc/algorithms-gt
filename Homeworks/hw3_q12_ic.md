# LP for Regression

For a proposed line $\hat y=ax+b$, the prediction at $x_i$ is $\hat
y_i=ax_i+b$. 

We define the residual:

$$
r_i=y_i-\hat y_i=y_i-ax_i-b.
$$

## 1. $\ell_1$ regression

The objective is to solve:

$$
\min_{a,b}\sum_{i=1}^{n}\lvert y_i-ax_i-b\rvert.
$$

We introduce variables $t_1,t_2,\ldots,t_n$, where $t_i$ represents:

$$
t_i=\lvert y_i-ax_i-b\rvert.
$$

We note that $t_i\ge \lvert r_i\rvert$ is equivalent to:

$$t_i\ge r_i \text{ and } t_i\ge -r_i$$

Substituting, we obtain:

$$t_i\ge y_i-ax_i-b \text{ and } t_i\ge -y_i+ax_i+b$$

Re-writing, we get:

$$
y_i-ax_i-b\le t_i,
$$

$$
-y_i+ax_i+b\le t_i.
$$

Putting everything together, we get the LP for $\ell_1$ regression:

$$
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
$$

## 2. $\ell_\infty$ regression

Goal is to solve:

$$
\min_{a,b}\max_{1\le i\le n}\lvert y_i-ax_i-b\rvert.
$$

Let $t$ represent the largest absolute residual:

$$
t=\max_i \lvert y_i-ax_i-b\rvert.
$$

From the previous section, we have:

$$
y_i-ax_i-b\le t_i,
$$

$$
-y_i+ax_i+b\le t_i.
$$

Minimizing the upper bound, we get the LP for $\ell_\infty$ regression:

$$
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
$$

## 3. Dual
For both regression problems, we will use two dual variables for each point:

- $u_i\ge0$ for the constraint $ax_i+b+t_i\ge y_i$.
- $v_i\ge0$ for the constraint $-ax_i-b+t_i\ge-y_i$.

The dual objective is then:

$$
\max\sum_{i=1}^n(y_i u_i-y_i v_i) = \max\sum_{i=1}^n y_i(u_i-v_i).
$$

Dual constraints are derived as follows:

From the free variable $a$:
$$
\sum_{i=1}^n x_i u_i-\sum_{i=1}^n x_i v_i=0.
$$
$$
\sum_{i=1}^n x_i(u_i-v_i)=0.
$$

From the free variable $b$:
$$
\sum_{i=1}^n(u_i-v_i)=0.
$$

From each variable $t_i$:
$$
u_i+v_i\le1.
$$

Putting everything together, we get the dual LP for $\ell_1$:
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

For the dual LP of $\ell_\infty$, the constraints from the free variables $a$ and $b$ remain unchanged.

Since there is only one variable $t$, we have the following dual constraint:
$$
\sum_{i=1}^n(u_i+v_i)\le1.
$$

Finally, the dual LP for $\ell_\infty$:
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

