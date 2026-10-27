class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        total_max = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = total_max
            if temp > total_max:
                total_max = temp
        return arr
    