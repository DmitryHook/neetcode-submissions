class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        unmatched_count = 0

        for ch in s:
            if ch == '[':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    unmatched_count += 1
                    balance = 0
        
        return (unmatched_count + 1) // 2