class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101
        for height in heights:
            counts[height] += 1

        result = 0
        excepted = 0
        for i, height in enumerate(heights):
            while counts[excepted] == 0:
                excepted += 1
            if height != excepted:
                result += 1
            counts[excepted] -= 1

        return result

        # excepted = sorted(heights)
        # return sum(h != e for h, e in zip(heights, excepted))