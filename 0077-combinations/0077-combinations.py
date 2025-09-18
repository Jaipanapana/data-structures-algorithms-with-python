class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(temp,j):
            if len(temp)==k:
                res.append(temp[:])
                return
            while j<=n:
                temp.append(j)
                backtrack(temp,j+1)
                temp.pop()
                j+=1
        backtrack([],1)
        return res
        