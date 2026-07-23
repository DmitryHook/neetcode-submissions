class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)

        for char in ransomNote:
            if counts[char] <= 0:
                return False
            else:
                counts[char] -= 1

        return True