"""Top K Frequent Elements"""
"""Link to the problem: https://leetcode.com/problems/top-k-frequent-elements/"""

from typing import (
    List
)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [1, 1, 1, 2, 2, 3], "k": 2}
    print(f"Input:{Input}")
    Output = solution.topKFrequent(Input["nums"], Input["k"])
    print(f"Output:{Output}")
