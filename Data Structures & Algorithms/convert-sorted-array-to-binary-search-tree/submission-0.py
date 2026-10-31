class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build_tree(left, right):
            if left > right:
                return None

            middle = (left + right) // 2

            root = TreeNode(nums[middle])

            root.left = build_tree(left, middle - 1)
            root.right = build_tree(middle + 1, right)

            return root

        return build_tree(0, len(nums) - 1)
