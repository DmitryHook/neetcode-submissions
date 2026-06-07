class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = sorted(set(nums))
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(num_set)):
            if num_set[i] == num_set[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)
