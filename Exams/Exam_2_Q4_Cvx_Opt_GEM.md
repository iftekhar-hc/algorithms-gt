# Study Guide: Question 4 — Convex Optimization & Gradient Descent
**Course:** CS 6515 / 4540 (Practice Exam 2 — Section 4: Convex Optimization, 20 Points)

---

## 1. The Exam Problem Statement (Question 4)

> **Definition 1 (Strong Convexity):** A differentiable $f$ is $\alpha$-strongly convex, for $\alpha > 0$, if for all $x, y \in \mathbb{R}^d$,
> $$f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle + \frac{\alpha}{2} \|y - x\|^2.$$
> Consider an $\alpha$-strongly convex and $\beta$-smooth function $f : \mathbb{R}^d \to \mathbb{R}$ with a global minimum at some $x^* \in \mathbb{R}^d$. We run gradient descent with no constraints (no projection) on $f$ beginning from some point $x_0$, with step size $\eta = \frac{1}{\beta}$. Let $x_k \in \mathbb{R}^d$ be the iterate after $k$ steps:
> $$x_{k+1} = x_k - \frac{1}{\beta} \nabla f(x_k).$$
> 1. **(8 points)** Using the definition of $\beta$-smoothness and step size $\eta = 1/\beta$, show that
>    $$\frac{1}{2\beta} \|\nabla f(x_k)\|^2 \le f(x_k) - f(x_{k+1}).$$
> 2. **(6 points)** For any $\alpha$-strongly convex function $f$ with global minimum at $x^*$, it can be shown that
>    $$\|\nabla f(x_k)\|^2 \ge 2\alpha \big(f(x_k) - f(x^*)\big).$$
>    Assuming this and part 1, prove that
>    $$f(x_{k+1}) - f(x^*) \le \left(1 - \frac{\alpha}{\beta}\right) \big(f(x_k) - f(x^*)\big).$$
> 3. **(6 points)** Using the results above show that for any $k \ge 0$
>    $$f(x_k) - f(x^*) \le \left(1 - \frac{\alpha}{\beta}\right)^k \big(f(x_0) - f(x^*)\big),$$
>    i.e., gradient descent on $\alpha$-strongly convex and $\beta$-smooth functions converges exponentially fast.

---

## 2. Core Concepts & Geometric Intuition

### 2.1 Vectors, Inner Products, and Gradient Norms
Before diving into convexity, keep these essential vector identities on your exam cheat sheet:
- **Gradient $\nabla f(x) \in \mathbb{R}^d$:** Points in the direction of **steepest ascent** of $f$ at $x$. Its negative, $-\nabla f(x)$, points in the direction of **steepest descent**.
- **At the global minimum $x^*$ (unconstrained):** $\nabla f(x^*) = 0$.
- **Inner Product and Squared Euclidean Norm Identity:** For any vector $v \in \mathbb{R}^d$, the inner product of $v$ with itself equals its squared norm:
  $$\langle v, v \rangle = \|v\|^2.$$
- **Scaling Inside a Norm:** For any scalar $c \in \mathbb{R}$ and vector $v \in \mathbb{R}^d$:
  $$\|c \cdot v\|^2 = c^2 \|v\|^2.$$
  *(For example, $\left\| -\frac{1}{\beta} \nabla f(x_k) \right\|^2 = \frac{1}{\beta^2} \|\nabla f(x_k)\|^2$. This identity is the heart of Part 1!)*

---

### 2.2 Convexity vs. $\alpha$-Strong Convexity vs. $\beta$-Smoothness

Think of the first-order Taylor approximation (tangent hyperplane) of $f$ at $x$:
$$L_x(y) = f(x) + \langle \nabla f(x), y - x \rangle.$$

| Property | Mathematical Definition ($\forall x, y \in \mathbb{R}^d$) | Geometric Meaning |1D Second-Derivative View ($f''(x)$) |
| :--- | :--- | :--- | :--- |
| **Convex** | $f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle$ | $f$ lies **above** its tangent line. | $f''(x) \ge 0$ |
| **$\alpha$-Strongly Convex** ($\alpha > 0$) | $f(y) \ge f(x) + \langle \nabla f(x), y - x \rangle + \frac{\alpha}{2}\|y - x\|^2$ | $f$ lies **above a upward parabola** of curvature $\alpha$. (Cannot be too flat!) | $f''(x) \ge \alpha > 0$ |
| **$\beta$-Smooth** ($\beta > 0$) | $f(y) \le f(x) + \langle \nabla f(x), y - x \rangle + \frac{\beta}{2}\|y - x\|^2$ | $f$ lies **below an upward parabola** of curvature $\beta$. (Cannot curve up too sharply!) | $f''(x) \le \beta$ *(for convex $f$)* |

