class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        numberDict=defaultdict(list)
        numberDict['2']=['a','b','c']
        numberDict['3']=['d','e','f']
        numberDict['4']=['g','h','i']
        numberDict['5']=['j','k','l']
        numberDict['6']=['m','n','o']
        numberDict['7']=['p','q','r','s']
        numberDict['8']=['t','u','v']
        numberDict['9']=['w','x','y','z']
        
        res=[]
        def dfs(curStr,idx):
            if idx>=len(digits):
                res.append(curStr)
                return
            aplhas=numberDict[digits[idx]]
            for i in range(0,len(aplhas)):
                curStr+=aplhas[i]
                dfs(curStr,idx+1)
                curStr=curStr[:-1]
                
            return
        
        dfs("",0)
        return res