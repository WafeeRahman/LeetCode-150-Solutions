#Given a string containing the phone digits 2-9, compute all possible letter combinations that each digit could represent
#With each digit, we can compute the current letter, then move onto the next letter combination for the next digit
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = { "2": "abc", 
                     "3": "def", 
                     "4": "ghi",
                     "5": "jkl",
                     "6": "mno",
                     "7": "pqrs",
                     "8": "tuv",
                     "9": "wxyz"}
        res = []
        curStr = ""
        if len(digits) == 0:
            return res
        def backtrack(i):
            nonlocal res, curStr
            if i == len(digits):
                res.append(curStr)
                return
            
            charList = digitMap[digits[i]]
            #At each step, we can choose to include the current character and move to the next digit
            #Or move into the next character of the current digit and try the combinations of the next digits and so forth
            for char in charList:
                curStr = curStr + "" + char #Include Current Character
                backtrack(i+1) #Include every character from next digit
                curStr = curStr[:len(curStr)-1] #Backtrack and remove current character to try the comb with next curr char
            return
        backtrack(0)
        return res
