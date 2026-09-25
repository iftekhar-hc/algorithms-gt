# CS 6515 Lecture 9 Study Guide

## Linear Programming: Models and Geometry

**Course:** CS 6515, Graduate Algorithms
**Instructors:** Sahil Singla and Gerandy Brito
**Term:** Fall 2026
**Source note:** Lecture 9, unmarked notes

This guide explains the lecture, works the in-class exercises, and adds examples, ASCII visualizations, pseudocode, quizzes, and exam-style questions. Math is written in LaTeX delimiters so a Markdown viewer with math support can render it.

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

\[
\begin{aligned}
\text{maximize} \quad & c^\top x \\
\text{subject to} \quad & Ax \le b, \\
& x \ge 0,
\end{aligned}
\]

where \(A \in \mathbb{R}^{m \times n}\), \(b \in \mathbb{R}^{m}\), and \(c \in \mathbb{R}^{n}\). Inequalities are coordinatewise. Row \(j\) says

\[
\sum_{i=1}^{n} A_{ji} x_i \le b_j.
\]

For computational claims, the input coefficients are rational.

**Feasible region.**

\[
P = \{ x \in \mathbb{R}^{n} : Ax \le b,\ x \ge 0 \}.
\]

A vector in \(P\) is feasible. An optimal solution is a feasible vector whose objective is best. For a maximization problem, that means the largest value of \(c^\top x\).

### What is not a plain LP

These are outside the definition used here:

- a product constraint such as \(x_1 x_2 \le 1\);
- a nonlinear objective such as \(x_1^2 + x_2^2\);
- an integrality requirement \(x_i \in \{0,1\}\);
- a strict inequality.

The last one is subtle. Maximizing \(x\) subject to \(x < 1\) has supremum \(1\), but no feasible point attains it. Non-strict inequalities are what let a finite LP attain its optimum.

### A tiny feasible example

\[
\begin{aligned}
\text{maximize} \quad & x_1 + 2x_2 \\
\text{subject to} \quad & x_1 + x_2 \le 3, \\
& x_1, x_2 \ge 0.
\end{aligned}
\]

The point \((1,1)\) is feasible and has value \(3\). The point \((0,3)\) is feasible and has value \(6\). The point \((2,2)\) is not feasible, because \(2+2 = 4 > 3\).

---

## 3. Running example: smoothies

There are \(3\) units of oranges, \(10\) of bananas, and \(6\) of strawberries. Smoothies may be made in fractional liters.

| Smoothie | Oranges | Bananas | Strawberries | Revenue per liter |
|---|---:|---:|---:|---:|
| 1 | 1 | 2 | 0 | $5 |
| 2 | 0 | 1 | 2 | $4 |
| 3 | 1 | 1 | 1 | $6 |

Let \(x_i\) be liters of smoothie \(i\).

\[
\begin{aligned}
\text{maximize} \quad & 5x_1 + 4x_2 + 6x_3 \\
\text{subject to} \quad & x_1 + x_3 \le 3 && \text{(oranges)}, \\
& 2x_1 + x_2 + x_3 \le 10 && \text{(bananas)}, \\
& 2x_2 + x_3 \le 6 && \text{(strawberries)}, \\
& x_1, x_2, x_3 \ge 0.
\end{aligned}
\tag{1}
\]

The vector \((3,3,0)\) uses \(3\) oranges, \(9\) bananas, and \(6\) strawberries. It is feasible and earns

\[
5\cdot 3 + 4\cdot 3 + 6\cdot 0 = 27.
\]

That proves \(\mathrm{OPT} \ge 27\). It does not yet prove optimality, because some other feasible vector might earn more. A lower bound and an upper bound are different objects.

### Exercise: write \(A\), \(b\), and \(c\)

Putting the three resource inequalities into \(Ax \le b\), and leaving nonnegativity separate as in the canonical form,

\[
A =
\begin{bmatrix}
1 & 0 & 1 \\
2 & 1 & 1 \\
0 & 2 & 1
\end{bmatrix},
\quad
b =
\begin{bmatrix}
3 \\ 10 \\ 6
\end{bmatrix},
\quad
c =
\begin{bmatrix}
5 \\ 4 \\ 6
\end{bmatrix}.
\]

If nonnegativity is folded into \(A\), append three rows \(-e_1^\top\), \(-e_2^\top\), and \(-e_3^\top\), with right-hand sides \(0\). Both writings describe the same set.

### What changes for whole-liter batches?

Replace \(x_i \ge 0\) by \(x_i \in \mathbb{Z}_{\ge 0}\). The resulting program is an **integer linear program**, not a plain LP. The feasible region is no longer a convex polyhedron in the continuous sense: the midpoint of two integer points need not be integer. Integral optima of arbitrary LPs are not guaranteed, so the continuous optimum is only a relaxation of the batch problem. Its value is an upper bound on the best whole-liter revenue, not necessarily an attainable revenue.

