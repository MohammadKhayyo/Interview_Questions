"""Best Time to Buy and Sell Stock"""
"""Link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

from typing import (
    List
)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP


if __name__ == '__main__':
    solution = Solution()
    Input = {"prices": [7, 1, 5, 3, 6, 4]}
    print(f"Input:{Input}")
    Output = solution.maxProfit(Input["prices"])
    print(f"Output:{Output}")
