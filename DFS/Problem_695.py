"""
You are given an m x n binary matrix grid.

An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)

You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visit = {}
        max_area = 0

        def valid_pt(pt):
            x, y = pt[0], pt[1]
            if 0 <= x < m and 0 <= y < n:
                return True
            else:
                return False

        def get_area(start_pt):
            x_0, y_0 = start_pt[0], start_pt[1]

            if not valid_pt(start_pt):
                return 0
            if grid[x_0][y_0] == 0:
                return 0
            if start_pt in visit:
                return 0
            else:
                visit[start_pt] = 1
                left, right = get_area((x_0, y_0-1)), get_area((x_0, y_0+1))
                up, down = get_area((x_0-1, y_0)), get_area((x_0+1, y_0))

                return left + right + up + down + 1

        for i in range(m):
            for j in range(n):
                island_area = get_area((i, j))
                if max_area < island_area:
                    max_area = island_area

        return max_area


solver = Solution()
print(solver.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                              [0,0,0,0,0,0,0,1,1,1,0,0,0],
                              [0,1,1,0,1,0,0,0,0,0,0,0,0],
                              [0,1,0,0,1,1,0,0,1,0,1,0,0],
                              [0,1,0,0,1,1,0,0,1,1,1,0,0],
                              [0,0,0,0,0,0,0,0,0,0,1,0,0],
                              [0,0,0,0,0,0,0,1,1,1,0,0,0],
                              [0,0,0,0,0,0,0,1,1,0,0,0,0]]))