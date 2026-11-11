class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words_count = {}

        for word in s1.split() + s2.split():
            words_count[word] = words_count.get(word, 0) + 1

        return [word for word, count in words_count.items() if count == 1]
