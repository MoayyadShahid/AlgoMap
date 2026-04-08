import heapq as hp

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we will have a dictionary to store the 'element:frequency' pair
        freq = {}
        # we will have a heap we will use to store the tuples (-frequency, element)
        # we use -frequency to invert the default min-heap into a max-heap
        heap = []

        # create element:frequency pairs
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        # create the list of tuples
        for i in freq.keys():
            heap.append((-freq[i], i))
        
        # heapify the list of tuples
        hp.heapify(heap)
        # we will use this list to store the final elements of the top K frequent elements
        lst = []

        # loop until k, and pop off top K frequent elements
        for i in range(k):
            val = hp.heappop(heap)
            # the 2nd value in the tuple is the element
            lst.append(val[1])
    
        # return the list of the top K frequent elements
        return lst
    # Run Time: O(N)
