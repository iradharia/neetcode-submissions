class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                if nums[lo]+nums[hi] < -1*nums[i]:
                    lo +=1
                elif nums[lo]+nums[hi] > -1*nums[i]:
                    hi-=1
                else:
                    output.append([nums[lo], nums[i], nums[hi]])
                    lo+=1
                    hi -=1
                    while lo < hi and nums[lo]== nums[lo-1]:
                        lo+=1

        return output