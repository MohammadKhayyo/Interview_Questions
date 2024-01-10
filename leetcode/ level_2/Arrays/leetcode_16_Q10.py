"""3Sum Closest"""
"""Link to the problem: https://leetcode.com/problems/3sum-closest/"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Choose nums[i] as the first number in the triplet, then search the
            # remaining numbers in [i + 1, n - 1].
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:
                    return summ
                if abs(summ - target) < abs(ans - target):
                    ans = summ
                if summ < target:
                    l += 1
                else:
                    r -= 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [-1, 2, 1, -4], "target": 1}
    print(f"Input:{Input}")
    Output = solution.threeSumClosest(Input["nums"], Input["target"])
    print(f"Output:{Output}")
