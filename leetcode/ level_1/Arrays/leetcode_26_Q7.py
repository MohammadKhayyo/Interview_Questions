"""Remove Duplicates from Sorted Array"""
"""Link to the problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Return, if array is empty or contains
        # a single element
        n = len(nums)
        if n == 0 or n == 1:
            return n

        temp = list(range(n))

        # Start traversing elements
        j = 0
        for i in range(0, n - 1):

            # If current element is not equal to next
            # then store that current element
            if nums[i] != nums[i + 1]:
                temp[j] = nums[i]
                j += 1

        # Store the last element as whether it is unique
        # or repeated, it isn't stored previously
        temp[j] = nums[n - 1]
        j += 1

        # Modify original array
        for i in range(0, j):
            nums[i] = temp[i]

        return j


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [1, 1, 2]}
    print(f"Input:{Input}")
    Output = solution.removeDuplicates(Input["nums"])
    print(f"Output:{Output}")
