from collections import deque
class Solution(object):
    """
    we want to do DFS to find the connected components
    of a graph

    i can keep track of what i've seen already through marker
    that mutates the individual values to -1 so i know i
    visited it already

    for dfs in general you would use a stack to be able to
    process the elements in order pop the element off the
    stack and when you hit a 0 you can mark it as -1 and 
    move on

    general pseudo code
    
    islands = 0
    loop through the rows
    if we see a 1, we know we have found a new island:
        lets add it to the stack
        increase our island count
        while the stack exists:
            pop element off the stack
            loop through all possible combinations
            of U, D L R for the current element in grid:
                -if any of them are 1's we pursue that path
                and add it to the stack
                -ensure we mark elements as "SEEN" when we
                push it onto stack
    return islands count
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                stack = []
                if grid[i][j] == '1':
                    islands +=1
                    stack.append((i,j))
                    while stack:
                        elemR, elemC = stack.pop()
                        combinations = [(elemR-1, elemC), (elemR+1,elemC), (elemR, elemC-1), (elemR, elemC+1)]
                        for combo in combinations:
                            newI, newJ = combo[0], combo[1]
                            if 0 <= newI < len(grid) and 0<=newJ<len(grid[0]):
                                if grid[newI][newJ] == '1':
                                    stack.append((newI, newJ))
                                    grid[newI][newJ] = '-1' # now the element is seen
        return islands

    