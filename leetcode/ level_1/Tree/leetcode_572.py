"""Subtree of Another Tree"""
"""Link to the problem: https://leetcode.com/problems/subtree-of-another-tree/"""

from typing import (
    Optional,
)


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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Recursion DFS (pre-order)"""
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    solution = Solution()
    root = [3, 4, 5, 1, 2, None, None, None, None, 0]
    subRoot = [4, 1, 2]
    # Build the tree
    root_p = solution.build_tree(root)
    root_q = solution.build_tree(subRoot)
    print(solution.isSubtree(root_p, root_q))

    root = [3, 4, 5, 1, 2]
    subRoot = [4, 1, 2]
    # Build the tree
    root_p = solution.build_tree(root)
    root_q = solution.build_tree(subRoot)
    print(solution.isSubtree(root_p, root_q))
