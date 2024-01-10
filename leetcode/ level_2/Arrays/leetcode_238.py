"""Product of Array Except Self"""
"""Link to the problem: https://leetcode.com/problems/product-of-array-except-self/"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [1, 2, 3, 4]}
    print(f"Input:{Input}")
    Output = solution.productExceptSelf(Input["nums"])
    print(f"Output:{Output}")
