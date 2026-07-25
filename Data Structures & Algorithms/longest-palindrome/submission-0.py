class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        result = 0
        has_odd = False

        for count in counts.values():
            if count % 2 == 0:
                result += count
            else:
                result += count - 1
                has_odd = True

        return result + has_odd