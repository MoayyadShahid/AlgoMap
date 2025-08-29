class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # create a hashmap of the occurrences of nums called 'occ'
        occ = {}
        # go through the 'nums' list and create the num:occurrences key-value pairs
        for i in nums:
            occ[i] = occ.get(i, 0) + 1
        
        # now we just go through the hashmap keys and see which one is the max element
        maj = 0
        maj_count = 0
        for i in occ.keys():
            # we check the occurrences of the number i in in nums is greater than the max count number
            if occ[i] > maj_count:
                # update the majority element and the count of that element
                maj = i
                maj_count = occ[i]
        # return the majority element
        return maj
        # Run Time: O(N)

