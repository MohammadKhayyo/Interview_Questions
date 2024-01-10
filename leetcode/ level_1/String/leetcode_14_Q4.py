"""Longest Common Prefix"""
"""Link to the problem: https://leetcode.com/problems/longest-common-prefix/"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        size = len(strs)
        # if size is 0, return empty string
        if (size == 0):
            return ""

        if (size == 1):
            return strs[0]

        # sort the array of strings
        strs.sort()

        # find the minimum length from
        # first and last string
        end = min(len(strs[0]), len(strs[size - 1]))

        # find the common prefix between
        # the first and last string
        i = 0
        while i < end and strs[0][i] == strs[size - 1][i]:
            i += 1

        pre = strs[0][0: i]
        return pre


if __name__ == '__main__':
    solution = Solution()
    Input = {"strs": ["flower", "flow", "flight"]}
    print(f"Input:{Input}")
    Output = solution.longestCommonPrefix(Input["strs"])
    print(f"Output:{Output}")
