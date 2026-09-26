# CS 6515 Lecture 9 Study Guide

## Linear Programming: Models and Geometry

**Course:** CS 6515, Graduate Algorithms
**Instructors:** Sahil Singla and Gerandy Brito
**Term:** Fall 2026
**Source note:** Lecture 9, unmarked notes

This guide explains the lecture, works the in-class exercises, and adds examples, ASCII visualizations, pseudocode, quizzes, and exam-style questions. Equations use plain-text Unicode notation and fenced text blocks, so no MathJax or LaTeX renderer is required.

---

## 1. Where this lecture sits

Part 1 designed algorithms from divide and conquer, dynamic programming, and graph structure. Part 2 starts from a different question: write the feasible solutions and the objective as a mathematical program, then use the structure of that program.

| Block | Lectures | Main questions |
|---|---|---|
| Linear programming | 9–11 | How do we model linear constraints? How do we certify optimality? |
| Convex optimization | 12–13 | What survives beyond linear functions? How does gradient descent approximate an optimum? |
| Approximation algorithms | 14–16 | When exact discrete optimization is hard, how do relaxations, rounding, and lower bounds give provable guarantees? |

Two connections are already in place. Maximum flow, from Lecture 8, is the first graph problem written as a linear program. The knapsack FPTAS from Lecture 5 previewed approximation. Later, linear programs will be used as relaxations of discrete problems.

The modeling lesson is the one to keep: an LP separates the **model** from the **algorithm**. You can prove facts about a proposed solution without rerunning a solver.

---

## 2. What a linear program is

A linear program has real-valued variables, a linear objective, and linear equality or non-strict inequality constraints. The canonical maximization form used in these lectures is

```text
maximize cᵀ x
subject to Ax ≤ b,
x ≥ 0,
```

where `A ∈ ℝ^(m × n)`, `b ∈ ℝ^(m)`, and `c ∈ ℝⁿ`. Inequalities are coordinatewise. Row `j` says

```text
∑_(i=1)ⁿ Aⱼᵢ xᵢ ≤ bⱼ.
```

For computational claims, the input coefficients are rational.

**Feasible region.**

```text
P = { x ∈ ℝⁿ : Ax ≤ b, x ≥ 0 }.
```

A vector in `P` is feasible. An optimal solution is a feasible vector whose objective is best. For a maximization problem, that means the largest value of `cᵀ x`.

### What is not a plain LP

These are outside the definition used here:

- a product constraint such as `x₁ x₂ ≤ 1`;
- a nonlinear objective such as `x₁² + x₂²`;
- an integrality requirement `xᵢ ∈ {0,1}`;
- a strict inequality.

The last one is subtle. Maximizing `x` subject to `x < 1` has supremum `1`, but no feasible point attains it. Non-strict inequalities are what let a finite LP attain its optimum.

### A tiny feasible example

```text
maximize x₁ + 2x₂
subject to x₁ + x₂ ≤ 3,
x₁, x₂ ≥ 0.
```

The point `(1,1)` is feasible and has value `3`. The point `(0,3)` is feasible and has value `6`. The point `(2,2)` is not feasible, because `2+2 = 4 > 3`.

---

## 3. Running example: smoothies

There are `3` units of oranges, `10` of bananas, and `6` of strawberries. Smoothies may be made in fractional liters.

| Smoothie | Oranges | Bananas | Strawberries | Revenue per liter |
|---|---:|---:|---:|---:|
| 1 | 1 | 2 | 0 | $5 |
| 2 | 0 | 1 | 2 | $4 |
| 3 | 1 | 1 | 1 | $6 |

Let `xᵢ` be liters of smoothie `i`.

```text
maximize 5x₁ + 4x₂ + 6x₃
subject to x₁ + x₃ ≤ 3 (oranges),
2x₁ + x₂ + x₃ ≤ 10 (bananas),
2x₂ + x₃ ≤ 6 (strawberries),
x₁, x₂, x₃ ≥ 0. (1)
```

The vector `(3,3,0)` uses `3` oranges, `9` bananas, and `6` strawberries. It is feasible and earns

```text
5· 3 + 4· 3 + 6· 0 = 27.
```

That proves `OPT ≥ 27`. It does not yet prove optimality, because some other feasible vector might earn more. A lower bound and an upper bound are different objects.

### Exercise: write `A`, `b`, and `c`

Putting the three resource inequalities into `Ax ≤ b`, and leaving nonnegativity separate as in the canonical form,

```text
A = [[1, 0, 1],
     [2, 1, 1],
     [0, 2, 1]]
b = [3, 10, 6]ᵀ
c = [5, 4, 6]ᵀ
```

If nonnegativity is folded into `A`, append three rows `-e₁ᵀ`, `-e₂ᵀ`, and `-e₃ᵀ`, with right-hand sides `0`. Both writings describe the same set.

### What changes for whole-liter batches?

Replace `xᵢ ≥ 0` by `xᵢ ∈ ℤ_(≥ 0)`. The resulting program is an **integer linear program**, not a plain LP. The feasible region is no longer a convex polyhedron in the continuous sense: the midpoint of two integer points need not be integer. Integral optima of arbitrary LPs are not guaranteed, so the continuous optimum is only a relaxation of the batch problem. Its value is an upper bound on the best whole-liter revenue, not necessarily an attainable revenue.

