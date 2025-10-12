# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        mid = count // 2 if count % 2 == 0 else count // 2 + 1

        pos = 0
        curr = head
        while pos != mid:
            pos += 1
            curr = curr.next
        
        return curr
