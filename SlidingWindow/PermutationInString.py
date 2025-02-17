#With two strings s1 and s2, we need to find out if s2 contains a permutation of s1
#If a substring of s2 matches contains each character of s1, then that means there is a permutation of
#S1 in s2

#This means that for some window in s2, each character count of s2 matches s1 for each letter in the alphabet
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #for some window of length s1, we have 26 matches, the amount of characters for each letter in the alphabet in s2 matches s1
        #
        countS1 = [0] * 26
        countS2 = [0] * 26
        matches = 0
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1
        #Maintain a window of len(s1), as a permutation will have
        #26 matches for the count of each letter in the alphabet within the window if the perm exists
        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            #Increment the count of the current value
            countS2[ord(s2[r]) - ord('a')] += 1
            #If the count of the character now matches s1
            if countS2[ord(s2[r]) - ord('a')] == countS1[ord(s2[r]) - ord('a')]:
                matches += 1
            #Or if did match s1 and now it is 1 greater, decrement matches
            elif countS2[ord(s2[r]) - ord('a')] == countS1[ord(s2[r]) - ord('a')]+1:
                matches -= 1
            
            print(l, r)
            #Shrink Window
            countS2[ord(s2[l]) - ord('a')] -= 1
            #If we decremented the count and now we have a match, increment matches
            if countS2[ord(s2[l]) - ord('a')] == countS1[ord(s2[l]) - ord('a')]:
                matches += 1
            #If we previously had a match and now are 1 less then the count of s1, decrement matches
            elif countS2[ord(s2[l]) - ord('a')] == countS1[ord(s2[l]) - ord('a')]-1:
                matches -= 1
            l+=1 #Continue in window lengths of s1
        return matches == 26




        
