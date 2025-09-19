class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        The idea behind this problem is a 2 ptr solution, where we compare the 2 ptr
        formed sum and compare it with the target. If we are under we move the left ptr
        which comes from the left end, and if we are over the target we move the right
        ptr from the right end. So the goal is by doing this we will coverge to the target value.
        '''
        # set up 2 ptrs (left and right)
        left = 0
        right = len(numbers) - 1
        # loop until ptrs are about to crossover
        while left < right:
            val = numbers[left] + numbers[right] # have the current sum that is formed
            if val < target: # if sum is under than target, increment left ptr
                left += 1
            elif val > target: # if sum is over than target, decrement right ptr
                right -= 1
            else: # otherwise we got the target
                return [left, right]
        # Run Time: O(N)
