# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if root is empty we can't result in any numerical value, so no such path exists
        if root is None:
            return False
        
        # we will use this nested function to recurse from the root to the leaf and track
        # the sum of the path
        def path(node, curr, target):
            # base case, if the node we have is Null then we can't form any such path
            if node is None:
                return False
            
            # update the curr sum to include the current node value
            curr += node.val

            # we check if we are at a leaf by seeing if both left and right are empty
            if node.left is None and node.right is None:
                # if at the the leaf, we check if the running sum is equal to target or not
                return curr == target
            
            # if we aren't at a leaf, then we recurse on both the left and right pathway
            return path(node.left, curr, target) or path(node.right, curr, target)

        # now we use the nested function with the root as the intiial node, 0 as the start of the sum, and add targetSum as our target
        return path(root, 0, targetSum)
    
    # Run Time: O(N)
