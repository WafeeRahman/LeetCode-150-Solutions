#With a string s consisting of only uppercase characters and an integer k, we have up to k characters we can replace
#With any other character, we can make at most k replacements

#Return the length of the longest substring, or window that we can after we make k replacements there is only one 
#distinct repeated character in the substring

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countS = {}

        l = 0
        longest = 0
        for r in range(len(s)):
            #Count the amount of characters within the current window
            countS[s[r]] = countS.get(s[r], 0) + 1
            windowLen = (r-l)+1
            
            #Returns to us the character that has appeared most frequently within window
            mostFrequentChar = max(countS, key=lambda x: countS[x]) 
            print(mostFrequentChar)
            #If we can make up to k replacements within the current window
            #Where we can replace the most frequent character up to k times to make a substring of one distinct character
            if windowLen - countS[mostFrequentChar] <= k:
                longest = max(windowLen, longest)
          
            #If we cant make k replacements within the current window, shrink window
            print(l,r, countS[mostFrequentChar], windowLen)
            
            while windowLen - countS[mostFrequentChar] > k:
                countS[s[l]] -= 1
                l+=1
                mostFrequentChar = max(countS, key=lambda x: countS[x]) 
                windowLen = (r-l)+1
                
            
            
            
        return longest


        
