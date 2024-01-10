"""Coin Change"""
"""Link to the problem: https://leetcode.com/problems/coin-change/"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    solution = Solution()
    Input = {"coins": [1, 2, 5], "amount": 11}
    print(f"Input:{Input}")
    Output = solution.coinChange(Input["coins"], Input["amount"])
    print(f"Output:{Output}")
