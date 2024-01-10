"""Jump Game"""
"""Link to the problem: https://leetcode.com/problems/jump-game/"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [2, 3, 1, 1, 4]}
    print(f"Input:{Input}")
    Output = solution.canJump(Input["nums"])
    print(f"Output:{Output}")
