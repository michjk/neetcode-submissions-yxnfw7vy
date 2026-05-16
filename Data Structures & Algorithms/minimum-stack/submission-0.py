import heapq

class MinStack:

    def __init__(self):
        self.min_num = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_num:
            if self.min_num[-1] > val:
                self.min_num.append(val)
            else:
                self.min_num.append(self.min_num[-1])
        else:
            self.min_num.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]
        
