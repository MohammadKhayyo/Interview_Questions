"""Validate Binary Search Tree"""
"""Link to the problem: https://leetcode.com/problems/validate-binary-search-tree/"""

from typing import (
    Optional
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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))


if __name__ == '__main__':
    solution = Solution()
    root = [5, 1, 4, None, None, 3, 6]
    # Build the tree

    root_p = solution.build_tree(root)
    print(solution.isValidBST(root_p))
