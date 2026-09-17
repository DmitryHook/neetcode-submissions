class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        satisfied = 0

        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]

        current = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                current += customers[i]

        best = current

        for i in range(minutes, n):
            if grumpy[i] == 1:
                current += customers[i]
            
            if grumpy[i - minutes] == 1:
                current -= customers[i - minutes]
            
            if current > best:
                best = current

        return satisfied + best