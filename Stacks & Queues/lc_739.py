class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a stack
        stk = []
        n = len(temperatures)
        # create an array of differences
        diff = [0] * n

        for i in range(n):
            if stk != [] and stk[-1][0] < temperatures[i]:
                elem = stk.pop()
                diff[elem[1]] = i - elem[1]
                while True:
                    if stk != [] and stk[-1][0] < temperatures[i]:
                        elem = stk.pop()
                        diff[elem[1]] = i - elem[1]
                    else:
                        break
                stk.append((temperatures[i], i))
            else:
                stk.append((temperatures[i], i))
        
        return diff

