class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result=[-1]*len(nums)
        n=len(nums)
        for i in range(n):
            j=i+1
            max_val=nums[i]
            while (j%n)!=i:
                if max_val<nums[j%n]:
                    max_val=nums[j%n]
                    break
                j+=1
            if max_val!=nums[i]:
                result[i]=max_val
        return result
        