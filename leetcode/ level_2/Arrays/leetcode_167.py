"""Two Sum II - Input Array Is Sorted"""
"""Link to the problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [2, 7, 11, 15], "target": 9}
    print(f"Input:{Input}")
    Output = solution.twoSum(Input["nums"], Input["target"])
    print(f"Output:{Output}")
