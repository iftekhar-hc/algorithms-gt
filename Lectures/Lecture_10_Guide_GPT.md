# Converting a Primal Linear Program to Its Dual

## 1. Start with the standard maximization case

Suppose the primal is

$$
\begin{aligned}
\text{maximize}\quad & c^\top x \\
\text{subject to}\quad & Ax\le b, \\
& x\ge 0.
\end{aligned}
$$

Its dual is

$$
\begin{aligned}
\text{minimize}\quad & b^\top y \\
\text{subject to}\quad & A^\top y\ge c, \\
& y\ge 0.
\end{aligned}
$$

Here, $A$ is an $m\times n$ matrix.

## 2. Example 1: Maximization with $\le$ constraints

Consider

$$
\begin{aligned}
\text{maximize}\quad & 3x_1+2x_2 \\
\text{subject to}\quad
& x_1+x_2\le4, \\
& 2x_1+x_2\le5, \\
& x_1,x_2\ge0.
\end{aligned}
$$

### Step 2: Dual objective

$$
\text{minimize}\quad 4y_1+5y_2
$$

For $x_1$:

$$
y_1+2y_2\ge3
$$

For $x_2$:

$$
y_1+y_2\ge2
$$

Therefore,

$$
\boxed{
\begin{aligned}
\text{minimize}\quad &4y_1+5y_2 \\
\text{subject to}\quad
&y_1+2y_2\ge3, \\
&y_1+y_2\ge2, \\
&y_1,y_2\ge0.
\end{aligned}}
$$

### Matrix visualization

$$
A=
\begin{bmatrix}
1 & 1 \\
2 & 1
\end{bmatrix},
\qquad
A^\top=
\begin{bmatrix}
1 & 2 \\
1 & 1
\end{bmatrix}.
$$

### Geometric visualization

The primal feasible region has vertices

$$
(0,0),\quad (2.5,0),\quad (1,3),\quad (0,4).
$$

Evaluating the objective:

| Vertex | $3x_1+2x_2$ |
|----------|----------|
| $(0,0)$ | 0 |
| $(2.5,0)$ | 7.5 |
| $(1,3)$ | 9 |
| $(0,4)$ | 8 |

The primal optimum is $x=(1,3)$ with objective value $9$.

The dual point $y=(1,1)$ is feasible because

$$
1+2(1)=3,
\qquad
1+1=2,
$$

and its objective value is

$$
4(1)+5(1)=9.
$$

## 3. Why the dual works

$$
y^\top Ax\le y^\top b.
$$

Dual feasibility requires

$$
A^\top y\ge c.
$$

Since $x\ge0$,

$$
c^\top x\le (A^\top y)^\top x = y^\top Ax.
$$

Combining gives

$$
\boxed{c^\top x\le b^\top y.}
$$

For Example 1:

$$
\begin{aligned}
x_1+x_2 &\le 4, \\
2x_1+x_2 &\le 5, \\
\hline
3x_1+2x_2 &\le 9.
\end{aligned}
$$

## 4. General conversion rules

### A. Primal constraint type → dual variable sign

| Primal constraint | Maximization primal | Minimization primal |
|---|---|---|
| $a_i^Tx\le b_i$ | $y_i\ge0$ | $y_i\le0$ |
| $a_i^Tx\ge b_i$ | $y_i\le0$ | $y_i\ge0$ |
| $a_i^Tx=b_i$ | unrestricted | unrestricted |

### B. Primal variable sign → dual constraint direction

| Primal variable restriction | Maximization primal | Minimization primal |
|---|---|---|
| $x_j\ge0$ | $(A^Ty)_j\ge c_j$ | $(A^Ty)_j\le c_j$ |
| $x_j\le0$ | $(A^Ty)_j\le c_j$ | $(A^Ty)_j\ge c_j$ |
| free | $(A^Ty)_j=c_j$ | $(A^Ty)_j=c_j$ |

## 5. Example 2: Minimization with $\ge$ constraints

$$
\begin{aligned}
\text{minimize}\quad &4x_1+5x_2 \\
\text{subject to}\quad
&x_1+2x_2\ge3, \\
&x_1+x_2\ge2, \\
&x_1,x_2\ge0.
\end{aligned}
$$

Dual:

$$
\boxed{
\begin{aligned}
\text{maximize}\quad &3y_1+2y_2 \\
\text{subject to}\quad
&y_1+y_2\le4, \\
&2y_1+y_2\le5, \\
&y_1,y_2\ge0.
\end{aligned}}
$$

## 6. Example 3: Mixed constraints and variable signs

$$
\begin{aligned}
\text{maximize}\quad &4x_1+x_2-2x_3 \\
\text{subject to}\quad
&x_1+2x_2-x_3\le6, \\
&3x_1-x_2+2x_3\ge4, \\
&x_1+x_2+x_3=3, \\
&x_1\ge0,\quad x_2\text{ unrestricted},\quad x_3\le0.
\end{aligned}
$$

Dual:

$$
\boxed{
\begin{aligned}
\text{minimize}\quad &6y_1+4y_2+3y_3 \\
\text{subject to}\quad
&y_1+3y_2+y_3\ge4, \\
&2y_1-y_2+y_3=1, \\
&-y_1+2y_2+y_3\le-2, \\
&y_1\ge0,\quad y_2\le0,\quad y_3\text{ unrestricted}.
\end{aligned}}
$$

## 7. Pseudocode

```text
FUNCTION BuildDual(sense, A, b, c, row_type, variable_sign):
    m ← number of rows in A
    n ← number of columns in A
    dual.sense ← MIN if sense = MAX, otherwise MAX
    dual.A ← TRANSPOSE(A)
    dual.objective ← COPY(b)
    dual.rhs ← COPY(c)
    ...
    RETURN dual
```

## 8. Final checking checklist

- Optimization direction reversed.
- $m$ primal rows become $m$ dual variables.
- $n$ primal variables become $n$ dual constraints.
- Dual objective is $b^Ty$.
- Dual right-hand side is $c$.
- Rows become variables.
- Columns become constraints.
