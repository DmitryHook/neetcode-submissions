class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_length = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - left - 1

        for i in range(len(s)):
            left, length = expand(i, i)
            if length > max_length:
                start = left
                max_length = length

            left, length = expand(i, i + 1)
            if length > max_length:
                start = left
                max_length = length

        return s[start:start + max_length]