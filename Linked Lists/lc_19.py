# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        The idea: get the size of the list, then get the position from the end by subtracting the N'th from 
        end from size, and then loop through the list to get to that N'th from end position. Then remove it by making its
        previous node/ptr point to the n'th nodes next ptr/node.
        '''
        size = 0
        curr = head
        # loop through the list and get the size of the list
        while curr:
            size += 1
            curr = curr.next
        
        # calculate the position of the node that is to be removed
        pos = size - n + 1

        i = 1
        # 2 ptr strategy, we have the curr and then prev ptr/nodes
        curr = head
        prev = None

        # we loop through the array again
        while curr:
            # if the node to be removed is the first one then we just return the next node after the head
            if pos == 1:
                return curr.next
            # if we found the node, then we change the connections of the previous node to point to the next of the curr node
            elif i == pos:
                prev.next = curr.next
                # return the head, since we need to give the update list
                return head
            # otherwise we updated the 2 ptrs, and increment the position tracker i
            else:
                prev = curr
                curr = curr.next
                i += 1
    
    # Run Time: O(N)
