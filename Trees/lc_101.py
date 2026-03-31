# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # pre-check, if root is Null, return True
        if root is None:
            return True
        
        # nested function which we will use to recurse on to determine the SYMMETRY of tree
        # we will basically recurse on the left and right subtrees of the main tree
        def subtree(p, q):
            # if both left and subtree are empty or have reached empty together, then they're symmetric
            if p is None and q is None:
                return True
            # if one subtree is null while the other isn't then they aren't symmetric
            elif p is None or q is None:
                return False
            # otherwise we recurse on both subtrees
            else:
                # if the values are not equal then symmetry has failed
                if p.val != q.val:
                    return False
                # now that we are going further into the subtrees
                # we recurse and check if the left-left subtree is symmetric to the right-right subtree
                # and if the left-right subtree is symmetric to the right-left subtree
                return subtree(p.left, q.right) and subtree(p.right, q.left)
        
        # return the value of the recursive search
        return subtree(root.left, root.right)

    # Run Time: O(N)
        