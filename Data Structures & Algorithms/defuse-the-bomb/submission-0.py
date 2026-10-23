class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        code *= 2
        result = []

        if k == 0:
            return [0] * n

        for i in range(n):
            if k > 0:
                result.append(sum(code[i + 1 : i + 1 + k]))
            else:
                result.append(sum(code[i + n + k : i + n]))
        
        return result
