from math import gcd


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        pairs = 0

        for width, height in rectangles:
            common_divisor = gcd(width, height)

            ratio = (
                width // common_divisor,
                height // common_divisor
            )

            pairs += ratios.get(ratio, 0)
            ratios[ratio] = ratios.get(ratio, 0) + 1

        return pairs
