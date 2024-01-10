"""Number of Provinces"""
"""https://leetcode.com/problems/number-of-provinces/"""

from typing import (
    List,
)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    res -= union(i, j)
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"isConnected": [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]}
    print(f"Input:{Input}")
    Output = solution.findCircleNum(Input["isConnected"])
    print(f"Output:{Output}")

    Input = {"isConnected": [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]}
    print(f"Input:{Input}")
    Output = solution.findCircleNum(Input["isConnected"])
    print(f"Output:{Output}")
