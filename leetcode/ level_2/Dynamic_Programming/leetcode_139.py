"""Word Break"""
"""Link to the problem: https://leetcode.com/problems/word-break/"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # _list = []   # reconstruction
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    # _list.append(w)
                    break
        # print(_list[::-1])
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    Input = {"s": "leetcode", "wordDict": ["leet", "code"]}
    print(f"Input:{Input}")
    Output = solution.wordBreak(Input["s"], Input["wordDict"])
    print(f"Output:{Output}")

    Input = {"s": "applepenapple", "wordDict": ["apple", "pen"]}
    print(f"Input:{Input}")
    Output = solution.wordBreak(Input["s"], Input["wordDict"])
    print(f"Output:{Output}")

    Input = {"s": "catsandog", "wordDict": ["cats", "dog", "sand", "and", "cat"]}
    print(f"Input:{Input}")
    Output = solution.wordBreak(Input["s"], Input["wordDict"])
    print(f"Output:{Output}")
