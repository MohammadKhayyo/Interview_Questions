"""Maximum Subarray"""
"""Link to the problem: https://leetcode.com/problems/maximum-subarray/"""

import math


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currSum = 0
        ans = -math.inf
        for num in nums:
            currSum = max(num, currSum + num)
            ans = max(ans, currSum)
        return ans


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}
    print(f"Input:{Input}")
    Output = solution.maxSubArray(Input["nums"])
    print(f"Output:{Output}")
