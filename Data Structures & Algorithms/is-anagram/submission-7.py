"""
understand: are 2 strings anagrams of each other?
input: 2 strings
output: t/f boolean
edgecases: no annagrams -> f

what is an annagram? order doesn't matter, characters must be same
plan:
one dictionary of counts
loop through s and t, incrementing the counts for s
and decrementing the counts for t
check if any value is < 0 and immediately return false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i],0) +1
            counts[t[i]] = counts.get(t[i], 0) -1
        
        for val in counts.values():
            if val != 0:
                return False
        return True
            

