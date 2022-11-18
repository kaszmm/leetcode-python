class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        maxArea=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        def bfs(islandQueue:deque):
            area=0
            while islandQueue:
                r,c=islandQueue.popleft()
                if (r,c) in visited:
                    continue
                area+=1
                visited.add((r,c))
                for d1,d2 in directions:
                    row=r+d1
                    col=c+d2
                    if row<0 or row>=ROWS or col<0 or col>=COLUMNS or grid[row][col]==0 or (row,col) in visited:
                        continue
                    islandQueue.append((row,col))
            return area
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col]>0 and (row,col) not in visited:
                    islandQueue=deque()
                    islandQueue.append((row,col))
                    area=bfs(islandQueue)
                    maxArea=max(maxArea,area)
        
        return maxArea
                
        
        