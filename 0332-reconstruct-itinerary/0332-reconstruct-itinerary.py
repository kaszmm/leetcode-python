class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True) 
        adj=defaultdict(list)
        for fr,to in tickets:
            adj[fr].append(to)
        
        res=[]
        def dfs(node):
            while adj[node]:
                val=adj[node].pop()
                dfs(val)
            res.append(node)
        dfs("JFK")
        return res[::-1]