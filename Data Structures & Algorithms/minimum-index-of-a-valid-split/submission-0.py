class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)

        major = max(freq, key=freq.get)
        total_count = freq[major]

        left_count = 0

        for i in range(n - 1):
            if nums[i] == major:
                left_count += 1

            left_length = i + 1
            right_length = n - left_length
            right_count = total_count - left_count

            if (left_count * 2 > left_length and 
                right_count * 2 > right_length):
                    return i

        return -1