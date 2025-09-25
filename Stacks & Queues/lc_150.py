class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i == '+':
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = first + second
                stk.append(new_token)
            elif i == '-':
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = first - second
                stk.append(new_token)
            elif i == '*':
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = first * second
                stk.append(new_token)
            elif i == "/":
                second = int(stk.pop())
                first = int(stk.pop())
                new_token = int(first / second)
                stk.append(new_token)
            else:
                stk.append(int(i))
        
        return stk[-1]