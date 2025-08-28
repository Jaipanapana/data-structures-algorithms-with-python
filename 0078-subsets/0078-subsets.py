class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(temp,i,nums):
            if i>=len(nums):
                res.append(temp[:])
                return
            else:
                temp.append(nums[i])
                backtrack(temp,i+1,nums)
                temp.pop()
                backtrack(temp,i+1,nums)
        backtrack([],0,nums)
        return res
        