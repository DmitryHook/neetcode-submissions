class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7

        nums.sort()

        left, right = 0, len(nums) - 1
        result = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                result += pow(2, right - left, MOD)
                result %= MOD
                left += 1
            else:
                right -= 1

        return result