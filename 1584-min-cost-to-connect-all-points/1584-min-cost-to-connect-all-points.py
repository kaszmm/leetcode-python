class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents=[i for i in range(len(points)) ]
        minHeap=[]
        res=0
        visited=set()
        def find(p):
            if p==parents[p]:
                return p
            return find(parents[p])
        
        def union(node1,node2):
            p1=find(node1)
            p2=find(node2)
            if p1==p2:
                return False
            parents[p1]=p2
            return True
    
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1=points[i][0],points[i][1]
                x2,y2=points[j][0],points[j][1]
                cost=abs(x1-x2)+abs(y1-y2)
                minHeap.append([cost,(i,j)])
        heapq.heapify(minHeap)
        
        nodeCount=0
        while nodeCount<len(points)-1:
            cost,cords=heapq.heappop(minHeap)
            if union(cords[0],cords[1]):
                visited.add((cords[0],cords[1]))
                nodeCount+=1
                res+=cost
        return res
        
            