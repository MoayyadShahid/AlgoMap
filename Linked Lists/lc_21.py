# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        The main idea behind this problem is the 'zipper principle' where we go through both lists simultaneously
        until one or both of the lists gets exhausted, at which point we will append the remainder of the list that isn't empty
        or if both are empty then we just append Null/None. 
        '''

        # we create a temp node, which is suppose to serve as a head of the merged list
        temp = ListNode(0)
        # this will be our ptr which will traverse through the merged list
        curr = temp
        
        # we will run a loop [ O(N) ] until either or both lists have been exhausted
        while list1 and list2:
            # we check which of the lists has a smaller value
            if list1.val <= list2.val:
                # we updated the next ptr of the merged list
                curr.next = list1
                # we updated the list1 ptr to go to the next node
                list1 = list1.next
            # otherwise list2 is bigger so just do everything in the 1st conditional in this statement
            else:
                curr.next = list2
                list2 = list2.next
            # we updated the curr ptr of the merged list to go to the next node, which is the node we just appended
            curr = curr.next
        
        # once we are done, we simply just add the remainder of the list which still exists, or it would we just add None/Null ptr
        curr.next = list1 or list2

        # we return temp.next, since temp points to a random node we created, but temp.next points to the start of the actual merged list
        return temp.next
        # Run Time: O(N)
