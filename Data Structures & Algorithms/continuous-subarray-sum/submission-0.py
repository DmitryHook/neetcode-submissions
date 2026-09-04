class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}
        prefix_sum = 0

        for i, x in enumerate(nums):
            prefix_sum += x
            remainder = prefix_sum % k

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False
