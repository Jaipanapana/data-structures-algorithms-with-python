class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(sub,i):
            if sum(sub)==target:
                res.append(sub[:])
                return
            elif sum(sub)>target:
                return
            else:
                prev=-1
                while i<len(candidates):
                    if candidates[i] == prev:
                        i+=1
                        continue
                    sub.append(candidates[i])
                    backtrack(sub,i+1)
                    sub.pop()
                    prev=candidates[i]
                    i+=1

        backtrack([],0)
        return res
