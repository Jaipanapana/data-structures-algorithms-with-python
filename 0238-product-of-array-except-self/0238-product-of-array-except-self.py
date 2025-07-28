class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*(len(nums))
        prefix=sufix=1
        for i in range(len(nums)):
            output[i]*=prefix
            prefix*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i]*=sufix
            sufix*=nums[i]
        return output