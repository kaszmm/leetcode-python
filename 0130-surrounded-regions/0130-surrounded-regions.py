class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS=len(board)
        COLUMNS=len(board[0])
        
        def getDeadCircles(row,col):
            if row<0 or row>=ROWS or col<0 or col>=COLUMNS or board[row][col]!="O":
                return
            board[row][col]="-"
            getDeadCircles(row-1,col)
            getDeadCircles(row+1,col)
            getDeadCircles(row,col-1)
            getDeadCircles(row,col+1)
            return
        
        for col in range(COLUMNS):
            if  board[0][col]=="O":
                getDeadCircles(0,col)
            if  board[ROWS-1][col]=="O":
                getDeadCircles(ROWS-1,col)
        
        for row in range(ROWS):
            if board[row][0]=="O":
                getDeadCircles(row,0)
            if board[row][COLUMNS-1]=="O":
                getDeadCircles(row,COLUMNS-1)
                
        
        for row in range(1,ROWS-1):
            for col in range(1,COLUMNS-1):
                if board[row][col]=="O":
                    board[row][col]="X"
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if board[row][col]=="-":
                    board[row][col]="O"
        
        
        
        
        
        
        
        