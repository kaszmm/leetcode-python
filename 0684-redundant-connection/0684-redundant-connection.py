class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents=[i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)
        
    
        def find(p):
            p=parents[p]
            while p!=parents[p]:
                parents[p]=parents[parents[p]]
                p=parents[p]
            return p
        
        def union(parent1,parent2):
            p1=find(parent1)
            p2=find(parent2)
            if p1==p2:
                return False
            if rank[p2]>rank[p1]:
                parents[p1]=p2
                rank[p2]+=rank[p1]
            else:
                parents[p2]=p1
                rank[p1]+=rank[p2]
            return True
        
        for edge in edges:
            if not union(edge[0],edge[1]):
                return edge