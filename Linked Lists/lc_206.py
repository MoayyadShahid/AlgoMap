# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        My idea here is to store all the nodes in a stack, that way the first node is the last node be accessed and the last node becomes the first, 
        then I will go through the stack and update the next values of each 'popped' node from the stack to be the value of the next element being 'popped' from the stack
        '''
        # if the list is empty or the list is a single node, just return the list/head
        if head != None and head.next == None:
            return head

        # create the stack
        stk = []
        # set a pointer to head of the Linked List
        curr = head
        # go through the linkedin list
        while curr:
            # add each node to the stack
            stk.append(curr)
            # update the curr ptr to go to the next node
            curr = curr.next
        
        # now we go through the stack, and then modify each node's next ptr to point to the next 'popped' node in the stack
        for i in range(len(stk) - 1, 0, -1): # go until the very last node, excluding the last node
            curr = stk[i]
            stk[i].next = stk[i - 1]
        
        # at the very end, we make the final node point to Null and then return the new reversed linked list
        stk[0].next = None
        return stk[len(stk) - 1]
        # Run Time: O(N)
