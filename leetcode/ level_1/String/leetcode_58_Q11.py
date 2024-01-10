"""Length of Last Word"""
"""Link to the problem: https://leetcode.com/problems/length-of-last-word/"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1
        lastIndex = i
        while i >= 0 and s[i] != ' ':
            i -= 1

        return lastIndex - i


if __name__ == '__main__':
    solution = Solution()
    Input = {"s": "Hello World"}
    print(f"Input:{Input}")
    Output = solution.lengthOfLastWord(Input["s"])
    print(f"Output:{Output}")
