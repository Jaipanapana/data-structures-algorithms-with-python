class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst=[]
        for val in tokens:
            if val[0]=="-" and val[1:].isnumeric():
                lst.append(int(val))
            elif val.isnumeric():
                lst.append(int(val))
            else:
                val2=lst.pop()
                val1=lst.pop()
                if val=="+":
                    lst.append(val1+val2)
                elif val=="-":
                    lst.append(val1-val2)
                elif val=="*":
                    lst.append(val1*val2)
                elif val=="/":
                    lst.append(int(val1/val2))
        return lst[0]