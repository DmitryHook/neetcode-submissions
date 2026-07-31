class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = []

        for char in s:
            if char == ']':
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())

                stack.pop()

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                num = ''.join(num[::-1])

                stack.append(''.join(temp[::-1]) * int(num))

                temp = []

            else:
                stack.append(char)

        return ''.join(stack)