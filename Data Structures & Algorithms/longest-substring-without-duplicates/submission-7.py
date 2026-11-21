class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        chars = set()
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left +=1
            curr_window = right - left +1 
            longest = max(longest, curr_window)
            chars.add(s[right])

        return longest       

