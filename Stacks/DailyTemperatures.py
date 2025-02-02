class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        #Maintain a stack of encountered temperatures
        for i in range(len(temperatures)):
            #If the most recent temperature is greater than the 
            #Last added temperature in the stack
            while stack and stack[-1][0] < temperatures[i]:
                #Change the ith position in res to the amount of days
                #That passed where there was no greater temperature
                res[stack[-1][1]] = (i-stack[-1][1])
                #Check the next value in stack after popping
                stack.pop()
            stack.append([temperatures[i], i])
        return res
        
