class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            key=''.join(sorted(word))
            if key in dic:
                dic[key].append(word)
            else:
                dic[key]=[word]
        result=list()
        for key in dic:
            result.append(dic[key])
        return result