class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ops = 0
        
        for count in freq.values():
            if count == 1:
                return -1

            ops += count // 3

            if count % 3 != 0:
                ops += 1

        return ops