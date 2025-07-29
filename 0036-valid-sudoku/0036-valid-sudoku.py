class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row=set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                elif board[i][j] in row:
                    return False
                else:
                    row.add(board[i][j])
        for i in range(9):
            col=set()
            for j in range(9):
                if board[j][i]=='.':
                    continue
                elif board[j][i] in col:
                    return False
                else:
                    col.add(board[j][i])
        dic={}
        for i in range(9):
            for j in range(9):
                val=str(i//3)+str(j//3)
                if board[i][j]=='.':
                    continue
                if val not in dic:
                    dic[val]=[]
                if board[i][j] in dic[val]:
                    return False
                else:
                    dic[val].append(board[i][j])
        return True

                
        
        