class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        for _ in range(k):
            num, i = heapq.heappop(heap)

            num *= multiplier
            nums[i] = num

            heapq.heappush(heap, (num, i))

        return nums