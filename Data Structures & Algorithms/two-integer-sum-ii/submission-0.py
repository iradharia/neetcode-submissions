class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers)-1
        output = []
        while lo < hi:
            if numbers[lo]+ numbers[hi] == target:
                output.append(lo+1)
                output.append(hi+1)
                return output
            elif numbers[lo]+ numbers[hi] > target:
                hi -=1
            else:
                lo +=1

        