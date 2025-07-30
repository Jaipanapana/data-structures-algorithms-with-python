class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletset=set()
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            if nums[i]>0:
                break
            rem=0-nums[i]
            while j<k:
                sum=nums[j]+nums[k]
                if sum==rem:
                    triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
                    tripletset.add(triplet)
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                        continue
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                        continue
                    j+=1
                    k-=1
                elif sum>rem:
                    k-=1
                else:
                    j+=1
        return [list(triplet) for triplet in tripletset]

