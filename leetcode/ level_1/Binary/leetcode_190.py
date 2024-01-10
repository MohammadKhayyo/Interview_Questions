"""Reverse Bits"""
"""Link to the problem: https://leetcode.com/problems/reverse-bits/"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"n": 43261596}
    print(f"Input:{Input}")
    Output = solution.reverseBits(Input["n"])
    print(f"Output:{Output}")

    print(Output == 964176192)
