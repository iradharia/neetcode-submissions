from collections import deque
class Solution(object):
    """
    understand: 
    - an island is formed with horizontal and adjecent lands
    - every single island must have up down left right boxes 
    - example two shows us that diagonals are islands (3)

    match: is this bfs or dfs?
    
    plan:
    
    island count =0
    mark the first element as visited
    loop through the grid while visited not empty

    take the element out from the beginning 
    for each neighbor the element has:
        if neighbor not visited
            add to visited
            dequeue curr 
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]== "1" and (row,col) not in visited:
                    # we hit a new island
                    island_count +=1
                    queue = deque([(row,col)])
                    visited.add((row, col))
                    while queue:
                        elem = queue.popleft()
                        currR = elem[0]
                        currC = elem[1]
                        neighbors = [(currR -1, currC), (currR +1, currC), (currR, currC +1), (currR, currC-1)]
                        for neighborR, neighborC in neighbors:
                            if not(0<= neighborR < len(grid) and 0 <= neighborC < len(grid[row])):
                                continue
                            if grid[neighborR][neighborC] != "1":
                                continue
                            if (neighborR, neighborC) in queue:
                                continue
                            if (neighborR, neighborC) in visited:
                                continue
                            queue.append((neighborR, neighborC))
                            visited.add((neighborR, neighborC))
        return island_count






        