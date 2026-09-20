# CS6515 Exam 1 Study Guide

> **Coverage:** Lectures 1–8: asymptotic analysis, divide and conquer, dynamic programming, graph algorithms, matchings, and maximum flow. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/e9312164-0d70-499e-bf27-2becf865baec/Lec_1_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=KWDLfH3P9G0YhEKF0fiR5GwMqNk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## How to study

For every algorithm, practise answering:

1. What is the input and objective?
2. What invariant, state definition, or structural fact makes it work?
3. Why is it correct?
4. What is the runtime, and what operations create that cost?

A reliable exam response usually has: a precise algorithm, a correctness argument, and an explicit runtime analysis.

***

# Core Algorithmic Lenses

## Divide and conquer

**Idea:** Split a problem into smaller mostly independent subproblems, solve them recursively, then combine their solutions.

1. **Divide** the problem.
2. **Conquer** subproblems recursively.
3. **Combine** their answers.

Efficiency depends on the number and sizes of recursive calls and the work required to combine their results. Merge sort, maximum difference, and median-of-medians selection are the main examples. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/2b72ad50-6313-474a-b7bd-5cc9c170fc9e/Lec_2_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=%2FmrR%2BY2KUse5tTj2geXWJJP0q2A%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Dynamic programming

**Idea:** Store answers to overlapping subproblems rather than recomputing them.

A complete DP design includes:

1. A precise **state definition**
2. A **recurrence**
3. **Base cases**
4. An **evaluation order**
5. A way to recover an actual solution when needed

