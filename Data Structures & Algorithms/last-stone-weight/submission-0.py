class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        values = [-stone for stone in stones]
        heapq.heapify(values)

        while len(values) > 1:
            stone_1 = heapq.heappop(values)
            stone_2 = heapq.heappop(values)

            if stone_1 != stone_2:
                heapq.heappush(values, (stone_1 - stone_2))

        return -values[0] if values else 0
