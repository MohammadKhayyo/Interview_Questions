"""Lowest Common Ancestor of a Binary Search Tree"""
"""Link to the problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


if __name__ == '__main__':
    solution = Solution()
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = TreeNode(2)
    q = TreeNode(8)
    # Build the tree
    root_p = solution.build_tree(root)
    Output = solution.lowestCommonAncestor(root_p, p, q)
    print(Output.val)
