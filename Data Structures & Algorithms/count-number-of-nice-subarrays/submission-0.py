class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}

        prefix_sum = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                prefix_sum += 1

            req_sum = prefix_sum - k

            result += prefix_counts.get(req_sum, 0)

            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

        return result