---

## 4. Maximum flow is an LP

For a directed network, give each edge `e` a variable `fₑ`. As in Lecture 8, the value is net flow out of the source:

```text
maximize ∑_((s,v)∈ E) fₛᵥ - ∑_((v,s)∈ E) fᵥₛ
subject to ∑_((u,v)∈ E) fᵤᵥ = ∑_((v,w)∈ E) f_vw (v ∉ {s,t}),
0 ≤ fₑ ≤ cₑ (e ∈ E).
```

There are `m = |E|` variables and `O(m+n)` constraints. Writing flow as an LP does not replace the specialized flow algorithms. It places flow inside a broader optimization framework.

### Fractional versus integral flow

The LP allows fractional flows. Lecture 8 proved that integer capacities guarantee an integral optimal flow. That is special structure. An arbitrary LP need not have an integral optimum.

**Example.** Maximize `x` subject to `x ≤ 1/2` and `x ≥ 0`. The unique optimum is `x = 1/2`, which is not an integer. Nothing in the definition of an LP forces vertices to have integer coordinates.

---

## 5. Equivalent forms

Any of the following can be rewritten in canonical form. The new formulation is only polynomially larger.

| Feature | Conversion |
|---|---|
| Minimize `cᵀ x` | Maximize `-cᵀ x`, then negate the optimal value. |
| `aᵀ x ≥ d` | Write `-aᵀ x ≤ -d`. |
| `aᵀ x = d` | Write both `aᵀ x ≤ d` and `-aᵀ x ≤ -d`. |
| Unrestricted `z` | Substitute `z = z⁺ - z⁻`, with `z⁺, z⁻ ≥ 0`. |

Another useful form adds a slack variable for each inequality:

```text
Ax + s = b, x, s ≥ 0,
```

where `s = b - Ax`. Each slack measures how far that inequality is from equality.

### Worked conversion

Convert

```text
minimize 2u - v
subject to u - v = 3,
u ≥ 0,
```

with `v` unrestricted, into canonical form.

1. Replace the objective by maximization of its negative: maximize `-2u + v`. The original optimal value is the negative of this new value.
2. Split the unrestricted variable: `v = v⁺ - v⁻`, with `v⁺, v⁻ ≥ 0`.
3. Split the equality into two inequalities.

The canonical program in variables `(u, v⁺, v⁻)` is

```text
maximize -2u + v⁺ - v⁻
subject to u - v⁺ + v⁻ ≤ 3,
-u + v⁺ - v⁻ ≤ -3,
u, v⁺, v⁻ ≥ 0.
```

A feasible point of the original problem, such as `(u,v) = (3,0)`, maps to `(u, v⁺, v⁻) = (3, 0, 0)`. A negative `v`, such as `v = -1` with `u = 2`, maps to `v⁺ = 0` and `v⁻ = 1`.

### Pseudocode: rewrite to canonical form

```text
function TO_CANONICAL(program):
    # program has objective sense, linear objective, and linear constraints
    variables ← copy of the original variables

    for each unrestricted variable z:
        replace z by z_plus - z_minus everywhere
        add z_plus ≥ 0 and z_minus ≥ 0
        add z_plus, z_minus to variables

    inequalities ← empty list
    for each constraint C:
        if C is aᵀx ≥ d:
            append (−a)ᵀx ≤ −d
        else if C is aᵀx = d:
            append aᵀx ≤ d
            append (−a)ᵀx ≤ −d
        else if C is aᵀx ≤ d:
            append aᵀx ≤ d
        else:
            reject C    # nonlinear, strict, or integral

    if objective sense is minimize cᵀx:
        new_objective ← maximize (−c)ᵀx
        remember to negate the optimal value at the end
    else:
        new_objective ← maximize cᵀx

    return (new_objective, inequalities, variables ≥ 0)
```

This is a modeling transformation, not a solution algorithm. It preserves feasibility and, after the sign flip for minimization, preserves the optimal value.

---

## 6. Geometry: convex feasible regions

**Definition.** A set `P ⊆ ℝⁿ` is convex if for every `x, y ∈ P` and every `λ ∈ [0,1]`,

```text
λ x + (1-λ)y ∈ P.
```

Equivalently, the entire line segment between any two points of `P` stays in `P`.

**Theorem.** The feasible region of every LP is convex.

**Proof.** Suppose `Ax ≤ b` and `Ay ≤ b`. For `λ ∈ [0,1]`,

```text
A(λ x + (1-λ)y) = λ Ax + (1-λ)Ay ≤ λ b + (1-λ)b = b.
```

The inequality direction is valid because both weights are nonnegative. If `x ≥ 0` and `y ≥ 0`, the same weights preserve `x ≥ 0`. An equality `aᵀ x = d` is preserved by the same calculation, with equality throughout.

### Picture of a convex combination

```text
y •
  |\
  | \
  |  •  λx + (1-λ)y
  |   \
  |    \
  •-----• x
```

If `P` is convex, every such interior segment point is feasible. If a set has a dent, some segment between feasible points leaves the set, so the set is not convex and cannot be an LP feasible region.

**Nonconvex example.** The set `{(0,0), (1,0)}` is not convex, because the midpoint `(1/2, 0)` is missing. That is why adding `xᵢ ∈ {0,1}` takes us outside ordinary linear programming.

