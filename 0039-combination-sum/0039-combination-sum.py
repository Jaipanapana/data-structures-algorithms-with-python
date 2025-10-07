class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(temp,i):
            if sum(temp)==target:
                res.append(temp[:])
                return
            if sum(temp)>target:
                return
            while i<len(candidates):
                temp.append(candidates[i])
                backtrack(temp,i)
                temp.pop()
                i+=1
        backtrack([],0)
        return res