"""House Robber II"""
"""Link to the problem: https://leetcode.com/problems/house-robber-ii/"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, •••]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         if not nums:
#             return 0
#
#         def rob(l: int, r: int) -> int:
#             rob1, rob2 = 0, 0
#             # [rob1, rob2, n, n+1, •••]
#             for i in range(l, r + 1):
#                 temp = max(nums[i] + rob1, rob2)
#                 rob1 = rob2
#                 rob2 = temp
#             return rob2
#
#         return max(nums[0], rob(0, len(nums) - 2), rob(1, len(nums) - 1))

if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [2, 3, 2]}
    print(f"Input:{Input}")
    Output = solution.rob(Input["nums"])
    print(f"Output:{Output}")
