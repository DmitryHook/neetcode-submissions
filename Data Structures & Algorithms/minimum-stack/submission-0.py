class MinStack:

    def __init__(self):
        self.stack = []
        self.min_nums = []

    def push(self, val: int) -> None:
        self.stack.append(val)     
        self.min_nums.append(min(val, self.min_nums[-1]) if self.min_nums else val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_nums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_nums[-1]