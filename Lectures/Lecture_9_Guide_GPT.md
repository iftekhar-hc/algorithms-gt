# Lecture 9 study guide: Linear programming, models, and geometry

Based on **CS 6515, Lecture 9: Linear Programming: Models and Geometry** (Sahil Singla and Gerandy Brito, Fall 2026). This guide expands the note with worked examples, text visualizations, pseudocode, practice questions, and solutions. [file:1]

> **Rendering note:** Display mathematics uses `\[ ... \]`, and inline mathematics uses `\( ... \)`. Use a Markdown viewer with LaTeX/MathJax or KaTeX support.

## 1. The big idea

Linear programming (LP) separates **what solutions are allowed** from **which solution is best**. Choose real-valued decision variables, impose linear constraints, and optimize a linear objective. The lecture's canonical maximization form is

\[
\begin{aligned}
\max_{x\in\mathbb R^n}\quad &c^{\mathsf T}x\\
\text{subject to}\quad &Ax\le b,\\
&x\ge 0.
\end{aligned}
\]

Here \(A\in\mathbb R^{m\times n}\), \(b\in\mathbb R^m\), and \(c\in\mathbb R^n\); inequalities are coordinatewise. Computational complexity claims assume rational input coefficients. The **feasible region** is \(P=\{x:Ax\le b,\ x\ge0\}\). A feasible point meets every constraint; an optimal point is feasible and has the best objective value. [file:1]

**Modeling checklist:** What are the decisions? What is being maximized or minimized? What are the limited resources or other rules? Are decisions divisible, or must they be whole numbers? The last question matters: integrality requirements change the problem from a plain LP to an integer program. [file:1]

## 2. Model the smoothie problem

Let \(x_i\) be liters of smoothie \(i\). Ingredients and revenue per liter are:

| Smoothie | Oranges | Bananas | Strawberries | Revenue |
|---|---:|---:|---:|---:|
| 1 | 1 | 2 | 0 | 5 |
| 2 | 0 | 1 | 2 | 4 |
| 3 | 1 | 1 | 1 | 6 |

Supplies are 3 oranges, 10 bananas, and 6 strawberries. The model is

\[
\begin{aligned}
\max\quad &5x_1+4x_2+6x_3\\
\text{s.t.}\quad &x_1+x_3\le3 &&\text{(oranges)},\\
&2x_1+x_2+x_3\le10 &&\text{(bananas)},\\
&2x_2+x_3\le6 &&\text{(strawberries)},\\
&x_1,x_2,x_3\ge0.
\end{aligned}
\]

**Matrix version:**

\[
A=\begin{pmatrix}1&0&1\\2&1&1\\0&2&1\end{pmatrix},\qquad
b=\begin{pmatrix}3\\10\\6\end{pmatrix},\qquad
c=\begin{pmatrix}5\\4\\6\end{pmatrix}.
\]

Try \(x=(3,3,0)\): its resource use is \((3,9,6)\), so it is feasible and earns \(5(3)+4(3)=27\). This establishes a **lower bound** \(\mathrm{OPT}\ge27\), not optimality by itself. Bananas have 1 unit of slack; oranges and strawberries are fully used. If sales must be in whole liters, add \(x_i\in\mathbb Z_{\ge0}\); that is an integer linear program rather than the LP above. [file:1]

### Slack as unused capacity

For each resource, set \(s=b-Ax\). Then \(Ax+s=b\), with \(s\ge0\). At \((3,3,0)\), \(s=(0,1,0)\). A zero slack means the corresponding resource constraint is **tight**. [file:1]

```text
capacity:       oranges  3/3  [###]   tight
                bananas  9/10 [#########.]  1 unused
           strawberries  6/6  [######] tight
```

## 3. Recognize and convert LPs

