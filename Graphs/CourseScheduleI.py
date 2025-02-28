#With a list of prerequisites and number of courses in the course set, we have preq[i] [ai, bi] where b is a preq of a
#We need to return true if we can finish all courses and prerequisites
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for a, b in prerequisites:
            adj[b].append(a)

        #Cycle: [[1,0],[0,1]] These are invalid because theyre prerequisites of eachother
        #Motivation: If we can visit all courses and prerequisites 
        #without the existence of a cycle, that tells us we can complete
        #The courses and prerequisites in a valid order
        cycle = set()
        visit = set()
        def dfs(node, cycle, visit):
            if node in cycle:
                return False
            if node in visit:
                return True
            visit.add(node)     #Visit node and add it to check if the currnode has a cycle within its neighbors     
            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei, cycle, visit):
                    return False
            cycle.remove(node) #Backtrack for cycle checking if we dont find a cycle
            return True

        for i in range(numCourses):
            #If we already visited a node, we already verified that it has no cycle
            if i not in visit:
                if not dfs(i,cycle,visit): #Cycle Check
                    return False
        return True
        
