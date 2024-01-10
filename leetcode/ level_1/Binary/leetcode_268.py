"""Missing Number"""
"""Link to the problem: https://leetcode.com/problems/missing-number/"""


class Solution:

    # def missingNumber(self, nums: list[int]) -> int:  # [0,1,2,4,5],      sum([0,1,2,3,4,5]) - sum([0,1,2,4,5]) = 3
    #     res = len(nums)
    #     for i in range(len(nums)):
    #         res += (i - nums[i])
    #     return res

    def missingNumber(self, nums: list[int]) -> int:  # [0,1,2,4,5], 5^5 =0 ,  0^0 , 1^1 , 2^2,   3,  4^4, 5^5  = 3
        ans = len(nums)

        for i, num in enumerate(nums):
            ans ^= i ^ num

        return ans


if __name__ == '__main__':
    solution = Solution()
    Input = {"n": "00000010100101000001111010011100"}
    print(f"Input:{Input}")
    Output = solution.missingNumber(Input["nums"])
    print(f"Output:{Output}")

    Input = {"nums": [0, 1, 2, 4, 5]}
    print(f"Input:{Input}")
    Output = solution.missingNumber(Input["nums"])
    print(f"Output:{Output}")
