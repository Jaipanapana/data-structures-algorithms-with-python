class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[-1]*len(nums1)
        for k in range(len(nums1)):
            i=nums2.index(nums1[k])
            j=i+1
            while(j<len(nums2)):
                if nums2[j]>nums1[k]:
                    result[k]=nums2[j]
                    break
                j+=1
        return result

        