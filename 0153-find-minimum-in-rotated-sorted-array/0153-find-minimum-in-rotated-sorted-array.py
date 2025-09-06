class Solution:
    def findMin(self, nums: List[int]) -> int:
        r=len(nums)-1
        l=0
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[r]


        