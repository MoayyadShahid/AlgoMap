# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        tmp = head
        while tmp:
            if tmp in nodes:
                return True
            else:
                nodes.add(tmp)
            tmp = tmp.next
            
        return False
        