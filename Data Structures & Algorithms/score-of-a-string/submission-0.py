class Solution:
    def scoreOfString(self, s: str) -> int:
        total_sum = 0
        for i in range(len(s)-1):
            i_ord = ord(s[i])
            j_ord = ord(s[i+1])
            difference = abs(i_ord-j_ord)
            total_sum += difference
        return total_sum
        