---

## 7. A two-dimensional picture

Consider

```text
maximize 2x₁ + 3x₂
subject to x₁ + x₂ ≤ 5,
x₁ ≥ 1,
x₂ ≥ 0.
```

The feasible region is a right triangle with vertices `(1,0)`, `(5,0)`, and `(1,4)`.

```text
x2
4 |  (1,4) • value 14
  |       /|
  |      / |
  |     /  |  objective level 2x1 + 3x2 = 14
  |    /   |  touches P only at (1,4)
  |   / P /
  |  /   /
  | /   /
0 |•---•------------ x1
  1   5
 (1,0) (5,0)

c = (2,3) points up and to the right.
Increasing q moves the line 2x1 + 3x2 = q in that direction.
```

Level curves of the objective are the lines `2x₁ + 3x₂ = q`. Increasing `q` translates those lines in the direction `c = (2,3)`. The best line that still touches `P` touches it at the vertex `(1,4)`, where

```text
2· 1 + 3· 4 = 14.
```

The other vertices are worse: `(1,0)` has value `2`, and `(5,0)` has value `10`.

### An optimum need not be unique

If the objective were `x₁ + x₂`, every point on the edge from `(1,4)` to `(5,0)` has value `5`. The optimal set is that entire edge, not a single point. An LP can have many optimal solutions. The vertex theorem only says that, when a finite optimum exists in canonical form, at least one optimal solution is a vertex.

### Tight constraints at each vertex

At a point in `ℝ²`, two linearly independent tight constraints certify a vertex.

| Vertex | Tight constraints | Normals |
|---|---|---|
| `(1,0)` | `x₁ = 1`, written `-x₁ ≤ -1`; and `x₂ = 0`, written `-x₂ ≤ 0` | `(-1,0)` and `(0,-1)` |
| `(5,0)` | `x₁ + x₂ = 5`; and `x₂ = 0` | `(1,1)` and `(0,-1)` |
| `(1,4)` | `x₁ + x₂ = 5`; and `x₁ = 1` | `(1,1)` and `(-1,0)` |

Each pair is linearly independent, so each point is a vertex. The edge point `(3,2)` has only `x₁ + x₂ = 5` tight. One normal cannot span `ℝ²`, so `(3,2)` is not a vertex, even though it is optimal for the objective `x₁ + x₂`.

---

## 8. Vertices and the three outcomes

An LP has exactly one of three outcomes.

1. **Infeasible.** No point satisfies every constraint. Example: `x ≥ 2` and `x ≤ 1`.
2. **Unbounded in objective.** Feasible points make the objective arbitrarily good. Example: maximize `x` subject to `x ≥ 0`.
3. **Feasible with a finite optimum.** Then the optimum is attained.

An unbounded region does not imply an unbounded objective. Maximize `-x` subject to `x ≥ 0`: the region is the unbounded ray `[0,∞)`, but the best value is `0`, attained at `x = 0`.

```text
Infeasible                 Unbounded objective         Finite optimum
x ≤ 1 and x ≥ 2            max x, x ≥ 0                max −x, x ≥ 0

1    2                     0 ----------------► x       0 •------------► x
•----•----•               value → +∞                  value = 0 at x = 0
empty overlap
```

### Tight constraints and vertices

An inequality `aᵀ x ≤ d` is **tight** at `x` if `aᵀ x = d`. A feasible point of a polyhedron in `ℝⁿ` is a **vertex**, also called a **basic feasible solution**, if the normals of its tight constraints span `ℝⁿ`. Equivalently, some `n` of those tight constraints are linearly independent.

Nonnegativity counts. Write `xᵢ ≥ 0` as `-xᵢ ≤ 0`. A vertex may have more than `n` tight constraints; what matters is that some `n` of their normals are independent.

### Basic optimal solutions

**Theorem.** If an LP in canonical form `Ax ≤ b`, `x ≥ 0` is feasible and has finite optimal value, then it has an optimal solution at a vertex.

**Geometric intuition.** Suppose fewer than `n` independent constraints are tight at a feasible point `x`. Their normals do not span `ℝⁿ`, so there is a nonzero direction `d` orthogonal to all of them. For a sufficiently small step `ε > 0`, both `x+ε d` and `x-ε d` remain feasible.

If `x` is optimal, neither direction can improve the objective, so `cᵀ d = 0`: the objective is constant along `d`. Move in one direction until another independent constraint becomes tight. Repeat. Each move adds an independent tight constraint, so the process stops after at most `n` additions. Nonnegativity is what prevents a whole line from staying feasible forever in both directions. That is why the canonical form matters.

### A useful caveat

Without the canonical-form assumption, a polyhedron can have no vertices. The half-plane

```text
{(u,v) : v ≥ 0}
```

has none: at every point, at most one constraint can be tight, and one normal cannot span `ℝ²`. Still, maximizing `-v` has finite optimum `0`, attained on the entire boundary line `v = 0`. Converting to canonical form restores the vertex statement in the new variables, because the substitution for an unrestricted variable adds nonnegativity constraints.

### Smoothie point `(3,3,0)`

In `ℝ³`, three independent tight constraints are required. At `x = (3,3,0)`:

