"""
Given two strings word1 and word2,

return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    1. Insert a character
    2. Delete a character
    3. Replace a character

Example 1
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

constraints
  1. 0 <= word1.length, word2.length <= 500
  2. word1 and word2 consist of lowercase English letters.

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        :param word1: An original word
        :param word2: A target word
        :return: minimum distance
        """
        # 복습...
        

print(len("intention"))
print(len("execution"))
