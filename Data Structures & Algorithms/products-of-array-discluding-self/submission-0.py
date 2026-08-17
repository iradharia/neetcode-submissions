"""
plan:
prefix_run = 1
prefix = []
for i in nums:
    prefix[i] = prefix_run
    prefix_run = prefix_run * i
#repeat for suffix run

for i in range(len(nums))
    output.append(prefix[i] * suffix[i])

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_run = 1
        prefix = [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] = prefix_run
            prefix_run = prefix_run * nums[i]
        
        suffix_run = 1
        suffix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffix_run
            suffix_run = suffix_run * nums[i]

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        
        return output