| Starting feature | Canonical-form transformation |
|---|---|
| Minimize \(c^{\mathsf T}x\) | Maximize \(-c^{\mathsf T}x\); negate the resulting optimal value |
| \(a^{\mathsf T}x\ge d\) | Multiply by \(-1\): \(-a^{\mathsf T}x\le-d\) |
| \(a^{\mathsf T}x=d\) | Use \(a^{\mathsf T}x\le d\) and \(-a^{\mathsf T}x\le-d\) |
| Free variable \(z\in\mathbb R\) | Replace by \(z^+-z^-\), with \(z^+,z^-\ge0\) |
| \(Ax\le b\) | Add slack \(s=b-Ax\ge0\) to get \(Ax+s=b\) |

**Worked conversion.** Convert \(\min(2u-v)\) subject to \(u-v=3\), \(u\ge0\), and unrestricted \(v\). Set \(v=p-q\), where \(p,q\ge0\). The canonical LP is

\[
\begin{aligned}
\max\quad &-2u+p-q\\
\text{s.t.}\quad &u-p+q\le3,\\
&-u+p-q\le-3,\\
&u,p,q\ge0.
\end{aligned}
\]

The original equality gives \(v=u-3\), so the original objective is \(2u-v=u+3\). Thus \(u=0,v=-3\) attains minimum 3, while the canonical maximum is \(-3\). [file:1]

**Not plain LPs:** A product \(x_1x_2\), a squared objective such as \(x_1^2+x_2^2\), or the requirement \(x_i\in\{0,1\}\) falls outside the definition. Strict constraints are excluded too: \(\max x\) subject to \(x<1\) approaches 1 but never reaches it. [file:1]

### Maximum flow as an LP

In a directed network, assign a flow \(f_e\) to every edge \(e\) with capacity \(u_e\). Maximize net flow out of source \(s\):

\[
\max\left(\sum_{(s,v)\in E}f_{sv}-\sum_{(v,s)\in E}f_{vs}\right),
\quad 0\le f_e\le u_e,
\quad \sum_{(u,v)\in E}f_{uv}=\sum_{(v,w)\in E}f_{vw}\quad(v\notin\{s,t\}).
\]

For example, if the only route is \(s\to a\to t\), with capacities 4 and 2, flow conservation sets both edge flows equal, so the maximum is 2. LP variables allow fractions, but integer capacities in a flow network admit an integral optimum; general LPs do not necessarily have that property. [file:1]

## 4. See the geometry

A set is **convex** if the line segment joining any two of its points stays inside it. If feasible \(x,y\) satisfy \(Ax,Ay\le b\), then for \(0\le\lambda\le1\),

\[
A(\lambda x+(1-\lambda)y)=\lambda Ax+(1-\lambda)Ay\le b.
\]

Nonnegativity is also preserved, so every LP feasible region is convex. Each inequality cuts out a half-space; intersecting these half-spaces yields a polyhedron. [file:1]

Consider the lecture's two-variable LP:

\[
\max\ 2x_1+3x_2
\quad\text{s.t.}\quad x_1+x_2\le5,\quad x_1\ge1,\quad x_2\ge0.
\]

```text
 x2
  ^
4 |    * (1,4), objective 14
  |    |\
3 |    | \       feasible triangle P is inside
2 |    |  \
1 |    |   \
0 +----*----\-----------*----> x1
       (1,0)           (5,0)
       objective 2     objective 10

 sloped boundary: x1 + x2 = 5
 vertical boundary: x1 = 1
 horizontal boundary: x2 = 0
```

Objective lines \(2x_1+3x_2=q\) are parallel; increasing \(q\) slides the line in direction \(c=(2,3)\). The last line that still touches the triangle passes through \((1,4)\), giving value 14. If the objective were \(x_1+x_2\), the entire sloped edge would have value 5: an optimum need not be unique. [file:1]

### Tight constraints and vertices

A constraint is **tight** when equality holds. In \(\mathbb R^n\), a feasible point is a vertex when the normals of its tight constraints include \(n\) linearly independent vectors. Nonnegativity constraints count: \(x_i\ge0\) means \(-x_i\le0\). Having \(n\) tight constraints alone is not enough if their normals are dependent. [file:1]

