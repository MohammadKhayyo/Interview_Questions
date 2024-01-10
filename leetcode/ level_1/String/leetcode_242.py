"""Valid Anagram"""
"""Link to the problem: https://leetcode.com/problems/valid-anagram/"""

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = collections.Counter(s)
        count.subtract(collections.Counter(t))
        return all(freq == 0 for freq in count.values())  # freq1 == 0 and freq2 == 0 ......

    # def isAnagram(self, s: str, t: str) -> bool:
    # """solution 2"""
    #     if len(s) != len(t):
    #         return False
    #
    #     return collections.Counter(s) == collections.Counter(t)

    # def isAnagram(self, s: str, t: str) -> bool:
    #     """solution 3, memory o(1) , time o(nlog(n))"""
    #     if len(s) != len(t):
    #         return False
    #
    #     return sorted(s) == sorted(t)


if __name__ == '__main__':
    solution = Solution()
    Input = {"s": "anagram", "t": "nagaram"}
    print(f"Input:{Input}")
    Output = solution.isAnagram(Input["s"], Input["t"])
    print(f"Output:{Output}")
