class Solution:
    def isHappy(self, n: int) -> bool:
        existing = set()

        while n != 1 and n not in existing:
            existing.add(n)

            new_n = 0
            for ch in str(n):
                new_n += int(ch) ** 2
            n = new_n

        return n == 1