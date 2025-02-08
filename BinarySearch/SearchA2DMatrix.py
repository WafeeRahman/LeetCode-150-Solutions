class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #In an mxn square sorted matrix, find a specific value in O(logm*n) time
        #Without naive search, we can use binary search to find the value given that
        #All arrays are sorted, and we can start by finding the array that holds the value by testing
        #It against the final column value in each row (max of each row)
        ROWS, COLS = len(matrix), len(matrix[0]) 
        l = 0
        r = ROWS-1

        #Binary Search the Correct Row where target should be located in

        while l <= r:
            midROW = (l+r)//2
            if target > matrix[midROW][-1]:
                l = midROW+1
            elif target < matrix[midROW][0]:
                r = midROW-1
            else:
                break
        
        #After finding the correct left and right pointers, calculate middle again, as l <= target <= r
        midROW = (l+r)//2    

         
        l = 0  
        r= COLS-1
        while l <= r:
            midCOL = (l+r)//2
            if matrix[midROW][midCOL] > target:
                r = midCOL-1
            elif matrix[midROW][midCOL] < target:
                l = midCOL+1
            else:
                return True
        return False
        
