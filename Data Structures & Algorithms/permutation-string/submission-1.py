class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        memory = defaultdict(int)
        left = 0

        for ch in s1:
            memory[ch] += 1

        for right, ch in enumerate(s2):
            memory[ch] -= 1

            if memory[ch] == 0:
                del memory[ch]

            if right - left + 1 > len(s1):
                left_ch = s2[left]
                memory[left_ch] += 1
                if memory[left_ch] == 0:
                    del memory[left_ch]
                left += 1

            if not memory:
                return True

        return False