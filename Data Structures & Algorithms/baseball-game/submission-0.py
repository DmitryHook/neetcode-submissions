class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        actions = {
            "+": lambda: stack.append(stack[-1] + stack[-2]),
            "D": lambda: stack.append(stack[-1] * 2),
            "C": lambda: stack.pop(),
        }

        for operation in operations:
            if operation not in actions:
                stack.append(int(operation))
            else:
                actions[operation]()

        return sum(stack)