---

## 4. Maximum flow is an LP

For a directed network, give each edge \(e\) a variable \(f_e\). As in Lecture 8, the value is net flow out of the source:

\[
\begin{aligned}
\text{maximize} \quad
& \sum_{(s,v)\in E} f_{sv} - \sum_{(v,s)\in E} f_{vs} \\
\text{subject to} \quad
& \sum_{(u,v)\in E} f_{uv} = \sum_{(v,w)\in E} f_{vw}
&& (v \notin \{s,t\}), \\
& 0 \le f_e \le c_e
&& (e \in E).
\end{aligned}
\]

There are \(m = |E|\) variables and \(O(m+n)\) constraints. Writing flow as an LP does not replace the specialized flow algorithms. It places flow inside a broader optimization framework.

### Fractional versus integral flow

The LP allows fractional flows. Lecture 8 proved that integer capacities guarantee an integral optimal flow. That is special structure. An arbitrary LP need not have an integral optimum.

**Example.** Maximize \(x\) subject to \(x \le 1/2\) and \(x \ge 0\). The unique optimum is \(x = 1/2\), which is not an integer. Nothing in the definition of an LP forces vertices to have integer coordinates.

---

## 5. Equivalent forms

Any of the following can be rewritten in canonical form. The new formulation is only polynomially larger.

| Feature | Conversion |
|---|---|
| Minimize \(c^\top x\) | Maximize \(-c^\top x\), then negate the optimal value. |
| \(a^\top x \ge d\) | Write \(-a^\top x \le -d\). |
| \(a^\top x = d\) | Write both \(a^\top x \le d\) and \(-a^\top x \le -d\). |
| Unrestricted \(z\) | Substitute \(z = z^+ - z^-\), with \(z^+, z^- \ge 0\). |

Another useful form adds a slack variable for each inequality:

\[
Ax + s = b, \qquad x, s \ge 0,
\]

where \(s = b - Ax\). Each slack measures how far that inequality is from equality.

### Worked conversion

Convert

\[
\begin{aligned}
\text{minimize} \quad & 2u - v \\
\text{subject to} \quad & u - v = 3, \\
& u \ge 0,
\end{aligned}
\]

with \(v\) unrestricted, into canonical form.

1. Replace the objective by maximization of its negative: maximize \(-2u + v\). The original optimal value is the negative of this new value.
2. Split the unrestricted variable: \(v = v^+ - v^-\), with \(v^+, v^- \ge 0\).
3. Split the equality into two inequalities.

The canonical program in variables \((u, v^+, v^-)\) is

\[
\begin{aligned}
\text{maximize} \quad & -2u + v^+ - v^- \\
\text{subject to} \quad & u - v^+ + v^- \le 3, \\
& -u + v^+ - v^- \le -3, \\
& u, v^+, v^- \ge 0.
\end{aligned}
\]

A feasible point of the original problem, such as \((u,v) = (3,0)\), maps to \((u, v^+, v^-) = (3, 0, 0)\). A negative \(v\), such as \(v = -1\) with \(u = 2\), maps to \(v^+ = 0\) and \(v^- = 1\).

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

**Definition.** A set \(P \subseteq \mathbb{R}^{n}\) is convex if for every \(x, y \in P\) and every \(\lambda \in [0,1]\),

\[
\lambda x + (1-\lambda)y \in P.
\]

Equivalently, the entire line segment between any two points of \(P\) stays in \(P\).

**Theorem.** The feasible region of every LP is convex.

**Proof.** Suppose \(Ax \le b\) and \(Ay \le b\). For \(\lambda \in [0,1]\),

\[
A\bigl(\lambda x + (1-\lambda)y\bigr)
= \lambda Ax + (1-\lambda)Ay
\le \lambda b + (1-\lambda)b
= b.
\]

The inequality direction is valid because both weights are nonnegative. If \(x \ge 0\) and \(y \ge 0\), the same weights preserve \(x \ge 0\). An equality \(a^\top x = d\) is preserved by the same calculation, with equality throughout.

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

If \(P\) is convex, every such interior segment point is feasible. If a set has a dent, some segment between feasible points leaves the set, so the set is not convex and cannot be an LP feasible region.

**Nonconvex example.** The set \(\{(0,0), (1,0)\}\) is not convex, because the midpoint \((1/2, 0)\) is missing. That is why adding \(x_i \in \{0,1\}\) takes us outside ordinary linear programming.

---

## 7. A two-dimensional picture

Consider

\[
\begin{aligned}
\text{maximize} \quad & 2x_1 + 3x_2 \\
\text{subject to} \quad & x_1 + x_2 \le 5, \\
& x_1 \ge 1, \\
& x_2 \ge 0.
\end{aligned}
\]

The feasible region is a right triangle with vertices \((1,0)\), \((5,0)\), and \((1,4)\).

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

