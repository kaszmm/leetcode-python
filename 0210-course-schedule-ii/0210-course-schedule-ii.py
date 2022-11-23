class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i :set() for i in range(numCourses)}
        for course,preq in prerequisites:
            adj[course].add(preq)
        
        doneCourses=set()
        res=[]
        def dfs(visited,course):
            if len(adj[course])==0 or course in doneCourses:
                return True
            visited.add(course)
            for preq in adj[course].copy():
                if preq in doneCourses:
                    adj[course].remove(preq)
                else:
                    if preq not in visited and dfs(visited,preq):
                        doneCourses.add(preq)
                        res.append(preq)
                        adj[course].remove(preq)
                    else:
                        return False
            return len(adj[course])==0
        for i in range(numCourses):
            visited=set()
            if i not in doneCourses and dfs(visited,i):
                doneCourses.add(i)
                res.append(i)
        return res if len(doneCourses)==numCourses else []
