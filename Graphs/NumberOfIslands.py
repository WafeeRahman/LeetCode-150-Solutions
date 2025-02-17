#Given an mxn 2d grid that represents a map of 1s and 0s, where 12s are land and zeros are water
#An island is surrounded by water and is formed by connected adjacent lands horizontally or vertically

#With this grid, how many connected components are there?    
#We can use matrix DFS starting at every land, marking each land as visited, ensuring we dont visit the same land again
#With each dfs, we clear the board, once we visit every connected component, we know how many islandsa there are
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            #If we visited the current cell or if its not land, or if we're out of bounds, do not continue search
            if (min(r,c) < 0 
                or r >= ROWS or c >= COLS
                or grid[r][c] == "."
                or grid[r][c] == "0"):
                return
            grid[r][c] = "." #Visit so we never visit again
            #Look for adjacent cells of land
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in dirs:
                nr,nc = r+dr, c+dc
                dfs(nr,nc)
            return
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res+=1 #Count the amount of times we find an unvisited connect component
        return res
        
