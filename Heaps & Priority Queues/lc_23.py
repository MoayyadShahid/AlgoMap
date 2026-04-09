import heapq as hp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # this will be the list that stores the values of all the linked lists
        heap = []

        # we will go through each linked lists stored in the 'lists' list and store them as one continously array in 'heap'
        for i in range(len(lists)):
            # get current linked list
            curr = lists[i]
            # loop through the current linked list and add its value to the 'heap'
            while curr:
                heap.append(curr.val)
                curr = curr.next
            
        # turn 'heap' into an actual min-heap using heapify
        hp.heapify(heap)

        # now we need to create the consolidate MEGA linked list
        # create the head
        head = ListNode()
        # create the pointer to the head we will iterate with
        curr = head

        # loop through the length of the heap
        for i in range(len(heap)):
            # pop off the minimum value so far in the heap
            val = hp.heappop(heap)
            # set the next of the current to the a new linked list node with the latest smallest value
            curr.next = ListNode(val)
            # update curr ptr of linked list to point to the newest ListNode we just created
            curr = curr.next
        
        # at the very end we want the start of this new linked list, so we just return the next of the head ptr we created
        return head.next
    # Run Time: O(M * N), where M is the size of the largest linked list which is capped at 500 so in essence run time is just O(N)
