class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        x = 0
        y = len(heights)-1
        while x <= y:
            delta = y-x
            area = delta * min(heights[x],heights[y])
            if area >= maxArea:
                maxArea = area
            minimum = min(heights[x],heights[y])
            if minimum == heights[x]:
                x+=1
            elif minimum == heights[y]:
                y -=1
        return maxArea