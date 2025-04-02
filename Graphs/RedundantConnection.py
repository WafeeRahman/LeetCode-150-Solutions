#Use Case of a Union Find:
#Count Connected Components, Detect Cycles through Checking Root Parents of Set Unions for Edged Nodes
class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self , n):
        #A node is the root if the parent is itself
        if n != self.par[n]:
            #Find the root node
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, n1,n2):
        #Compare Hierarchy of the Parents of the Nodes Before Unioning them Under the Higher Ranked Parent
        p1 = self.find(n1)
        p2 = self.find(n2)
        
        if p1 == p2:
            return False
        
        #Set The Union Parent Based On Rank
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        UnionFind = DSU(len(edges))
        for u, v in edges:
          #If we find that an edge formed has the same parents
          #That indicates a redundant connection with a cycle. 
            if not UnionFind.union(u, v):
                return [u,v]
        #OTWS return last connection
        return [u,v]
        
            
        
