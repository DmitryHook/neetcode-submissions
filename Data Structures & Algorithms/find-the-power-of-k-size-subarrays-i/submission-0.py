class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        streak = 0

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1

            if i >= k - 1:
                result.append(nums[i] if streak >= k else -1)

        return result
