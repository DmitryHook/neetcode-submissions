class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window_sum = sum(arr[:k])
        result = 0

        if window_sum >= target:
            result += 1

        for right in range(k, len(arr)):
            window_sum += arr[right]
            window_sum -= arr[right - k]

            if window_sum >= target:
                result += 1

        return result