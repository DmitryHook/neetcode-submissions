class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        memory, left, count = defaultdict(int), 0, 0

        for right, cur_char in enumerate(fruits):
            memory[cur_char] += 1

            while len(memory) > 2:
                left_char = fruits[left]
                memory[left_char] -= 1

                if memory[left_char] == 0:
                    del memory[left_char]

                left += 1
                
            count = max(count, right - left + 1)

        return count