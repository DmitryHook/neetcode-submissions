
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        left = 0
        right = length - 1

        while left < right:
            middle = (left + right) // 2

            if mountainArr.get(middle) < mountainArr.get(middle + 1):
                left = middle + 1
            else:
                right = middle

        peak = left

        left = 0
        right = peak

        while left <= right:
            middle = (left + right) // 2
            value = mountainArr.get(middle)

            if value == target:
                return middle
            elif value < target:
                left = middle + 1
            else:
                right = middle - 1

        left = peak + 1
        right = length - 1

        while left <= right:
            middle = (left + right) // 2
            value = mountainArr.get(middle)

            if value == target:
                return middle
            elif value > target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
