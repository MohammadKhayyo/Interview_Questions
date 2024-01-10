"""Add Binary"""
"""Link to the problem: https://leetcode.com/problems/add-binary/"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            ans.append(str(carry % 2))
            carry //= 2

        return ''.join(ans[::-1])


if __name__ == '__main__':
    solution = Solution()
    Input = {"a": "11", "b": "1"}
    print(f"Input:{Input}")
    Output = solution.addBinary(Input["a"], Input["b"])
    print(f"Output:{Output}")
