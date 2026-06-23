class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums * 2

        length = len(nums)

        result = [0] * (2 * length)

        for i in range(length):
            result[i] = nums[i]
            result[i + length] = nums[i]

        return result