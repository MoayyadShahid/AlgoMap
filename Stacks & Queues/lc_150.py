class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        The focus behind this question is using stacks. We are basically evaluating a postfix notation expression
        in an array. The idea is as follows: we keep inputting numbers into a stack and once we 
        reach a operation (+, -, *, /) then we 'pop' the last 2 numbers in the stack and use the operator to do the operation and then
        'push' that calculated value back onto the stack. Eventually, we will be left with 1 number which will be the evaluation
        of the RPN.
        '''
        # create the stack
        stk = []
        # go through all the tokens
        for i in tokens:
            # check if the token is either one of the operation (+, -, *, /)
            if i == '+':
                # when we remove elements from the stack for expression evaluation, the 2nd number will be 'popped' first and then the
                # 1st number will be 'popped' from the stack
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = first + second
                # once we're done the operation, the 2 numbers would have been removed and we then 'push' the evaluated number to the stack
                stk.append(new_token)
            elif i == '-':
                # same thing as the '+' case
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = first - second
                stk.append(new_token)
            elif i == '*':
                # same thing as the '+' case
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = first * second
                stk.append(new_token)
            elif i == "/":
                # same thing as the '+' case
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = int(first / second)
                stk.append(new_token)
            else:
                # in this scenario, the token 'i' isn't an operator, so it must be a number, that's why we just add it to the stack
                stk.append(int(i))
        
        # the final element, and only element in the stack will be the result of the RPN evaluation process
        return stk[-1]
        # Run Time: O(N)
