"""
understand: 
"""
class Solution:
    """
    understand: two numbers in the array add to target, find their indices
    input:  nums, target
    output: [array of indices]
    edge cases: always one answer exists

    plan:
    counts = {}
    target - nums[index] = value
    -> if we have previously seen the value we check it in the dictionary? 
    -> else add the value
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if target - nums[i] in counts:
                return [counts[target - nums[i]], i]
            else:
                counts[nums[i]] = i
