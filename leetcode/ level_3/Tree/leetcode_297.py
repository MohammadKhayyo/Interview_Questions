"""Serialize and Deserialize Binary Tree"""
"""Link to the problem: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
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

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


if __name__ == '__main__':
    solution = Codec()
    root = [1, 2, 3, None, None, 4, 5]
    # Build the tree
    root_p = solution.build_tree(root)
    ser = solution.serialize(root_p)
    deser = solution.deserialize(ser)
    print(solution.tree_to_list(deser))
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
