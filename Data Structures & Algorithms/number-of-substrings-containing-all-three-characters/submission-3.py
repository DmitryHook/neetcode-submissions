class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = -1, -1, -1
        result = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                a = i
            elif ch == 'b':
                b = i
            else:
                c = i

            result += min(a, b, c) + 1

        return result
