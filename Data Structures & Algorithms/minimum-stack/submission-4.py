class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack = self.stack + [val]
        if (not self.mini):  
            self.mini.append(val)
        elif (val <= self.mini[len(self.mini)-1]):
            self.mini.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0 and len(self.mini):
            temp = self.stack[len(self.stack)-1]
            del self.stack[len(self.stack)-1]
            if temp == self.mini[len(self.mini)-1]:
                del self.mini[len(self.mini)-1]
            return temp

    def top(self) -> int:
        return self.stack[len(self.stack)-1]        

    def getMin(self) -> int:
        foo = float("-inf")
        if len(self.mini) > 0:
            return self.mini[len(self.mini)-1]
        return 0
        
