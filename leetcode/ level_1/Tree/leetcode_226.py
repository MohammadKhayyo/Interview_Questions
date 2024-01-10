"""Invert Binary Tree"""
"""Link to the problem: https://leetcode.com/problems/invert-binary-tree/"""

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

    def tree_to_list(self, root):
        if not root:
            return []

        result, queue = [], [root]

        while any(queue):  # as long as there is at least one non-null node
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left if node.left or node.right else None)
                queue.append(node.right if node.left or node.right else None)
            else:
                result.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Recursion DFS (pre-order)"""
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    solution = Solution()
    root = [4, 2, 7, 1, 3, 6, 9]
    # Build the tree
    root_p = solution.build_tree(root)
    solution.invertTree(root_p)
    print(solution.tree_to_list(root_p))
