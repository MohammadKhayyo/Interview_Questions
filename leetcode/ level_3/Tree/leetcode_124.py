"""Binary Tree Maximum Path Sum"""
"""Link to the problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/"""

from typing import (
    Optional,
)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert_level_order(self, arr, root, i, n):
        # Base case for recursion
        if i < n:
            if arr[i] is not None:
                temp = TreeNode(arr[i])
                root = temp

                # insert left child
                root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)

                # insert right child
                root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
            else:
                root = None
        return root

    # Function to build the tree and return the root
    def build_tree(self, arr):
        n = len(arr)
        root = None
        return self.insert_level_order(arr, root, 0, n)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     # return max path sum without split
    #     def dfs(root, res=0):
    #         if not root:
    #             return 0, float("-inf")
    #         left, wl = dfs(root.left)
    #         left = max(left, 0)
    #
    #         right, wr = dfs(root.right)
    #         right = max(right, 0)
    #
    #         res = max(wl, wr, root.val + left + right)
    #         return root.val + max(left, right), res
    #
    #     _, res = dfs(root)
    #     return res


if __name__ == '__main__':
    solution = Solution()
    root = [-10, 9, 20, None, None, 15, 7]
    # Build the tree
    root_p = solution.build_tree(root)
    print(solution.maxPathSum(root_p))
