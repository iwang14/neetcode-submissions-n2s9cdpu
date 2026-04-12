class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
# push(1)
# push(2)
# push(5)
# push(1)
# push(0)
# pop
# top
# getMin

# Main Stack            # Min Stack
# [1]                   # [1]
# [1,2]                 # [1]
# [1,2,5]               # [1]
# [1,2,5,1]             # [1,1]
# [1,2,5,1,0]           # [1,1,0]



