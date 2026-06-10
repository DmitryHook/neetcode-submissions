class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memory = defaultdict(int)
        left, max_repeats, result = 0, 0, 0

        for right, cur_char in enumerate(s):
            memory[cur_char] += 1

            max_repeats = max(max_repeats, memory[cur_char])

            while (right - left + 1) - max_repeats > k:
                memory[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result