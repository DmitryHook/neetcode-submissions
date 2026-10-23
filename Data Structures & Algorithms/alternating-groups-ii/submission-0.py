class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        result = 0
        length = 1

        for i in range(1, n + k - 1):
            prev = colors[(i - 1) % n]
            curr = colors[i % n]

            if curr != prev:
                length += 1
            else:
                length = 1

            if length >= k:
                result += 1

        return result
