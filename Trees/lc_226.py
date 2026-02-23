# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if we reach the leafs, or if the root is Null, then just return None
        if root == None:
            return None
    
        # simultaneously set the left side to the right, and the right side to left
        root.left, root.right = root.right, root.left

        # Recurse on the child nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return the root node
        return root
    # Run Time: O(N)
    # Space Time: O(h) <- h = height of the tree
