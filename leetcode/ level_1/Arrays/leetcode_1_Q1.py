"""Two Sum"""
"""Link to the problem: https://leetcode.com/problems/two-sum/"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create an empty hashmap
        num_map = {}

        # Traverse through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the difference needed to achieve the target
            diff = target - num

            # Check if the difference is already in the hashmap
            if diff in num_map:
                # Return the index from the hashmap and the current index
                return [num_map[diff], i]

            # Add the current number and its index to the hashmap
            num_map[num] = i
        return [0, 0]


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums": [2, 7, 11, 15], "target": 9}
    print(f"Input:{Input}")
    Output = solution.twoSum(Input["nums"], Input["target"])
    print(f"Output:{Output}")
