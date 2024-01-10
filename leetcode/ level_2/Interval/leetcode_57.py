"""Insert Interval"""
"""Link to the problem: https://leetcode.com/problems/insert-interval/"""
from typing import (
    List,
)
_

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]}
    print(f"Input:{Input}")
    Output = solution.insert(Input["intervals"], Input["newInterval"])
    print(f"Output:{Output}")

    Input = {"intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], "newInterval": [4, 8]}
    print(f"Input:{Input}")
    Output = solution.insert(Input["intervals"], Input["newInterval"])
    print(f"Output:{Output}")
