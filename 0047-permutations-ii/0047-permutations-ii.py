class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(temp,used):
            if len(temp)==len(nums) and temp not in res:
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                temp.append(nums[i])
                backtrack(temp,used)
                used.remove(i)
                temp.pop()
        backtrack([],set())
        return res
        