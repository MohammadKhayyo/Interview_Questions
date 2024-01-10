"""String to Integer (atoi)"""
"""Link to the problem: https://leetcode.com/problems/string-to-integer-atoi/"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] in {'-', '+'}:
            s = s[1:]

        num = 0

        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + ord(c) - ord('0')
            if sign * num <= -2 ** 31:
                return -2 ** 31
            if sign * num >= 2 ** 31 - 1:
                return 2 ** 31 - 1

        return sign * num


if __name__ == '__main__':
    solution = Solution()
    Input = "42"
    print(f"Input:{Input}")
    Output = solution.myAtoi(Input)
    print(f"Output:{Output}")

    Input = "   -42"
    print(f"Input:{Input}")
    Output = solution.myAtoi(Input)
    print(f"Output:{Output}")

    Input = " +4193 with words"
    print(f"Input:{Input}")
    Output = solution.myAtoi(Input)
    print(f"Output:{Output}")
