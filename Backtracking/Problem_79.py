"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,

where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

"""
from typing import List
from functools import lru_cache
from collections import defaultdict, Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        self.m = len(board)
        self.n = len(board[0])
        self.board = board

        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(i, j, word):
                    return True
        return False

    @lru_cache(None)
    def dfs(self, i, j, word):
        if len(word) == 0:
            # Complete Search
            return True
        # Invalid point check + word check
        if i < 0 or i >= self.m or j < 0 or j >= self.n or word[0] != self.board[i][j]:
            return False

        tmp = self.board[i][j]
        self.board[i][j] = "#"  # Found word is replaced
        # You must understand below DFS logic.
        result = self.dfs(i + 1, j, word[1:]) or self.dfs(i - 1, j, word[1:]) or \
                 self.dfs(i, j + 1, word[1:]) or self.dfs(i, j - 1, word[1:])
        # After finishing all recursion, refill the value for main loop
        self.board[i][j] = tmp
        return result


class Solution_2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(r, c, i):
            if i == len(word):
                return True
            if 0 <= r < m and 0 <= c < n and board[r][c] == word[~i] and (r, c) not in seen:
                seen.add((r, c))
                counter[(r, c, i)] += 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if counter[(nr, nc, i)] < 2 and DFS(nr, nc, i + 1):
                        return True
                seen.remove((r, c))
            return False

        counter = defaultdict(int)
        seen = set()
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if DFS(r, c, 0):
                    return True
        return False


class Solution_3:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, pos):
            if pos == len(word):
                return True

            if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    board[r][c] != word[pos]):
                return False

            temp = board[r][c]
            board[r][c] = ""

            pos += 1
            res = (dfs(r + 1, c, pos) or
                   dfs(r, c + 1, pos) or
                   dfs(r - 1, c, pos) or
                   dfs(r, c - 1, pos))
            board[r][c] = temp
            return res

        # reverse the word if frequency of the first letter is more than the last letter's => Why?
        count = dict(sum(map(Counter, board), Counter()))
        if word[0] not in count or word[-1] not in count:
            return False

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != word[0]:
                    continue
                if dfs(r, c, 0):
                    return True
        return False


class Solution_4:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        counter = Counter(word)
        freq = Counter()
        for i in range(m):
            for j in range(n):
                freq[board[i][j]] += 1
        for k, v in counter.items():
            if freq[k] < v:
                return False  # 조기 종료를 위한 구문
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def backtrack(i: int, j: int, wi: int) -> bool:
            if board[i][j] != word[wi]:
                return False

            if wi == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = ""

            for di, dj in directions:
                i1, j1 = di + i, dj + j
                if 0 <= i1 < m and 0 <= j1 < n and board[i1][j1] != "":
                    if backtrack(i1, j1, wi + 1):
                        return True
            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


solver = Solution()
board_1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word_1 = "SEE"

board_2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word_2 = "ABCCED"

board_3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word_3 = "ABCB"

print(solver.exist(board_1, word_1))  # True
print(solver.exist(board_2, word_2))  # True
print(solver.exist(board_3, word_3))  # False
