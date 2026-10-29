class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s)
        n = len(words)
        left = 0

        while left < n:
            right = left
            
            while right < n and words[right] != ' ':
                right += 1

            i, j = left, right - 1
            while i < j:
                words[i], words[j] = words[j], words[i]
                i += 1
                j -= 1

            left = right + 1
        
        return ''.join(words)
