class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            left = s.find(ch)
            right = s.rfind(ch)

            if left < right:
                result += len(set(s[left + 1: right]))

        return result