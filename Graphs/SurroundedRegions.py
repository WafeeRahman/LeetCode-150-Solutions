#Given a matrix board containing the letters x and o, capture all regions that are surrounded
#A region is an set of os that are connected adjacently, they are surrounded when you can
#Connect the regions to x cells and non of the cells are on the edge of the board (borders)
#That is, any given region is surrounded if it is not adjacent to a bordering cell (an O at the edges)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #We can use DFS to mark all of the safe regions by starting searches at bordering Os and marking them
        #Every O Value that isnt marked as safe is surrounded. 
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r,c,grid):
            #If we're out of bounds, or already visited, or on an X, we cant continue traversal
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "X" or grid[r][c] == "T"):
                return
            
            grid[r][c] = "T" #OTWS mark safe O as visited
            dirs = [[0,1],[0,-1],[1,0],[-1,0]] #Visit adjacent cells
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(nr,nc, grid)
            return
        
        #Start at each bordering O
        for r in range(ROWS):
            if board[r][COLS-1] == "O":
               dfs(r,COLS-1, board)
            if board[r][0] == "O":
               dfs(r,0, board)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c, board)

            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c, board)
        #Scan grid for unmarked Os to change them to surrounded
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"        

        
