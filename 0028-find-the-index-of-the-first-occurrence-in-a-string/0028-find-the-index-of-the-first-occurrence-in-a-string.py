class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r=len(needle)
        result=-1
        for i in range(len(haystack)-r+1):
            if haystack[i]==needle[0]:
                if haystack[i:r+i]==needle:
                    result=i
                    break
        return result

        