# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # we basically want to track the prev number and minimum so far
        prev = None
        minim = float('inf')

        # the idea here is an in order traversal where we will basically calculate the 
        # current minimum and compare it with the absolute minimum we've seen so far
        # for this nested method instead of using a list object to track the variable
        # we will use the nonlocal keyword
        def traverse(root):
            # declare nonlocal for the outer scope variable
            nonlocal prev
            nonlocal minim

            # base case, if root is Null, return Null
            if root is None:
                return None
            # otherwise we will do in-order traversal
            else:
                # traverse left
                traverse(root.left)
                # if we have an actual previous node, and we have a lower distance/difference between node values
                # we will update the minimum distance
                if prev is not None and abs(root.val - prev) < minim:
                    # update minimum distance
                    minim = abs(root.val - prev)
                # update the previous node to be the current node
                prev = root.val
                # traverse right
                traverse(root.right)
        
        # we will use the nested method on the actual tree
        traverse(root)
        # return the updated minimum value
        return minim
    
    # Run Time: O(N)
