class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited=set()
        adj=defaultdict(list)
        minHeap=[[0,k]]
        for trans,recei,delay in times:
            adj[trans].append([delay,recei])
        
        timeTaken=0
        while minHeap and len(visited)<n:
            delay,t =heapq.heappop(minHeap)
            if t in visited:
                continue;
            visited.add(t)
            timeTaken=max(timeTaken,delay)
            for d,r in adj[t]:
                if r not in visited:
                    heapq.heappush(minHeap,[delay+d,r])
        return timeTaken if len(visited)==n else -1
            
            
            
            
            
            
            
            
              
        