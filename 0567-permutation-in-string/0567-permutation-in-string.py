class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=len(s1)
        for i in range(len(s2)-l+1):
            if sorted(s1)==sorted(s2[i:i+l]):
                return True
        return  False