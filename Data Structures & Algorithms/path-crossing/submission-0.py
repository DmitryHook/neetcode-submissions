class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        coordinate = (0, 0)

        for way in path:
            if way == "N":
                coordinate = (coordinate[0], coordinate[1] + 1)
            elif way == "S":
                coordinate = (coordinate[0], coordinate[1] - 1)
            elif way == "E":
                coordinate = (coordinate[0] + 1, coordinate[1])
            else:
                coordinate = (coordinate[0] - 1, coordinate[1])

            if coordinate in visited:
                return True
            else:
                visited.add(coordinate)
            
        return False
