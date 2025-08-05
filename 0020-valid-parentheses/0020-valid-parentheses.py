class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={")":"(","}":"{","]":"["}
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif len(stack)==0 or char not in dic or stack.pop(-1)!=dic[char]:
                return False
        if len(stack)==0:
            return True
        return False

