"""Zigzag Conversion"""
"""Link to the problem: https://leetcode.com/problems/zigzag-conversion/"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        k = 0
        direction = (numRows == 1) - 1

        for c in s:
            rows[k] += c
            if k == 0 or k == numRows - 1:
                direction *= -1
            k += direction

        return ''.join(rows)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    print("Input:", s)
    numRows = 3
    solution = Solution()
    _s = solution.convert(s, numRows)
    print("Output:", _s)
