class Solution:
    def trap(self, heights: List[int]) -> int:
        if len(heights) < 3:
            return 0

        left = 0
        right = len(heights) - 1
        max_left, max_right = 0, 0
        total = 0

        while left < right:
            if heights[left] < heights[right]:
                if heights[left] >= max_left:
                    max_left = heights[left]
                else:
                    total += max_left - heights[left]
                left += 1
            else:
                if heights[right] >= max_right:
                    max_right = heights[right]
                else:
                    total += max_right - heights[right]
                right -= 1

        return total