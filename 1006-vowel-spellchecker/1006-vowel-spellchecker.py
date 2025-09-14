class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        case_error={}
        vowels_error={}
        res=[]
        def conver_to_consonants(word):
            s=''
            for i in word:
                if i in 'aeiouAEIOU':
                    s+='*'
                else:
                    s+=i
            return s

        for word in wordlist:
            if word.lower() not in case_error:
                case_error[word.lower()]=word
            s=conver_to_consonants(word)
            if s.lower() not in vowels_error:
                vowels_error[s.lower()]=word
        
        for word in queries:
            flag1=flag2=flag3=0
            if word in wordlist:
                res.append(word)
                flag1=1
            elif word.lower() in case_error:
                res.append(case_error[word.lower()])
                flag2=1
            elif flag1==0 and flag2==0:
                s=conver_to_consonants(word)
                if s.lower() in vowels_error:
                    res.append(vowels_error[s.lower()])
                    flag3=1
            if flag1==0 and flag2==0 and flag3==0:
                res.append("")
        return res
