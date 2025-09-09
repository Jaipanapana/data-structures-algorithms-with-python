class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not(s):
            return 0
        j=count=i=0
        max_val=float("-inf")
        while j<len(s):
            while s[j] in s[i:j]:
                i+=1
                count-=1
            count+=1
            max_val=max(max_val,count)
            j+=1
        return max_val
            

        