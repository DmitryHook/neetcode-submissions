class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        curr = 0
        result = 0

        for num in nums:
            curr += num
            result += count[curr - k]
            count[curr] += 1
        
        return result