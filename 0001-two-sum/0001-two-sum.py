class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,num in enumerate(nums):
            val=target-num
            if val in dic:
                return [dic[val],i]
            dic[num]=i
        