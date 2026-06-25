class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.largest_values = nums
        heapq.heapify(self.largest_values)

        while len(self.largest_values) > k:
            heapq.heappop(self.largest_values)

    def add(self, val: int) -> int:
        if len(self.largest_values) < self.k:
            heapq.heappush(self.largest_values, val)
        elif len(self.largest_values) == self.k:
            if self.largest_values[0] < val:
                heapq.heappop(self.largest_values)
                heapq.heappush(self.largest_values, val)
        return self.largest_values[0]
