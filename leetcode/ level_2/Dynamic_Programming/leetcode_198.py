"""House Robber"""
"""Link to the problem: https://leetcode.com/problems/house-robber/"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, •••]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [1, 2, 3, 1]}
    print(f"Input:{Input}")
    Output = solution.rob(Input["nums"])
    print(f"Output:{Output}")
