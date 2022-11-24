class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        def detectCycle(node):
            queue=deque()
            visited=set()
            prevVisited=set()
            queue.append(node)
            visited.add(node)
            while queue:
                for i in range(len(queue)):
                    curNode=queue.popleft()
                    prevVisited.add(curNode)
                    for neighbors in adj[curNode]:
                        if neighbors not in prevVisited:
                            if neighbors in visited:
                                return True
                            queue.append(neighbors)
                            visited.add(neighbors)
            return False

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            if detectCycle(edge[0]):
                return edge
        