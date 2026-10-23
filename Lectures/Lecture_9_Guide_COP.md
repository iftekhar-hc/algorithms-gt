# Lecture 9 Study Guide: Linear Programming, Models, and Geometry

This guide expands the lecture note into a structured tutorial with worked examples, geometric visualizations, pseudocode, review questions, and textbook references. The central theme is that linear programming separates **modeling** from **solving**: first express feasible solutions and objectives mathematically, then use LP theory or a solver to optimize them.

---

## 1. Where Linear Programming Fits in Algorithms

Earlier algorithm-design techniques often exploit a particular computational structure:

- **Divide and conquer** breaks a problem into smaller independent pieces.
- **Dynamic programming** exploits overlapping subproblems.
- **Graph algorithms** exploit graph structure.
- **Linear programming** describes all feasible solutions using linear constraints and lets a general optimization algorithm search that region.

The broader sequence is:

```text
Discrete or continuous problem
            |
            v
Choose decision variables
            |
            v
Write linear constraints
            |
            v
Choose a linear objective
            |
            v
Solve the resulting LP
            |
            v
Interpret or round the solution
```

Linear programming also prepares the ground for convex optimization and approximation algorithms. For example, a difficult integer problem can sometimes be relaxed into an LP, solved efficiently, and then rounded to a discrete solution.

---

## 2. What Is a Linear Program?

A **linear program**, or LP, consists of:

1. Real-valued decision variables.
2. A linear objective function.
3. Linear equality or non-strict inequality constraints.

A common canonical maximization form is

$$
\begin{aligned}
\text{maximize} \quad & c^\top x \\
\text{subject to} \quad & Ax \le b, \\
& x \ge 0,
\end{aligned}
$$

where

$$
A \in \mathbb{R}^{m\times n}, \qquad
b \in \mathbb{R}^m, \qquad
c \in \mathbb{R}^n.
$$

Here:

- $x=(x_1,\dots,x_n)^\top$ contains the variables.
- $c_i$ is the objective contribution of one unit of $x_i$.
- Row $j$ of $A$ represents one constraint.
- $b_j$ is the upper bound in constraint $j$.
- All inequalities are interpreted coordinatewise.

The $j$-th constraint is

$$
\sum_{i=1}^{n} A_{ji}x_i \le b_j.
$$

### 2.1 Feasible region

The **feasible region** is

$$
P=\{x\in\mathbb{R}^n:Ax\le b,\ x\ge 0\}.
$$

A vector $x$ is **feasible** if it satisfies every constraint. An **optimal solution** is a feasible vector with the best objective value.

---

## 3. Modeling an Optimization Problem

A useful modeling process is:

```text
1. Identify the choices that must be made.
2. Introduce one variable for each independent choice.
3. Write resource, balance, or logical restrictions.
4. Write the quantity to maximize or minimize.
5. Check units and signs.
6. Test the model using a few candidate solutions.
```

### Modeling pseudocode

```text
MODEL_AS_LP(problem):
    identify decision variables x[1..n]

    for each limited resource or requirement:
        express its use as a linear expression
        add a linear constraint

    construct a linear objective:
        objective = sum(c[i] * x[i])

    add domain constraints:
        x[i] >= 0 when negative values are meaningless

    return objective, constraints
```

This is not an LP-solving algorithm. It is a disciplined procedure for translating a problem into an LP.

---

## 4. Running Example: Smoothie Production

Suppose a shop has:

- 3 units of oranges,
- 10 units of bananas,
- 6 units of strawberries.

The products are:

| Smoothie | Oranges | Bananas | Strawberries | Revenue |
|---|---:|---:|---:|---:|
| 1 | 1 | 2 | 0 | $5 |
| 2 | 0 | 1 | 2 | $4 |
| 3 | 1 | 1 | 1 | $6 |

Let $x_i$ be the number of liters of smoothie $i$. Fractional liters are permitted. The resulting LP is

$$
\begin{aligned}
\text{maximize}\quad
& 5x_1+4x_2+6x_3\\
\text{subject to}\quad
& x_1+x_3\le 3 &&\text{oranges},\\
& 2x_1+x_2+x_3\le 10 &&\text{bananas},\\
& 2x_2+x_3\le 6 &&\text{strawberries},\\
& x_1,x_2,x_3\ge 0.
\end{aligned}
$$

This illustrates the basic correspondence:

```text
product amounts      -> variables
ingredient limits    -> constraints
revenue              -> objective
physical quantities  -> nonnegativity
```

The candidate solution

$$
x=(3,3,0)
$$

is feasible because

$$
3+0\le3,
$$

$$
2(3)+3+0=9\le10,
$$

and

$$
2(3)+0=6\le6.
$$

Its revenue is

$$
5(3)+4(3)+6(0)=27.
$$

Therefore,

$$
\operatorname{OPT}\ge27.
$$

This proves only a **lower bound** for a maximization problem. It does not yet prove that $27$ is optimal.

### 4.1 Matrix representation

The same LP can be written using

