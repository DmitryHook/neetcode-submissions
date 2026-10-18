class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled = s + s

        flips = 0
        min_flips = n
        left = 0

        for right in range(2 * n):
            expected = '0' if right % 2 == 0 else '1'

            if doubled[right] != expected:
                flips += 1

            if right - left + 1 > n:
                expected_left = '0' if left % 2 == 0 else '1'

                if doubled[left] != expected_left:
                    flips -= 1

                left += 1

            if right - left + 1 == n:
                min_flips = min(min_flips, flips, n - flips)

        return min_flips
