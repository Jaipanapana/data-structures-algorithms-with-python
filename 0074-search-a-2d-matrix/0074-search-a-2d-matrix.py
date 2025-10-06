class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)-1,-1,-1):
            for c in range(len(matrix[0])-1,-1,-1):
                if matrix[r][c]==target:
                    return True
                elif matrix[r][c]<target:
                    break
        return False                    
                