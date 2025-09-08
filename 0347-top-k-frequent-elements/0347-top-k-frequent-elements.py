class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for val in nums:
            if val not in dic:
                dic[val]=1
            else:
                dic[val]+=1
        lst=list(dic.values())
        lst.sort(reverse=True)
        res=[]
        for i in range(k):
            val=lst[i]
            d=dic.copy()
            for j in d:
                if dic[j]==val:
                    res.append(j)
                    del dic[j]
        return res