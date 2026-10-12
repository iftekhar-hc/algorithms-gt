## 14. Convex Sets and Convex Functions
### 14.1 Unions and Intersections
For $K,L\subseteq\mathbb R^n$, $K\cap L$ must be convex.

We choose any two points $x,y\in K\cap L$. It follows that:
$$
x,y\in K \quad\text{and}\quad x,y\in L.
$$

Since $K$ is convex, for every $t\in[0,1]$, the following holds:

$$
tx+(1-t)y\in K.
$$

Since $L$ is also convex, we have:

$$
tx+(1-t)y\in L.
$$

The point $tx+(1-t)y$ belongs to both $K$ and $L$. Therefore,

$$
tx+(1-t)y\in K\cap L.
$$

This is precisely the definition of a convex set. Hence,

$$
K\cap L\text{ is convex}.
$$

On the contrary, $K\cup L$ need not be convex.

We choose two convex sets:
$$
K=[0,1],\qquad L=[2,3].
$$

Their union is

$$
K\cup L=[0,1]\cup[2,3].
$$

We calculate their midpoint as follows:

$$
\frac{x+y}{2}=\frac{0+3}{2}=1.5\notin [0,1]\cup[2,3]..
$$

Hence,

$$
K\cup L\text{ need not be convex}.
$$

### 14.2 Sum

The sum of convex functions is convex.
We define:
$$
h(x)=f(x)+g(x).
$$

We need to show that, for all $x,y\in\mathbb R$ and $t\in[0,1]$,

$$
h(tx+(1-t)y)
\leq th(x)+(1-t)h(y).
$$

The left-hand side is:

$$
\begin{aligned}
h(tx+(1-t)y)
={}&f(tx+(1-t)y)\\
&+g(tx+(1-t)y).
\end{aligned}
$$

Since $f$ is convex,

$$
f(tx+(1-t)y)
\leq tf(x)+(1-t)f(y).
$$

Since $g$ is convex,

$$
g(tx+(1-t)y)
\leq tg(x)+(1-t)g(y).
$$

Adding the above inequalities:
$$
\begin{aligned}
h(tx+(1-t)y)
&\leq tf(x)+(1-t)f(y)\\
&\quad+tg(x)+(1-t)g(y).
\end{aligned}
$$

Grouping the terms:

$$
\begin{aligned}
h(tx+(1-t)y)
&\leq t[f(x)+g(x)]\\
&\quad+(1-t)[f(y)+g(y)].
\end{aligned}
$$

Since $h=f+g$, this becomes:

$$
h(tx+(1-t)y)\leq th(x)+(1-t)h(y).
$$

which proves that $f + g$ is convex.

### 14.3 Product
The product of two convex functions need not be convex.

We consider the following two linear functions [and hence convex]:

$$
f(x)=x,\qquad g(x)=-x.
$$

We have:

$$
h(x)=f(x)g(x)=x(-x)=-x^2.
$$

We choose $x=-1$, $y=1$, and $t=\frac12$.

The midpoint is $0$, and $h(0)=0$.

For convexity, we would need:

$$
h(0)\leq\frac{h(-1)+h(1)}2 = -1.
$$

The above would require $0\leq-1$ which is not plausible.

Hence,

$$
fg\text{ need not be convex}.
$$

### 14.4 Max
Elementwise maximum of two convex functions is convex.

We choose arbitrary $x,y\in\mathbb R$ and $t\in[0,1]$.
Let

$$
z=tx+(1-t)y.
$$

We need to show that

$$
h(z)\leq th(x)+(1-t)h(y).
$$
Since $f$ is convex,

$$
f(z)\leq tf(x)+(1-t)f(y).
$$

Since $h(x) = \text{max}(f(x), g(x))$, we have:

$$
f(x)\leq h(x),\qquad f(y)\leq h(y).
$$
Because $t$ and $1-t$ are nonnegative:

$$
f(z)\leq th(x)+(1-t)h(y).
$$
Similarly, convexity of $g$ gives:

$$
g(z)\leq tg(x)+(1-t)g(y).
$$

Using $g(x)\leq h(x)$ and $g(y)\leq h(y)$,

$$
g(z)\leq th(x)+(1-t)h(y).
$$

Since both $f(z)$ and $g(z)$ are at most $th(x)+(1-t)h(y)$, their maximum is also at most that quantity.

$$
\begin{aligned}
h(z)&=\max\{f(z),g(z)\}\\
&\leq th(x)+(1-t)h(y).
\end{aligned}
$$

Substitute $z=tx+(1-t)y$:

$$
h(tx+(1-t)y)
\leq th(x)+(1-t)h(y).
$$
The above implies convexity of $h(x)$. Hence,

$$
\max\{f,g\}\text{ is convex}.
$$