$$
A=
\begin{bmatrix}
1&0&1\\
2&1&1\\
0&2&1
\end{bmatrix},
\qquad
b=
\begin{bmatrix}
3\\10\\6
\end{bmatrix},
\qquad
c=
\begin{bmatrix}
5\\4\\6
\end{bmatrix}.
$$

Thus,

$$
\max c^\top x
\quad\text{subject to}\quad
Ax\le b,\quad x\ge0.
$$

### 4.2 What if only whole liters can be sold?

Then the additional condition is

$$
x_1,x_2,x_3\in\mathbb{Z}_{\ge0}.
$$

This is an **integer linear program**, not an ordinary LP. The linear objective and constraints remain unchanged, but integrality makes the problem fundamentally different.

---

## 5. Maximum Flow as a Linear Program

For each directed edge $e$, introduce a variable $f_e$, representing the amount of flow through that edge.

The objective is to maximize net flow leaving the source $s$:

$$
\max
\left(
\sum_{(s,v)\in E}f_{sv}
-
\sum_{(v,s)\in E}f_{vs}
\right).
$$

For every intermediate vertex $v\notin\{s,t\}$, impose flow conservation:

$$
\sum_{(u,v)\in E}f_{uv}
=
\sum_{(v,w)\in E}f_{vw}.
$$

For every edge $e$, impose capacity constraints:

$$
0\le f_e\le c_e.
$$

There are $|E|$ variables and $O(|V|+|E|)$ constraints. This formulation shows that maximum flow is a special case of linear programming, although specialized flow algorithms are generally more direct for this particular problem.

### Important integrality distinction

The LP allows fractional flows. However, maximum flow has a special property:

> If all capacities are integers, there exists an integral optimal flow.

An arbitrary LP does **not** necessarily have an integral optimal solution. The integrality of maximum flow comes from the structure of its constraint system, not merely from the coefficients being integers.

---

## 6. Converting LPs into Canonical Form

Many LPs do not initially look like

$$
\max c^\top x
\quad\text{subject to}\quad
Ax\le b,\quad x\ge0.
$$

The following transformations convert common forms.

### 6.1 Minimization

To convert

$$
\min c^\top x
$$

into maximization, use

$$
\max -c^\top x.
$$

If the maximum value is $M$, the original minimum value is $-M$.

### 6.2 Greater-than constraints

Convert

$$
a^\top x\ge d
$$

into

$$
-a^\top x\le-d.
$$

### 6.3 Equality constraints

Convert

$$
a^\top x=d
$$

into the pair

$$
a^\top x\le d,
$$

$$
-a^\top x\le-d.
$$

### 6.4 Unrestricted variables

If $z$ may be positive or negative, represent it as

$$
z=z^+-z^-,
$$

where

$$
z^+\ge0,\qquad z^-\ge0.
$$

For example, $z=-5$ can be represented by $z^+=0$ and $z^-=5$.

### 6.5 Slack variables

Convert

$$
Ax\le b
$$

into

$$
Ax+s=b,
\qquad
x,s\ge0,
$$

where

$$
s=b-Ax
$$

is the vector of unused resources. These transformations increase the size of the formulation only polynomially.

### 6.6 Worked conversion example

Convert

$$
\begin{aligned}
\text{minimize}\quad &2u-v\\
\text{subject to}\quad &u-v=3,\\
&u\ge0,
\end{aligned}
$$

where $v$ is unrestricted.

Write

$$
v=v^+-v^-,
\qquad v^+,v^-\ge0.
$$

Negate the objective:

$$
\max -2u+v^+-v^-.
$$

Convert the equality into two inequalities:

$$
u-v^++v^-\le3,
$$

$$
-u+v^+-v^-\le-3.
$$

The canonical form is therefore

$$
\begin{aligned}
\text{maximize}\quad
&-2u+v^+-v^-\\
\text{subject to}\quad
&u-v^++v^-\le3,\\
&-u+v^+-v^-\le-3,\\
&u,v^+,v^-\ge0.
\end{aligned}
$$

---

## 7. What Is Not a Plain LP?

The following are not ordinary LP constraints or objectives:

### Product of variables

$$
x_1x_2\le1
$$

is nonlinear.

### Quadratic objective

$$
\min x_1^2+x_2^2
$$

is not a linear objective.

### Binary restrictions

$$
x_i\in\{0,1\}
$$

create an integer or binary optimization problem.

### Strict inequalities

$$
x<1
$$

are excluded from the ordinary LP framework. For example,

$$
\max x \quad\text{subject to}\quad x<1
$$

has supremum $1$, but no feasible point actually attains $1$.

---

## 8. Geometry of Linear Programs

### 8.1 Convex sets

A set $P\subseteq\mathbb{R}^n$ is **convex** if, for all $x,y\in P$ and every $\lambda\in[0,1]$,

$$
\lambda x+(1-\lambda)y\in P.
$$

Geometrically, the entire line segment connecting any two points in $P$ must remain inside $P$.

