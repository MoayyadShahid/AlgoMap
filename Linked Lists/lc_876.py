# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Idea is straightforward here, we just get the size of the linked list first by looping through once and then
        we loop through till the mid-point by calculating the middle node position from the total size.
        '''
        size = 0
        curr = head
        # loop through the list and get the size of the list
        while curr:
            size += 1
            curr = curr.next
        
        # calculate the middle node position, if odd size then middle element, if even then 2nd middle element
        mid = size // 2 if size % 2 == 0 else size // 2 + 1
        pos = 0

        # reset the curr node/ptr to point to the head node of the list
        curr = head
        # loop through the list again until we reach the middle node
        while pos != mid:
            pos += 1
            curr = curr.next
        
        # return the middle node
        return curr
        # O(N) Solution
