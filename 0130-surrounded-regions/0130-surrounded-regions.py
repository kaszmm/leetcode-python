class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS=len(board)
        COLUMNS=len(board[0])
        rowBounds=[0,ROWS-1]
        colBounds=[0,COLUMNS-1]
        queue=deque()

        def inBound(r,c):
            if r>=0 and r<ROWS and c>=0 and c<COLUMNS:
                return True
            else:
                return False
        def bfs():
            while queue:
                r,c=queue.popleft()
                if inBound(r,c) and board[r][c]=="O":
                    board[r][c]="-"
                    queue.append((r+1,c))
                    queue.append((r-1,c))
                    queue.append((r,c+1))
                    queue.append((r,c-1))
            return
        
        for col in range(COLUMNS):
            queue.append((0,col))
            queue.append((ROWS-1,col))
                    
        for row in range(ROWS):
            queue.append((row,0))
            queue.append((row,COLUMNS-1))
        bfs()    
        for row in range(ROWS):
            for col in range(COLUMNS):
                if board[row][col]=="O":
                    board[row][col]="X"
                elif board[row][col]=="-":
                    board[row][col]="O"
                    
                    
                
        
        
        
        
        
        
        
        