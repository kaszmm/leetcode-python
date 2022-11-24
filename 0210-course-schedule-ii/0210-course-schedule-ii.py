class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i :set() for i in range(numCourses)}
        for course,preq in prerequisites:
            adj[course].add(preq)
        doneCourses=set()
        visited=set()
        res=[]
        def dfs(course):
            if course in doneCourses:
                return True
            if course in visited:
                return False
            visited.add(course)
            for preq in adj[course]:
                if not dfs(preq):
                    return False
            res.append(course)
            doneCourses.add(course)
            visited.remove(course)
            return True
            
        for i in range(numCourses):
            visited=set()   #this used for detetcing cycles in graph
            if not dfs(i):
                return []
        return res
