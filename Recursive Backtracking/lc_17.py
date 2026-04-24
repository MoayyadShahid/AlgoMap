class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # the idea here is that we will use the backtracking index i as the index of the current digit in digits
        # and for each recursion we will go through the list of possible letters that the digit maps to, and then 
        # we recurse to the next digit
        n = len(digits)
        res = []
        sol = []

        # create the map, although we can also create a list of chars sized 10, where index 2 to 9, are strings of the possible chars
        mapp = {'2' : ['a', 'b', 'c'], 
                '3' : ['d', 'e', 'f'],
                '4' : ['g', 'h', 'i'],
                '5' : ['j', 'k', 'l'],
                '6' : ['m', 'n', 'o'],
                '7' : ['p', 'q', 'r', 's'],
                '8' : ['t', 'u', 'v'],
                '9' : ['w', 'x', 'y', 'z']
                }

        def backtrack(i):
            # base case is if we reach the end of the digits list with the index tracking current digit i == n / len(digits)
            if i == n:
                # since we are creating a list of strings, then sol is a list of chars, so we need to turn it into a string
                res.append(''.join(sol))
                return
            
            # at each digit, i, of digits, we need to go through all the possible chars that digits[i] can map to
            for k in mapp[digits[i]]:
                sol.append(k)
                backtrack(i + 1)
                sol.pop()
        
        # start the backtracking with the first element digits[0]
        backtrack(0)
        # return the final array of possible strings
        return res
    
    # Run Time: O(N * 4 ^ N)
