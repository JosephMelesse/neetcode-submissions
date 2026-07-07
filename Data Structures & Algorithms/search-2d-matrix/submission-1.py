class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T, B = 0, len(matrix) - 1
        L, R = 0, len(matrix[0]) - 1
        row = None
        while T <= B:
            M = (T + B)//2
            if (target < matrix[T][0]) or (target > matrix[B][-1]):
                return False
            if (target <= matrix[M][-1]) and (target >= matrix[M][0]):
                row = M
                break 
            elif target < matrix[M][0]:
                B = M - 1
            else:
                T = M + 1

        while L <= R and (row is not None):
            M = (R + L)//2
            if matrix[row][M] == target:
                return True 
            elif matrix[row][M] < target:
                L = M + 1
            else:
                R = M - 1
        return False


        