#We need to find out how many ways we can place N queens on an nxn board such that no queens can attack eachother
#Queens can only attack one another horizontally, or diagonally
#Given this, we know that only 1 queen can sit on each row

#What we can do is backtrack for each possible column 0..n in row i that a queen can sit on
#where valid position is one where a queen cannot be attacked vertically, horizontally, or diagonally
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        
        #Maintain Sets to maintain where each queen is on the board
        colSet = set()
        posDiag = set() #The positive diagonal for a cell is r+c for any cell (r,c)
        negDiag = set() #R-C for any cell (r,c)
        res = []
        def backtrack(r):

            if r >= n:
                retnBoard = []
                for row in board:
                    retnBoard.append("".join(row))
                res.append(retnBoard)
                return 
            
            #Search the current row for a valid position
            for c in range(n):
                #If the current column is invalid, try the next
                if (r-c) in negDiag or (r+c) in posDiag or c in colSet:
                    continue
                #Add Q to the board
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                
                board[r][c] = "Q"

                #Try the next row for a valid queen position
                backtrack(r+1)
                
                #After exploring decision path, backtrack and try the next row of the current column
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        print(res) 
        return res
                    


        
        
