class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        result = 0

        for x in nums:
            prefix += x
            result += count[prefix - goal]
            count[prefix] += 1

        return result