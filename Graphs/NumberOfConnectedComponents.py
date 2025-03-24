class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        #Build Adj List
        for i in range(n):
            adj[i] = []
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #Visit Connected Components
        visit = set()
        def dfs(node, visit):
            #Dont Revisit Connected Component
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == node:
                    continue
                dfs(nei, visit)
            return True
        
        count = 0
        for i in range(n):
            #Each time we visit a new connected component
            if dfs(i, visit):
                count += 1
        return count


            

