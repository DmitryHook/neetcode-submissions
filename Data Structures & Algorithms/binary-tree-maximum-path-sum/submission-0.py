# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)

            return node.val + max(left_sum, right_sum)

        dfs(root)

        return self.max_sum
        