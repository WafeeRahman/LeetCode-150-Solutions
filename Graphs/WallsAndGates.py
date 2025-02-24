#Given an mxn 2d grid with possible values -1 (intraversable), 0 (treasure chest), INF - land
#Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest, the its value
#Should be INF

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #In other words, we need to find the shortest path to a treasure chest from land
        #But we have multiple treasure chests, so if we had the case of a farther and nearer treasure chest
        #We'd have to account for that when starting from land. 
        #Therefore, we can compute the the shortest paths starting from each treasure chest, to its adjacent pieces of land
        q = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        INF = 2147483647
        
        #Multi Sourced BFS, start with each source and find the shortest path to dependencies
        #Treasure Chests ->
        length = 1 #Starting at a treasure chest, any given land is atleast 1 distance away
        while q:
            #The main difference between bfs and multi-sourced, we go level per level based on the source we're at
            #For each source compute adjacent cells we can traverse to, and continue traversal at each level of length
            for source in range(len(q)):
                r, c = q.popleft()
                dirs = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if not (min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1 or (nr,nc) in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        grid[nr][nc] = length
            length += 1 #
        

 

