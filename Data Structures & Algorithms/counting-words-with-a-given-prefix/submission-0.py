class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #return sum(word.startswith(pref) for word in words)

        result = 0
        n = len(pref)

        for word in words:
            if len(word) < n:
                continue
            
            is_prefix = True
            for i in range(n):
                if word[i] != pref[i]:
                    is_prefix = False
                    break

            if is_prefix:
                result += 1

        return result
