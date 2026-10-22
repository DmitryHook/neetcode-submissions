class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])
        stack = []

        for i in order:
            if directions[i] == 'R':
                stack.append(i)
                continue
            while stack and healths[i] > 0:
                j = stack[-1]
                if healths[j] < healths[i]:
                    healths[j] = 0
                    stack.pop()
                    healths[i] -= 1
                elif healths[j] > healths[i]:
                    healths[j] -= 1
                    healths[i] = 0
                else:
                    healths[j] = 0
                    healths[i] = 0
                    stack.pop()
        
        return [h for h in healths if h > 0]
