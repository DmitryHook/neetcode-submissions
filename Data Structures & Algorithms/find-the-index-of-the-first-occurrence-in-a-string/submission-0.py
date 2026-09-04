class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1

        lps = self._build_lps(needle)

        i, j = 0, 0
        n, m = len(haystack), len(needle)

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            
            if j == m:
                return i - m
        
        return -1

    def _build_lps(self, needle: str) -> list[int]:
        m = len(needle)
        lps = [0] * m
        prevLPS = 0
        i = 1

        while i < m:
            if needle[i] == needle[prevLPS]:
                prevLPS += 1
                lps[i] = prevLPS
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        return lps