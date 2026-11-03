class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped_index = 0

        for value in pushed:
            stack.append(value)

            while stack and stack[-1] == popped[popped_index]:
                stack.pop()
                popped_index += 1

        return not stack