Level curves of the objective are the lines \(2x_1 + 3x_2 = q\). Increasing \(q\) translates those lines in the direction \(c = (2,3)\). The best line that still touches \(P\) touches it at the vertex \((1,4)\), where

\[
2\cdot 1 + 3\cdot 4 = 14.
\]

The other vertices are worse: \((1,0)\) has value \(2\), and \((5,0)\) has value \(10\).

### An optimum need not be unique

If the objective were \(x_1 + x_2\), every point on the edge from \((1,4)\) to \((5,0)\) has value \(5\). The optimal set is that entire edge, not a single point. An LP can have many optimal solutions. The vertex theorem only says that, when a finite optimum exists in canonical form, at least one optimal solution is a vertex.

### Tight constraints at each vertex

At a point in \(\mathbb{R}^{2}\), two linearly independent tight constraints certify a vertex.

| Vertex | Tight constraints | Normals |
|---|---|---|
| \((1,0)\) | \(x_1 = 1\), written \(-x_1 \le -1\); and \(x_2 = 0\), written \(-x_2 \le 0\) | \((-1,0)\) and \((0,-1)\) |
| \((5,0)\) | \(x_1 + x_2 = 5\); and \(x_2 = 0\) | \((1,1)\) and \((0,-1)\) |
| \((1,4)\) | \(x_1 + x_2 = 5\); and \(x_1 = 1\) | \((1,1)\) and \((-1,0)\) |

Each pair is linearly independent, so each point is a vertex. The edge point \((3,2)\) has only \(x_1 + x_2 = 5\) tight. One normal cannot span \(\mathbb{R}^{2}\), so \((3,2)\) is not a vertex, even though it is optimal for the objective \(x_1 + x_2\).

---

## 8. Vertices and the three outcomes

An LP has exactly one of three outcomes.

1. **Infeasible.** No point satisfies every constraint. Example: \(x \ge 2\) and \(x \le 1\).
2. **Unbounded in objective.** Feasible points make the objective arbitrarily good. Example: maximize \(x\) subject to \(x \ge 0\).
3. **Feasible with a finite optimum.** Then the optimum is attained.

An unbounded region does not imply an unbounded objective. Maximize \(-x\) subject to \(x \ge 0\): the region is the unbounded ray \([0,\infty)\), but the best value is \(0\), attained at \(x = 0\).

```text
Infeasible                 Unbounded objective         Finite optimum
x ≤ 1 and x ≥ 2            max x, x ≥ 0                max −x, x ≥ 0

1    2                     0 ----------------► x       0 •------------► x
•----•----•               value → +∞                  value = 0 at x = 0
empty overlap
```

### Tight constraints and vertices

An inequality \(a^\top x \le d\) is **tight** at \(x\) if \(a^\top x = d\). A feasible point of a polyhedron in \(\mathbb{R}^{n}\) is a **vertex**, also called a **basic feasible solution**, if the normals of its tight constraints span \(\mathbb{R}^{n}\). Equivalently, some \(n\) of those tight constraints are linearly independent.

Nonnegativity counts. Write \(x_i \ge 0\) as \(-x_i \le 0\). A vertex may have more than \(n\) tight constraints; what matters is that some \(n\) of their normals are independent.

### Basic optimal solutions

**Theorem.** If an LP in canonical form \(Ax \le b\), \(x \ge 0\) is feasible and has finite optimal value, then it has an optimal solution at a vertex.

**Geometric intuition.** Suppose fewer than \(n\) independent constraints are tight at a feasible point \(x\). Their normals do not span \(\mathbb{R}^{n}\), so there is a nonzero direction \(d\) orthogonal to all of them. For a sufficiently small step \(\varepsilon > 0\), both \(x+\varepsilon d\) and \(x-\varepsilon d\) remain feasible.

If \(x\) is optimal, neither direction can improve the objective, so \(c^\top d = 0\): the objective is constant along \(d\). Move in one direction until another independent constraint becomes tight. Repeat. Each move adds an independent tight constraint, so the process stops after at most \(n\) additions. Nonnegativity is what prevents a whole line from staying feasible forever in both directions. That is why the canonical form matters.

### A useful caveat

Without the canonical-form assumption, a polyhedron can have no vertices. The half-plane

\[
\{(u,v) : v \ge 0\}
\]

has none: at every point, at most one constraint can be tight, and one normal cannot span \(\mathbb{R}^{2}\). Still, maximizing \(-v\) has finite optimum \(0\), attained on the entire boundary line \(v = 0\). Converting to canonical form restores the vertex statement in the new variables, because the substitution for an unrestricted variable adds nonnegativity constraints.

### Smoothie point \((3,3,0)\)

In \(\mathbb{R}^{3}\), three independent tight constraints are required. At \(x = (3,3,0)\):

