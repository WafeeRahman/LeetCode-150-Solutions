class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        newS = ""

        for char in s:
            #Filter Out Non Alnums
            if char.isalnum():
                newS += char.lower()
        print(newS)

        #Verify Palindromes with two pointers
        
        l = 0
        r = len(newS)-1
        #L = 0
        #R = End of the word
        #Each Letter must be the same until l and r meet, otherwise
        #The word is not a palindrome
        while l <= r:
            if newS[l] != newS[r]:
                return False
            l+= 1
            r-=1    
        return True

        