- oranges: `x₁ + x₃ = 3`, normal `(1,0,1)`;
- strawberries: `2x₂ + x₃ = 6`, normal `(0,2,1)`;
- nonnegativity: `x₃ = 0`, normal `(0,0,-1)`.

Bananas are not tight: `2· 3 + 3 + 0 = 9 < 10`.

The three normals form

```text
[[1, 0,  1],
 [0, 2,  1],
 [0, 0, -1]]
```

This matrix is upper triangular after swapping nothing essential in the first column; its determinant is `1· 2· (-1) = -2 ≠ 0`. The three normals are linearly independent, so `(3,3,0)` is a vertex. That does not by itself prove optimality. Vertex status and optimal status are separate claims.

### Pseudocode: test whether a feasible point is a vertex

```text
function IS_VERTEX(A, b, x):
    # A, b include every inequality, including x ≥ 0 written as −x ≤ 0
    require A x ≤ b and x has dimension n

    rows ← empty list
    for each inequality row (a, d) in (A, b):
        if aᵀx = d:          # numerically, |aᵀx − d| below a tolerance
            append a to rows

    return RANK(rows) = n
```

Rank, not the number of tight rows, is the test. Five tight constraints can still fail to span `ℝ⁴` if they are dependent. Two tight constraints can never certify a vertex in `ℝ³`.

---

## 9. Why LPs are algorithmically useful

**Theorem, used as a black box.** For rational input, an LP can be solved in time polynomial in its total binary encoding length. The algorithm reports infeasibility or unboundedness, or returns an exact rational optimum when the optimal value is finite.

The ellipsoid method and interior-point methods are the classical sources of this polynomial-time guarantee. This course uses LP solving as a tool and does not develop those algorithms.

### Why a basic solution has polynomial bit length

At a vertex, select `n` independent tight constraints, including nonnegativity constraints if needed. They give a nonsingular system

```text
Bx = d.
```

By Cramer’s rule,

```text
xᵢ = (det(Bᵢ) / det(B)),
```

where `Bᵢ` is `B` with column `i` replaced by `d`. After clearing rational denominators, one is taking determinants of integer matrices. Each determinant is a sum of `n!` products of `n` entries, so its encoding length is polynomial in the encoding length of those entries. Therefore a basic optimal solution has polynomial bit length.

This is not an enumeration algorithm. There may be exponentially many choices of `n` tight constraints. Existence of a short answer does not mean that testing every candidate vertex is efficient.

### Encoding length versus magnitude

Polynomial in the input bit length is not the same as polynomial in the numerical magnitudes. If a capacity is `B = 2ʳ`, writing `B` uses `r+1` bits, while a dynamic program taking `O(nB)` time is pseudo-polynomial. The LP theorem is a guarantee in the encoding length. It does not say that the running time depends only on the number of variables and constraints, ignoring the size of the coefficients.

### Box constraints and fractional coordinates

**Exercise.** An LP in `n` variables has box constraints `0 ≤ xᵢ ≤ 1` and only `k` other linear inequalities. Show that any vertex has at most `k` coordinates strictly between `0` and `1`.

**Proof.** Let `x` be a vertex, and let `S` be the set of coordinates with `0 < xᵢ < 1`. For each `i ∉ S`, either `xᵢ = 0` or `xᵢ = 1`, so a box constraint is tight. Those `| [n]∖ S |` tight box normals are distinct coordinate normals, hence linearly independent.

The only other inequalities available are the `k` non-box inequalities. At most `k` of them can be tight. A vertex needs `n` linearly independent tight normals in total. Therefore

```text
n ≤ (n - |S|) + k,
```

which rearranges to `|S| ≤ k`.

This is the geometric reason a vertex solution is mostly pinned to bounds when there are few extra constraints. It is also the starting point for later rounding arguments: few fractional coordinates are easier to control than an arbitrary fractional vector.

---

## 10. Proving a proposed solution is optimal

Return to the smoothie LP. The feasible solution `x = (3,3,0)` has value `27`. To prove optimality, every feasible solution needs an upper bound of `27`.

Take five copies of the orange constraint and two copies of the strawberry constraint:

```text
5(x₁ + x₃) + 2(2x₂ + x₃) ≤ 5· 3 + 2· 6 = 27.
```

The left side expands to `5x₁ + 4x₂ + 7x₃`. Since `x₃ ≥ 0`,

```text
5x₁ + 4x₂ + 6x₃ ≤ 5x₁ + 4x₂ + 7x₃ ≤ 27.
```

Equivalently, include one copy of `-x₃ ≤ 0`. Then the weighted left side is exactly the objective:

```text
5(x₁ + x₃) + 0(2x₁ + x₂ + x₃) + 2(2x₂ + x₃) + 1(-x₃) = 5x₁ + 4x₂ + 6x₃.
```

```text
feasible x = (3,3,0)                weighted constraints
value 27                            5·oranges + 2·strawberries
        \                          /
         \                        /
          \                      /
           -------- 27 ----------
         lower bound      upper bound

If the two bounds meet, the feasible solution is optimal.
```

The nonnegative weights `(5,0,2)` on the three resource constraints are a certificate. They were found by inspection here. The systematic search for the best such upper bound is itself a linear program: the **dual**. That is the next lecture’s question.

