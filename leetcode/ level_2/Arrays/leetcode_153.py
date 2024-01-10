"""Find Minimum in Rotated Sorted Array"""
"""Link to the problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        if l > r:
            return -1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [3, 4, 5, 1, 2]}
    print(f"Input:{Input}")
    Output = solution.findMin(Input["nums"])
    print(f"Output:{Output}")

    Input = {"nums": [1, 2, 3, 4, 5]}
    print(f"Input:{Input}")
    Output = solution.findMin(Input["nums"])
    print(f"Output:{Output}")

    Input = {"nums": [1]}
    print(f"Input:{Input}")
    Output = solution.findMin(Input["nums"])
    print(f"Output:{Output}")

    Input = {"nums": []}
    print(f"Input:{Input}")
    Output = solution.findMin(Input["nums"])
    print(f"Output:{Output}")
