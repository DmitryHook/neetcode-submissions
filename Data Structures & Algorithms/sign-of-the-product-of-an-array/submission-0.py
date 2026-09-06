class Solution:
    def signFunc(self, x: int) -> int:
        if x > 0:
            return 1
        elif x < 0:
            return -1
        return 0

    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
        return self.signFunc(sign)