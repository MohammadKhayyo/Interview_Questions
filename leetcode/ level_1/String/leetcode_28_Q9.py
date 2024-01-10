"""Find the Index of the First Occurrence in a String"""
"""Link to the problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    Input = {"haystack": "sadbutsad", "needle": "sad"}
    print(f"Input:{Input}")
    Output = solution.strStr(Input["haystack"], Input["needle"])
    print(f"Output:{Output}")
