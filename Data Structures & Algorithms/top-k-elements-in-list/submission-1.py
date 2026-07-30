from collections import defaultdict
"""
use a dictionary as buckets for {key = number, value = sum}
while adding the counts of numbers to dictionary, 
check to see if the value is ever equal to the target and append to op
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        output = []
        for num in nums:
            counts[num]+=1
        
        sorted_nums = sorted(counts, key = lambda num: counts[num], reverse = True)
        return sorted_nums[:k]