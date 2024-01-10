"""Number of 1 Bits"""
"""Link to the problem: https://leetcode.com/problems/number-of-1-bits/"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # Flip the least significant set bit
            count += 1
        return count
