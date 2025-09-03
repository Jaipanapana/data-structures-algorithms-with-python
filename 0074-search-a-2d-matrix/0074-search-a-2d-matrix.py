class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        length=len(matrix)
        while i<length:
            m=0
            n=len(matrix[i])-1
            while m<=n:
                mid=(m+n)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]<target:
                    m=mid+1
                else:
                    n=mid-1
            i+=1
        return False        