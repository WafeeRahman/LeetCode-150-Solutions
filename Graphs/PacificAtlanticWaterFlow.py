#Given an mxn grid where the leftmost and topmost columns border the pacific ocean, and the rightmost and bottommost columns
#Border The Atlantic, return a list of cells where water can flow between the pacific and atlantic
#Each cell at r,c represents a height, where water can flow from any cell adjacent if and only if the water at the adjacent cell
#Is less than or equal to the height at the current cell
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #A naive solution could be checking each cell in the graph that can reach a cell in the bordering columns and rows
        #But that would mean we would have a dfs/bfs call for each cell in the row
        #Well, we could limit the amount of dfs calls by starting a dfs for each border regions,
        #Where visited cells represent the deepest the water can flow from each region, the intersection of these cells
        #Would represent the amount of cells that can flow between each border
        ROWS = len(heights)
        COLS = len(heights[0])
        def dfs(r,c,visit,prevCell):
            #Reverse traversal property, since we're starting at endpoints for each path
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or prevCell > heights[r][c] or (r,c) in visit):
                return
            visit.add((r,c))
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(nr,nc,visit,heights[r][c])
            return
        
        pac = set()
        atl = set()
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res
            

        
