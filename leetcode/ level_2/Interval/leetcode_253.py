"""253. Meeting Rooms II"""
"""Link to the problem: https://www.lintcode.com/problem/919/"""
from typing import (
    List,
)

"""Definition of Interval:"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end}]"

    def __repr__(self):
        return self.__str__()


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"intervals": [Interval(0, 30), Interval(5, 10), Interval(15, 20)]}
    print(f"Input:{Input}")
    Output = solution.min_meeting_rooms(Input["intervals"])
    print(f"Output:{Output}")

    Input = {"intervals": [Interval(2, 7)]}
    print(f"Input:{Input}")
    Output = solution.min_meeting_rooms(Input["intervals"])
    print(f"Output:{Output}")
