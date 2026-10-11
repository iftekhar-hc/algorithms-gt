# Converting a Primal Linear Program to Its Dual

To convert a primal linear program into its **dual**, exchange the roles of variables and constraints, transpose the coefficient matrix, swap the objective coefficients with the constraint right-hand sides, and reverse the optimization direction. The signs of the dual variables and the directions of the dual constraints depend on the primal's constraint types and variable restrictions. ([Stanford lecture notes](https://theory.stanford.edu/~trevisan/cs261/lecture06.pdf), [general duality rules](https://en.wikipedia.org/wiki/Dual_linear_program))

Below is a step-by-step method, three worked examples, visual explanations, and pseudocode that handles mixed constraints.

## 1. Start with the standard maximization case

Suppose the primal is

```math
\begin{aligned}
\text{maximize}\quad & c^\top x\\
\text{subject to}\quad & Ax\le b,\\
&x\ge0.
\end{aligned}
```

Its dual is

```math
\begin{aligned}
\text{minimize}\quad & b^\top y\\
\text{subject to}\quad & A^\top y\ge c,\\
&y\ge0.
\end{aligned}
```

Here, `A` is an `m × n` matrix: the primal has `n` variables and `m` main constraints; the dual has `m` variables and `n` main constraints. Variable sign restrictions are not counted as main constraints in this correspondence. ([Stanford lecture notes](https://theory.stanford.edu/~trevisan/cs261/lecture06.pdf))

### Visual correspondence

```text
PRIMAL                                  DUAL

maximize                                minimize
objective coefficients c ─────────────► constraint RHS c
constraint RHS b ─────────────────────► objective coefficients b

m constraint rows ────────────────────► m dual variables
n primal variables ───────────────────► n dual constraint rows

coefficient matrix A ─────────────────► transposed matrix Aᵀ
```

The essential structural idea is:

```text
A row of the primal becomes a dual variable.
A column of the primal becomes a dual constraint.
```

This is why the matrix is transposed.

## 2. Example 1: Maximization with “≤” constraints

Consider

```math
\begin{aligned}
\text{maximize}\quad &3x_1+2x_2\\
\text{subject to}\quad
&x_1+x_2\le4,\\
&2x_1+x_2\le5,\\
&x_1,x_2\ge0.
\end{aligned}
```

### Step 1: Introduce one dual variable per constraint

Associate:

- `y₁` with `x₁ + x₂ ≤ 4`.
- `y₂` with `2x₁ + x₂ ≤ 5`.

Because this is a maximization primal with “≤” constraints, both dual variables are nonnegative.

### Step 2: Form the dual objective from the primal right-hand sides

The right-hand sides are `4` and `5`, so the dual objective is

```math
\text{minimize}\quad 4y_1+5y_2.
```

### Step 3: Read each primal column to build a dual constraint

For `x₁`, the constraint coefficients are `1, 2`, and its objective coefficient is `3`:

```math
y_1+2y_2\ge3.
```

For `x₂`, the constraint coefficients are `1, 1`, and its objective coefficient is `2`:

```math
y_1+y_2\ge2.
```

Therefore, the dual is

```math
\boxed{
\begin{aligned}
\text{minimize}\quad &4y_1+5y_2\\
\text{subject to}\quad
&y_1+2y_2\ge3,\\
&y_1+y_2\ge2,\\
&y_1,y_2\ge0.
\end{aligned}}
```

### Matrix visualization

```math
A=
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix},
\qquad
A^\top=
\begin{bmatrix}
1&2\\
1&1
\end{bmatrix}.
```

```text
Primal coefficient table                Dual coefficient table

          x₁   x₂   RHS                           y₁   y₂   RHS
row 1      1    1     4                  row 1      1    2     3
row 2      2    1     5                  row 2      1    1     2

objective  3    2                       objective   4    5
```

Notice how the original objective row becomes the dual right-hand-side column, while the original right-hand-side column becomes the dual objective row.

### Geometric visualization

The primal's feasible region is the quadrilateral with vertices

```math
(0,0),\quad (2.5,0),\quad (1,3),\quad (0,4).
```

```text
x₂
↑
4   ● (0,4)
    │╲
3   │ ● (1,3)  ← optimum
    │  ╲
2   │   ╲
    │    ╲
1   │     ╲
    │      ╲
0   ●───────●────────→ x₁
  (0,0)   (2.5,0)

Schematic, not to scale.
Feasible points lie inside or on the quadrilateral.
```

Evaluating the objective at the vertices:

| Vertex | Objective: 3x₁ + 2x₂ |
|---|---:|
| (0, 0) | 0 |
| (2.5, 0) | 7.5 |
| (1, 3) | 9 |
| (0, 4) | 8 |

The primal optimum is `x = (1, 3)`, with objective value `9`.

The dual point `y = (1, 1)` is feasible because

```math
1+2(1)=3,\qquad 1+1=2,
```

and its objective value is also

```math
4(1)+5(1)=9.
```

Matching feasible primal and dual objective values certify that both solutions are optimal. ([Stanford lecture notes](https://theory.stanford.edu/~trevisan/cs261/lecture06.pdf))

## 3. Why the dual works: constructing a bound

For the standard maximization case, multiply each primal constraint by its nonnegative dual variable and add:

```math
y^\top Ax\le y^\top b.
```

Dual feasibility requires

```math
A^\top y\ge c.
```

Since `x ≥ 0`,

```math
c^\top x\le (A^\top y)^\top x=y^\top Ax.
```

Combining these inequalities gives

```math
\boxed{c^\top x\le b^\top y.}
```

Thus, every feasible dual solution provides an upper bound on every feasible primal objective value. This is weak duality. When an LP has a finite optimum, strong duality gives equality between the optimal primal and dual values. ([Stanford lecture notes](https://theory.stanford.edu/~trevisan/cs261/lecture06.pdf), [MIT chapter on duality](https://web.mit.edu/15.053/www/AMP-Chapter-04.pdf))

For Example 1, choosing `y₁ = y₂ = 1` simply adds the two constraints:

```math
\begin{aligned}
x_1+x_2&\le4,\\
2x_1+x_2&\le5,\\
\hline
3x_1+2x_2&\le9.
\end{aligned}
```

The primal achieves `9`, so this bound is tight.

## 4. General conversion rules

You do not have to transform every LP into the standard form above. You can directly handle equality constraints, mixed inequalities, and unrestricted variables.

Use two separate tables: one determines dual variable signs; the other determines dual constraint directions. ([General duality rules](https://en.wikipedia.org/wiki/Dual_linear_program))

### A. Primal constraint type → dual variable sign

| Primal constraint | Maximization primal | Minimization primal |
|---|---|---|
| aᵢᵀx ≤ bᵢ | yᵢ ≥ 0 | yᵢ ≤ 0 |
| aᵢᵀx ≥ bᵢ | yᵢ ≤ 0 | yᵢ ≥ 0 |
| aᵢᵀx = bᵢ | yᵢ unrestricted | yᵢ unrestricted |

### B. Primal variable sign → dual constraint direction

The dual constraint for `xⱼ` compares component `j` of `Aᵀy` with `cⱼ`.

| Primal variable restriction | Maximization primal | Minimization primal |
|---|---|---|
| xⱼ ≥ 0 | (Aᵀy)ⱼ ≥ cⱼ | (Aᵀy)ⱼ ≤ cⱼ |
| xⱼ ≤ 0 | (Aᵀy)ⱼ ≤ cⱼ | (Aᵀy)ⱼ ≥ cⱼ |
| xⱼ unrestricted | (Aᵀy)ⱼ = cⱼ | (Aᵀy)ⱼ = cⱼ |

“Unrestricted” means the variable may be positive, negative, or zero. Equality constraints correspond to unrestricted dual variables; unrestricted primal variables correspond to equality constraints in the dual.

## 5. Example 2: Minimization with “≥” constraints

Consider

```math
\begin{aligned}
\text{minimize}\quad &4x_1+5x_2\\
\text{subject to}\quad
&x_1+2x_2\ge3,\\
&x_1+x_2\ge2,\\
&x_1,x_2\ge0.
\end{aligned}
```

Apply the minimization column of the rules:

1. Change minimization to maximization.
2. Use `3, 2`, the primal right-hand sides, as dual objective coefficients.
3. Both primal constraints are “≥,” so `y₁, y₂ ≥ 0`.
4. Both primal variables are nonnegative, so both dual constraints are “≤.”

The result is

```math
\boxed{
\begin{aligned}
\text{maximize}\quad &3y_1+2y_2\\
\text{subject to}\quad
&y_1+y_2\le4,\\
&2y_1+y_2\le5,\\
&y_1,y_2\ge0.
\end{aligned}}
```

This is Example 1's primal, with different variable names. It illustrates that taking the dual twice recovers the original primal, up to equivalent representations. ([MIT chapter on duality](https://web.mit.edu/15.053/www/AMP-Chapter-04.pdf))

## 6. Example 3: Mixed constraints and variable signs

Consider

```math
\begin{aligned}
\text{maximize}\quad &4x_1+x_2-2x_3\\
\text{subject to}\quad
&x_1+2x_2-x_3\le6,\\
&3x_1-x_2+2x_3\ge4,\\
&x_1+x_2+x_3=3,\\
&x_1\ge0,\quad x_2\text{ unrestricted},\quad x_3\le0.
\end{aligned}
```

### Dual variables

Because the primal maximizes:

```text
Primal row 1: ≤    →    y₁ ≥ 0
Primal row 2: ≥    →    y₂ ≤ 0
Primal row 3: =    →    y₃ unrestricted
```

The dual objective is

```math
\text{minimize}\quad 6y_1+4y_2+3y_3.
```

### Dual constraints

Read the columns and apply the primal variable restrictions:

| Primal variable | Its column in A | Dual constraint |
|---|---|---|
| x₁ ≥ 0 | (1, 3, 1)ᵀ | y₁ + 3y₂ + y₃ ≥ 4 |
| x₂ unrestricted | (2, −1, 1)ᵀ | 2y₁ − y₂ + y₃ = 1 |
| x₃ ≤ 0 | (−1, 2, 1)ᵀ | −y₁ + 2y₂ + y₃ ≤ −2 |

Hence,

```math
\boxed{
\begin{aligned}
\text{minimize}\quad &6y_1+4y_2+3y_3\\
\text{subject to}\quad
&y_1+3y_2+y_3\ge4,\\
&2y_1-y_2+y_3=1,\\
&-y_1+2y_2+y_3\le-2,\\
&y_1\ge0,\quad y_2\le0,\quad y_3\text{ unrestricted}.
\end{aligned}}
```

The negative right-hand side in the final dual constraint does not determine its direction. The restriction `x₃ ≤ 0` determines that direction. ([General duality rules](https://en.wikipedia.org/wiki/Dual_linear_program))

## 7. Pseudocode for converting a general LP

Represent the primal using:

- `sense`: `MAX` or `MIN`
- `A`: an `m × n` constraint matrix
- `b`: the `m` right-hand sides
- `c`: the `n` objective coefficients
- `row_type[i]`: `LE`, `GE`, or `EQ`
- `variable_sign[j]`: `NONNEG`, `NONPOS`, or `FREE`

The following implements the general correspondence rules.

```text
FUNCTION BuildDual(sense, A, b, c, row_type, variable_sign):

    m ← number of rows in A
    n ← number of columns in A

    REQUIRE length(b) = m
    REQUIRE length(c) = n
    REQUIRE length(row_type) = m
    REQUIRE length(variable_sign) = n

    dual.sense ← MIN if sense = MAX, otherwise MAX
    dual.A ← TRANSPOSE(A)
    dual.objective ← COPY(b)
    dual.rhs ← COPY(c)

    # One dual variable per primal constraint
    FOR i FROM 1 TO m:

        IF row_type[i] = EQ:
            dual.variable_sign[i] ← FREE

        ELSE IF sense = MAX:
            IF row_type[i] = LE:
                dual.variable_sign[i] ← NONNEG
            ELSE:
                dual.variable_sign[i] ← NONPOS

        ELSE:  # primal minimizes
            IF row_type[i] = GE:
                dual.variable_sign[i] ← NONNEG
            ELSE:
                dual.variable_sign[i] ← NONPOS

    # One dual constraint per primal variable
    FOR j FROM 1 TO n:

        IF variable_sign[j] = FREE:
            dual.row_type[j] ← EQ

        ELSE IF sense = MAX:
            IF variable_sign[j] = NONNEG:
                dual.row_type[j] ← GE
            ELSE:
                dual.row_type[j] ← LE

        ELSE:  # primal minimizes
            IF variable_sign[j] = NONNEG:
                dual.row_type[j] ← LE
            ELSE:
                dual.row_type[j] ← GE

    RETURN dual
```

This constructs the dual; it does not solve either optimization problem.

For an explicit dense `m × n` matrix, materializing the transpose takes `O(mn)` time and storage.

## 8. Final checking checklist

Before accepting your dual, check:

1. Optimization direction: maximization became minimization, or vice versa.
2. Dimensions: `m` primal rows became `m` dual variables; `n` primal variables became `n` dual rows.
3. Coefficients: dual objective is `bᵀy`; dual right-hand sides are `c`.
4. Matrix: each dual constraint uses a column of the original `A`.
5. Signs: primal row types determine dual variable signs.
6. Directions: primal variable restrictions determine dual row types.

A useful memory aid is: “Rows become variables; columns become constraints; b becomes the objective; c becomes the right-hand side.”
