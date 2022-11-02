"""
You are climbing a staircase.

It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        ### 독립적인 경로의 갯수를 찾는 문제로, 굉장히 고전적인 문제 !
        ### Memoization 을 쓸 부분은 중간 중간 분기점들 ?
        """
        :param n: 계단의 갯수
        :return: unique way 의 갯수
        """
        # 1. subproblem 은 무엇으로 볼 수 있을까 ?
        # - 만약 1로 시작하면 남은 경로의 길이는 n-1, 2로 시작하면 n-2.
        # - 이 때 n-1 에 대한 Solution 은 n 에 대한 Solution 과 같고 n-2에 대한 Solution 도 마찬가지
        # 즉... f(n) = f(n-1) 이고 f(n) = f(n-2) 라는 소리임.  => 수열문제 같은데 ?
        # 2. 최적구조는 ?
        # 3. bottom-up 이 좋을까, top-down이 적합할까 ?