- oranges: \(x_1 + x_3 = 3\), normal \((1,0,1)\);
- strawberries: \(2x_2 + x_3 = 6\), normal \((0,2,1)\);
- nonnegativity: \(x_3 = 0\), normal \((0,0,-1)\).

Bananas are not tight: \(2\cdot 3 + 3 + 0 = 9 < 10\).

The three normals form

\[
\begin{bmatrix}
1 & 0 & 1 \\
0 & 2 & 1 \\
0 & 0 & -1
\end{bmatrix}.
\]

This matrix is upper triangular after swapping nothing essential in the first column; its determinant is \(1\cdot 2\cdot (-1) = -2 \ne 0\). The three normals are linearly independent, so \((3,3,0)\) is a vertex. That does not by itself prove optimality. Vertex status and optimal status are separate claims.

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

Rank, not the number of tight rows, is the test. Five tight constraints can still fail to span \(\mathbb{R}^{4}\) if they are dependent. Two tight constraints can never certify a vertex in \(\mathbb{R}^{3}\).

---

## 9. Why LPs are algorithmically useful

**Theorem, used as a black box.** For rational input, an LP can be solved in time polynomial in its total binary encoding length. The algorithm reports infeasibility or unboundedness, or returns an exact rational optimum when the optimal value is finite.

The ellipsoid method and interior-point methods are the classical sources of this polynomial-time guarantee. This course uses LP solving as a tool and does not develop those algorithms.

### Why a basic solution has polynomial bit length

At a vertex, select \(n\) independent tight constraints, including nonnegativity constraints if needed. They give a nonsingular system

\[
Bx = d.
\]

By Cramer’s rule,

\[
x_i = \frac{\det(B_i)}{\det(B)},
\]

where \(B_i\) is \(B\) with column \(i\) replaced by \(d\). After clearing rational denominators, one is taking determinants of integer matrices. Each determinant is a sum of \(n!\) products of \(n\) entries, so its encoding length is polynomial in the encoding length of those entries. Therefore a basic optimal solution has polynomial bit length.

This is not an enumeration algorithm. There may be exponentially many choices of \(n\) tight constraints. Existence of a short answer does not mean that testing every candidate vertex is efficient.

### Encoding length versus magnitude

Polynomial in the input bit length is not the same as polynomial in the numerical magnitudes. If a capacity is \(B = 2^{r}\), writing \(B\) uses \(r+1\) bits, while a dynamic program taking \(O(nB)\) time is pseudo-polynomial. The LP theorem is a guarantee in the encoding length. It does not say that the running time depends only on the number of variables and constraints, ignoring the size of the coefficients.

### Box constraints and fractional coordinates

**Exercise.** An LP in \(n\) variables has box constraints \(0 \le x_i \le 1\) and only \(k\) other linear inequalities. Show that any vertex has at most \(k\) coordinates strictly between \(0\) and \(1\).

**Proof.** Let \(x\) be a vertex, and let \(S\) be the set of coordinates with \(0 < x_i < 1\). For each \(i \notin S\), either \(x_i = 0\) or \(x_i = 1\), so a box constraint is tight. Those \(|\,[n]\setminus S\,|\) tight box normals are distinct coordinate normals, hence linearly independent.

The only other inequalities available are the \(k\) non-box inequalities. At most \(k\) of them can be tight. A vertex needs \(n\) linearly independent tight normals in total. Therefore

\[
n \le \bigl(n - |S|\bigr) + k,
\]

which rearranges to \(|S| \le k\).

This is the geometric reason a vertex solution is mostly pinned to bounds when there are few extra constraints. It is also the starting point for later rounding arguments: few fractional coordinates are easier to control than an arbitrary fractional vector.

---

## 10. Proving a proposed solution is optimal

Return to the smoothie LP. The feasible solution \(x = (3,3,0)\) has value \(27\). To prove optimality, every feasible solution needs an upper bound of \(27\).

Take five copies of the orange constraint and two copies of the strawberry constraint:

\[
5(x_1 + x_3) + 2(2x_2 + x_3) \le 5\cdot 3 + 2\cdot 6 = 27.
\]

The left side expands to \(5x_1 + 4x_2 + 7x_3\). Since \(x_3 \ge 0\),

\[
5x_1 + 4x_2 + 6x_3
\le 5x_1 + 4x_2 + 7x_3
\le 27.
\]

Equivalently, include one copy of \(-x_3 \le 0\). Then the weighted left side is exactly the objective:

\[
5(x_1 + x_3) + 0(2x_1 + x_2 + x_3) + 2(2x_2 + x_3) + 1(-x_3)
= 5x_1 + 4x_2 + 6x_3.
\]

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

The nonnegative weights \((5,0,2)\) on the three resource constraints are a certificate. They were found by inspection here. The systematic search for the best such upper bound is itself a linear program: the **dual**. That is the next lecture’s question.

### A smaller certificate, fully checked

