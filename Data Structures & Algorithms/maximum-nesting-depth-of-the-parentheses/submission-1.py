class Solution:
    """
    max = 0
    loop through digits in s:
        current running = 0
        if parenthesis is (:
            current running +=1
            if current running > max:
                max = current running
        if parenthesis is ):
            current_running -=1
            


    """
    def maxDepth(self, s: str) -> int:
        max = 0
        curr = 0
        for letter in s:
            if letter == "(":
                curr+=1
                if curr > max:
                    max = curr
            if letter == ")":
                curr-=1
        return max


