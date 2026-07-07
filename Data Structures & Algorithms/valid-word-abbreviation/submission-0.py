class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        num = ""

        while i < len(word) and j < len(abbr):

            while j < len(abbr) and abbr[j].isdigit():
                if abbr[j] == "0" and num == "":
                    return False

                num += abbr[j]
                j += 1

            if num != "":
                i += int(num)
                num = ""

                if i > len(word):
                    return False

                if j == len(abbr):
                    break

            if i >= len(word):
                return False

            if word[i] != abbr[j]:
                return False

            i += 1
            j += 1
            
        return i == len(word) and j == len(abbr)