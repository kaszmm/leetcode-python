class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited=set()
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def inBound(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLUMNS:
                return False
            return True
        res=float("inf")
        minHeap=[[grid[0][0],0,0]]
        while minHeap:
            cost,r,c =heapq.heappop(minHeap)
            if r==ROWS-1 and c==COLUMNS-1:
                res=min(res,cost)
                break
            if (r,c) in visited:
                continue
            visited.add((r,c))
    
            for rd,cd in directions:
                r1=r+rd
                c1=c+cd
                if inBound(r1,c1) and (r1,c1) not in visited:
                    heapq.heappush(minHeap,[max(cost,grid[r1][c1]),r1,c1])
        return res
            
            