class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS=len(board)
        COLUMNS=len(board[0])
        parents={i:i for i in range(ROWS*COLUMNS+1)}
        rank={i:1 for i in range(ROWS*COLUMNS+1)}
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        
        def find(parent):
            parent=parents[parent]
            while parent!=parents[parent]:
                parents[parent]=parents[parents[parent]]
                parent=parents[parent]
            return parent
        
        def union(parent1,parent2):
            p1=find(parent1)
            p2=find(parent2)
            if p1==p2:
                return
            if rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                parents[p2]=p1
            else:
                rank[p2]+=rank[p1]
                parents[p1]=p2
            return
                    
        def isConnected(p1,p2):
            return find(p1)==find(p2)
        def getPosition(r,c):
            return r*COLUMNS+c
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if board[row][col]=="O":
                    if row==0 or col==0 or row==ROWS-1 or col==COLUMNS-1:
                        union(getPosition(row,col),ROWS*COLUMNS)
                    else:
                        for d1,d2 in directions:
                            if board[row+d1][col+d2]=="O":
                                union(getPosition(row,col),getPosition(row+d1,col+d2))
        for row in range(ROWS):
            for col in range(COLUMNS):
                if board[row][col]=="O":
                    if not isConnected(getPosition(row,col),ROWS*COLUMNS):
                        board[row][col]="X"
                            
                        
                    
                    
                    
                
            
            
                    
                    
                
        
        
        
        
        
        
        
        