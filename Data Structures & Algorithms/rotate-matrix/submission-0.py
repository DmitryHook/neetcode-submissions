class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            for column in range(row + 1, n):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column]
                )

        for row in matrix:
            row.reverse()