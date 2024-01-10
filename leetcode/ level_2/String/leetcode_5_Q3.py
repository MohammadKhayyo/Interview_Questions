"""Longest Palindromic Substring"""
"""Link to the problem: https://leetcode.com/problems/longest-palindromic-substring/"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        # (start, end) indices of the longest palindrome in s
        indices = [0, 0]

        def extend(s: str, l: int, r: int) -> tuple[int, int]:
            """
            Returns the (start, end) indices of the longest palindrome extended from
            the substring s[i..j].
            """
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            l1, r1 = extend(s, i, i)  # ODD,    ABA
            if r1 - l1 > indices[1] - indices[0]:
                indices = l1, r1
            if i + 1 < len(s) and s[i] == s[i + 1]:  # EVEN,   BAAB
                l2, r2 = extend(s, i, i + 1)
                if r2 - l2 > indices[1] - indices[0]:
                    indices = l2, r2

        return s[indices[0]:indices[1] + 1]


if __name__ == '__main__':
    s = "forgeeksskeegfor"
    solution = Solution()
    _s = solution.longestPalindrome(s)
    print("Output:", _s)
