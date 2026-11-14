class Solution:
    """
    i think it would be helpful to have something to keep track of
    how many times a letter occurs 

    we need to find a formula that would ideally tell us, given
    k, the length of the string, and how many of each unique characters 
    there are + their frequencies


    will replacing a character by k give us the max length of one distinct character?

    what happens if we replace x by k characters?
    what happens if we replace y by k characters?

    i think in a brute force method, you would iterate through the input s 
    and then when you reach a new character, you would decrement the k and change
    the letter to your current letter to keep track of the curr max??

    trying to think of something more effecient.
    - still need a way to keep track of the start and end of a new window of same chars
    - errr might just try some sliding window approach and see what happens 
        cuz only solution i can think of rn


    MORE THOUGHTS:
    - when using a hash map i would need to look up the
    frequencies of each character in the string i guess?
    
    - key (char): val (frequency)

    - if we check our total # of characters and see the most
    frequent, we know that there are 
    total # - most frequent = x number of characters to replace

    - but i don't get how it would work if i know that there are 
    x characters that need replacing but i dont really know
    where they are or their relative order cuz ideally wouldn't
    we need to have them be consecutive?

    - we can use formula as replacements needed = window length - most frequent character
    """


    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        max_len = 0
        left = 0 
        for right in range(len(s)):
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1
            replacements = right - left + 1 - (max(frequencies.values()))
            while replacements > k:
                frequencies[s[left]] -=1
                left +=1
                replacements = right - left + 1 -(max(frequencies.values()))

            if replacements <= k:
                if right - left + 1 > max_len:
                    max_len = right - left +1
        return max_len

# time O(n)
# space O(1) we will have at most 26 unique letters 






        