class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for index, value in enumerate(nums):
            if not stack or value < nums[stack[-1]]:
                stack.append(index)

        max_width = 0

        for right_index in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[right_index]:
                left_index = stack.pop()
                max_width = max(max_width, right_index - left_index)

        return max_width
