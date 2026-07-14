class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i, word in enumerate(words):
            for j, another_word in enumerate(words):
                if i != j and word in another_word:
                    result.append(word)
                    break
        
        return result