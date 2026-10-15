class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # we need to satisfy the children with the biggest greed factor by sorting s
        g.sort()
        s.sort()
        greed = 0
        cookie_size = 0
        max_Content = 0
        while greed < len(g) and cookie_size < len(s):
            if s[cookie_size] >= g[greed]:
                max_Content +=1
                greed +=1
                cookie_size +=1
            # if s[cookie_size] < g[greed]
            else:
                cookie_size+=1
        return max_Content


        