class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        left = 0
        right = nums[-1] - nums[0]
        n = len(nums)

        def can_make_pairs(max_difference: int) -> bool:
            pairs = 0
            index = 0

            while index < n - 1:
                if nums[index + 1] - nums[index] <= max_difference:
                    pairs += 1
                    index += 2

                    if pairs == p:
                        return True
                else:
                    index += 1

            return False

        while left < right:
            max_difference = (left + right) // 2

            if can_make_pairs(max_difference):
                right = max_difference
            else:
                left = max_difference + 1

        return left