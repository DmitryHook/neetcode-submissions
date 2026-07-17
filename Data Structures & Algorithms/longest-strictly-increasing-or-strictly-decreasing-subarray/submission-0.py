class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increment, decrement = 1, 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increment += 1
                decrement = 1
            elif nums[i] < nums[i - 1]:
                decrement += 1
                increment = 1
            else:
                increment = decrement = 1
            
            longest = max(longest, increment, decrement)

        return longest
