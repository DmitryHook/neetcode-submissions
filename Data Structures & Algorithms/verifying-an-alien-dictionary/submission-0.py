
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        letter_order = {
            letter: index for index, letter in enumerate(order)
        }

        def is_correct_order(first_word: str, second_word: str) -> bool:
            for first_letter, second_letter in zip(first_word, second_word):
                if letter_order[first_letter] < letter_order[second_letter]:
                    return True

                if letter_order[first_letter] > letter_order[second_letter]:
                    return False

            return len(first_word) <= len(second_word)

        for index in range(len(words) - 1):
            if not is_correct_order(words[index], words[index + 1]):
                return False

        return True
