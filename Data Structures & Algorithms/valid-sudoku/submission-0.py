class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            for j in range(9):
                digit = board[i][j]
                
                if digit == '.':
                    continue
                    
                if digit in row_set:
                    return False
                
                row_set.add(digit)

        for j in range(9):
            col_set = set()
            for i in range(9):
                digit = board[i][j]
                
                if digit == '.':
                    continue
                    
                if digit in col_set:
                    return False
                
                col_set.add(digit)

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                square_set = set()

                for i in range(3):
                    for j in range(3):
                        row = start_row + i
                        col = start_col + j

                        digit = board[row][col]

                        if digit == '.':
                            continue

                        if digit in square_set:
                            return False

                        square_set.add(digit)

        return True