```text
Convex set                    Nonconvex set

       ______                    ___     ___
     /        \                 /   \___/   \
    |  x----y  |               | x         y |
     \________/                 \___       ___/
                                   \_____/

Entire segment is inside.      Segment can leave the set.
```

### 8.2 Why every LP feasible region is convex

Suppose $x$ and $y$ are feasible:

$$
Ax\le b,\qquad Ay\le b.
$$

For $\lambda\in[0,1]$, let

$$
z=\lambda x+(1-\lambda)y.
$$

Then

$$
\begin{aligned}
Az
&=A\left(\lambda x+(1-\lambda)y\right)\\
&=\lambda Ax+(1-\lambda)Ay\\
&\le\lambda b+(1-\lambda)b\\
&=b.
\end{aligned}
$$

If $x,y\ge0$, then $z\ge0$ as well. Therefore, $z$ is feasible, proving that LP feasible regions are convex.

---

## 9. Two-Dimensional Geometric Example

Consider

$$
\begin{aligned}
\text{maximize}\quad &2x_1+3x_2\\
\text{subject to}\quad
&x_1+x_2\le5,\\
&x_1\ge1,\\
&x_2\ge0.
\end{aligned}
$$

The vertices are

$$
(1,0),\qquad (5,0),\qquad (1,4).
$$

### 9.1 ASCII visualization

```text
x2
^
|  (1,4) *
|         |\
|         | \
|         |  \
|         |   \
|         |    \
|  (1,0) *-----* (5,0)
+------------------------> x1
```

Evaluate the objective at each vertex:

$$
f(1,0)=2,
$$

$$
f(5,0)=10,
$$

$$
f(1,4)=2+12=14.
$$

Therefore, the optimum is

$$
x^*=(1,4),
\qquad
\operatorname{OPT}=14.
$$

Lines of constant objective have the form

$$
2x_1+3x_2=q.
$$

Increasing $q$ shifts the line in the direction

$$
c=(2,3).
$$

The final objective line that still touches the feasible region touches it at $(1,4)$. If the objective were $x_1+x_2$, every point on the edge $x_1+x_2=5$ would be optimal, demonstrating that an LP optimum need not be unique.

---

## 10. Three Possible LP Outcomes

### 10.1 Infeasible

There is no point satisfying all constraints.

Example:

$$
x\ge2,\qquad x\le1.
$$

```text
x <= 1          x >= 2
<======|        |=======|
       1        2

No overlap
```

### 10.2 Unbounded objective

Feasible solutions exist, and the objective can become arbitrarily large.

Example:

$$
\max x
\quad\text{subject to}\quad
x\ge0.
$$

For every candidate $x$, $x+1$ is feasible and has a larger value.

### 10.3 Feasible with a finite optimum

The feasible region is nonempty, and the best objective value is finite. In the LP setting considered in the lecture, an optimum is attained.

### Important distinction

An **unbounded feasible region** does not necessarily produce an **unbounded objective**.

For example,

$$
\max -x
\quad\text{subject to}\quad
x\ge0
$$

has an unbounded feasible region, but its finite optimum is

$$
x^*=0,\qquad \operatorname{OPT}=0.
$$

The objective direction, not just the shape of the feasible region, determines objective unboundedness.

---

## 11. Tight Constraints and Vertices

A constraint

$$
a^\top x\le d
$$

is **tight** at $x$ if

$$
a^\top x=d.
$$

It is **slack** if

$$
a^\top x<d.
$$

A feasible point in $\mathbb{R}^n$ is a **vertex**, or basic feasible solution, if the normals of its tight constraints span $\mathbb{R}^n$. Equivalently, there are $n$ linearly independent tight constraints. Nonnegativity constraints count as constraints, and a vertex can have more than $n$ tight constraints. The crucial property is linear independence.

### 11.1 Tight constraints in the triangle

The constraints can be written as

$$
x_1+x_2\le5,
$$

$$
-x_1\le-1,
$$

$$
-x_2\le0.
$$

At $(1,0)$:

$$
x_1=1,\qquad x_2=0.
$$

At $(5,0)$:

$$
x_1+x_2=5,\qquad x_2=0.
$$

At $(1,4)$:

$$
x_1=1,\qquad x_1+x_2=5.
$$

Each vertex is determined by two independent tight constraints because the problem is in $\mathbb{R}^2$.

### 11.2 Tight constraints in the smoothie solution

At

$$
x=(3,3,0),
$$

the following constraints are tight:

1. Orange constraint:
   $$x_1+x_3=3.$$
2. Strawberry constraint:
   $$2x_2+x_3=6.$$
3. Nonnegativity of $x_3$:
   $$x_3=0.$$

Their normals are

$$
(1,0,1),\qquad(0,2,1),\qquad(0,0,1),
$$

which are linearly independent. Thus, $(3,3,0)$ is a vertex.

---

## 12. Why an Optimal Vertex Exists

For an LP in canonical form, if it is feasible and has a finite optimal value, then it has an optimal solution at a vertex.

### Geometric intuition

Suppose an optimal point has fewer than $n$ independent tight constraints. Then there is a nonzero direction $d$ parallel to all currently tight constraint boundaries.

