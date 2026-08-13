class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}

        for c in nums:
            freq[c] = freq.get(c, 0) + 1
        return sorted(nums, key=lambda x: (freq[x], -x))