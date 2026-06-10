class Solution:
    def minWindow(self, s: str, t: str) -> str:
        memory = defaultdict(int)
        left, cur_size = 0, 0
        res = ""

        for ch in t:
            memory[ch] += 1 

        for right, ch in enumerate(s):
            if ch in memory:
                memory[ch] -= 1

                if memory[ch] == 0:
                    cur_size += 1

            while cur_size == len(memory):
                cur_window = s[left:right + 1]

                if not res or len(cur_window) < len(res):
                    res = cur_window

                left_ch = s[left]
                if left_ch in memory:
                    if memory[left_ch] == 0:
                        cur_size -= 1
                    memory[left_ch] += 1
                left+=1

        return res