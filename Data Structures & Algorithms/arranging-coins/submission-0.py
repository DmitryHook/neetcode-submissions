class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n

        while low <= high:
            mid = low + (high - low) // 2
            result = mid * (mid + 1) // 2

            if result == n:
                return mid
            elif result < n:
                low = mid + 1
            else:
                high = mid - 1
        
        return high