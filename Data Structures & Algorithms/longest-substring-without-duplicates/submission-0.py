class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_result = 0
        l_idx = 0

        for r_idx, value in enumerate(s):
            if value in char_index and char_index[value] >= l_idx:
                l_idx = char_index[value] + 1
            
            max_result = max(max_result, r_idx - l_idx + 1)
            
            char_index[value] = r_idx

        return max_result
