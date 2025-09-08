class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not(nums):
            return 0
        nums.sort()
        print(nums)
        max_val=float("-inf")
        count=1
        i=0
        while i<(len(nums)-1):
            if nums[i]==nums[i+1]:
                pass
            elif nums[i]+1==nums[i+1]:
                count+=1
            else:
                max_val=max(count,max_val)
                count=1
            i+=1
        max_val=max(count,max_val)
        return max_val
        