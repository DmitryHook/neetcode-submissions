class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = k

        for i in range(len(blocks) - k + 1):
            window = blocks[i:i + k]
            ops = window.count('W')
            result = min(result, ops)

        return result