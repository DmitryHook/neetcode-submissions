class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        curr_vowels = 0

        for idx in range(k):
            if s[idx] in vowels:
                curr_vowels += 1

        max_vowels = curr_vowels

        for idx in range(k, len(s)):
            if s[idx - k] in vowels:
                curr_vowels -= 1

            if s[idx] in vowels:
                curr_vowels += 1
            
            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels
