class Solution:
    def maxArea(self, height: List[int]) -> int:
        output=0
        x_axis=len(height)-1
        height_left=0
        height_right=len(height)-1
        while(height_left<height_right):
            less_height=min(height[height_left],height[height_right])
            if less_height==height[height_left] :
                height_left+=1
            else:
                height_right-=1
            res=x_axis*less_height
            if output<res:
                output=res
            x_axis-=1
        return output
        