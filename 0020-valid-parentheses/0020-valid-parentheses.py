class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        for bracket in s:
            if bracket in "({[":
                lst.append(bracket)
            elif len(lst)!=0 and (bracket==")" and lst[-1]=="(" or bracket=="}" and lst[-1]=="{" or bracket=="]" and lst[-1]=="["):
                lst.pop(-1)
            else:
                return False
        if len(lst)==0:
            return True
        return False
                
                   