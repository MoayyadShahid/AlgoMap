class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        score = 0
        for i in operations:
            if i == '+':
                first = int(stk.pop())
                second = int(stk.pop())
                score = first + second
                stk.append(second)
                stk.append(first)
                stk.append(score)
            elif i == 'D':
                num = int(stk.pop())
                double = 2 * num
                stk.append(num)
                stk.append(double)
            elif i == 'C':
                stk.pop()
            else:
                stk.append(int(i))
        final_sum = sum(stk)
        return final_sum
            
            
        