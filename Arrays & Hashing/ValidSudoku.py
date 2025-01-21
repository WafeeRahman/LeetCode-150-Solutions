class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Each column, row, and nxn board should be a set of unique values
        colSet = defaultdict(set)
        rowSet = defaultdict(set)
        
        #For boxes, we know there are nine possible boxes
        #We can sort them by dividing each row number and column number by n
        #Add setting their tuple pairs as keys to each box
        #I.E, rows 0, 1, 2 paired with columns 0,1,2 will contain box zero
        #(0-2//3, 0-2//3) = (0,0), we know that r and c will range from 0-8, giving us
        #9 possible boxes
        
        boxSet = defaultdict(set)

        #Iterate through the board
        for r in range(len(board)):
            for c in range(len(board[r])):
                #If value is empty skip to next iteration
                if board[r][c] == ".":
                    continue
                #If we find a duplicate in any respective set, return false
                if board[r][c] in colSet[c] or board[r][c] in rowSet[r] or board[r][c] in boxSet[(r//3, c//3)]:
                    return False
                #OTWS add to boxes
                colSet[c].add(board[r][c])
                rowSet[r].add(board[r][c])
                boxSet[(r//3, c//3)].add(board[r][c])
        return True
        #If we never reach a false case, the board is valid
                
