"""Combination Sum"""
"""Link to the problem: https://leetcode.com/problems/combination-sum/"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"candidates": [2, 3, 6, 7], "target": 7}
    print(f"Input:{Input}")
    Output = solution.combinationSum(Input["candidates"], Input["target"])
    print(f"Output:{Output}")