| Triangle vertex | Two independent tight constraints | Objective \(2x_1+3x_2\) |
|---|---|---:|
| \((1,0)\) | \(x_1=1\), \(x_2=0\) | 2 |
| \((5,0)\) | \(x_1+x_2=5\), \(x_2=0\) | 10 |
| \((1,4)\) | \(x_1=1\), \(x_1+x_2=5\) | 14 |

For smoothie point \((3,3,0)\), oranges \(x_1+x_3=3\), strawberries \(2x_2+x_3=6\), and nonnegativity \(x_3=0\) give three independent tight constraints. Bananas are **not** tight because the left side is 9. [file:1]

A canonical-form LP that is feasible with a finite optimal value has an optimal vertex. Intuitively, if an optimal point is not a vertex, one can move along a feasible direction that keeps the objective unchanged until another independent constraint becomes tight; repeat. This does not mean **every** optimal point is a vertex. The canonical-form condition matters: \(\{(u,v):v\ge0\}\) has no vertex even though \(\max(-v)\) has optimal value 0. [file:1]

### Three outcomes and a trap

- **Infeasible:** \(x\ge2\) and \(x\le1\) leave no feasible point.
- **Unbounded objective:** \(\max x\) with \(x\ge0\) can grow without limit.
- **Finite optimum:** \(\max(-x)\) with \(x\ge0\) attains 0 at \(x=0\), although its feasible region is unbounded.

Do not confuse an unbounded region with an unbounded objective. [file:1]

## 5. Optimality certificates and algorithms

A candidate solution alone supplies a lower bound for a **maximization** problem. To establish optimality, supply a matching upper bound that applies to *every* feasible point. For the smoothie model, multiply the orange constraint by 5 and the strawberry constraint by 2:

\[
5(x_1+x_3)+2(2x_2+x_3)\le 5(3)+2(6)=27.
\]

The left side is \(5x_1+4x_2+7x_3\). Since \(x_3\ge0\),

\[
5x_1+4x_2+6x_3\le5x_1+4x_2+7x_3\le27.
\]

Thus \((3,3,0)\) achieves the universal upper bound 27 and is optimal. **Visualize the sandwich:**

```text
candidate feasible value       OPT        universal upper bound
          27               <=  ?  <=              27
                         therefore OPT = 27
```

The weights \(y=(5,0,2)\) on orange, banana, and strawberry constraints produce the bound \(b^{\mathsf T}y=27\). More generally, for the canonical LP, any \(y\ge0\) satisfying \(A^{\mathsf T}y\ge c\) gives

\[
c^{\mathsf T}x\le (A^{\mathsf T}y)^{\mathsf T}x=y^{\mathsf T}Ax\le y^{\mathsf T}b
\]

for every feasible \(x\). This is the lecture's motivation for the **dual LP** (developed later): find the smallest such upper bound by minimizing \(b^{\mathsf T}y\) subject to \(A^{\mathsf T}y\ge c\), \(y\ge0\). Here the dual constraints are \(y_1+2y_2\ge5\), \(y_2+2y_3\ge4\), and \(y_1+y_2+y_3\ge6\); \((5,0,2)\) satisfies all three. [file:1]

### Pseudocode: verify a certificate

This checks a proposed pair; it does **not** find one. Exact rational arithmetic is ideal for exact claims.

```text
VERIFY_MAX_LP_CERTIFICATE(A, b, c, x, y):
    if any coordinate of x < 0 or A*x > b:
        return "invalid: proposed solution is not feasible"
    if any coordinate of y < 0 or transpose(A)*y < c:
        return "invalid: proposed weights give no universal upper bound"
    lower = dot(c, x)
    upper = dot(b, y)
    if lower == upper:
        return "optimal, with value lower"
    return "valid lower and upper bounds, but no optimality proof yet"
```

For the smoothie input, \(x=(3,3,0)\) and \(y=(5,0,2)\) pass, with lower = upper = 27.

### Pseudocode: geometric search, not an efficient LP solver

