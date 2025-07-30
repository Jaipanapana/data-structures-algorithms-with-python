class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        sufix = [0] * len(height)
        prefix[0] = height[0]
        i = 1
        while i < len(height):
            prefix[i] = max(prefix[i - 1], height[i])
            i += 1
        sufix[len(height) - 1] = height[len(height) - 1]
        i = len(height) - 2
        while i >= 0:
            sufix[i] = max(sufix[i + 1], height[i])
            i -= 1
        i = 0
        total_water = 0
        while i < len(height):
            left_max = prefix[i]
            right_max = sufix[i]
            water_level = min(left_max, right_max)
            if height[i] < water_level:
                total_water += water_level - height[i]
            i += 1
        return total_water
