# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque([p, q])

        while stack:
            node_q = stack.pop()
            node_p = stack.pop()

            if not node_q and not node_p:
                continue
            elif not node_q or not node_p or node_q.val != node_p.val:
                return False

            if node_q.right or node_p.right:
                stack.append(node_p.right)
                stack.append(node_q.right)
            if node_q.left or node_p.left:
                stack.append(node_p.left)
                stack.append(node_q.left)

        return True
