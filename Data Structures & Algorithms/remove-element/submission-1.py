class Solution:
    """
    tracker = num of vals
    loop through nums:
        if num == val:
            tracker +=1
            temp = nums[len-tracker]
            nums[len-tracker] = num
            nums[i] = temp
    return tracker, nums
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        tracker = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[tracker] = nums[i]
                tracker+=1
        return tracker
        