For a sufficiently small $\varepsilon>0$, both

$$
x+\varepsilon d
\quad\text{and}\quad
x-\varepsilon d
$$

remain feasible.

Three possibilities exist:

1. $c^\top d>0$: moving in direction $d$ improves the objective, contradicting optimality.
2. $c^\top d<0$: moving in direction $-d$ improves the objective, contradicting optimality.
3. $c^\top d=0$: the objective is constant along the direction.

In the third case, move while preserving the objective until another independent constraint becomes tight. Repeat until reaching a vertex.

```text
optimal point on a face
          |
          | move without changing objective
          v
lower-dimensional face
          |
          | repeat
          v
optimal vertex
```

### Caveat

The canonical-form assumption matters. A general polyhedron may have no vertices. For instance,

$$
\{(u,v):v\ge0\}
$$

contains complete horizontal lines and has no vertices. The objective

$$
\max -v
$$

still has finite optimal value $0$, attained at every point with $v=0$. Converting to canonical form introduces new variables and restores the relevant vertex statement in the transformed space.

---

## 13. Conceptual Vertex Enumeration

The vertex theorem suggests the following brute-force procedure.

```text
ENUMERATE_VERTICES(A, b, c):
    best_point = NONE
    best_value = -INFINITY

    include Ax <= b and all nonnegativity constraints

    for each choice S of n constraints:
        if constraints in S are linearly independent:
            solve the corresponding equality system

            if the solution x satisfies every constraint:
                if c^T x > best_value:
                    best_point = x
                    best_value = c^T x

    if no feasible point was found:
        report "infeasible"
    else:
        return best_point, best_value
```

This is useful for understanding the geometry, but it is generally **not efficient**. With $M$ total constraints, it may inspect

$$
\binom{M}{n}
$$

candidate bases, which can be exponential in the input size.

The statement “there is an optimal vertex” does not imply “enumerating all vertices is polynomial.”

---

## 14. Polynomial-Time Solvability and Input Size

For rational input, linear programming can be solved in time polynomial in the total binary encoding length. An appropriate algorithm can report:

- infeasibility,
- unboundedness, or
- an exact rational optimal solution when a finite optimum exists.

The polynomial-time guarantee is supported by methods such as the ellipsoid method and interior-point methods.

### 14.1 Why an optimal vertex has a compact representation

At a vertex, choose $n$ independent tight constraints. They form a nonsingular system

$$
Bx=d.
$$

By Cramer’s rule,

$$
x_i=\frac{\det(B_i)}{\det(B)},
$$

where $B_i$ replaces column $i$ of $B$ with $d$.

After rational denominators are cleared, the determinants have polynomially bounded encoding length. Thus, a basic optimal solution can be represented with polynomially many bits. This proves that an optimal solution has a short representation, but it does not provide an efficient enumeration algorithm.

### 14.2 Polynomial versus pseudo-polynomial time

Suppose a numerical capacity is

$$
B=2^r.
$$

Its binary representation requires only approximately $r+1$ bits. An algorithm with running time

$$
O(nB)
$$

therefore takes

$$
O(n2^r)
$$

time as a function of the encoded input length. This is pseudo-polynomial, not polynomial in the bit length.

LP polynomial-time results refer to the number of input bits, not merely the number of variables and constraints.

---

## 15. A Useful Vertex Sparsity Property

Suppose an LP in $n$ variables has box constraints

$$
0\le x_i\le1
$$

and only $k$ additional linear inequalities.

At a vertex, $n$ independent constraints must be tight.

If a coordinate satisfies

$$
0<x_i<1,
$$

neither $x_i=0$ nor $x_i=1$ is tight. Therefore, each fractional coordinate must be fixed through the $k$ additional constraints.

Since those constraints provide at most $k$ independent tight conditions, at most $k$ coordinates can be strictly between $0$ and $1$.

Hence every vertex has at most $k$ fractional coordinates.

This property is important in rounding arguments: an LP vertex may already be “mostly integral.”

---

## 16. Proving Optimality Without Solving the LP Again

A feasible solution gives a lower bound in a maximization problem:

$$
c^\top x\le\operatorname{OPT}.
$$

To prove that $x$ is optimal, we also need an upper bound:

$$
\operatorname{OPT}\le c^\top x.
$$

If the lower and upper bounds agree, the solution is optimal.

### 16.1 Smoothie optimality certificate

Recall the candidate

$$
x=(3,3,0)
$$

with objective value $27$.

Take:

- five times the orange constraint,
- two times the strawberry constraint.

This gives

$$
5(x_1+x_3)+2(2x_2+x_3)
\le
5(3)+2(6).
$$

After simplification,

$$
5x_1+4x_2+7x_3\le27.
$$

Because $x_3\ge0$,

$$
5x_1+4x_2+6x_3
\le
5x_1+4x_2+7x_3.
$$

Therefore, every feasible solution satisfies

$$
5x_1+4x_2+6x_3\le27.
$$

But the candidate $(3,3,0)$ achieves $27$. Thus,

