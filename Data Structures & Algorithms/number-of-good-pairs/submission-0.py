class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)

        return sum(count * (count - 1) // 2 for count in counts.values())