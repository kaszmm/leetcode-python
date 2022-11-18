class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        ROWS=len(grid)
        COLUMNS=len(grid[0])
    
        parents=defaultdict()
        rank=defaultdict()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col]>0:
                    parents[(row,col)]=(row,col)
                    rank[(row,col)]=1
    
        def find(r,c):
            parent=parents[(r,c)]
            while parent!=parents[parent]:
                parents[parent]=parents[parents[parent]]
                parent=parents[parent]
            return parent
        
        def union(r1,c1,r2,c2):
            parent1=find(r1,c1)
            parent2=find(r2,c2)
            if parent1==parent2:
                return rank[parent1]
            if rank[parent1]>rank[parent2]:
                rank[parent1]+=rank[parent2]
                parents[parent2]=parent1
                return rank[parent1]
            else:
                rank[parent2]+=rank[parent1]
                parents[parent1]=parent2
                return rank[parent2]
    
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col]>0:
                    area=0
                    maxArea=max(maxArea,1)
                    for r,c in directions:
                        if row+r>=0 and row+r<ROWS and col+c>=0 and col+c<COLUMNS and grid[row+r][col+c]>0:
                            area=union(row,col,row+r,col+c)
                            maxArea=max(maxArea,area if area>0 else 1)
        return maxArea
                
        
        