#with a string s, we need to find the longest substring where each character is unique
#where a substring is a contigous sequence of characters within a string
#In other words, we need to find the maximum contiguous window length where all characters in the string are unique
#We can track the current window of characters in a string, and take the maximum window length at each step, shrinking the window
#When we encounter duplicate values
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curCharSet = set() 
        longest = 1 #longest at worst case will be 1 for nonempty strings
        #Edge Case for Empty String
        if len(s) == 0:
            return 0
        
        #Sliding Windoww
        l = 0
        for r in range(len(s)):
            #If the charSet contains a duplicate within the current window
            #Shrink window until values are strictly unique again
            while s[r] in curCharSet:
                curCharSet.remove(s[l])
                l+= 1
                
            #Add unique characters to current set and take max window length
            curCharSet.add(s[r])
            windowLen = (r-l)+1
            longest = max(windowLen, longest)
        return longest

         
