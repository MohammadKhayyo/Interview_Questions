"""Median of Two Sorted Arrays"""
"""Link to the problem: https://leetcode.com/problems/median-of-two-sorted-arrays/"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        l = 0
        r = n1

        while l <= r:
            partition1 = (l + r) // 2
            partition2 = (n1 + n2 + 1) // 2 - partition1
            maxLeft1 = -2 ** 31 if partition1 == 0 else nums1[partition1 - 1]
            maxLeft2 = -2 ** 31 if partition2 == 0 else nums2[partition2 - 1]
            minRight1 = 2 ** 31 - 1 if partition1 == n1 else nums1[partition1]
            minRight2 = 2 ** 31 - 1 if partition2 == n2 else nums2[partition2]
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(
                    maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                r = partition1 - 1
            else:
                l = partition1 + 1


if __name__ == '__main__':
    solution = Solution()
    Input = {"nums1": [1, 3], "nums2": [2]}
    print(f"Input:{Input}")
    Output = solution.findMedianSortedArrays(Input["nums1"], Input["nums2"])
    print(f"Output:{Output}")

    Input = {"nums1": [1, 3, 5], "nums2": [7, 9]}
    print(f"Input:{Input}")
    Output = solution.findMedianSortedArrays(Input["nums1"], Input["nums2"])
    print(f"Output:{Output}")
