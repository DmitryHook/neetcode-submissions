class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        result = 0
        cost = 0
        left = 0

        for right in range(n):
            cost += abs(ord(s[right]) - ord(t[right]))
            
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
    