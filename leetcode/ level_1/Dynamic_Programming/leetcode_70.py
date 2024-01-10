"""Climbing Stairs"""
"""Link to the problem: https://leetcode.com/problems/climbing-stairs/"""


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


if __name__ == '__main__':
    solution = Solution()
    Input = {"n": 5}
    print(f"Input:{Input}")
    Output = solution.climbStairs(Input["n"])
    print(f"Output:{Output}")
