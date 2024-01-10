"""Rotate Image"""
"""Link to the problem: https://leetcode.com/problems/rotate-image/"""
from typing import (
    List,
)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1


if __name__ == '__main__':
    solution = Solution()
    Input = {"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
    print(f"Input:{Input}")
    solution.rotate(Input["matrix"])
    print(f"Output:{Input}")
