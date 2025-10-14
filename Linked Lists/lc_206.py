# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    we're going to apply a 3 ptr strategy here. Where we keep track of the previous, current and next ptr/nodes. We
    will store the next node as a temporary variable, then we assign the current node's next node to the previous, then
    we update the previous to become the current node, and then the current node should become the temporary variable we used
    to store the next node of the current node in the original seqeuence. This will continue till current is Null/None
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        # create the current and previous ptrs
        curr = head
        prev = None

        # loop through the list
        while curr:
            # create the temporary variable to store the next ptr/node, then do the classic swap
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # once curr becomes Null/None then previous will be the head of the new reversed list, since the prev node is always 1 
        # node/ptr behind the curr node
        return prev
    # Run Time: O(N)
