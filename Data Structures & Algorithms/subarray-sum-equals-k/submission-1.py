class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {0:1}
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - k in seen:
                count = count + seen[running_sum-k]
            
            seen[running_sum] = seen.get(running_sum, 0) +1
        return count
            

