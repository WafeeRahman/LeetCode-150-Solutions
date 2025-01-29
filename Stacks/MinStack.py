class MinStack:

    #Keep a stack to hold the minimum value at all times
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    #Add a value to the normal stack, and add the minimum between the top of the minstack
    #And the current value unless the value is the first value added to the stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)
        
    #Pop off both stacks
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    #Return the top of stack/minstack if they exist respectively
    def top(self) -> int:
        return self.stack[-1] if self.stack else []

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else []
