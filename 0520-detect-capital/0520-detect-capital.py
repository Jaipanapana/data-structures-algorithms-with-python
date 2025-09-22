class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c=lower=upper=f1=f2=0
        for i in word:
            if 'a'<=i<='z' :
                if c==0:
                    lower=1
                    c+=1
                f1=1
            else:
                if c==0:
                    upper=1
                    c+=1
                else:
                    f2=1
        if upper==1 and f2==1 and f1==0:
            return True
        elif upper==1 and f2==0 and f1==1:
            return True
        elif lower==1 and f1==1 and f2==0:
            return True
        elif upper==1 and f1==0 and f2==0:
            return True
        return False 
