#With a string s, return every partition of s such that every partition is a palindrome
#Well, a string s can be partitioned 1..len(s) times, where we partition it 1 character at a time, 2 characters
#..n characters at a time. 
#aba -> partitions of len 1 "a" "b" "a"
# partition of len 3 "aba"
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        currentPart = []
        
        #Use Backtracking to keep track of every partition
        def backtrack(i):
            #If we have no more values to add to current partition
            #Add the current partition and return to previous call
            if i == len(s):
                res.append(currentPart.copy())
                return
            
            #At each step, we can partition the ith value from s[i] .. s[i:len(s)]
            for j in range(i, len(s)):
                #If s[i:j] is a valid palindrome, add it to the partition, and check
                #The if the next partition is valid by calling backtracking on the next position (j+1)
                if self.isPal(i, j, s): #Helper to find palindromic strings
                    currentPart.append(s[i:j+1])
                    backtrack(j+1)
                    #After getting every partition, pop to backtrack and check the next set of partitions
                    #After the partitions of length j-i+1
                    currentPart.pop()
                
        #Backtrack to build res and return it
        backtrack(0)
        return res
        
    #Use left and right pointers to check if each partition is a valid palindrome
    def isPal (self,  l, r, s):
        while l <= r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        
