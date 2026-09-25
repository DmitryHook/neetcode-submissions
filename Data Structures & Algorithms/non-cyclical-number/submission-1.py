class Solution:
    def isHappy(self, n: int) -> bool:
        existing = set()

        while n != 1 and n not in existing:
            existing.add(n)

            new_n = 0
            x = n

            while x > 0:
                d = x % 10
                new_n += d * d
                x //= 10
            n = new_n

        return n == 1