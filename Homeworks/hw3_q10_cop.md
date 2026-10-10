# Solving Alice's Fruit-Bundle Problem with Linear Programming

This problem is a **covering linear program**: Alice must satisfy minimum fruit requirements while minimizing cost. Because fractional bundles are allowed, the decision variables can be any nonnegative real numbers rather than integers.

---

## 1. Formulate the linear program

### Step 1: Define the decision variables

Let

$$
x_A = \text{number of Bundle A units purchased},
$$

and

$$
x_B = \text{number of Bundle B units purchased}.
$$

Fractional bundles are permitted, so

$$
x_A,x_B\in \mathbb{R}_{\ge 0}.
$$

### Step 2: Write the fruit constraints

The contents of the bundles are:

| Bundle | Oranges | Bananas | Cost |
|---|---:|---:|---:|
| A | 1 | 2 | $3 |
| B | 3 | 1 | $2 |

#### Orange requirement

Alice receives

$$
x_A+3x_B
$$

oranges. She needs at least 8, so

$$
x_A+3x_B\ge 8.
$$

#### Banana requirement

Alice receives

$$
2x_A+x_B
$$

bananas. She needs at least 20, so

$$
2x_A+x_B\ge 20.
$$

### Step 3: Write the objective function

Bundle A costs $3 and Bundle B costs $2. Therefore, Alice's total cost is

$$
3x_A+2x_B.
$$

She wants to minimize this amount.

### Complete linear program

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

### Why is this the correct LP?

- The objective $3x_A+2x_B$ is exactly the amount Alice spends.
- The first constraint guarantees at least 8 oranges.
- The second constraint guarantees at least 20 bananas.
- The nonnegativity constraints prohibit buying negative bundles.
- Since fractional bundles are allowed, $x_A$ and $x_B$ do not have to be integers.

---

## 2. Find a feasible solution costing $30

A natural place to begin is with only Bundle A:

$$
x_A=10,\qquad x_B=0.
$$

Let us check this solution carefully.

### Oranges

$$
x_A+3x_B=10+3(0)=10.
$$

Because

$$
10\ge 8,
$$

the orange requirement is satisfied.

### Bananas

$$
2x_A+x_B=2(10)+0=20.
$$

Because

$$
20\ge 20,
$$

the banana requirement is satisfied exactly.

### Cost

$$
3x_A+2x_B=3(10)+2(0)=30.
$$

Thus,

$$
(x_A,x_B)=(10,0)
$$

is feasible and has objective value

$$
\boxed{30}.
$$

Therefore, the optimal cost, denoted by $\mathrm{OPT}$, cannot be greater than 30:

$$
\boxed{\mathrm{OPT}\le 30}.
$$

This is an **upper bound** on the minimum cost because we have exhibited a concrete way for Alice to spend $30 successfully.

---

## 3. Prove that every feasible solution costs at least $30

Finding a feasible solution costing $30 does not by itself prove optimality. There could, in principle, be another feasible solution costing $29 or $25.

We therefore need a **lower bound** that applies to every feasible solution.

### The key banana constraint

Every feasible solution satisfies

$$
2x_A+x_B\ge 20.
$$

Multiply this constraint by the nonnegative number $\frac32$:

$$
\frac32(2x_A+x_B)\ge \frac32(20).
$$

This gives

$$
3x_A+\frac32x_B\ge 30.
$$

We want the left side to become the objective function

$$
3x_A+2x_B.
$$

The coefficient of $x_B$ is currently $\frac32$, so we need an additional $\frac12x_B$. Because $x_B\ge 0$, multiplying the nonnegativity constraint by $\frac12$ gives

$$
\frac12x_B\ge 0.
$$

Now add the two inequalities:

$$
3x_A+\frac32x_B\ge 30,
$$

$$
\frac12x_B\ge 0.
$$

Adding them produces

$$
3x_A+2x_B\ge 30.
$$

But $3x_A+2x_B$ is exactly Alice's total cost. Therefore, every feasible solution has cost at least $30:

