class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left=top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        res=[]
        while top<=bottom and left<=right:
            # first row
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            # last column
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            # bottom row
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            # first column
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res