Maximize \(x_1 + x_2\) subject to \(x_1 \le 2\), \(x_2 \le 3\), and \(x \ge 0\). The point \((2,3)\) is feasible and has value \(5\). One copy of each upper bound gives

\[
x_1 + x_2 \le 2 + 3 = 5
\]

for every feasible \(x\). The lower bound matches the upper bound, so \(\mathrm{OPT} = 5\).

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

The condition \(A^\top y \ge c\) is exactly the statement that a nonnegative combination of the rows dominates the objective. The lecture’s extra weight on \(-x_3 \le 0\) is the same idea when nonnegativity is included among the rows.

---

## 11. Worked examples beyond the note

### Example A: three outcomes in one family

For each right-hand side, classify

\[
\text{maximize } x_1 \quad \text{subject to } x_1 \le t,\ x_1 \ge 0.
\]

- If \(t < 0\), the program is infeasible.
- If \(t \ge 0\), it is feasible and the optimum is \(t\), attained at \(x_1 = t\).
- Dropping the constraint \(x_1 \le t\) makes the objective unbounded.

Same variables, three different outcomes. Feasibility of the region and boundedness of the objective have to be checked separately.

### Example B: objective constant on an edge

Maximize \(x_1 + x_2\) subject to \(x_1 + x_2 \le 1\) and \(x \ge 0\). Every point on the segment from \((1,0)\) to \((0,1)\) is optimal with value \(1\). Both endpoints are vertices. The midpoint is optimal but not a vertex. The theorem does not say every optimal solution is a vertex. It says some optimal solution is a vertex.

### Example C: converting a diet-style minimum

Minimize \(3a + 2b\) subject to \(a + b \ge 4\), \(a \ge 0\), and \(b\) unrestricted.

Canonical form:

\[
\begin{aligned}
\text{maximize} \quad & -3a - 2b^+ + 2b^- \\
\text{subject to} \quad & -a - b^+ + b^- \le -4, \\
& a, b^+, b^- \ge 0.
\end{aligned}
\]

If this program has optimal value \(-q\), the original minimum is \(q\).

### Example D: a flow constraint in numbers

Take vertices \(s, v, t\) and edges \((s,v)\), \((v,t)\), \((v,s)\), with capacities \(4, 3, 1\). The flow LP is

\[
\begin{aligned}
\text{maximize} \quad & f_{sv} - f_{vs} \\
\text{subject to} \quad & f_{sv} + f_{vs} = f_{vt} && \text{conservation at } v, \\
& 0 \le f_{sv} \le 4,\quad 0 \le f_{vt} \le 3,\quad 0 \le f_{vs} \le 1.
\end{aligned}
\]

One feasible flow is \(f_{sv} = 3\), \(f_{vt} = 3\), \(f_{vs} = 0\), with value \(3\). The LP also allows \(f_{sv} = 2.5\), \(f_{vt} = 2.5\), \(f_{vs} = 0\). Integer capacities do not forbid fractional feasible flows. They guarantee that some optimal flow is integral. Here an integral optimum is \(3\), limited by the capacity of \((v,t)\).

---

## 12. Takeaways

- An LP has a linear objective and linear non-strict constraints. Products, squares, strict inequalities, and integrality are not part of a plain LP.
- Canonical form is \(\max c^\top x\) subject to \(Ax \le b\), \(x \ge 0\). Minimization, lower bounds, equalities, and unrestricted variables convert to it with only polynomial growth.
- A feasible point gives a lower bound for a maximization problem. It does not certify optimality until a matching upper bound exists.
- Every LP feasible region is convex. A nonconvex constraint, including a discrete restriction, leaves ordinary LP.
- An LP is infeasible, unbounded in objective, or feasible with an attained finite optimum. An unbounded region can still have a bounded objective.
- In canonical form, a finite optimum is attained at a vertex: a feasible point with \(n\) linearly independent tight constraints.
- LP is polynomial-time solvable in the binary encoding length. That is a black box here. Short basic solutions do not justify enumerating all vertices.
- Nonnegative weights on constraints can certify optimality. Finding the best weights is the dual.

---

## 13. Quiz

Answers are in the next section. Try the questions before looking.

### Conceptual

1. Which of the following is a linear program?
   - (a) maximize \(x_1 x_2\) subject to \(x_1 + x_2 \le 1\), \(x \ge 0\)
   - (b) maximize \(x_1 + x_2\) subject to \(x_1 < 1\), \(x \ge 0\)
   - (c) maximize \(3x_1 - x_2\) subject to \(x_1 + 2x_2 = 4\), \(x_1, x_2 \ge 0\)
   - (d) maximize \(x_1\) subject to \(x_1 \in \{0,1\}\)

2. True or false: if \((3,3,0)\) is feasible for the smoothie LP and has value \(27\), then \(\mathrm{OPT} = 27\).

3. True or false: every LP with an unbounded feasible region has an unbounded objective.

4. True or false: every optimal solution of a canonical-form LP is a vertex.

