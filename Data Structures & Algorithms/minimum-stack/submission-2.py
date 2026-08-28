class MinStack:

    # def __init__(self):
    #     self.stack = []
        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
        

    # def pop(self) -> None:
    #     self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     min_value = self.stack[0]
    #     for value in self.stack:
    #         if value < min_value:
    #             min_value = value
    #     return min_value

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


        
