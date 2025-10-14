"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    '''
    we first create a hashmap of the old nodes to the new nodes (where the new ones just store the numeric value of the old node)
    then once we have created the hashmap, then we can loop through the old list, acess the corresponding new node, and then
    set that new node to its corresponding next node and random node by accessing the hashmap, which maps the old nodes to the
    new nodes. Once we go through the old list we will have created a new, deep copy of the old list.
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # edge case, if old list is empty return None
        if head == None:
            return None
        
        curr = head
        # create the hashmap
        old_to_new = {}
        # go through the old list
        while curr:
            # create the new node, but just set the numeric value
            node = Node(x = curr.val)
            # create the key value pair of Old_node : New_node
            old_to_new[curr] = node
            # update the current node to the next node
            curr = curr.next
        
        # reset the current node to the start of the old list
        curr = head
        # we will go through the old list to now construct a deep copy of the new list
        while curr:
            # get the new node, which is suppose to be the value of the old_node key
            new_node = old_to_new[curr]
            # we set the new node's next to the value of the current old node's next if it exist, else it's Null / None
            new_node.next = old_to_new[curr.next] if curr.next else None
            # we set the new node's random to the value of the current old node's random if it exist, else it's Null / None 
            new_node.random = old_to_new[curr.random] if curr.random else None
            # update the current old node to go to the next node in the old list
            curr = curr.next
        
        # to get the new list's first/head node, we simply just use the hashmap to access the new version of the head node,
        # by using the head of the old list as the key
        return old_to_new[head]
    # Run Time: O(N)
