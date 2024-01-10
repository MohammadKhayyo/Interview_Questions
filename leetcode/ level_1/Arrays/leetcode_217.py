"""Contains Duplicate"""
"""Link to the problem: https://leetcode.com/problems/contains-duplicate/"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(nums) != len(set(nums))


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [1, 2, 3, 1]}
    print(f"Input:{Input}")
    Output = solution.containsDuplicate(Input["nums"])
    print(f"Output:{Output}")
