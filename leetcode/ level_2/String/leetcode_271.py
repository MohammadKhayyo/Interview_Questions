"""271. Encode and Decode Strings"""
"""Link to the problem: https://leetcode.com/problems/palindromic-substrings/"""


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1

            length = int(str[i:j])
            res.append(str[(j + 1):(j + 1) + length])
            i = j + 1 + length

        return res


if __name__ == '__main__':
    solution = Solution()
    Input = {"str": ["lint", "code", "love", "you"]}
    print(f"Input:{Input}")
    Output = solution.encode(Input["str"])
    print(f"encode:{Output}")
    Output = solution.decode(Output)
    print(f"decode:{Output}")
