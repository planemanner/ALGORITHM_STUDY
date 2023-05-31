"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside

the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces,

square brackets are well-formed, etc. Furthermore,

you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.

For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]" => a2[c] a2[c] a2[c] => acc acc acc
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef" =>
Output: "abcabccdcdcdef"

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


class Solution:
    def decodeString(self, s: str) -> str:

        def find_bracket(_string):
            # Constraint : _string 의 가장 처음 문자는 [ 이다.
            left_bracket = [_string[0]]
            idx = 1

            while left_bracket:
                if _string[idx] == "[":
                    left_bracket.append(_string[idx])
                elif _string[idx] == "]":
                    left_bracket.pop()
                    if len(left_bracket) == 0:
                        return idx
                idx += 1

        def decode(remain: str, result: str):

            if len(remain) == 0:
                return result

            if remain[0].isdigit():
                idx = 0
                while remain[idx].isdigit():
                    idx += 1

                new_remain = ""
                right_idx = find_bracket(remain[idx:])

                for _ in range(int(remain[:idx])):
                    new_remain += remain[idx+1:idx+right_idx]

                new_remain += remain[idx+right_idx+1:]

                return decode(new_remain, result)

            elif remain[0].isalpha():
                return decode(remain[1:], result + remain[0])

        result = decode(s, "")

        return result


solver = Solution()
print(solver.decodeString("3[a]2[bc]"))
print(solver.decodeString("3[a2[c]]"))
print(solver.decodeString("2[abc]3[cd]ef"))
print(solver.decodeString("100[leetcode]"))