$$
\boxed{\operatorname{OPT}=27}
$$

and

$$
\boxed{x^*=(3,3,0)}
$$

is optimal.

### Certificate visualization

```text
Feasible solution                          Weighted constraints
gives lower bound                          give upper bound

       27 <= OPT                    OPT <= 5(orange) + 2(strawberry)
                                             = 5(3) + 2(6)
                                             = 27

                         Therefore
                         OPT = 27
```

---

## 17. Why the Multipliers Must Be Nonnegative

Suppose a feasible solution satisfies

$$
a_i^\top x\le b_i.
$$

Multiplying by $y_i\ge0$ preserves the inequality:

$$
y_i a_i^\top x\le y_i b_i.
$$

Adding the weighted inequalities gives

$$
\left(\sum_i y_i a_i\right)^\top x
\le
\sum_i y_i b_i.
$$

If the combined left side dominates the objective, then the right side is an upper bound on every feasible solution.

Negative multipliers would reverse inequalities, so arbitrary negative weights cannot be used safely. The search for the best nonnegative combination of constraints forms another LP, called the **dual**. The smoothie proof is therefore a preview of LP duality.

### Optimality-certificate pseudocode

```text
VERIFY_MAX_LP_CERTIFICATE(A, b, c, x, y):
    # Primal feasibility
    if x has a negative coordinate:
        return FALSE

    if A*x is not coordinatewise <= b:
        return FALSE

    # Certificate multipliers
    if y has a negative coordinate:
        return FALSE

    # Weighted constraints must dominate the objective
    if A^T*y is not coordinatewise >= c:
        return FALSE

    lower_bound = c^T*x
    upper_bound = b^T*y

    if lower_bound == upper_bound:
        return TRUE
    else:
        return FALSE
```

This captures the structure of a primal feasible solution and a matching upper-bound certificate.

---

## 18. Key Concept Map

```text
                         LINEAR PROGRAMMING
                                  |
          +-----------------------+----------------------+
          |                       |                      |
       Modeling                Geometry              Algorithms
          |                       |                      |
   variables/objective       convex region       polynomial time
   linear constraints        vertices            bit complexity
          |                       |                      |
          +-----------------------+----------------------+
                                  |
                            Optimality proof
                                  |
                    feasible solution + upper bound
                                  |
                                duality
```

---

## 19. Common Mistakes

### Mistake 1: Treating feasibility as optimality

Finding a feasible solution of value $27$ proves only

$$
\operatorname{OPT}\ge27.
$$

It does not prove equality.

### Mistake 2: Assuming integer coefficients imply an integer optimum

An LP with integer data may have fractional vertices. Maximum flow has integrality because of special structural properties.

### Mistake 3: Assuming an unbounded feasible region means an unbounded objective

The objective must improve along an unbounded feasible direction.

### Mistake 4: Counting tight constraints without checking independence

A point may have many tight constraints whose normal vectors are linearly dependent.

### Mistake 5: Replacing $a^\top x\ge d$ incorrectly

The correct conversion is

$$
-a^\top x\le-d.
$$

Both sides must be negated.

### Mistake 6: Calling $O(nB)$ polynomial without considering encoding

If $B$ is encoded in binary, $O(nB)$ may be exponential in the number of input bits.

### Mistake 7: Enumerating all vertices and calling it a polynomial algorithm

The number of possible bases or vertices can be exponential.

---

## 20. Quiz Questions

### Conceptual questions

1. What three ingredients define a linear program?
2. What is the feasible region of an LP?
3. Why is every LP feasible region convex?
4. What is the difference between a tight and a slack constraint?
5. Does every optimal LP solution have to be a vertex?
6. If an LP has multiple optimal solutions, what geometric structure might contain them?
7. Why does a feasible solution provide a lower bound for a maximization LP?
8. Why must constraint multipliers be nonnegative when building an upper bound?
9. Does an unbounded feasible region imply an unbounded objective?
10. Why is integer linear programming not equivalent to ordinary linear programming?

### Short calculations

11. Convert
    $$3x_1-x_2\ge7$$
    into a $\le$ constraint.

12. Replace the unrestricted variable $z$ using nonnegative variables.

13. Convert
    $$x_1+2x_2=5$$
    into two inequalities.

14. For
    $$\max x_1+2x_2$$
    subject to
    $$x_1+x_2\le4,\quad x_1,x_2\ge0,$$
    evaluate the objective at every vertex.

15. At $(3,3,0)$ in the smoothie LP, which resource constraint is slack?

### Quiz answers

1. Real variables, a linear objective, and linear equality or non-strict inequality constraints.
2. The set of all vectors satisfying every constraint.
3. Linear inequalities are preserved under convex combinations.
4. A tight constraint holds with equality; a slack constraint has strict inequality.
5. Not every optimal solution must be a vertex, but a canonical-form LP with a finite optimum has at least one optimal vertex.
6. A face, such as an edge.
7. The optimum is at least as large as the value of any particular feasible solution.
8. Multiplying an inequality by a nonnegative number preserves its direction.
9. No.
10. Integrality is a discrete, nonconvex restriction.
11. $-3x_1+x_2\le-7$.
12. $z=z^+-z^-$, where $z^+,z^-\ge0$.
13. $x_1+2x_2\le5$ and $-x_1-2x_2\le-5$.
14. The vertices are $(0,0),(4,0),(0,4)$, with values $0,4,8$. The optimum is $(0,4)$.
15. The banana constraint: $2(3)+3+0=9<10$.

