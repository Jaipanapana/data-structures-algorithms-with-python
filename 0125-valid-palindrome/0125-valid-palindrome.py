class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for char in s:
            if char==' ':
                continue
            if char.isalnum():
                res+=char
        res=res.lower()
        if res==res[::-1]:
            return True
        return False
        