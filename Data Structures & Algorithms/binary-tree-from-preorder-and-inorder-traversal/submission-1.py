# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        next_node = iter(preorder)

        def build_node(left_bound, right_bound):
            if left_bound > right_bound:
                return None

            root_val = next(next_node)
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build_node(left_bound, mid - 1)
            root.right = build_node(mid + 1, right_bound)

            return root

        return build_node(0, len(inorder) - 1)