The central design question is: **What information must a subproblem remember so it can be extended correctly?** [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/eeb7c8cf-e45a-473e-aaac-44c9c6112817/Lec_3_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=lGu2ICzpashBwAjsegaz3AOmu3I%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Graph algorithms

The graph topics use recurring ideas:

- **Layers and reachability:** BFS
- **Greedy settling:** Dijkstra
- **Cuts and exchange arguments:** MST and Prim
- **Alternating paths:** matching
- **Residual networks and cuts:** maximum flow

For each graph algorithm, distinguish the method that constructs a solution from the argument or certificate that proves it is optimal. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/269b5302-2d10-4868-a47b-b8b5ccb28f10/Lec_8_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=3b4G1FlG7zxVjjxpJE3JtXn6Fw8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Asymptotic Notation

Let \(f(n)\) and \(g(n)\) describe resource growth as input size \(n\) becomes large.

- \(f(n)\in O(g(n))\): \(f\) is eventually at most a constant multiple of \(g\).
- \(f(n)\in \Omega(g(n))\): \(f\) is eventually at least a constant multiple of \(g\).
- \(f(n)\in \Theta(g(n))\): both upper and lower bounds hold.
- \(f(n)\in o(g(n))\): \(f\) grows strictly more slowly than \(g\).
- \(f(n)\in \omega(g(n))\): \(f\) grows strictly faster than \(g\). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/e9312164-0d70-499e-bf27-2becf865baec/Lec_1_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=KWDLfH3P9G0YhEKF0fiR5GwMqNk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

Useful growth ordering:

\[
1=o(\log\log n)=o(\log n)=o(n^{0.1})=o(n)=o(n^2)=o(2^n)=o(n^n)
\]

Also:

\[
n! = o(n^n)
\]

\[
\log(n!)=\Theta(n\log n)
\]

***

# Recurrences

## Recursion trees

A recursion tree counts work at every level.

For merge sort:

\[
T(n)=2T(n/2)+cn
\]

At level \(i\), there are \(2^i\) subproblems, each of size \(n/2^i\). The merge work at that level is:

\[
2^i \cdot c(n/2^i)=cn
\]

There are \(\log_2 n\) levels before reaching subproblems of size 1, giving:

\[
T(n)=\Theta(n\log n)
\]

 [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/e9312164-0d70-499e-bf27-2becf865baec/Lec_1_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=KWDLfH3P9G0YhEKF0fiR5GwMqNk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Strong induction

Use strong induction to prove recurrence bounds, especially if recursive calls have different or rounded-down sizes.

Typical proof pattern:

1. Guess a bound.
2. Verify finitely many base cases.
3. Assume the bound holds for **all smaller inputs**.
4. Substitute the induction hypothesis into recursive terms.
5. Simplify until the target bound appears.

For example, to prove linear time for a recurrence, guess:

\[
T(n)\le An
\]

Then choose \(A\) large enough to absorb the nonrecursive work. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/2b72ad50-6313-474a-b7bd-5cc9c170fc9e/Lec_2_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=%2FmrR%2BY2KUse5tTj2geXWJJP0q2A%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Master Theorem

For recurrences of the form:

\[
T(n)=aT(n/b)+n^d
\]

compare \(d\) with:

\[
\log_b a
\]

| Comparison | Result |
|---|---|
| \(d>\log_b a\) | \(\Theta(n^d)\) |
| \(d=\log_b a\) | \(\Theta(n^d\log n)\) |
| \(d<\log_b a\) | \(\Theta(n^{\log_b a})\) |

Interpretation: compare root work \(n^d\) with the growth contributed by recursive leaves, \(n^{\log_b a}\). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/2b72ad50-6313-474a-b7bd-5cc9c170fc9e/Lec_2_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=%2FmrR%2BY2KUse5tTj2geXWJJP0q2A%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Divide and Conquer

## Merge Sort

**Goal:** Sort an array in nondecreasing order.

### Algorithm

1. If the array has length 1, return it.
2. Split the array into two halves.
3. Recursively sort each half.
4. Merge the sorted halves.

The merge step repeatedly compares the first unmerged elements and outputs the smaller one.

### Correctness

By induction:

- A one-element array is sorted.
- Recursive calls correctly sort each half.
- Merging two sorted arrays produces a sorted array containing every input element exactly once.

### Runtime

\[
T(n)=2T(n/2)+O(n)
\]

\[
\boxed{T(n)=\Theta(n\log n)}
\]

**Common pitfall:** The merge step is \(O(n)\), not \(O(1)\). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/e9312164-0d70-499e-bf27-2becf865baec/Lec_1_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=KWDLfH3P9G0YhEKF0fiR5GwMqNk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

## Maximum Difference

**Input:** Array \(A,\ldots,A[n-1]\)

**Goal:** Maximize:

\[
A_i-A_j
\]

subject to:

\[
i<j
\]

This represents the largest drop from an earlier element to a later element.

### Crossing solution

If the optimal pair crosses the midpoint, then it has value:

\[
\max(A_{\text{left}})-\min(A_{\text{right}})
\]

### Weak summary approach

If each recursive call returns only the best difference, finding the crossing value requires scanning each half.

\[
T(n)=2T(n/2)+O(n)
\]

\[
\boxed{T(n)=\Theta(n\log n)}
\]

### Rich summary approach

Return three quantities for each subarray:

- \(D\): best difference within the subarray
- \(M\): maximum element
- \(m\): minimum element

For left and right halves:

\[
D=\max(D_L,D_R,M_L-m_R)
\]

\[
M=\max(M_L,M_R)
\]

\[
m=\min(m_L,m_R)
\]

Now the combine step is constant time:

\[
T(n)=2T(n/2)+O(1)
\]

\[
\boxed{T(n)=\Theta(n)}
\]

**Key lesson:** Returning exactly the extra information required for combining can dramatically improve runtime. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/2b72ad50-6313-474a-b7bd-5cc9c170fc9e/Lec_2_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=%2FmrR%2BY2KUse5tTj2geXWJJP0q2A%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

## Deterministic Selection: Median of Medians

**Goal:** Find the \(k\)-th smallest of \(n\) distinct numbers in deterministic linear time.

Sorting first costs:

\[
\Theta(n\log n)
\]

Median-of-medians achieves:

\[
\boxed{\Theta(n)}
\]

### Why a good pivot matters

An arbitrary pivot may leave a recursive call of size \(n-1\):

\[
T(n)=T(n-1)+O(n)
\]

which can be quadratic.

A good pivot ensures both sides after partitioning have size at most:

\[
\frac{7n}{10}+O(1)
\]

### Algorithm

1. Partition the input into groups of 5.
2. Sort each group and take its median.
3. Recursively find the median of those medians.
4. Use it as pivot \(p\).
5. Partition the original array around \(p\).
6. Recurse only into the side containing rank \(k\).

### Why the pivot is good

At least half of the group medians are at least \(p\). In each such group, the median and its two larger elements are at least \(p\).

Thus at least:

\[
3\cdot \frac{1}{2}\cdot\frac{n}{5}
\]

elements are at least \(p\), which is:

\[
\frac{3n}{10}
\]

A symmetric argument gives at least \(3n/10\) elements at most \(p\). So at least a constant fraction is discarded each recursive step. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/eeb7c8cf-e45a-473e-aaac-44c9c6112817/Lec_3_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=lGu2ICzpashBwAjsegaz3AOmu3I%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

### Runtime

\[
T(n)=T(n/5)+T(7n/10)+O(n)
\]

Because the recursive fractions sum to less than 1:

\[
\frac{1}{5}+\frac{7}{10}=\frac{9}{10}
\]

the runtime is:

\[
\boxed{T(n)=O(n)}
\]

***

# Dynamic Programming

## Largest Contiguous Sum

**Input:** An array containing positive and negative numbers.

**Goal:** Find a contiguous interval with maximum sum. The empty interval, with value 0, is permitted.

### State

Let \(M_i\) be the maximum sum of a nonempty contiguous subarray ending exactly at index \(i\).

### Recurrence

\[
M_0=A_0
\]

\[
M_i=\max(A_i,A_i+M_{i-1})
\]

The best interval ending at \(i\) either:

- starts fresh at \(i\), or
- extends the best interval ending at \(i-1\).

### Answer

\[
\max\left(0,\max_i M_i\right)
\]

### Complexity

\[
\boxed{O(n)\text{ time}}
\]

\[
\boxed{O(1)\text{ auxiliary space for the value only}}
\]

To recover the interval endpoints, also store whether the recurrence chose “start new” or “extend previous.” [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/eeb7c8cf-e45a-473e-aaac-44c9c6112817/Lec_3_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=lGu2ICzpashBwAjsegaz3AOmu3I%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

## Longest Common Subsequence

A **subsequence** preserves order but does not need to be contiguous. A substring must be contiguous.

**Goal:** Find the maximum length subsequence shared by sequences:

\[
A=a_1a_2\ldots a_n
\]

and

\[
B=b_1b_2\ldots b_m
\]

### State

\[
D[i,j]
\]

is the LCS length of prefixes:

\[
a_1\ldots a_i
\]

and

\[
b_1\ldots b_j
\]

### Base cases

\[
D[0,j]=0
\]

\[
D[i,0]=0
\]

### Recurrence

If final characters match:

\[
D[i,j]=D[i-1,j-1]+1
\]

If final characters differ:

\[
D[i,j]=\max(D[i-1,j],D[i,j-1])
\]

### Why it works

- If \(a_i=b_j\), an optimal common subsequence can end with this shared character.
- If \(a_i\ne b_j\), a common subsequence cannot use both final characters, so at least one must be discarded.

### Complexity

\[
\boxed{O(nm)\text{ time}}
\]

\[
\boxed{O(nm)\text{ space}}
\]

### Recovery

Start from \(D[n,m]\):

- If characters match, output the character and move diagonally.
- Otherwise move to a neighboring cell with the same value.
- Reverse collected characters at the end.

Ties can represent multiple valid optimal LCSs. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/39da8591-ea3b-416e-ba23-bdc2d8277c86/Lec_4_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=Jj1C5nKWxVRyBSfaJ%2FpTTqGDWfM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

## Maximum Independent Set in a Tree

An **independent set** is a set of vertices with no adjacent pair.

Root the tree at an arbitrary vertex.

### Two-state formulation

For a vertex \(v\):

- \(I_v\): best solution in subtree \(T_v\) when \(v\) is included.
- \(X_v\): best solution in subtree \(T_v\) when \(v\) is excluded.

### Recurrences

If \(v\) is included, children cannot be included:

\[
I_v=1+\sum_{u\text{ child of }v}X_u
\]

If \(v\) is excluded, each child may be included or excluded:

\[
X_v=\sum_{u\text{ child of }v}\max(I_u,X_u)
\]

### Answer

\[
\max(I_r,X_r)
\]

where \(r\) is the root.

### Evaluation order

Use postorder traversal so all child states are available before computing the parent.

### Runtime

\[
\boxed{O(|V|)}
\]

The important DP insight is that the parent only needs to know whether the child is allowed to be included. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/39da8591-ea3b-416e-ba23-bdc2d8277c86/Lec_4_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=Jj1C5nKWxVRyBSfaJ%2FpTTqGDWfM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

## Knapsack: Value-Indexed DP

Each item \(i\) has:

- size \(s_i\)
- value \(v_i\)

The capacity is \(B\).

**Goal:** Maximize total value subject to:

\[
\sum_{i\in S}s_i\le B
\]

### State

Let:

\[
V_{\text{sum}}=\sum_{i=1}^{n}v_i
\]

Define:

\[
D[i,v]
\]

as the minimum total size needed to obtain total value exactly \(v\) using the first \(i\) items.

Set impossible states to infinity.

### Base cases

\[
D[0,0]=0
\]

\[
D[0,v]=\infty
\]

for every \(v>0\).

### Recurrence

If \(v\ge v_i\):

\[
D[i,v]=\min(D[i-1,v],s_i+D[i-1,v-v_i])
\]

If \(v<v_i\), item \(i\) cannot be included in a solution of value \(v\), so use:

\[
D[i,v]=D[i-1,v]
\]

### Answer

Find the largest \(v\) such that:

\[
D[n,v]\le B
\]

### Runtime

\[
O(nV_{\text{sum}})
\]

This is **pseudo-polynomial**, because it is polynomial in the numerical magnitudes of values, not necessarily the number of bits used to encode them. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/61a42b7f-51ad-4c9b-bd45-c5041a500368/Lec_5_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9K2%2F3vDKkMXvBs9gste3us0NbAY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

## Knapsack FPTAS

For a maximization problem, a \((1-\varepsilon)\)-approximation returns a feasible solution valued at least:

\[
(1-\varepsilon)\mathrm{OPT}
\]

An FPTAS has runtime polynomial in both input size and:

\[
\frac{1}{\varepsilon}
\]

### Scaling construction

First discard items with:

\[
s_i>B
\]

Let:

\[
V_{\max}=\max_i v_i
\]

Then:

\[
V_{\max}\le\mathrm{OPT}
\]

Set:

\[
K=\frac{\varepsilon V_{\max}}{n}
\]

Scale each value downward:

\[
\hat{v}_i=\left\lfloor\frac{v_i}{K}\right\rfloor
\]

Run the value-indexed DP on the scaled values.

### Runtime

Every scaled value is at most:

\[
\frac{n}{\varepsilon}
\]

so the sum of scaled values is at most:

\[
\frac{n^2}{\varepsilon}
\]

Thus the runtime is:

\[
\boxed{O\left(\frac{n^3}{\varepsilon}\right)}
\]

### Approximation guarantee

Rounding down loses less than \(K\) per chosen item. At most \(n\) items are chosen, so the total loss is below:

\[
nK=\varepsilon V_{\max}
\]

Since:

\[
V_{\max}\le\mathrm{OPT}
\]

the loss is at most:

\[
\varepsilon\mathrm{OPT}
\]

Therefore the returned solution has value at least:

\[
\boxed{(1-\varepsilon)\mathrm{OPT}}
\]

 [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/61a42b7f-51ad-4c9b-bd45-c5041a500368/Lec_5_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9K2%2F3vDKkMXvBs9gste3us0NbAY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

## Finite-Horizon Markov Decision Processes

An MDP includes:

- a finite state space \(S\)
- a finite action space \(A\)
- transition probabilities \(p(a,s,s')\)
- immediate reward \(r(a,s)\)
- a starting state
- a time horizon \(T\)

An action produces immediate reward, then transitions probabilistically to a new state.

### State

\[
V[s,t]
\]

is the maximum expected total reward when currently in state \(s\) with exactly \(t\) actions remaining.

### Base case

\[
V[s,0]=0
\]

### Bellman optimality equation

\[
V[s,t]=\max_{a\in A}\left(r(a,s)+\sum_{s'\in S}p(a,s,s')V[s',t-1]\right)
\]

### Key conclusions

There exists an optimal policy that is:

- **Markov:** depends only on the current state and time remaining.
- **Deterministic:** chooses an action that maximizes the Bellman expression.

Randomization cannot improve on selecting the highest expected-value action.

### Complexity

With explicitly stored transition probabilities:

\[
\boxed{O(T|A||S|^2)}
\]

time and:

\[
\boxed{O(T|S|)}
\]

space for the full value table. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/61a42b7f-51ad-4c9b-bd45-c5041a500368/Lec_5_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9K2%2F3vDKkMXvBs9gste3us0NbAY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Graph Representations

For a graph \(G=(V,E)\):

\[
n=|V|
\]

\[
m=|E|
\]

| Representation | Space | Useful operation |
|---|---:|---|
| Adjacency matrix | \(O(n^2)\) | Test whether an edge exists in \(O(1)\) |
| Adjacency lists | \(O(n+m)\) | Scan all neighbors efficiently |

For an undirected graph:

\[
\sum_{v\in V}\deg(v)=2m
\]

Adjacency lists are typically preferred for sparse graphs. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/b51c781b-ab02-4a9a-8f46-7a8c244af296/Lec_6_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=auLHnwyjg7ghz7VGh%2BZRTS8Z7tA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Breadth-First Search

Use BFS in an **unweighted** graph, where path length means number of edges.

### Algorithm

1. Set source distance to zero.
2. Set all other distances to infinity or unvisited.
3. Put the source in a FIFO queue.
4. Repeatedly remove a vertex \(u\).
5. For each undiscovered neighbor \(v\), set:

\[
\mathrm{dist}[v]=\mathrm{dist}[u]+1
\]

6. Record \(u\) as \(v\)'s parent and enqueue \(v\).

### Correctness idea

BFS explores distance layers in order.

When \(v\) is first discovered from \(u\), BFS has found a path of length:

\[
\mathrm{dist}[u]+1
\]

If a shorter path existed, its predecessor would occur in an earlier layer and would have discovered \(v\) first.

### Runtime

\[
\boxed{O(n+m)}
\]

Each vertex enters the queue at most once, and each adjacency-list entry is scanned once. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/b51c781b-ab02-4a9a-8f46-7a8c244af296/Lec_6_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=auLHnwyjg7ghz7VGh%2BZRTS8Z7tA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Dijkstra’s Algorithm

Use Dijkstra for shortest paths with **nonnegative** edge weights.

### Algorithm

Maintain tentative distances \(d[v]\).

1. Set:

\[
d[s]=0
\]

2. Set all other distances to infinity.
3. Store vertices in a min-priority queue.
4. Extract the unsettled vertex \(u\) with minimum tentative distance.
5. Relax each outgoing edge \((u,v)\). If:

\[
d[u]+w(u,v)<d[v]
\]

then update \(d[v]\) and set its parent to \(u\).

### Key invariant

When \(u\) is extracted from the queue:

\[
d[u]=\mathrm{dist}(s,u)
\]

That is, its tentative distance is its true shortest-path distance.

### Why nonnegative weights matter

The proof relies on the fact that a prefix of a shortest path cannot be longer than the full path. Negative edges break this reasoning and can cause a vertex to be settled too early.

### Runtime

With adjacency lists and a binary heap:

\[
\boxed{O((n+m)\log n)}
\]

 [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/b51c781b-ab02-4a9a-8f46-7a8c244af296/Lec_6_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=auLHnwyjg7ghz7VGh%2BZRTS8Z7tA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Minimum Spanning Trees

A spanning tree connects all vertices without cycles and contains:

\[
n-1
\]

edges.

An MST minimizes the total selected edge weight.

**Important:** An MST is not necessarily a shortest-path tree. An MST minimizes total connection cost, while a shortest-path tree minimizes route lengths from a particular source. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/76259b22-47b8-4039-a237-34954633c105/Lec_7_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9cEvib3Sxkd3U9YrWQ9%2ByQ5nPVI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Cut Property

For nonempty proper subset:

\[
S\subset V
\]

the cut is:

\[
(S,V\setminus S)
\]

A light edge is a minimum-weight edge crossing that cut.

### Theorem

Any light edge crossing a cut belongs to some MST.

If that edge is uniquely lightest across the cut, it belongs to every MST.

### Exchange proof

1. Start with an MST \(T\) that omits light edge \(e\).
2. Add \(e\), creating a cycle.
3. The cycle must contain another edge \(f\) crossing the cut.
4. Because \(e\) is light:

\[
w(e)\le w(f)
\]

5. Remove \(f\). The result remains a spanning tree and has no larger weight.

Thus an MST containing \(e\) exists. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/76259b22-47b8-4039-a237-34954633c105/Lec_7_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9cEvib3Sxkd3U9YrWQ9%2ByQ5nPVI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Prim’s Algorithm

Prim grows one tree from a chosen root.

### Algorithm

1. Start with:

\[
S=\{r\}
\]

2. Repeatedly choose the minimum-weight edge crossing:

\[
(S,V\setminus S)
\]

3. Add that edge and its outside endpoint to the tree.
4. Continue until every vertex is included.

### Invariant

Some MST contains all selected edges so far.

### Priority queue key

For each unvisited vertex \(v\):

\[
\mathrm{key}[v]=\min\{w(u,v):u\in S\}
\]

Store a parent that attains this minimum.

### Runtime

With adjacency lists and a binary heap:

\[
\boxed{O((n+m)\log n)}
\]

### Prim versus Dijkstra

| Algorithm | Meaning of key for \(v\) |
|---|---|
| Dijkstra | Total length of a candidate path from source to \(v\) |
| Prim | Cost of one cheapest edge connecting \(v\) to the current tree |

Prim can handle negative edge weights because it relies on the cut property, not path-distance monotonicity. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/76259b22-47b8-4039-a237-34954633c105/Lec_7_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9cEvib3Sxkd3U9YrWQ9%2ByQ5nPVI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Matchings

A matching is a set of edges such that no vertex touches more than one selected edge.

- A **maximal** matching cannot be extended by adding one edge.
- A **maximum** matching has the largest possible number of edges.

A maximal matching may not be maximum. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/76259b22-47b8-4039-a237-34954633c105/Lec_7_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9cEvib3Sxkd3U9YrWQ9%2ByQ5nPVI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Augmenting Paths

Given matching \(M\), an augmenting path:

- alternates between edges outside \(M\) and edges in \(M\)
- starts and ends at unmatched vertices

It begins and ends with unmatched edges, so it contains one more unmatched edge than matched edge.

### Augmentation

Flip all path edges:

- remove matched edges on the path
- add unmatched edges on the path

The result is still a matching, and its size increases by one:

\[
|M'|=|M|+1
\]

 [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/76259b22-47b8-4039-a237-34954633c105/Lec_7_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9cEvib3Sxkd3U9YrWQ9%2ByQ5nPVI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Berge’s Theorem

A matching is maximum if and only if it has no augmenting path.

- If an augmenting path exists, the matching can be improved.
- If a larger matching existed, the symmetric difference between matchings would contain an augmenting path.

This theorem provides both an algorithmic strategy and an optimality certificate. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/76259b22-47b8-4039-a237-34954633c105/Lec_7_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9cEvib3Sxkd3U9YrWQ9%2ByQ5nPVI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Bipartite Matching

For a bipartite graph with sides \(A\) and \(B\):

- Direct unmatched edges from \(A\) to \(B\).
- Direct matched edges from \(B\) to \(A\).
- Search from unmatched vertices of \(A\) to unmatched vertices of \(B\).

A directed path found this way is exactly an augmenting path.

### Complexity

One BFS or DFS costs:

\[
O(n+m)
\]

Each augmentation increases matching size by one, and a matching has at most \(n/2\) edges:

\[
\boxed{O(n(n+m))}
\]

General graphs need more advanced handling because odd cycles complicate the process. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/76259b22-47b8-4039-a237-34954633c105/Lec_7_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=9cEvib3Sxkd3U9YrWQ9%2ByQ5nPVI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Maximum Flow

A flow network has:

- directed graph \(G=(V,E)\)
- capacities \(c_e\ge 0\)
- source \(s\)
- sink \(t\)

## Feasible Flow

A flow \(f\) satisfies capacity constraints:

\[
0\le f_e\le c_e
\]

and flow conservation at every non-source, non-sink vertex:

\[
\sum_{(u,v)\in E}f_{uv}
=
\sum_{(v,w)\in E}f_{vw}
\]

The flow value is net outgoing flow from \(s\). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/269b5302-2d10-4868-a47b-b8b5ccb28f10/Lec_8_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=3b4G1FlG7zxVjjxpJE3JtXn6Fw8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Bipartite Matching as Flow

To transform bipartite matching into flow:

1. Add source edges to every vertex in \(A\), each with capacity 1.
2. Direct original bipartite edges from \(A\) to \(B\), capacity 1.
3. Add capacity-1 edges from every vertex in \(B\) to the sink.

An integral flow of value \(k\) corresponds to a matching of size \(k\). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/269b5302-2d10-4868-a47b-b8b5ccb28f10/Lec_8_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=3b4G1FlG7zxVjjxpJE3JtXn6Fw8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Residual Graph

For original edge \((u,v)\) with capacity \(c_e\) and current flow \(f_e\):

- Forward residual capacity:

\[
c_e-f_e
\]

- Reverse residual capacity:

\[
f_e
\]

The reverse edge allows cancellation of previously sent flow. It does not represent an original edge in the network.

An \(s\)-to-\(t\) path in the residual graph is an **augmenting path**.

Its bottleneck is:

\[
\min\{\text{residual capacity of edges on the path}\}
\]

Augmenting by the bottleneck preserves feasibility and increases flow value. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/269b5302-2d10-4868-a47b-b8b5ccb28f10/Lec_8_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=3b4G1FlG7zxVjjxpJE3JtXn6Fw8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Ford-Fulkerson

1. Start with zero flow.
2. Construct the residual graph.
3. Find an \(s\)-to-\(t\) path.
4. Augment by its bottleneck.
5. Repeat until no residual \(s\)-to-\(t\) path exists.

With integer capacities, every augmentation raises flow by at least 1.

### Runtime

The simple bound is:

\[
O(m(n+|f^*|))
\]

where:

\[
|f^*|
\]

is maximum-flow value.

This is pseudo-polynomial because \(|f^*|\) can be large relative to the number of bits used to encode capacities.  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/269b5302-2d10-4868-a47b-b8b5ccb28f10/Lec_8_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=3b4G1FlG7zxVjjxpJE3JtXn6Fw8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

## Edmonds-Karp

Edmonds-Karp chooses the augmenting path with the fewest residual edges, found using BFS.

It is polynomial in \(n\) and \(m\), independent of capacity magnitudes. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/269b5302-2d10-4868-a47b-b8b5ccb28f10/Lec_8_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=3b4G1FlG7zxVjjxpJE3JtXn6Fw8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# Minimum Cuts and Max-Flow Min-Cut

An \(s\)-\(t\) cut separates vertices into:

\[
X
\]

and:

\[
V\setminus X
\]

where:

\[
s\in X
\]

and:

\[
t\notin X
\]

Its capacity counts only directed edges leaving \(X\):

\[
c(X,V\setminus X)
=
\sum_{u\in X,\,v\notin X}c_{uv}
\]

## Weak Duality

Every feasible flow satisfies:

\[
|f|\le c(X,V\setminus X)
\]

for every \(s\)-\(t\) cut.

## Max-Flow Min-Cut Theorem

\[
\boxed{\text{maximum flow value}=\text{minimum cut capacity}}
\]

### Optimality certificate

When no residual \(s\)-to-\(t\) path exists:

1. Let \(X\) be vertices reachable from \(s\) in the final residual graph.
2. Every original edge leaving \(X\) is saturated.
3. Every original edge entering \(X\) has zero flow.
4. Therefore the current flow value equals the cut capacity.

Since no flow can exceed any cut capacity, the current flow is maximum and the cut is minimum. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/2077514303/269b5302-2d10-4868-a47b-b8b5ccb28f10/Lec_8_Unmarked.pdf?AWSAccessKeyId=ASIA2F3EMEYEQSPAJ5AK&Signature=3b4G1FlG7zxVjjxpJE3JtXn6Fw8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCQVx0wpaciAUC1NZQwtH0SsJMG90Fo2sKj3IwvQwt%2F8QIhAI4%2BMjxjp5FBiimYhl3x50LZDDVPLQQqkha8IxXHVQ7JKvMECH0QARoMNjk5NzUzMzA5NzA1IgywjfNXYxl6BQc3h9Iq0AQyXWDu1xiRLQ3%2FlF5aM7Laz%2B6cnQY13ds33uexqFnSfaiqzzROZFLHAsl1nTCvhCS5e4QjTy5Ae%2B9fXEertHpAEvueU42ZxUdby9tyqLeGxVAkdpvFOOU2nNHP3u7RIs3%2Ba3ShkeAnYqso69Qk7URs444ZQv8zkUedPbIv9NZkNFqqyU8IvZYvieHN%2Fgt9jfEtlw0OPjv0iFOJW8npYlQ4Tc%2BzHPrggWV3AVfHudN%2BCZGCA%2F0luv0WcHG9KJBXOK6zWLGGMj%2FiUEAzXsJEwT7F%2FPQj6aiS2tGI%2B3p9BLSGrKkQ37W69U8eIzUXlcepvAD%2Bwbn94zOYfJDkeHy13ZLotPlhjnwvflAM0s94bpI7Ezu7mvSPFKbmHFEESKmy59hbD3J1Kqyk8KKqVgoguKphL8dJfx7G9DEFyHaPQjcR86B8QOslzfROV3Pq59PRH7wxG8x2U9cETq2xT5qeOiyUM8Mjoo8WovRv9x49SAW2dKppU1999s7aKIlmBwsT5A4lPT5LABZth6FUzLp8E9FAwy%2Bk4Sir%2Fse6BBqAq3VGdPLSS3BuQ0khniWV9JnxmZVjb0gCIHrCFTu%2F%2BsWLi4dCXYD1U%2Fn9vrgCVK2OWOiTitllJHEIW%2FM5Qq3HwBC0V4F%2F4wBOuRJZrvKMAwHoXVigQZJg9WXpowoJeQG6xWnT5YiEJBOO5ziFc2EMONmZQ2XMjN6qJzyc%2FPRM1t1RF%2F3OOCnIt4jRtoBOFbzEqvDdjBi6JnhCuSsLySmqW7SkmKewLvd7WTs21SUC1z7SZkSoMLv1wNUGOpcBvaD5y7yTUswOtAlDbyOukyUhoJOLbK%2FFNttggVc2IRNHXBYukbrKjEWuqyLWlfV0j8DI3GRswZuL%2BdqWum4X3qK6uodBkZZ9QcqgKbFfZEtz%2Bohmq5tnjIe24jiuX%2FpUC3r3WKu2kmfeTchFuG26XeUoqiS0Nf%2FYahjFIlFb%2FZ6lJHE%2F8FeOjKQPIMy9cMng6Nh4sLrO%2FA%3D%3D&Expires=1789937806)

***

# High-Yield Comparisons

| Concept pair | Key distinction |
|---|---|
| Subsequence vs. substring | A subsequence can skip elements; a substring cannot |
| Maximum vs. maximal matching | Maximum is globally largest; maximal cannot be enlarged by one immediate edge |
| MST vs. shortest-path tree | MST minimizes total selected-edge weight; shortest-path trees minimize distances from a source |
| Dijkstra vs. Prim | Similar data structures, but different key meanings and objectives |
| Polynomial vs. pseudo-polynomial | Pseudo-polynomial runtime depends on numeric magnitudes, not only input bit length |
| Reverse residual edge vs. original edge | Reverse residual edges allow cancellation; they need not exist in the original graph |
| BFS vs. Dijkstra | BFS requires uniform edge length; Dijkstra handles nonnegative weighted edges |

***

# Retrieval Practice

Try these without consulting the relevant section first:

1. Why is merge sort’s total merge work \(O(n)\) at every non-leaf recursion level?
2. What three values must maximum-difference subproblems return to achieve linear time?
3. Reconstruct the median-of-medians \(3n/10\) pivot-quality argument.
4. What five components should every dynamic-programming design specify?
5. Explain both branches of the LCS recurrence in words.
6. Why is the value-indexed knapsack DP pseudo-polynomial?
7. How does scaling create a knapsack FPTAS?
8. Why must finite-horizon MDP state include time remaining?
9. What BFS invariant proves shortest fewest-edge paths?
10. What exact part of Dijkstra’s proof fails with negative edges?
11. State the MST cut property and outline its exchange proof.
12. Why does augmenting along an augmenting path increase matching size by one?
13. Why are reverse residual edges essential in maximum flow?
14. How does failed residual-graph reachability produce a min-cut certificate?

What topic would you like to test yourself on first: recurrences, dynamic programming, or graph algorithms?
