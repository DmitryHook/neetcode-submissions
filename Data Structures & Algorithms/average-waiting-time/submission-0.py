class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        result = 0

        for arrival, time in customers:
            if curr_time < arrival:
                curr_time = arrival
            
            curr_time += time
            result += curr_time - arrival

        return result / len(customers)