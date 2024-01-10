"""Sqrt(x)"""
"""Link to the problem: https://leetcode.com/problems/sqrtx/"""


class Solution:
    def mySqrt(self, x: int) -> int:
        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2

        return int(result)


if __name__ == '__main__':
    solution = Solution()
    Input = {"x": 4}
    print(f"Input:{Input}")
    Output = solution.mySqrt(Input["x"])
    print(f"Output:{Output}")
