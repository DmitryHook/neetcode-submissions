# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        if not root:
            return None

        stack = deque([root])

        while stack:
            node = stack.popleft()

            if p.val <= node.val <= q.val:
                return node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

