"""Longest Increasing Subsequence"""
"""Link to the problem: https://leetcode.com/problems/longest-increasing-subsequence/"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [10, 9, 2, 5, 3, 7, 101, 18]}
    print(f"Input:{Input}")
    Output = solution.lengthOfLIS(Input["nums"])
    print(f"Output:{Output}")
