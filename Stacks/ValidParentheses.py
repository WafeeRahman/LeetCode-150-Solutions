class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = { "[": "]", "(":")", "{": "}"}
        for char in s:
            #Store all open parens into a stack
            if char in "({[":
                stack.append(char)
            elif char in ")]}":
                #If there are no opens to match, invalid
                if len(stack) == 0:
                    return False
                bracketType = stack.pop()
                #If the most recent open bracket doesnt match the type
                #of the close bracket, the parentheses is invalid
                if char != bracketMap[bracketType]:
                    return False
        #There should be no more opens left in the stack after a valid iteration
        return len(stack) == 0
