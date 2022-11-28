class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True) 
        adj=defaultdict(list)
        for fr,to in tickets:
            adj[fr].append(to)
        
        res=[]
        stack=["JFK"]
        while stack:
            if len(adj[stack[-1]])>0:
                val= adj[stack[-1]][-1]
                adj[stack[-1]].pop()
                stack.append(val)
            else:
                res.append(stack[-1])
                stack.pop()
        return res[::-1]