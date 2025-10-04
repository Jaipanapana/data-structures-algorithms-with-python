class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        maxValue=0
        for currRow in matrix:
            inverted=[0]*len(currRow)
            for i in range(len(currRow)):
                if currRow[i]==0:
                    inverted[i]=1
                else:
                    inverted[i]=0
            count=0
            for row in matrix:
                if row==currRow or row==inverted:
                    count+=1
            maxValue=max(maxValue,count)
        return maxValue

        