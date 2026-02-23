# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # For tree problems we tend to take a recursive approach, so we need to have a base case
        # since we are calculating a numerical value, a sensible base case value is 0
        # if root is Null / None, return 0, or if we reach the leaf nodes and are accessing the leaf's children then those would be 0
        if root == None:
            return 0
        
        # since we want to calculate the maximum depth, we will recurse on both the left and right sub-trees
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # from the recursion, once we reach the bottom or end, we will basically be doing 1 + the max of either the left or right
        # this way we keep taking the larger pathway getting our maximum depth
        return 1 + max(leftDepth, rightDepth)
    
        # Run Time: O(N)
