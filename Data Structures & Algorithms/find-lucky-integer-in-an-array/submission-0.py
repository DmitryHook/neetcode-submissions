class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        result = [num for num, freq in counts.items() if num == freq]

        return max(result) if result else -1 