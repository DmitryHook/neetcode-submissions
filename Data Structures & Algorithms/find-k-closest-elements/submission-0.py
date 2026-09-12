class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid + k] - x < x - arr[mid]:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]