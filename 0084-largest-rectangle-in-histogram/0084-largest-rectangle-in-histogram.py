class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[-1]+heights+[-1]
        result=float("-inf")
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                curr_val=stack.pop()
                result=max(result,((i-stack[-1]-1)*heights[curr_val]))
            stack.append(i)
        return result


        