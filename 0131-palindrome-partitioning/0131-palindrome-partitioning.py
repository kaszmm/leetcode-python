class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        res=[]
        for i in range(len(s)):
            for j in range(0,i+1):
                if s[i]==s[j] and (i-j<3 or dp[i-1][j+1]):
                    dp[i][j]=True
        
        
        def dfs(curIdx,palindromes):
            if curIdx>=len(s):
                res.append(palindromes[:])
                return
            for i in range(curIdx,len(s)):
                if dp[i][curIdx]:
                    palindromes.append(s[curIdx:i+1])
                    dfs(i+1,palindromes)
                    palindromes.pop()
            return
        dfs(0,[])
        return res
                    
            