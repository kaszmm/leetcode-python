class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort() 
        adj=defaultdict(list)
        res=["JFK"]
        for fr,to in tickets:
            adj[fr].append(to)
        
        def dfs(node):
            if len(res)==len(tickets)+1:
                return True
            temp=list(adj[node])
            for idx,ticket in enumerate(temp):
                res.append(ticket)
                adj[node].pop(idx)
                if dfs(ticket):
                    return True
                res.pop()
                adj[node].insert(idx,ticket)
            return False
        
        dfs("JFK")
        return res