"""Maximum Product Subarray"""
"""Link to the problem: https://leetcode.com/problems/maximum-product-subarray/"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [-2, 0, -1]}
    print(f"Input:{Input}")
    Output = solution.maxProduct(Input["nums"])
    print(f"Output:{Output}")
