class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj=defaultdict(list)
        visited=set()
        frontier=[[0,0]]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1=points[i]
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
                
                
                
        res=0
        while len(visited)!=len(points):
            dist,point=heapq.heappop(frontier)
            if point in visited:
                continue
            visited.add(point)
            res+=dist
            for cost,p in adj[point]:
                if p in visited: continue
                heapq.heappush(frontier,[cost,p])
        return res
                
        
        
            