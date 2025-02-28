#With a total of numCourses we can take labled 0 - numcourses-1. we have an array of prerequisites ai bi, where bi is a preq of ai
#We need to  return the ordering to finish all courses in any valid order, where prerequisites come before the courses that depend on them

#CASES:
#[[1,0]]
#[0, 1], as zero has no preqs it should come before 1, as one has the preq zero

#[[1,0],[2,0],[3,1],[3,2]] --> [0,2,1,3] #Ordering by prerequisite

#Again, like course schedule 1, we need to ensure there are no cycles
#We can also use DFS post order to create a topological sort of the prerequisite graph, where for each edge u, v the 
#Verticies are ordered such that u comes before v as it has no edges
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for ai, bi in prerequisites:
            adj[ai].append(bi)
        

        cycle = set()
        visit = set()
        order = []
        def dfs(node, visit, cycle):
            #If the node repeats more than once in the current path there is a cycle
            if node in cycle:
                return False
            #If we've already processed this node dont do repeated work
            if node in visit:
                return True
            
            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei, visit, cycle):
                    return False
            
            cycle.remove(node) #If the cycle of each neighbor is valid, backtrack
            visit.add(node) #Add nodes to path in post order, visit every preq neighbor and add to path before current
            order.append(node)
            
            return True
        #For disconnected nodes, we need to iterate through each possible course and only visit unvisited nodes
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i,visit,cycle):
                    return []
        return order


        

      
