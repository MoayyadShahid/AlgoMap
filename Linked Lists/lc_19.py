# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        pos = count - n + 1

        i = 1
        curr = head
        prev = None
        while curr:
            if pos == 1:
                return curr.next
            elif i == pos:
                prev.next = curr.next
                return head
            else:
                prev = curr
                curr = curr.next
                i += 1
