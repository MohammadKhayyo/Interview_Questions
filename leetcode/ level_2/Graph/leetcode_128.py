"""Longest Consecutive Sequence"""
"""Link to the problem: https://leetcode.com/problems/longest-consecutive-sequence/"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [100, 4, 200, 1, 3, 2]}
    print(f"Input:{Input}")
    Output = solution.longestConsecutive(Input["nums"])
    print(f"Output:{Output}")
