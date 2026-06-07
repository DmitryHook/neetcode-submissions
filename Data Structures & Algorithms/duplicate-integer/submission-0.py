class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = {}
        
        for num in nums:
            if num not in items:
                items[num] = 1
            else:
                return True

        return False