#Given an mxn grid of chracters board, and a target string word, return true if the word is a valid path in the grid
#That is, there exists a path of cells in board where each character is adjacent to one another to spell out word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        #Matrix DFS, for cells where the starting character belongs in word, DFS until we reach the valid path
        #OTWS backtrack and try another valid direction

        def dfs(r, c, i, visit):
            if i == len(word):
                return True
            
            #If this isnt a valid visit that will or if the current cell isnt the letter we're looking for
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] != word[i]:
                return False
            
            visit.add((r,c))
            nei = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in nei:
                nr, nc = r+dr,c+dc

                #Check adjacent nodes to see if we can reach the true case where we complete the words
                if dfs(nr,nc,i+1,visit):
                    return True
            #If we cant, backtrack and unvisit current node
            visit.remove((r,c))
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i,j,0,set()):
                        return True
        return False
            

        
