"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell,

you can either move in four directions: left, right, up, or down.

You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 231 - 1

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Input : matrix = [[1]]
Output : 1
"""

from typing import List
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
Python’s @lru_cache decorator offers a maxsize attribute that defines the maximum number of entries before the cache starts evicting old items. By default, maxsize is set to 128. If you set maxsize to None, then the cache will grow indefinitely, and no entries will be ever evicted. This could become a problem if you’re storing a large number of different calls in memory.
        """
        memo = {}
        self.m, self.n = len(matrix), len(matrix[0])
        self.global_max_length = 1
        self.searching = set()

        # start is the (x,y) tuple
        # return longest path
        def findLongestPath(x, y) -> int:
            # return condition is important to prevent stack overflow or infinite loop
            if (x, y) in memo:
                return memo[(x, y)]
            length = 1
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx, ny = dx + x, dy + y
                # check valid next node
                if 0 <= nx < self.m and 0 <= ny < self.n and matrix[nx][ny] > matrix[x][y]:
                    length = max(length, 1 + memo.get((nx, ny), findLongestPath(nx, ny)))
            # put it in memo for quick reference
            memo[(x, y)] = length
            self.global_max_length = max(self.global_max_length, length)
            return length

        for i in range(self.m):
            for j in range(self.n):
                if (i, j) not in memo:
                    findLongestPath(i, j)
        return self.global_max_length


class Good_Solution:
    def longestIncreasingPath(self, matrix):
        # 이 답안은 다수의 조건을 한 가지 조건으로 집약시켜서 불필요한 연산들을 제거하는 형태임 +Memoization 을 극한으로 잘 쓴 케이스.
        # 명시성도 좋고 매우 좋은 코드.
        if not matrix or not matrix[0]:
            return 0

        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        return max(dfs(x, y) for x in range(M) for y in range(N))


mat = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
mat_2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
mat_3 = [[7, 7, 5], [2, 4, 6], [8, 2, 0]]
solver = Solution()
print(f"Answer : {solver.longestIncreasingPath(matrix=mat)}")
print(f"Answer : {solver.longestIncreasingPath(matrix=mat_2)}")
print(f"Answer : {solver.longestIncreasingPath(matrix=mat_3)}")

if -1:
    print("????")