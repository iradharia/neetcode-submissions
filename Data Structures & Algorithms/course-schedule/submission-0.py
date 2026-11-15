from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for dest,source in prerequisites:
            adj[source].append(dest)
        
        visited_set = set()
        visited_safe = set()
        def dfs(course):
            if course in visited_set:
                return False
            if course in visited_safe:
                return True
            visited_set.add(course)
            visited_safe.add(course)
        
            for elem in adj[course]:
                if not dfs(elem):
                    return False
            visited_set.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True