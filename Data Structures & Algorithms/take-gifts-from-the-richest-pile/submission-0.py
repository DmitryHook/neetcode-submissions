import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        for _ in range(k):
            max_value = heapq.heappop_max(gifts)

            heapq.heappush_max(gifts, math.isqrt(max_value))

        return sum(gifts)