"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
 If this is impossible, return -1.

 Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_points = []
        fresh_points = {}
        m, n = len(grid), len(grid[0])
        c_time = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        imp_check = False

        for i in range(m):
            if any(grid[i]):
                imp_check = True
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_points.append((i, j))
                if grid[i][j] == 1:
                    fresh_points[(i, j)] = 1
        # Check boundaries
        num_rotten = len(rotten_points)

        if num_rotten == 0:
            if imp_check:
                return -1
            else:
                return 0

        if num_rotten == m * n:
            return 0

        def rot(r_pts, cur_t):
            new_r_pts = []
            for r_pt in r_pts:
                for direction in directions:
                    x, y = r_pt[0] + direction[0], r_pt[1] + direction[1]
                    # Valid points
                    if 0 <= x < m and 0 <= y < n and (x, y) in fresh_points:
                        fresh_points.pop((x, y))
                        new_r_pts.append((x, y))

            return cur_t + 1, new_r_pts

        renew_flag = True
        rot_pts = rotten_points

        while len(fresh_points) != 0 and renew_flag:
            c_time, rot_pts = rot(rot_pts, c_time)

            if len(rot_pts) == 0:
                renew_flag = False

        if len(fresh_points) == 0:
            return c_time
        else:
            return -1


solver = Solution()
print(solver.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(solver.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(solver.orangesRotting(grid=[[0, 2]]))
print(solver.orangesRotting([[0]]))  # 0
print(solver.orangesRotting([[1]]))  # -1

