class Solution:
    def isValid(self, s: str) -> bool:
        '''
        The idea here is pretty simple. We'll keep adding the open braces, and then if we get a close brace, we need to ensure
        it matches with the last added open brace so they can 'cancel' off each other. We'll use a stack to track the open
        braces added, and then we will see if a closed brace gets added then does it match the type of last added open brace in
        the stack 'stk'. If it does, then we just 'pop' off the open brace, else we return False. In the end, the stack 'stk' 
        should be empty to yield True, otherwise we didn't get rid off all braces, meaning its False.
        '''
        # create the stack to track open braces
        stk = []
        # creating these variables below will enable us to get O(1) lookup
        pair = {')':'(', '}':'{', ']':'['} # create a hashmap to pair the relevant closed brace with open brace
        first = {'(', '{', '['} # create a set to see the valid open braces

        # loop through the string s
        for i in s:
            if i in first: # we check if the current brace is an open brace, if so add it to the stack
                stk.append(i)
            elif stk == [] or stk[-1] != pair[i]: # otherwise, we check if our fail condition, if the stack is empty or if the pairs don't match up
                return False
            else: # otherwise we have it that the pairs match up, so remove the last added open brace
                stk.pop()
        
        # in the end we check if the stack 'stk' of the open braces is empty, if so, all went well, return True
        if stk == []:
            return True
        # otherwise something went wrong, return False for an invalid strinh
        else:
            return False
        # Run Time: O(N)
