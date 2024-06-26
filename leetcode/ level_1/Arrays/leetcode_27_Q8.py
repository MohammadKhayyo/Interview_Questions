"""Remove Element"""
"""Link to the problem: https://leetcode.com/problems/remove-element/"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Counter for keeping track of elements other than val
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not val
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [3, 2, 2, 3], "val": 3}
    print(f"Input:{Input}")
    Output = solution.removeElement(Input["nums"], Input["val"])
    print(f"Output:{Output}")
