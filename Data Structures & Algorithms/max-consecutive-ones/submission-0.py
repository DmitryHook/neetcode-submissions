class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, maximum = 0, 0

        for num in nums:
            if num == 1:
                curr += 1
                maximum = max(maximum, curr)
            else:
                curr = 0
        
        return maximum