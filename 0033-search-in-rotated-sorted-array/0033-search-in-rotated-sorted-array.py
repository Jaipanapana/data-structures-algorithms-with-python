class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(l,r,nums):
            while l<r:
                mid=(l+r)//2
                if nums[mid]>nums[r]:
                    l=mid+1
                else:
                    r=mid
            return r
        def search(l,r,nums,target):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return -1
        idx=-1
        n=len(nums)-1
        pivot_index=find_pivot(0,n,nums)
        idx=search(0,pivot_index-1,nums,target)
        if idx!=-1:
            return idx
        idx=search(pivot_index,n,nums,target)
        return idx