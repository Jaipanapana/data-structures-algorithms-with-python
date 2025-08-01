class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        j=len(s1)
        st=s2[:j]
        while(j<=len(s2)):
            if sorted(s1)==sorted(st):
                return True
            i+=1
            j+=1
            st=s2[i:j]
        return False
        