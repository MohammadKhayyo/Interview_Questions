"""Unique Paths"""
"""Link to the problem: https://leetcode.com/problems/unique-paths/"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


if __name__ == '__main__':
    solution = Solution()
    Input = {"m": 3, "n": 7}
    print(f"Input:{Input}")
    Output = solution.uniquePaths(Input["m"], Input["n"])
    print(f"Output:{Output}")
