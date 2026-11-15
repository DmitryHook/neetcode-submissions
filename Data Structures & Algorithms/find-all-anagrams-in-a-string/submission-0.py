class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        char_count = defaultdict(int)

        for char in p:
            char_count[char] += 1

        left = 0
        result = []

        for right in range(len(s)):
            char_count[s[right]] -= 1

            if right - left + 1 > len(p):
                char_count[s[left]] += 1
                left += 1

            if right - left + 1 == len(p) and all(
                count == 0 for count in char_count.values()
            ):
                result.append(left)

        return result
