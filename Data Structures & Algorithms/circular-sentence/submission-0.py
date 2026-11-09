class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for index in range(len(words)):
            current_word = words[index]
            next_word = words[(index + 1) % len(words)]

            if current_word[-1] != next_word[0]:
                return False

        return True
