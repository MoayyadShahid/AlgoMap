import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if we only have 1 stone, then just return the singular stone
        if len(stones) == 1:
            return stones[0]

        # to create a max heap we need to negate the values as a 'trick' as heapq stores min-heaps
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        # apply heapify upon the stones array to create the max-heap with negated values
        heapq.heapify(stones)

        # we can have at max 1 stone in the heap so we loop till the heap has length at max 1
        while(len(stones) > 1):
            # pop off the 2 largest values from the heap
            big1 = -heapq.heappop(stones)
            big2 = -heapq.heappop(stones)

            # in the case that the largest is greater than 2nd largest then we push the
            # difference back into the heap
            if big1 > big2:
                heapq.heappush(stones, -(big1 - big2))
        
        # after we are the 'smashing' sequence, then we check if the length is 1 or 0
        # we return either the remaining singular value or 0
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
    
    # Run Time: O(N)
