"""Longest Repeating Character Replacement"""
"""Link to the problem: https://leetcode.com/problems/longest-repeating-character-replacement/"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxFrequency = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFrequency = max(maxFrequency, count[s[r]])

            while (r - l + 1) - maxFrequency > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"s": "ABAB", "k": 2}
    print(f"Input:{Input}")
    Output = solution.characterReplacement(Input["s"], Input["k"])
    print(f"Output:{Output}")
