class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potion_count = len(potions)
        result = []

        for spell in spells:
            left = 0
            right = potion_count

            while left < right:
                middle = (left + right) // 2

                if spell * potions[middle] >= success:
                    right = middle
                else:
                    left = middle + 1

            result.append(potion_count - left)

        return result
