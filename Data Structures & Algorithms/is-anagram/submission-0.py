from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1

        return all(value == 0 for value in count.values())
