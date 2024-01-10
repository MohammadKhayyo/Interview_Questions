"""Kth Smallest Element in a BST"""
"""Link to the problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/"""

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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


if __name__ == '__main__':
    solution = Solution()
    root = [3, 1, 4, None, 2]
    # Build the tree
    root_p = solution.build_tree(root)
    print(solution.kthSmallest(root_p, 1))

    root = [5, 3, 6, 2, 4, None, None, 1]
    # Build the tree
    root_p = solution.build_tree(root)
    print(solution.kthSmallest(root_p, 3))
