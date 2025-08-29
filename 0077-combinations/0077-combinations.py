class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n=list(range(1,n+1))
        res=[]
        def backtrack(n,temp,k,i):
            if k==0 :
                res.append(temp[:])
                return
            else:
                while i<len(n):
                    temp.append(n[i])
                    backtrack(n,temp,k-1,i+1)
                    temp.pop()
                    i+=1
        backtrack(n,[],k,0)
        return res


        