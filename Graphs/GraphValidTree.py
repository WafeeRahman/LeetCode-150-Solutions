class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #A valid tree is a an undirected acyclical graph that is connected
        
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(node, visit, parNode):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                #Skip Undirected Cycles
                if parNode != None and nei == parNode:
                    continue
                if not dfs(nei, visit, node):
                    return False
         
            return True

        if not dfs(0, visit, None):
            return False
        if len(visit) != n:
            return False
        return True
        

        
