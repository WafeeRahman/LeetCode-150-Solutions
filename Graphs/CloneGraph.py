#Given a reference of a node in a connected undirected graph, deep copy the graph into new node structures

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        oldToCopy = {node: Node(node.val)}
        #We can use BFS to visit all nodes for each neighbor of the connected graph
        visit = set([node]) 
        #Since the graph is connected, we know we may revisit nodes, we want to only visit each node once
        #And populate the copied associated values
        q = deque([node])

        while q:
            oldNode = q.popleft()
            for nei in oldNode.neighbors:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
                    oldToCopy[nei] = Node(nei.val)
                oldToCopy[oldNode].neighbors.append(oldToCopy[nei])
        print(oldToCopy[node].neighbors)
        return oldToCopy[node]

            
