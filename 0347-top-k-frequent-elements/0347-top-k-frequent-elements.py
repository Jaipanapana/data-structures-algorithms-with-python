class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        check=0
        lst=list()
        for i in dic:
            lst.append(dic[i])
        lst.sort(reverse=True)
        val=0
        result=list()
        val=0
        while(val<k):
            for key in dic:
                if lst[val]==dic[key]:
                    result.append(key)
                    del dic[key]
                    break
            val+=1
        return result



        