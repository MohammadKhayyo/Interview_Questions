"""Maximum Product of Two Elements in an Array"""
"""Link to the problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/?envType=daily-question&envId=2023-12-12"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                max2, max1 = max1, num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [3, 4, 5, 2]}
    print(f"Input:{Input}")
    Output = solution.maxProduct(Input["nums"])
    print(f"Output:{Output}")
