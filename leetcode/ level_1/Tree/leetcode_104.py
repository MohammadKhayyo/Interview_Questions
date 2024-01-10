"""Maximum Depth of Binary Tree"""
"""Link to the problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/"""

from typing import (
    Optional,
)

from collections import deque


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

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     """Recursion DFS (post-order)"""
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     """BFS Iteration (level-order)"""
    #     if not root:
    #         return 0
    #     level = 0
    #     q = deque([root])
    #     while q:
    #         size = len(q)
    #         for i in range(size):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         level += 1
    #     return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """DFS Iteration (pre-order)"""
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return res


if __name__ == '__main__':
    solution = Solution()
    input_arr = [3, 9, 20, None, None, 15, 7]
    print(f"Input:{input_arr}")
    # Build the tree
    root = solution.build_tree(input_arr)

    _maxDepth = solution.maxDepth(root)
    print(f"maxDepth:{_maxDepth}")
    result_list = solution.tree_to_list(root)
    print(result_list)
