class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            count = self.count_numbers(n, current, current + 1)

            if count <= k:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1

        return current

    def count_numbers(self, n: int, left: int, right: int) -> int:
        count = 0

        while left <= n:
            count += min(n + 1, right) - left

            left *= 10
            right *= 10

        return count