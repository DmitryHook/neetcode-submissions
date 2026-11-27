class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        for i in range(n):
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1

            if nums[n - 1 - i] > pivot:
                result[right] = nums[n - 1 - i]
                right -= 1
            
        for i in range(left, right + 1):
            result[i] = pivot
        
        return result
