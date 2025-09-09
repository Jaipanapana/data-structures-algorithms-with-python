class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        left_heights=[0]*len(height)
        for i in range(len(height)):
            left_heights[i]=left
            left=max(left,height[i])
        right=0
        right_heights=[0]*len(height)
        for i in range(len(height)-1,-1,-1):
            right_heights[i]=right
            right=max(right,height[i])
        output=0
        for i in range(len(height)):
            val=min(left_heights[i],right_heights[i])
            val=val-height[i]
            if val>0:
                output+=val
        return output
