class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_res = 0

        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                pop_index = stack.pop()
                curr_height = heights[pop_index]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_res = max(max_res, curr_height * width)
                
            stack.append(i)

        return max_res