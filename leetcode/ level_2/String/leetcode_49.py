"""Group Anagrams"""
"""Link to the problem: https://leetcode.com/problems/group-anagrams/"""

from typing import (
    List,
)

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()


if __name__ == '__main__':
    solution = Solution()
    Input = {"strs": ["eat", "tea", "tan", "ate", "nat", "bat"]}
    print(f"Input:{Input}")
    Output = solution.groupAnagrams(Input["strs"])
    print(f"Output:{Output}")