5. Why is \(x < 1\) not allowed as an LP constraint when maximizing \(x\)?

### Modeling

6. Rewrite \(a + 2b \ge 7\) as a \(\le\) constraint.

7. Rewrite \(3u - v = 1\) as two \(\le\) constraints.

8. Variable \(z\) is unrestricted. Which substitution puts it into canonical form?

9. In the maximum-flow LP, what does the constraint at a vertex \(v \notin \{s,t\}\) say?

10. Why does an LP formulation of flow not replace Ford–Fulkerson-style algorithms?

### Geometry

11. For the triangle \(\max 2x_1 + 3x_2\) subject to \(x_1 + x_2 \le 5\), \(x_1 \ge 1\), \(x_2 \ge 0\), which vertex is optimal?

12. Which two constraints are tight at \((5,0)\)?

13. Give a feasible point of that triangle that is not a vertex.

14. At the smoothie point \((3,3,0)\), name three independent tight constraints.

15. Why does the half-plane \(v \ge 0\) have no vertex?

### Certificates and algorithms

16. In the smoothie certificate, why is \(5x_1 + 4x_2 + 6x_3 \le 5x_1 + 4x_2 + 7x_3\)?

17. What upper bound do the weights \((5,0,2)\) prove?

18. A proposed weight vector \(y\) satisfies \(y \ge 0\) and \(A^\top y \ge c\). What quantity is a valid upper bound?

19. Cramer’s rule writes a basic solution using ratios of what?

20. Why is “there are finitely many vertices, and each has polynomial bit length” not a polynomial-time algorithm?

---

## 14. Quiz answers

1. **(c).** Equality constraints are allowed and can be split into two inequalities. (a) has a product objective, (b) is strict, and (d) is integral.
2. **False.** Feasibility proves only \(\mathrm{OPT} \ge 27\). The matching upper bound is a separate argument.
3. **False.** Maximize \(-x\) subject to \(x \ge 0\).
4. **False.** Some optimal solution is a vertex. An entire edge may be optimal, and its interior points are not vertices.
5. The supremum is \(1\), but no feasible point attains it. LP theory uses non-strict inequalities so a finite optimum is attained.
6. \(-a - 2b \le -7\).
7. \(3u - v \le 1\) and \(-3u + v \le -1\).
8. \(z = z^+ - z^-\) with \(z^+, z^- \ge 0\).
9. Flow in equals flow out: \(\sum_{(u,v)\in E} f_{uv} = \sum_{(v,w)\in E} f_{vw}\).
10. The formulation places flow in a general framework. Specialized algorithms still exploit graph structure, and an arbitrary LP need not have the integral optimum that integer-capacity flow has.
11. \((1,4)\), with value \(14\).
12. \(x_1 + x_2 = 5\) and \(x_2 = 0\).
13. Any open-edge or interior point works. For example, \((3,0)\) has only \(x_2 = 0\) tight, and \((3,1)\) has no tight constraint.
14. \(x_1 + x_3 = 3\), \(2x_2 + x_3 = 6\), and \(x_3 = 0\). Their normals \((1,0,1)\), \((0,2,1)\), and \((0,0,-1)\) are independent.
15. At most one constraint is ever tight, so the tight normals cannot span \(\mathbb{R}^{2}\).
16. Because \(x_3 \ge 0\), so \(6x_3 \le 7x_3\).
17. \(27\). Together with the feasible value \(27\), this proves optimality.
18. \(b^\top y\).
19. Determinants: \(x_i = \det(B_i)/\det(B)\) for a nonsingular tight system \(Bx = d\).
20. There can be exponentially many candidate bases. A short solution is not the same as a short search over all solutions.

---

## 15. Exam-style questions

These are written in the style of a graduate algorithms exam: short proofs, modeling, and counterexamples. Suggested times assume a closed-book setting.

### Question 1 (15 minutes)

Consider

\[
\begin{aligned}
\text{maximize} \quad & x_1 + 2x_2 \\
\text{subject to} \quad & x_1 + x_2 \le 4, \\
& x_2 \le 3, \\
& x_1, x_2 \ge 0.
\end{aligned}
\]

(a) Draw or describe the feasible region and list its vertices.
(b) Evaluate the objective at each vertex and state an optimal solution.
(c) Give nonnegative weights on the two resource inequalities that prove your solution is optimal. If you need a nonnegativity constraint, include it and say so.

**Solution.**

(a) The region is a convex polygon with vertices \((0,0)\), \((4,0)\), \((1,3)\), and \((0,3)\). Check the intersections: \(x_2 = 0\) with \(x_1 = 0\); \(x_2 = 0\) with \(x_1 + x_2 = 4\); \(x_2 = 3\) with \(x_1 + x_2 = 4\); and \(x_2 = 3\) with \(x_1 = 0\).

(b) Values: \(0\), \(4\), \(7\), and \(6\). The unique vertex optimum is \((1,3)\), with value \(7\).

