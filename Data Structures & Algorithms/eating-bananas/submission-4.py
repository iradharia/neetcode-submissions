import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # basic case
        if sum(piles) / max(piles) == h:
            return max(piles)
        
        lo = 1
        hi = max(piles)
        minRate = float('inf')
        while lo <= hi:
            mid = (lo + hi)//2
            total = 0
            for i in range(len(piles)):
                hours = math.ceil(piles[i]/mid)
                total+=hours
            if total <= h:
                # lo stays same
                hi = mid-1
                # iterate binary search again
                if mid < minRate:
                    minRate = mid
            if total > h:
                lo = mid+1
                # high stays the same
                # iterate binary search again
        return minRate


        

        