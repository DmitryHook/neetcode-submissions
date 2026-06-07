import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not any(num != 0 for num in nums) or nums.count(0) > 1:
            return [0] * len(nums)

        if nums.count(0) == 1:
            result = math.prod(num for num in nums if num != 0)
            return [0 if num != 0 else result for num in nums]

        result = math.prod(num for num in nums if num != 0)

        for i, val in enumerate(nums):
            if val != 0:
                nums[i] = result // nums[i]

        return nums
