"""Counting Bits"""
"""Link to the problem: https://leetcode.com/problems/counting-bits/"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


if __name__ == '__main__':
    solution = Solution()
    Input = {"n": 5}
    print(f"Input:{Input}")
    Output = solution.countBits(Input["n"])
    print(f"Output:{Output}")
