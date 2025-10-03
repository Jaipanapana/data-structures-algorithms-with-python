from copy import deepcopy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dummy= deepcopy(matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    k=0
                    while k<len(matrix[0]):
                        dummy[i][k]=0
                        k+=1
                    k=0 
                    while k<len(matrix):
                        dummy[k][j]=0 
                        k+=1
        print(dummy)                
        matrix[:]=dummy

