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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()

            if not node:
                continue

            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return False