(c) One copy of \(x_1 + x_2 \le 4\) and one copy of \(x_2 \le 3\) give \(x_1 + 2x_2 \le 7\). The weights are \((1,1)\), and no nonnegativity weight is needed because both objective coefficients are covered exactly.

### Question 2 (15 minutes)

Convert the following program to canonical form. State how to recover the original optimal value.

\[
\begin{aligned}
\text{minimize} \quad & 4p - q \\
\text{subject to} \quad & p + q \ge 2, \\
& p - q = 1, \\
& p \ge 0,
\end{aligned}
\]

with \(q\) unrestricted.

**Solution.** Set \(q = q^+ - q^-\), with \(q^+, q^- \ge 0\). Maximize \(-4p + q^+ - q^-\), and negate that optimal value to recover the minimum. The constraints become

\[
\begin{aligned}
-p - q^+ + q^- &\le -2, \\
p - q^+ + q^- &\le 1, \\
-p + q^+ - q^- &\le -1, \\
p, q^+, q^- &\ge 0.
\end{aligned}
\]

### Question 3 (20 minutes)

Prove that the feasible region of \(\max c^\top x\) subject to \(Ax \le b\) and \(x \ge 0\) is convex. Then give an example of a feasible set defined by one forbidden constraint type from the lecture that is not convex.

**Solution.** If \(x, y\) are feasible and \(\lambda \in [0,1]\), then

\[
A(\lambda x + (1-\lambda)y) = \lambda Ax + (1-\lambda)Ay \le b,
\]

and \(\lambda x + (1-\lambda)y \ge 0\). Thus the segment stays feasible.

For a nonconvex example, take \(x_1 \in \{0,1\}\) in \(\mathbb{R}^{1}\). Both endpoints are feasible, but the midpoint \(1/2\) is not. A product constraint can also make a nonconvex set; the integrality example matches the lecture directly.

### Question 4 (20 minutes)

(a) Give one LP showing each of the three outcomes: infeasible, unbounded objective, and finite attained optimum.
(b) Give an LP whose feasible region is unbounded but whose objective is bounded, and identify the optimum.
(c) Explain why the half-plane \(\{(u,v): v \ge 0\}\) does not contradict the vertex theorem in the lecture.

**Solution.**

(a) Infeasible: \(x \ge 2\), \(x \le 1\). Unbounded: maximize \(x\) subject to \(x \ge 0\). Finite: maximize \(-x\) subject to \(x \le 1\), \(x \ge 0\), with optimum \(0\) at \(x = 0\).
(b) Maximize \(-x\) subject to \(x \ge 0\). The region is unbounded and the optimum is \(0\) at \(x = 0\).
(c) The vertex theorem in the lecture assumes canonical form, including nonnegativity of every variable. The half-plane has an unrestricted variable and no vertex, even though \(\max(-v)\) has finite optimum \(0\). Substituting \(u = u^+ - u^-\) restores nonnegativity and the vertex statement in the new variables.

### Question 5 (20 minutes)

Let \(x\) be feasible for a polyhedron in \(\mathbb{R}^{n}\), and suppose the tight constraints at \(x\) have rank \(r < n\).

(a) Show there is a nonzero direction \(d\) such that, for all sufficiently small \(\varepsilon > 0\), both \(x+\varepsilon d\) and \(x-\varepsilon d\) remain feasible. You may assume the only constraints are the inequalities defining the polyhedron, and that a constraint that is slack stays satisfied under a small perturbation.
(b) Suppose \(x\) is optimal for \(\max c^\top x\). Show \(c^\top d = 0\).
(c) Explain, in words, how repeating this movement proves that a canonical-form LP with finite optimum has a vertex optimum.

**Solution.**

(a) The tight normals span an \(r\)-dimensional subspace, with \(r < n\), so their common orthogonal complement contains a nonzero \(d\). Moving along \(d\) does not change any tight left-hand side. Slack inequalities remain satisfied for small enough \(\varepsilon\), in both directions.
(b) If \(c^\top d > 0\), then \(x+\varepsilon d\) is feasible and better for small \(\varepsilon\). If \(c^\top d < 0\), then \(x-\varepsilon d\) is better. Optimality forces \(c^\top d = 0\).
(c) The objective is constant along \(d\), so move until a new independent constraint becomes tight. Each step increases the rank of the tight normals. Canonical nonnegativity prevents the line from remaining feasible in both directions forever, so the process reaches a feasible point with \(n\) independent tight constraints and the same objective value.

### Question 6 (15 minutes)

An LP in \(n\) variables has constraints \(0 \le x_i \le 1\) for every \(i\), plus \(k\) additional linear inequalities. Prove that every vertex has at most \(k\) coordinates strictly between \(0\) and \(1\).

