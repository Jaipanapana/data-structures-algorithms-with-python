class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        min_start=r=l=0
        min_len=float('inf')
        t_dic={}
        window_s={}
        for char in t:
            if char in t_dic:
                t_dic[char]+=1
            else:
                t_dic[char]=1
        formed=0
        required=len(t_dic)
        while r<len(s) :
            ch=s[r]
            if ch in window_s:
                window_s[ch]+=1
            else:
                window_s[ch]=1
            if ch in t_dic and t_dic[ch]==window_s[ch] :
                formed+=1
            while l<=r and formed==required :
                if r-l+1<min_len :
                    min_len=r-l+1
                    min_start=l
                char=s[l]
                window_s[char]-=1
                if char in t_dic and window_s[char]<t_dic[char] :
                    formed-=1
                l+=1
            r+=1
        if min_len == float('inf'):
            return ""
        else:
            return s[min_start:min_start+min_len]

        
        
        