class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image

        rows = len(image)
        columns = len(image[0])

        def dfs(row: int, column: int) -> None:
            if (
                row < 0
                or row >= rows
                or column < 0
                or column >= columns
                or image[row][column] != original_color
            ):
                return

            image[row][column] = color

            dfs(row - 1, column)
            dfs(row + 1, column)
            dfs(row, column - 1)
            dfs(row, column + 1)

        dfs(sr, sc)

        return image