$$
\boxed{\mathrm{OPT}\ge 30}.
$$

Combining the two bounds,

$$
\mathrm{OPT}\le 30
$$

and

$$
\mathrm{OPT}\ge 30,
$$

we conclude that

$$
\boxed{\mathrm{OPT}=30}.
$$

The solution found earlier is therefore optimal:

$$
\boxed{x_A^*=10,\qquad x_B^*=0}.
$$

Alice should buy 10 Bundle As and no Bundle Bs.

---

## The nonnegative linear combination written compactly

The lower-bound proof can be shown as

$$
\frac32(2x_A+x_B\ge 20)
+
\frac12(x_B\ge 0).
$$

Adding the left-hand sides and right-hand sides gives

$$
3x_A+2x_B\ge 30.
$$

Thus, the objective function itself is bounded below by 30.

Notice that the coefficients in the combination,

$$
\frac32\quad\text{and}\quad\frac12,
$$

are both nonnegative. This is important because multiplying a valid inequality by a nonnegative number preserves the inequality direction.

---

## Geometric visualization

Use $x_A$ as the horizontal coordinate and $x_B$ as the vertical coordinate.

### Constraint boundaries

The orange boundary is

$$
x_A+3x_B=8,
$$

or

$$
x_B=\frac{8-x_A}{3}.
$$

Its intercepts are

$$
(8,0)
\qquad\text{and}\qquad
\left(0,\frac83\right).
$$

The banana boundary is

$$
2x_A+x_B=20,
$$

or

$$
x_B=20-2x_A.
$$

Its intercepts are

$$
(10,0)
\qquad\text{and}\qquad
(0,20).
$$

Because both inequalities use $\ge$, feasible points lie **above** both boundary lines in the first quadrant.

```text
x_B
 ^
 |       Feasible region
 |       #####################
20 B-----#####################     Banana boundary
 |  \    #####################     2x_A + x_B = 20
 |   \   #####################
 |    \  #####################
 |     \ #####################
 |      \#####################
 |       \
 |        \
8/3 O------\-------------------     Orange boundary
 |    \     \                       x_A + 3x_B = 8
 |     \     \
 |      \     \
 +-------O-----B----------------> x_A
         8     10

                    Optimal point:
                    (x_A,x_B) = (10,0)
```

The orange boundary lies below the banana boundary in the relevant first-quadrant region. Consequently, satisfying the banana constraint together with nonnegativity already provides enough oranges.

---

## Why the orange constraint is redundant

It may initially seem surprising that the lower-bound proof did not use the orange requirement. The reason is that the banana requirement is so demanding that any nonnegative bundle combination satisfying it automatically supplies at least 8 oranges.

Consider the minimum possible number of oranges subject to

$$
2x_A+x_B\ge 20,\qquad x_A,x_B\ge 0.
$$

On the boundary,

$$
x_B=20-2x_A,
$$

where

$$
0\le x_A\le 10.
$$

The number of oranges is

$$
x_A+3x_B.
$$

Substitute $x_B=20-2x_A$:

$$
\begin{aligned}
x_A+3(20-2x_A)
&=60-5x_A.
\end{aligned}
$$

For $0\le x_A\le 10$, this expression is minimized at $x_A=10$:

$$
60-5(10)=10.
$$

Thus, the banana constraint guarantees at least 10 oranges:

$$
2x_A+x_B\ge20,\quad x_A,x_B\ge0
\quad\Longrightarrow\quad
x_A+3x_B\ge10.
$$

Since $10\ge8$, the orange requirement is automatically satisfied. In this LP, the orange constraint is therefore **redundant**.

---

## An alternative view using cost per banana

Because bananas are the limiting resource, compare bundles by their cost per banana.

- Bundle A costs $3 and provides 2 bananas:

  $$
  \frac{\$3}{2}=\$1.50
  $$

  per banana.

- Bundle B costs $2 and provides 1 banana:

  $$
  \frac{\$2}{1}=\$2.00
  $$

  per banana.

Bundle A is cheaper per banana. To obtain 20 bananas using only Bundle A, Alice needs

