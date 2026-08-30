class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prefix = 0
        min_length = len(nums)

        seen = {0: -1}

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            needed = (prefix - target + p) % p

            if needed in seen:
                min_length = min(min_length, i - seen[needed])

            seen[prefix] = i

        if min_length == len(nums):
            return -1

        return min_length