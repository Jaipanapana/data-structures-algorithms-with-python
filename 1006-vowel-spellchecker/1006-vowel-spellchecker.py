class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res=[]
        lower_case=[]
        remove_vowels=[]
        wordlist_updated=[]
        for letter in wordlist:
            word=letter.lower()
            lower_case.append(word)
            s=''
            s1=''
            for i in letter:
                if i not in 'aeiouAEIOU':
                    s+=i
                    s1+=i
                else:
                    s1+='@'
            wordlist_updated.append(s1)
            remove_vowels.append(s)
        for word in queries:
            flag1=0
            flag2=0
            flag3=0
            new_word='' 
            if word in wordlist:
                res.append(word)
                flag2=1
            elif word.lower() in lower_case:
                for i in range(len(wordlist)):
                    if word.lower()==lower_case[i]:
                        res.append(wordlist[i])
                        flag1=1
                        break     
            elif flag1==0 and flag2==0:
                for i in word:
                    if i in 'aeiouAEIOU':
                        new_word+='@'
                    else:
                        new_word+=i
                for i in range(len(wordlist)):
                    if new_word.lower()==wordlist_updated[i].lower():
                        res.append(wordlist[i])
                        flag3=1
                        break
            if flag1==0 and flag2==0 and flag3==0:
                res.append("")
        return res