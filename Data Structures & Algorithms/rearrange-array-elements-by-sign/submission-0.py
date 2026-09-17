class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        positive = 0
        negative = 1

        for value in nums:
            if value > 0:
                result[positive] = value
                positive += 2
            else:
                result[negative] = value
                negative += 2
            
        return result