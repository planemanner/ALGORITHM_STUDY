from collections import defaultdict, deque
from bisect import bisect_right


def view(_map):
    for row in _map:
        print(row)
    print("\n")


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        L = [[0 for x in range(n + 1)] for x in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        return L[m][n]


class Solution_3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1

        box = [[0] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    box[i][j] = 1 + box[i - 1][j - 1]

                else:
                    box[i][j] = max(box[i - 1][j], box[i][j - 1])
        view(box)
        return box[m - 1][n - 1]


text1 = "abcde"
text2 = "ace"

text3 = "abc"
text4 = "abc"

text5 = "abc"
text6 = "def"

text7 = "bl"
text8 = "yby"

text9 = "ezupkr"
text10 = "ubmrapg"

text11 = "abc"
text12 = "def"


solver = Solution()
solver_2 = Solution_3()
# print(solver.longestCommonSubsequence(text1, text2))
# print(solver.longestCommonSubsequence(text3, text4))
# print(solver.longestCommonSubsequence(text5, text6))
# print(solver.longestCommonSubsequence(text7, text8))
print(solver_2.longestCommonSubsequence(text9, text10))
# print(solver.longestCommonSubsequence(text11, text12))