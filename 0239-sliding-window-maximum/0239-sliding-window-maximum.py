class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        result=list()
        dq=list()
        n=len(nums)
        val=k
        while i<n:
            ele=nums[i]
            while len(dq)!=0 and dq[-1]<ele:
                dq.pop(-1)
            dq.append(ele)
            if i>=k-1:
                result.append(dq[0])
            if len(dq)!=0 and i>=k-1 and dq[0]==nums[i-k+1]:
                dq.pop(0)     
            i+=1
        return result
           
            