class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = Counter(chars)
        result = 0

        for word in words:
            word_counts = Counter(word)
            if all(word_counts[c] <= counts[c] for c in word_counts):
                result += len(word)

        return result