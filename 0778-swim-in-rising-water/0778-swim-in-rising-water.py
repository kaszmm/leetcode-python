class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited=set()
        n=len(grid)
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def inBound(r,c):
            if r<0 or r>=n or c<0 or c>=n:
                return False
            return True
        def getPosition(r,c):
            return r*n+c
        parents=[0]*(n*n)
        positions=[]
        for i in range(n):
            for j in range(n):
                pos=getPosition(i,j)
                parents[pos]=pos
                positions.append([grid[i][j],i,j])
            
        def find(p):
            if p==parents[p]:
                return p
            return find(parents[p])
        
        def union(x1,x2):
            p1=find(x1)
            p2=find(x2)
            
            if p1==p2:
                return False
            parents[p2]=p1
            return True
        positions.sort(key=lambda x:x[0])
        for  cost,r,c in positions:
            visited.add((r,c))
            for dr,dc in directions:
                if inBound(r+dr,c+dc) and (r+dr,c+dc) in visited:
                    union(getPosition(r,c),getPosition(r+dr,c+dc))
            if find(getPosition(0,0))==find(getPosition(n-1,n-1)):
                return cost
                        
        return -1
            
            