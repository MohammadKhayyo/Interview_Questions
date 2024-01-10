"""323. Number of Connected Components in an Undirected Graph"""
"""Link to the problem: https://www.lintcode.com/problem/3651/"""
from typing import (
    List,
)


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
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
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"n": 3, "edges": [[0, 1], [0, 2]]}
    print(f"Input:{Input}")
    Output = solution.count_components(Input["n"], Input["edges"])
    print(f"Output:{Output}")

    Input = {"n": 6, "edges": [[0, 1], [1, 2], [2, 3], [4, 5]]}
    print(f"Input:{Input}")
    Output = solution.count_components(Input["n"], Input["edges"])
    print(f"Output:{Output}")
