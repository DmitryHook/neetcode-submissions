class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        team_count = len(skill) // 2
        total_skill = sum(skill)

        if total_skill % team_count != 0:
            return -1

        target_skill = total_skill // team_count

        left = 0
        right = len(skill) - 1

        total_chemistry = 0

        while left < right:
            if skill[left] + skill[right] != target_skill:
                return -1

            total_chemistry += skill[left] * skill[right]

            left += 1
            right -= 1

        return total_chemistry
