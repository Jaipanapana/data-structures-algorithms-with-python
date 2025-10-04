class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_water=0
        while i<j:
            x_axis=j-i
            min_val=min(height[i],height[j])
            max_water=max(min_val*x_axis,max_water)
            if min_val==height[i]:
                i+=1
            else:
                j-=1
        return max_water


        
        