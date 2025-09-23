class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        The idea here is we go through the 'operations' list and we add numbers sequentially to a stack. Depending on 
        the relevant operation, we will either 'pop' off elements from the stack and temporarily store them to use them to
        get another value to add back onto the stack alongside the original numbers on the stack in the order they previously
        were on the stack, OR we will simply remove the element from the stack. Else, if we just get a number from the 
        'operations' list we will just add it to the stack.
        '''
        # create the stack
        stk = []
        # loop through all the operations
        for i in operations: # O(N)
            if i == '+': # if operation is to sum, remove last 2 nums on stk and add them, then 'push' all 3 numbers in order back on stack
                second = int(stk.pop()) 
                first = int(stk.pop()) # first is here beacause the '1st' element is accessed later due to LIFO structure of stack
                score = first + second
                # 'push' back elements onto the stack 'stk'
                stk.append(first)
                stk.append(second)
                stk.append(score)
            elif i == 'D': # if operation is to double, then remove last added element, 2x it, then push both back to 'stk'
                num = int(stk.pop()) # pop off last added element
                double = 2 * num # double the num
                # add the last added nums back in order to the stack 'stk'
                stk.append(num) 
                stk.append(double)
            elif i == 'C': # otherwise the operation is to get rid of the last added number on the stack 'stk'
                stk.pop() 
            else: # Else, we just have a number so push that on the stack 'stk'
                stk.append(int(i))

        # once we are done, then we just sum up the elements in the stack 'stk', which equivalent was called 'the record' from the question
        final_sum = sum(stk) # O(M), where M is the size of stk

        return final_sum
        # Run Time: O(N)