---

## 21. Exam-Style Questions

### Question 1: Modeling

A company manufactures desks and chairs.

- A desk requires 4 hours of carpentry and 2 hours of painting.
- A chair requires 2 hours of carpentry and 3 hours of painting.
- There are 40 carpentry hours and 36 painting hours available.
- A desk earns $60 and a chair earns $45.

Formulate an LP that maximizes profit.

#### Solution sketch

Let $d$ and $h$ be the numbers of desks and chairs.

$$
\begin{aligned}
\max\quad &60d+45h\\
\text{s.t.}\quad
&4d+2h\le40,\\
&2d+3h\le36,\\
&d,h\ge0.
\end{aligned}
$$

If products must be manufactured in whole units, add $d,h\in\mathbb{Z}_{\ge0}$, producing an integer LP.

### Question 2: Geometry and optimization

Solve geometrically:

$$
\begin{aligned}
\max\quad &3x_1+2x_2\\
\text{s.t.}\quad
&x_1+x_2\le6,\\
&2x_1+x_2\le8,\\
&x_1,x_2\ge0.
\end{aligned}
$$

#### Solution sketch

The vertices are

$$
(0,0),\quad(4,0),\quad(0,6),
$$

and the intersection of $x_1+x_2=6$ with $2x_1+x_2=8$. Subtracting gives $x_1=2$, so $x_2=4$.

Objective values:

$$
f(0,0)=0,\quad f(4,0)=12,\quad f(0,6)=12,\quad f(2,4)=14.
$$

Therefore,

$$
x^*=(2,4),\qquad\operatorname{OPT}=14.
$$

### Question 3: Convexity proof

Prove that the intersection of convex sets is convex. Use this to give another proof that an LP feasible region is convex.

#### Solution sketch

Let

$$
P=\bigcap_{i\in I}P_i,
$$

where every $P_i$ is convex. If $x,y\in P$, then $x,y\in P_i$ for every $i$. Thus,

$$
\lambda x+(1-\lambda)y\in P_i
$$

for every $i$, so it belongs to their intersection $P$.

Each linear inequality defines a half-space, and every half-space is convex. Therefore, the intersection of all LP constraint half-spaces is convex.

### Question 4: Tight constraints

For the feasible region

$$
\begin{aligned}
x_1+x_2&\le5,\\
x_1&\ge1,\\
x_2&\ge0,
\end{aligned}
$$

identify the tight constraints at each vertex and verify that their normals are independent.

#### Solution sketch

- At $(1,0)$: $x_1=1$ and $x_2=0$.
- At $(5,0)$: $x_1+x_2=5$ and $x_2=0$.
- At $(1,4)$: $x_1=1$ and $x_1+x_2=5$.

Each pair has linearly independent normals.

### Question 5: Optimality certificate

Consider

$$
\begin{aligned}
\max\quad &3x_1+2x_2\\
\text{s.t.}\quad
&x_1+x_2\le4,\\
&2x_1+x_2\le6,\\
&x_1,x_2\ge0.
\end{aligned}
$$

Show that $x=(2,2)$ is optimal by constructing a weighted combination of constraints.

#### Solution sketch

The candidate is feasible and has value

$$
3(2)+2(2)=10.
$$

Use weight $1$ on each constraint:

$$
(x_1+x_2)+(2x_1+x_2)\le4+6.
$$

Therefore,

$$
3x_1+2x_2\le10.
$$

The candidate achieves $10$, so it is optimal.

### Question 6: Fractional-coordinate theorem

An LP in $n$ variables contains $0\le x_i\le1$ for every $i$, plus $k$ other inequalities. Prove that any vertex has at most $k$ fractional coordinates.

#### Solution sketch

If $0<x_i<1$, neither box boundary is tight for coordinate $i$. If $r$ variables are fractional, the box constraints provide at most $n-r$ independent tight constraints. A vertex needs $n$ independent tight constraints, so at least $r$ must come from the $k$ additional constraints. Hence

$$
r\le k.
$$

### Question 7: Bit complexity

Explain why an $O(nB)$ algorithm is not necessarily polynomial-time when $B$ is part of the input.

#### Solution sketch

If $B=2^r$, then $B$ uses only $r+1$ binary bits, but

$$
O(nB)=O(n2^r),
$$

which is exponential in $r$. Such a running time is pseudo-polynomial.

### Question 8: Challenge question

Construct an LP with:

1. an unbounded feasible region but a unique finite optimum;
2. an unbounded feasible region and infinitely many optimal solutions;
3. a bounded feasible region and multiple optimal solutions.

