class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        s_idx = 0

        for r in range(1, len(chars) + 1):
            if r == len(chars) or chars[r] != chars[l]:
                length = r - l
                chars[s_idx] = chars[l]
                s_idx += 1
                if length > 1:
                    for char in str(length):
                        chars[s_idx] = char
                        s_idx += 1
                l = r

        return s_idx