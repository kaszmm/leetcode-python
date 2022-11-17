class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[["."]*n for i in range(n)]
    
        def IsQueenPresent(row,col):
            tempRow=row
            tempCol=col
            #check if Queen present in same column
            while tempRow>=0:
                if board[tempRow][tempCol]=="Q":
                    return True
                tempRow-=1
            
            tempRow=row
            tempCol=col
            #check if Queen present in leftside upward diagonal
            while tempRow>=0 and tempCol>=0:
                if board[tempRow][tempCol]=="Q":
                    return True
                tempRow-=1
                tempCol-=1
            
            tempRow=row
            tempCol=col
            #check if Queen present in rightside upward diagonal
            while tempRow>=0 and tempCol<n:
                if board[tempRow][tempCol]=="Q":
                    return True
                tempRow-=1
                tempCol+=1
            return False
    
        def dfs(curRow):
            if curRow==n:
                dummyBoard=["".join(row) for row in board]
                res.append(dummyBoard[:])
                return
            for col in range(n):
                if not IsQueenPresent(curRow,col):
                    board[curRow][col]="Q"
                    dfs(curRow+1)
                    board[curRow][col]="."
                    
        dfs(0)
        return res
            
            