#### The "Quadratic Sandwich" Picture
When $f$ is **both $\alpha$-strongly convex and $\beta$-smooth**, at every point $x$, the function $f(y)$ is sandwiched between two quadratics:
$$f(x) + \langle \nabla f(x), y - x \rangle + \frac{\alpha}{2} \|y - x\|^2 \;\le\; f(y) \;\le\; f(x) + \langle \nabla f(x), y - x \rangle + \frac{\beta}{2} \|y - x\|^2.$$

- **Important Fact:** Because the lower bound must be $\le$ the upper bound for all $y \ne x$, we **always have $\alpha \le \beta$**, so $0 < \frac{\alpha}{\beta} \le 1$ and $0 \le 1 - \frac{\alpha}{\beta} < 1$.
- **Why do we need BOTH properties for fast Gradient Descent?**
  1. **$\beta$-Smoothness (Upper Bound)** guarantees the gradient doesn't change too wildly ($\|\nabla f(y) - \nabla f(x)\| \le \beta \|y - x\|$). This tells us how large a step size $\eta = 1/\beta$ we can safely take while **guaranteeing $f$ decreases** at every step (Part 1).
  2. **$\alpha$-Strong Convexity (Lower Bound)** guarantees the function doesn't get "too flat" before reaching $x^*$. Specifically, if $f(x_k)$ is still far above $f(x^*)$, the gradient $\|\nabla f(x_k)\|^2$ must still be large (Part 2).

---

### 2.3 Step Size $\eta$ and Gradient Descent Convergence
The Gradient Descent update rule with step size $\eta > 0$ is:
$$x_{k+1} = x_k - \eta \nabla f(x_k) \quad \Longleftrightarrow \quad x_{k+1} - x_k = -\eta \nabla f(x_k).$$

Plugging $x = x_k$ and $y = x_{k+1}$ into the $\beta$-smoothness inequality gives:
$$\begin{aligned}
f(x_{k+1}) &\le f(x_k) + \langle \nabla f(x_k), -\eta \nabla f(x_k) \rangle + \frac{\beta}{2} \|-\eta \nabla f(x_k)\|^2 \\
&= f(x_k) - \eta \|\nabla f(x_k)\|^2 + \frac{\beta \eta^2}{2} \|\nabla f(x_k)\|^2 \\
&= f(x_k) - \eta \left(1 - \frac{\beta \eta}{2}\right) \|\nabla f(x_k)\|^2.
\end{aligned}$$

Look closely at the factor $\eta \left(1 - \frac{\beta \eta}{2}\right)$:
- **If $\eta = \frac{1}{\beta}$ (Optimal Step Size for the Upper Bound):**
  The factor $\eta \left(1 - \frac{\beta \eta}{2}\right)$ achieves its **maximum possible value** of $\frac{1}{2\beta}$, guaranteeing the largest guaranteed drop in $f$:
  $$f(x_{k+1}) \le f(x_k) - \frac{1}{2\beta} \|\nabla f(x_k)\|^2.$$
- **If $\eta \ge \frac{2}{\beta}$ (Step Size Too Large!):**
  Then $1 - \frac{\beta \eta}{2} \le 0$, so $f(x_{k+1})$ can **overshoot** and actually **increase** ($f(x_{k+1}) > f(x_k)$), diverging to $\infty$!
  *(Connection to Short Answer Q1.4: "When running gradient descent on a $\beta$-smooth, convex function, we will converge to the optimum regardless of step size or initial point chosen" is **FALSE** because if the step size $\eta > 2/\beta$ is too large, GD can oscillate or diverge—e.g., on $f(x) = \frac{\beta}{2}x^2$ with $\eta = 3/\beta$, $x_{k+1} = -2x_k$, which blows up!)*

---

### 2.4 Bonus Intuition: Where Does $\|\nabla f(x_k)\|^2 \ge 2\alpha(f(x_k) - f(x^*))$ Come From?
*(Note: Part 2 gives you this inequality for free, so you don't have to prove it on the exam! However, knowing why it's true deepens your understanding.)*

Take the $\alpha$-strong convexity inequality at $x = x_k$:
$$f(y) \ge f(x_k) + \langle \nabla f(x_k), y - x_k \rangle + \frac{\alpha}{2} \|y - x_k\|^2.$$
Minimize both sides over $y \in \mathbb{R}^d$:
- The minimum of the LHS over $y$ is $f(x^*)$.
- The RHS is a simple quadratic in $y$, whose minimum occurs when its gradient w.r.t. $y$ is zero: $\nabla f(x_k) + \alpha(y - x_k) = 0 \implies y - x_k = -\frac{1}{\alpha}\nabla f(x_k)$.
- Plugging that $y$ into the RHS gives:
  $$f(x^*) \ge f(x_k) - \frac{1}{\alpha}\|\nabla f(x_k)\|^2 + \frac{\alpha}{2} \cdot \frac{1}{\alpha^2}\|\nabla f(x_k)\|^2 = f(x_k) - \frac{1}{2\alpha}\|\nabla f(x_k)\|^2.$$
