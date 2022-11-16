class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[["."]*n for i in range(n)]
        avoidCols=set()
        avoidDownwardDiag=set()
        avoidUpwardDiag=set()
        def dfs(curRow):
            if curRow>=n:
                dummyBoard=["".join(r) for r in board]
                res.append(dummyBoard[:])
                return
            for col in range(n):
                if col not in avoidCols and col-curRow not in avoidDownwardDiag and col+curRow not in avoidUpwardDiag:
                    avoidCols.add(col)
                    avoidDownwardDiag.add(col-curRow)
                    avoidUpwardDiag.add(col+curRow)
                    board[curRow][col]="Q"
                    dfs(curRow+1)
                    avoidCols.remove(col)
                    avoidDownwardDiag.remove(col-curRow)
                    avoidUpwardDiag.remove(col+curRow)
                    board[curRow][col]="."
        dfs(0)
        return res
                
            
            