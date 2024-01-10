"""Decode Ways"""
"""Link to the problem: https://leetcode.com/problems/decode-ways/"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    Input = {"s": "121"}
    print(f"Input:{Input}")
    Output = solution.numDecodings(Input["s"])
    print(f"Output:{Output}")

    Input = {"s": "127"}
    print(f"Input:{Input}")
    Output = solution.numDecodings(Input["s"])
    print(f"Output:{Output}")
