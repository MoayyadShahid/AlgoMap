# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        So we create a set to track all of the nodes we have encountered in a list, and since each node is a ptr, which
        essentially is a memory address, then all these nodes must be unique since the memory addresses are unique. In that
        case if we attemp to add a node/ptr that already exists in the set, then we have a cycle.
        '''
        # create the set
        nodes = set()
        # create a ptr to go through the list
        curr = head
        # loop through the list
        while curr:
            # if the curr ptr/node is in the set then we have a cycle, return True
            if curr in nodes:
                return True
            # otherwise the curr ptr/node is a new node, we will add it to the set, and update curr to go to the next node
            else:
                nodes.add(curr)
            curr = curr.next
            
        # since we reached the end of the list, that means there's no cycle
        return False
        # Run Time: O(N)
