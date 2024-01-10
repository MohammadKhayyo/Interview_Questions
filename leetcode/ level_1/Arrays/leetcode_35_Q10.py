"""Search Insert Position"""
"""Link to the problem: https://leetcode.com/problems/search-insert-position/"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [1, 3, 5, 6], "target": 5}
    print(f"Input:{Input}")
    Output = solution.searchInsert(Input["nums"], Input["target"])
    print(f"Output:{Output}")
