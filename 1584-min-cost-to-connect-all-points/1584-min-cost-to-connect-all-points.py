class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj=defaultdict(list)
        visited=set()
        minHeap=[]
        res=0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1=points[i][0],points[i][1]
                x2,y2=points[j][0],points[j][1]
                cost=abs(x1-x2)+abs(y1-y2)
                adj[i].append([cost,j])
                adj[j].append([cost,i])
        minHeap.append([0,0])
        while len(visited)!=len(points):
            cost,cord=heapq.heappop(minHeap)
            if cord in visited:
                continue
            res+=cost
            visited.add(cord)
            for cost,node in adj[cord]:
                if node not in visited:
                    heapq.heappush(minHeap,[cost,node])
        return res
        
            