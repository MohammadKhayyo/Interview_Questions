"""Palindrome Number"""
"""Link to the problem: https://leetcode.com/problems/palindrome-number/"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        rev = 0
        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10
        if rev == x:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    Input = {"x": 121}
    print(f"Input:{Input}")
    Output = solution.isPalindrome(Input["x"])
    print(f"Output:{Output}")
