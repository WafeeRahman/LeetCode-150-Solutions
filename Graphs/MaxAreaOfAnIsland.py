#With an mxn binary matrix, an island is represented by adjacent groups of ones
#The area of an island is the number of cells that with value one, where each island are built
#Of adjacent ones that are surrounded by zeros
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        curArea = 0
        #Lets use DFS to visit every adjacent land for each unvisited island
        #We can use a global variable curArea to keep track of the amount of lands we find
        #For each unvisited adjacent island
        def dfs(r, c):
            nonlocal curArea
            if (min(r,c) < 0 
               or r >= ROWS or c >= COLS
               or (r,c) in visit
               or grid[r][c] == 0):
               return 0 
            visit.add((r,c)) #Lets not revisit this island, or any values adj to it
            curArea += 1 #Add one for each land we find for the current island area

            #Search Adjacent Islands
            dirs = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(nr,nc)
            return 
        
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                curArea = 0
                if grid[r][c] == 1: #If we find an unvisited island
                    dfs(r,c) #Build CurArea
                    maxArea = max(maxArea,curArea) #Take Max
        return maxArea
