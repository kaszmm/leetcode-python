class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        minuteElasped=0
        freshOranges=0
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def inBound(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLUMNS:
                return False
            return True
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col]==2:
                    queue.append((row,col))
                elif grid[row][col]==1:
                    freshOranges+=1
        
        
        while queue and freshOranges>0:
            rottenOranges=len(queue)
            for i in range(rottenOranges):
                r,c=queue.popleft()
                for d1,d2 in directions:
                    row=r+d1
                    col=c+d2
                    if inBound(row,col) and grid[row][col]==1:
                        grid[row][col]=2
                        queue.append((row,col))
                        freshOranges-=1
            minuteElasped+=1
    
        return minuteElasped if freshOranges==0 else -1