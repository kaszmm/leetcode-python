class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        def detectCycle(visited:set,prev,node):
            if node in visited:
                return True
            visited.add(node)
            for neighbours in adj[node]:
                if neighbours!=prev and detectCycle(visited,node,neighbours):
                    return True
            return False

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            if detectCycle(set(),-1,edge[0]):
                return edge
        