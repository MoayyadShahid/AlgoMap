class Solution:
    def romanToInt(self, s: str) -> int:
        numMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        prevSmall = False
        prevNum = 1000

        for i in s:
            if prevNum < numMap[i]:
                num += numMap[i] - prevNum - prevNum
            else:
                num += numMap[i]
            prevNum = numMap[i]

        return num
