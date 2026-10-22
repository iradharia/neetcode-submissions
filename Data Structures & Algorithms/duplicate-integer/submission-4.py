"""
understand: return true if any value appears more than once, else false
input: array
output: boolean T/F
edge cases: no repeats -> false

plan:
dictionary to hold number: count
loop through list, if seen then return True else at end return false
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if num in counts:
                return True
            else:
                counts[num] = 1
        return False


        