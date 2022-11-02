"""
You are given an integer array coins representing coins of different

denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.

If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104

"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Constraint
        assert 1 <= len(coins) <= 12
        # Base Case
        # 현재 Logic 이 틀렸으므로... 아마도, 추정컨대
        coins.sort()
        if amount == 0:
            return 0

        stack = []
        remained = amount
        while coins:
            divider = coins.pop()
            q = remained // divider
            stack.append(q)
            remained = remained - q * divider

        if remained != 0:
            return -1
        else:
            return sum(stack)


solver = Solution()
# coins = [1,2,5], amount = 11
print(solver.coinChange([1, 2, 5], 11))
print(solver.coinChange([2], 3))
print(solver.coinChange([1], 0))
print(solver.coinChange([2, 5, 10, 1], 27))
print(solver.coinChange([186, 419, 83, 408], 6249))  # Return 20

