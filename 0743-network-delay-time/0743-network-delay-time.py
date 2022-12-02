class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float("inf")]*(n+1)
        dist[0]=0
        queue=deque()
        queue.append([k,0])
        res=0
        adj=defaultdict(list)
        for t,r,w in times:
            adj[t].append([r,w])
    
        while queue:
            t,w=queue.popleft()
            if w<dist[t]:
                dist[t]=w
                for r,d in adj[t]:
                    queue.append([r,d+w])
        res=max(dist)
        return res if res!=float("inf") else -1
                
            
            
            
            
            
            
            
            
              
        