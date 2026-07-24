class Solution:
    def minOperations(self, s: str) -> int:
        changes1, changes2 = 0, 0

        for i, char in enumerate(s):
            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'

            changes1 += 1 if char != expected1 else 0
            changes2 += 1 if char != expected2 else 0

        return min(changes1, changes2)
