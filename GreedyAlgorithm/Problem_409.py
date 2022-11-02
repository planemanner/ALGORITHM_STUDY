"""
Given a string s which consists of lowercase or uppercase letters,

return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1)
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2)
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
"""
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        dic = defaultdict(int)
        max_len = 0
        odd_case = False
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        for ch_key in dic:
            max_len += 2 * (dic[ch_key] - dic[ch_key] % 2) // 2
            if dic[ch_key] % 2 == 1:
                odd_case = True
        return max_len + odd_case


class good_solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        max_pali = 0
        flag = 0
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        for key in hash_map:
            if hash_map[key] == 1:
                flag = 1
            elif hash_map[key] % 2 == 0:
                max_pali += hash_map[key]
            else:
                max_pali += hash_map[key] - 1
                flag = 1
        return max_pali + flag


solver = Solution()
print(solver.longestPalindrome("a"))
print(solver.longestPalindrome("abbvvdd"))
print(solver.longestPalindrome("abcabc"))
print(solver.longestPalindrome("abbadbcwdg"))
print(solver.longestPalindrome("ccc"))

# a:2, b:3, c:1, d:2, w: 1, g:1



