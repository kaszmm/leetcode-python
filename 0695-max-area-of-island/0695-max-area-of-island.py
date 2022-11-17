class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        visited=set()
        def calculateArea(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLUMNS or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return 1 + calculateArea(r-1,c) + calculateArea(r+1,c) +calculateArea(r,c-1) + calculateArea(r,c+1)
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col]>0 and (row,col) not in visited:
                    area=calculateArea(row,col)
                    maxArea=max(maxArea,area)
        return maxArea
                
        
        