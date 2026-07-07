class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            L, R = 0, len(row)-1
            while L <= R:
                M = (R + L)//2
                if row[M] == target:
                    return True 
                elif row[M] < target:
                    L = M + 1
                else:
                    R = M - 1
        return False


        