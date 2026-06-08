class Solution:
    def trap(self, heights: List[int]) -> int:
        if len(heights) < 3:
            return 0

        max_left = [0] * len(heights)
        max_left[0] = heights[0]
        for i in range(1, len(heights)):
            max_left[i] = max(max_left[i-1], heights[i])

        max_right = [0] * len(heights)
        max_right[-1] = heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], heights[i])

        total = 0
        for i in range(len(heights)):
            total += min(max_left[i], max_right[i]) - heights[i]

        return total