### A smaller certificate, fully checked

Maximize `x₁ + x₂` subject to `x₁ ≤ 2`, `x₂ ≤ 3`, and `x ≥ 0`. The point `(2,3)` is feasible and has value `5`. One copy of each upper bound gives

```text
x₁ + x₂ ≤ 2 + 3 = 5
```

for every feasible `x`. The lower bound matches the upper bound, so `OPT = 5`.

### Pseudocode: check a nonnegative weighted certificate

```text
function CHECK_UPPER_BOUND(A, b, c, y):
    # maximization form: max cᵀx subject to A x ≤ b, x ≥ 0
    # y is a proposed weight vector, one weight per row of A
    require y ≥ 0
    require Aᵀ y ≥ c          # every objective coefficient is covered
    return bᵀ y               # a valid upper bound on OPT

# If x is feasible and cᵀx = bᵀy, then x is optimal and y is an optimal certificate.
```

The condition `Aᵀ y ≥ c` is exactly the statement that a nonnegative combination of the rows dominates the objective. The lecture’s extra weight on `-x₃ ≤ 0` is the same idea when nonnegativity is included among the rows.

---

## 11. Worked examples beyond the note

### Example A: three outcomes in one family

For each right-hand side, classify

```text
maximize x₁ subject to x₁ ≤ t, x₁ ≥ 0.
```

- If `t < 0`, the program is infeasible.
- If `t ≥ 0`, it is feasible and the optimum is `t`, attained at `x₁ = t`.
- Dropping the constraint `x₁ ≤ t` makes the objective unbounded.

Same variables, three different outcomes. Feasibility of the region and boundedness of the objective have to be checked separately.

### Example B: objective constant on an edge

Maximize `x₁ + x₂` subject to `x₁ + x₂ ≤ 1` and `x ≥ 0`. Every point on the segment from `(1,0)` to `(0,1)` is optimal with value `1`. Both endpoints are vertices. The midpoint is optimal but not a vertex. The theorem does not say every optimal solution is a vertex. It says some optimal solution is a vertex.

### Example C: converting a diet-style minimum

Minimize `3a + 2b` subject to `a + b ≥ 4`, `a ≥ 0`, and `b` unrestricted.

Canonical form:

```text
maximize -3a - 2b⁺ + 2b⁻
subject to -a - b⁺ + b⁻ ≤ -4,
a, b⁺, b⁻ ≥ 0.
```

If this program has optimal value `-q`, the original minimum is `q`.

### Example D: a flow constraint in numbers

Take vertices `s, v, t` and edges `(s,v)`, `(v,t)`, `(v,s)`, with capacities `4, 3, 1`. The flow LP is

```text
maximize fₛᵥ - fᵥₛ
subject to fₛᵥ = fᵥₜ + fᵥₛ  (conservation at v),
0 ≤ fₛᵥ ≤ 4, 0 ≤ fᵥₜ ≤ 3, 0 ≤ fᵥₛ ≤ 1.
```

One feasible flow is `fₛᵥ = 3`, `fᵥₜ = 3`, `fᵥₛ = 0`, with value `3`. The LP also allows `fₛᵥ = 2.5`, `fᵥₜ = 2.5`, `fᵥₛ = 0`. Integer capacities do not forbid fractional feasible flows. They guarantee that some optimal flow is integral. Here an integral optimum is `3`, limited by the capacity of `(v,t)`.

---

## 12. Takeaways

- An LP has a linear objective and linear non-strict constraints. Products, squares, strict inequalities, and integrality are not part of a plain LP.
- Canonical form is `max cᵀ x` subject to `Ax ≤ b`, `x ≥ 0`. Minimization, lower bounds, equalities, and unrestricted variables convert to it with only polynomial growth.
- A feasible point gives a lower bound for a maximization problem. It does not certify optimality until a matching upper bound exists.
- Every LP feasible region is convex. A nonconvex constraint, including a discrete restriction, leaves ordinary LP.
- An LP is infeasible, unbounded in objective, or feasible with an attained finite optimum. An unbounded region can still have a bounded objective.
- In canonical form, a finite optimum is attained at a vertex: a feasible point with `n` linearly independent tight constraints.
- LP is polynomial-time solvable in the binary encoding length. That is a black box here. Short basic solutions do not justify enumerating all vertices.
- Nonnegative weights on constraints can certify optimality. Finding the best weights is the dual.

---

## 13. Quiz

Answers are in the next section. Try the questions before looking.

### Conceptual

1. Which of the following is a linear program?
   - (a) maximize `x₁ x₂` subject to `x₁ + x₂ ≤ 1`, `x ≥ 0`
   - (b) maximize `x₁ + x₂` subject to `x₁ < 1`, `x ≥ 0`
   - (c) maximize `3x₁ - x₂` subject to `x₁ + 2x₂ = 4`, `x₁, x₂ ≥ 0`
   - (d) maximize `x₁` subject to `x₁ ∈ {0,1}`

2. True or false: if `(3,3,0)` is feasible for the smoothie LP and has value `27`, then `OPT = 27`.

3. True or false: every LP with an unbounded feasible region has an unbounded objective.

4. True or false: every optimal solution of a canonical-form LP is a vertex.

5. Why is `x < 1` not allowed as an LP constraint when maximizing `x`?

