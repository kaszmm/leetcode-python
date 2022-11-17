class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea=0
        self.area=0
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        def calculateArea(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLUMNS or grid[r][c]==0:
                return
            
            grid[r][c]=0
            self.area+=1
            self.maxArea=max(self.maxArea,self.area)
            calculateArea(r-1,c)
            calculateArea(r+1,c)
            calculateArea(r,c-1)
            calculateArea(r,c+1)
            return
        
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col]>0:
                    self.area=0
                    calculateArea(row,col)
        return self.maxArea
                
        
        