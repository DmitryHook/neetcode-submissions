class Solution:

    def __init__(self, w: list[int]):
        self.prefix = []

        total = 0

        for weight in w:
            total += weight
            self.prefix.append(total)

        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        left, right = 0, len(self.prefix) - 1

        while left < right:
            mid = left + (right - left) // 2

            if self.prefix[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
