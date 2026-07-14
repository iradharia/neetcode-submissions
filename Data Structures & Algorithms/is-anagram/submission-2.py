"""
understand: are 2 strings anagrams of each other?
input: 2 strings
output: t/f boolean
edgecases: no annagrams -> f

what is an annagram? order doesn't matter, characters must be same
plan:
have 2 dicts for each string
loop through and add all characters from strings to set
check sets
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter]+=1
            else:
                s_dict[letter]=1
        
        t_dict = {}
        for letter in t:
            if letter in t_dict:
                t_dict[letter]+=1
            else:
                t_dict[letter]=1
        return True if s_dict == t_dict else False
