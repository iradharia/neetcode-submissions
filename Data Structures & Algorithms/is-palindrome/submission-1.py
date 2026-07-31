"""
have a 2-pointer approach where you check each letter, 
if ever the letters dont match return false

left = s[0]
right = s[-1]
while left < right:
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1

        return True







        