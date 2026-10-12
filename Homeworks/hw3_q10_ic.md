# 10. LPs
## 1. LP Formulation

Let

$$
x_A = \text{number of Bundle A units purchased},
$$

$$
x_B = \text{number of Bundle B units purchased}.
$$

$$
x_A,x_B\in \mathbb{R}_{\ge 0}.
$$

The following table lists the bundles and their costs:

| Bundle | Oranges | Bananas | Cost |
|---|---:|---:|---:|
| A | 1 | 2 | $3 |
| B | 3 | 1 | $2 |

The given problem is formulated as the following linear program:
$$
\boxed{
\begin{aligned}
\text{minimize}\quad
    &3x_A+2x_B\\[2mm]
\text{subject to}\quad
    &x_A+3x_B\ge 8
        &&\text{(oranges)}\\
    &2x_A+x_B\ge 20
        &&\text{(bananas)}\\
    &x_A\ge 0,\\
    &x_B\ge 0.
\end{aligned}}
$$

We note that:
- The objective $3x_A+2x_B$ is exactly the amount Alice spends.
- The first constraint guarantees at least 8 oranges.
- The second constraint guarantees at least 20 bananas.
- The nonnegativity constraints prohibit buying negative bundles.
- Since fractional bundles are allowed, $x_A$ and $x_B$ do not have to be integers.

## 2. Feasible solution with value $30
Considering only Bundle A, we have:

$$
x_A=10,\qquad x_B=0.
$$

Number of oranges:

$$
x_A+3x_B=10+3(0)=10 \ge 8.
$$

Number of bananas:

$$
2x_A+x_B=2(10)+0=20 \ge 20.
$$

Cost:

$$
3x_A+2x_B=3(10)+2(0)=30.
$$

Thus, $(x_A,x_B)=(10,0)$ is feasible and has objective value $30$.

This is an **upper bound** on the minimum cost: $\mathrm{OPT}\le 30$.

## 3. Optimality Proof

Every feasible solution satisfies

$$
2x_A+x_B\ge 20.
$$

Multiply this constraint by $\frac32$:

$$
\frac32(2x_A+x_B)\ge \frac32(20).
$$
$$
3x_A+\frac32x_B\ge 30.
$$
Because $x_B\ge 0$, multiplying by $\frac12$ gives

$$
\frac12x_B\ge 0.
$$

Summing them, we get:

$$
3x_A+2x_B\ge 30.
$$

which represents the total cost. Hence, the **lower bound** on the minimum cost: $\mathrm{OPT}\ge 30$.

Since we have both $\mathrm{OPT}\le 30$ and $\mathrm{OPT}\ge 30$, we conclude that:

$$
\boxed{\mathrm{OPT}=30}.
$$


