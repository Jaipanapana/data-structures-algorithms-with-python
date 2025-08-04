class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        print(s)
        count=0
        for char in s[::-1]:
            if char==" ":
                break
            count+=1
        return count