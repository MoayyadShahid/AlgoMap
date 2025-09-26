class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        So my logic behind this question is as follows, we should keep adding elements (temp values) to the stack and if a newly added value
        is greater than the last added value, then we remove the last added value and update the day difference value in the 'diff' array which
        tracks the number of days difference till a HIGHER (>) temperature. Now, once we have a scenario where a number is greater than the last
        added value we will keep checking the other values that remain in the stack and see if they are less than the new value that is to be added
        to the stack. In order to be able to calculate the difference, we need both the value and index, so I will store tuples in the stack
        which follow the structure (temperature_val, index_in_array), this way we can compare the value of the temperatures and then the 
        difference in days for those specific temperature value on a given day.
        '''
        # create a stack
        stk = []
        n = len(temperatures)
        # create an array of differences
        diff = [0] * n

        # Loop through all the temperatures
        for i in range(n):
            # we make sure that a stack isnt empty, and check if the last temperature value that got 'pushed' is less than the new value
            if stk != [] and stk[-1][0] < temperatures[i]:
                # if the last temperature value is smaller, then we 'pop' that tuple out of the stack
                elem = stk.pop()
                # then we update the difference of days array by accessing the appropriate index spot in the 'diff' array for the 'popped' temperature val
                diff[elem[1]] = i - elem[1] # we calculate and update the difference
                # then we check if there are more values in the stack that are less than the incoming 'new' temperature value
                while True:
                    if stk != [] and stk[-1][0] < temperatures[i]:
                        # if there are lesser values in the stack then we remove that element and update the 'diff' array accordingly
                        elem = stk.pop()
                        diff[elem[1]] = i - elem[1]
                    else:
                        # otherwise, if there is no smaller element than the 'incoming' temperature value, then we simply exit the inner loop
                        break
                # After removing lesser values, we add the new tuple containing the new larger temperature value and its corresponding index
                stk.append((temperatures[i], i))
            else:
                stk.append((temperatures[i], i))
        
        # we return the 'diff' array as needed
        return diff
        # Run Time: O(N)