- Rearranging yields $\|\nabla f(x_k)\|^2 \ge 2\alpha(f(x_k) - f(x^*))$!

---

## 3. Step-by-Step Walkthrough & Model Exam Solutions

### Part 1 (8 points): Prove $\frac{1}{2\beta} \|\nabla f(x_k)\|^2 \le f(x_k) - f(x_{k+1})$

#### Strategy:
1. Write down the definition of **$\beta$-smoothness** with $x = x_k$ and $y = x_{k+1}$.
2. Substitute the gradient descent update $x_{k+1} - x_k = -\frac{1}{\beta} \nabla f(x_k)$.
3. Simplify the inner product and squared norm, then rearrange!

> **Model Exam Solution (Part 1):**
> By the definition of $\beta$-smoothness applied at $x = x_k$ and $y = x_{k+1}$:
> $$f(x_{k+1}) \le f(x_k) + \langle \nabla f(x_k), x_{k+1} - x_k \rangle + \frac{\beta}{2} \|x_{k+1} - x_k\|^2.$$
> Since $x_{k+1} = x_k - \frac{1}{\beta}\nabla f(x_k)$, we have $x_{k+1} - x_k = -\frac{1}{\beta}\nabla f(x_k)$. Substituting this in:
> $$\begin{aligned}
> f(x_{k+1}) &\le f(x_k) + \left\langle \nabla f(x_k), -\frac{1}{\beta}\nabla f(x_k) \right\rangle + \frac{\beta}{2} \left\| -\frac{1}{\beta}\nabla f(x_k) \right\|^2 \\
> &= f(x_k) - \frac{1}{\beta} \|\nabla f(x_k)\|^2 + \frac{\beta}{2} \cdot \frac{1}{\beta^2} \|\nabla f(x_k)\|^2 \\
> &= f(x_k) - \frac{1}{\beta} \|\nabla f(x_k)\|^2 + \frac{1}{2\beta} \|\nabla f(x_k)\|^2 \\
> &= f(x_k) - \frac{1}{2\beta} \|\nabla f(x_k)\|^2.
> \end{aligned}$$
> Rearranging terms yields:
> $$\frac{1}{2\beta} \|\nabla f(x_k)\|^2 \le f(x_k) - f(x_{k+1}). \quad \blacksquare$$

---

### Part 2 (6 points): Prove $f(x_{k+1}) - f(x^*) \le \left(1 - \frac{\alpha}{\beta}\right) \big(f(x_k) - f(x^*)\big)$

#### Strategy:
1. Chain the inequality from Part 1 with the given inequality $\|\nabla f(x_k)\|^2 \ge 2\alpha(f(x_k) - f(x^*))$.
2. Use the standard algebra trick of **subtracting $f(x^*)$** (or rewriting $f(x_k) - f(x_{k+1}) = [f(x_k) - f(x^*)] - [f(x_{k+1}) - f(x^*)]$) to get $f(x_{k+1}) - f(x^*)$ on the LHS and $f(x_k) - f(x^*)$ on the RHS!

> **Model Exam Solution (Part 2):**
> From Part 1, we know that:
> $$f(x_{k+1}) \le f(x_k) - \frac{1}{2\beta} \|\nabla f(x_k)\|^2.$$
> Using the given inequality $\|\nabla f(x_k)\|^2 \ge 2\alpha\big(f(x_k) - f(x^*)\big)$ (and dividing by $-2\beta < 0$, which flips the inequality):
> $$-\frac{1}{2\beta} \|\nabla f(x_k)\|^2 \le -\frac{2\alpha}{2\beta} \big(f(x_k) - f(x^*)\big) = -\frac{\alpha}{\beta} \big(f(x_k) - f(x^*)\big).$$
> Substituting this into the Part 1 bound gives:
> $$f(x_{k+1}) \le f(x_k) - \frac{\alpha}{\beta} \big(f(x_k) - f(x^*)\big).$$
> Subtracting $f(x^*)$ from both sides:
> $$\begin{aligned}
> f(x_{k+1}) - f(x^*) &\le \big(f(x_k) - f(x^*)\big) - \frac{\alpha}{\beta} \big(f(x_k) - f(x^*)\big) \\
> &= \left(1 - \frac{\alpha}{\beta}\right) \big(f(x_k) - f(x^*)\big). \quad \blacksquare
> \end{aligned}$$

---

### Part 3 (6 points): Prove $f(x_k) - f(x^*) \le \left(1 - \frac{\alpha}{\beta}\right)^k \big(f(x_0) - f(x^*)\big)$

