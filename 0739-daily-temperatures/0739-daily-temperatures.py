class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                pre_val=stack.pop()
                ans[pre_val]=i-pre_val
            stack.append(i)
        return ans