class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        import math
        x=abs(z-x)
        y=abs(z-y)
        if x>y:
            return 2
        elif y>x:
            return 1
        else:
            return 0

        