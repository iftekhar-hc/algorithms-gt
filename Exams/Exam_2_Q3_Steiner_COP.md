# Question 2 (Matching) - Complete Study Guide

## Topics Covered

1. Graphs and Matchings
2. Maximum Matching
3. LP Formulation
4. LP Relaxation
5. Integrality Gap
6. Duality
7. Bipartite Graphs
8. Vertex Cover Connection
9. Self-Test Questions

---

# 1. What is a Matching?

Given a graph

$$
G=(V,E)
$$

a **matching** is a set of edges such that no two selected edges share a vertex.

Example:

```text
A ----- B
|       |
|       |
D ----- C
```

Edges:

$$
E=\{AB,BC,CD,DA\}
$$

A matching could be

$$
M=\{AB,CD\}
$$

since those two edges do not touch.

The size of the matching is

$$
|M|=2.
$$

---

# 2. Maximum Matching

The maximum matching problem asks:

> Select as many pairwise-disjoint edges as possible.

Example:

```text
A --- B --- C --- D
```

Maximum matching:

$$
\{AB,CD\}
$$

with size

$$
2.
$$

---

# 3. Integer LP Formulation of Maximum Matching

Introduce one variable per edge:

$$
x_e=
\begin{cases}
1 & \text{if edge } e \text{ is selected}\\
0 & \text{otherwise}
\end{cases}
$$

Objective:

$$
\max \sum_{e\in E} x_e
$$

Matching constraint:

For every vertex \(v\), at most one incident edge can be chosen.

$$
\sum_{e\in \delta(v)} x_e \le 1
$$

where

$$
\delta(v)
$$

is the set of edges incident to vertex \(v\).

The integer program becomes:

$$
\begin{aligned}
\max \quad & \sum_{e\in E} x_e \\
\text{s.t.}\quad
& \sum_{e\in\delta(v)} x_e \le 1
&& \forall v\\
& x_e \in \{0,1\}
&& \forall e
\end{aligned}
$$

---

# 4. LP Relaxation

Relax the integrality constraints:

$$
\begin{aligned}
\max \quad & \sum_{e\in E} x_e\\
\text{s.t.}\quad
&\sum_{e\in\delta(v)}x_e\le1
&&\forall v\\
&x_e\ge0
&&\forall e
\end{aligned}
$$

Now fractional values such as

$$
x_e=0.5
$$

are allowed.

---

# Why LP Relaxation Gives an Upper Bound

Every matching corresponds to a feasible LP solution.

Define

$$
x_e=
\begin{cases}
1 & e\in M\\
0 & e\notin M
\end{cases}
$$

for a matching \(M\).

Since no vertex is incident to more than one selected edge,

$$
\sum_{e\in\delta(v)}x_e\le1.
$$

Thus every integer solution is also LP-feasible.

Since the LP has a larger feasible region,

$$
\text{LP optimum}
\ge
\text{integer optimum}.
$$

---

# Part (a): Proof

Let \(M\) be a maximum matching.

Set

$$
x_e=
\begin{cases}
1 & e\in M\\
0 & e\notin M
\end{cases}
$$

This is feasible for the LP.

The objective value is

$$
\sum_e x_e = |M|.
$$

Since the LP optimum is at least the value of every feasible LP solution,

$$
\text{LP optimum}
\ge
|M|.
$$

Hence the LP value is at least the maximum matching size.

---

# 5. Bipartite Graphs

A graph is **bipartite** if the vertices can be partitioned into two sets

$$
L,R
$$

such that every edge connects a vertex in \(L\) to a vertex in \(R\).

Example:

```text
L1 ----- R1
 |
 |
 R2
```

No edge joins two vertices within the same side.

---

# Why Bipartite Graphs Matter

For bipartite graphs,

$$
\text{LP optimum}
=
\text{Maximum Matching}.
$$

The LP relaxation is integral.

Therefore there is **no integrality gap**.

---

# 6. Non-Bipartite Graphs and Integrality Gap

In general graphs, the LP may have fractional optimal solutions.

The smallest example is a triangle.

```text
    A
   / \
  /   \
 B-----C
```

Edges:

$$
AB,BC,CA.
$$

---

# Maximum Matching in a Triangle

Any two edges share a vertex.

Therefore only one edge can be selected.

Maximum matching size:

$$
1.
$$

---

# Fractional LP Solution

Assign

$$
x_{AB}=x_{BC}=x_{CA}=\frac12.
$$

At every vertex:

$$
\frac12+\frac12=1.
$$

Therefore all constraints are satisfied.

The objective value is

$$
\frac12+\frac12+\frac12
=
\frac32.
$$

Thus

$$
\text{LP optimum}
\ge
1.5.
$$

while

$$
\text{Maximum Matching}=1.
$$

