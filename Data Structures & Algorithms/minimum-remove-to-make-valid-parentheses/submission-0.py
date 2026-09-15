class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = set()
        
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    invalid.add(index)

        invalid.update(stack)

        result = []

        for index, char in enumerate(s):
            if index not in invalid:
                result.append(char)

        return ''.join(result)