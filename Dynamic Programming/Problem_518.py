"""
You are given an integer array coins representing coins of different denominations and

an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.

If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

Constraints
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""
from typing import List


class SolutionTimeOver:
    def change(self, amount: int, coins: List[int]) -> int:
        # amount is the capacity of a knapsack.
        # size is defined as a coin value * the number of coins.
        results = set()
        n_coins = len(coins)

        def backtracking(comb, start):
            cur_amt = sum(comb)
            if tuple(comb) in results:
                return

            if cur_amt == amount:
                # Optimization Point 1
                results.add(tuple(sorted(comb)))
                return
            elif cur_amt > amount:
                return
            # Optimization Point 2
            for i in range(start, n_coins):
                comb.append(coins[i])
                backtracking(comb, i)
                comb.pop()

        backtracking([], 0)
        n_comb = len(results)
        if n_comb == 0:
            return 0

        return n_comb


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Knapsack Algorithm.
        :param amount:
        :param coins:
        :return:
        """
        dp_mat = [[0] * (amount + 1) for _ in range(len(coins)+1)]
        # Initialization
        for j in range(len(coins)+1):
            dp_mat[j][0] = 1  # amount 가 0 이면 아예 안 내면 되기 때문

        # Core function
        def unbounded_knapsack(coin_id, cur_amt):
            if coins[coin_id-1] > cur_amt:
                return dp_mat[coin_id-1][cur_amt]
            else:
                return dp_mat[coin_id-1][cur_amt] + dp_mat[coin_id][cur_amt-coins[coin_id-1]]

        for i in range(1, len(dp_mat)):
            for j in range(1, len(dp_mat[0])):
                dp_mat[i][j] = unbounded_knapsack(i, j)

        return dp_mat[-1][-1]


class SolutionOpt:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)

        def f(i, target, dp):
            if i == 0:
                if target % coins[i] == 0:
                    return 1
                return 0

            if dp[i][target] != -1:
                return dp[i][target]

            ntake = f(i - 1, target, dp)
            take = 0
            if target >= coins[i]:
                take = f(i, target - coins[i], dp)
            dp[i][target] = ntake + take
            return dp[i][target]

        dp = [[-1] * (amount + 1) for _ in range(N)]
        return f(N - 1, amount, dp)


solver = Solution()
print(solver.change(amount=5, coins=[1, 2, 5]))  # 4
print(solver.change(amount=3, coins=[2]))  # 0
print(solver.change(amount=10, coins=[10]))  # 1
print(solver.change(amount=500, coins=[3, 5, 7, 8, 9, 10, 11]))  # 0