### Modeling

6. Rewrite `a + 2b ≥ 7` as a `≤` constraint.

7. Rewrite `3u - v = 1` as two `≤` constraints.

8. Variable `z` is unrestricted. Which substitution puts it into canonical form?

9. In the maximum-flow LP, what does the constraint at a vertex `v ∉ {s,t}` say?

10. Why does an LP formulation of flow not replace Ford–Fulkerson-style algorithms?

### Geometry

11. For the triangle `max 2x₁ + 3x₂` subject to `x₁ + x₂ ≤ 5`, `x₁ ≥ 1`, `x₂ ≥ 0`, which vertex is optimal?

12. Which two constraints are tight at `(5,0)`?

13. Give a feasible point of that triangle that is not a vertex.

14. At the smoothie point `(3,3,0)`, name three independent tight constraints.

15. Why does the half-plane `v ≥ 0` have no vertex?

### Certificates and algorithms

16. In the smoothie certificate, why is `5x₁ + 4x₂ + 6x₃ ≤ 5x₁ + 4x₂ + 7x₃`?

17. What upper bound do the weights `(5,0,2)` prove?

18. A proposed weight vector `y` satisfies `y ≥ 0` and `Aᵀ y ≥ c`. What quantity is a valid upper bound?

19. Cramer’s rule writes a basic solution using ratios of what?

20. Why is “there are finitely many vertices, and each has polynomial bit length” not a polynomial-time algorithm?

---

## 14. Quiz answers

1. **(c).** Equality constraints are allowed and can be split into two inequalities. (a) has a product objective, (b) is strict, and (d) is integral.
2. **False.** Feasibility proves only `OPT ≥ 27`. The matching upper bound is a separate argument.
3. **False.** Maximize `-x` subject to `x ≥ 0`.
4. **False.** Some optimal solution is a vertex. An entire edge may be optimal, and its interior points are not vertices.
5. The supremum is `1`, but no feasible point attains it. LP theory uses non-strict inequalities so a finite optimum is attained.
6. `-a - 2b ≤ -7`.
7. `3u - v ≤ 1` and `-3u + v ≤ -1`.
8. `z = z⁺ - z⁻` with `z⁺, z⁻ ≥ 0`.
9. Flow in equals flow out: `∑_((u,v)∈ E) fᵤᵥ = ∑_((v,w)∈ E) f_vw`.
10. The formulation places flow in a general framework. Specialized algorithms still exploit graph structure, and an arbitrary LP need not have the integral optimum that integer-capacity flow has.
11. `(1,4)`, with value `14`.
12. `x₁ + x₂ = 5` and `x₂ = 0`.
13. Any open-edge or interior point works. For example, `(3,0)` has only `x₂ = 0` tight, and `(3,1)` has no tight constraint.
14. `x₁ + x₃ = 3`, `2x₂ + x₃ = 6`, and `x₃ = 0`. Their normals `(1,0,1)`, `(0,2,1)`, and `(0,0,-1)` are independent.
15. At most one constraint is ever tight, so the tight normals cannot span `ℝ²`.
16. Because `x₃ ≥ 0`, so `6x₃ ≤ 7x₃`.
17. `27`. Together with the feasible value `27`, this proves optimality.
18. `bᵀ y`.
19. Determinants: `xᵢ = det(Bᵢ)/det(B)` for a nonsingular tight system `Bx = d`.
20. There can be exponentially many candidate bases. A short solution is not the same as a short search over all solutions.

---

## 15. Exam-style questions

These are written in the style of a graduate algorithms exam: short proofs, modeling, and counterexamples. Suggested times assume a closed-book setting.

### Question 1 (15 minutes)

Consider

```text
maximize x₁ + 2x₂
subject to x₁ + x₂ ≤ 4,
x₂ ≤ 3,
x₁, x₂ ≥ 0.
```

(a) Draw or describe the feasible region and list its vertices.
(b) Evaluate the objective at each vertex and state an optimal solution.
(c) Give nonnegative weights on the two resource inequalities that prove your solution is optimal. If you need a nonnegativity constraint, include it and say so.

**Solution.**

(a) The region is a convex polygon with vertices `(0,0)`, `(4,0)`, `(1,3)`, and `(0,3)`. Check the intersections: `x₂ = 0` with `x₁ = 0`; `x₂ = 0` with `x₁ + x₂ = 4`; `x₂ = 3` with `x₁ + x₂ = 4`; and `x₂ = 3` with `x₁ = 0`.

(b) Values: `0`, `4`, `7`, and `6`. The unique vertex optimum is `(1,3)`, with value `7`.

(c) One copy of `x₁ + x₂ ≤ 4` and one copy of `x₂ ≤ 3` give `x₁ + 2x₂ ≤ 7`. The weights are `(1,1)`, and no nonnegativity weight is needed because both objective coefficients are covered exactly.

### Question 2 (15 minutes)

Convert the following program to canonical form. State how to recover the original optimal value.

```text
minimize 4p - q
subject to p + q ≥ 2,
p - q = 1,
p ≥ 0,
```

with `q` unrestricted.

**Solution.** Set `q = q⁺ - q⁻`, with `q⁺, q⁻ ≥ 0`. Maximize `-4p + q⁺ - q⁻`, and negate that optimal value to recover the minimum. The constraints become

