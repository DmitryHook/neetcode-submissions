# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = deque([root])
        result = []

        while stack:
            result.append([])
            
            for _ in range(len(stack)):
                node = stack.popleft()

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

                result[-1].append(node.val)

        return result