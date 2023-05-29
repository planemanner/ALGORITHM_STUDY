"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        s_len = len(s)
        for idx in range(s_len):
            substring = {}
            idy = idx

            while idy < s_len:
                if s[idy] not in substring:
                    substring[s[idy]] = 1
                else:
                    result = max(result, len(substring))
                    break
                idy += 1

            result = max(result, len(substring))
        return result


class BetterSolution:
    # Sliding Window
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        res = []
        window = ""
        for ch in s:
            if ch not in window:
                window += ch
            else:
                res.append(len(window))
                window = window[window.index(ch)+1:] + ch

        res.append(len(window))
        if not len(res) or len(window) > max(res):
            return len(window)

        return max(res)


solver = Solution()
print(solver.lengthOfLongestSubstring("abcabcbb"))
print(solver.lengthOfLongestSubstring(" "))
print(solver.lengthOfLongestSubstring("dvdf"))
print(solver.lengthOfLongestSubstring("dvadfabdcde"))