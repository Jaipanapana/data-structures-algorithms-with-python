class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()
            if len(stack)==0:
                ans[i]=0
                stack.append(i)
            else:
                ans[i]=stack[-1]-i
                stack.append(i)
        return ans