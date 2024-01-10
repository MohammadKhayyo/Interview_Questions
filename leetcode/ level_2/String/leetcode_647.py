"""Palindromic Substrings"""
"""Link to the problem: https://leetcode.com/problems/palindromic-substrings/"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        def extend(s: str, l: int, r: int) -> tuple[int, int, int]:
            """
            Returns the (start, end) indices of the longest palindrome extended from
            the substring s[i..j].
            """
            res = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
                res += 1
            return l + 1, r - 1, res

        sumResults = 0
        for i in range(len(s)):
            l1, r1, res = extend(s, i, i)  # ODD,    ABA
            sumResults += res
            if i + 1 < len(s) and s[i] == s[i + 1]:  # EVEN,   BAAB
                l2, r2, res = extend(s, i, i + 1)
                sumResults += res
        return sumResults


if __name__ == '__main__':
    solution = Solution()
    Input = {"s": "abc"}
    print(f"Input:{Input}")
    Output = solution.countSubstrings(Input["s"])
    print(f"Output:{Output}")

    Input = {"s": "aaa"}
    print(f"Input:{Input}")
    Output = solution.countSubstrings(Input["s"])
    print(f"Output:{Output}")
