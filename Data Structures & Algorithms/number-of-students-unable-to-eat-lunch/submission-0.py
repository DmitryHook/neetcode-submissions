class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)

        for i, sandwich in enumerate(sandwiches):
            if counts[sandwich] == 0:
                return len(sandwiches) - i
            counts[sandwich] -= 1

        return 0