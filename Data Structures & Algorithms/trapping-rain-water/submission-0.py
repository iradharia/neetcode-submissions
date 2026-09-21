class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height)-1
        maxLeft = height[left]
        maxRight = height[right]
        trapped_water = 0

        while left < right:
            if maxLeft < maxRight:
                left +=1
                maxLeft = max(maxLeft, height[left])
                collected = maxLeft - height[left]
                trapped_water += collected
            else:
                right -=1
                maxRight = max(maxRight, height[right])
                collected = maxRight - height[right]
                trapped_water += collected
            
        return trapped_water
            