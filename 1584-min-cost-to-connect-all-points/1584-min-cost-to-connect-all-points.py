class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        q = [(0, 0)]
        dist = [float('inf')]*n
        mst = set()
        while q:
            # 1. pop min node which is not in mst
            w, min_idx = heapq.heappop(q)
            if min_idx in mst:
                continue # node was already added to the mst set
                
            # 2 add min node to mst
            res += w
            mst.add(min_idx)
            
            # 3. update min distance for neighbors in graph if not in mst and add to heap
            for v in range(n):
                if v not in mst:
                    d = abs(points[v][0]-points[min_idx][0]) + abs(points[v][1]-points[min_idx][1])
                    if d < dist[v]:
                        dist[v] = d
                        heapq.heappush(q, (d, v))
        return res
        
            