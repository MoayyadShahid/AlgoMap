class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hashmap to pair up the num with its occurrences
        hmap = {}
        # loop through all the nums
        for i in nums:
            # add the num to the hashmap, and increment its occurrence
            hmap[i] = hmap.get(i,0) + 1
            # if an element already exists then its occurrences will be > 1
            # so no need to go through the entire list, just return True & terminate
            if hmap[i] > 1:
                return True
        # otherwise if we have gone through the entire list, and haven't found any such num
        # return false since we have only occurrences of = 1
        return False
        