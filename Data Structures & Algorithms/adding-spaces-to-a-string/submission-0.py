class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_idx = 0

        for i, ch in enumerate(s):
            if space_idx < len(spaces) and spaces[space_idx] == i:
                result.append(' ')
                space_idx += 1
            result.append(ch)

        return ''.join(result)
