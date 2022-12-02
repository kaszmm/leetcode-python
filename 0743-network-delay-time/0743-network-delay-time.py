class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, s: int) -> int:
        dist=[[float("inf")]*(n) for i in range(n)]
        res=0
        for i in range(n):
            dist[i][i]=0
        
        for t,r,w in times:
            dist[t-1][r-1]=w
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if j==i or k==i:
                        continue
                    dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k])
        
        for j in range(n):
            if dist[s-1][j]==float("inf"):
                return -1
            res=max(res,dist[s-1][j])
        return res if res!=float("inf") else -1
                
            
            
            
            
            
            
            
            
              
        