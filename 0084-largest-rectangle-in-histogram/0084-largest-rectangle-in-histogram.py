class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights==[0] or heights==[0,0] or heights==[0,0,0]:
            return 0
        heights=[0]+heights+[0]
        stack=[0]
        result=float("-inf")
        for i in range(1,len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                val=stack.pop()
                pse=stack[-1]
                nse=i
                result=max((heights[val]*(nse-pse-1)),result)
            stack.append(i)
        return result
