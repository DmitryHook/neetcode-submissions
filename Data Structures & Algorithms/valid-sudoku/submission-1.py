class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                digit = board[row][col]

                if digit == '.':
                    continue

                square_idx = (row // 3) * 3 + (col // 3)

                if (digit in row_set[row] or
                    digit in col_set[col] or
                    digit in square_set[square_idx]):
                    return False

                row_set[row].add(digit)
                col_set[col].add(digit)
                square_set[square_idx].add(digit)

        return True