```text
-p - q⁺ + q⁻ ≤ -2,
p - q⁺ + q⁻ ≤ 1,
-p + q⁺ - q⁻ ≤ -1,
p, q⁺, q⁻ ≥ 0.
```

### Question 3 (20 minutes)

Prove that the feasible region of `max cᵀ x` subject to `Ax ≤ b` and `x ≥ 0` is convex. Then give an example of a feasible set defined by one forbidden constraint type from the lecture that is not convex.

**Solution.** If `x, y` are feasible and `λ ∈ [0,1]`, then

```text
A(λ x + (1-λ)y) = λ Ax + (1-λ)Ay ≤ b,
```

and `λ x + (1-λ)y ≥ 0`. Thus the segment stays feasible.

For a nonconvex example, take `x₁ ∈ {0,1}` in `ℝ¹`. Both endpoints are feasible, but the midpoint `1/2` is not. A product constraint can also make a nonconvex set; the integrality example matches the lecture directly.

### Question 4 (20 minutes)

(a) Give one LP showing each of the three outcomes: infeasible, unbounded objective, and finite attained optimum.
(b) Give an LP whose feasible region is unbounded but whose objective is bounded, and identify the optimum.
(c) Explain why the half-plane `{(u,v): v ≥ 0}` does not contradict the vertex theorem in the lecture.

**Solution.**

(a) Infeasible: `x ≥ 2`, `x ≤ 1`. Unbounded: maximize `x` subject to `x ≥ 0`. Finite: maximize `-x` subject to `x ≤ 1`, `x ≥ 0`, with optimum `0` at `x = 0`.
(b) Maximize `-x` subject to `x ≥ 0`. The region is unbounded and the optimum is `0` at `x = 0`.
(c) The vertex theorem in the lecture assumes canonical form, including nonnegativity of every variable. The half-plane has an unrestricted variable and no vertex, even though `max(-v)` has finite optimum `0`. Substituting `u = u⁺ - u⁻` restores nonnegativity and the vertex statement in the new variables.

### Question 5 (20 minutes)

Let `x` be feasible for a polyhedron in `ℝⁿ`, and suppose the tight constraints at `x` have rank `r < n`.

(a) Show there is a nonzero direction `d` such that, for all sufficiently small `ε > 0`, both `x+ε d` and `x-ε d` remain feasible. You may assume the only constraints are the inequalities defining the polyhedron, and that a constraint that is slack stays satisfied under a small perturbation.
(b) Suppose `x` is optimal for `max cᵀ x`. Show `cᵀ d = 0`.
(c) Explain, in words, how repeating this movement proves that a canonical-form LP with finite optimum has a vertex optimum.

**Solution.**

(a) The tight normals span an `r`-dimensional subspace, with `r < n`, so their common orthogonal complement contains a nonzero `d`. Moving along `d` does not change any tight left-hand side. Slack inequalities remain satisfied for small enough `ε`, in both directions.
(b) If `cᵀ d > 0`, then `x+ε d` is feasible and better for small `ε`. If `cᵀ d < 0`, then `x-ε d` is better. Optimality forces `cᵀ d = 0`.
(c) The objective is constant along `d`, so move until a new independent constraint becomes tight. Each step increases the rank of the tight normals. Canonical nonnegativity prevents the line from remaining feasible in both directions forever, so the process reaches a feasible point with `n` independent tight constraints and the same objective value.

### Question 6 (15 minutes)

An LP in `n` variables has constraints `0 ≤ xᵢ ≤ 1` for every `i`, plus `k` additional linear inequalities. Prove that every vertex has at most `k` coordinates strictly between `0` and `1`.

**Solution.** At a vertex `x`, every coordinate outside `(0,1)` has a tight box constraint. Those tight box normals are distinct unit normals, so they are independent. At most `k` additional normals are available. Since some `n` tight normals are independent,

```text
n ≤ (n - \#{i : 0 < xᵢ < 1}) + k.
```

Hence the number of strictly fractional coordinates is at most `k`.

### Question 7 (15 minutes)

The smoothie LP is

```text
maximize 5x₁ + 4x₂ + 6x₃
subject to x₁ + x₃ ≤ 3,
2x₁ + x₂ + x₃ ≤ 10,
2x₂ + x₃ ≤ 6,
x ≥ 0.
```

(a) Verify that `(3,3,0)` is a vertex by exhibiting three independent tight constraints.
(b) Prove it is optimal.
(c) What changes, conceptually, if liters must be integers? Do not solve the integer program.

**Solution.**

(a) Tight constraints: `x₁ + x₃ = 3`, `2x₂ + x₃ = 6`, and `x₃ = 0`. The normals `(1,0,1)`, `(0,2,1)`, and `(0,0,-1)` have nonzero determinant `-2`.
(b) Five times oranges plus two times strawberries gives `5x₁ + 4x₂ + 7x₃ ≤ 27`. Nonnegativity of `x₃` drops the coefficient `7` to `6`, so every feasible objective is at most `27`. The feasible value equals this upper bound.
(c) The problem becomes an integer linear program. The continuous optimum remains an upper bound, but an arbitrary LP need not have an integral optimum, and the integer feasible set is not convex.