$$
\frac{20}{2}=10
$$

Bundle As, costing

$$
10(3)=30.
$$

This explains the optimal solution intuitively. The linear-combination proof makes the intuition mathematically rigorous.

---

## Objective behavior along the banana boundary

Suppose Alice exactly satisfies the banana requirement:

$$
2x_A+x_B=20.
$$

Solving for $x_A$,

$$
x_A=\frac{20-x_B}{2}.
$$

Substitute this expression into the cost:

$$
\begin{aligned}
3x_A+2x_B
&=3\left(\frac{20-x_B}{2}\right)+2x_B\\
&=30-\frac32x_B+2x_B\\
&=30+\frac12x_B.
\end{aligned}
$$

Therefore, along the banana boundary,

$$
\boxed{\text{cost}=30+\frac12x_B}.
$$

Since $x_B\ge0$,

$$
30+\frac12x_B\ge30.
$$

Every time Alice replaces some Bundle A capacity with Bundle B capacity while maintaining exactly 20 bananas, the cost increases. The smallest cost occurs at

$$
x_B=0,
$$

which gives

$$
x_A=10.
$$

---

## Example solutions

### An infeasible solution

Consider

$$
(x_A,x_B)=(4,2).
$$

Oranges:

$$
4+3(2)=10\ge8.
$$

Bananas:

$$
2(4)+2=10<20.
$$

Although Alice has enough oranges, she does not have enough bananas. Therefore, this solution is infeasible.

### A feasible but nonoptimal solution

Consider

$$
(x_A,x_B)=(8,4).
$$

Oranges:

$$
8+3(4)=20\ge8.
$$

Bananas:

$$
2(8)+4=20\ge20.
$$

Cost:

$$
3(8)+2(4)=32.
$$

This solution is feasible, but it costs $32, which is more than the optimal cost of $30.

### Another feasible but expensive solution

Using only Bundle B requires

$$
x_B\ge20
$$

to obtain 20 bananas. Taking

$$
(x_A,x_B)=(0,20)
$$

provides 60 oranges and 20 bananas, but costs

$$
2(20)=40.
$$

It is feasible, but it overproduces oranges and costs $10 more than the optimum.

---

## Upper-bound and lower-bound proof pattern

This problem illustrates a standard LP optimality strategy.

### Step 1: Produce an upper bound

Find a feasible solution with value $C$. Then

$$
\mathrm{OPT}\le C.
$$

Here,

$$
(x_A,x_B)=(10,0)
$$

has cost 30, so

$$
\mathrm{OPT}\le30.
$$

### Step 2: Produce a lower bound

Use a nonnegative combination of valid constraints to show that every feasible solution has value at least $C$:

$$
\text{objective}\ge C.
$$

Here,

$$
3x_A+2x_B\ge30,
$$

so

$$
\mathrm{OPT}\ge30.
$$

### Step 3: Match the bounds

If

$$
\mathrm{OPT}\le C
\quad\text{and}\quad
\mathrm{OPT}\ge C,
$$

then

$$
\mathrm{OPT}=C.
$$

This is often called a **certificate of optimality**.

---

## Final answer

The LP is

$$
\boxed{
\begin{aligned}
\min\quad &3x_A+2x_B\\
\text{s.t.}\quad
&x_A+3x_B\ge8,\\
&2x_A+x_B\ge20,\\
&x_A,x_B\ge0.
\end{aligned}}
$$

The solution

$$
\boxed{(x_A,x_B)=(10,0)}
$$

is feasible and costs

$$
\boxed{\$30}.
$$

For every feasible solution,

$$
\begin{aligned}
\frac32(2x_A+x_B)&\ge30,\\
\frac12x_B&\ge0.
\end{aligned}
$$

Adding these inequalities gives

$$
3x_A+2x_B\ge30.
$$

Therefore, every feasible solution costs at least $30, and the optimal solution is

$$
\boxed{x_A^*=10,\qquad x_B^*=0,\qquad \mathrm{OPT}=\$30}.
$$
