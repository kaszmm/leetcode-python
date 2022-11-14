class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        partitions=[]
        def isPalindrome(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
                 
                
        def dfs(idx):
            if idx>=len(s):
                res.append(partitions[:])
                return
            for i in range(idx,len(s)):
                if isPalindrome(s,idx,i):
                    partitions.append(s[idx:i+1])
                    dfs(i+1)
                    partitions.pop()
            return
        
        dfs(0)
        return res
        
                    
            