#### Example answers

1. Unique finite optimum:
   $$
   \max -x-y
   \quad\text{s.t.}\quad
   x,y\ge0.
   $$
   Unique optimum: $(0,0)$.

2. Infinitely many optimal solutions:
   $$
   \max -y
   \quad\text{s.t.}\quad
   y\ge0,
   $$
   with $x$ unrestricted. Every $(x,0)$ is optimal.

3. Bounded region with multiple optima:
   $$
   \max x_1+x_2
   \quad\text{s.t.}\quad
   x_1+x_2\le1,\quad x_1,x_2\ge0.
   $$
   Every point on $x_1+x_2=1$ is optimal.

---

## 22. Recommended Textbook References

### Primary references

1. **Dasgupta, Papadimitriou, and Vazirani, _Algorithms_**  
   Useful for an algorithms-oriented introduction to linear programming, duality, flows, approximation, and computational complexity.

2. **Kleinberg and Tardos, _Algorithm Design_**  
   Recommended for connecting LP formulations to network flow, approximation algorithms, and broader algorithm-design techniques.

3. **Cormen, Leiserson, Rivest, and Stein, _Introduction to Algorithms_**  
   Useful for reviewing maximum flow, polynomial-time analysis, input encoding, and related algorithmic foundations.

4. **Bertsimas and Tsitsiklis, _Introduction to Linear Optimization_**  
   A focused treatment of LP geometry, vertices, basic feasible solutions, duality, simplex methods, and sensitivity.

5. **Chvátal, _Linear Programming_**  
   A rigorous reference for polyhedra, vertices, simplex methods, duality, and linear-programming theory.

### Convexity and duality reference

6. **Boyd and Vandenberghe, _Convex Optimization_**  
   Especially relevant sections include the introductory discussion of linear programming, the chapter on convex sets, supporting hyperplanes, and the chapter on duality.

### Suggested reading sequence

```text
Lecture 9 notes
    |
    +--> Algorithms-oriented LP chapter
    |
    +--> Bertsimas and Tsitsiklis for LP geometry
    |
    +--> Boyd and Vandenberghe for convexity
    |
    +--> LP duality and optimality certificates
    |
    +--> LP relaxations and approximation algorithms
```

---

## 23. Final Takeaways

1. An LP models a problem using real variables, a linear objective, and linear constraints.
2. LP feasible regions are convex because linear constraints are preserved under convex combinations.
3. A finite canonical-form LP optimum can be attained at a vertex.
4. A vertex is characterized by enough linearly independent tight constraints.
5. A feasible solution alone gives only one side of an optimality argument.
6. Weighted combinations of constraints can provide matching upper bounds.
7. These upper-bound certificates motivate the dual LP.
8. LPs with rational input are solvable in polynomial time measured in binary encoding length.
9. A compact optimal solution does not justify enumerating all vertices.
10. LPs form a bridge from exact optimization to duality, convex optimization, and approximation algorithms.


## 24. Video Lectures
Based on the lecture note you shared, I’d prioritize videos on **LP formulation, feasible-region geometry, vertices, simplex, duality, and LP applications in algorithms**.

## Best starting point

### 1. MIT: Introduction to Linear Programming