For a **bounded, nonempty** canonical feasible region, every optimum occurs at a vertex, so exhaustive vertex enumeration is conceptually valid. Include \(-x_i\le0\) in the list of constraints. The exhaustive search may require exponentially many combinations and should not be mistaken for the polynomial-time LP theorem.

```text
ENUMERATE_VERTICES_FOR_BOUNDED_LP(A, b, c):
    constraints = rows of (A*x <= b) plus rows of (-I*x <= 0)
    best_value = -infinity
    best_point = NONE
    for each selection of n constraints:
        form the n-by-n system B*x = d using their tight equalities
        if B is singular: continue
        solve B*x = d
        if x satisfies all constraints and dot(c, x) > best_value:
            best_point = x
            best_value = dot(c, x)
    return best_point, best_value
```

A rational-input LP can instead be solved in time polynomial in its **total binary encoding length**, reporting infeasibility or unboundedness or returning an exact rational optimum when finite. At a vertex, independent tight constraints give \(Bx=d\), and Cramer's rule writes each coordinate as a ratio of determinants; this helps explain why an exact basic optimal solution has polynomially many bits. It does **not** justify enumerating all vertices. For example, \(B=2^r\) takes only \(r+1\) bits to encode, whereas an \(O(nB)\) dynamic program is pseudo-polynomial in the magnitude \(B\). [file:1]

## 6. Quiz: check your understanding

Attempt these without looking at the answers below.

1. In \(\max c^{\mathsf T}x\) subject to \(Ax\le b,x\ge0\), what dimensions must \(A,b,c,x\) have?
2. Why does the feasible smoothie point \((3,3,0)\) not *by itself* prove optimality?
3. At \((3,3,0)\), what are the orange, banana, and strawberry slack values?
4. Convert \(3z\ge6\) to a \(\le\) inequality. How would you represent a free \(z\)?
5. State why two feasible LP points have a feasible midpoint.
6. List the three vertices of the triangle \(x_1+x_2\le5,x_1\ge1,x_2\ge0\). Which maximizes \(2x_1+3x_2\)?
7. True or false: An unbounded feasible region always has an unbounded objective. Give an example if false.
8. For the smoothie model, check whether \(y=(5,0,2)\) satisfies \(A^{\mathsf T}y\ge c\). Why does that matter?
9. True or false: A point in \(\mathbb R^3\) with three tight constraints must be a vertex.
10. Why does an \(O(nB)\) algorithm with a binary-encoded capacity \(B\) need not be polynomial-time in input length?

### Quiz answers

1. \(A:m\times n\), \(b:m\times1\), \(c:n\times1\), \(x:n\times1\).
2. It gives only a feasible value (a lower bound of 27); an upper bound is also needed.
3. \((0,1,0)\).
4. \(-3z\le-6\); write \(z=z^+-z^-\) with \(z^+,z^-\ge0\).
5. For midpoint \((x+y)/2\), linear inequalities average and remain \(\le b\); nonnegativity remains true.
6. \((1,0),(5,0),(1,4)\); \((1,4)\) wins with value 14.
7. False: maximize \(-x\) over \(x\ge0\); maximum 0 at \(x=0\).
8. \(A^{\mathsf T}y=(5,4,7)^{\mathsf T}\ge(5,4,6)^{\mathsf T}=c\), so 27 is a universal upper bound.
9. False; their normal vectors must be linearly independent.
10. \(B=2^r\) uses only \(r+1\) bits, but \(O(nB)=O(n2^r)\) grows exponentially with \(r\).

## 7. Exam-style problems with solutions

### Problem A: Formulation and optimality certificate (12 points)

A lab makes assays A and B. Each batch of A uses 2 reagent units and 1 instrument-hour and earns 6 points. Each batch of B uses 1 reagent unit and 2 instrument-hours and earns 6 points. Available: 6 reagent units and 6 instrument-hours. Batches are divisible.

1. Write the canonical LP.
2. Exhibit a feasible solution with objective 24.
3. Prove it is optimal using a weighted sum of constraints.

**Solution.** Let \(a,b\ge0\) be batch amounts:

