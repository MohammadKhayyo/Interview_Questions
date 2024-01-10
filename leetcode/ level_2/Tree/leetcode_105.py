"""Construct Binary Tree from Preorder and Inorder Traversal"""
"""Link to the problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/"""

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

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # Build the tree
    root_p = solution.buildTree(preorder, inorder)
    print(solution.tree_to_list(root_p))
