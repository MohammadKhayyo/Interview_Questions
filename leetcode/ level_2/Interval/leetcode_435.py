"""Non-overlapping Intervals"""
"""Link to the problem: https://leetcode.com/problems/non-overlapping-intervals/"""

from typing import (
    List,
)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"intervals": [[1, 2], [2, 3], [3, 4], [1, 3]]}
    print(f"Input:{Input}")
    Output = solution.eraseOverlapIntervals(Input["intervals"])
    print(f"Output:{Output}")
