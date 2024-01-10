"""Binary Tree Level Order Traversal"""
import collections

"""Link to the problem: https://leetcode.com/problems/binary-tree-level-order-traversal/"""

from typing import (
    Optional, List
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

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


if __name__ == '__main__':
    solution = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    # Build the tree
    root_p = solution.build_tree(root)
    print(solution.levelOrder(root_p))
