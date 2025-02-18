#Given two strings and t, return the shortest sucbstring such that every character in t including dupes is in the substring
#In other words, we need to find the smallest window (substr) in s such that each character in t is present
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        countS = {}
        l = 0
        have = 0
        need = len(countT) 
        res = [-1,-1]

        #If every character in t is in the substring of s, that means we have matching counts for every char in t
        #Which equates length the of unique characters in t (keys in countT)
        for r in range(len(s)):
            char = s[r]

            countS[char] = countS.get(char, 0) + 1
            if char in t:
                if countS[char] == countT[char]:
                    have += 1
                    print(have)
            
           
            #While the substring includes all characters from t, shrink the substring to find the min substring
            while have == need:
                res = [l,r]
                char = s[l]
                countS[char] = countS[char] - 1
                if char in t:
                    if countS[char] < countT[char]:
                        have -= 1
                l+=1
        
        lft, rgt = res
        return s[lft:rgt+1]
            


