"""
understand: a consecutive sequence is elements in which one is exactly 
1 greater than the other, they can be presented in any order in nums
- input: nums (list of ints)
- output: int with the length of the list

plan:
- sort the list where the elements are one greater than each other
- could use the nums as elements in a dictionary and then add the one greater element to it as a key
- find the value associated in the dictionary's key and append to output?

start with a set
loop through the nums list
if num - 1 in set, skip this num
if num - 1 not in set, this is the first occurrence of a sequence need to keep track of it,
    - if num - 1 not in set, track num + 1, num + 2, etc until you reach the  end of the sequence
    - keep track of total lenght of a sequence as a max counter
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        counter = 0
        for num in nums:
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length +=1
                counter = max(counter, length)
        return counter

        
