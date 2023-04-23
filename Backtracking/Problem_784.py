"""
Given a string s, you can transform every letter

individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""
from typing import List
from itertools import product
# product => Cartesian product


# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         record = []
#         for ch in s:
#             record.append([ch] if ch.isdigit() else [ch.lower(), ch.upper()])
#
#         return [''.join(v) for v in product(*record)]


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = {}
        # Time complexity O(2^k * k)

        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                if sub not in res:
                    res[sub] = 1
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)
        backtrack()
        return list(res.keys())


solver = Solution()
print(solver.letterCasePermutation("a1b2"))
# print(solver.letterCasePermutation("abcd"))
# print(solver.letterCasePermutation("3z4"))
