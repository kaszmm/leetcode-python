class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea=0
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        def calculateArea(r,c,area):
            if r<0 or r>=ROWS or c<0 or c>=COLUMNS or grid[r][c]==0:
                return 0
            grid[r][c]=0
            area+=1
            area=max(calculateArea(r-1,c,area),area)  #down
            area=max(calculateArea(r+1,c,area),area)  #up
            area=max(calculateArea(r,c-1,area),area)  #left
            area=max(calculateArea(r,c+1,area),area)  #right
            return area
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col]>0:
                    area=calculateArea(row,col,0)
                    maxArea=max(maxArea,area)
        return maxArea
                
        
        