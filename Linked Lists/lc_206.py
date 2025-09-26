# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next == None:
            return head

        stk = []
        curr = head
        while curr:
            stk.append(curr)
            curr = curr.next
        for i in range(len(stk) - 1, 0, -1):
            curr = stk[i]
            stk[i].next = stk[i - 1]
        if len(stk) > 1:
            stk[0].next = None
            return stk[len(stk) - 1]
        else:
            return None
        # Run Time: O(N)