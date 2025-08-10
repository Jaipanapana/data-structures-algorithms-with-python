class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        result=""
        for word in lst[::-1]:
            result+=word+" "
        return result.strip()