\[
\max 6a+6b\quad\text{s.t.}\quad 2a+b\le6,\quad a+2b\le6,\quad a,b\ge0.
\]

\((a,b)=(2,2)\) consumes 6 of each resource and earns 24. Add both resource constraints: \(3a+3b\le12\); multiply by 2 to obtain \(6a+6b\le24\). The feasible point matches the upper bound, so it is optimal. The example is a mathematical exercise, not an operational lab recommendation.

### Problem B: Geometry and alternate optima (12 points)

For \(P=\{(x_1,x_2):x_1+x_2\le5,\ x_1\ge1,\ x_2\ge0\}\):

1. Identify all vertices and two independent tight constraints at each.
2. Find the optimum of \(\max(x_1+x_2)\) and describe *all* optimizers.
3. Explain why listing one maximizing point does not show uniqueness.

**Solution.** The vertices and tight constraints are \((1,0):x_1=1,x_2=0\); \((5,0):x_1+x_2=5,x_2=0\); and \((1,4):x_1=1,x_1+x_2=5\). The constraint \(x_1+x_2\le5\) gives upper bound 5. Every point \((t,5-t)\) with \(1\le t\le5\) is feasible and achieves 5, so the *whole sloped edge* is optimal. A single maximizing vertex can coexist with infinitely many other optimal points.

### Problem C: Fractional-coordinate bound (14 points)

An LP in \(n\) variables has \(0\le x_i\le1\) and only \(k\) other inequalities. Prove that every vertex has at most \(k\) coordinates satisfying \(0<x_i<1\).

**Solution.** Suppose \(r\) coordinates are fractional. Their lower and upper box inequalities are both *not tight*. Each of the other \(n-r\) coordinates can supply at most one independent tight box normal (at 0 or 1). Thus box constraints provide rank at most \(n-r\), and the \(k\) additional inequalities contribute rank at most \(k\). A vertex needs tight-constraint rank \(n\). Hence \(n\le(n-r)+k\), giving \(r\le k\). This is a useful reason why LP relaxations with few coupling constraints may have nearly integral vertices. [file:1]

### Problem D: Flow modeling and complexity (12 points)

A network has edges \(s\to a\) of capacity 3, \(s\to t\) of capacity 1, and \(a\to t\) of capacity 2. Formulate its flow LP, find a maximum flow, and give an upper-bound certificate without invoking a flow algorithm.

**Solution.** Let \(p=f_{sa},q=f_{st},r=f_{at}\). Maximize \(p+q\) subject to \(p=r\), \(0\le p\le3\), \(0\le q\le1\), and \(0\le r\le2\). Set \((p,q,r)=(2,1,2)\) for flow value 3. Every feasible flow satisfies \(p+q=r+q\le2+1=3\). This matching upper bound certifies optimality. It also illustrates the LP idea: feasible construction below, universal bound above. [file:1]

## 8. Textbook reading path

- **Best match for this lecture:** Dimitris Bertsimas and John N. Tsitsiklis, *Introduction to Linear Optimization* (Athena Scientific, 1997): Chapter 1 for formulations; Chapter 2, especially §§2.1–2.6, for convex polyhedra, vertices, and extreme-point optimality; Chapter 4, especially §§4.1–4.4, for upper bounds and duality; Chapter 7 for network flows; and Chapter 8 for LP complexity. MIT OpenCourseWare maps these chapters to its optimization course readings. [web:9][web:10]
- **Alternative LP-focused treatment:** Robert J. Vanderbei, *Linear Programming: Foundations and Extensions*: Chapters 1–3 for introduction, simplex, and degeneracy; Chapter 5 for duality; Chapter 10 for convex analysis; Chapter 14 for network flow problems (chapter numbers follow the cited catalog's table of contents; check your edition). [web:5]

**Suggested order:** Work through Lecture 9 and the quiz; read Bertsimas–Tsitsiklis Chapters 1–2; revisit the certificate and then read Chapter 4; use Chapter 7 when reviewing max flow and Chapter 8 when distinguishing encoding length from numeric magnitude. [file:1][web:9][web:10]
