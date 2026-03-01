# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we keep a list to track the 'global' boolean balanced
        balanced = [True] # instead of doing it this way, we can also have a variable boolean, but must have 'nonlocal balanced'
                          # set into the nested function at the top

        # nested function to determine the height of a tree
        def height(root):
            # base case, since we are calculating height then we need to have numerical 0 as dead end
            if root is None:
                return 0
            
            # to calculate height we need recursive step into the left subtree
            left_height = height(root.left)
            # in the scenario that the tree is not balanced in the left subtree then we can add an optimization to return 0
            # or False before actually going further into the right subtree
            if balanced[0] == False:
                return 0
            # also to calculate height we need recurisve step into the right subtree
            right_height = height(root.right)

            # after going into both right and left subtree and getting their heights we compare if the absolute distance
            # in height is greater than 1, if so then we have an imbalance
            if abs(left_height - right_height) > 1:
                # update the global boolean to False saying we have an imbalance
                balanced[0] = False
                # return 0 early to exit out of the nested function
                return 0
            
            # else if we haven't determined an issue / imbalance then we continue calculating height
            return 1 + max(left_height, right_height)
        
        # apply the nested function on the root node of the tree
        height(root)
        # after running the nested function on the tree we will have an updated balanced global variable so return its value
        return balanced[0]
    # Run Time: O(N)
