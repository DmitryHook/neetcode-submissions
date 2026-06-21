# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, node: TreeNode, max_value: int) -> int:
        if not node:
            return 0

        count = 1 if node.val >= max_value else 0

        new_max = max(max_value, node.val)

        left_node = self.dfs(node.left, new_max)
        right_node = self.dfs(node.right, new_max)

        return count + left_node + right_node