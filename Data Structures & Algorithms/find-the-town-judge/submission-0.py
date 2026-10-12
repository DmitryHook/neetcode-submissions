class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_balance = [0] * (n + 1)

        for person, trusted_person in trust:
            trust_balance[person] -= 1
            trust_balance[trusted_person] += 1

        for person in range(1, n + 1):
            if trust_balance[person] == n - 1:
                return person

        return -1