# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    What we do is simple here, we loop through the nodes and what we do is check if the current node has a next value, if so then we check if the curr value
    is equal to the next value, if so, we link the curr node's next ptr to the node of the next ptr's next ptr. Otherwise we move onto the next node.

    [a] -> [a] -> [b] -> [c]  
    we have [a], we check that the next node of [a] is also [a] so we make the next node of the 1st [a] equal to the node [b] which is the next node of the 2nd [a]
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr node which will be used to go through the list and be modified
        curr = head
        while curr: # go through the list while the curr node isn't Null
            # we check the condition that the next node's value isn't the same as the curr node's value,  if so then we have to change the node of the curr node's next ptr
            if curr.next != None and curr.next.val == curr.val:
                # update curr's next to be the curr node's next node's next ptr
                curr.next = curr.next.next
            else:
                # otherwise we don't have a duplicate, so we just update the curr to be the next node
                curr = curr.next
        # return the modified, de-duplicated list
        return head
        # Run Time: O(N)