### Question 8 (15 minutes)

Write the maximum-flow LP for a directed graph `G = (V,E)` with source `s`, sink `t`, and capacities `cₑ`. Then answer:

(a) How many variables are there?
(b) Why may a feasible solution be fractional even when every `cₑ` is an integer?
(c) What special fact from Lecture 8 is not true for a general LP?

**Solution.** Maximize `∑_((s,v)∈ E) fₛᵥ - ∑_((v,s)∈ E) fᵥₛ`, subject to conservation at every `v ∉ {s,t}` and `0 ≤ fₑ ≤ cₑ`.

(a) `m = |E|` variables.
(b) The constraints are linear equalities and inequalities over the reals. Integer right-hand sides do not force every feasible point to be integral; they only create the special integral-optimum property for this particular polyhedron.
(c) Integer capacities imply some optimal flow is integral. A general LP can have a unique fractional optimum.

### Question 9 (10 minutes)

Explain the difference between a polynomial-time algorithm and a pseudo-polynomial algorithm, using capacity `B = 2ʳ` and the lecture’s comparison between LP and knapsack DP. Then explain why polynomial bit length of a basic solution does not yield an enumeration algorithm.

**Solution.** The integer `B = 2ʳ` has encoding length `r+1`, but magnitude `2ʳ`. An `O(nB)` knapsack DP is polynomial in the magnitude and only pseudo-polynomial in the input length. The LP black box is polynomial in the total binary encoding length, not merely in `m` and `n`, and not in the magnitudes.

A vertex solves some nonsingular system `Bx = d`, so Cramer’s rule gives polynomial bit length after clearing denominators. The number of possible `n`-row bases can still be exponential, so listing them is not a polynomial-time algorithm.

---

## 16. Textbook references

The lecture’s required course text, from the CS 6515 syllabus, is Dasgupta, Papadimitriou, and Vazirani. The linear-programming geometry and certificates are developed more fully in the specialized books below. Chapter pointers are to standard editions; page numbers vary by printing.

| Reference | What to read for this lecture |
|---|---|
| Dasgupta, Papadimitriou, and Vazirani, *Algorithms*, McGraw-Hill, 2008. Chapter 7, “Linear programming and reductions.” | The course textbook. LP as an algorithmic tool, reductions to LP, and maximum flow as a network problem that fits the optimization viewpoint. |
| Matoušek and Gärtner, *Understanding and Using Linear Programming*, Springer, 2007. Chapters 1–4 and 6. | The closest match to this lecture: what an LP is, equivalent forms, convexity and vertices, basic feasible solutions, and why a short certificate matters. Written for computer scientists. |
| Vanderbei, *Linear Programming: Foundations and Extensions*, 5th ed., Springer, 2020. Chapters 1–2. | Inequality form, geometry of the feasible region, and the dictionary between models and standard form. Later chapters cover simplex and interior-point methods, which this lecture treats as a black box. |
| Chvátal, *Linear Programming*, W. H. Freeman, 1983. Chapters 1–2 and 5. | Classical treatment of feasible regions, vertices, and the theorem that a finite optimum is attained at a basic feasible solution. |
| Schrijver, *Theory of Linear and Integer Programming*, Wiley, 1986. Chapters 7–8 and 13–15. | The precise polynomial-time and bit-length theory: Cramer’s rule, encoding length, the ellipsoid method, and the distinction between LP and integer programming. Use this when the quiz questions on bit length need a reference proof. |
| Bertsimas and Tsitsiklis, *Introduction to Linear Optimization*, Athena Scientific, 1997. Chapters 1–2. | Polyhedra, extreme points, and equivalent characterizations of vertices. Good backup for the tight-constraint definition. |
| Kleinberg and Tardos, *Algorithm Design*, Pearson, 2006. Chapter 11, and the flow chapter. | Flow as an optimization problem, and a computer-science view of using LP without deriving interior-point methods. |
| Ahuja, Magnanti, and Orlin, *Network Flows*, Prentice Hall, 1993. Chapter 1 and the flow-formulation sections. | The edge-variable formulation used in the lecture, including conservation and capacity constraints. |

For the dual, which the lecture only previews, start with Matoušek and Gärtner, Chapter 6, or Vanderbei’s duality chapter. The lecture stops once the smoothie weights `(5,0,2)` show that the search for the best upper bound is itself an LP.

---

## 17. One-page formula sheet

```text
Canonical form: max cᵀ x s.t. Ax ≤ b, x ≥ 0.
Feasible region: P = {x : Ax ≤ b, x ≥ 0}.
Convexity: x,y ∈ P, λ ∈ [0,1] ⇒ λ x + (1-λ)y ∈ P.
Vertex in ℝⁿ: feasible, and n independent tight normals.
Tight: aᵀ x = d for a constraint aᵀ x ≤ d.
Basic solution: Bx = d, xᵢ = det(Bᵢ)/det(B).
Certificate: y ≥ 0, Aᵀ y ≥ c ⇒ cᵀ x ≤ bᵀ y.
Optimality: x feasible, y a certificate, and cᵀ x = bᵀ y.
```

Conversions: flip the sign to turn minimization into maximization; multiply a `≥` constraint by `-1`; split an equality into two inequalities; replace an unrestricted variable by a difference of two nonnegative variables.
