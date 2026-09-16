class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_words = []
        current_length = 0

        for word in words:
            required_length = current_length + len(word) + len(current_words)

            if required_length > maxWidth:
                gaps = len(current_words) - 1
                total_spaces = maxWidth - current_length

                if gaps == 0:
                    line = current_words[0] + ' ' * total_spaces
                else:
                    spaces_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps

                    line = ''

                    for index, current_word in enumerate(current_words):
                        line += current_word

                        if index < gaps:
                            spaces = spaces_per_gap

                            if index < extra_spaces:
                                spaces += 1

                            line += ' ' * spaces

                result.append(line)

                current_words = []
                current_length = 0

            current_words.append(word)
            current_length += len(word)

        last_line = ' '.join(current_words)
        last_line += ' ' * (maxWidth - len(last_line))

        result.append(last_line)

        return result