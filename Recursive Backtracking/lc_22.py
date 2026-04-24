class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        # idea here is we basically track open vs close parantheses, if open < than mid point, we keep adding open PARENS
        # likewise if at any time we have close is less than open PARENS we explore close PARENS
        def backtrack(open, close):
            # if we reached the base case of total parens then we just add that combo
            if open + close == 2 * n:
                res.append("".join(sol))
                return
            
            # if open parens is less than mid point, then we can keep adding open parens
            if open < n:
                sol.append("(")
                backtrack(open + 1, close)
                sol.pop()
            
            # likewise if we have more open parens than close parens, then we should add close parens
            if close < open:
                sol.append(")")
                backtrack(open, close + 1)
                sol.pop()
        
        # initialize backtrack
        backtrack(0, 0)
        # return solution
        return res
        
