# Finite-Horizon MDP Analysis and Reward Perturbation Bounds

## 1. Solving the Small MDP (Horizon T = 2)

### 1.1 Problem Setup
Consider an MDP defined by:
- State space: $\mathcal{S} = \{S_1, S_2, S_3, S_4\}$
- Action space: $\mathcal{A} = \{a_1, a_2\}$
- Horizon: $T = 2$ actions are taken starting from state $s_0 = S_1$.
- Rewards per action pulled:
  - $R(S_1, a) = 0$ for all $a \in \{a_1, a_2\}$
  - $R(S_2, a) = 0$ for all $a \in \{a_1, a_2\}$
  - $R(S_3, a) = 10$ for all $a \in \{a_1, a_2\}$
  - $R(S_4, a) = 100$ for all $a \in \{a_1, a_2\}$

- Transition dynamics $P(s' \mid s, a)$:
  - From $S_1$:
    - Action $a_1$: transitions to $S_1$ with probability $0.2$, and to $S_2$ with probability $0.8$.
    - Action $a_2$: transitions to $S_3$ with probability $1.0$.
  - From $S_2$:
    - Action $a_1$: transitions to $S_4$ with probability $1.0$.
    - Action $a_2$: transitions to $S_3$ with probability $1.0$.
  - From $S_3$:
    - Both actions lead to $S_3$ with probability $1.0$.
  - From $S_4$:
    - Both actions lead to $S_4$ with probability $1.0$.

---

### 1.2 Backward Induction (Finite Horizon Dynamic Programming)

For a finite horizon $T=2$, let $V_t^*(s)$ denote the optimal expected return from time step $t$ onward, where $t \in \{1, 2\}$, and $V_3^*(s) = 0$ for all $s \in \mathcal{S}$ because no further actions remain after step 2.

#### Step $t = 2$ (Last Action)
At the final step, the agent chooses an action to maximize the immediate reward:
$$V_2^*(s) = \max_{a \in \mathcal{A}} R(s, a)$$

- For $S_1$: $V_2^*(S_1) = \max \{0, 0\} = 0$ (actions $a_1, a_2$ are equivalent).
- For $S_2$: $V_2^*(S_2) = \max \{0, 0\} = 0$ (actions $a_1, a_2$ are equivalent).
- For $S_3$: $V_2^*(S_3) = \max \{10, 10\} = 10$ (actions $a_1, a_2$ are equivalent).
- For $S_4$: $V_2^*(S_4) = \max \{100, 100\} = 100$ (actions $a_1, a_2$ are equivalent).

#### Step $t = 1$ (First Action, starting at $S_1$)
At step 1, the value function is given by:
$$Q_1(S_1, a) = R(S_1, a) + \sum_{s' \in \mathcal{S}} P(s' \mid S_1, a) V_2^*(s')$$

- Evaluating action $a_1$:
  $$Q_1(S_1, a_1) = R(S_1, a_1) + 0.2 \cdot V_2^*(S_1) + 0.8 \cdot V_2^*(S_2) = 0 + 0.2(0) + 0.8(0) = 0$$

- Evaluating action $a_2$:
  $$Q_1(S_1, a_2) = R(S_1, a_2) + 1.0 \cdot V_2^*(S_3) = 0 + 1.0(10) = 10$$

### 1.3 Conclusion and Intuition
- **Optimal Policy**: Choose $a_2$ at step 1. At step 2, the agent is in state $S_3$; choose either action $a_1$ or $a_2$.
- **Optimal Expected Total Reward**: $10$.
- **Why action $a_1$ is sub-optimal**: Although taking $a_1$ at $S_1$ and then $a_1$ at $S_2$ reaches the high-value state $S_4$, the agent arrives at $S_4$ after taking the second action. Because the horizon is limited to $T=2$ actions, no action can ever be pulled from $S_4$. The zero-reward states $S_1$ and $S_2$ consume both action opportunities, yielding total reward $0$. In contrast, choosing $a_2$ immediately transitions to $S_3$ after step 1, enabling the agent to pull an action from $S_3$ at step 2 and collect a reward of $10$.

---

## 2. MDPs with Approximate Rewards

### 2.1 Problem Formulation
Let $M = (\mathcal{S}, \mathcal{A}, P, r, T)$ be the original MDP and $\widehat M = (\mathcal{S}, \mathcal{A}, P, \widehat r, T)$ be the perturbed MDP.
- Transition dynamics $P(s' \mid s, a)$ are identical in both MDPs.
- For all $s \in \mathcal{S}$ and $a \in \mathcal{A}$:
  $$|r_a(s) - \widehat r_a(s)| \le \epsilon$$
- Horizon is $T < \infty$.
- Let $\mathrm{OPT} = V^{\pi^*}(s_0)$ be the optimal expected cumulative reward in $M$.
- Let $\widehat\pi$ be an optimal policy for $\widehat M$.

### 2.2 Trajectory Representation and Uniform Approximation Lemma

Any policy $\pi$ (deterministic, stochastic, Markovian, or history-dependent) defines a probability distribution $P^\pi$ over action-state trajectories:
$$\tau = (s_1, a_1, s_2, a_2, \dots, s_T, a_T)$$
Because transition dynamics $P(s_{t+1} \mid s_t, a_t)$ and the policy decision rules $\pi(a_t \mid \dots)$ are identical in both $M$ and $\widehat M$, the trajectory distribution $P^\pi$ is identical in both MDPs.

The expected total reward of policy $\pi$ in $M$ and $\widehat M$ are:
$$V^\pi(s_0) = \mathbb{E}_{\tau \sim P^\pi}\left[\sum_{t=1}^T r_{a_t}(s_t)\right]$$
$$\widehat V^\pi(s_0) = \mathbb{E}_{\tau \sim P^\pi}\left[\sum_{t=1}^T \widehat r_{a_t}(s_t)\right]$$

#### Lemma: Uniform Value Bound
For any policy $\pi$:
$$|V^\pi(s_0) - \widehat V^\pi(s_0)| \le T\epsilon$$

*Proof:*
$$\begin{aligned}
|V^\pi(s_0) - \widehat V^\pi(s_0)| &= \left|\mathbb{E}_{\tau \sim P^\pi}\left[\sum_{t=1}^T (r_{a_t}(s_t) - \widehat r_{a_t}(s_t))\right]\right| \\
&\le \mathbb{E}_{\tau \sim P^\pi}\left[\sum_{t=1}^T |r_{a_t}(s_t) - \widehat r_{a_t}(s_t)|\right] \\
&\le \mathbb{E}_{\tau \sim P^\pi}\left[\sum_{t=1}^T \epsilon\right] \\
&= T\epsilon.
\end{aligned}$$
This immediately gives two inequalities valid for every policy $\pi$:
1. $V^\pi(s_0) \ge \widehat V^\pi(s_0) - T\epsilon$
2. $\widehat V^\pi(s_0) \ge V^\pi(s_0) - T\epsilon$

---

### 2.3 Proof of the Performance Guarantee

Let $\pi^*$ denote an optimal policy for the original MDP $M$, so $V^{\pi^*}(s_0) = \mathrm{OPT}$.
Because $\widehat\pi$ is optimal in $\widehat M$, its value in $\widehat M$ is at least as large as any other policy's value in $\widehat M$:
$$\widehat V^{\widehat\pi}(s_0) \ge \widehat V^{\pi^*}(s_0)$$

We chain the inequalities as follows:
$$\begin{aligned}
V^{\widehat\pi}(s_0) &\ge \widehat V^{\widehat\pi}(s_0) - T\epsilon && \text{(by Lemma applied to policy } \widehat\pi \text{)} \\
&\ge \widehat V^{\pi^*}(s_0) - T\epsilon && \text{(by optimality of } \widehat\pi \text{ in } \widehat M \text{)} \\
&\ge (V^{\pi^*}(s_0) - T\epsilon) - T\epsilon && \text{(by Lemma applied to policy } \pi^* \text{)} \\
&= V^{\pi^*}(s_0) - 2T\epsilon \\
&= \mathrm{OPT} - 2T\epsilon.
\end{aligned}$$
Thus, following $\widehat\pi$ in the original MDP achieves expected total reward at least $\mathrm{OPT} - 2T\epsilon$. $\blacksquare$

---

### 2.4 Concrete Numerical Example of Tightness

Consider an MDP with 1 state $S$, horizon $T$, and 2 actions:
- Action $a_1$: true reward $r(a_1) = \epsilon$, approximate reward $\widehat r(a_1) = 0$.
- Action $a_2$: true reward $r(a_2) = 0$, approximate reward $\widehat r(a_2) = \epsilon$.

Both satisfy $|r - \widehat r| = \epsilon$.
- In the original MDP, optimal action is $a_1$ with return $\mathrm{OPT} = T \cdot \epsilon$.
- In the approximate MDP, optimal policy chooses $a_2$ (since $\widehat r(a_2) = \epsilon > 0$).
- When $\widehat\pi$ is executed in the original MDP, it collects $r(a_2) = 0$ at each step, yielding total return $0$.
- Notice that $\mathrm{OPT} - 2T\epsilon = T\epsilon - 2T\epsilon = -T\epsilon \le 0$. If action $a_2$ had true reward $-\epsilon$ and approximate reward $0$, while $a_1$ had true reward $\epsilon$ and approximate reward $0$, the gap would exactly match $2T\epsilon$.