**Lecture 12: Introduction to Linear Programming**, taught by Peter Shor, covers the definition of LPs, the diet and bake-sale examples, standard and canonical forms, and an introduction to duality. It aligns especially well with the first half of your lecture note. [[youtube.com]](https://www.youtube.com/watch?v=qKNkP6IfjvY)

**Recommended for:**

- Formulating an LP
- Standard and canonical forms
- Primal and dual programs
- A concise university-level introduction

[Watch Lecture 12 on YouTube](https://www.youtube.com/watch?v=qKNkP6IfjvY) [[youtube.com]](https://www.youtube.com/watch?v=qKNkP6IfjvY)

---

### 2. MIT: LP, Reductions, and Simplex

**Lecture 15: Linear Programming: LP, Reductions, Simplex** from MIT’s _Design and Analysis of Algorithms_ course is the strongest single lecture for connecting linear programming to algorithms. It introduces LP formulations and reductions, discusses duality, and walks through the simplex algorithm and pivoting. [[ocw.mit.edu]](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/resources/lecture-15-linear-programming-lp-reductions-simplex/), [[youtube.com]](https://www.youtube.com/watch?v=WwMz2fJwUCg)

**Recommended for:**

- LPs in algorithm design
- General LP formulations
- Duality intuition
- Slack form
- Simplex and pivot operations
- Connections to computational complexity

[Watch on MIT OpenCourseWare](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/resources/lecture-15-linear-programming-lp-reductions-simplex/) [[ocw.mit.edu]](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/resources/lecture-15-linear-programming-lp-reductions-simplex/)

[](https://www.youtube.com/watch?v=WwMz2fJwUCg)

[15. Linear Programming: LP, reductions, Simplex](https://www.youtube.com/watch?v=WwMz2fJwUCg)

[MIT 6.046J Design and Analysis of Algorithms, Spring 2015 View the complete course: http://ocw.mit.edu/6-046JS15 Instructor: Srinivas Devadas In this lecture, Professor Devadas introduces linear programming. License: Creative Commons BY-NC-SA More information at http://ocw.mit.edu/terms More courses at http://ocw.mit.edu](https://www.youtube.com/watch?v=WwMz2fJwUCg)

---

## Best complete course

### 3. Cornell: Fundamentals of Linear Programming

The **Fundamentals of Linear Programming** playlist contains 24 videos based on an introductory master’s-level course taught at Cornell. It covers formulation, graphical solutions, linear-algebra preparation, simplex, initial feasible solutions, degeneracy, network flows, Gurobi, weak and strong duality, complementary slackness, integer programming, branch-and-bound, logistics, and optimization under uncertainty. Course notes and handwritten lecture materials are also available through the associated course page. [[youtube.com]](https://www.youtube.com/playlist?list=PLc6nihbq_fwa4EG4kvpwz9AJlFpIoFgld)

**Recommended for:**

- A systematic semester-style treatment
- Simplex calculations
- Duality and complementary slackness
- Network-flow formulations
- Integer programming after LP
- Practical solver usage

[Open the Cornell playlist](https://www.youtube.com/playlist?list=PLc6nihbq_fwa4EG4kvpwz9AJlFpIoFgld) [[youtube.com]](https://www.youtube.com/playlist?list=PLc6nihbq_fwa4EG4kvpwz9AJlFpIoFgld)

This would be my **primary recommendation** if you want to learn the subject thoroughly rather than watch only one or two overview lectures.

---

## Shorter options

### 4. Graphical LP for beginners

Class Central lists a 33-minute **Linear Programming** lesson from The Organic Chemistry Tutor. It focuses on translating profit and sales problems into objective functions and constraints, graphing the feasible region, and checking corner points. [[classcentral.com]](https://www.classcentral.com/subject/linear-programming)

**Recommended for:**

- Two-variable graphical problems
- Feasible regions
- Corner-point optimization
- Quick review before solving exercises

This is a good warm-up before watching the more theoretical MIT lectures.

### 5. Duality-focused lecture

Ryan O’Donnell’s **Linear Programming Duality**, listed through Class Central, discusses duality through Farkas’ lemma and Fourier–Motzkin elimination, including certificates of infeasibility. It is a shorter but more theoretical treatment. [[classcentral.com]](https://www.classcentral.com/subject/linear-programming)

**Recommended for:**

- Why dual certificates work
- Infeasibility certificates
- Stronger theoretical foundations
- Preparation for approximation algorithms

Watch this after you understand primal and dual LP formulations.

### 6. Structured course with assessments

The **Industrial Optimization: Models & Linear Programming** course on Coursera has four modules and covers LP formulation, graphical solutions, simplex, Big-M, revised simplex, dual simplex, and software-supported solution methods. Its first module introduces operations research and LP through formulation and graphical examples. [[coursera.org]](https://www.coursera.org/learn/industrial-optimization-models--linear-programming)

**Recommended for:**

- Guided assignments and assessments
- Operations-research applications
- Several simplex variants
- A structured course experience

Some course access or assessment features may require payment.

---

## Suggested viewing sequence

### Fast track: approximately 4 to 6 hours

1. **Graphical introduction** from The Organic Chemistry Tutor
2. **MIT Lecture 12** on LP formulation and canonical forms
3. **MIT Lecture 15** on reductions and simplex
4. **Ryan O’Donnell’s duality lecture**
5. Solve the quiz and exam problems from your study guide

### Thorough track

Work through the Cornell playlist in this order:

1. Formulating optimization problems
2. Graphical solution of LPs
3. Linear-algebra review
4. Simplex method
5. Initial feasible solutions
6. Multiple optima, unboundedness, and degeneracy
7. Network-flow problems
8. Weak and strong duality
9. Complementary slackness
10. Integer programming and branch-and-bound [[youtube.com]](https://www.youtube.com/playlist?list=PLc6nihbq_fwa4EG4kvpwz9AJlFpIoFgld)

Then use the MIT algorithms lecture to reinforce how LP fits into algorithm design and reductions. [[ocw.mit.edu]](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/resources/lecture-15-linear-programming-lp-reductions-simplex/), [[youtube.com]](https://www.youtube.com/watch?v=WwMz2fJwUCg)

## Best match by topic

- **Modeling and canonical form:** MIT Lecture 12
- **Feasible-region geometry:** Organic Chemistry Tutor, then Cornell graphical LP lectures
- **Vertices and simplex:** Cornell playlist and MIT Lecture 15
- **Duality and optimality certificates:** Cornell duality lectures, followed by Ryan O’Donnell
- **Maximum flow and network LPs:** Cornell network-flow lectures
- **Algorithms and complexity:** MIT Lecture 15
- **Solver practice:** Cornell Gurobi lecture or the Coursera course

For your current lecture note, the most efficient combination is **MIT Lecture 12 → MIT Lecture 15 → Cornell’s duality and network-flow lectures**.
