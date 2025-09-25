class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.min_stk == []:
            self.min_stk.append(val)
        elif val < self.min_stk[-1]:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])

    def pop(self) -> None:
        if self.stk != []:
            self.stk.pop()
            self.min_stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
    