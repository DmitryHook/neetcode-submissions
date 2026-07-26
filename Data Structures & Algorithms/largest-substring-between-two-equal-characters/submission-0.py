class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indeces = {}
        result = -1

        for i, char in enumerate(s):
            if char in indeces:
                length = i - indeces[char] - 1
                result = max(result, length)
            else:
                indeces[char] = i

        return result