class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store the element:index key-value pairs
        sMap = {}
        # loop through the nums list and add the elements to the hashmap, and update their index if 
        # an element re-occurs later on in the list
        for i in range(len(nums)):
            sMap[nums[i]] = i
        
        # loop through the nums list again and this time we will see if the complement integer exists in the hashmap
        for i in range(len(nums)):
            # define the complement integer as 'need' for the current integer nums[i]
            need = target - nums[i]
            # we see if 'need' is inside the hashmap, and also that it is at a different index than i
            # if so, then we have found our pair
            if need in sMap and sMap[need] != i:
                return [i, sMap[need]]
        # Run Time: O(N)
        