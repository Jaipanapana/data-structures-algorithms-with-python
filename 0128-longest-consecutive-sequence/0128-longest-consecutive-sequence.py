class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=sorted(list(set(nums)))
        print(nums)
        count=val=1
        for i in range(len(nums)-1):
            print(nums[i]+1,nums[i+1])
            if nums[i]+1==nums[i+1]:
                count+=1
            else:
                if val<count:
                    print(count)
                    val=count
                count=1
        if val<count:
            val=count
        return val
        