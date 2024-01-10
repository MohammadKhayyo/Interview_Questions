"""Plus One"""
"""Link to the problem: https://leetcode.com/problems/plus-one/"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i, d in reversed(list(enumerate(digits))):
            if d < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


if __name__ == '__main__':
    solution = Solution()
    Input = {"digits": [1, 2, 3]}
    print(f"Input:{Input}")
    Output = solution.plusOne(Input["digits"])
    print(f"Output:{Output}")
