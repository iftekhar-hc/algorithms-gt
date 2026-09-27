# Linear Programming and Maximum Flow

This guide introduces **linear programming**, followed by **maximum flow** as an important graph optimization problem that can itself be formulated as a linear program. It develops both topics through mathematical models, worked examples, geometric and network visualizations, and pseudocode.

## Table of Contents

1. [Linear Programming](#1-linear-programming)
2. [A Linear Programming Example](#2-a-linear-programming-example)
3. [Visualizing the Objective Function](#3-visualizing-the-objective-function)
4. [Important LP Concepts](#4-important-lp-concepts)
5. [Linear Programming Duality](#5-linear-programming-duality)
6. [Maximum Flow](#6-maximum-flow)
7. [Flow Constraints](#7-flow-constraints)
8. [Worked Maximum-Flow Example](#8-worked-maximum-flow-example)
9. [Maximum Flow as a Linear Program](#9-maximum-flow-as-a-linear-program)
10. [Cuts in a Flow Network](#10-cuts-in-a-flow-network)
11. [Max-Flow Min-Cut Theorem](#11-max-flow-min-cut-theorem)
12. [Residual Networks](#12-residual-networks)
13. [Ford-Fulkerson Method](#13-ford-fulkerson-method)
14. [Edmonds-Karp Algorithm](#14-edmonds-karp-algorithm)
15. [Extracting a Minimum Cut](#15-extracting-a-minimum-cut-from-the-final-residual-graph)
16. [LP and Maximum Flow](#16-lp-and-maximum-flow-the-main-connection)
17. [Path-Based LP Formulation](#17-path-based-lp-formulation)
18. [Detailed Augmenting-Path Example](#18-a-more-detailed-augmenting-path-example)
19. [When to Use LP Versus a Flow Algorithm](#19-when-to-use-general-lp-versus-a-flow-algorithm)
20. [Key Takeaways](#20-key-takeaways)

---

## 1. Linear Programming

### 1.1 What is linear programming?

**Linear programming**, or **LP**, optimizes a linear objective function subject to linear equality and inequality constraints.

A common standard form is:

$$
\begin{aligned}
\text{maximize} \quad & c^T x \\
\text{subject to} \quad & Ax \le b, \\
& x \ge 0,
\end{aligned}
$$

where:

- $x \in \mathbb{R}^n$ is the vector of **decision variables**.
- $c \in \mathbb{R}^n$ contains the objective-function coefficients.
- $A \in \mathbb{R}^{m\times n}$ contains the constraint coefficients.
- $b \in \mathbb{R}^m$ contains the resource limits.

The set of points satisfying all constraints is the **feasible region**. Because the constraints are linear, this region is a convex polyhedron, or a polygon in two dimensions.

If a bounded LP has an optimal solution, at least one optimum occurs at a vertex of its feasible region.

### 1.2 Why must everything be linear?

An expression is linear if its variables:

- Appear only to the first power.
- Are not multiplied by one another.
- Do not appear inside nonlinear functions.

#### Linear expressions

$$
3x+5y
$$

$$
2x-y\le 8
$$

#### Nonlinear expressions

$$
xy, \qquad x^2, \qquad \sqrt{x}, \qquad \log x
$$

For example,

$$
\max 4x+3y
$$

is linear, but

$$
\max 4xy
$$

is not.

---

## 2. A Linear Programming Example

Suppose a factory produces two products:

- $x$: number of units of product $X$.
- $y$: number of units of product $Y$.

The profit is:

- $\$3$ per unit of $X$.
- $\$5$ per unit of $Y$.

The factory has two resource constraints:

$$
x+y\le 4
$$

$$
x+3y\le 6
$$

Production cannot be negative:

$$
x\ge 0, \qquad y\ge 0.
$$

The LP is therefore:

$$
\begin{aligned}
\text{maximize} \quad & z=3x+5y \\
\text{subject to} \quad
&x+y\le 4,\\
&x+3y\le 6,\\
&x,y\ge 0.
\end{aligned}
$$

### 2.1 Geometric interpretation

Each inequality defines a half-plane. The intersection of all the half-planes gives the feasible region.

```text
y
^
| 2       B = (0,2)
| *--------\
| |         \
| |          * C = (3,1)
| |           \
| |            \
| *-------------*------> x
| A = (0,0)     D = (4,0)
+----------------------------
```

A conceptual view is:

```text
                 x + 3y = 6
                    \
                     \
           feasible  \
            region    * (3,1)
              #######/ \
              ######/   \  x + y = 4
              #####/
              ####/
              *----------------*
            (0,0)             (4,0)
```

The vertices are:

$$
(0,0), \qquad (0,2), \qquad (3,1), \qquad (4,0).
$$

The point $(3,1)$ comes from solving the two binding constraints:

$$
x+y=4
$$

$$
x+3y=6.
$$

Subtracting the first equation from the second gives:

$$
2y=2 \implies y=1.
$$

Therefore,

$$
x=4-y=3.
$$

### 2.2 Evaluate the objective at every vertex

| Vertex | Objective value $3x+5y$ |
|---|---:|
| $(0,0)$ | $0$ |
| $(0,2)$ | $10$ |
| $(3,1)$ | $14$ |
| $(4,0)$ | $12$ |

Thus, the optimal solution is:

$$
\boxed{x=3, \qquad y=1}
$$

with maximum profit:

$$
\boxed{z^*=14}.
$$

This illustrates the **corner-point principle**: for a bounded feasible polyhedron, an optimal linear objective can be attained at a vertex.

---

## 3. Visualizing the Objective Function

The objective function

$$
3x+5y=z
$$

defines a family of parallel lines:

$$
y=-\frac{3}{5}x+\frac{z}{5}.
$$

Increasing $z$ shifts the line upward and to the right.

```text
                larger objective
                       /
        3x + 5y = 15
              /
             /   3x + 5y = 14
            /        * optimum
           /        /
          /        /  3x + 5y = 10
         /        /
        *--------*
```

The last objective line that still touches the feasible region reaches the vertex $(3,1)$.

That geometric movement is the intuitive meaning of maximizing a linear function over a polygon.

---

## 4. Important LP Concepts

### 4.1 Feasible solution

A **feasible solution** is a point satisfying every constraint.

For example, $(1,1)$ is feasible because:

$$
1+1\le 4
$$

and

$$
1+3(1)\le 6.
$$

### 4.2 Infeasible solution

An **infeasible solution** violates at least one constraint.

For example, $(3,2)$ is infeasible because:

$$
3+3(2)=9>6.
$$

### 4.3 Binding constraint

A constraint is **binding** at a solution if it holds with equality.

At $(3,1)$:

$$
3+1=4
$$

and

$$
3+3(1)=6.
$$

Therefore, both resource constraints are binding.

### 4.4 Slack

For a constraint

$$
a^Tx\le b,
$$

its slack is:

$$
b-a^Tx.
$$

At the feasible point $(1,1)$:

$$
\operatorname{slack}_1=4-(1+1)=2,
$$

$$
\operatorname{slack}_2=6-(1+3)=2.
$$

At the optimum $(3,1)$, both slacks are zero.

### 4.5 Possible LP outcomes

An LP may be:

1. **Optimal:** It has a finite best solution.
2. **Infeasible:** No point satisfies all constraints.
3. **Unbounded:** The objective can improve indefinitely.
4. **Multiply optimal:** An entire edge or face contains optimal solutions.

---

## 5. Linear Programming Duality

Every LP has a closely related optimization problem called its **dual**.

Consider the primal LP:

$$
\begin{aligned}
\text{maximize} \quad & c^Tx\\
\text{subject to} \quad & Ax\le b,\\
&x\ge 0.
\end{aligned}
$$

Its dual is:

$$
\begin{aligned}
\text{minimize} \quad & b^Ty\\
\text{subject to} \quad & A^Ty\ge c,\\
&y\ge 0.
\end{aligned}
$$

The dual variables can often be interpreted as **resource prices** or **shadow prices**.

### 5.1 Weak duality

For every primal-feasible $x$ and dual-feasible $y$:

$$
c^Tx\le b^Ty.
$$

Thus:

- Every dual-feasible solution gives an upper bound on a maximization LP.
- Every primal-feasible solution gives a lower bound on a minimization dual.

### 5.2 Strong duality

When feasible optimal solutions exist:

$$
\boxed{c^Tx^*=b^Ty^*}.
$$

This becomes especially important for maximum flow:

$$
\boxed{\text{maximum flow value}=\text{minimum cut capacity}}.
$$

---

## 6. Maximum Flow

### 6.1 Problem definition

A **flow network** is a directed graph

$$
G=(V,E)
$$

with:

- A source vertex $s$.
- A sink vertex $t$.
- A capacity $c(u,v)\ge 0$ on every edge $(u,v)$.

A flow assigns a value

$$
f(u,v)
$$

to each edge.

The goal is to send as much flow as possible from $s$ to $t$, without exceeding capacities and without accumulating flow at intermediate vertices.

Typical interpretations include:

- Water through pipes.
- Packets through communication links.
- Vehicles through roads.
- Products through a supply network.
- Tasks through a matching network.

---

## 7. Flow Constraints

A feasible flow must satisfy two main conditions.

### 7.1 Capacity constraint

For every edge $(u,v)$:

$$
0\le f(u,v)\le c(u,v).
$$

The flow cannot be negative or exceed the edge capacity.

### 7.2 Flow conservation

For every intermediate vertex

$$
v\in V\setminus\{s,t\},
$$

the incoming flow must equal the outgoing flow:

$$
\sum_{u:(u,v)\in E} f(u,v)
=
\sum_{w:(v,w)\in E} f(v,w).
$$

In words:

$$
\boxed{\text{flow into }v=\text{flow out of }v}.
$$

### 7.3 Value of a flow

Assuming no edges enter the source, the flow value can be written as:

$$
|f|=\sum_{v:(s,v)\in E} f(s,v).
$$

More generally:

$$
|f|
=
\sum_v f(s,v)-\sum_u f(u,s).
$$

The amount leaving the source equals the amount entering the sink.

---

## 8. Worked Maximum-Flow Example

Consider this network:

```text
              3             2
         s --------> a ----------> t
          \           |
           \          | 1
          2\          v
             -------> b ----------> t
                         3
```

The capacities are:

$$
c(s,a)=3, \qquad c(s,b)=2,
$$

$$
c(a,t)=2, \qquad c(b,t)=3,
$$

and

$$
c(a,b)=1.
$$

### 8.1 Constructing a flow

Send:

$$
f(s,a)=3.
$$

Of these three units, send:

$$
f(a,t)=2,
$$

and send the remaining unit through:

$$
f(a,b)=1.
$$

Also send:

$$
f(s,b)=2.
$$

Vertex $b$ receives $2+1=3$ units, so send:

$$
f(b,t)=3.
$$

The resulting flow is:

```text
            3/3              2/2
       s ----------> a ------------> t
        \             |
         \            | 1/1
        2/2           v
           ---------> b ------------> t
                           3/3
```

Each edge label has the form:

$$
\text{flow}/\text{capacity}.
$$

The flow value is:

$$
|f|=f(s,a)+f(s,b)=3+2=5.
$$

Therefore:

$$
\boxed{|f|=5}.
$$

### 8.2 Why can the flow not exceed 5?

The total capacity leaving $s$ is:

$$
c(s,a)+c(s,b)=3+2=5.
$$

Therefore, no flow can have value greater than $5$:

$$
|f|\le 5.
$$

Because we constructed a feasible flow of value $5$:

$$
\boxed{\text{maximum flow}=5}.
$$

This gives both:

- A feasible lower bound of $5$, from the constructed flow.
- An upper bound of $5$, from the capacity leaving $s$.

Since the bounds match, the flow is optimal.

---

## 9. Maximum Flow as a Linear Program

Introduce one decision variable $f_{uv}$ for each directed edge $(u,v)$. Also introduce a variable $F$, representing the total flow value.

The objective is:

$$
\text{maximize} \quad F.
$$

Subject to edge capacities:

$$
0\le f_{uv}\le c_{uv}
\qquad \forall (u,v)\in E,
$$

flow conservation at intermediate vertices:

$$
\sum_{u:(u,v)\in E}f_{uv}
-
\sum_{w:(v,w)\in E}f_{vw}
=0
\qquad
\forall v\in V\setminus\{s,t\},
$$

source balance:

$$
\sum_{v:(s,v)\in E}f_{sv}
-
\sum_{u:(u,s)\in E}f_{us}
=F,
$$

and sink balance:

$$
\sum_{u:(u,t)\in E}f_{ut}
-
\sum_{v:(t,v)\in E}f_{tv}
=F.
$$

Everything is linear, so this is a linear program.

### 9.1 LP for the worked example

The variables are:

$$
f_{sa},f_{sb},f_{ab},f_{at},f_{bt}.
$$

The LP is:

$$
\text{maximize} \quad F
$$

subject to:

$$
f_{sa}+f_{sb}=F,
$$

$$
f_{sa}=f_{at}+f_{ab},
$$

$$
f_{sb}+f_{ab}=f_{bt},
$$

$$
f_{at}+f_{bt}=F,
$$

and:

$$
0\le f_{sa}\le 3,
$$

$$
0\le f_{sb}\le 2,
$$

$$
0\le f_{ab}\le 1,
$$

$$
0\le f_{at}\le 2,
$$

$$
0\le f_{bt}\le 3.
$$

An optimal LP solution is:

$$
f_{sa}=3,\quad
f_{sb}=2,\quad
f_{ab}=1,\quad
f_{at}=2,\quad
f_{bt}=3,
$$

with:

$$
\boxed{F=5}.
$$

---

## 10. Cuts in a Flow Network

An $s$-$t$ cut partitions the vertices into two sets:

$$
S\subseteq V, \qquad T=V\setminus S,
$$

such that:

$$
s\in S, \qquad t\in T.
$$

The capacity of the cut is:

$$
c(S,T)
=
\sum_{\substack{u\in S\\v\in T\\(u,v)\in E}}
c(u,v).
$$

Only edges directed from $S$ to $T$ contribute to the cut capacity.

### 10.1 Cut visualization

For the earlier network, choose:

$$
S=\{s\}, \qquad T=\{a,b,t\}.
$$

```text
            S                 T

        +-------+       +----------------+
        |       |  3    | a ----------> t|
        |   s   |------>|                |
        |       |  2    | b ----------> t|
        |       |------>|                |
        +-------+       +----------------+
```

The cut capacity is:

$$
c(S,T)=c(s,a)+c(s,b)=3+2=5.
$$

Any flow from $s$ to $t$ must cross this cut, so:

$$
|f|\le c(S,T)=5.
$$

---

## 11. Max-Flow Min-Cut Theorem

The central theorem is:

$$
\boxed{
\max_f |f|
=
\min_{\substack{S\subseteq V\\s\in S,\;t\notin S}}
c(S,V\setminus S)
}.
$$

In words:

> The maximum amount of flow that can be sent from $s$ to $t$ equals the capacity of the smallest $s$-$t$ cut.

For every feasible flow and every cut:

$$
|f|\le c(S,T).
$$

This resembles weak LP duality. The deeper result is that some maximum flow and minimum cut attain equality.

For the worked example:

$$
\text{maximum flow}=5
$$

and

$$
\text{minimum cut capacity}=5.
$$

Therefore:

$$
\boxed{\text{max flow}=\text{min cut}=5}.
$$

---

## 12. Residual Networks

A greedy approach that uses only unused forward capacity can make poor choices. A **residual network** allows an algorithm to undo or redirect previously assigned flow.

For an edge $(u,v)$, the forward residual capacity is:

$$
c_f(u,v)=c(u,v)-f(u,v).
$$

If $f(u,v)>0$, the residual graph also contains a reverse edge with capacity:

$$
c_f(v,u)=f(u,v).
$$

Thus:

- A forward residual edge means that more flow can be sent.
- A reverse residual edge means that some previously assigned flow can be canceled.

Residual reverse edges allow an augmenting-path algorithm to recover from an earlier routing choice.

### 12.1 Residual-edge example

Suppose an edge has capacity $7$ and currently carries $4$ units:

$$
f(u,v)=4, \qquad c(u,v)=7.
$$

The residual capacities are:

$$
c_f(u,v)=7-4=3,
$$

$$
c_f(v,u)=4.
$$

```text
Original flow:

u -------- 4/7 --------> v

Residual graph:

u -------- 3 --------> v
u <------- 4 --------- v
```

We may:

- Send up to $3$ more units from $u$ to $v$.
- Cancel up to $4$ units by sending residual flow from $v$ to $u$.

---

## 13. Ford-Fulkerson Method

The **Ford-Fulkerson method** repeatedly finds an augmenting path from $s$ to $t$ in the residual graph.

For an augmenting path $P$, define its bottleneck residual capacity:

$$
\Delta
=
\min_{(u,v)\in P}c_f(u,v).
$$

Then augment the flow by $\Delta$ along the entire path.

### Pseudocode

```text
FORD-FULKERSON(G, s, t, capacity):
    set flow on every edge to 0

    while there is an s-to-t path P in the residual graph:
        delta = minimum residual capacity on P

        for each residual edge (u, v) in P:
            if (u, v) is an original edge:
                flow[u, v] = flow[u, v] + delta
            else:
                flow[v, u] = flow[v, u] - delta

    return flow
```

A feasible flow is maximum exactly when its residual graph contains no augmenting path.

---

## 14. Edmonds-Karp Algorithm

Ford-Fulkerson does not specify how to select the augmenting path. **Edmonds-Karp** always selects an augmenting path having the fewest edges by using breadth-first search.

```text
EDMONDS-KARP(G, s, t, capacity):
    initialize all flows to 0

    while BFS finds an s-to-t path P
          in the residual graph:

        delta = minimum residual capacity on P

        augment the flow by delta along P

    return flow
```

Its running time is:

$$
O(VE^2).
$$

This is polynomial in the number of vertices and edges.

---

## 15. Extracting a Minimum Cut from the Final Residual Graph

After a maximum-flow algorithm terminates:

1. Start at $s$.
2. Run DFS or BFS using only residual edges with positive capacity.
3. Let $S$ be the set of reachable vertices.
4. Let $T=V\setminus S$.

Then $(S,T)$ is a minimum cut.

```text
Final residual graph:

           reachable                 unreachable
        +-------------+          +----------------+
        |             |          |                |
        | s ...       |    X     | ... t          |
        |             |          |                |
        +-------------+          +----------------+
                 no positive-residual edge
                    crosses from S to T
```

If there were a positive-residual path from $s$ to $t$, the flow could still be augmented. Therefore, when the algorithm stops, $t$ is unreachable from $s$ in the residual graph.

This reachability partition produces a cut that certifies optimality.

---

## 16. LP and Maximum Flow: The Main Connection

Maximum flow is a special, highly structured LP.

| Linear programming concept | Maximum-flow interpretation |
|---|---|
| Decision variable | Flow $f(u,v)$ on an edge |
| Linear objective | Maximize total flow $F$ |
| Inequality constraint | Edge-capacity limit |
| Equality constraint | Flow conservation |
| Primal-feasible solution | Valid network flow |
| Dual bound | Capacity of an $s$-$t$ cut |
| Primal optimum | Maximum flow |
| Dual optimum | Minimum cut |
| Strong duality | Max-flow min-cut theorem |

There is also an important integrality property:

> If every edge capacity is an integer, then a maximum flow exists in which every edge carries an integer amount of flow.

Although the flow problem is written as a continuous LP, its network structure allows an integral optimum when capacities are integral.

---

## 17. Path-Based LP Formulation

There is another way to formulate maximum flow.

Let $\mathcal P$ be the set of all $s$-$t$ paths, and define:

$$
x_P=\text{amount of flow routed along path }P.
$$

Then:

$$
\begin{aligned}
\text{maximize} \quad
&\sum_{P\in\mathcal P}x_P\\
\text{subject to} \quad
&\sum_{\substack{P\in\mathcal P\\e\in P}}x_P
\le c_e
&&\forall e\in E,\\
&x_P\ge 0
&&\forall P\in\mathcal P.
\end{aligned}
$$

The constraint for edge $e$ says that the total flow assigned to paths using $e$ cannot exceed the capacity of $e$.

This formulation removes explicit flow-conservation constraints because each variable already represents a complete $s$-$t$ path. Its disadvantage is that a graph may contain exponentially many paths.

---

## 18. A More Detailed Augmenting-Path Example

Consider:

```text
              4              3
        s ----------> a ----------> t
        |             |             ^
        |             | 2           |
      3 |             v             | 4
        +-----------> b ------------+
```

Capacities:

$$
c(s,a)=4, \quad c(s,b)=3,
$$

$$
c(a,b)=2, \quad c(a,t)=3, \quad c(b,t)=4.
$$

### 18.1 Augmentation 1

Choose:

$$
s\to a\to t.
$$

The bottleneck is:

$$
\min(4,3)=3.
$$

Send $3$ units:

```text
s --3/4--> a --3/3--> t
```

Current flow value:

$$
|f|=3.
$$

### 18.2 Augmentation 2

Choose:

$$
s\to b\to t.
$$

The bottleneck is:

$$
\min(3,4)=3.
$$

Send $3$ units:

```text
s --3/3--> b --3/4--> t
```

Current flow value:

$$
|f|=6.
$$

### 18.3 Augmentation 3

The remaining path is:

$$
s\to a\to b\to t.
$$

Its residual capacities are:

$$
1, \quad 2, \quad 1.
$$

Therefore:

$$
\Delta=\min(1,2,1)=1.
$$

The final flow value is:

$$
|f|=7.
$$

The completed flow is:

```text
              4/4            3/3
        s ----------> a ----------> t
        |             |             ^
        |             | 1/2         |
      3/3             v             | 4/4
        +-----------> b ------------+
```

Since the total outgoing capacity of $s$ is:

$$
4+3=7,
$$

no flow can exceed $7$. Hence:

$$
\boxed{\text{maximum flow}=7}.
$$

---

## 19. When to Use General LP Versus a Flow Algorithm

Use a dedicated maximum-flow algorithm when the problem contains only:

- One source.
- One sink.
- Edge capacities.
- Ordinary flow conservation.
- A maximum-throughput objective.

Use a general LP solver when the model includes additional linear conditions such as:

- Production costs.
- Budget constraints.
- Fairness conditions.
- Resource sharing among several networks.
- Side constraints connecting unrelated edges.
- Required minimum or maximum allocation percentages.

For example:

$$
f(a,b)\le 2f(c,d)
$$

is linear and can be added to an LP, but a standard maximum-flow algorithm does not directly handle this cross-edge constraint.

---

## 20. Key Takeaways

### Linear programming

$$
\boxed{\text{Optimize a linear objective over linear constraints}}
$$

The basic geometry is:

```text
linear constraints
        |
        v
convex feasible polyhedron
        |
        v
best objective value attained at a boundary point
        |
        v
an optimal vertex exists under standard bounded conditions
```

### Maximum flow

$$
\boxed{\text{Send as much flow as possible from }s\text{ to }t}
$$

subject to:

$$
0\le f(u,v)\le c(u,v)
$$

and:

$$
\text{inflow}=\text{outflow}
$$

at intermediate vertices.

### Central optimality relationship

$$
\boxed{\text{maximum flow}=\text{minimum cut capacity}}
$$

A maximum flow gives a feasible solution, while a minimum cut gives an upper-bound certificate. When their values match, optimality is proven.

### Algorithmic insight

Residual graphs make it possible to:

- Identify unused capacity.
- Reverse earlier decisions.
- Find augmenting paths.
- Construct a minimum cut after termination.

### Suggested mental model

Think of LP as the general mathematical language:

$$
\text{variables}+\text{linear constraints}+\text{linear objective}.
$$

Think of maximum flow as one elegant sentence written in that language:

$$
\text{maximize throughput while respecting capacities and conservation}.
$$
