"""Longest Common Subsequence"""
"""Link to the problem: https://leetcode.com/problems/longest-common-subsequence/"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  # o(n * m)
        n = len(text1)  # row
        m = len(text2)  # col
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    Input = {"text1": "abcde", "text2": "ace"}
    print(f"Input:{Input}")
    Output = solution.longestCommonSubsequence(Input["text1"], Input["text2"])
    print(f"Output:{Output}")

    solution = Solution()
    Input = {"text1": "abcba", "text2": "abcbcba"}
    print(f"Input:{Input}")
    Output = solution.longestCommonSubsequence(Input["text1"], Input["text2"])
    print(f"Output:{Output}")
