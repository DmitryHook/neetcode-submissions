class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        memory = defaultdict(int)
        res = []

        for right, digit in enumerate(nums):
            memory[digit] += 1

            if right - left + 1 == k:
                res.append(max(memory))

                left_digit = nums[left]
                memory[left_digit] -= 1
                if memory[left_digit] == 0:
                    del memory[left_digit]

                left += 1

        return res