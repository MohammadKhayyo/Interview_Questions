"""261. Graph Valid Tree"""
"""Link to the problem: https://www.lintcode.com/problem/178/"""
from typing import (
    List,
)


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)


if __name__ == '__main__':
    solution = Solution()
    Input = {"n": 5, "edges": [[0, 1], [0, 2], [0, 3], [1, 4]]}
    print(f"Input:{Input}")
    Output = solution.valid_tree(Input["n"], Input["edges"])
    print(f"Output:{Output}")

    Input = {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]}
    print(f"Input:{Input}")
    Output = solution.valid_tree(Input["n"], Input["edges"])
    print(f"Output:{Output}")
