class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            left = i
            right = len(temperatures) - 1
            res = 0

            while left < right:
                if temperatures[right] > temperatures[left]:

                    res = right - left
                    
                right -= 1

            result[i] = res

        return result