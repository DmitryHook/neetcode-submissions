class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        counts = [0] * (n * n + 1)

        for row in grid:
            for num in row:
                counts[num] += 1

        a, b = 0, 0

        for num in range(1, n*n+1):
            if counts[num] == 2:
                a = num
            elif counts[num] == 0:
                b = num

        return [a, b]