#Given a 2-D Matrix Grid, where each of the cells can have hte 3 poossible values
#0 - empty, 1-fresh fruit, 2-rotten fruti

#Every minute, a fresh fruit is horizontally or vertically adjacent to a rotten fruit then the fresh fruit also becomes rotten
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #We can use a multi-sourced BFS starting at each rotten fruit, iterating each level of distance until all fruit are rotten
        #Increment time as each minute elapsed when we traverse in every adjacent direction from a rotten fruit
        #Add the sources to start our search
        
        ROWS = len(grid)
        COLS = len(grid[0])

        #When we have as much rottenfruit as total fruit, we know we can stop.
        rottenFruit, total = 0, 0 
        q = deque([])
        visit = set()
        #Add sources to start search, and increment totals for stopping condition
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rottenFruit +=1
                    total += 1
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    total +=1
        #If there are no fruit, we need no time cycles
        if total == 0:
            return 0
        #If there are no rotten fruit to start with, then we cant rot any fruit
        if rottenFruit == 0:
            return -1
        t = 0 #Start at zero time elapsed, as each time cycle elapses, the level of distance that reaches
        while q:
            #For each path starting ath the sources of BFS (initial q)
            if rottenFruit == total:
                return t
            for sourcePath in range(len(q)):
                r, c = q.popleft()  
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or (nr,nc) in visit):
                        continue
                    #If we encounter a fresh fruit thats adjacent, count it as rotten and continue the path
                    q.append((nr,nc))
                    visit.add((nr,nc))
                    rottenFruit += 1
            t+=1
        return -1

                    
