"""
Given an array of distinct integers candidates and a target integer target,

return a list of all unique combinations of candidates where the chosen numbers sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations

that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

"""
from typing import List
from collections import Counter


class Solution_1:
    # First Solution
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        outputs = []

        def backtracking(comb):
            cur_total = sum(comb)

            if cur_total == target:
                # 탐색의 끝에 도달
                if Counter(comb) not in results:
                    results.append(Counter(comb))
                return
            elif cur_total < target:
                for candidate in candidates:
                    backtracking(comb + [candidate])
            else:
                # 초과시 끝냄
                return

        backtracking([])
        for com in results:
            tmp = []
            for num, repeat in zip(com.keys(), com.values()):
                tmp += [*[num] * repeat]
            outputs.append(tmp)

        return outputs


class Solution:
    # Optimized Version
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(comb, start):
            if sum(comb) == target:
                # Optimization Point 1
                results.add(tuple(sorted(comb)))
                return
            elif sum(comb) > target:
                return
            # Optimization Point 2
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtracking(comb, i)
                comb.pop()

        results = set()
        backtracking([], 0)
        outputs = [list(comb) for comb in results]
        return outputs


solver = Solution()
print(solver.combinationSum(candidates=[2,3,6,7], target=7))
print(solver.combinationSum(candidates=[2,3,5], target=8))