class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #Start with the vehicles closest to target
        #(highest position and highest speed)
        posSpeed = [(p,s) for p, s in zip(position, speed)]
        posSpeed.sort()
        posSpeed.reverse()
        stack = []

        #Take each cars speed and position
        for speedTuple in posSpeed:

            p, s = speedTuple[0], speedTuple[1]
            #Calculate ETA and add to stack
            time = (target-p)/s
            stack.append(time)
            
            #For any two cars, if the last added car has a time <= the second last car added
            #They will be apart of the same fleet, therefore pop it out of the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            



        

        
