from collections import defaultdict
class Solution:
    """
    understand: group anagrams together and return sublists
    input: list of strings
    output: sublists of strings
    edge cases: empty strings, one element

    plan:
    commonality is 26 letters
    if act has a, put it in the dictionary
    if act has c, put it in the dictionary
    if act has t, put it in the dictionary
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            anagrams[tuple(counts)].append(word)
        return list(anagrams.values())
        
