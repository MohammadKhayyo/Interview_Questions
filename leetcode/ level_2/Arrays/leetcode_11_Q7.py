"""Container With Most Water"""
"""Link to the problem: https://leetcode.com/problems/container-with-most-water/"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1

        while l < r:
            minHeight = min(height[l], height[r])
            ans = max(ans, minHeight * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    Input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input:{Input}")
    Output = solution.maxArea(Input)
    print(f"Output:{Output}")
