"""252. Meeting Rooms"""
"""Link to the problem: https://www.lintcode.com/problem/920/"""
from typing import (
    List,
)

# from lintcode import (
#     Interval,
# )

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
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    Input = {"intervals": [Interval(0, 30), Interval(5, 10), Interval(15, 20)]}
    print(f"Input:{Input}")
    Output = solution.can_attend_meetings(Input["intervals"])
    print(f"Output:{Output}")
