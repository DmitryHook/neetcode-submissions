class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_matrix, right_matrix = 0, len(matrix) - 1

        while left_matrix <= right_matrix:
            mid_matrix = (left_matrix + right_matrix) // 2

            if matrix[mid_matrix][0] <= target <= matrix[mid_matrix][-1]:
                left_number, right_number = 0, len(matrix[mid_matrix]) - 1

                while left_number <= right_number:
                    mid_number = (left_number + right_number) // 2

                    if matrix[mid_matrix][mid_number] == target:
                        return True
                    elif matrix[mid_matrix][mid_number] < target:
                        left_number = mid_number + 1
                    else:
                        right_number = mid_number - 1

                return False

            if target < matrix[mid_matrix][0]:
                right_matrix = mid_matrix - 1
            else:
                left_matrix = mid_matrix +1

        return False