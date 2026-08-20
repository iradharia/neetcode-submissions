"""
a * b - c * d with pairs (a,b) and (c,d)
"""
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxPair = []
        maxPrd= 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] * nums[j] > maxPrd:
                    maxPrd = nums[i] * nums[j]
                    maxPair.append((nums[i], nums[j]))
        
        minPair = []
        minPrd = float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] * nums[j] < minPrd:
                    minPrd = nums[i] * nums[j]
                    minPair.append((nums[i], nums[j]))
        
        return (maxPrd - minPrd)
        