Hence the LP is strictly better than the integer optimum.

---

# Integrality Gap

The integrality gap is

$$
\frac{\text{LP value}}{\text{Integer value}}
=
\frac{3/2}{1}
=
1.5.
$$

---

# Geometric Intuition

Integer solutions are:

$$
(1,0,0),
(0,1,0),
(0,0,1).
$$

The LP also allows

$$
\left(\frac12,\frac12,\frac12\right),
$$

which is not a true matching.

---

# 7. LP Duality Review

For a primal LP of the form

$$
\begin{aligned}
\max &\quad c^T x\\
\text{s.t.}&\quad Ax\le b\\
&\quad x\ge0
\end{aligned}
$$

its dual is

$$
\begin{aligned}
\min &\quad b^T y\\
\text{s.t.}&\quad A^T y\ge c\\
&\quad y\ge0.
\end{aligned}
$$

---

# 8. Deriving the Dual

Primal:

$$
\begin{aligned}
\max &\sum_{e\in E}x_e\\
\text{s.t.}
&\sum_{e\in\delta(v)}x_e\le1
&&\forall v\\
&x_e\ge0
&&\forall e
\end{aligned}
$$

Introduce one dual variable

$$
y_v\ge0
$$

for each vertex constraint.

---

# Dual Objective

The right-hand side of every constraint is 1.

Therefore:

$$
\min
\sum_{v\in V} y_v.
$$

---

# Dual Constraints

Consider an edge

$$
e=(u,v).
$$

The variable \(x_e\) appears in exactly two vertex constraints:

- vertex \(u\)
- vertex \(v\)

Therefore the corresponding dual constraint is

$$
y_u+y_v\ge1.
$$

---

# Final Dual LP

$$
\boxed{
\begin{aligned}
\min\quad &\sum_{v\in V}y_v\\
\text{s.t.}\quad
&y_u+y_v\ge1
&&\forall (u,v)\in E\\
&y_v\ge0
&&\forall v
\end{aligned}}
$$

---

# 9. Interpretation of the Dual

The integer version is

$$
y_v\in\{0,1\}.
$$

The constraint

$$
y_u+y_v\ge1
$$

means every edge must have at least one endpoint selected.

This is exactly the **Minimum Vertex Cover** problem.

Thus:

- Matching = packing edges
- Vertex Cover = covering edges

---

# Strong Duality Example

For the triangle:

Primal:

$$
x_{AB}=x_{BC}=x_{CA}=\frac12.
$$

Objective:

$$
1.5.
$$

Dual:

$$
y_A=y_B=y_C=\frac12.
$$

Every constraint satisfies

$$
\frac12+\frac12=1.
$$

Dual objective:

$$
\frac12+\frac12+\frac12=1.5.
$$

Primal value equals dual value.

---

# 10. Fundamental Bipartite Matching Theorem

For bipartite graphs:

$$
\boxed{
\text{Maximum Matching}
=
\text{Minimum Vertex Cover}
}
$$

This is **Kőnig's Theorem**.

Consequently, the LP relaxation is integral.

---

# Key Facts to Memorize

## Matching LP

$$
\max \sum_e x_e
$$

subject to

$$
\sum_{e\in\delta(v)}x_e\le1.
$$

---

## LP Relaxation Fact

$$
\text{LP optimum}
\ge
\text{Integer optimum}.
$$

---

## Integrality Gap Example

Triangle:

$$
\text{Maximum Matching}=1
$$

$$
\text{LP Value}=1.5
$$

---

## Dual LP

$$
\min\sum_v y_v
$$

subject to

$$
y_u+y_v\ge1.
$$

---

## Bipartite Graph Property

$$
\text{Maximum Matching}
=
\text{Minimum Vertex Cover}.
$$

---

# Self-Test Questions

## Basic

1. What does \(\delta(v)\) mean?
2. Why can't two edges in a matching share a vertex?
3. Why does every integer matching correspond to a feasible LP solution?

## LP Relaxation

4. Why can the LP optimum never be smaller than the integer optimum?
5. What extra solutions become possible after relaxation?
6. Give a fractional feasible solution for a triangle.

## Integrality Gap

7. What is the maximum matching size of a triangle?
8. What LP value results if every edge is assigned \(1/2\)?
9. Why does this demonstrate an integrality gap?

## Duality

10. Why is there one dual variable per vertex?
11. Why does edge \((u,v)\) generate the constraint

$$
y_u+y_v\ge1?
$$

12. What combinatorial problem does the dual represent?

## Advanced Understanding

13. Why does the triangle create an integrality gap while a path graph does not?
14. What property of bipartite graphs eliminates the integrality gap?
15. How can the LP be strengthened to exactly characterize matching in general graphs?

**Answer:** Add the odd-set (blossom) constraints.
