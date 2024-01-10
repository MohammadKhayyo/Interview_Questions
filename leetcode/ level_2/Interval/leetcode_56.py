"""Merge Intervals"""
"""Link to the problem: https://leetcode.com/problems/merge-intervals/"""
from typing import (
    List,
)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output


if __name__ == '__main__':
    solution = Solution()
    Input = {"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}
    print(f"Input:{Input}")
    Output = solution.merge(Input["intervals"])
    print(f"Output:{Output}")
