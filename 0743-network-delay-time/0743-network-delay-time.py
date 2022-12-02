class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances=[float("INF")]*(n+1)
        result=0
        distances[0],distances[k]=0,0
        
        for i in range(1,n):
            for trans,receive,weight in times:
                distances[receive]=min(distances[receive],distances[trans]+weight)
        
        for cost in distances:
            if cost==float("inf"):
                return -1
            result=max(result,cost)
        return result
                
            
            
            
            
            
            
            
            
              
        