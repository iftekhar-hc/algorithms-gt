# Divide & Conquer Problem Set 1

**CS 6515/4540 - Fall 2026**

**Due:** Thursday, September 3  
**Submission:** Gradescope

Your solution must be a typed PDF (for example, created with LaTeX). No handwritten solutions.

## 1. O-Notation

### 1.1 LLM Question

Use the following prompt in an LLM, such as ChatGPT, Copilot, or Gemini, and upload the transcript of your session:

> Act like an undergrad with a CS major who wants to understand Big O notation. Now interactively ask me 5 questions (i.e., one by one while waiting for my answers) to improve your (and my) understanding of Big O. In the end, give me all the correct answers and constructive feedback.

### 1.2 Question

We are interested in finding *all* constants for which the following $O(\cdot)$ bounds hold.

1. For which constants $c, d > 0$ do we have
   $$
   n^c = O(d^n)?
   $$
   Prove your answer.

2. For which constants $c, d > 0$ do we have
   $$
   (\log n)^c = O(n^d)?
   $$
   Prove your answer.

> **Remark:** $c$ and $d$ do not need to be integers. In particular, they could be smaller than 1.

## 2. Divide & Conquer Algorithm

Given a length-$n$ array $A$ containing only non-negative entries, construct an algorithm that returns the maximum possible product of contiguous entries.

For example, when

$$
A = [0.5, 2, 0.25, 2, 0.75, 2, 0.5],
$$

the maximum product is $3$, obtained from the subarray

$$
[2, 0.75, 2].
$$

### Problem

Construct a divide-and-conquer algorithm `MaxProduct(A[1...n])` that solves the problem above. Your answer must provide the following:

1. **Pseudocode description** of your algorithm.

2. **Correctness argument.** You may provide a proof by induction, but answering the following questions suffices:

   1. Why is the base case correct when $A$ has length 1?
   2. Why does the algorithm return the correct answer if it has the solutions for the left and right halves of the array, that is,
      $$
      \operatorname{MaxProduct}(A[1...n/2])
      $$
      and
      $$
      \operatorname{MaxProduct}(A[n/2 + 1,...,n])?
      $$

3. **Complexity analysis**, using, for example, the tree method, induction, or a bound from class.

> **Requirement:** Iterative algorithms exist for this problem, but the purpose of this exercise is to practice divide and conquer. Your solution must recursively split $A[1...n]$ into $A[1...n/2]$ and $A[n/2 + 1...n]$. For full credit, your solution should be as fast as possible.

## 3. Median of Medians

The standard median-of-medians algorithm uses groups of five. Instead, consider a median-of-medians algorithm with groups of $M \ge 3$.

1. Give the recurrence for this algorithm, in terms of $M$, to calculate its worst-case runtime.

2. Suppose $M = 7$. Solve the recurrence by induction. Clearly state the following:

   - Induction hypothesis
   - Base case
   - Induction step

3. Which statement is true about the running time of the algorithm in part 2 for $M = 7$, compared with $M = 5$ from class?

   1. The running time improves to $o(n)$.
   2. The running time stays $\Theta(n)$.
   3. The running time worsens to $\omega(n)$.

   Briefly explain your choice.
