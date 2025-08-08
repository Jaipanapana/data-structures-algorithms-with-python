class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        previous_val=-1
        total=0
        for val in range(len(s)-1,-1,-1):
            if dic[s[val]]<previous_val:
                total-=dic[s[val]]
            else:
                total+=dic[s[val]]
            previous_val=dic[s[val]]
        return total
        