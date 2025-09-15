class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        count=0
        for i in text:
            flag=0
            for j in brokenLetters:
                if j in i:
                    flag=1
                    break
            if flag==0:
                count+=1
        return count
            
            