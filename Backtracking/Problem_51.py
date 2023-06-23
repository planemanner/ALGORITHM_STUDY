"""
Classic Backtracking Problem

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q'

and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 0 : Non-allocated, -1 : Unavailable, 1 : Queen-allocated
        cur_board = [[0] * n for i in range(n)]
        sol = []

        def is_safe(board, row_id, col_id):

            # Horizontal
            for tmp_col in range(n):

                if tmp_col != col_id:

                    if board[row_id][tmp_col] != 0:

                        return False

            # Vertical
            for tmp_row in range(n):
                if tmp_row != row_id:
                    if board[tmp_row][col_id] != 0:
                        return False
            # Diagonal
            # print("left down diagonal")
            for i, j in zip(range(row_id, n), range(col_id, -1, -1)):
                if board[i][j] != 0:
                    return False
            # print("left up diagonal")
            for i, j in zip(range(row_id, -1, -1), range(col_id, -1, -1)):

                if board[i][j] != 0:
                    return False

            # print("left up diagonal")
            for i, j in zip(range(row_id, -1, -1), range(col_id, -1, -1)):
                if board[i][j] != 0:
                    return False
            # print("right up diagonal")
            for i, j in zip(range(row_id, -1, -1), range(col_id, n)):

                if board[i][j] != 0:
                    return False

            return True

        def find_solutions(board, cur_col_id, cur_row_id, cur_solution):
            if cur_col_id > n - 1:
                # Solution 저장
                cur_solution += [board]
            # 그렇지 않으면 전진, 그리고 잘못됐을 경우 후진 (backtracking)


solver = Solution()
solver.solveNQueens(5)