#### Strategy:
Apply Part 2 repeatedly (by unrolling the recurrence from $k$ down to $0$, or by induction on $k$). Also note that $1 - \frac{\alpha}{\beta} \ge 0$ since $\alpha \le \beta$.

> **Model Exam Solution (Part 3):**
> We prove the claim by induction on $k \ge 0$ (or by repeatedly applying Part 2):
> - **Base case ($k = 0$):** $f(x_0) - f(x^*) \le \left(1 - \frac{\alpha}{\beta}\right)^0 (f(x_0) - f(x^*)) = f(x_0) - f(x^*)$, which holds with equality.
> - **Inductive step:** Suppose the inequality holds for $k-1$. Applying Part 2 at step $k-1$ (and noting $1 - \frac{\alpha}{\beta} \ge 0$ since $\alpha \le \beta$):
>   $$\begin{aligned}
>   f(x_k) - f(x^*) &\le \left(1 - \frac{\alpha}{\beta}\right) \big(f(x_{k-1}) - f(x^*)\big) \\
>   &\le \left(1 - \frac{\alpha}{\beta}\right) \left(1 - \frac{\alpha}{\beta}\right)^{k-1} \big(f(x_0) - f(x^*)\big) \\
>   &= \left(1 - \frac{\alpha}{\beta}\right)^k \big(f(x_0) - f(x^*)\big). \quad \blacksquare
>   \end{aligned}$$

---

## 4. Iteration Complexity: How Many Steps to Reach Error $\epsilon$?

Sometimes a follow-up question asks: *"How many iterations $k$ are needed so that $f(x_k) - f(x^*) \le \epsilon$?"*
Using the standard inequality $1 - x \le e^{-x}$ (valid for all $x \in \mathbb{R}$):
$$f(x_k) - f(x^*) \le \left(1 - \frac{\alpha}{\beta}\right)^k \big(f(x_0) - f(x^*)\big) \le e^{-(\alpha/\beta) k} \big(f(x_0) - f(x^*)\big).$$
Setting the RHS $\le \epsilon$ and taking $\ln$:
$$k \ge \frac{\beta}{\alpha} \ln\left(\frac{f(x_0) - f(x^*)}{\epsilon}\right) = O\left(\frac{\beta}{\alpha} \log \frac{1}{\epsilon}\right).$$
- Notice that $k$ depends only **logarithmically** on $1/\epsilon$! In optimization, $O(\log(1/\epsilon))$ is called **linear convergence** (or **exponentially fast convergence** because the error decays exponentially in $k$).
- By contrast, if $f$ is only convex and $\beta$-smooth (i.e., $\alpha = 0$, not strongly convex), gradient descent takes $O\left(\frac{\beta \|x_0 - x^*\|^2}{\epsilon}\right) = O(1/\epsilon)$ steps, which is exponentially slower in $\epsilon$ (see **Short Answer Q1.5**, where LP objectives are linear, so $\alpha = 0$ and GD only gives $O(1/\epsilon)$ pseudo-polynomial dependence rather than polynomial time in $\log(1/\epsilon)$!).

---

## 5. Self-Assessment Questions

Test your understanding with these questions:

1. **Memorizing the $\beta$-Smoothness Formula:** Notice that the exam gives you the formula for $\alpha$-strong convexity in Definition 1, but expects you to know the formula for **$\beta$-smoothness** from memory in Part 1! How can you immediately write down the $\beta$-smoothness inequality just by looking at Definition 1 on the exam page?
2. **Sign Flip Carefulness:** In Part 2, we had $f(x_{k+1}) \le f(x_k) - \frac{1}{2\beta}\|\nabla f(x_k)\|^2$ and $\|\nabla f(x_k)\|^2 \ge 2\alpha(f(x_k) - f(x^*))$. Why is it valid to replace $\|\nabla f(x_k)\|^2$ with $2\alpha(f(x_k) - f(x^*))$ and keep the $\le$ sign? What mistake do students often make if the inequality goes the wrong way?
3. **Different Step Size Variation:** Suppose on the actual exam, they use step size $\eta = \frac{1}{2\beta}$ instead of $\eta = \frac{1}{\beta}$, so $x_{k+1} = x_k - \frac{1}{2\beta}\nabla f(x_k)$. What constant replaces $\frac{1}{2\beta}$ in Part 1?
4. **Relationship Between $\alpha$ and $\beta$:** Can a function ever be $\alpha$-strongly convex and $\beta$-smooth with $\alpha = 5$ and $\beta = 2$? Why or why not?
5. **Short Answer Q1.4 & Q1.5 Connection:**
   - Why is Short Answer Q1.4 (*"GD on a $\beta$-smooth convex function converges regardless of step size"*) **False**?
   - Why is Short Answer Q1.5 (*"We can run GD to solve LPs in polynomial time"*) **False**?
