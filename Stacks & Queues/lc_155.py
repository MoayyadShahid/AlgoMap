class MinStack:
    '''
    In order to achieve O(1) Run Time on all operations we will utilize a 2 stack technique. Where 1 stack is the actual stack storing the values
    and the other stack is a stack that is running parallel to the actual stack but it contains the min value so far.
    '''

    def __init__(self):
        # we define the stacks, one to track the actual values and the other to track the minimum value seen so far
        self.stk = []
        self.min_stk = []
        # the idea here is basically if we had an initial stack of [-3, 0, 2] then the corresponding min_stack would be [-3, -3, -3]
        # and then by adding -4 we would get stacks [-3, 0, 2, -4] and min_stack [-3, -3, -3, -4]
        # so then if we added 8 we would get stacks [-3, 0, 2, -4, 8] and min_stack [-3, -3, -3, -4, -4]

    def push(self, val: int) -> None:
        # when pushing a value we simply add it to the actual stack, and then we see how that value fits into the min_stack
        self.stk.append(val)
        # if the min_stack is empty then we add the value
        if self.min_stk == []:
            self.min_stk.append(val)
        # otherwise if the new value is less than the last added minimum we added the val to the stack
        elif val < self.min_stk[-1]:
            self.min_stk.append(val)
        else:
            # otherwise if the value is larger than the last added minimum value, we just re-add the last added minimum value
            self.min_stk.append(self.min_stk[-1])

    def pop(self) -> None:
        # 'pop' is striaghtforward, we just checkif the stack is empty, if not then we just remove the last added element of the regular stack and min_stack
        if self.stk != []:
            self.stk.pop()
            self.min_stk.pop()
        
    # 'top' is simple, just access the last element and return it
    def top(self) -> int:
        return self.stk[-1]

    # This is simple, just see the last added minimum value.
    def getMin(self) -> int:
        return self.min_stk[-1]
    
    # Run Time: O(1)
