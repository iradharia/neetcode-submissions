import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sortLargest = heapq.nlargest(k, nums)
        return sortLargest[-1]