**Solution.** At a vertex \(x\), every coordinate outside \((0,1)\) has a tight box constraint. Those tight box normals are distinct unit normals, so they are independent. At most \(k\) additional normals are available. Since some \(n\) tight normals are independent,

\[
n \le \bigl(n - \#\{i : 0 < x_i < 1\}\bigr) + k.
\]

Hence the number of strictly fractional coordinates is at most \(k\).

### Question 7 (15 minutes)

The smoothie LP is

\[
\begin{aligned}
\text{maximize} \quad & 5x_1 + 4x_2 + 6x_3 \\
\text{subject to} \quad & x_1 + x_3 \le 3, \\
& 2x_1 + x_2 + x_3 \le 10, \\
& 2x_2 + x_3 \le 6, \\
& x \ge 0.
\end{aligned}
\]

(a) Verify that \((3,3,0)\) is a vertex by exhibiting three independent tight constraints.
(b) Prove it is optimal.
(c) What changes, conceptually, if liters must be integers? Do not solve the integer program.

**Solution.**

(a) Tight constraints: \(x_1 + x_3 = 3\), \(2x_2 + x_3 = 6\), and \(x_3 = 0\). The normals \((1,0,1)\), \((0,2,1)\), and \((0,0,-1)\) have nonzero determinant \(-2\).
(b) Five times oranges plus two times strawberries gives \(5x_1 + 4x_2 + 7x_3 \le 27\). Nonnegativity of \(x_3\) drops the coefficient \(7\) to \(6\), so every feasible objective is at most \(27\). The feasible value equals this upper bound.
(c) The problem becomes an integer linear program. The continuous optimum remains an upper bound, but an arbitrary LP need not have an integral optimum, and the integer feasible set is not convex.

### Question 8 (15 minutes)

Write the maximum-flow LP for a directed graph \(G = (V,E)\) with source \(s\), sink \(t\), and capacities \(c_e\). Then answer:

(a) How many variables are there?
(b) Why may a feasible solution be fractional even when every \(c_e\) is an integer?
(c) What special fact from Lecture 8 is not true for a general LP?

**Solution.** Maximize \(\sum_{(s,v)\in E} f_{sv} - \sum_{(v,s)\in E} f_{vs}\), subject to conservation at every \(v \notin \{s,t\}\) and \(0 \le f_e \le c_e\).

(a) \(m = |E|\) variables.
(b) The constraints are linear equalities and inequalities over the reals. Integer right-hand sides do not force every feasible point to be integral; they only create the special integral-optimum property for this particular polyhedron.
(c) Integer capacities imply some optimal flow is integral. A general LP can have a unique fractional optimum.

### Question 9 (10 minutes)

Explain the difference between a polynomial-time algorithm and a pseudo-polynomial algorithm, using capacity \(B = 2^{r}\) and the lecture’s comparison between LP and knapsack DP. Then explain why polynomial bit length of a basic solution does not yield an enumeration algorithm.

**Solution.** The integer \(B = 2^{r}\) has encoding length \(r+1\), but magnitude \(2^{r}\). An \(O(nB)\) knapsack DP is polynomial in the magnitude and only pseudo-polynomial in the input length. The LP black box is polynomial in the total binary encoding length, not merely in \(m\) and \(n\), and not in the magnitudes.

A vertex solves some nonsingular system \(Bx = d\), so Cramer’s rule gives polynomial bit length after clearing denominators. The number of possible \(n\)-row bases can still be exponential, so listing them is not a polynomial-time algorithm.

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

For the dual, which the lecture only previews, start with Matoušek and Gärtner, Chapter 6, or Vanderbei’s duality chapter. The lecture stops once the smoothie weights \((5,0,2)\) show that the search for the best upper bound is itself an LP.

---

## 17. One-page formula sheet

\[
\begin{aligned}
&\text{Canonical form:} && \max c^\top x \text{ s.t. } Ax \le b,\ x \ge 0. \\
&\text{Feasible region:} && P = \{x : Ax \le b,\ x \ge 0\}. \\
&\text{Convexity:} && x,y \in P,\ \lambda \in [0,1] \Rightarrow \lambda x + (1-\lambda)y \in P. \\
&\text{Vertex in } \mathbb{R}^{n}: && \text{feasible, and } n \text{ independent tight normals.} \\
&\text{Tight:} && a^\top x = d \text{ for a constraint } a^\top x \le d. \\
&\text{Basic solution:} && Bx = d,\ x_i = \det(B_i)/\det(B). \\
&\text{Certificate:} && y \ge 0,\ A^\top y \ge c \Rightarrow c^\top x \le b^\top y. \\
&\text{Optimality:} && x \text{ feasible, } y \text{ a certificate, and } c^\top x = b^\top y.
\end{aligned}
\]

Conversions: flip the sign to turn minimization into maximization; multiply a \(\ge\) constraint by \(-1\); split an equality into two inequalities; replace an unrestricted variable by a difference of two nonnegative variables.
