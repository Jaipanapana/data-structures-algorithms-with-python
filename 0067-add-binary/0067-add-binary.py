class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary_number(b):
            power=result=0
            for num in b[::-1]:
                result+=(2**power*int(num))
                power+=1
            return result
        def number_binary(num):
            res=""
            val=0
            while num>0 :
                val=(num%2)
                res+=str(val)
                num=num//2
            return(res[::-1])
        if a=="0" and b=="0":
            return "0"
        a=binary_number(a)
        b=binary_number(b)
        result=number_binary(a+b)
        return str(result)
        
                