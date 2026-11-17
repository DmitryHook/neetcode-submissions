class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        result = 0

        while left <= right:
            middle = (left + right) // 2

            portions = 0

            for pile in candies:
                portions += pile // middle

            if portions >= k:
                result = middle
                left = middle + 1
            else:
                right = middle - 1

        return result
