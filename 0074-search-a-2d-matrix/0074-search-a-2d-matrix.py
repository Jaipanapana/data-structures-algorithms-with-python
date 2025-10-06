class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        start=0
        end=rows*cols-1
        while start<=end:
            mid=(start+end)//2
            if matrix[mid//cols][mid%cols]==target:
                return True
            elif matrix[mid//cols][mid%cols]>target:
                end=mid-1
            else:
                start=mid+1
        return False
        
            

                