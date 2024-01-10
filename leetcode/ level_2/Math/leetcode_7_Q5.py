"""Reverse Integer"""
"""Link to the problem: https://leetcode.com/problems/reverse-integer/"""


class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = -1 if x < 0 else 1
        x *= sign

        while x:
            ans = ans * 10 + x % 10
            x //= 10

        return 0 if ans < -2 ** 31 or ans > 2 ** 31 - 1 else sign * ans


if __name__ == '__main__':
    solution = Solution()
    Input = -123
    print("Input: ", Input)
    Output = solution.reverse(Input)
    print("Output:", Output)
