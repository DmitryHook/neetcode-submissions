class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for right, value in enumerate(nums):
            while q and nums[q[-1]] < value:
                q.pop()

            q.append(right)

            if q[0] < right - k + 1:
                q.popleft()

            if right >= k - 1:
                res.append(nums[q[0]])

        return res